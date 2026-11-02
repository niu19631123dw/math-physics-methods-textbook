# 附录 F 特殊函数速查

> 正文不背递推式和生成函数——物理里很少手算它们。但做积分、化高阶为低阶、凑边界条件时会用到，所以集中放这里查。

## F.1 Gamma 函数

$$\Gamma(z)=\int_0^{\infty}t^{z-1}e^{-t}\,\mathrm{d}t,\qquad
\Gamma(z+1)=z\Gamma(z),\qquad \Gamma(n+1)=n! .$$

$$\Gamma\!\left(\tfrac12\right)=\sqrt{\pi},\qquad
\Gamma(z)\Gamma(1-z)=\frac{\pi}{\sin(\pi z)}.$$

**斯特林公式**（$|z|$ 大）：

$$\Gamma(z+1)\approx\sqrt{2\pi z}\left(\frac{z}{e}\right)^{z}.$$

它在两个地方出现：一是球坐标分离变量后 $(l+m)!/(l-m)!$ 这类因子，二是第 6 章算带支割线的积分时 $z^{a-1}$ 的围道。

## F.2 贝塞尔函数

**递推关系**

$$J_{m-1}(x)+J_{m+1}(x)=\frac{2m}{x}J_m(x),$$

$$J_{m-1}(x)-J_{m+1}(x)=2\frac{\mathrm{d}J_m}{\mathrm{d}x},$$

$$\frac{\mathrm{d}J_m}{\mathrm{d}x}=J_{m-1}(x)-\frac{m}{x}J_m(x).$$

**带权导数**（最常用的一条）

$$\frac{\mathrm{d}}{\mathrm{d}x}\left[x^mJ_m(x)\right]=x^mJ_{m-1}(x)
\quad\Longrightarrow\quad
\int x^mJ_{m-1}(x)\,\mathrm{d}x=x^mJ_m(x).$$

**生成函数**

$$\exp\left[\frac{x}{2}\left(t-\frac{1}{t}\right)\right]
=\sum_{n=-\infty}^{\infty}J_n(x)\,t^n.$$

取 $t=e^{i\varphi}$ 就得到雅可比展开 $e^{ix\sin\varphi}=\sum_n J_n(x)e^{in\varphi}$，这是调频信号与相位光栅的数学基础。

**正交性**（带权 $r$）

$$\int_0^a J_m\!\left(\frac{j_{mn}r}{a}\right)J_m\!\left(\frac{j_{mk}r}{a}\right)r\,\mathrm{d}r
=\frac{a^2}{2}\left[J_{m+1}(j_{mn})\right]^2\delta_{nk}.$$

**渐近行为**

$$J_m(x)\approx\sqrt{\frac{2}{\pi x}}\cos\left(x-\frac{m\pi}{2}-\frac{\pi}{4}\right),\qquad x\gg1,$$

$$J_m(x)\approx\frac{1}{m!}\left(\frac{x}{2}\right)^m,\qquad x\ll1\ (m\ \text{固定}).$$

小 $x$ 行为决定了「能不能在 $r=0$ 处取这个解」：$J_0(0)=1$ 有界，$Y_0(0)\to-\infty$ 发散。

**常用积分**

$$\int_0^\infty e^{-ax}J_0(bx)\,\mathrm{d}x=\frac{1}{\sqrt{a^2+b^2}},\qquad a>0.$$

## F.3 勒让德多项式

**递推关系**

$$(l+1)P_{l+1}(x)=(2l+1)xP_l(x)-lP_{l-1}(x).$$

**导数关系**

$$(1-x^2)\frac{\mathrm{d}P_l}{\mathrm{d}x}=l\left[P_{l-1}(x)-xP_l(x)\right].$$

**生成函数**

$$\frac{1}{\sqrt{1-2xt+t^2}}=\sum_{l=0}^{\infty}P_l(x)\,t^l.$$

**正交性**

$$\int_{-1}^{1}P_l(x)P_{l'}(x)\,\mathrm{d}x=\frac{2}{2l+1}\delta_{ll'}.$$

**加法定理**

