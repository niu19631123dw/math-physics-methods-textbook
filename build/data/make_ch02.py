#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""第 2 章插图数据 + 正文数值核对。

运行：python build/data/make_ch02.py
输出：build/figs/ch02-0*.dat （pgfplots 直接读）
      stdout 里的核对报告（正文与例题引用的数字都出自这里）
"""
import numpy as np

L = 1.0                     # 弦长，全部无量纲化：x/L
OUT = 'build/figs/'


def write(name, header, cols):
    a = np.column_stack(cols)
    np.savetxt(OUT + name, a, header=header, comments='', fmt='%.6e')


# ---------------------------------------------------------------- 图 2.3 方波
def gen_square():
    """f=1 在 (0,L) 上的奇延拓（跳变在 x=0 与 x=L），正弦级数 a_n=4/(n pi)（n 奇）。"""
    x = np.linspace(0, 1, 3001)
    cols = [x]
    for N in (1, 5, 20, 100):
        s = np.zeros_like(x)
        for n in range(1, N + 1, 2):
            s += 4.0 / (n * np.pi) * np.sin(n * np.pi * x)
        cols.append(s)
    write('ch02-03.dat', 'x N1 N5 N20 N100', cols)
    return x


def square_overshoot(N):
    x = np.linspace(0, 0.5, 400001)
    s = np.zeros_like(x)
    for n in range(1, N + 1, 2):
        s += 4.0 / (n * np.pi) * np.sin(n * np.pi * x)
    i = np.argmax(s)
    return x[i], s[i]


# ---------------------------------------------------------------- 图 2.4 三角
def tri(x):
    """等腰三角波：峰 1 在 x=1/2，两端 0；奇延拓后周期 2。"""
    x = np.mod(x, 1.0)
    return np.where(x <= 0.5, 2 * x, 2 * (1 - x))


def tri_partial(x, N):
    s = np.zeros_like(x)
    for n in range(1, N + 1, 2):
        s += 8.0 / (n * np.pi) ** 2 * (-1) ** ((n - 1) // 2) * np.sin(n * np.pi * x)
    return s


def gen_triangle():
    x = np.linspace(0, 1, 3001)
    write('ch02-04a.dat', 'x ex N1 N3 N40',
          [x, tri(x), tri_partial(x, 1), tri_partial(x, 3), tri_partial(x, 40)])
    # 导数级数：角点 x=1/2 两侧有 9% 过冲
    xd = np.linspace(0.30, 0.70, 2001)
    cols = [xd]
    for N in (10, 40, 160):
        s = np.zeros_like(xd)
        for n in range(1, N + 1, 2):
            s += 8.0 / (np.pi * n) * (-1) ** ((n - 1) // 2) * np.cos(n * np.pi * xd)
        cols.append(s)
    write('ch02-04b.dat', 'x N10 N40 N160', cols)
    return x


def tri_overshoot(N):
    x = np.linspace(0.2, 0.8, 400001)
    s = tri_partial(x, N)
    i = np.argmax(s)
    return x[i], s[i] - 1.0


def tri_deriv_peak(N):
    """三角波导数级数在角点附近的极大值（真值 +2）。"""
    x = np.linspace(0.35, 0.499, 400001)
    s = np.zeros_like(x)
    for n in range(1, N + 1, 2):
        s += 8.0 / (np.pi * n) * (-1) ** ((n - 1) // 2) * np.cos(n * np.pi * x)
    i = np.argmax(s)
    return x[i], s[i]


# ------------------------------------------------------------ 图 2.6 共振曲线
def gen_resonance():
    """单模受迫：A = 1/sqrt((1-W^2)^2+(gamma W)^2)，W = Omega/omega_1。"""
    W = np.linspace(0.5, 1.5, 601)
    cols = [W]
    for g in (0.05, 0.15, 0.40):
        cols.append(1.0 / np.sqrt((1 - W ** 2) ** 2 + (g * W) ** 2))
    write('ch02-06.dat', 'W g005 g015 g040', cols)


# -------------------------------------------------------- 图 2.5 受迫弦的空间形状
def gen_forced_shape():
    """一端固定、一端驱动：X(x)=sin(k pi x)/sin(k pi)，k=Omega/omega_1。"""
    x = np.linspace(0, 1, 1201)
    cols = [x]
    for k in (0.5, 0.9, 1.5):
        cols.append(np.sin(k * np.pi * x) / np.sin(k * np.pi))
    write('ch02-05.dat', 'x k05 k09 k15', cols)


# ------------------------------------------------------------------ 图 2.7 拍
def gen_beats():
    """两个频率比为 1:1.2 的模叠加，横轴以 T_1=2pi/omega_1 为单位。"""
    t = np.linspace(0, 5, 2401)
    y = np.cos(2 * np.pi * t) + np.cos(2 * np.pi * 1.2 * t)
    env = 2 * np.abs(np.cos(2 * np.pi * 0.1 * t))
    write('ch02-07.dat', 't y env', [t, y, env])


# ---------------------------------------------------------------------- 核对
def report():
    p = print
    p('=== 正文/例题数字核对 ===')
    p('Si(pi)=%.6f  2 Si(pi)/pi - 1 = %.6f' % (si(np.pi), 2 / np.pi * si(np.pi) - 1))

    p('\n[吉布斯] 方波 S_N 的过冲（相对半幅 1）')
    for N in (5, 20, 100, 400):
        xm, ym = square_overshoot(N)
        p('  N=%3d  x_max/L=%.5f  S_max=%.5f  偏离=%.4f' % (N, xm, ym, ym - 1))
    p('  N=100 时 x_max*N = %.3f' % (square_overshoot(100)[0] * 100))

    p('\n[吉布斯] 方波中点 S_N(0.5) 的误差（真值 1）')
    for N in (5, 21, 51, 127):
        s = sum(4.0 / (n * np.pi) * np.sin(n * np.pi * 0.5)
                for n in range(1, N + 1, 2))
        p('  N=%3d  S=%.5f  误差=%.2f%%' % (N, s, 100 * abs(s - 1)))

    p('\n[吉布斯] 三角波（导数跳变）在角点 x=L/2 的函数值误差（真值 1）')
    for N in (3, 10, 40, 160):
        xm, ym = tri_overshoot(N)
        p('  N=%3d  x_max/L=%.4f  误差=%.4f  误差*N=%.3f' % (N, xm, ym, ym * N))
    p('[吉布斯] 三角波导数级数在角点附近的峰值（真值 2）')
    for N in (10, 40, 160):
        xm, ym = tri_deriv_peak(N)
        p('  N=%3d  x/L=%.4f  S\'=%.4f  过冲=%.2f%%' % (N, xm, ym, 100 * (ym / 2 - 1)))

    p('\n[例2.1] 抛物线初值在中点的部分和（真值 0.25）')
    for N in (1, 3, 5, 7):
        s = sum(8.0 / (n * np.pi) ** 3 * np.sin(n * np.pi * 0.5)
                for n in range(1, N + 1, 2))
        p('  N=%d  %.6f  误差 %.3f%%' % (N, s, 100 * abs(s - 0.25) / 0.25))

    p('\n[例2.3] 铜杆 L=0.5 m, a^2=1.1e-4, 两端 100/0 度, 中点从 0 升到 25 度')
    a2, Lr = 1.1e-4, 0.5
    lam = a2 * np.pi ** 2 / Lr ** 2
    t = np.linspace(0, 400, 400001)

    def midT(t):
        s = 0.0
        for n in range(1, 400, 2):
            s += ((-1) ** ((n - 1) // 2)) / n * np.exp(-a2 * n ** 2 * np.pi ** 2 * t / Lr ** 2)
        return 50 - 200 / np.pi * s
    i = np.argmin(np.abs(midT(t) - 25))
    p('  lambda=%.4e 1/s, t=%.0f s = %.2f h' % (lam, t[i], t[i] / 3600))

    p('\n[吉他] L=0.65 m, T=70 N, rho=4.5e-3 kg/m')
    Lg, Tg, rg = 0.65, 70.0, 4.5e-3
    c = np.sqrt(Tg / rg)
    p('  c=%.2f m/s  f1=%.2f Hz  f2=%.2f  f3=%.2f' % (c, c / 2 / Lg, c / Lg, 1.5 * c / Lg))
    A = np.pi * (0.2e-3) ** 2
    EA = 2.0e11 * A
    strain = Tg / EA
    dT = -1.2e-5 * 10 / strain
    p('  strain=%.3e  deltaT/T=%.4f  deltaf/f=%.4f (%.1f cents)'
      % (strain, dT, dT / 2, 1200 * np.log2(1 + dT / 2)))
    p('  Q=1000: 带宽 %.3f Hz, 衰减时间 %.2f s' % (c / 2 / Lg / 1000, 1000 / (np.pi * c / 2 / Lg)))

    p('\n[例2.5] Q=1000, f1=196 Hz: 带宽 %.3f Hz, tau=%.2f s'
      % (196 / 1000, 1000 / (np.pi * 196)))

    p('\n[受迫] 驱动端 A=1 mm, k=Omega/omega_1=0.9 -> 最大位移 %.2f mm'
      % (1.0 / abs(np.sin(0.9 * np.pi))))

    p('\n[例2.6] 膜 a=0.20, b=0.202, c=50 m/s')
    a, b, cm = 0.20, 0.202, 50.0
    f12 = cm / 2 * np.sqrt(1 / a ** 2 + 4 / b ** 2)
    f21 = cm / 2 * np.sqrt(4 / a ** 2 + 1 / b ** 2)
    p('  f12=%.3f  f21=%.3f  Delta f=%.3f Hz  拍周期=%.3f s'
      % (f12, f21, f21 - f12, 1 / (f21 - f12)))

    p('\n[例2.7] 钢杆 L=0.4, a^2=1.2e-5, 初值 cos(pi x/L)')
    a2s, Ls = 1.2e-5, 0.4
    p('  半衰期=%.0f s = %.1f min' % (np.log(2) * Ls ** 2 / (a2s * np.pi ** 2),
                                     np.log(2) * Ls ** 2 / (a2s * np.pi ** 2) / 60))

    p('\n[正交性反例] int_0^L sin(pi x/L) sin(3 pi x/(2L)) dx = %.6f' % (
        np.trapz(np.sin(np.pi * np.linspace(0, 1, 200001))
                 * np.sin(1.5 * np.pi * np.linspace(0, 1, 200001)),
                 np.linspace(0, 1, 200001))))
    x = np.linspace(0, 1, 400001)
    p('  int_0^L cos(pi x/L) cos(2 pi x/L) dx = %.6f' % np.trapz(np.cos(np.pi * x) * np.cos(2 * np.pi * x), x))

    p('\n[习题2.32] cos(pi x/L) 的正弦展开，x=L/4 处（真值 0.70711）')
    xs = 0.25
    for Nm in (10, 50, 200):
        s = sum(4.0 * n / (np.pi * (n ** 2 - 1)) * np.sin(n * np.pi * xs)
                for n in range(2, Nm + 1, 2))
        p('  末项 n=%3d: S=%.6f' % (Nm, s))

    p('\n[习题2.30] 三角拨弦的能量分配 E_n ∝ 1/n^2 (n 奇)')
    tot = sum(1.0 / n ** 2 for n in range(1, 20000, 2))
    for n in (1, 3, 5, 7):
        p('  n=%d: %.4f' % (n, (1.0 / n ** 2) / tot))

    p('\n[习题2.24] 中点挂 10 g: delta = mgL/(4T) = %.3e m'
      % (0.01 * 9.8 * Lg / (4 * Tg)))
    p('[习题2.18] 弦自重垂度 rho g L^2/(8T) = %.3e m'
      % (rg * 9.8 * Lg ** 2 / (8 * Tg)))

    p('\n[习题2.23] 杆内均匀热源 q=0.5 K/s, L=0.5, a^2=1.1e-4: u_max=%.1f K'
      % (0.5 * 0.5 ** 2 / (8 * 1.1e-4)))

    p('\n[习题2.21] 正方形膜 a=0.3, c=80: f11=%.2f Hz' % (cm / 2 / 0.3 * np.sqrt(2)))
    for mn in ((1, 1), (1, 2), (2, 2), (1, 3), (2, 3)):
        m, n = mn
        p('  (%d,%d): ratio %.4f  f=%.1f Hz' % (m, n, np.sqrt(m ** 2 + n ** 2) / np.sqrt(2),
                                                cm / 2 / 0.3 * np.sqrt(m * m + n * n)))
    p('[习题2.22] a=0.20, b=0.201: Delta f=%.2f Hz, beat %.2f s'
      % (cm / 2 * (np.sqrt(4 / 0.2 ** 2 + 1 / 0.201 ** 2) - np.sqrt(1 / 0.2 ** 2 + 4 / 0.201 ** 2)),
         1 / (cm / 2 * (np.sqrt(4 / 0.2 ** 2 + 1 / 0.201 ** 2) - np.sqrt(1 / 0.2 ** 2 + 4 / 0.201 ** 2)))))

    p('\n[习题2.17] 钢杆 L=1 m, a^2=1.2e-5, 初 100 度, 两端 0: 中点降到 50 度')
    t2 = np.linspace(0, 20000, 400001)
    s = np.zeros_like(t2)
    for n in range(1, 400, 2):
        s += 1.0 / n * np.sin(n * np.pi / 2) * np.exp(-1.2e-5 * n ** 2 * np.pi ** 2 * t2)
    u = 400 / np.pi * s
    i = np.argmin(np.abs(u - 50))
    p('  t=%.0f s = %.2f h' % (t2[i], t2[i] / 3600))

    p('\n[习题2.31] gamma/omega=0.05, Omega/omega=0.9: phase=%.2f deg'
      % (np.degrees(np.arctan2(0.05 * 0.9, 1 - 0.81))))


def si(x):
    """Si(x) = int_0^x sin t / t dt，用梯形求和。"""
    t = np.linspace(1e-12, x, 200001)
    return np.trapz(np.sin(t) / t, t)


if __name__ == '__main__':
    gen_square()
    gen_triangle()
    gen_resonance()
    gen_forced_shape()
    gen_beats()
    print('dat 文件已写入 build/figs/：ch02-03/04/05/06/07')
    report()
