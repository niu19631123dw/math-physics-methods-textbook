#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""第 4 章插图数据：Legendre 多项式、阶梯电势的 Legendre 部分和、多极角向分布、
实球谐截面、氢原子径向函数与径向概率密度、球贝塞尔函数。

运行：  python build/data/make_ch04.py
输出：  build/figs/ch04-01.dat ... ch04-07.dat
        （ch04-03*.dat、ch04-04*.dat 供 plain TikZ 的 plot file 使用，只有 x y 两列，无表头）

所有曲线都由公式现算，不手填数据；脚本可重复运行。
"""
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, '..', 'figs'))


def legendre(nmax, x):
    """P_0..P_nmax 在数组 x 上的值，三项递推。返回 (len(x), nmax+1)。"""
    x = np.asarray(x, dtype=float)
    p = np.zeros((x.size, nmax + 1))
    p[:, 0] = 1.0
    if nmax >= 1:
        p[:, 1] = x
    for l in range(1, nmax):
        p[:, l + 1] = ((2 * l + 1) * x * p[:, l] - l * p[:, l - 1]) / (l + 1)
    return p


def save(name, header, cols):
    data = np.column_stack(cols)
    path = os.path.join(OUT, name)
    if header:
        np.savetxt(path, data, header=' '.join(header), comments='', fmt='%.6e')
    else:
        np.savetxt(path, data, fmt='%.6e')
    print('  %-16s %4d 行' % (name, len(data)))


# ---------------------------------------------------------------- 图 4.1
def fig01():
    x = np.linspace(-1.0, 1.0, 401)
    p = legendre(4, x)
    save('ch04-01.dat', ['x', 'P0', 'P1', 'P2', 'P3', 'P4'],
         [x] + [p[:, l] for l in range(5)])


# ---------------------------------------------------------------- 图 4.2 的数据
def fig02():
    """P_3 的零点 -> 球面上的节锥。只打印核对用，图本身由 TikZ 画。"""
    z = np.roots([5.0, 0.0, -3.0, 0.0])          # 5x^3-3x=0
    th = np.degrees(np.arccos(np.sort(z.real)))
    print('  P_3 零点 x=%s -> theta=%s 度'
          % (np.array2string(np.sort(z.real), precision=4),
             np.array2string(th, precision=1)))


# ---------------------------------------------------------------- 图 4.3
def fig03():
    """三种多极的角向分布，极坐标截面 r(theta)=|P_l(cos theta)|。"""
    t = np.linspace(0.0, 2 * np.pi, 361)
    c = np.cos(t)
    curves = {
        'a': np.ones_like(t),                       # 单极：圆
        'b': np.abs(c),                             # 偶极：两瓣
        'c': np.abs(0.5 * (3 * c ** 2 - 1)),        # 四极：四瓣
    }
    for k, r in curves.items():
        save('ch04-03%s.dat' % k, [], [r * c, r * np.sin(t)])


# ---------------------------------------------------------------- 图 4.4
def fig04():
    """实球谐 |Y|^2 在 xz 平面（phi=0）的截面，各自归一到峰值 1。"""
    t = np.linspace(0.0, 2 * np.pi, 361)
    c, s = np.cos(t), np.sin(t)
    curves = {
        'a': np.ones_like(t),                       # s：球对称
        'b': c ** 2,                                # p_z
        'c': 0.25 * (3 * c ** 2 - 1) ** 2,          # d_z^2
        'd': s ** 4,                                # d_{x^2-y^2} 的 xz 截面
    }
    for k, r in curves.items():
        save('ch04-04%s.dat' % k, [], [r * c, r * s])


# ---------------------------------------------------------------- 图 4.5 / 4.6
def fig05():
    """氢原子径向函数。真实振幅相差近两个量级，为看清节点，各条按自身峰值归一。"""
    chi = np.linspace(0.0, 20.0, 601)
    R10 = 2.0 * np.exp(-chi)
    R20 = (1.0 / (2 * np.sqrt(2))) * (2.0 - chi) * np.exp(-chi / 2)
    R21 = (1.0 / (2 * np.sqrt(6))) * chi * np.exp(-chi / 2)
    R30 = (2.0 / (81 * np.sqrt(3))) * (27 - 18 * chi + 2 * chi ** 2) * np.exp(-chi / 3)

    d = chi[1] - chi[0]
    for name, R in (('1s', R10), ('2s', R20), ('2p', R21), ('3s', R30)):
        print('  %s 归一化积分 = %.6f  (峰值 %.3f)'
              % (name, np.sum(R ** 2 * chi ** 2) * d, np.max(np.abs(R))))

    cols, head = [chi], ['chi']
    for name, R in (('R10', R10), ('R20', R20), ('R21', R21), ('R30', R30)):
        cols.append(R / np.max(np.abs(R)))
        head.append(name)
    save('ch04-05.dat', head, cols)


def fig06():
    """径向概率密度 P(chi)=chi^2 |R|^2，单位 a0^{-1}，面积归一化到 1。"""
    chi = np.linspace(0.0, 30.0, 1201)
    R10 = 2.0 * np.exp(-chi)
    R20 = (1.0 / (2 * np.sqrt(2))) * (2.0 - chi) * np.exp(-chi / 2)
    R21 = (1.0 / (2 * np.sqrt(6))) * chi * np.exp(-chi / 2)
    R30 = (2.0 / (81 * np.sqrt(3))) * (27 - 18 * chi + 2 * chi ** 2) * np.exp(-chi / 3)
    cols = [chi]
    head = ['chi']
    for name, R in (('P10', R10), ('P20', R20), ('P21', R21), ('P30', R30)):
        cols.append(chi ** 2 * R ** 2)
        head.append(name)
    save('ch04-06.dat', head, cols)

    print('  1s 峰位 %.3f a0；2p 峰位 %.3f a0；2s 外峰 %.3f a0；3s 峰位 %.3f a0'
          % (chi[np.argmax(cols[1])], chi[np.argmax(cols[3])],
             chi[np.argmax(cols[2])], chi[np.argmax(cols[4])]))


# ---------------------------------------------------------------- 图 4.7
def fig07():
    """球贝塞尔函数 j_0, j_1, j_2。"""
    x = np.linspace(0.02, 15.0, 601)
    j0 = np.sin(x) / x
    j1 = np.sin(x) / x ** 2 - np.cos(x) / x
    j2 = (3.0 / x ** 3 - 1.0 / x) * np.sin(x) - 3.0 * np.cos(x) / x ** 2
    save('ch04-07.dat', ['x', 'j0', 'j1', 'j2'], [x, j0, j1, j2])


def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    print('生成第 4 章插图数据 ->', OUT)
    fig01()
    fig02()
    fig03()
    fig04()
    fig05()
    fig06()
    fig07()
    print('完成。')


if __name__ == '__main__':
    main()
