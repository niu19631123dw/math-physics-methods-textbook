#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""第 1 章插图数据生成器。重跑即可复现 build/figs/ch01-*.dat。

用法：
    python build/data/make_ch01.py

生成：
    ch01-02.dat  d'Alembert：三角形初值分裂成两个半高三角（图 1.2）
    ch01-04.dat  行波 vs 驻波的能量密度（图 1.4）
    ch01-05.dat  固定端 / 自由端反射（图 1.5）
    ch01-07.dat  刚度引起的非谐性 f_n/(n f_1) 对 n（图 1.7）
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(os.path.dirname(HERE), 'figs')


def save(name, header, cols):
    path = os.path.join(FIGS, name)
    data = np.column_stack(cols)
    np.savetxt(path, data, fmt='%.6f', header=header, comments='')
    print('wrote %s  (%d 行)' % (path, data.shape[0]))


def tri(x, xc, a):
    """顶点在 xc、半宽 a、峰高 1 的三角脉冲。"""
    return np.clip(1.0 - np.abs(x - xc) / a, 0.0, None)


# ---------------------------------------------------------------- 图 1.2
# 三角形初值（峰高 1，顶点 x=3，半宽 1.8）在 t=0 后分裂成两个半高的三角，
# 分别以 c 左右跑。t 用 ct 计量。
x = np.linspace(0.0, 7.0, 281)
u0 = tri(x, 3.0, 1.8)
cols = [x, u0]
for ct in (0.8, 1.6):
    cols.append(0.5 * tri(x - ct, 3.0, 1.8) + 0.5 * tri(x + ct, 3.0, 1.8))
save('ch01-02.dat', 'x u0 u1 u2', cols)

# ---------------------------------------------------------------- 图 1.4
# 左：右行波 u = exp(-(x-ct)^2/w^2)。动能密度 = 势能密度，两者重合。
# 右：驻波 u = sin(kx)cos(wt)，取 wt=pi/4，ek ∝ sin^2、ep ∝ cos^2，空间互补。
x = np.linspace(0.0, 6.0, 401)
w = 0.5
s = x - 3.0
F = np.exp(-s ** 2 / w ** 2)
Fp = -2.0 * s / w ** 2 * F          # du/dx
ek_t = 0.5 * Fp ** 2
ep_t = ek_t.copy()                   # 行波：ek = ep
ek_t /= ek_t.max()
ep_t /= ep_t.max()
u_t = F / F.max()

k = np.pi / 3.0
u_s = np.sin(k * x)                  # 已取 cos(wt)=sqrt(1/2) 的公因子
ek_s = np.sin(k * x) ** 2
ep_s = np.cos(k * x) ** 2
save('ch01-04.dat', 'x ut ekt ept us eks eps',
     [x, u_t, ek_t, ep_t, u_s, ek_s, ep_s])

# ---------------------------------------------------------------- 图 1.5
# 左：固定端 u = F(x+ct-x0) - F(-x+ct-x0)；右：自由端取 +。
# 入射脉冲中心 x0=4，宽 w；三个时刻：入射 / 到达墙面 / 反射之后。
x = np.linspace(0.0, 7.0, 401)
w, x0 = 0.7, 4.0
times = (1.6, 4.0, 6.4)
cols = [x]
for ct in times:
    cols.append(np.exp(-(x + ct - x0) ** 2 / w ** 2)
                - np.exp(-(-x + ct - x0) ** 2 / w ** 2))
for ct in times:
    cols.append(np.exp(-(x + ct - x0) ** 2 / w ** 2)
                + np.exp(-(-x + ct - x0) ** 2 / w ** 2))
save('ch01-06.dat', 'x f1 f2 f3 g1 g2 g3', cols)

# ---------------------------------------------------------------- 图 1.7
# 有弯曲刚度的弦：f_n = n f_1 sqrt(1 + B n^2)。
n = np.arange(1, 17)
cols = [n.astype(float)]
for B in (0.0, 1e-4, 3.3e-4, 1e-3):
    cols.append(np.sqrt(1.0 + B * n.astype(float) ** 2))
save('ch01-07.dat', 'n b0 b1 b2 b3', cols)
