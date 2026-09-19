#!/usr/bin/env python3
"""Fail if v2 manuscript math uses a constant that is not declared in v2/ledger.md.

Usage: python3 tests/check_ledger.py [--list]

Rules enforced:
  * every symbol row in the ledger's Parameters table counts toward the budget
    declared on the "**Budget: N parameters" line;
  * every symbol-like token found inside $...$ or $$...$$ in v2/*.md (excluding the
    design/audit documents listed in SKIP) must be a ledger symbol, an allowlisted
    field/coordinate/operator, or a LaTeX control word.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V2 = ROOT / "v2"
LEDGER = V2 / "ledger.md"
ALLOWLIST = ROOT / "tests" / "ledger_allowlist.txt"
SKIP = {"ledger.md", "ledger_v1_audit.md", "01_action_skeleton.md", "README.md", "v1_chapter_audit.md"}

MATH_RE = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)
# a "symbol" is a Greek/named macro or a single Latin letter, with an optional subscript
TOKEN_RE = re.compile(r"(\\[A-Za-z]+|[A-Za-z])(?:_(\{[^{}]*\}|[A-Za-z0-9]))?")
LATEX_CONTROL = {
    r"\frac", r"\sqrt", r"\int", r"\sum", r"\partial", r"\nabla", r"\left", r"\right",
    r"\cdot", r"\times", r"\approx", r"\sim", r"\lesssim", r"\gtrsim", r"\ll", r"\gg",
    r"\leq", r"\geq", r"\neq", r"\to", r"\rightarrow", r"\propto", r"\infty", r"\pm",
    r"\text", r"\mathrm", r"\mathcal", r"\mathbf", r"\ln", r"\log", r"\exp", r"\dot",
    r"\ddot", r"\hat", r"\bar", r"\tilde", r"\vec", r"\quad", r"\qquad", r"\,", r"\;",
    r"\!", r"\dots", r"\cdots", r"\ldots", r"\equiv", r"\det", r"\operatorname",
    r"\Big", r"\big", r"\Bigl", r"\Bigr", r"\displaystyle", r"\boxed", r"\begin", r"\end",
    r"\langle", r"\rangle", r"\lvert", r"\rvert", r"\lbrace", r"\rbrace", r"\mid",
    r"\hline", r"\lim", r"\min", r"\max", r"\otimes", r"\oint", r"\prime",
}


def ledger_symbols() -> tuple[list[str], int]:
    text = LEDGER.read_text(encoding="utf-8")
    budget_m = re.search(r"\*\*Budget:\s*(\d+)\s+parameters", text)
    if not budget_m:
        sys.exit("ledger.md: missing '**Budget: N parameters' line")
    budget = int(budget_m.group(1))
    section = text.split("## Parameters", 1)[1].split("\n## ", 1)[0]
    symbols = []
    for line in section.splitlines():
        m = re.match(r"\|\s*\d+\s*\|\s*`([^`]+)`", line)
        if m:
            symbols.append(m.group(1).strip())
    return symbols, budget


def normalize(tok: str) -> str:
    return tok.replace("{", "").replace("}", "").replace(" ", "")


def scan_v2(known: set[str]) -> dict[str, list[str]]:
    unknown: dict[str, list[str]] = {}
    for path in sorted(V2.glob("*.md")):
        if path.name in SKIP:
            continue
        text = path.read_text(encoding="utf-8")
        for m in MATH_RE.finditer(text):
            body = m.group(1) or m.group(2)
            # \mathrm{...} is reserved for units and is ignored; \text{...} is kept so that
            # subscripts like N_{\text{eff}} survive as N_eff
            body = re.sub(r"\\mathrm\{[^{}]*\}", " ", body)
            body = re.sub(r"\\(?:text|mathcal|mathbf)(\{[^{}]*\})", r"\1", body)
            body = re.sub(r"\{\{([^{}]*)\}\}", r"{\1}", body)
            for t in TOKEN_RE.finditer(body):
                head = t.group(1)
                if head in LATEX_CONTROL:
                    continue
                tok = normalize(t.group(0))
                if tok in known:
                    continue
                unknown.setdefault(tok, []).append(f"{path.name}: {body.strip()[:60]}")
    return unknown


def main() -> int:
    symbols, budget = ledger_symbols()
    allow = {
        normalize(l.strip())
        for l in ALLOWLIST.read_text(encoding="utf-8").splitlines()
        if l.strip() and not l.startswith("#")
    }
    known = {normalize(s) for s in symbols} | allow

    ok = True
    if len(symbols) > budget:
        print(f"FAIL: ledger declares {len(symbols)} parameters, budget is {budget}")
        ok = False
    else:
        print(f"ledger: {len(symbols)}/{budget} parameters used")

    unknown = scan_v2(known)
    if "--list" in sys.argv:
        for tok in sorted(unknown):
            print(tok)
        return 0
    if unknown:
        ok = False
        print("FAIL: symbols in v2/ math with no ledger row or allowlist entry:")
        for tok, where in sorted(unknown.items()):
            print(f"  {tok:20s} <- {where[0]}")
    else:
        print("v2/: all math symbols declared")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
