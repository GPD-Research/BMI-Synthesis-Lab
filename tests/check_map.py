"""Consistency checks for the theory maps (v2/map_v1.yaml, v2/map.yaml) and viewer/map_data.js.

Fails when the map drifts from the repository: a file, section or test it names is missing; the
v2 parameter boxes differ from the nine rows of v2/ledger.md; a RETRACTED.md entry has no box (or
a box cites a missing entry); a CI script appears on no box; a link points nowhere, forms a
cycle, or is verified without saying by what; a derived box rests on an unresolved link; or
viewer/map_data.js is stale. If node is installed, also checks that viewer/graph.js computes the
same conditional set as tests/build_map.py.
"""
import json, os, re, subprocess, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_map as B

ROOT = B.ROOT
STATUSES = {
    "v2": {"axiom", "derived", "verify", "fitted", "open", "paused", "killed", "retracted", "borrowed",
           "passed", "fired", "relabelled"},
    "v1": {"axiom", "kept", "hypothesis", "hard-stop", "dropped", "suspended", "retracted"},
}
KINDS = {"axiom", "choice", "derived", "parameter", "prediction", "question", "leap", "dead", "kill"}
LINKS = {"verified", "open", "broken"}
errors = []


def err(msg):
    errors.append(msg)


def exists(p):
    return os.path.exists(os.path.join(ROOT, p))


def check_map(version, m):
    nodes = m["nodes"]
    ids = [n["id"] for n in nodes]
    idset = set(ids)
    for i in idset:
        if ids.count(i) > 1:
            err(f"{version}: duplicate id {i}")
    ntiers = len(m["meta"]["tiers"])
    traps = m["meta"].get("traps", {})
    for n in nodes:
        where = f"{version}:{n['id']}"
        if n.get("status") not in STATUSES[version]:
            err(f"{where}: status {n.get('status')!r} not in {sorted(STATUSES[version])}")
        if n.get("kind") not in KINDS:
            err(f"{where}: kind {n.get('kind')!r}")
        if not (isinstance(n.get("tier"), int) and 0 <= n["tier"] < ntiers):
            err(f"{where}: tier {n.get('tier')!r} out of range")
        if not n.get("title"):
            err(f"{where}: no title")
        f = n.get("file")
        if not f or not exists(f):
            err(f"{where}: file {f!r} missing")
        elif n.get("section") and n.get("line") is None:
            err(f"{where}: no heading for section {n['section']!r} in {f}")
        for t in n["test"]:
            if not exists(t):
                err(f"{where}: test {t} missing")
        if n.get("trap") and n["trap"] not in traps:
            err(f"{where}: trap {n['trap']!r} not in meta.traps")
        if n["status"] in ("retracted",) and not n.get("retracted") and version == "v1":
            err(f"{where}: retracted box without a RETRACTED.md key")
        incoming = set()
        for e in n["from"]:
            if e.get("id") not in idset:
                err(f"{where}: link from unknown id {e.get('id')!r}")
            if e.get("link") not in LINKS:
                err(f"{where}: link type {e.get('link')!r}")
            if e.get("link") == "verified" and not e.get("by"):
                err(f"{where}: verified link from {e.get('id')} has no 'by'")
            if e.get("link") in ("open", "broken") and not e.get("why"):
                err(f"{where}: {e.get('link')} link from {e.get('id')} has no 'why'")
            incoming.add(e.get("link"))
        if n["status"] == "derived" and incoming - {"verified"}:
            err(f"{where}: derived but rests on an unresolved link (mark it open/paused/leap or verify the link)")
    for c in m.get("contradictions", []):
        for k in ("a", "b"):
            if c.get(k) not in idset:
                err(f"{version}: contradiction names unknown id {c.get(k)!r}")
        if not c.get("why"):
            err(f"{version}: contradiction {c.get('a')}–{c.get('b')} has no 'why'")
    # cycles
    parents = {n["id"]: [e["id"] for e in n["from"]] for n in nodes}
    state = {}

    def visit(i, path):
        if state.get(i) == 1:
            err(f"{version}: cycle {' -> '.join(path + [i])}")
            return
        if state.get(i) == 2:
            return
        state[i] = 1
        for p in parents.get(i, []):
            visit(p, path + [i])
        state[i] = 2
    for i in parents:
        visit(i, [])


