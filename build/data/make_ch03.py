# -*- coding: utf-8 -*-
"""第 3 章（圆形的振动）插图数据生成。

不依赖 scipy：J_m 用幂级数，Y_m 用含 digamma 的级数（这里 digamma -> 调和数），
零点用二分法从扫描出的变号区间求。

运行：python build/data/make_ch03.py
输出：build/figs/ch03-02.dat ... ch03-06.dat
"""
import io
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(HERE)
FIGS = os.path.join(BUILD, 'figs')
os.makedirs(FIGS, exist_ok=True)

EULER = 0.5772156649015329


# ---------------------------------------------------------------- Bessel 函数
def J(m, x):
    """第一类 Bessel 函数，幂级数，逐项递推。负阶用 J_{-m} = (-1)^m J_m。"""
    if m < 0:
        return (-1) ** (-m) * J(-m, x)
    x = float(x)
    if x == 0.0:
        return 1.0 if m == 0 else 0.0
    half = x / 2.0
    term = half ** m / math.factorial(m)
    s = term
    k = 0
    while abs(term) > 1e-18 * max(abs(s), 1e-300):
        k += 1
        term *= -(half * half) / (k * (k + m))
        s += term
        if k > 400:
            break
    return s


def _H(n):
    """调和数 H_n（H_0 = 0）。"""
    return sum(1.0 / i for i in range(1, n + 1))


def Y(m, x):
    """第二类 Bessel 函数（Neumann 函数）的级数表示，x>0。"""
    x = float(x)
    if x <= 0:
        return float('-inf')
    half = x / 2.0
    jm = J(m, x)
    # 对数项
    s = (2.0 / math.pi) * jm * (math.log(half) + EULER)
    # 有限项：k = 0 .. m-1
    for k in range(m):
        s -= (1.0 / math.pi) * (math.factorial(m - k - 1) / math.factorial(k)) * half ** (2 * k - m)
    # 无穷级数项
    term = half ** m / math.factorial(m)
    for k in range(0, 400):
        if k > 0:
            term *= -(half * half) / (k * (k + m))
        s -= (1.0 / math.pi) * (-1) ** k * (_H(k) + _H(m + k)) * half ** (2 * k + m) / (
            math.factorial(k) * math.factorial(m + k))
        if abs(term) < 1e-18 and k > 30:
            break
    return s


def Jp(m, x):
    """J_m'(x)，用 J_m' = (J_{m-1} - J_{m+1})/2。"""
    return 0.5 * (J(m - 1, x) - J(m + 1, x))


# 已知值自检（Abramowitz & Stegun 表 9.1 / 9.4）
assert abs(J(0, 1.0) - 0.7651976866) < 1e-9
assert abs(J(1, 1.0) - 0.4400505857) < 1e-9
assert abs(J(0, 0.5) - 0.9384698072) < 1e-9
assert abs(Y(0, 1.0) - 0.0882569642) < 1e-8
assert abs(Y(1, 1.0) + 0.7812128213) < 1e-8
assert abs(Y(0, 0.5) + 0.4445187335) < 1e-8
assert abs(Jp(0, 1.0) + 0.4400505857) < 1e-9


def zero(f, a, b, n=200):
    """f 在 [a,b] 上变号时二分求零点。"""
    fa = f(a)
    for _ in range(n):
        c = 0.5 * (a + b)
        fc = f(c)
        if (fa < 0) == (fc < 0):
            a, fa = c, fc
        else:
            b = c
    return 0.5 * (a + b)


def zeros(f, xmax, count, step=0.02):
    """从 x=step 扫到 xmax，收集前 count 个变号零点。"""
    out = []
    x0 = step
    f0 = f(x0)
    while x0 < xmax and len(out) < count:
        x1 = x0 + step
        f1 = f(x1)
        if (f0 < 0) != (f1 < 0):
            out.append(zero(f, x0, x1))
        x0, f0 = x1, f1
    return out


# J_m 与 J_m' 的前若干零点
JZ = {m: zeros(lambda x, m=m: J(m, x), 40, 5) for m in range(0, 6)}
JPZ = {m: zeros(lambda x, m=m: Jp(m, x), 40, 5) for m in range(0, 6)}

