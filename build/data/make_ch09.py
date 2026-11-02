#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""第 9 章插图数据：最速降线（摆线/直线/圆弧）、悬链线与抛物线对比、瑞利商。

运行：  python build/data/make_ch09.py
输出：  build/figs/ch09-01.dat, ch09-03.dat, ch09-06.dat
所有曲线由公式现算，可重复运行；运行时打印正文引用的数值。
"""
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, '..', 'figs'))
G = 9.80665


def save(name, header, cols):
    data = np.column_stack(cols)
    path = os.path.join(OUT, name)
    np.savetxt(path, data, header=' '.join(header), comments='', fmt='%.6e')
    print('  %-16s %4d 行' % (name, len(data)))


# ---------------------------------------------------------------- 图 9.1
def fig01():
    """最速降线对比。y 轴向下，A=(0,0)，B=(x_B,y_B)，单位米。"""
    xB, yB = 1.0, 1.0

    def f(t):
        return (1.0 - np.cos(t)) * xB - yB * (t - np.sin(t))

    lo, hi = 1e-2, np.pi
    assert f(lo) * f(hi) < 0, 'tB 的括号区间里没有变号'
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    tB = 0.5 * (lo + hi)
    a = yB / (1.0 - np.cos(tB))

    t = np.linspace(0.0, tB, 400)
    xc = a * (t - np.sin(t))
    yc = a * (1.0 - np.cos(t))

    xl = np.linspace(0.0, xB, 400)
    yl = yB * xl / xB

    xa = np.linspace(0.0, xB, 400)                     # 圆弧：圆心 (1,0)，半径 1
    ya = np.sqrt(np.maximum(1.0 - (xa - 1.0) ** 2, 0.0))

    # 时间：摆线用解析式，直线用解析式，圆弧用 u^2 替换去掉端点奇性
    T_cyc = tB * np.sqrt(a / G)
    slope = yB / xB
    T_line = 2.0 * np.sqrt(1.0 + slope ** 2) / np.sqrt(2.0 * G * slope) * np.sqrt(xB)
    u = np.linspace(1e-6, np.sqrt(np.pi / 2), 400001)
    T_arc = np.trapezoid(2.0 * u / np.sqrt(2.0 * G * np.sin(u ** 2)), u)

    s_cyc = 4.0 * a * (1.0 - np.cos(tB / 2.0))
    print('  摆线：theta_B=%.4f, a=%.4f m, 弧长=%.4f m, T=%.4f s' % (tB, a, s_cyc, T_cyc))
    print('  直线：T=%.4f s（慢 %.1f%%）' % (T_line, 100 * (T_line / T_cyc - 1)))
    print('  圆弧：T=%.4f s（慢 %.1f%%）' % (T_arc, 100 * (T_arc / T_cyc - 1)))
    print('  摆线终点：x=%.4f y=%.4f（应等于 1,1）' % (xc[-1], yc[-1]))

    save('ch09-01.dat', ['x', 'yc', 'yl', 'ya'], [xc, yc, yl, ya])


# ---------------------------------------------------------------- 图 9.2
def fig02():
    """跨度 10 m、垂度 2 m：悬链线与同端点同垂度的抛物线。"""
    half, sag = 5.0, 2.0

    def g(a):
        return a * (np.cosh(half / a) - 1.0) - sag

    lo, hi = 0.5, 500.0
    assert g(lo) * g(hi) < 0
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if g(mid) > 0:
            lo = mid
        else:
            hi = mid
    a = 0.5 * (lo + hi)
    x = np.linspace(-half, half, 401)
    ycat = a * np.cosh(x / a) - a
    ypar = sag * (x / half) ** 2
    d = np.abs(ycat - ypar)
    s_cat = 2.0 * a * np.sinh(half / a)
    s_par = np.trapezoid(np.sqrt(1.0 + (2.0 * sag * x / half ** 2) ** 2), x)
    print('  悬链线：a=%.4f m，弧长=%.4f m' % (a, s_cat))
    print('  抛物线：弧长=%.4f m，与悬链线最大差 %.1f mm（在 x=%.2f m 处）'
          % (s_par, 1000 * d.max(), x[np.argmax(d)]))
    # 第三条：把差放大 20 倍，画在 y=0.5 这条零线上，用来看出差的形状
    save('ch09-03.dat', ['x', 'ycat', 'ypar', 'd20'],
         [x, ycat, ypar, 0.5 + 20.0 * (ycat - ypar)])


# ---------------------------------------------------------------- 图 9.4
def fig04():
    """弦的瑞利商：L=T=rho=1，精确值 pi^2。单参数族 y=x(1-x)(1+a sin pi x)。"""
    pip = np.pi ** 2
    a = np.linspace(-0.4, 1.0, 281)
    x = np.linspace(0.0, 1.0, 20001)
    R = np.zeros_like(a)
    for i, ai in enumerate(a):
        y = x * (1 - x) * (1 + ai * np.sin(np.pi * x))
        dy = np.gradient(y, x)
        R[i] = np.trapezoid(dy ** 2, x) / np.trapezoid(y ** 2, x)
    k = np.argmin(R)
    print('  抛物试探 a=0：R=%.4f（精确 %.4f，高 %.2f%%）'
          % (R[np.argmin(np.abs(a))], pip, 100 * (R[np.argmin(np.abs(a))] / pip - 1)))
    print('  单参数族最优：a*=%.3f，R=%.4f（高 %.4f%%）' % (a[k], R[k], 100 * (R[k] / pip - 1)))
    print('  族内任何 a 都有 R>=pi^2：%s' % np.all(R >= pip - 1e-9))
    save('ch09-06.dat', ['a', 'R'], [a, R])


def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    print('生成第 9 章插图数据 ->', OUT)
    fig01()
    fig02()
    fig04()
    print('完成。')


if __name__ == '__main__':
    main()
