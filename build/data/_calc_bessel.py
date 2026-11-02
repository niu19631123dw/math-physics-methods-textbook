# -*- coding: utf-8 -*-
"""为新节「贝塞尔函数怎么算」算数：级数收敛、递推稳定性、零点、三类积分、渐近误差、量子点能级。"""
import math
import numpy as np

# ---------- 基础：级数 ----------
def J(m, x, nmax=400):
    x = float(x)
    if x == 0:
        return 1.0 if m == 0 else 0.0
    half = x / 2
    term = half ** m / math.factorial(m)
    s = term
    for k in range(1, nmax):
        term *= -(half * half) / (k * (k + m))
        s += term
        if abs(term) < 1e-18:
            break
    return s


def terms_to(m, x, tol=1e-6):
    """加到哪一项才能把后续项全部压到 tol 以下（返回项数 k+1 与最后一项大小）。"""
    half = x / 2
    term = half ** m / math.factorial(m)
    s = term
    k = 0
    while True:
        k += 1
        term *= -(half * half) / (k * (k + m))
        s += term
        if abs(term) < tol:
            return k + 1, abs(term), s


print('=== 级数收敛 ===')
for m, x in ((0, 1.0), (1, 2.0), (2, 3.0)):
    n, last, val = terms_to(m, x)
    print('J_%d(%g): %d 项到 1e-6，最后一项 %.2e，值 %.7f（真值 %.7f）'
          % (m, x, n, last, val, J(m, x)))

print('\n=== 部分和 ===')
for m, x in ((0, 1.0), (1, 2.0), (2, 3.0)):
    half = x / 2
    term = half ** m / math.factorial(m)
    s = term
    row = ['k=0: %.6f' % s]
    for k in range(1, 8):
        term *= -(half * half) / (k * (k + m))
        s += term
        row.append('k=%d: %.6f' % (k, s))
    print('J_%d(%g)' % (m, x), ' | '.join(row[:6]))
    print('   继续', ' | '.join(row[6:]))

# ---------- 递推稳定性 ----------
print('\n=== 向前递推 ===')
x = 1.0
J0, J1 = J(0, x), J(1, x)
vals = [J0, J1]
for m in range(1, 21):
    vals.append(2 * m / x * vals[m] - vals[m - 1])
for m in (2, 3, 5, 10, 15, 20):
    print('J_%d(1) 递推 %.3e   真值 %.3e   相对误差 %.1e'
          % (m, vals[m], J(m, x), abs(vals[m] - J(m, x)) / max(abs(J(m, x)), 1e-300)))

# ---------- 零点 ----------
def zeros(f, xmax=25, n=4, step=0.02):
    out, a, fa = [], step, f(step)
    while a < xmax and len(out) < n:
        b = a + step
        fb = f(b)
        if (fa < 0) != (fb < 0):
            lo, hi = a, b
            for _ in range(200):
                mid = 0.5 * (lo + hi)
                if (f(lo) < 0) == (f(mid) < 0):
                    lo = mid
                else:
                    hi = mid
            out.append(0.5 * (lo + hi))
        a, fa = b, fb
    return out


z = zeros(lambda t: J(0, t), 25, 4)
print('\n=== 零点 ===')
print('j_{0,n} 二分:', ['%.6f' % t for t in z])
for n in (1, 2, 3, 4):
    print('n=%d 渐近 (n-1/4)pi = %.6f，真值 %.6f，误差 %.3f%%'
          % (n, (n - 0.25) * math.pi, z[n - 1], 100 * abs((n - 0.25) * math.pi - z[n - 1]) / z[n - 1]))

# ---------- 渐近误差 ----------
print('\n=== 渐近误差 ===')
for t in (1.0, 5.0, 20.0):
    asym = math.sqrt(2 / (math.pi * t)) * math.cos(t - math.pi / 4)
    print('x=%g: 渐近 %.6f  真值 %.6f  绝对差 %.4f 相对差 %.1f%%'
          % (t, asym, J(0, t), asym - J(0, t), 100 * abs(asym - J(0, t)) / abs(J(0, t))))

# ---------- 积分 ----------
print('\n=== 积分（数值核对） ===')
xs = np.linspace(0, 3.0, 200001)
f1 = xs * np.array([J(0, t) for t in xs])
print('int_0^3 xJ0 dx = %.6f   公式 xJ1 = %.6f'
      % (np.trapezoid(f1, xs), 3.0 * J(1, 3.0)))
f2 = xs ** 2 * np.array([J(1, t) for t in xs])
print('int_0^3 x^2J1 dx = %.6f   公式 x^2J2 = %.6f'
      % (np.trapezoid(f2, xs), 9.0 * J(2, 3.0)))

a = 1.0
j01 = z[0]
xs = np.linspace(0, a, 200001)
f3 = xs * np.array([J(0, j01 * t / a) for t in xs]) ** 2
print('int_0^a rJ0^2 = %.6f   (a^2/2)J1^2 = %.6f'
      % (np.trapezoid(f3, xs), 0.5 * a * a * J(1, j01) ** 2))

# ---------- 量子点 ----------
print('\n=== 量子点 a=5 nm ===')
hbar = 1.054571817e-34
me = 9.1093837015e-31
eV = 1.602176634e-19
a = 5e-9
E01 = hbar ** 2 * j01 ** 2 / (2 * me * a ** 2)
print('E01 = %.4e J = %.3f meV' % (E01, E01 / eV * 1e3))
for name, j in (('01', 2.4048255577), ('11', 3.8317059702), ('21', 5.1356223018), ('02', 5.5200781103)):
    print('  E%s/E01 = %.4f' % (name, (j / j01) ** 2))
print('E01 用 hbar^2 pi^2/(2ma^2) 作尺子: %.3f meV' % (math.pi ** 2 * hbar ** 2 / (2 * me * a ** 2) / eV * 1e3))
