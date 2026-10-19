# 附录 A 数学约定

> 约定不统一，是物理文献里最容易被忽略、又最折磨人的问题。本附录把本书用到的约定集中列出。

## A.1 Fourier 变换

本书采用

$$\tilde f(k)=\int_{-\infty}^{\infty}f(x)\,e^{-ikx}\,dx,
\qquad
f(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\tilde f(k)\,e^{ikx}\,dk.$$

**1/2π 只放在逆变换上。**

常见变体对照：

| 约定 | 正变换 | 逆变换 | 出处 |
|---|---|---|---|
| 本书 | $e^{-ikx}$，系数 1 | $e^{ikx}$，系数 $1/2\pi$ | 物理主流 |
| 对称型 | $1/\sqrt{2\pi}$ | $1/\sqrt{2\pi}$ | 数学、部分工程 |
| 工程型 | $e^{-i2\pi fx}$ | $e^{i2\pi fx}$ | 信号处理（用频率 $f$ 而非角频率） |

**换算规则**：如果别人的公式里 $k$ 和你的 $k$ 差一个因子，先检查对方用的是 $k$ 还是 $2\pi f$（以及 $\omega=2\pi f$）。用频率 $f$ 而非角频率 $\omega$ 时，$k\to2\pi f$，所有 $2\pi$ 会重新排列。

## A.2 δ 函数

$$\int f(x)\,\delta(x-x_0)\,dx=f(x_0).$$

| 恒等式 | 说明 |
|---|---|
| $\delta(ax)=\frac{1}{|a|}\delta(x)$ | 伸缩 |
| $\delta(-x)=\delta(x)$ | 偶函数 |
| $x\,\delta(x)=0$ | 支撑在原点 |
| $\delta(g(x))=\sum_i\frac{\delta(x-x_i)}{|g'(x_i)|}$ | 复合函数，$g(x_i)=0$ |
| $\delta(\mathbf r)=\frac{1}{4\pi r^2}\delta(r)$ | 三维球对称 |
| $\int\delta'\,f=-\int\delta\,f'$ | 分部积分 |

## A.3 Green 函数

本书约定

$$\nabla^2G(\mathbf r,\mathbf r')=\delta(\mathbf r-\mathbf r'),$$

物理响应写作

$$\phi(\mathbf r)=-\frac{1}{\varepsilon_0}\int G(\mathbf r,\mathbf r')\rho(\mathbf r')\,d^3r'.$$

**注意负号**：$\nabla^2$ 的 Green 函数是 $-1/(4\pi r)$，负号来自算子的符号。不同教材对 $G$ 的定义可能差一个负号，用之前先确认。

## A.4 常用积分

$$\int_{-\infty}^{\infty}e^{-ax^2}\,dx=\sqrt{\frac{\pi}{a}},\qquad a>0.$$

$$\int_{-\infty}^{\infty}\frac{dx}{1+x^2}=\pi.$$

$$\int_{-\infty}^{\infty}\frac{\cos(ax)}{1+x^2}\,dx=\pi e^{-a},\qquad a>0.$$

$$\int_0^\infty\frac{x^{a-1}}{1+x}\,dx=\frac{\pi}{\sin(\pi a)},\qquad 0<a<1.$$

$$\int_0^\infty e^{-ax}\cos(bx)\,dx=\frac{a}{a^2+b^2}.$$

## A.5 Bessel 函数零点

| $n$ | $j_{0,n}$ | $j_{1,n}$ | $j_{2,n}$ |
|---|---|---|---|
| 1 | 2.4048 | 3.8317 | 5.1356 |
| 2 | 5.5201 | 7.0156 | 8.4172 |
| 3 | 8.6537 | 10.1735 | 11.6198 |
| 4 | 11.7915 | 13.3237 | 14.7960 |

**近似公式**（$n$ 大时）：

$$j_{m,n}\approx\left(n+\frac{m}{2}-\frac14\right)\pi.$$

## A.6 Legendre 多项式

$$P_0=1,\quad P_1=x,\quad P_2=\frac12(3x^2-1),\quad P_3=\frac12(5x^3-3x).$$

正交性：

$$\int_{-1}^{1}P_l(x)P_{l'}(x)\,dx=\frac{2}{2l+1}\delta_{ll'}.$$

## A.7 符号表

| 符号 | 含义 |
|---|---|
| $\nabla^2$ | Laplace 算子 |
| $\delta_{nm}$ | Kronecker delta |
| $\operatorname{Res}$ | 留数 |
| P.V. | Cauchy 主值 |
| $\operatorname{Im}z$ | 虚部 |
| $\mathcal F,\ \mathcal L$ | Fourier、Laplace 变换 |
| $j_{m,n}$ | $J_m$ 的第 $n$ 个零点（$J^{\prime}_m$ 的零点记 $j^{\prime}_{m,n}$） |
| $Y_{lm}$ | 球谐函数 |
| $\varepsilon_0$ | 真空介电常数 |
| $c$ | 波速（弦上 $c=\sqrt{T/\rho}$，真空中为光速） |
| $\omega_n$ | 第 $n$ 个本征频率 |
| $\gamma$ | 阻尼系数 |
| $Q$ | 品质因数，$Q=\omega_n/\gamma$ |
| $\alpha$ | 热扩散率 |
| $G_0$ | 自由空间 Green 函数 |
| $G_{\rm ret}$ | 推迟 Green 函数 |
| $\Box$ | 波动算子 $\nabla^2-\frac{1}{c^2}\partial_t^2$ |
| $\lambda_n$ | $-\nabla^2$ 的本征值 |
| $j_l,\ y_l$ | 球贝塞尔函数 |
| $P_l^m$ | 连带 Legendre 函数 |
| $a_0$ | 玻尔半径 |
| $\Gamma$ | 环量 |
| $s=\sigma+i\omega$ | Laplace 变量；$\sigma$ 为收敛横坐标 |
| $\rho$ | 第 1 章：线密度；第 3 章起：电荷密度 |
