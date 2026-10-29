# hynix-kit

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
```
git clone https://github.com/<아이디>/hynix-kit
cp hynix-kit/AGENTS.md .
cp hynix-kit/templates/PLAN.md PLAN.md
cp hynix-kit/templates/REPORT.md REPORT.md
```
