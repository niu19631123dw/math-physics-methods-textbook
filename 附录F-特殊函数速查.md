# 附录 F 特殊函数速查

> 正文不给递推和生成函数——物理里很少手算它们。但做积分、化高阶为低阶时会用到，所以集中放这里查。

## F.1 Bessel 函数

**递推关系**

$$J_{m-1}(x)+J_{m+1}(x)=\frac{2m}{x}J_m(x),$$

$$J_{m-1}(x)-J_{m+1}(x)=2J'_m(x),$$

$$J'_m(x)=J_{m-1}(x)-\frac{m}{x}J_m(x).$$

**带权导数**

$$\frac{d}{dx}\left[x^mJ_m(x)\right]=x^mJ_{m-1}(x).$$

它的直接用途是把含 Bessel 的积分化成可算形式：

$$\int x^mJ_{m-1}(x)\,dx=x^mJ_m(x).$$

**生成函数**

$$\exp\left[\frac{x}{2}\left(t-\frac{1}{t}\right)\right]
=\sum_{n=-\infty}^{\infty}J_n(x)\,t^n.$$

**正交性**

$$\int_0^a J_m\left(\frac{j_{mn}r}{a}\right)J_m\left(\frac{j_{mk}r}{a}\right)r\,dr
=\frac{a^2}{2}J_{m+1}^2(j_{mn})\,\delta_{nk}.$$

**常用积分**

$$\int_0^\infty e^{-ax}J_0(bx)\,dx=\frac{1}{\sqrt{a^2+b^2}}.$$

## F.2 Legendre 多项式

**递推关系**

$$(l+1)P_{l+1}(x)=(2l+1)xP_l(x)-lP_{l-1}(x).$$

**导数关系**

$$(1-x^2)P'_l(x)=l\left[P_{l-1}(x)-xP_l(x)\right].$$

**生成函数**

$$\frac{1}{\sqrt{1-2xt+t^2}}=\sum_{l=0}^{\infty}P_l(x)\,t^l.$$

**正交性**

$$\int_{-1}^{1}P_l(x)P_{l'}(x)\,dx=\frac{2}{2l+1}\delta_{ll'}.$$

**加法定理**

$$P_l(\cos\gamma)=P_l(\cos\theta)P_l(\cos\theta')
+2\sum_{m=1}^{l}\frac{(l-m)!}{(l+m)!}P_l^m(\cos\theta)P_l^m(\cos\theta')\cos m(\varphi-\varphi'),$$

其中 $\gamma$ 是 $(\theta,\varphi)$ 与 $(\theta',\varphi')$ 之间的夹角。**展开球面函数时，这条定理能省掉一大半计算。**

## F.3 Hermite 多项式

**递推关系**

$$H_{n+1}(x)=2xH_n(x)-2nH_{n-1}(x).$$

**生成函数**

$$e^{2xt-t^2}=\sum_{n=0}^{\infty}H_n(x)\frac{t^n}{n!}.$$

**正交性**

$$\int_{-\infty}^{\infty}e^{-x^2}H_n(x)H_m(x)\,dx=\sqrt{\pi}\,2^nn!\,\delta_{nm}.$$

**物理出处：** 一维谐振子的波函数，$\psi_n\propto e^{-x^2/2}H_n(x)$。

## F.4 Laguerre 多项式

**递推关系**

$$(n+1)L_{n+1}(x)=(2n+1-x)L_n(x)-nL_{n-1}(x).$$

**生成函数**

$$\frac{1}{1-t}\exp\left(-\frac{xt}{1-t}\right)=\sum_{n=0}^{\infty}L_n(x)\,t^n.$$

**正交性**

$$\int_0^{\infty}e^{-x}L_n(x)L_m(x)\,dx=\delta_{nm}.$$

**连带形式：** 氢原子径向用到 $L_n^m(x)$，满足

$$\int_0^{\infty}x^m e^{-x}L_n^m(x)L_{n'}^m(x)\,dx
=\frac{(n+m)!}{n!}\delta_{nn'}.$$

## F.5 球贝塞尔函数

**与普通 Bessel 的关系**

$$j_l(x)=\sqrt{\frac{\pi}{2x}}J_{l+1/2}(x),\qquad
y_l(x)=\sqrt{\frac{\pi}{2x}}Y_{l+1/2}(x).$$

**递推关系**

$$\frac{2l+1}{x}j_l(x)=j_{l-1}(x)+j_{l+1}(x).$$

**前几个显式形式**

$$j_0(x)=\frac{\sin x}{x},\qquad
j_1(x)=\frac{\sin x}{x^2}-\frac{\cos x}{x},$$

$$y_0(x)=-\frac{\cos x}{x},\qquad
y_1(x)=-\frac{\cos x}{x^2}-\frac{\sin x}{x}.$$

**用途：** 球对称问题的径向解、球面波的展开。

## F.6 什么时候用哪一条

| 要做的事 | 用哪个 |
|---|---|
| 把 $J_{m+1}$ 化成 $J_m$、$J_{m-1}$ | 递推关系 |
| 算 $\int x^mJ_{m-1}dx$ | 带权导数 |
| 求含 Bessel 的级数和 | 生成函数 |
| 按本征函数展开 | 正交性 |
| 球面两点的角距离 | Legendre 加法定理 |
| 谐振子、氢原子波函数 | Hermite、Laguerre |

### 三个"怎么用"的例子

**例一：把 $\int x^2J_1(x)dx$ 算出来。** 用带权导数 $\frac{d}{dx}[x^mJ_m]=x^mJ_{m-1}$，取 $m=2$：$\frac{d}{dx}[x^2J_2]=x^2J_1$。所以积分直接是 $x^2J_2(x)+C$。**不需要分部积分，也不需要查积分表。**

**例二：证明 $J_0'(x)=-J_1(x)$。** 用递推 $J_{m-1}-J_{m+1}=2J_m'$，取 $m=1$：$J_0-J_2=2J_1'$；再用 $J_0+J_2=\frac{2}{x}J_1$ 联立消去 $J_2$，得 $J_1'=J_0-\frac1xJ_1$。这与 $J_0'=-J_1$ 配合，可逐步推出所有低阶导数关系。

**例三：把 $1/|\mathbf r-\mathbf r'|$ 按 Legendre 展开。** 用生成函数 $\frac{1}{\sqrt{1-2xt+t^2}}=\sum P_l(x)t^l$，取 $x=\cos\gamma$、$t=r'/r$，就得到第 3.9 节多极展开用的那个式子。**这也是为什么多极展开的每一项系数都是 Legendre 多项式。**

**一条经验：** 物理里真正需要手算的特殊函数恒等式，九成以上出自上面这几类。剩下的（Hankel 函数、渐近展开的高阶项、积分表示）交给查表或数值库。
