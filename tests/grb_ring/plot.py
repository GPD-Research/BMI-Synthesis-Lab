import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import fit

xy = fit.gnomonic(fit.grb)
obs = fit.fit_all(xy, spiral_starts=12)
fig, ax = plt.subplots(figsize=(7, 7))
ax.scatter(xy[:, 0], xy[:, 1], c="k", zorder=5, label="9 GRBs (Balázs+2015 Tab.1)")
t = np.linspace(0, 2 * np.pi, 400)
cx, cy, r = obs["circle"][1]
ax.plot(cx + abs(r) * np.cos(t), cy + abs(r) * np.sin(t), "b-", label=f"circle (RMS {np.sqrt(obs['circle'][0]/9):.2f}°)")
cx, cy, A, B, ang = obs["ellipse"][1]
ex, ey = abs(A) * np.cos(t), abs(B) * np.sin(t)
ax.plot(cx + ex * np.cos(ang) - ey * np.sin(ang), cy + ex * np.sin(ang) + ey * np.cos(ang), "g--",
        label=f"ellipse (RMS {np.sqrt(obs['ellipse'][0]/9):.2f}°)")
for name, b, sty in [("golden", np.sign(1), "r-"), ("logspiral", None, "m-")]:
    p = obs[name][1]
    if name == "golden":
        # recover chirality by refitting sign
        cands = [(fit.spiral_rss(p, xy, s * fit.B_GOLDEN), s) for s in (1, -1)]
        b = min(cands)[1] * fit.B_GOLDEN
        cx, cy, a, th0 = p
    else:
        cx, cy, a, th0, b = p
    th = np.linspace(0, 2 * np.pi, 400)
    rr = abs(a) * np.exp(b * th)
    ax.plot(cx + rr * np.cos(th + th0), cy + rr * np.sin(th + th0), sty,
            label=f"{name} b={b:.3f} (RMS {np.sqrt(obs[name][0]/9):.2f}°)")
ax.set_aspect("equal"); ax.legend(fontsize=8); ax.grid(alpha=.3)
ax.set_xlabel("tangent-plane x (deg)"); ax.set_ylabel("tangent-plane y (deg)")
ax.set_title("Giant GRB Ring: circle vs. ellipse vs. spiral fits (1-turn arcs)")
plt.savefig("/home/ubuntu/grbring/fits.png", dpi=130, bbox_inches="tight")
print("saved")
