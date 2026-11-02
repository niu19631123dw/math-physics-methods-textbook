#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""第 7 章插图数据生成器。重跑即可复现 build/figs/ch07-*.dat。

用法：
    python build/data/make_ch07.py

生成（数据文件编号与图号不是一一对应，以下注明每个数据文件服务于哪张图）：
    ch07-01.dat   儒可夫斯基共形网格（偏心圆 → 翼型）              图 7.1
    ch07-01b.dat  只有翼型轮廓（加粗描边用）                        图 7.1、图 7.2
    ch07-02a.dat  圆柱绕流流线，无环量                              图 7.3 左
    ch07-02b.dat  圆柱绕流流线，环量 2*pi*U*a（beta = 30 度）       图 7.3 右
    ch07-03.dat   翼型绕流流线，环量取库塔值                         图 7.5
    ch07-03c.dat  翼型轮廓（加粗描边用）                             图 7.5
    ch07-04.dat   翼型表面速度：环量 0.85 / 1.00 / 1.15 倍库塔值     图 7.6
    ch07-05.dat   升力系数随攻角（薄翼理论）                         图 7.7

约定：复势 w(z)，复速度 dw/dz = u - i v；环量 Gamma 以逆时针为正。
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(os.path.dirname(HERE), 'figs')

A = 1.0                 # 儒可夫斯基变换 z = zeta + a^2/zeta 里的 a
U = 1.0                 # 远场速度
ZETA0 = -0.10 + 0.09j   # 圆心的偏移（后移 + 上抬，造厚度与弯度）
R = abs(A - ZETA0)      # 圆半径：圆过临界点 zeta = a
ALPHA = np.deg2rad(5.0)  # 来流攻角
THETA_T = np.angle(A - ZETA0)


def gamma_kutta():
    """库塔条件给出的环量：后驻点落在 zeta = a。"""
    return 4 * np.pi * U * R * np.sin(THETA_T - ALPHA)


def save(name, polys, header='x y', nmax=240):
    """若干条折线写成 x y 表，折线之间用 nan nan 分隔。"""
    rows = []
    for p in polys:
        p = np.asarray(p)
        if len(p) < 2:
            continue
        if len(p) > nmax:
            idx = np.linspace(0, len(p) - 1, nmax).astype(int)
            p = p[idx]
        for x, y in p:
            rows.append('%.5f %.5f' % (x, y))
        rows.append('nan nan')
    path = os.path.join(FIGS, name)
    with open(path, 'w') as f:
        f.write(header + '\n')
        f.write('\n'.join(rows) + '\n')
    print('wrote %s  (%d 条)' % (name, len(polys)))


def circle_flow(zeta, zeta0, R, U, alpha, Gamma):
    """圆心 zeta0、半径 R 的圆柱绕流：返回 dw/dzeta。"""
    d = zeta - zeta0
    return (U * (np.exp(-1j * alpha)
                 - (R ** 2) * np.exp(1j * alpha) / d ** 2)
            - 1j * Gamma / (2 * np.pi * d))


def streamline(seed, vel, h=0.004, n=2400, stop_r=0.0, center=0j,
               xlim=(-6.0, 6.0), ylim=(-3.4, 3.4)):
    """RK4 积分 dz/dt = conj(vel(z))，返回折线。"""
    pts = []
    z = seed
    for _ in range(n):
        k1 = np.conj(vel(z))
        k2 = np.conj(vel(z + 0.5 * h * k1))
        k3 = np.conj(vel(z + 0.5 * h * k2))
        k4 = np.conj(vel(z + h * k3))
        z = z + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        pts.append((z.real, z.imag))
        if abs(z - center) < stop_r:
            break
        if not (xlim[0] < z.real < xlim[1] and ylim[0] < z.imag < ylim[1]):
            break
    return np.array(pts)


def jouk(z):
    return z + A ** 2 / z


