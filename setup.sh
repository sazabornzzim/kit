#!/bin/bash
# 사용법: 작업 폴더에서 bash kit/setup.sh

KIT="$(cd "$(dirname "$0")" && pwd)"
cd "$KIT/.."

copy() {
  if [ -e "$2" ]; then
    echo "⚠️  $2 이미 있음 → 덮어쓰지 않음 (직접 확인 필요)"
  else
    cp "$1" "$2" && echo "✅ $2 생성"
  fi
}

copy "$KIT/AGENTS.md"           AGENTS.md
copy "$KIT/templates/PLAN.md"   PLAN.md
copy "$KIT/templates/REPORT.md" REPORT.md
[ -e progress.md ] || { echo "# progress" > progress.md && echo "✅ progress.md 생성"; }

# 키트 폴더는 제출물 커밋에 섞이지 않게 제외
grep -qx "kit/" .gitignore 2>/dev/null || echo "kit/" >> .gitignore

echo "완료. CHECKLIST.md, PROMPTS.md는 kit 폴더에서 열어보세요."
