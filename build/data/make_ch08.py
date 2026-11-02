# -*- coding: utf-8 -*-
"""第 8 章（分解与因果：傅里叶与拉普拉斯变换）插图数据生成。

运行：python build/data/make_ch08.py
输出：build/figs/ch08-0*.dat
"""
import io
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(HERE)
FIGS = os.path.join(BUILD, 'figs')
os.makedirs(FIGS, exist_ok=True)


def J1(x):
    """第一类贝塞尔函数 J_1，幂级数（艾里斑要用）。"""
    x = float(x)
    if x == 0.0:
        return 0.0
    half = x / 2.0
    term = half
    s = term
    k = 0
    while abs(term) > 1e-16 * max(abs(s), 1e-30) and k < 200:
        k += 1
        term *= -(half * half) / (k * (k + 1))
        s += term
    return s


assert abs(J1(1.0) - 0.4400505857) < 1e-9


def save(name, header, cols):
    path = os.path.join(FIGS, name)
    data = np.column_stack(cols)
    np.savetxt(path, data, fmt='%.6e', header=header, comments='')
    print('  %-14s %5d 行' % (name, len(data)))


print('[第 8 章] 生成插图数据：')

# ---- ch08-01a/b/c：方波脉冲的傅里叶系数，周期 L 越大谱线越密 -------
a = 0.5                                   # 脉冲宽度
for tag, L in (('a', 2.0), ('b', 4.0), ('c', 8.0)):
    n = np.arange(-40, 41)
    k = 2 * np.pi * n / L
    cn = (a / L) * np.sinc(k * a / (2 * np.pi))
    keep = np.abs(k) <= 10
    save('ch08-01%s.dat' % tag, 'k Lcn', [k[keep], (L * cn)[keep]])

# 连续谱的包络（用于同图对照）
k = np.linspace(-10, 10, 801)
save('ch08-01d.dat', 'k env', [k, a * np.sinc(k * a / (2 * np.pi))])

# ---- ch08-02：矩形脉冲 / 高斯脉冲，及其频谱 -------------------------
x = np.linspace(-3, 3, 601)
rect = np.where(np.abs(x) <= 0.5, 1.0, 0.0)
sig = 0.25
gauss = np.exp(-x ** 2 / (2 * sig ** 2))
kk = np.linspace(-20, 20, 1201)
spec_rect = 1.0 * np.sinc(kk * 1.0 / (2 * np.pi))      # ∫_{-1/2}^{1/2} e^{-ikx}dx
spec_gauss = sig * np.sqrt(2 * np.pi) * np.exp(-sig ** 2 * kk ** 2 / 2)
save('ch08-02.dat', 'x rect gauss',
     [x, rect, gauss])
save('ch08-02k.dat', 'k rect gauss', [kk, spec_rect, spec_gauss / spec_gauss.max()])

# ---- ch08-03：高斯波包在色散介质中的展宽 ----------------------------
xs = np.linspace(-8, 8, 801)
for tag, t in (('a', 0.0), ('b', 2.0), ('c', 5.0)):
    s0 = 1.0
    s = s0 * np.sqrt(1 + (t / 3.0) ** 2)               # 宽度随时间增长
    env = np.exp(-xs ** 2 / (2 * s ** 2)) / s
    save('ch08-03%s.dat' % tag, 'x env', [xs, env])

# ---- ch08-04：三种极点位置对应的时域响应 ----------------------------
tt = np.linspace(0, 6, 601)
gam = 0.5
save('ch08-04.dat', 't decay const grow',
     [tt, np.exp(-gam * tt), np.ones_like(tt), np.exp(0.35 * tt)])

# ---- ch08-05：单缝 sinc^2 与圆孔艾里斑 ------------------------------
u = np.linspace(0.001, 3.2, 801)                       # u = sinθ/(λ/a)
I_single = (np.sin(np.pi * u) / (np.pi * u)) ** 2
vv = np.pi * 1.22 * u                                  # x = πD sinθ/λ
I_circ = (2 * np.array([J1(t) for t in vv]) / vv) ** 2
db = lambda y: np.maximum(10 * np.log10(np.maximum(y, 1e-9)), -60)
save('ch08-05.dat', 'u single circ', [u, db(I_single), db(I_circ)])

# ---- ch08-06：RC 低通的幅频与相频 ----------------------------------
f = np.logspace(-2, 2, 401)                            # f/f_c
H = 1.0 / (1 + 1j * f)
save('ch08-06.dat', 'f mag phase',
     [f, 20 * np.log10(np.abs(H)), np.angle(H) * 180 / np.pi])

# ---- 正文要用的数 ---------------------------------------------------
print('\n[带宽]')
c = 3e8
for dt, lam in ((10e-15, 800e-9), (100e-15, 800e-9), (1e-12, 1.55e-6)):
    dnu = 0.441 / dt
    print('  Δt=%.0f fs, λ=%.0f nm -> Δν=%.3g THz, Δλ=%.1f nm' %
          (dt * 1e15, lam * 1e9, dnu / 1e12, lam ** 2 / c * dnu * 1e9))

print('\n[衍射]')
for D, lam, dist in ((5e-3, 550e-9, 10.0), (0.1, 550e-9, 1.0), (2.4e-3, 550e-9, 1.0)):
    th = 1.22 * lam / D
    print('  D=%.2g m, λ=%.0f nm -> θ=%.3g rad, 在 %.1f m 处 %.3g m' %
          (D, lam * 1e9, th, dist, th * dist))

print('\n[RC]')
for RC in (1e-3, 1e-6):
    print('  RC=%.0e s -> f_c=%.3g Hz, t_r(10-90%%)=%.3g s' % (RC, 1 / (2 * np.pi * RC), 2.197 * RC))

print('\nok')
