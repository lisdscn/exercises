# -*- coding: utf-8 -*-
"""生成 Applied Combinatorics 第 5 章 HW3 题解的配图（SVG）。

坐标直接取自课本页面 SVG 的几何数据，因此图形与教材一致。
运行：python make_figs.py
"""
from pathlib import Path
import math

OUT = Path(r"c:\Users\21981\OneDrive\文档\GitHub\exercises\组合数学\figs")
OUT.mkdir(parents=True, exist_ok=True)

SERIF = "Georgia, 'Times New Roman', serif"
INK = "#38424f"
TXT = "#1a1a1a"
C1 = "#cfe3f7"   # 颜色 1 / 房间 1 / 节次 1
C2 = "#fbd6d6"   # 颜色 2
C3 = "#d6f0d0"   # 颜色 3
C4 = "#f7e8b8"   # 颜色 4
HL = "#c0392b"   # 高亮（K4、加边）


def head(w, h, vb):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{vb}" '
            f'font-family="{SERIF}">'
            f'<rect x="-300" y="-300" width="3000" height="3000" fill="#ffffff"/>')


def edge(p, q, r=0.0, color=INK, w=1.7, dash=None):
    x1, y1 = p
    x2, y2 = q
    if r:
        d = math.hypot(x2 - x1, y2 - y1)
        if d > 2 * r + 1:
            ux, uy = (x2 - x1) / d, (y2 - y1) / d
            x1, y1, x2, y2 = x1 + ux * r, y1 + uy * r, x2 - ux * r, y2 - uy * r
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
            f'stroke="{color}" stroke-width="{w}" stroke-linecap="round"{da}/>')


def node(p, r=7.5, fill="#fdf0d5", stroke=INK, w=1.7):
    return (f'<circle cx="{p[0]}" cy="{p[1]}" r="{r}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{w}"/>')


def txt(p, s, fs=14, anchor="start", fill=TXT, italic=True, bold=False):
    st = ' font-style="italic"' if italic else ''
    wt = ' font-weight="bold"' if bold else ''
    return (f'<text x="{p[0]:.2f}" y="{p[1]:.2f}" font-size="{fs}" fill="{fill}" '
            f'text-anchor="{anchor}"{st}{wt}>{s}</text>')


def sub(p, main, idx, fs=14, fill=TXT):
    return (f'<text x="{p[0]:.2f}" y="{p[1]:.2f}" font-size="{fs}" fill="{fill}" font-style="italic">'
            f'{main}<tspan dy="{fs * 0.26:.1f}" font-size="{fs * 0.68:.1f}">{idx}</tspan></text>')


def build(name, vb, scale, body):
    x, y, w, h = [float(v) for v in vb.split()]
    W, H = round(w * scale), round(h * scale)
    svg = head(W, H, vb) + "".join(body) + "</svg>"
    p = OUT / name
    p.write_text(svg, encoding="utf-8")
    print(f"{name:24s} {W}x{H}  {len(svg)} bytes")


def draw(name, vb, scale, pos, edges, labels, r=7.5, fs=14, fill="#fdf0d5",
         colors=None, thick=(), ewidth=1.7, ecolor=INK, extra=(), sub_idx=None):
    body = []
    for a, b in edges:
        col = HL if (a, b) in thick or (b, a) in thick else ecolor
        wd = 3.0 if (a, b) in thick or (b, a) in thick else ewidth
        body.append(edge(pos[a], pos[b], r=r, color=col, w=wd))
    for lb, xy in pos.items():
        body.append(node(xy, r=r, fill=(colors or {}).get(lb, fill)))
    for lb, xy in labels.items():
        if sub_idx and lb in sub_idx:
            body.append(sub(xy, lb, sub_idx[lb], fs=fs))
        else:
            body.append(txt(xy, lb, fs=fs))
    body.extend(extra)
    build(name, vb, scale, body)


