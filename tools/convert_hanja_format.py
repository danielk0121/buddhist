#!/usr/bin/env python3
"""
수필 문서의 '원문 전체 보기' 섹션에서
인라인 한자 풀이 형식을 한 줄 한 글자 형식으로 변환한다.

변환 전: 如(같을 여) 是(이 시) 我(나 아)
변환 후:
  如 여 (같을)
  是 시 (이)
  我 아 (나)

사용법:
  python3 tools/convert_hanja_format.py                  # src/essay/ 전체 처리
  python3 tools/convert_hanja_format.py <파일1> <파일2>  # 지정 파일만 처리
"""

import re
import sys
from pathlib import Path

ESSAY_DIR = Path(__file__).parent.parent / "src" / "essay"
SECTION_MARKER = "## 원문 전체 보기"
INLINE_PATTERN = re.compile(r"([一-龯])\(([가-힣]+) ([가-힣]+)\)")


def convert_line(line: str) -> str:
    tokens = INLINE_PATTERN.findall(line)
    if not tokens:
        return line
    return "\n".join(f"{hanja} {reading} ({meaning})" for hanja, meaning, reading in tokens)


def convert_section(section: str) -> str:
    return "\n".join(convert_line(line) for line in section.split("\n"))


def process_file(path: Path) -> bool:
    content = path.read_text()
    idx = content.find(SECTION_MARKER)
    if idx == -1:
        return False

    before = content[:idx]
    section = content[idx:]
    converted = convert_section(section)

    if converted == section:
        return False

    path.write_text(before + converted)
    return True


def main():
    if len(sys.argv) > 1:
        targets = [Path(p) for p in sys.argv[1:]]
    else:
        targets = sorted(ESSAY_DIR.glob("*.md"))

    changed = 0
    for path in targets:
        if process_file(path):
            print(f"변환 완료: {path.name}")
            changed += 1
        else:
            print(f"변경 없음: {path.name}")

    print(f"\n총 {changed}개 파일 변환됨.")


if __name__ == "__main__":
    main()
