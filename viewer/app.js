/* BMI theory map viewer. Data: window.BMI_MAP (viewer/map_data.js). Logic: window.MapGraph (graph.js). */
(function () {
  "use strict";
  const DATA = window.BMI_MAP;
  const G = window.MapGraph;
  const SVGNS = "http://www.w3.org/2000/svg";
  const STATUS = {
    axiom: ["#1f3a5f", "#1f3a5f", "#fff", "axiom"],
    derived: ["#e8f5e9", "#2e7d32", "#1b3d1d", "derived"],
    verify: ["#fff8e1", "#f9a825", "#5d4300", "derived, [verify] open"],
    open: ["#e3f2fd", "#1565c0", "#0d2f57", "open"],
    paused: ["#f3e5f5", "#7b1fa2", "#3d1050", "paused"],
    killed: ["#eceff1", "#546e7a", "#37474f", "killed by data"],
    retracted: ["#ffebee", "#c62828", "#6d0f0f", "dead / retracted"],
    borrowed: ["#fff3e0", "#ef6c00", "#5a2a00", "parameter (borrowed)"],
    passed: ["#c8e6c9", "#1b5e20", "#0f3311", "kill test passed"],
    fired: ["#ffcdd2", "#b71c1c", "#5c0a0a", "kill test fired"],
    relabelled: ["#eceff1", "#78909c", "#37474f", "kill test re-labelled"],
    kept: ["#e8f5e9", "#2e7d32", "#1b3d1d", "kept (survives into v2)"],
    hypothesis: ["#e3f2fd", "#1565c0", "#0d2f57", "kept as hypothesis"],
    "hard-stop": ["#b71c1c", "#7f0000", "#fff", "hard stop"],
    dropped: ["#eeeeee", "#757575", "#424242", "dropped"],
    suspended: ["#fff3e0", "#e65100", "#5a2a00", "suspended"],
  };
  const KIND = { axiom: "AXIOM", choice: "CHOICE", derived: "RESULT", parameter: "PARAMETER", prediction: "PREDICTION",
    question: "OPEN QUESTION", leap: "LEAP", dead: "DEAD BRANCH", kill: "DATA / KILL TEST" };
  const LINK = { verified: ["✓", "#2e7d32"], open: ["?", "#1565c0"], broken: ["✗", "#c62828"] };
  const DEAD = new Set(["retracted", "killed", "dropped"]);

  const state = { view: "v1", hideDead: false, contradictions: true, failuresOnly: false, search: "", sel: {} };
  const $ = (s) => document.querySelector(s);
  const el = (tag, attrs, parent) => {
    const e = document.createElementNS(SVGNS, tag);
    for (const k in attrs || {}) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  };
  const h = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };

  function wrap(text, max) {
    const words = text.split(/\s+/), lines = [];
    let cur = "";
    for (const w of words) {
      if ((cur + " " + w).trim().length > max && cur) { lines.push(cur); cur = w; } else cur = (cur + " " + w).trim();
    }
    if (cur) lines.push(cur);
    if (lines.length > 3) { lines.length = 3; lines[2] = lines[2].replace(/.{0,2}$/, "…"); }
    return lines;
  }

  function visibleNodes(m) {
    let nodes = m.nodes;
    if (state.hideDead) nodes = nodes.filter((n) => !DEAD.has(n.status) && n.kind !== "dead");
    return nodes;
  }

  // ---------------------------------------------------------------- one pane
  function Pane(host, version) {
    const m = DATA.maps[version];
    const nodes = visibleNodes(m);
    const ids = new Set(nodes.map((n) => n.id));
    const byId = new Map(m.nodes.map((n) => [n.id, n]));
    const L = G.layout(nodes);
    const cond = new Set(m.conditional);
    host.innerHTML = "";
    const svg = el("svg", { class: "map" }, host);
    const pad = 140;
    let vb = { x: -pad, y: -10, w: L.width + 2 * pad, h: L.height + 20 };
    const setVB = () => svg.setAttribute("viewBox", `${vb.x} ${vb.y} ${vb.w} ${vb.h}`);
    const fit = () => { vb = { x: -pad, y: -10, w: L.width + 2 * pad, h: L.height + 20 }; setVB(); };
    fit();
    const root = el("g", {}, svg);

    // tier bands
    L.tiers.forEach((t, r) => {
      const y = r * (64 + 92) + 40;
      el("rect", { x: -pad, y: y - 30, width: L.width + 2 * pad, height: 64 + 60, class: r % 2 ? "band odd" : "band" }, root);
      const lab = el("text", { x: -pad + 8, y: y - 14, class: "bandlabel" }, root);
      lab.textContent = m.meta.tiers[t];
    });

    const edgeLayer = el("g", {}, root), contraLayer = el("g", {}, root), nodeLayer = el("g", {}, root), markLayer = el("g", {}, root);
    const nodeEls = new Map(), edgeEls = [];

    // spread entry/exit points along each box edge so markers and lines do not pile up
    const inSlots = new Map(), outSlots = new Map();
    for (const n of nodes) for (const e of n.from) {
      if (!ids.has(e.id)) continue;
      if (!inSlots.has(n.id)) inSlots.set(n.id, []);
      if (!outSlots.has(e.id)) outSlots.set(e.id, []);
      inSlots.get(n.id).push(e.id); outSlots.get(e.id).push(n.id);
    }
    const sortX = (arr) => arr.sort((p, q) => L.boxes.get(p).x - L.boxes.get(q).x);
    for (const v of inSlots.values()) sortX(v);
    for (const v of outSlots.values()) sortX(v);
    const slotX = (box, list, other) => box.x + box.w * (list.indexOf(other) + 1) / (list.length + 1);
    const bez = (p0, p1, p2, p3, t) => {
      const u = 1 - t;
      return u * u * u * p0 + 3 * u * u * t * p1 + 3 * u * t * t * p2 + t * t * t * p3;
    };
    function curve(fromId, toId) {
      const a = L.boxes.get(fromId), b = L.boxes.get(toId);
      const ax = slotX(a, outSlots.get(fromId), toId), bx = slotX(b, inSlots.get(toId), fromId);
      let ay, by, c1, c2;
      if (b.y > a.y) { ay = a.y + a.h; by = b.y; const d = Math.min(80, (by - ay) / 2); c1 = ay + d; c2 = by - d; }
      else if (b.y < a.y) { ay = a.y; by = b.y + b.h; const d = Math.min(80, (ay - by) / 2); c1 = ay - d; c2 = by + d; }
      else { ay = a.y + a.h; by = b.y + b.h; c1 = ay + 46; c2 = by + 46; }
      const t = b.y === a.y ? 0.5 : 0.86;
      return { d: `M${ax},${ay} C${ax},${c1} ${bx},${c2} ${bx},${by}`, mx: bez(ax, ax, bx, bx, t), my: bez(ay, c1, c2, by, t) };
    }

    for (const n of nodes) for (const e of n.from) {
      if (!ids.has(e.id)) continue;
      const c = curve(e.id, n.id);
      const [sym, col] = LINK[e.link];
      const p = el("path", { d: c.d, class: "edge " + e.link, stroke: col }, edgeLayer);
      const g = el("g", { class: "mark", transform: `translate(${c.mx},${c.my})` }, markLayer);
      el("circle", { r: 8.5, fill: "#fff", stroke: col, "stroke-width": 1.6 }, g);
      const t = el("text", { y: 4, "text-anchor": "middle", fill: col, class: "marksym" }, g);
      t.textContent = sym;
      el("title", {}, g).textContent = `${byId.get(e.id).title} → ${n.title}\n${e.link === "verified" ? "✓ by " + e.by : (e.link === "open" ? "? " : "✗ ") + e.why}`;
      g.addEventListener("click", (ev) => { ev.stopPropagation(); showLink(version, e, n); });
      edgeEls.push({ from: e.id, to: n.id, p, g });
    }

    const contraEls = [];
    if (state.contradictions) for (const c of m.contradictions) {
      if (!ids.has(c.a) || !ids.has(c.b)) continue;
      const a = L.boxes.get(c.a), b = L.boxes.get(c.b);
      const ax = a.x + a.w / 2, ay = a.y + a.h / 2, bx = b.x + b.w / 2, by = b.y + b.h / 2;
      const mx = (ax + bx) / 2, my = Math.min(ay, by) - 70 - Math.abs(ax - bx) * 0.08;
      const p = el("path", { d: `M${ax},${ay} Q${mx},${my} ${bx},${by}`, class: "contra" }, contraLayer);
      const g = el("g", { class: "mark", transform: `translate(${mx},${(my + (ay + by) / 2) / 2})` }, markLayer);
      el("rect", { x: -10, y: -10, width: 20, height: 20, rx: 3, fill: "#c62828" }, g);
      const t = el("text", { y: 5, "text-anchor": "middle", fill: "#fff", class: "marksym" }, g);
      t.textContent = "≠";
      el("title", {}, g).textContent = "Contradiction: " + c.why;
      g.addEventListener("click", (ev) => { ev.stopPropagation(); showContradiction(version, c); });
      contraEls.push({ a: c.a, b: c.b, p, g });
    }

    for (const n of nodes) {
      const b = L.boxes.get(n.id);
      const [fill, stroke, ink] = STATUS[n.status] || ["#fff", "#999", "#000"];
      const g = el("g", { class: "node", transform: `translate(${b.x},${b.y})`, tabindex: 0 }, nodeLayer);
      if (n.critical) el("rect", { x: -5, y: -5, width: b.w + 10, height: b.h + 10, rx: 10, class: "critical-halo" }, g);
      const leap = n.kind === "leap" || n.kind === "question";
      const dashed = leap || (cond.has(n.id) && !DEAD.has(n.status));
      el("rect", { width: b.w, height: b.h, rx: leap ? 14 : 6, fill, stroke, "stroke-width": n.critical ? 2.6 : 1.4,
        "stroke-dasharray": dashed ? "5 3" : null, class: "box" }, g);
      const kt = el("text", { x: 7, y: 12, class: "kind", fill: ink }, g);
      kt.textContent = KIND[n.kind] + (n.generic ? " · generic" : "");
      wrap(n.title, 31).forEach((line, i) => {
        const t = el("text", { x: 7, y: 27 + i * 13, class: "title", fill: ink }, g);
        t.textContent = line;
      });
      if (DEAD.has(n.status) || n.kind === "dead") el("line", { x1: 4, y1: b.h - 5, x2: b.w - 4, y2: b.h - 5, stroke, "stroke-width": 1.2 }, g);
      let bx = b.w - 4;
      const badge = (txt, color, title) => {
        const w = 7 + txt.length * 6.4;
        bx -= w;
        const bg = el("g", { transform: `translate(${bx},-9)` }, g);
        el("rect", { width: w, height: 15, rx: 7.5, fill: color }, bg);
        const t = el("text", { x: w / 2, y: 11, "text-anchor": "middle", class: "badge" }, bg);
        t.textContent = txt;
        el("title", {}, bg).textContent = title;
        bx -= 3;
      };
      if (n.needs) badge("!", "#f57c00", "Needs a number the theory does not supply: " + n.needs);
      if (n.retracted) badge(n.retracted, "#c62828", "RETRACTED.md " + n.retracted);
      if (n.v2) badge("→v2", "#37474f", "Survives into v2 as: " + DATA.maps.v2.nodes.find((x) => x.id === n.v2).title);
      if (n.v1) badge("←v1", "#37474f", "From v1: " + DATA.maps.v1.nodes.find((x) => x.id === n.v1).title);
      if (n.critical) badge("CRITICAL", "#7f0000", "One of the failures that sank v1: " + (n.trap || ""));
      g.addEventListener("click", (ev) => { ev.stopPropagation(); select(version, n.id, true); });
      nodeEls.set(n.id, g);
    }

    // pan / zoom
    let drag = null;
    svg.addEventListener("wheel", (ev) => {
      ev.preventDefault();
      const k = Math.exp(ev.deltaY * 0.0015);
      const pt = svg.createSVGPoint();
      pt.x = ev.clientX; pt.y = ev.clientY;
      const u = pt.matrixTransform(svg.getScreenCTM().inverse());
      const px = u.x, py = u.y;
      vb = { x: px - (px - vb.x) * k, y: py - (py - vb.y) * k, w: vb.w * k, h: vb.h * k };
      setVB();
    }, { passive: false });
    svg.addEventListener("pointerdown", (ev) => {
      drag = { x: ev.clientX, y: ev.clientY, vb: Object.assign({}, vb), moved: false, id: ev.pointerId };
    });
    svg.addEventListener("pointermove", (ev) => {
      if (!drag) return;
      const r = svg.getBoundingClientRect();
      const dx = ev.clientX - drag.x, dy = ev.clientY - drag.y;
      if (!drag.moved && Math.abs(dx) + Math.abs(dy) > 3) { drag.moved = true; svg.setPointerCapture(drag.id); }
      const s = Math.max(vb.w / r.width, vb.h / r.height);
      vb.x = drag.vb.x - dx * s; vb.y = drag.vb.y - dy * s;
      setVB();
    });
    svg.addEventListener("pointerup", () => { setTimeout(() => (drag = null), 0); });
    svg.addEventListener("pointercancel", () => { drag = null; });
    svg.addEventListener("click", () => { if (!drag || !drag.moved) select(version, null, true); });

    function highlight(id) {
      const q = state.search.trim().toLowerCase();
      const match = (n) => q && (n.title + " " + (n.file || "") + " " + n.id + " " + (n.statement || "")).toLowerCase().includes(q);
      const up = id ? G.upstream(nodes, id) : null, down = id ? G.downstream(nodes, id) : null;
      for (const [nid, g] of nodeEls) {
        const n = byId.get(nid);
        let cls = "node";
        if (id) cls += nid === id ? " sel" : up.has(nid) ? " up" : down.has(nid) ? " down" : " dim";
        else if (state.failuresOnly && !n.critical) cls += " dim";
        if (match(n)) cls += " hit";
        g.setAttribute("class", cls);
      }
      for (const e of edgeEls) {
        const on = !id || ((e.to === id || up.has(e.to)) && (e.from === id || up.has(e.from))) ||
          ((e.from === id || down.has(e.from)) && (e.to === id || down.has(e.to)));
        e.p.classList.toggle("dim", !on);
        e.g.classList.toggle("dim", !on);
      }
      for (const c of contraEls) {
        const on = !id || c.a === id || c.b === id;
        c.p.classList.toggle("dim", !on); c.g.classList.toggle("dim", !on);
      }
    }
    function center(id) {
      const b = L.boxes.get(id);
      if (!b) return;
      vb.x = b.x + b.w / 2 - vb.w / 2; vb.y = b.y + b.h / 2 - vb.h / 2; setVB();
    }
    highlight(null);
    return { highlight, center, fit, has: (id) => ids.has(id) };
  }

  // ---------------------------------------------------------------- detail panel
  function fileLink(file, line) {
    const span = h("span", "file");
    const a = h("a", null, file + (line ? ":" + line : ""));
    a.href = `${DATA.repo}/blob/main/${file}` + (line ? `?plain=1#L${line}` : "");
    a.target = "_blank";
    a.title = "Open on GitHub";
    span.appendChild(a);
    if (location.protocol === "file:") {
      const loc = h("a", "local", "local");
      loc.href = "../" + file;
      loc.target = "_blank";
      span.appendChild(loc);
    }
    return span;
  }
  function math(tex) {
    const d = h("div", "math");
    if (window.katex) window.katex.render(tex, d, { throwOnError: false, displayMode: true });
    else d.textContent = tex;
    return d;
  }
  function row(panel, label, content) {
    const r = h("div", "row");
    r.appendChild(h("div", "label", label));
    const v = h("div", "value");
    if (typeof content === "string") v.textContent = content; else v.appendChild(content);
    r.appendChild(v);
    panel.appendChild(r);
  }
  function chip(version, id, prefix) {
    const n = DATA.maps[version].nodes.find((x) => x.id === id);
    const b = h("button", "chip", (prefix || "") + n.title);
    const [fill, stroke] = STATUS[n.status];
    b.style.background = fill; b.style.borderColor = stroke;
    b.onclick = () => select(version, id, true, true);
    return b;
  }

  function showNode(version, id) {
    const m = DATA.maps[version];
    const n = m.nodes.find((x) => x.id === id);
    const p = $("#detail");
    p.innerHTML = "";
    p.appendChild(h("div", "dkind", KIND[n.kind] + " · " + version));
    p.appendChild(h("h2", null, n.title));
    const st = h("div", "status", (STATUS[n.status] || [])[3] || n.status);
    st.style.background = STATUS[n.status][0]; st.style.borderColor = STATUS[n.status][1]; st.style.color = STATUS[n.status][2];
    p.appendChild(st);
    if (new Set(m.conditional).has(n.id) && !DEAD.has(n.status))
      p.appendChild(h("div", "warn", "Conditional: rests, directly or further up, on a link that is not resolved (?) or broken (✗)."));
    if (n.statement) p.appendChild(math(n.statement));
    if (n.failure) row(p, n.critical ? "Critical failure" : "Why it failed", n.failure);
    if (n.trap) row(p, "Failure mode", `${n.trap}: ${m.meta.traps[n.trap]}`);
    if (n.guard) row(p, "v2 guard", n.guard);
    if (n.needs) row(p, "! Needs", n.needs);
    if (n.file) row(p, "File", fileLink(n.file, n.line));
    if (n.section) row(p, "Section", "§" + n.section);
    if (n.test.length) { const d = h("div"); n.test.forEach((t) => d.appendChild(fileLink(t))); row(p, "Check", d); }
    if (n.ledger) row(p, "Ledger", n.ledger.join(", "));
    if (n.retracted) row(p, "Record", fileLink("RETRACTED.md", null)), p.lastChild.querySelector("a").textContent = "RETRACTED.md " + n.retracted;
    if (n.tags) row(p, "Structure tags", n.tags.join(", "));
    if (n.notes) row(p, "Notes", n.notes);
    if (n.v2) { const d = h("div"); d.appendChild(chip("v2", n.v2, "v2: ")); row(p, "Became", d); }
    if (n.v1) { const d = h("div"); d.appendChild(chip("v1", n.v1, "v1: ")); row(p, "Came from", d); }
    const back = m.nodes.filter((x) => x.v1 === n.id || x.v2 === n.id);
    if (back.length) { /* handled by v1/v2 fields */ }
    if (n.from.length) {
      const d = h("div");
      for (const e of n.from) {
        const r = h("div", "linkrow");
        const s = h("span", "lsym " + e.link, LINK[e.link][0]);
        r.appendChild(s); r.appendChild(chip(version, e.id));
        r.appendChild(h("div", "lwhy", e.link === "verified" ? "by " + e.by : e.why));
        d.appendChild(r);
      }
      row(p, "Rests on", d);
    }
    const kids = m.nodes.filter((x) => x.from.some((e) => e.id === n.id));
    if (kids.length) {
      const d = h("div");
      for (const k of kids) {
        const e = k.from.find((x) => x.id === n.id);
        const r = h("div", "linkrow");
        r.appendChild(h("span", "lsym " + e.link, LINK[e.link][0]));
        r.appendChild(chip(version, k.id));
        d.appendChild(r);
      }
      row(p, "Feeds", d);
    }
    const cs = m.contradictions.filter((c) => c.a === n.id || c.b === n.id);
    for (const c of cs) {
      const d = h("div");
      d.appendChild(chip(version, c.a === n.id ? c.b : c.a, "≠ "));
      d.appendChild(h("div", "lwhy", c.why));
      row(p, "Contradicts", d);
    }
  }
  function showLink(version, e, n) {
    const m = DATA.maps[version];
    const p = $("#detail");
    p.innerHTML = "";
    p.appendChild(h("div", "dkind", "LINK · " + version));
    p.appendChild(h("h2", null, { verified: "Verified link", open: "Unresolved link", broken: "Broken link" }[e.link]));
    const d = h("div");
    d.appendChild(chip(version, e.id)); d.appendChild(h("div", "arrow", "↓ " + LINK[e.link][0]));
    d.appendChild(chip(version, n.id));
    row(p, "Connects", d);
    row(p, e.link === "verified" ? "Verified by" : e.link === "open" ? "What is missing" : "Why it fails", e.link === "verified" ? e.by : e.why);
    if (e.link === "open") p.appendChild(h("div", "warn", "Everything below this link is conditional until it is resolved, here or by a parallel branch."));
    void m;
  }
  function showContradiction(version, c) {
    const p = $("#detail");
    p.innerHTML = "";
    p.appendChild(h("div", "dkind", "CONTRADICTION · " + version));
    p.appendChild(h("h2", null, "These cannot both hold"));
    const d = h("div");
    d.appendChild(chip(version, c.a)); d.appendChild(h("div", "arrow", "≠")); d.appendChild(chip(version, c.b));
    row(p, "Between", d);
    row(p, "Why", c.why);
    if (c.source) row(p, "Source", fileLink(c.source));
  }
  function showOverview() {
    const p = $("#detail");
    p.innerHTML = "";
    const vs = state.view === "compare" ? ["v1", "v2"] : [state.view];
    for (const v of vs) {
      const m = DATA.maps[v];
      p.appendChild(h("h2", null, m.meta.title));
      if (m.meta.summary) p.appendChild(h("p", "summary", m.meta.summary));
      const links = m.nodes.flatMap((n) => n.from.map((e) => e.link));
      const cnt = (k) => links.filter((x) => x === k).length;
      const t = h("table", "stats");
      const add = (a, b) => { const r = h("tr"); r.appendChild(h("td", null, a)); r.appendChild(h("td", "num", String(b))); t.appendChild(r); };
      add("boxes", m.nodes.length);
      add("✓ verified links", cnt("verified"));
      add("? unresolved links", cnt("open"));
      add("✗ broken links", cnt("broken"));
      add("! boxes needing an unsupplied number", m.nodes.filter((n) => n.needs).length);
      add("≠ contradictions", m.contradictions.length);
      add("conditional boxes", m.conditional.filter((id) => !DEAD.has(m.nodes.find((n) => n.id === id).status)).length);
      add("critical failures", m.nodes.filter((n) => n.critical).length);
      add("dead / retracted / dropped", m.nodes.filter((n) => DEAD.has(n.status)).length);
      p.appendChild(t);
      const crit = m.nodes.filter((n) => n.critical);
      if (crit.length) {
        p.appendChild(h("h3", null, "Critical failures"));
        crit.forEach((n) => p.appendChild(chip(v, n.id)));
      }
    }
    p.appendChild(h("p", "hint", "Click a box or a link marker for details. Drag to pan, scroll to zoom."));
  }

  // ---------------------------------------------------------------- views
  let panes = {};
  function select(version, id, fromClick, center) {
    state.sel[version] = id;
    if (panes[version]) panes[version].highlight(id);
    if (center && id && panes[version]) panes[version].center(id);
    if (id) {
      if (!panes[version]) { setView(version); state.sel[version] = id; panes[version].highlight(id); panes[version].center(id); }
      showNode(version, id);
      if (state.view === "compare") {
        const n = DATA.maps[version].nodes.find((x) => x.id === id);
        const other = version === "v1" ? "v2" : "v1";
        const twin = n[other] || (DATA.maps[other].nodes.find((x) => x[version] === id) || {}).id;
        if (twin && panes[other].has(twin)) { panes[other].highlight(twin); panes[other].center(twin); state.sel[other] = twin; }
        else if (panes[other]) panes[other].highlight(null);
      }
    } else showOverview();
  }

  function trapTable() {
    const v1 = DATA.maps.v1, v2 = DATA.maps.v2;
    const box = h("div", "traps");
    box.appendChild(h("h3", null, "v1 failure modes and the v2 guard against each"));
    const t = h("table");
    const hr = h("tr");
    ["Failure mode", "v1 boxes", "v2 guard"].forEach((x) => hr.appendChild(h("th", null, x)));
    t.appendChild(hr);
    for (const [trap, desc] of Object.entries(v1.meta.traps)) {
      const ns = v1.nodes.filter((n) => n.trap === trap);
      if (!ns.length) continue;
      const r = h("tr");
      const a = h("td"); a.appendChild(h("b", null, trap)); a.appendChild(h("div", "lwhy", desc)); r.appendChild(a);
      const b = h("td"); ns.forEach((n) => b.appendChild(chip("v1", n.id))); r.appendChild(b);
      const c = h("td"); [...new Set(ns.map((n) => n.guard).filter(Boolean))].forEach((g) => c.appendChild(h("div", "guard", g)));
      if (!c.childNodes.length) c.appendChild(h("div", "lwhy", "no explicit guard recorded"));
      r.appendChild(c);
      t.appendChild(r);
    }
    box.appendChild(t);
    void v2;
    return box;
  }

  function render() {
    const main = $("#main");
    main.innerHTML = "";
    panes = {};
    document.querySelectorAll("#tabs button").forEach((b) => b.classList.toggle("on", b.dataset.view === state.view));
    if (state.view === "compare") {
      main.className = "compare";
      for (const v of ["v1", "v2"]) {
        const col = h("div", "col");
        col.appendChild(h("div", "coltitle", DATA.maps[v].meta.title));
        const host = h("div", "pane");
        col.appendChild(host);
        main.appendChild(col);
        panes[v] = Pane(host, v);
      }
      main.appendChild(trapTable());
    } else {
      main.className = "single";
      const host = h("div", "pane");
      main.appendChild(host);
      panes[state.view] = Pane(host, state.view);
    }
    const cur = state.view === "compare" ? null : state.sel[state.view];
    if (cur && panes[state.view].has(cur)) select(state.view, cur); else showOverview();
  }
  function setView(v) { state.view = v; render(); }

  function init() {
    document.querySelectorAll("#tabs button").forEach((b) => (b.onclick = () => setView(b.dataset.view)));
    $("#hideDead").onchange = (e) => { state.hideDead = e.target.checked; render(); };
    $("#contra").onchange = (e) => { state.contradictions = e.target.checked; render(); };
    $("#failuresOnly").onchange = (e) => { state.failuresOnly = e.target.checked; for (const v in panes) panes[v].highlight(state.sel[v] || null); };
    $("#search").oninput = (e) => { state.search = e.target.value; for (const v in panes) panes[v].highlight(state.sel[v] || null); };
    $("#fit").onclick = () => { for (const v in panes) panes[v].fit(); };
    $("#legendBtn").onclick = () => $("#legend").classList.toggle("open");
    const lg = $("#legendBody");
    const sec = (title, items) => {
      lg.appendChild(h("h4", null, title));
      for (const [k, v] of items) {
        const r = h("div", "lrow");
        const sw = h("span", "sw"); sw.style.background = v[0]; sw.style.borderColor = v[1]; r.appendChild(sw);
        r.appendChild(h("span", null, v[3] || k)); lg.appendChild(r);
      }
    };
    sec("v2 status", ["axiom", "derived", "verify", "open", "paused", "borrowed", "killed", "retracted", "passed", "fired", "relabelled"].map((k) => [k, STATUS[k]]));
    sec("v1 status", ["kept", "hypothesis", "hard-stop", "suspended", "dropped", "retracted"].map((k) => [k, STATUS[k]]));
    lg.appendChild(h("h4", null, "Marks"));
    [["✓", "#2e7d32", "verified link (click for the file/test that shows it)"], ["?", "#1565c0", "unresolved link: not yet worked out"],
      ["✗", "#c62828", "broken link: claimed, shown not to hold"], ["≠", "#c62828", "contradiction between two boxes"],
      ["!", "#f57c00", "needs a number the theory does not supply"], ["- -", "#555", "dashed border: conditional (rests on ? or ✗), or a leap"],
      ["▢", "#7f0000", "red halo: critical failure of v1"]].forEach(([s, c, t]) => {
      const r = h("div", "lrow"); const m = h("span", "msym", s); m.style.color = c; r.appendChild(m); r.appendChild(h("span", null, t)); lg.appendChild(r);
    });
    const v = new URLSearchParams(location.search).get("view");
    setView(["v1", "v2", "compare"].includes(v) ? v : "v1");
  }
  init();
})();
