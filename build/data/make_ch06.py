#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""生成第 6 章的数据图：Lorentz 振子的介电极化率实部与虚部。

物理量：单振子（振子强度 omega_p^2、共振频率 omega_0、阻尼 gamma）的极化率

    chi(omega) = omega_p^2 / (omega_0^2 - omega^2 - i gamma omega)

无量纲化：横轴 x = omega/omega_0，纵轴 chi/chi_st，其中 chi_st = omega_p^2/omega_0^2
是静态极化率。于是

    Re chi/chi_st = (1 - x^2) / ((1 - x^2)^2 + (gamma/omega_0)^2 x^2)
    Im chi/chi_st = (gamma/omega_0) x / ((1 - x^2)^2 + (gamma/omega_0)^2 x^2)

取 gamma/omega_0 = 0.5（峰高 = 2，便于作图；真实原子跃迁线宽约 10^-7，
峰高约 10^7，无法与横轴同图）。

输出 build/figs/ch06-06.dat，列名 w re im。
脚本可重复运行：不依赖任何外部数据。
"""
import os

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'figs', 'ch06-06.dat')

GAMMA = 0.5          # gamma/omega_0
XMIN, XMAX, N = 0.0, 2.6, 521


def chi(x):
    """返回 (Re chi/chi_st, Im chi/chi_st)。"""
    d = (1.0 - x * x) ** 2 + (GAMMA * x) ** 2
    re = (1.0 - x * x) / d
    im = GAMMA * x / d
    return re, im


def main():
    x = np.linspace(XMIN, XMAX, N)
    re, im = chi(x)
    with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('w re im\n')
        for xi, ri, ii in zip(x, re, im):
            f.write('%.6f %.6f %.6f\n' % (xi, ri, ii))
    print('写入 %s：%d 行' % (OUT, N))
    print('Re chi 范围 [%.3f, %.3f]，Im chi 峰值 %.3f（在 x=%.3f）'
          % (re.min(), re.max(), im.max(), x[np.argmax(im)]))
    # 供作图时核对：Im 峰高按解析式应为 2（x=1 处）
    print('x=1 处：Re = %.3f，Im = %.3f' % (chi(np.array([1.0]))[0][0],
                                            chi(np.array([1.0]))[1][0]))


if __name__ == '__main__':
    main()
