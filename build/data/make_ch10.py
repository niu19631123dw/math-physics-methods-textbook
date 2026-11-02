#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""生成第 10 章的数据图：水星轨道的近日点进动。

真实的水星每圈只进动 5.02e-7 rad（约 0.10 角秒），
400 圈才累积到 43 角秒，画在图上完全看不出来。
所以这张图把进动率放大到每圈约 10.8 度，图注里必须写明「已放大」。

轨道：r = p / (1 + e cos psi)，psi = (1 - eps) * phi
  - psi 从 0 增加 2*pi 时，phi 只增加了 2*pi/(1-eps)，
    所以下一圈的近日点比上一圈多转了 2*pi*eps/(1-eps)；
  - 取 eps = 0.03，每圈进动约 0.1885 rad = 10.8 度。

水星真实参数：e = 0.2056，p = a(1-e^2)，a = 0.387 AU。
这里取 a = 1（长度单位任意），只画形状。

输出 build/figs/ch10-07.dat，列名 x y；另附 peri.dat 标出各圈近日点。
"""
import os

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'figs', 'ch10-07.dat')
PERI = os.path.join(ROOT, 'figs', 'ch10-07-peri.dat')

E = 0.2056
EPS = 0.03
A = 1.0
P = A * (1.0 - E * E)
N_ORBIT = 3
N_PT = 900


def main():
    phi = np.linspace(0.0, N_ORBIT * 2 * np.pi / (1 - EPS), N_PT)
    psi = (1 - EPS) * phi
    r = P / (1 + E * np.cos(psi))
    x, y = r * np.cos(phi), r * np.sin(phi)
    with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('x y\n')
        for xi, yi in zip(x, y):
            f.write('%.6f %.6f\n' % (xi, yi))
    # 每圈近日点
    peri = []
    for k in range(N_ORBIT):
        ph = 2 * np.pi * k / (1 - EPS)
        rr = P / (1 + E)
        peri.append((rr * np.cos(ph), rr * np.sin(ph)))
    with open(PERI, 'w', encoding='utf-8', newline='\n') as f:
        f.write('px py\n')
        for xi, yi in peri:
            f.write('%.6f %.6f\n' % (xi, yi))
    print('写入 %s（%d 点）；近日点 %d 个' % (OUT, N_PT, len(peri)))
    print('每圈进动 %.4f rad = %.2f 度（真实值 5.02e-7 rad，已放大 %.0f 倍）'
          % (2 * np.pi * EPS / (1 - EPS),
             2 * np.pi * EPS / (1 - EPS) * 180 / np.pi,
             2 * np.pi * EPS / (1 - EPS) / 5.02e-7))


if __name__ == '__main__':
    main()