# ---------------------------------------------------------------- 图 5.49
P49 = {
    'v1': (24.8, 25.9), 'v2': (51.9, 25.2), 'v3': (78.6, 25.9),
    'v4': (24.6, 57.9), 'v5': (52.0, 57.6), 'v6': (79.1, 58.2),
    'u1': (113.4, 13.0), 'u2': (142.1, 13.1), 'u3': (155.1, 38.1),
    'u4': (141.9, 62.0), 'u5': (113.4, 63.0), 'u6': (98.1, 37.6),
    'w1': (36.0, 91.6), 'w2': (64.7, 91.7), 'w3': (77.7, 116.7),
    'w4': (64.5, 140.6), 'w5': (36.0, 141.6), 'w6': (20.7, 116.2),
    'x1': (101.1, 97.1), 'x2': (128.2, 97.4), 'x3': (155.0, 97.1),
    'x4': (101.0, 129.1), 'x5': (128.4, 128.8), 'x6': (155.5, 129.4),
}
E49 = [
    ('v1', 'v4'), ('v1', 'v5'), ('v2', 'v3'), ('v2', 'v4'), ('v2', 'v6'), ('v3', 'v6'), ('v5', 'v6'),
    ('u1', 'u2'), ('u2', 'u3'), ('u3', 'u4'), ('u4', 'u5'), ('u5', 'u6'), ('u6', 'u1'), ('u3', 'u6'),
    ('w1', 'w2'), ('w2', 'w3'), ('w3', 'w4'), ('w4', 'w5'), ('w5', 'w6'), ('w6', 'w1'), ('w3', 'w5'),
    ('x1', 'x4'), ('x4', 'x6'), ('x6', 'x3'), ('x3', 'x5'), ('x5', 'x2'), ('x2', 'x1'),
]
L49 = {
    'v1': (17.8, 19.4), 'v2': (44.2, 19.4), 'v3': (72.1, 19.4),
    'v4': (17.8, 67.8), 'v5': (44.2, 67.8), 'v6': (72.1, 67.8),
    'u1': (104.4, 6.1), 'u2': (135.3, 6.1), 'u3': (155.6, 40.9),
    'u4': (142.6, 66.4), 'u5': (94.6, 66.4), 'u6': (87.0, 28.5),
    'w1': (26.6, 86.9), 'w2': (58.2, 86.9), 'w3': (79.6, 118.6),
    'w4': (66.2, 142.7), 'w5': (14.4, 145.2), 'w6': (0.9, 116.3),
    'x1': (94.2, 90.9), 'x2': (120.6, 90.9), 'x3': (147.0, 90.9),
    'x4': (94.2, 139.8), 'x5': (120.6, 139.8), 'x6': (147.0, 139.8),
}
IDX49 = {k: k[1] for k in L49}

body = []
for a, b in E49:
    # G1 ≅ G3：把这两张图的边画成同色以示配对
    col = "#2c6fbb" if a[0] in 'vw' else INK
    body.append(edge(P49[a], P49[b], r=4.2, color=col, w=1.5))
for lb, xy in P49.items():
    body.append(node(xy, r=4.2, fill=("#dceaf9" if lb[0] in 'vw' else "#fdf0d5")))
for lb, xy in L49.items():
    body.append(sub(xy, lb[0], lb[1], fs=7.6))
for cap, xy in [('1', (44.2, 78.1)), ('2', (120.6, 78.1)), ('3', (44.2, 160.0)), ('4', (120.6, 160.0))]:
    body.append(txt(xy, 'G', fs=8.6, italic=False, bold=True))
    body.append(txt((xy[0] + 6.2, xy[1] + 1.6), cap, fs=6.2, italic=False, bold=True))
build("fig_5_49.svg", "-6 -8 184 180", 3.9, body)

# ---------------------------------------------------------------- 图 5.51
P51 = {'a': (49.1, 43.0), 'b': (7.8, 95.0), 'c': (203.8, 71.5), 'd': (94.5, 155.0),
       'e': (91.8, 20.4), 'f': (166.8, 31.9), 'g': (214.5, 199.5), 'h': (161.1, 206.2),
       'i': (174.5, 164.4), 'j': (135.8, 117.7), 'k': (99.8, 77.7), 'l': (62.5, 128.9),
       'm': (242.5, 123.5), 'n': (278.8, 178.5)}
