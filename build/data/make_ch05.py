# -*- coding: utf-8 -*-
"""生成第 5 章（点源与响应）插图所需的数据文件。

运行：python build/data/make_ch05.py
输出：build/figs/ch05-01.dat, ch05-03a.dat, ch05-03b.dat,
      ch05-04.dat, ch05-05.dat, ch05-07.dat
每个文件第一行是列名，pgfplots 用 table[x=..., y=...] 读取。
"""
import io
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(HERE)          # build/
FIG = os.path.join(BUILD, 'figs')


def save(name, header, cols):
    path = os.path.join(FIG, name)
    with io.open(path, 'w', encoding='utf-8') as f:
        f.write(' '.join(header) + '\n')
        for row in zip(*cols):
            f.write(' '.join('%.6e' % v for v in row) + '\n')
    print('->', name, len(cols[0]), 'lines')


# ---------------------------------------------------------------- 图 5.1
# 三个宽度不同、面积都为 1 的高斯序列，逼近 delta。
x = np.linspace(-1.2, 1.2, 401)
cols = [x]
for eps in (0.40, 0.20, 0.10):
    cols.append(np.exp(-(x / eps) ** 2) / (math.sqrt(math.pi) * eps))
save('ch05-01.dat', ['x', 'y1', 'y2', 'y3'], cols)

# ---------------------------------------------------------------- 图 5.3
# 一维 Dirichlet Green 函数：精确解 vs 本征函数部分和（L = 1, x' = 0.35）
L = 1.0
xp = 0.35
x = np.linspace(0.0, L, 601)


def g_exact(x, xp, L=1.0):
    lo = np.minimum(x, xp)
    hi = np.maximum(x, xp)
    return -lo * (L - hi) / L


def g_sum(x, xp, N, L=1.0):
    s = np.zeros_like(x)
    for n in range(1, N + 1):
        s += np.sin(n * math.pi * x / L) * math.sin(n * math.pi * xp / L) / n ** 2
    return -(2.0 * L / math.pi ** 2) * s


save('ch05-03a.dat', ['x', 'exact', 's3', 's20'],
     [x, g_exact(x, xp), g_sum(x, xp, 3), g_sum(x, xp, 20)])

# 截断误差随 N 的下降：误差 ~ 1/N（源点处尖角始终抹不平）
Ns = np.unique(np.round(np.logspace(0, 2.3, 60)).astype(int))
err = [np.max(np.abs(g_sum(x, xp, int(N)) - g_exact(x, xp))) for N in Ns]
save('ch05-03b.dat', ['N', 'err'], [Ns.astype(float), np.array(err)])

# ---------------------------------------------------------------- 图 5.4
# 热核随时间的展宽（alpha = 1）
x = np.linspace(-6.0, 6.0, 601)
cols = [x]
for t in (0.5, 2.0, 8.0):
    cols.append(np.exp(-x ** 2 / (4.0 * t)) / math.sqrt(4.0 * math.pi * t))
save('ch05-04.dat', ['x', 'k1', 'k2', 'k3'], cols)

# ---------------------------------------------------------------- 图 5.5
# 同一个方形初值：波动解（左右两个方波）与扩散解（抹平成一个高斯）
x = np.linspace(-3.0, 3.0, 601)
w = 0.2            # 初值半宽
t = 1.0            # 波速取 1，故 t = 1 时两个脉冲在 x = ±1
f0 = np.where(np.abs(x) < w, 1.0, 0.0)
wave = 0.5 * (np.where(np.abs(x - t) < w, 1.0, 0.0)
              + np.where(np.abs(x + t) < w, 1.0, 0.0))
ell = 0.25         # 扩散长度 sqrt(4*alpha*t)
erf = np.vectorize(math.erf)
diff = 0.5 * (erf((x + w) / ell) - erf((x - w) / ell))
save('ch05-05.dat', ['x', 'f0', 'wave', 'diff'], [x, f0, wave, diff])

# ---------------------------------------------------------------- 图 5.7
# 多极展开截断到 l <= L 的相对误差：沿轴向正好是 (a/r)^(L+1)
r = np.logspace(math.log10(1.05), 2.0, 200)
save('ch05-07.dat', ['r', 'e0', 'e1', 'e2'],
     [r, (1.0 / r) ** 1, (1.0 / r) ** 2, (1.0 / r) ** 3])

print('ch05 数据就绪：', FIG)
