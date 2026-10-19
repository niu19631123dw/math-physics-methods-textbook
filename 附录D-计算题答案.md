# 附录 D 计算题答案

> 只给结果和关键步骤。中间过程留给你自己补。

## 第 1 章

**1-1** 令 $u=x/L$，$f=u(1-u)$。逐项积分得

$$a_n=2\int_0^1 u(1-u)\sin(n\pi u)\,du=\frac{4}{n^3\pi^3}\big[1-(-1)^n\big].$$

奇数 $n$：$a_n=8/(n^3\pi^3)$；偶数 $n$：$a_n=0$。衰减是 $n^{-3}$，因为 $f$ 和它的一阶导数连续，二阶导数在端点有跳变。**一般规则：第 $k$ 阶导数有跳变，系数按 $n^{-(k+2)}$ 衰减。**

**1-2** 把驱动力按本征模展开，第 $n$ 模的等效力幅是 $(2F_0/L)\sin(n\pi x_0/L)$。稳态振幅

$$A_n=\frac{(2F_0/L)\sin(n\pi x_0/L)}{\sqrt{(\omega_n^2-\Omega^2)^2+\gamma^2\Omega^2}}.$$

共振条件 $\Omega\approx\omega_n$。若 $x_0$ 正好是某模的节点，该模不被激发。

**1-3** 令 $u=v+A(x/L)\cos\Omega t$，$v$ 满足齐次边界，方程多出源项 $A(x/L)\Omega^2\cos\Omega t$。展开得

$$v=\sum_n b_n\sin\frac{n\pi x}{L}\cos\Omega t,\qquad
b_n=\frac{2A\Omega^2(-1)^{n+1}}{n\pi(\omega_n^2-\Omega^2)}.$$

共振出现在 $\Omega=\omega_n$，奇数模更强（系数按 $1/n$ 衰减）。

## 第 2 章

**2-1** TM 模：$J_m(k_ca)=0$，$k_c=j_{mn}/a$，最低是 TM$_{01}$，$f_c=2.405c/(2\pi a)$。TE 模：$J'_m(k_ca)=0$，最低是 TE$_{11}$，$f_c=1.841c/(2\pi a)$。**主模是 TE$_{11}$。**

**2-2** 频率 $\omega_{mn}=cj_{mn}/a$。前五个零点：$j_{01}=2.405$，$j_{11}=3.832$，$j_{21}=5.136$，$j_{02}=5.520$，$j_{31}=6.380$。频率比

$$1:1.593:2.136:2.296:2.653.$$

$m\ge1$ 的模式都是二重简并（$+m$ 与 $-m$）。

**2-3** $P_3(\cos\theta)=\frac12(5\cos^3\theta-3\cos\theta)$。零点 $\cos\theta=0,\pm\sqrt{3/5}$，即

$$\theta=90^\circ,\ 39.2^\circ,\ 140.8^\circ.$$

球面上对应一个**赤道平面**（$\theta=90^\circ$）和两个**节锥**（$\theta=39.2^\circ,\ 140.8^\circ$），这些面上振动为零。

## 第 3 章

**3-1** 镜像法：把 $z<0$ 的初始温度取为 $-T_0$，则边界自动为零。结果是

$$T(z,t)=T_0\operatorname{erf}\left(\frac{z}{\sqrt{4\alpha t}}\right).$$

检验：$z=0$ 处恒为 $0$；$t\to0$ 时对 $z>0$ 给出 $T_0$。

**3-2** 把原点取在两电荷中点，$\pm q$ 位于 $\pm\frac{d}{2}\hat z$：

$$\phi=\frac{q}{4\pi\varepsilon_0}\left(\frac{1}{|\mathbf r-\frac{d}{2}\hat z|}-\frac{1}{|\mathbf r+\frac{d}{2}\hat z|}\right)
\approx\frac{qd\cos\theta}{4\pi\varepsilon_0r^2}.$$

偶极矩 $\mathbf p=q\mathbf d$（从 $-q$ 指向 $+q$），$\phi=p\cos\theta/(4\pi\varepsilon_0r^2)$。

**3-3** 总能量是电荷在感应电荷场中的能量的一半：

$$W=\frac12q\,\phi_{\text{ind}}=\frac12q\left(-\frac{q}{4\pi\varepsilon_0\cdot2d}\right)
=-\frac{q^2}{16\pi\varepsilon_0 d}.$$

负号表示系统束缚：把电荷移到无穷远需要做功。对 $d$ 求导得 $F=-q^2/(16\pi\varepsilon_0d^2)$，与直接算镜像力一致。

## 第 4 章

**4-1** 极点是 $z^4=-1$ 的四个根，上半平面两个：$e^{i\pi/4}$、$e^{i3\pi/4}$。对 $f=1/(1+z^4)$，留数 $=1/(4z_0^3)$。于是

