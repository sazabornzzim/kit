"""범용 CP-SAT 템플릿: 수요 그룹을 용량 있는 자원 슬롯에 배정 + 동시 가용 자원 제한.
예시 데이터는 동작 확인용 가짜 값. 실제 과제에서는 load_config()만 바꿔 쓴다.
실행: python opt/cpsat_template.py
"""
import math, time
from ortools.sat.python import cp_model


def load_config():
    # 파라미터는 여기만 수정 (조건 변경 시 재실행만 하면 됨)
    return {
        "groups": {"G1": {"demand": 130, "due": 48}, "G2": {"demand": 60, "due": 54}},
        "slots": list(range(36, 55)),  # 시간 슬롯 (예: 10분 단위)
        "cap": 45,          # 슬롯 1회당 용량
        "lead": 3,          # 슬롯 시작 → 도착까지 걸리는 슬롯 수
        "window": 4,        # due보다 최대 몇 슬롯 일찍 도착 허용
        "busy": 7,          # 자원 1개가 한 번 쓰이면 점유되는 슬롯 수
        "max_res": 3,       # 동시에 쓸 수 있는 자원 수
        "time_limit": 30,
    }


def baseline(c):
    return sum(math.ceil(g["demand"] / c["cap"]) for g in c["groups"].values())


def solve(c):
    G, S = c["groups"], c["slots"]
    feas = [(g, s) for g in G for s in S
            if G[g]["due"] - c["window"] <= s + c["lead"] <= G[g]["due"]]
    m = cp_model.CpModel()
    x = {s: m.NewBoolVar(f"x_{s}") for s in S}
    y = {k: m.NewIntVar(0, c["cap"], f"y_{k[0]}_{k[1]}") for k in feas}
    for g in G:  # C1 수요 전부 충족
        m.Add(sum(y[k] for k in feas if k[0] == g) == G[g]["demand"])
    for s in S:  # C2 용량
        m.Add(sum(y[k] for k in feas if k[1] == s) <= c["cap"] * x[s])
    for t in S:  # C3 동시 가용 자원
        m.Add(sum(x[s] for s in S if t - c["busy"] < s <= t) <= c["max_res"])
    m.Minimize(sum(x.values()))
    sv = cp_model.CpSolver()
    sv.parameters.max_time_in_seconds = c["time_limit"]
    t0 = time.time()
    st = sv.Solve(m)
    ok = st in (cp_model.OPTIMAL, cp_model.FEASIBLE)
    return {"status": sv.StatusName(st),
            "objective": int(sv.ObjectiveValue()) if ok else None,
            "bound": sv.BestObjectiveBound() if ok else None,
            "used_slots": [s for s in S if ok and sv.Value(x[s])],
            "sec": round(time.time() - t0, 2)}


if __name__ == "__main__":
    c = load_config()
    print("baseline:", baseline(c))
    print("optimize:", solve(c))
    c["max_res"] = 2  # 조건 변경 예시
    print("max_res=2:", solve(c))
