# kit

AI 코딩 에이전트와 과제를 수행할 때 쓰는 범용 작업 키트입니다.
특정 과제의 정답이나 결과물은 포함하지 않습니다.

## 구성
| 파일 | 용도 |
|---|---|
| `AGENTS.md` | 에이전트 작업 규칙 (작업 폴더 최상위에 두면 자동으로 읽힘) |
| `templates/PLAN.md` | 계획 문서 양식 |
| `templates/REPORT.md` | 결과 보고 양식 |
| `CHECKLIST.md` | 진행 순서와 실수 방지 목록 |
| `PROMPTS.md` | 단계별 프롬프트 모음 |

## 사용법
Codex에 아래 문장을 붙여넣는다.
```
https://github.com/sazabornzzim/kit 을 clone해줘. 그 안의 AGENTS.md와 templates의 PLAN.md, REPORT.md를 작업 폴더 최상위에 복사하고(이미 있으면 덮어쓰지 마), kit/ 폴더와 .bashrc, .profile, .config 같은 환경 파일은 .gitignore에 추가해서 커밋에 안 들어가게 해줘. 앞으로 AGENTS.md 지침대로 작업하고, 지금은 규칙을 3줄로 요약해줘.
```
이후 진행 순서는 `CHECKLIST.md` 참고.
