# -*- coding: utf-8 -*-
import numpy as np, os, io

os.makedirs('figs', exist_ok=True)

# ---- Gibbs: 方波部分和 ----
x = np.linspace(-np.pi, np.pi, 1200)
for N in (5, 25, 100):
    y = np.zeros_like(x)
    for k in range(1, N + 1, 2):
        y += (4.0 / (np.pi * k)) * np.sin(k * x)
    with io.open('figs/gibbs_%d.dat' % N, 'w', encoding='utf-8') as f:
        for a, b in zip(x, y):
            f.write('%.5f %.5f\n' % (a, b))

# ---- Joukowski 翼型 ----
a = 1.0
zx, zy = -0.12, 0.10          # 圆心偏移
R = np.hypot(a - zx, 0 - zy)  # 经过后缘 zeta = a
th = np.linspace(0, 2 * np.pi, 900)
eta = zx + R * np.cos(th)
xi = zy + R * np.sin(th)
zeta = eta + 1j * xi
z = zeta + a**2 / zeta
with io.open('figs/joukowski.dat', 'w', encoding='utf-8') as f:
    for xx, yy in zip(z.real, z.imag):
        f.write('%.5f %.5f\n' % (xx, yy))

print('figs data ok')