# 与标准值对照（见 Watson 15.1 / A&S 表 9.5）
assert abs(JZ[0][0] - 2.4048255577) < 1e-7
assert abs(JZ[1][0] - 3.8317059702) < 1e-7
assert abs(JZ[2][0] - 5.1356223018) < 1e-7
assert abs(JZ[0][1] - 5.5200781103) < 1e-7
assert abs(JPZ[1][0] - 1.8411837813) < 1e-7
assert abs(JPZ[2][0] - 3.0542369282) < 1e-7
assert abs(JPZ[0][0] - 3.8317059702) < 1e-7


def save(name, header, cols):
    path = os.path.join(FIGS, name)
    data = np.column_stack(cols)
    np.savetxt(path, data, fmt='%.6f', header=header, comments='')
    print('  %-14s %5d 行' % (name, len(data)))


print('[第 3 章] 生成插图数据：')

# ---- ch03-02：J_0 .. J_3，标出零点 -------------------------------------
x = np.arange(0.0, 12.001, 0.02)
save('ch03-02.dat', 'x J0 J1 J2 J3',
     [x, [J(0, t) for t in x], [J(1, t) for t in x],
      [J(2, t) for t in x], [J(3, t) for t in x]])

# ---- ch03-03：J_0 与 Y_0 在原点附近的行为 ------------------------------
x = np.arange(0.06, 10.001, 0.01)
save('ch03-03.dat', 'x J0 Y0 J1 Y1',
     [x, [J(0, t) for t in x], [Y(0, t) for t in x],
      [J(1, t) for t in x], [Y(1, t) for t in x]])

# ---- ch03-05：鼓膜径向剖面 J_0(j_{0n} r/a)，n = 1,2,3 -----------------
xi = np.arange(0.0, 1.0001, 0.005)
cols = [xi]
for n in range(3):
    k = JZ[0][n]
    cols.append([J(0, k * t) for t in xi])
save('ch03-05.dat', 'xi n1 n2 n3', cols)

# ---- ch03-06：零点随阶数的位置与渐近线 (n + m/2 - 1/4)*pi -------------
n = np.arange(1, 6)
cols = [n]
for m in range(4):
    cols.append([JZ[m][i] for i in range(5)])
cols.append((n - 0.25) * np.pi)          # m=0 的渐近线
save('ch03-06.dat', 'n m0 m1 m2 m3 asympt', cols)

# ---- 正文要用的数值，直接打印出来核对 --------------------------------
print('\n[零点]')
for m in range(4):
    print('  j_{%d,n}  n=1..4: %s' % (m, ' '.join('%.6f' % v for v in JZ[m][:4])))
for m in range(4):
    print("  j'_{%d,n} n=1..4: %s" % (m, ' '.join('%.6f' % v for v in JPZ[m][:4])))

print('\n[鼓膜] a=0.35 m, c=60 m/s')
a, c = 0.35, 60.0
zs = sorted([(JZ[m][i], m, i + 1) for m in range(6) for i in range(3)])[:10]
for j, m, k in zs:
    print('  (m,n)=(%d,%d)  j=%.4f  f=%.1f Hz  比 %.3f' % (m, k, j, c * j / (2 * np.pi * a), j / JZ[0][0]))

print('\n[圆波导] a=1 cm, c=2.998e8 m/s')
for lab, v in modes:
    print('  %-10s kca=%.4f  fc=%.2f GHz' % (lab.replace('$', ''), v, v * 2.998e8 / (2 * np.pi * 0.01) / 1e9))

print('\n[节圆] 模式 (m,n) 的节圆半径 r/a = j_{m,k}/j_{m,n}')
for m, n in [(0, 2), (0, 3), (1, 2), (1, 3), (2, 2)]:
    r = ' '.join('%.4f' % (JZ[m][k] / JZ[m][n - 1]) for k in range(n - 1))
    print('  (%d,%d): %s' % (m, n, r))

print('\n[光纤] V = 2*pi*a*NA/lambda')
for a_um, na, lam in [(4.1, 0.12, 1.55), (4.1, 0.12, 1.31), (4.1, 0.12, 0.85)]:
    print('  a=%.1f um NA=%.2f lambda=%.2f um -> V=%.3f' % (a_um, na, lam, 2 * np.pi * a_um * na / lam))

print('\nok')