$$\int_{-\infty}^{\infty}\frac{dx}{1+x^4}=2\pi i\left(\frac{1}{4z_1^3}+\frac{1}{4z_2^3}\right)=\frac{\pi}{\sqrt2},$$

上式是**全实轴**的积分；被积函数是偶函数，取一半得到：

$$\int_0^\infty\frac{dx}{1+x^4}=\frac{\pi}{2\sqrt2}.$$

只取上半平面是因为要让大半圆上的积分消失：被积函数按 $1/|z|^4$ 衰减，用 ML 估计即可（这里不需要 Jordan 引理，那条引理是给 $e^{iaz}$ 型振荡积分用的）。

**4-2** 被积函数是偶函数。考虑 $ze^{iaz}/(z^2+b^2)$，上半平面极点 $z=ib$，留数 $e^{-ab}/2$。取虚部再取一半：

$$\int_0^\infty\frac{x\sin(ax)}{x^2+b^2}\,dx=\frac{\pi}{2}e^{-ab}.$$

**4-3** 取 $f(z)=\pi\cot(\pi z)/z^2$。在 $z=\pm n$ 处留数为 $1/n^2$；在 $z=0$ 处

$$\frac{\pi\cot(\pi z)}{z^2}=\frac{1}{z^3}-\frac{\pi^2}{3z}-\cdots\Rightarrow \operatorname{Res}=-\frac{\pi^2}{3}.$$

回路积分等于零，于是

$$-\frac{\pi^2}{3}+2\sum_{n=1}^\infty\frac{1}{n^2}=0
\Rightarrow\sum_{n=1}^\infty\frac{1}{n^2}=\frac{\pi^2}{6}.$$

## 第 5 章

**5-1** 变换后 $\tilde u(k,t)=e^{-ikx_0}e^{-\alpha k^2t}$，逆变换得

$$u(x,t)=\frac{1}{\sqrt{4\pi\alpha t}}\exp\left(-\frac{(x-x_0)^2}{4\alpha t}\right).$$

这就是热核。

**5-2** $u(t)=1-e^{-t/RC}$。10% 对应 $t_1=RC\ln(10/9)\approx0.105RC$，90% 对应 $t_2=RC\ln10\approx2.303RC$。上升时间

$$t_r\approx2.2RC.$$

**5-3** Nyquist 要求 $f_s\ge2\times1.3=2.6\ \text{kHz}$。若用 $1\ \text{kHz}$，混叠频率为

$$|1300-1000|=300\ \text{Hz}.$$

这就是为什么采样前必须先做抗混叠滤波：一旦混叠，事后无法从数据里分辨。
## 第 6 章

**6-1** 圆柱面 $r=a$ 上，线元 $ds^2=a^2d\theta^2+dz^2$，路径长度

$$L=\int\sqrt{a^2\dot\theta^2+\dot z^2}\,d\theta.$$

被积函数不显含自变量 $\theta$，Euler–Lagrange 给 $\dot z/\sqrt{a^2\dot\theta^2+\dot z^2}=\text{const}$，即 $\dot z=\text{const}$，所以 $z\propto\theta$：螺旋线。

**6-2** 对摆线 $x=a(\theta-\sin\theta)$、$y=a(1-\cos\theta)$，有 $y'=\cot(\theta/2)$，于是

$$y(1+y'^2)=a(1-\cos\theta)\csc^2\frac{\theta}{2}=2a.$$

Beltrami 恒等式给出 $F-y'F_{y'}=\text{const}$，对 $F=\sqrt{1+y'^2}/\sqrt{2gy}$ 即 $y(1+y'^2)=\text{const}$。摆线满足它，所以是最速降线的解。

**6-3** 取 $y=\sin(\pi x/L)$：

$$\int_0^L y'^2dx=\frac{\pi^2}{2L},\qquad \int_0^L y^2dx=\frac{L}{2},$$

所以 $R=\pi^2T/(\rho L^2)$，恰好等于 $\lambda_1$。原因是 $\sin(\pi x/L)$ 本身就是第一本征函数，Rayleigh 商在极小元处取极小值。

**6-4** 约束 $\int\sqrt{1+y'^2}dx=l$。带乘子的被积函数 $F=(y+\lambda)\sqrt{1+y'^2}$。Beltrami 恒等式给 $F-y'F_{y'}=\text{const}$，即

