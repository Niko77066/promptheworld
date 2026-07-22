#!/usr/bin/env python3
"""Heuristic linter for prompts intended for Fable 5.

This catches high-cost mistakes. It does not grade prompt quality or replace review.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


SECRET_PATTERNS = [
    ("openai_like_key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("bearer_token", re.compile(r"\bBearer\s+[A-Za-z0-9._~+/=-]{20,}\b", re.I)),
    ("private_key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
]

RAW_COT = re.compile(
    r"(?:show|reveal|print|transcribe|expose).{0,40}(?:chain[- ]of[- ]thought|hidden reasoning|internal reasoning)"
    r"|(?:展示|输出|透露|复述).{0,20}(?:思维链|隐藏推理|内部推理)",
    re.I | re.S,
)

VAGUE_PHRASES = [
    "do your best",
    "be brilliant",
    "make it good",
    "尽你所能",
    "做到最好",
    "帮我弄好",
]


def lint(text: str) -> list[dict[str, str]]:
    warnings: list[dict[str, str]] = []
    for name, pattern in SECRET_PATTERNS:
        if pattern.search(text):
            warnings.append({"severity": "critical", "code": name, "message": "Possible credential embedded in prompt."})
    if RAW_COT.search(text):
        warnings.append({"severity": "critical", "code": "raw_chain_of_thought", "message": "Request decisions and evidence, not hidden reasoning."})
    lowered = text.lower()
    for phrase in VAGUE_PHRASES:
        if phrase in lowered:
            warnings.append({"severity": "warning", "code": "vague_instruction", "message": f"Replace vague instruction: {phrase}"})

    headings = re.findall(r"(?m)^\s*(?:#{1,6}\s+|<)([A-Za-z0-9_\-\u4e00-\u9fff ]+)", text)
    normalized = [re.sub(r"\s+", " ", h.strip().lower()) for h in headings]
    duplicates = sorted({h for h in normalized if normalized.count(h) > 1 and len(h) > 2})
    if duplicates:
        warnings.append({"severity": "warning", "code": "duplicate_sections", "message": "Repeated section labels: " + ", ".join(duplicates[:8])})

    if len(text) > 8000 and not re.search(r"(?:deliverable|交付|output|输出)", text, re.I):
        warnings.append({"severity": "warning", "code": "missing_deliverable", "message": "Long prompt has no obvious deliverable contract."})
    if len(text) > 8000 and not re.search(r"(?:verification|verify|验收|验证|自查|test)", text, re.I):
        warnings.append({"severity": "warning", "code": "missing_verification", "message": "Long prompt has no obvious verification contract."})
    if len(text) > 12000:
        warnings.append({"severity": "info", "code": "long_prompt", "message": "Review whether detailed knowledge belongs in files or references instead of the task prompt."})
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", help="Prompt file. Reads stdin when omitted.")
    args = parser.parse_args()
    text = Path(args.file).read_text(encoding="utf-8") if args.file else sys.stdin.read()
    warnings = lint(text)
    print(json.dumps({"ok": not any(w["severity"] == "critical" for w in warnings), "warnings": warnings}, ensure_ascii=False, indent=2))
    return 1 if any(w["severity"] == "critical" for w in warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
