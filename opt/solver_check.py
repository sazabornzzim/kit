"""사용 가능한 최적화 솔버 확인. 실행: python opt/solver_check.py"""
checks = {
    "OR-Tools CP-SAT": "from ortools.sat.python import cp_model",
    "scipy milp (HiGHS)": "from scipy.optimize import milp",
    "PuLP": "import pulp; print('  PuLP', pulp.__version__, '(4.x면 API 변경 주의)')",
    "Gurobi": "import gurobipy; gurobipy.Model()",
}
for name, code in checks.items():
    try:
        exec(code)
        print(f"[OK]   {name}")
    except Exception as e:
        print(f"[FAIL] {name}: {type(e).__name__}")