# ------------------------------------------------------------------ 图 7.1
def fig01():
    polys = []
    # 一族圆（映成绕翼型的闭合曲线）
    for k in (1.0, 1.18, 1.45, 1.85, 2.4):
        th = np.linspace(0, 2 * np.pi, 361)
        w = jouk(ZETA0 + k * R * np.exp(1j * th))
        polys.append(np.column_stack([w.real, w.imag]))
    # 一族从圆心出发的射线（映成与之正交的曲线）
    for ang in np.linspace(0, 2 * np.pi, 13)[:-1]:
        rho = np.linspace(R * 1.002, R * 2.4, 160)
        w = jouk(ZETA0 + rho * np.exp(1j * ang))
        polys.append(np.column_stack([w.real, w.imag]))
    save('ch07-01.dat', polys)
    save('ch07-01b.dat', [polys[0]], nmax=400)


# ------------------------------------------------------------------ 图 7.2
def fig02():
    for name, Gamma in (('ch07-02a.dat', 0.0),
                        ('ch07-02b.dat', 2 * np.pi * U * A)):
        vel = lambda z, G=Gamma: circle_flow(z, 0j, A, U, 0.0, G)
        polys = []
        for y0 in np.linspace(-2.4, 2.4, 13):
            polys.append(streamline(-3.2 + 1j * y0, vel, h=0.004, n=2200,
                                    stop_r=A * 1.001))
        save(name, polys)


# ------------------------------------------------------------------ 图 7.3
def fig03():
    cir = ZETA0 + R * np.exp(1j * np.linspace(0, 2 * np.pi, 361))
    af = jouk(cir)
    save('ch07-03c.dat', [np.column_stack([af.real, af.imag])], nmax=400)

    GK = gamma_kutta()
    vel = lambda z: circle_flow(z, ZETA0, R, U, ALPHA, GK)
    polys = []
    for y0 in np.linspace(-1.55, 1.55, 19):
        s0 = (ZETA0.real - 3.0) + 1j * (ZETA0.imag + y0)
        c = streamline(s0, vel, h=0.003, n=2600, stop_r=R * 1.001,
                       center=ZETA0)
        if len(c) > 3:
            w = jouk(c[:, 0] + 1j * c[:, 1])
            polys.append(np.column_stack([w.real, w.imag]))
    save('ch07-03.dat', polys)


# ------------------------------------------------------------------ 图 7.4
def fig04():
    GK = gamma_kutta()
    th = np.linspace(0, 2 * np.pi, 1441)
    zeta = ZETA0 + R * np.exp(1j * th)
    dzdz = 1 - A ** 2 / zeta ** 2
    cols = [np.rad2deg(th)]
    for frac in (0.85, 1.00, 1.15):
        Wp = circle_flow(zeta, ZETA0, R, U, ALPHA, frac * GK)
        cols.append(np.clip(np.abs(Wp / dzdz) / U, 0.0, 30.0))
    data = np.column_stack(cols)
    np.savetxt(os.path.join(FIGS, 'ch07-04.dat'), data, fmt='%.5f',
               header='th v1 v2 v3', comments='')
    print('wrote ch07-04.dat  (%d 行)' % data.shape[0])
    print('  库塔值 Gamma_K/U = %.4f，theta_T = %.2f deg'
          % (GK / U, np.rad2deg(THETA_T)))


# ------------------------------------------------------------------ 图 7.5
def fig05():
    alpha0 = np.deg2rad(3.2)
    al = np.linspace(-8.0, 16.0, 49)
    CL = 2 * np.pi * np.sin(np.deg2rad(al) + alpha0)
    np.savetxt(os.path.join(FIGS, 'ch07-05.dat'),
               np.column_stack([al, CL]), fmt='%.5f',
               header='al CL', comments='')
    print('wrote ch07-05.dat')


if __name__ == '__main__':
    fig01()
    fig02()
    fig03()
    fig04()
    fig05()