E51 = [('a', 'b'), ('a', 'e'), ('a', 'k'), ('a', 'l'), ('b', 'l'), ('c', 'f'), ('c', 'i'), ('c', 'j'),
       ('c', 'm'), ('d', 'h'), ('d', 'i'), ('d', 'j'), ('d', 'l'), ('e', 'f'), ('f', 'i'), ('f', 'k'),
       ('g', 'm'), ('g', 'n'), ('h', 'm'), ('i', 'm'), ('j', 'l'), ('j', 'm'), ('m', 'n')]
L51 = {'a': (29.2, 45.7), 'b': (0.5, 116.5), 'c': (214.0, 76.5), 'd': (78.0, 173.0),
       'e': (88.5, 11.5), 'f': (175.5, 26.5), 'g': (208.0, 218.5), 'h': (140.0, 222.0),
       'i': (158.0, 160.0), 'j': (126.0, 109.5), 'k': (98.0, 66.5), 'l': (38.0, 140.5),
       'm': (255.0, 133.0), 'n': (276.5, 196.5)}
draw("fig_5_51.svg", "-12 -6 312 248", 2.5, P51, E51, L51, r=8.0, fs=15.0)

# 图 5.51 + 欧拉回路编号
EULER51 = ['a', 'b', 'l', 'd', 'h', 'm', 'n', 'g', 'm', 'c', 'f', 'e',
           'a', 'k', 'f', 'i', 'd', 'j', 'c', 'i', 'm', 'j', 'l', 'a']
body = [edge(P51[x], P51[y], r=8.0) for x, y in E51]
for lb, xy in P51.items():
    body.append(node(xy, r=8.0))
for lb, xy in L51.items():
    body.append(txt(xy, lb, fs=15.0))
for no, (x, y) in enumerate(zip(EULER51[:-1], EULER51[1:]), 1):
    (x1, y1), (x2, y2) = P51[x], P51[y]
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    d = math.hypot(x2 - x1, y2 - y1) or 1
    ox, oy = -(y2 - y1) / d * 7, (x2 - x1) / d * 7
    body.append(txt((mx + ox, my + oy + 3.0), str(no), fs=9.5, anchor="middle",
                    italic=False, fill=HL))
build("fig_5_51_euler.svg", "-12 -6 312 248", 2.5, body)

# ---------------------------------------------------------------- 图 5.52
P52 = {'1': (25.1, 49.0), '2': (201.3, 95.5), '3': (136.0, 63.9), '4': (184.1, 20.8),
       '5': (17.0, 92.3), '6': (60.4, 41.2), '7': (77.9, 73.3), '8': (127.2, 96.7),
       '9': (234.6, 79.0), '10': (93.7, 15.2), '11': (198.3, 36.9), '12': (181.6, 65.8)}
E52 = [('10', '9'), ('8', '10'), ('8', '9'), ('5', '1'), ('1', '6'), ('5', '7'), ('5', '8'),
       ('7', '10'), ('6', '4'), ('4', '12'), ('12', '3'), ('9', '2'), ('2', '12'), ('12', '8'),
       ('3', '7'), ('7', '11'), ('11', '10'), ('9', '12')]
L52 = {'1': (8.0, 53.0), '2': (185.5, 101.0), '3': (129.0, 77.5), '4': (175.0, 14.0),
       '5': (-0.5, 98.0), '6': (51.0, 34.0), '7': (61.5, 72.5), '8': (119.5, 112.5),
       '9': (237.0, 83.0), '10': (82.5, 8.0), '11': (204.5, 42.5), '12': (166.0, 80.5)}

body = [edge(P52[x], P52[y], r=7.5, color=(HL if {x, y} == {'5', '12'} else INK),
             w=(2.6 if {x, y} == {'5', '12'} else 1.7),
             dash=("7 5" if {x, y} == {'5', '12'} else None)) for x, y in E52]
# 奇度顶点用红圈
body.append(edge(P52['5'], P52['12'], r=7.5, color=HL, w=2.6, dash="7 5"))
for lb, xy in P52.items():
    odd = lb in ('5', '12')
    body.append(node(xy, r=7.5, fill=("#fbd6d6" if odd else "#fdf0d5")))
for lb, xy in L52.items():
    body.append(txt(xy, lb, fs=13.5))