def main():
    data = B.build()
    v1, v2 = data["maps"]["v1"], data["maps"]["v2"]
    for version, m in data["maps"].items():
        check_map(version, m)
    v1ids = {n["id"] for n in v1["nodes"]}
    v2ids = {n["id"] for n in v2["nodes"]}
    for n in v1["nodes"]:
        if n.get("v2") and n["v2"] not in v2ids:
            err(f"v1:{n['id']}: v2 counterpart {n['v2']!r} missing")
    for n in v2["nodes"]:
        if n.get("v1") and n["v1"] not in v1ids:
            err(f"v2:{n['id']}: v1 counterpart {n['v1']!r} missing")

    # the nine parameters
    with open(os.path.join(ROOT, "v2/ledger.md"), encoding="utf-8") as f:
        rows = re.findall(r"^\| *\d+ \| `([^`]+)`", f.read(), re.M)
    boxes = [s for n in v2["nodes"] if n["kind"] == "parameter" for s in n.get("ledger", [])]
    if sorted(rows) != sorted(boxes):
        err(f"v2 parameter boxes {sorted(boxes)} != ledger rows {sorted(rows)}")

    # RETRACTED.md entries <-> boxes
    with open(os.path.join(ROOT, "RETRACTED.md"), encoding="utf-8") as f:
        keys = re.findall(r"^#+\s*([RN]\d+)\.", f.read(), re.M)
    used = {}
    for version, m in data["maps"].items():
        for n in m["nodes"]:
            if n.get("retracted"):
                used.setdefault(n["retracted"], []).append(f"{version}:{n['id']}")
    for k in keys:
        if k not in used:
            err(f"RETRACTED.md {k} has no box on either map")
    for k, who in used.items():
        if k not in keys:
            err(f"{who}: RETRACTED.md has no entry {k}")
        if len(who) > 1:
            err(f"RETRACTED.md {k} is on several boxes: {who}")
        if k.startswith("N") and not all(w.startswith("v2:") for w in who):
            err(f"{k} is a v2 result but sits on {who}")

    # every CI script appears on some box
    with open(os.path.join(ROOT, ".github/workflows/ledger.yml"), encoding="utf-8") as f:
        ci = set(re.findall(r"python3 (tests/\S+\.py)", f.read())) - {"tests/check_map.py", "tests/build_map.py"}
    on_map = {t for m in data["maps"].values() for n in m["nodes"] for t in n["test"]}
    for t in sorted(ci - on_map):
        err(f"CI script {t} appears on no map box")

    # generated file is fresh
    out = os.path.join(ROOT, B.OUT)
    fresh = B.render(data)
    if not os.path.exists(out) or open(out, encoding="utf-8").read() != fresh:
        err(f"{B.OUT} is stale: run python3 tests/build_map.py")

    # JS vs Python: conditional boxes
    node = shutil.which("node")
    if node:
        js = (
            "global.window={};require(process.argv[1]);const G=require(process.argv[2]);"
            "const o={};for(const v in window.BMI_MAP.maps){o[v]=[...G.downstreamOfOpen(window.BMI_MAP.maps[v].nodes)].sort();}"
            "console.log(JSON.stringify(o));"
        )
        r = subprocess.run([node, "-e", js, out, os.path.join(ROOT, "viewer/graph.js")],
                           capture_output=True, text=True)
        if r.returncode:
            err(f"node failed: {r.stderr.strip()}")
        else:
            got = json.loads(r.stdout)
            for v, m in data["maps"].items():
                if sorted(got.get(v, [])) != sorted(m["conditional"]):
                    err(f"{v}: viewer/graph.js conditional set differs from tests/build_map.py")
    else:
        print("node not found: skipped the JS vs Python check")

    for v, m in data["maps"].items():
        links = [e["link"] for n in m["nodes"] for e in n["from"]]
        print(f"{v}: {len(m['nodes'])} boxes, {links.count('verified')} ✓, {links.count('open')} ?, "
              f"{links.count('broken')} ✗, {len(m['contradictions'])} contradictions, "
              f"{sum(1 for n in m['nodes'] if n.get('needs'))} !, {len(m['conditional'])} conditional")
    if errors:
        print("\n".join("FAIL " + e for e in errors))
        sys.exit(1)
    print("map OK")


if __name__ == "__main__":
    main()
