// Pure graph logic for the theory map: no DOM. Loaded by index.html and by tests/check_map.py (node).
(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.MapGraph = factory();
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  // Ids that depend, directly or through other boxes, on a link marked open or broken.
  // Mirrors downstream_of_open() in tests/build_map.py.
  function downstreamOfOpen(nodes) {
    const children = new Map();
    const seeds = [];
    for (const n of nodes) {
      for (const e of n.from || []) {
        if (!children.has(e.id)) children.set(e.id, []);
        children.get(e.id).push(n.id);
        if (e.link === "open" || e.link === "broken") seeds.push(n.id);
      }
    }
    const out = new Set();
    const stack = seeds.slice();
    while (stack.length) {
      const i = stack.pop();
      if (out.has(i)) continue;
      out.add(i);
      for (const c of children.get(i) || []) stack.push(c);
    }
    return out;
  }

  function closure(start, next) {
    const out = new Set();
    const stack = [start];
    while (stack.length) {
      const i = stack.pop();
      for (const j of next(i)) if (!out.has(j)) { out.add(j); stack.push(j); }
    }
    return out;
  }

  function index(nodes) {
    const parents = new Map(), children = new Map();
    for (const n of nodes) { parents.set(n.id, []); children.set(n.id, []); }
    for (const n of nodes) for (const e of n.from || []) {
      if (!children.has(e.id)) continue;
      parents.get(n.id).push(e.id);
      children.get(e.id).push(n.id);
    }
    return { parents, children };
  }

  function upstream(nodes, id) { const g = index(nodes); return closure(id, (i) => g.parents.get(i) || []); }
  function downstream(nodes, id) { const g = index(nodes); return closure(id, (i) => g.children.get(i) || []); }

  // Layered layout: tier = row; order inside a row by the mean x of linked boxes (a few sweeps).
  function layout(nodes, opt) {
    const o = Object.assign({ w: 196, h: 64, gapX: 22, gapY: 92 }, opt || {});
    const g = index(nodes);
    const rows = new Map();
    for (const n of nodes) { if (!rows.has(n.tier)) rows.set(n.tier, []); rows.get(n.tier).push(n.id); }
    const tiers = [...rows.keys()].sort((a, b) => a - b);
    const pos = new Map();
    const place = () => {
      for (const t of tiers) rows.get(t).forEach((id, k) => pos.set(id, k));
    };
    place();
    const mean = (ids) => {
      const xs = ids.filter((i) => pos.has(i)).map((i) => pos.get(i) / Math.max(1, rows.get(tierOf(i)).length - 1));
      return xs.length ? xs.reduce((a, b) => a + b, 0) / xs.length : null;
    };
    const tierById = new Map(nodes.map((n) => [n.id, n.tier]));
    function tierOf(i) { return tierById.get(i); }
    for (let sweep = 0; sweep < 6; sweep++) {
      const order = sweep % 2 === 0 ? tiers : tiers.slice().reverse();
      for (const t of order) {
        const row = rows.get(t);
        const key = new Map();
        row.forEach((id, k) => {
          const nb = sweep % 2 === 0 ? g.parents.get(id) : g.children.get(id);
          const m = mean(nb || []);
          key.set(id, m === null ? k / Math.max(1, row.length - 1) : m);
        });
        row.sort((a, b) => key.get(a) - key.get(b));
        place();
      }
    }
    const widest = Math.max(...tiers.map((t) => rows.get(t).length));
    const full = widest * (o.w + o.gapX);
    const boxes = new Map();
    tiers.forEach((t, r) => {
      const row = rows.get(t);
      const span = row.length * (o.w + o.gapX);
      const x0 = (full - span) / 2;
      row.forEach((id, k) => boxes.set(id, { x: x0 + k * (o.w + o.gapX), y: r * (o.h + o.gapY) + 40, w: o.w, h: o.h, row: r }));
    });
    return { boxes, width: full, height: tiers.length * (o.h + o.gapY) + 40, tiers };
  }

  return { downstreamOfOpen, upstream, downstream, layout, index };
});