body.append(txt((108.0, 55.0), "+ 5-12", fs=13.0, fill=HL, italic=False))
body.append(txt((60.0, 118.0), "odd vertices: 5 (deg 3), 12 (deg 5)", fs=9.6,
                fill=HL, italic=False))
build("fig_5_52.svg", "-22 -14 292 150", 2.7, body)

# ---------------------------------------------------------------- 图 5.53
P53 = {'a': (217.1, 98.6), 'b': (7.6, 55.4), 'c': (203.6, 31.9), 'd': (101.0, 97.9),
       'e': (91.2, 130.1), 'f': (56.6, 73.9), 'g': (29.4, 99.7), 'h': (124.2, 22.7),
       'i': (174.3, 124.7), 'j': (135.6, 78.1)}
E53 = [('b', 'h'), ('b', 'g'), ('g', 'e'), ('e', 'i'), ('i', 'c'), ('c', 'j'), ('j', 'h'),
       ('g', 'f'), ('f', 'd'), ('d', 'e'), ('d', 'a'), ('a', 'c'), ('f', 'h'), ('a', 'h')]
L53 = {'a': (223.0, 104.0), 'b': (2.0, 76.5), 'c': (209.0, 25.5), 'd': (101.0, 88.5),
       'e': (85.0, 147.5), 'f': (47.5, 65.5), 'g': (23.5, 117.5), 'h': (122.0, 14.0),
       'i': (170.0, 144.0), 'j': (138.5, 66.5)}
draw("fig_5_53.svg", "-14 -10 258 172", 2.7, P53, E53, L53, r=7.5, fs=13.5)

COL53 = {'a': C1, 'b': C1, 'e': C1, 'f': C1, 'j': C1,
         'c': C2, 'd': C2, 'h': C2,
         'g': C3, 'i': C3}
body = [edge(P53[x], P53[y], r=7.5) for x, y in E53]
for lb, xy in P53.items():
    body.append(node(xy, r=7.5, fill=COL53[lb]))
for lb, xy in L53.items():
    body.append(txt(xy, lb, fs=13.5))
leg = [("color 1", C1, "{a,b,e,f,j}"), ("color 2", C2, "{c,d,h}"), ("color 3", C3, "{g,i}")]
for k, (nm, col, st) in enumerate(leg):
    yy = 14 + k * 13
    body.append(f'<circle cx="16" cy="{yy - 4}" r="5" fill="{col}" stroke="{INK}" stroke-width="1.3"/>')
    body.append(txt((26, yy), f"color {k + 1}: {st}", fs=10.5, italic=False))
body.append(txt((88, 168), "chi(G) = 3", fs=12.5, italic=False, fill=HL))
build("fig_5_53_color.svg", "-14 -10 258 186", 2.7, body)

# ---------------------------------------------------------------- 5.9.15 化学品冲突图
P15 = {'1': (250, 60), '2': (340, 140), '4': (250, 220), '5': (160, 140),
       '3': (450, 140), '6': (400, 255), '7': (128, 292), '8': (560, 78),
       '9': (560, 215), '10': (480, 300)}
E15 = [('1', '2'), ('2', '4'), ('4', '5'), ('5', '1'), ('1', '4'), ('2', '5'),
       ('1', '7'), ('2', '10'), ('3', '6'), ('3', '8'), ('3', '9'),
       ('5', '9'), ('6', '7'), ('6', '10'), ('7', '8')]
K4 = {('1', '2'), ('2', '4'), ('4', '5'), ('5', '1'), ('1', '4'), ('2', '5')}
L15 = {'1': (238, 52), '2': (352, 132), '4': (238, 236), '5': (140, 132),
       '3': (452, 128), '6': (404, 275), '7': (118, 310), '8': (566, 70),
       '9': (566, 230), '10': (486, 318)}
COL15 = {'1': C1, '8': C1, '9': C1, '10': C1,
         '2': C2, '3': C2,
         '4': C3, '7': C3,
         '5': C4, '6': C4}
body = []
for x, y in E15:
    hi = (x, y) in K4 or (y, x) in K4
    body.append(edge(P15[x], P15[y], r=16, color=(HL if hi else INK), w=(3.0 if hi else 1.8)))
