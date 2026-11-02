# 附录 A 数学约定

> 约定不统一，是物理文献里最容易被忽略、又最折磨人的问题。本附录把本书用到的约定集中列出。动手算之前，先在这里对一遍。

## A.1 符号书写：两条规矩

**第一条：偏导数写全。**

$$\frac{\partial u}{\partial x},\qquad
\frac{\partial^2 u}{\partial x^2},\qquad
\frac{\partial^2 u}{\partial x\partial t}$$

不写 $u_x$、$u_{tt}$、$u_{xy}$，也不写 $\partial_x u$、$\dot u$。原因很简单：$u_{xx}$ 需要读者在脑子里翻译一次，$\partial^2 u/\partial x^2$ 不需要。

**第二条：拉普拉斯算子统一写 $\nabla^2$。**

$$\nabla^2 u=\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}+\frac{\partial^2 u}{\partial z^2}$$

全书只用这一种写法，不用正三角 $\Delta$（它与「增量」「判别式」的记号撞车），也不用 $\Box$（那是达朗贝尔算子，含义不同）。在极坐标、球坐标里需要展示分量式时，会照常把分量写出来——那是推导的一部分。

## A.2 傅里叶变换本书采用

$$\tilde f(k)=\int_{-\infty}^{\infty}f(x)\,e^{-ikx}\,\mathrm{d}x,
\qquad
f(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\tilde f(k)\,e^{ikx}\,\mathrm{d}k.$$

**$1/2\pi$ 只放在逆变换上。**

常见变体对照：

| 约定 | 正变换 | 逆变换 | 出处 |
|---|---|---|---|
| 本书 | $e^{-ikx}$，系数 1 | $e^{ikx}$，系数 $1/2\pi$ | 物理主流 |
| 对称型 | $1/\sqrt{2\pi}$ | $1/\sqrt{2\pi}$ | 数学、部分工程 |
| 工程型 | $e^{-i2\pi fx}$ | $e^{i2\pi fx}$ | 信号处理（用频率 $f$ 而非角频率） |

**换算规则**：如果别人的公式里 $k$ 和你的 $k$ 差一个因子，先检查对方用的是 $k$ 还是 $2\pi f$（以及 $\omega=2\pi f$）。用频率 $f$ 而非角频率 $\omega$ 时，$k\to2\pi f$，所有 $2\pi$ 会重新排列。拉普拉斯变换取

$$\mathcal{L}\{f(t)\}(s)=\int_0^{\infty}f(t)\,e^{-st}\,\mathrm{d}t,\qquad s=\sigma+i\omega .$$

**积分下限是 $0^-$ 还是 $0$？** 本书取 $0$，即忽略 $t=0$ 处的冲激；如果问题里 $t=0$ 有 $\delta(t)$，就把它算进初值，用初值定理处理。

## A.3 $\delta$ 函数

$$\int f(x)\,\delta(x-x_0)\,\mathrm{d}x=f(x_0).$$

| 恒等式 | 说明 |
|---|---|
| $\delta(ax)=\dfrac{1}{|a|}\delta(x)$ | 伸缩 |
| $\delta(-x)=\delta(x)$ | 偶函数 |
| $x\,\delta(x)=0$ | 支撑在原点 |
| $\delta(g(x))=\sum_i\dfrac{\delta(x-x_i)}{|g'(x_i)|}$ | 复合函数，$g(x_i)=0$ |
| $\delta(\boldsymbol{r})=\dfrac{1}{4\pi r^2}\delta(r)$ | 三维球对称 |
| $\int\delta'(x)f(x)\,\mathrm{d}x=-\int\delta(x)f'(x)\,\mathrm{d}x$ | 分部积分 |
| $\dfrac{1}{2\pi}\int e^{ikx}\,\mathrm{d}k=\delta(x)$ | 与傅里叶约定配套 |

最后一条要配合 A.2 的约定使用：如果把 $1/2\pi$ 放到正变换上，这一条就要换个样子。**约定换了，$\delta$ 的积分表示也必须跟着换。**

## A.4 格林函数的符号约定

本书约定

$$\nabla^2 G(\boldsymbol{r},\boldsymbol{r}')=\delta(\boldsymbol{r}-\boldsymbol{r}'),$$

物理响应写作

$$\phi(\boldsymbol{r})=-\frac{1}{\varepsilon_0}\int G(\boldsymbol{r},\boldsymbol{r}')\,\rho(\boldsymbol{r}')\,\mathrm{d}^3r'.$$

**注意负号。** $\nabla^2$ 的格林函数是 $-1/(4\pi r)$，负号来自算子的符号：$\nabla^2(1/r)=-4\pi\delta(\boldsymbol{r})$。不同教材对 $G$ 的定义可能差一个负号，抄公式之前先确认对方用的是哪一种。热传导的格林函数没有这个负号问题（那里是 $\partial T/\partial t-\alpha\nabla^2T$，时间方向定符号）。

## A.5 常用积分

$$\int_{-\infty}^{\infty}e^{-ax^2}\,\mathrm{d}x=\sqrt{\frac{\pi}{a}},\qquad a>0.$$

$$\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{1+x^2}=\pi .$$

$$\int_{-\infty}^{\infty}\frac{\cos(ax)}{1+x^2}\,\mathrm{d}x=\pi e^{-a},\qquad a>0.$$

$$\int_0^\infty\frac{x^{a-1}}{1+x}\,\mathrm{d}x=\frac{\pi}{\sin(\pi a)},\qquad 0<a<1.$$

$$\int_0^\infty e^{-ax}\cos(bx)\,\mathrm{d}x=\frac{a}{a^2+b^2},\qquad
\int_0^\infty e^{-ax}\sin(bx)\,\mathrm{d}x=\frac{b}{a^2+b^2}.$$

$$\int_0^\infty x^{n}e^{-ax}\,\mathrm{d}x=\frac{n!}{a^{n+1}},\qquad
\int_0^\infty e^{-ax^2}\cos(bx)\,\mathrm{d}x=\frac{1}{2}\sqrt{\frac{\pi}{a}}\,e^{-b^2/(4a)}.$$

$$\int_0^{\pi}\sin(mx)\sin(nx)\,\mathrm{d}x=\frac{\pi}{2}\delta_{mn},\qquad
\int_0^{\pi}\cos(mx)\cos(nx)\,\mathrm{d}x=\frac{\pi}{2}\delta_{mn}\quad(m,n\ge1).$$

## A.6 贝塞尔函数零点

| $n$ | $j_{0,n}$ | $j_{1,n}$ | $j_{2,n}$ | $j'_{1,n}$ |
|---|---|---|---|---|
| 1 | 2.4048 | 3.8317 | 5.1356 | 1.8412 |
| 2 | 5.5201 | 7.0156 | 8.4172 | 5.3314 |
| 3 | 8.6537 | 10.1735 | 11.6198 | 8.5363 |
| 4 | 11.7915 | 13.3237 | 14.7960 | 11.7060 |

**近似公式**（$n$ 大时）：$j_{m,n}\approx\left(n+\frac{m}{2}-\frac14\right)\pi$，误差 $O(1/n)$。带撇的是 $J'_m$ 的零点，用于诺伊曼（自然）边界条件——波导的 TE 模、自由边的鼓膜。

## A.7 勒让德多项式的头几个

$$P_0(x)=1,\qquad P_1(x)=x,\qquad P_2(x)=\frac12(3x^2-1),$$
$$P_3(x)=\frac12(5x^3-3x),\qquad P_4(x)=\frac18(35x^4-30x^2+3).$$

正交性：

$$\int_{-1}^{1}P_l(x)P_{l'}(x)\,\mathrm{d}x=\frac{2}{2l+1}\delta_{ll'}.$$

连带勒让德函数与球谐函数都取**科顿–肖特利相位约定**（$P_l^m$ 带因子 $(-1)^m$，与第 4 章一致），球谐函数取

$$Y_{lm}(\theta,\varphi)=\sqrt{\frac{2l+1}{4\pi}\frac{(l-m)!}{(l+m)!}}\,P_l^m(\cos\theta)\,e^{im\varphi},\qquad m\ge0,$$

$m<0$ 时用 $Y_{l,-m}=(-1)^mY_{lm}^{*}$。这样 $Y_{lm}$ 是正交归一的，氢原子波函数里不出现额外的符号。

## A.8 其他常用约定

- 时间因子：波动取 $e^{-i\omega t}$；量子力学里波函数取 $e^{-iEt/\hbar}$（与前者一致）。
- 虚数单位用斜体 $i$。
- 矢量用粗斜体 $\boldsymbol{r}$、$\boldsymbol{E}$；单位矢量用 $\hat{\boldsymbol{e}}_x$、$\hat{\boldsymbol{e}}_r$；分量用下标 $E_x$。
- 张量章启用爱因斯坦求和约定（重复指标求和），其余各章一律写显式求和号。

## A.9 符号表

| 符号 | 含义 |
|---|---|
| $\nabla^2$ | 拉普拉斯算子（全书唯一写法） |
| $\delta_{mn}$ | 克罗内克 $\delta$ |
| $\delta(x)$ | 狄拉克 δ 函数 |
| $\operatorname{Res}$ | 留数 |
| $\mathrm{P.V.}$ | 柯西主值 |
| $\operatorname{Re}z,\ \operatorname{Im}z$ | 实部、虚部 |
| $\mathcal{F},\ \mathcal{L}$ | 傅里叶、拉普拉斯变换 |
| $j_{m,n}$ | $J_m$ 的第 $n$ 个零点（$J'_m$ 的零点记 $j'_{m,n}$） |
| $Y_{lm}$ | 球谐函数 |
| $P_l^m$ | 连带勒让德函数（含科顿–肖特利相位） |
| $j_l,\ y_l$ | 球贝塞尔函数 |
| $\varepsilon_0$ | 真空介电常数 |
| $c$ | 波速（弦上 $c=\sqrt{T/\rho}$，真空为光速） |
| $\omega_n$ | 第 $n$ 个本征频率 |
| $\gamma$ | 阻尼系数 |
| $Q$ | 品质因数，$Q=\omega_n/\gamma$ |
| $\alpha$ | 热扩散率 |
| $G,\ G_0,\ G_{\rm ret}$ | 格林函数、自由空间格林函数、推迟格林函数 |
| $\lambda_n$ | $-\nabla^2$ 的本征值 |
| $a_0$ | 玻尔半径 |
| $\Gamma$ | 环量（流体）；Gamma 函数在附录 F 用 $\Gamma(z)$ |
| $s=\sigma+i\omega$ | 拉普拉斯变量，$\sigma$ 为收敛横坐标 |
| $g_{\mu\nu}$ | 度规张量 |
| $R^\mu{}_{\nu\rho\sigma}$ | 黎曼张量 |
| $\rho$ | 第 1–2 章：线密度；第 5 章起：电荷密度；柱坐标半径**一律用 $r$** |