$$P_l(\cos\gamma)=P_l(\cos\theta)P_l(\cos\theta')
+2\sum_{m=1}^{l}\frac{(l-m)!}{(l+m)!}P_l^m(\cos\theta)P_l^m(\cos\theta')\cos m(\varphi-\varphi'),$$

其中 $\gamma$ 是 $(\theta,\varphi)$ 与 $(\theta',\varphi')$ 之间的夹角。**展开球面函数时，这条定理能省掉一大半计算。**

## F.4 球谐函数

正交归一：

$$\int Y_{lm}^{*}Y_{l'm'}\,\mathrm{d}\Omega=\delta_{ll'}\delta_{mm'}.$$

头几个（含科顿–肖特利相位，$m\ge0$）：

$$Y_{00}=\frac{1}{\sqrt{4\pi}},\qquad
Y_{10}=\sqrt{\frac{3}{4\pi}}\cos\theta,\qquad
Y_{11}=-\sqrt{\frac{3}{8\pi}}\sin\theta\,e^{i\varphi}.$$

加法公式（$P_l$ 展开的核心）：

$$\sum_{m=-l}^{l}Y_{lm}(\theta,\varphi)Y_{lm}^{*}(\theta',\varphi')
=\frac{2l+1}{4\pi}P_l(\cos\gamma).$$

## F.5 埃尔米特与拉盖尔多项式

**埃尔米特**（谐振子）：

$$H_{n+1}(x)=2xH_n(x)-2nH_{n-1}(x),\qquad
e^{2xt-t^2}=\sum_{n=0}^{\infty}H_n(x)\frac{t^n}{n!},$$

$$\int_{-\infty}^{\infty}e^{-x^2}H_n(x)H_m(x)\,\mathrm{d}x=\sqrt{\pi}\,2^nn!\,\delta_{nm}.$$

**拉盖尔**（氢原子径向）：

$$(n+1)L_{n+1}(x)=(2n+1-x)L_n(x)-nL_{n-1}(x),\qquad
\int_0^{\infty}e^{-x}L_n(x)L_m(x)\,\mathrm{d}x=\delta_{nm},$$

连带形式 $L_n^m(x)$ 满足

$$\int_0^{\infty}x^m e^{-x}L_n^m(x)L_{n'}^m(x)\,\mathrm{d}x
=\frac{(n+m)!}{n!}\delta_{nn'}.$$

## F.6 球贝塞尔函数

$$j_l(x)=\sqrt{\frac{\pi}{2x}}J_{l+1/2}(x),\qquad
y_l(x)=\sqrt{\frac{\pi}{2x}}Y_{l+1/2}(x).$$

**递推**

$$\frac{2l+1}{x}j_l(x)=j_{l-1}(x)+j_{l+1}(x).$$

**前几个显式形式**

$$j_0(x)=\frac{\sin x}{x},\qquad
j_1(x)=\frac{\sin x}{x^2}-\frac{\cos x}{x},$$

$$y_0(x)=-\frac{\cos x}{x},\qquad
y_1(x)=-\frac{\cos x}{x^2}-\frac{\sin x}{x}.$$

**小 $x$ 与大 $x$**

$$j_l(x)\approx\frac{x^l}{(2l+1)!!},\quad x\ll1;
\qquad
j_l(x)\approx\frac{1}{x}\sin\left(x-\frac{l\pi}{2}\right),\quad x\gg1.$$

小 $x$ 行为直接决定氢原子径向函数在原点是否可归一化：只有 $l$ 有限、$y_l$ 被丢掉，波函数才在 $r\to0$ 处有界。

## F.7 什么时候用哪一条

| 要做的事 | 用哪个 |
|---|---|
| 把 $J_{m+1}$ 化成 $J_m$、$J_{m-1}$ | 递推关系 |
| 算 $\int x^mJ_{m-1}\,\mathrm{d}x$ | 带权导数 |
| 求含贝塞尔的级数和、调频展开 | 生成函数 |
| 按本征函数展开 | 正交性 |
| 球面两点的角距离 | 勒让德 / 球谐加法定理 |
| 谐振子、氢原子波函数 | 埃尔米特、拉盖尔 |
| 判断某个解在原点是否有界 | $x\ll1$ 的渐近行为 |
| 判断远场行为、能否丢掉某个解 | $x\gg1$ 的渐近行为 |

**三个"怎么用"的例子**

**例一：算出 $\int x^2J_1(x)\,\mathrm{d}x$。** 用带权导数 $\frac{\mathrm{d}}{\mathrm{d}x}[x^mJ_m]=x^mJ_{m-1}$，取 $m=2$：$\frac{\mathrm{d}}{\mathrm{d}x}[x^2J_2]=x^2J_1$。所以积分直接是 $x^2J_2(x)+C$。**不需要分部积分，也不需要查积分表。**

**例二：证明 $\frac{\mathrm{d}J_0}{\mathrm{d}x}=-J_1$。** 用递推 $J_{m-1}-J_{m+1}=2\frac{\mathrm{d}J_m}{\mathrm{d}x}$，取 $m=0$：$J_{-1}-J_1=2\frac{\mathrm{d}J_0}{\mathrm{d}x}$；再用 $J_{-n}=(-1)^nJ_n$ 得 $J_{-1}=-J_1$，代入即得 $\frac{\mathrm{d}J_0}{\mathrm{d}x}=-J_1$。**关键是选对 $m$**：取 $m=0$ 直接把待证式变成一条递推，取 $m=1$ 得到的却是 $J_1'$ 的式子（$J_1'=J_0-J_1/x$），推不出待证式。

**例三：把 $1/|\boldsymbol{r}-\boldsymbol{r}'|$ 按勒让德展开。** 用生成函数，取 $x=\cos\gamma$、$t=r'/r$（$r>r'$），得到

$$\frac{1}{|\boldsymbol{r}-\boldsymbol{r}'|}=\frac{1}{r}\sum_{l=0}^{\infty}\left(\frac{r'}{r}\right)^{l}P_l(\cos\gamma).$$

**这就是多极展开每一项系数都是勒让德多项式的原因**，也是第 5 章多极展开的出发点。

**一条经验：** 物理里真正需要手算的特殊函数恒等式，九成以上出自上面这几类。剩下的（汉克尔函数、渐近展开的高阶项、积分表示）交给查表或数值库。