for lb, xy in P15.items():
    body.append(node(xy, r=16, fill=COL15[lb]))
for lb, xy in L15.items():
    body.append(txt(xy, lb, fs=19, italic=False))
leg = [("Room 1", C1, "1, 8, 9, 10"), ("Room 2", C2, "2, 3"),
       ("Room 3", C3, "4, 7"), ("Room 4", C4, "5, 6")]
for k, (nm, col, st) in enumerate(leg):
    xx, yy = 24 + (k % 2) * 250, 344 + (k // 2) * 26
    body.append(f'<rect x="{xx}" y="{yy - 13}" width="18" height="18" rx="9" fill="{col}" stroke="{INK}" stroke-width="1.4"/>')
    body.append(txt((xx + 26, yy + 2), f"{nm}: {st}", fs=14, italic=False))
body.append(txt((24, 34), "conflict graph (red = the K4 on 1,2,4,5)", fs=14, italic=False, fill=HL))
build("fig_5_15.svg", "0 0 620 420", 1.35, body)

# ---------------------------------------------------------------- 5.9.16 课程冲突图
P16 = {'E': (90, 62), 'Y': (300, 92), 'P': (412, 62), 'X': (300, 218),
       'D': (185, 150), 'S': (95, 218), 'C': (276, 150)}
E16 = [('E', 'D'), ('E', 'S'), ('D', 'S'), ('S', 'C'), ('C', 'D'),
       ('Y', 'P'), ('Y', 'X'), ('P', 'X'), ('E', 'Y')]
NAMES = {'E': 'English', 'Y': 'Chemistry', 'P': 'Physics', 'X': 'Economics',
         'D': 'German', 'S': 'Statistics', 'C': 'Calculus'}
COL16 = {'C': C1, 'P': C1, 'E': C1,
         'Y': C2, 'D': C2,
         'S': C3, 'X': C3}
body = [edge(P16[x], P16[y], r=15) for x, y in E16]
for lb, xy in P16.items():
    body.append(node(xy, r=15, fill=COL16[lb]))
    body.append(txt((xy[0], xy[1] + 5.5), lb, fs=16, anchor="middle"))
leg = [("Period 1", C1, "Calculus, Physics, English"), ("Period 2", C2, "Chemistry, German"),
       ("Period 3", C3, "Statistics, Economics")]
for k, (nm, col, st) in enumerate(leg):
    yy = 292 + k * 24
    body.append(f'<rect x="24" y="{yy - 13}" width="18" height="18" rx="9" fill="{col}" stroke="{INK}" stroke-width="1.4"/>')
    body.append(txt((50, yy + 2), f"{k + 1}  {st}", fs=14, italic=False))
body.append(txt((300, 300), "chi = 3", fs=15, italic=False, fill=HL))
body.append(txt((300, 322), "(triangle E-D-S)", fs=11, italic=False, fill="#5a6472"))
build("fig_5_16.svg", "0 0 560 390", 1.45, body)

# ---------------------------------------------------------------- 5.9.2 星形图 K(1,7)
R, CX, CY = 108, 175, 150
P2 = {'c': (CX, CY)}
lab2 = {'c': (CX - 5, CY - 18)}
body = []
for i in range(7):
    ang = -math.pi / 2 + i * 2 * math.pi / 7
    x, y = CX + R * math.cos(ang), CY + R * math.sin(ang)
    P2[f"L{i+1}"] = (x, y)
    k = 1.22
    lab2[f"L{i+1}"] = (CX + R * k * math.cos(ang) - 6, CY + R * k * math.sin(ang) + 5)
    body.append(edge((CX, CY), (x, y), r=13))
for lb, xy in P2.items():
    body.append(node(xy, r=13))
body.append(txt(lab2['c'], 'c', fs=16))
for i in range(7):
    body.append(sub(lab2[f"L{i+1}"], "\u2113", str(i + 1), fs=16))
body.append(txt((175, 296), "K(1,7):  all degrees odd, no path of length 3",
                fs=12, anchor="middle", italic=False))
build("fig_5_9_2.svg", "0 0 350 310", 2.0, body)

print("\n写入目录:", OUT)