$$\frac{y+\lambda}{\sqrt{1+y'^2}}=a,$$

解出

$$y+\lambda=a\cosh\frac{x-b}{a},$$

即悬链线。**中间步骤：** 由 $(y+\lambda)/\sqrt{1+y'^2}=a$ 解出 $y'$：

$$y'=\pm\frac{\sqrt{(y+\lambda)^2-a^2}}{a},$$

分离变量积分 $\int\frac{a\,d(y+\lambda)}{\sqrt{(y+\lambda)^2-a^2}}=\pm\int dx$，左边是 $a\operatorname{arcosh}\frac{y+\lambda}{a}$，于是 $y+\lambda=a\cosh\frac{x-b}{a}$。$a,b,\lambda$ 由端点条件和长度约束定。
## 第 7 章

**7-1** 极坐标 $g_{rr}=1$、$g_{\theta\theta}=r^2$，逆度规 $g^{rr}=1$、$g^{\theta\theta}=1/r^2$。只有 $\partial_r g_{\theta\theta}=2r$ 非零，代入

$$\Gamma^\mu_{\nu\lambda}=\frac12 g^{\mu\rho}\left(\partial_\nu g_{\rho\lambda}+\partial_\lambda g_{\nu\rho}-\partial_\rho g_{\nu\lambda}\right)$$

得到三个非零分量：

$$\Gamma^r_{\theta\theta}=-r,\qquad \Gamma^\theta_{r\theta}=\Gamma^\theta_{\theta r}=\frac1r.$$

其余五个为零。验证：取直角坐标匀速直线 $x=Vt$、$y=y_0$，换到极坐标 $r=\sqrt{x^2+y^2}$、$\theta=\arctan(y/x)$，直接代入

$$\ddot r=r\dot\theta^2,\qquad \ddot\theta=-\frac{2}{r}\dot r\dot\theta$$

两者恒成立（数值上残差为 0）。

**7-2** 用 7-1 的三个 $\Gamma$ 逐个算 $R^\rho_{\sigma\mu\nu}$。以 $R^r_{\theta r\theta}$ 为例：

$$R^r_{\theta r\theta}=\partial_r\Gamma^r_{\theta\theta}-\partial_\theta\Gamma^r_{r\theta}
+\Gamma^r_{r\lambda}\Gamma^\lambda_{\theta\theta}-\Gamma^r_{\theta\lambda}\Gamma^\lambda_{r\theta}
=-1-0+0-\left(\frac1r\right)(-r)=0.$$

其余分量同理相消。**所有分量都为零，说明平面在极坐标下依然是平直的。**

**7-3** 球面 $ds^2=a^2(d\theta^2+\sin^2\theta\,d\varphi^2)$，即 $g_{\theta\theta}=a^2$、$g_{\varphi\varphi}=a^2\sin^2\theta$。只有

$$\Gamma^\theta_{\varphi\varphi}=-\sin\theta\cos\theta,\qquad
\Gamma^\varphi_{\theta\varphi}=\Gamma^\varphi_{\varphi\theta}=\cot\theta.$$

由对称性 $R_{\theta\varphi\theta\varphi}=a^2\sin^2\theta$，缩并得

$$R_{\theta\theta}=\frac{R_{\theta\varphi\theta\varphi}}{g_{\varphi\varphi}}=1,\qquad
R_{\varphi\varphi}=a^2\sin^2\theta,$$

$$R=g^{\theta\theta}R_{\theta\theta}+g^{\varphi\varphi}R_{\varphi\varphi}
=\frac{1}{a^2}+\frac{1}{a^2}=\frac{2}{a^2}.$$

**7-4** 由第二 Bianchi 恒等式缩并得 $\nabla^\mu R_{\mu\nu}=\frac12\nabla_\nu R$，所以 $R_{\mu\nu}$ 本身不守恒。又由 $\nabla_\lambda g_{\mu\nu}=0$，

$$\nabla^\mu\left(R_{\mu\nu}-\frac12Rg_{\mu\nu}\right)
=\frac12\nabla_\nu R-\frac12\nabla_\nu R=0.$$

于是 $G_{\mu\nu}$ 守恒，这是引入这一项的真正理由。

**关于迹：** 在 $n$ 维中，$g^{\mu\nu}G_{\mu\nu}=R-\frac n2 R$。所以**四维时迹是 $-R$，不是零**。零迹的是 $R_{\mu\nu}-\frac14Rg_{\mu\nu}$（无迹版本）。本题要验证的是守恒性，不是迹为零。

**7-5** 平行移动绕环形变方向，说明存在曲率：这是曲率的等价定义（$[\nabla_\mu,\nabla_\nu]\propto R$）。反过来不一定：曲率张量非零，但在特定路径上绕一圈仍可能回到原方向（例如沿对称轴绕圈）。所以「绕一圈变了 ⇒ 弯的」成立，「没变 ⇒ 平的」不一定成立。

**7-6** 不能。$\Gamma=0$ 只在一点成立，曲率是 $\Gamma$ 一阶导数的组合，可以非零。局部令 $\Gamma=0$ 只是把一个点附近的「一阶」信息消掉，二阶信息（曲率）不可消除。这就是等效原理「局部」二字的准确含义。

**7-7** Einstein 方程 10 个分量，第二 Bianchi 恒等式自动保证 4 个不独立，剩下 6 个独立方程。这 4 个不独立的对应**坐标选择**（规范自由度），不是物理自由度。对无质量引力波，经过规范固定后只剩 **2 个物理偏振态**（$+$ 与 $\times$）。
