# 附录 C 习题详解

> 每题给关键步骤、中间结果和最终答案。缺的步骤请自己补全后再看。

## 第 1 章

> 每题的写法固定：**思路**（这一步为什么这么做）→ **过程**（代数逐步写开）→ **结果**（单独成行）→ **检验**（量纲、极限或已知结果）→ **读法**（物理含义，仅计算题）。

**1.1** **思路**：不解方程，直接把 $F(x-ct)$ 代进一阶算子；再把「算子作用为零」翻译成几何语言。

**过程**：令 $u=F(x-ct)$。由链式法则，对 $t$ 求导时内部多乘一个 $-c$：

$$
\frac{\partial u}{\partial t}=F'(x-ct)\cdot(-c),\qquad
\frac{\partial u}{\partial x}=F'(x-ct)\cdot 1 .
$$

代入方程：

$$
\frac{\partial u}{\partial t}+c\frac{\partial u}{\partial x}
=-cF'(x-ct)+cF'(x-ct)=0 .
$$

反过来，若 $\frac{\partial u}{\partial t}+c\frac{\partial u}{\partial x}=0$，就沿 $\mathrm{d}x/\mathrm{d}t=c$ 的路线走，此时

$$
\frac{\mathrm{d}u}{\mathrm{d}t}
=\frac{\partial u}{\partial t}+\frac{\mathrm{d}x}{\mathrm{d}t}\frac{\partial u}{\partial x}
=\frac{\partial u}{\partial t}+c\frac{\partial u}{\partial x}=0 .
$$

所以 $u$ 在每一条 $x-ct=$ 常数的线上取同一个值，$u$ 只能依赖这一族线的标号 $x-ct$。

**结果**：$u=F(x-ct)$ 满足 $\frac{\partial u}{\partial t}+c\frac{\partial u}{\partial x}=0$；反之该方程的解必为 $u=F(x-ct)$。

**检验**：取 $F(s)=s^{2}$，$u=(x-ct)^{2}$，则 $\frac{\partial u}{\partial t}=-2c(x-ct)$、$\frac{\partial u}{\partial x}=2(x-ct)$，相加恰为零 ✓。量纲上 $ct$ 与 $x$ 同为米，可以相减 ✓。

**读法**：一阶方程只允许一个方向的传播，所以它比波动方程"窄"；而"沿特征线取常值"与"$u=F(x-ct)$"是同一句话的两种写法——前者是几何，后者是代数。

**1.2** **思路**：初速为零，达朗贝尔公式只剩位移项；由对称性，极大值点只可能是中点或两个分裂出来的峰，一个一个比。

**过程**：$u=\dfrac{h}{2}\left[e^{-(x-ct)^{2}/a^{2}}+e^{-(x+ct)^{2}/a^{2}}\right]$。记 $s=ct$，$u$ 是 $x$ 的偶函数，所以 $x=0$ 必是驻点，值

$$
u(0,t)=h\,e^{-s^{2}/a^{2}} .
$$

另一族驻点在 $x=\pm s$ 附近（两峰完全分开时精确地在那里），值

$$
u(\pm s,t)=\frac{h}{2}\left(1+e^{-4s^{2}/a^{2}}\right).
$$

两者相等时转折，令 $\tau=s^{2}/a^{2}$，解 $e^{-\tau}=\frac{1}{2}(1+e^{-4\tau})$：$\tau\approx0.56$，即 $ct\approx0.75a$。

**结果**：
- $ct\ll a$：峰在 $x=0$，高 $h\,e^{-c^{2}t^{2}/a^{2}}\approx h$；
- $ct\gg a$：两个峰在 $x=\pm ct$，各高 $h/2$；
- 转折在 $ct\approx0.75a$。数值核对：$ct/a=0.4$ 时峰在 $0$、高 $0.852h$；$ct/a=1$ 时峰在 $\pm0.96a$、高 $0.510h$；$ct/a=2$ 时峰在 $\pm2a$、高 $0.500h$。

**检验**：$t=0$ 时两项重合，$u=h e^{-x^{2}/a^{2}}=f(x)$ ✓。总"面积"守恒：$\int u\,\mathrm{d}x=ha\sqrt{\pi}=\int f\,\mathrm{d}x$（两个半峰各带一半）✓。

**读法**：扰动既不衰减也不变形，只是对半分裂、以 $c$ 分开；弦上任何一点最终都会回到原位并永久静止——传播的是形状，不是物质。

**1.3** **思路**：初始位移为零、初速非零，所以解只由达朗贝尔公式的积分项给出；积分就是一维"重叠长度"。

**过程**：$u=\dfrac{1}{2c}\int_{x-ct}^{x+ct}g(s)\,\mathrm{d}s$。$g$ 只在 $[-a,a]$ 上等于 $v_{0}$，故

$$
u=\frac{v_{0}}{2c}\times\big([x-ct,\,x+ct]\text{ 与 }[-a,a]\text{ 的重叠长度}\big).
$$

设 $ct>a$，按区间端点与 $[-a,a]$ 的位置分三段：

$$
u(x,t)=
\begin{cases}
\dfrac{v_{0}a}{c}, & |x|<ct-a,\\[6pt]
\dfrac{v_{0}}{2c}\big(a+ct-|x|\big), & ct-a<|x|<ct+a,\\[6pt]
0, & |x|>ct+a .
\end{cases}
$$

（$ct<a$ 时把第一段的 $ct-a$ 换成 $a-ct$，图形是一个还没裂开的平台。）

**结果**：最大位移 $u_{\max}=\dfrac{v_{0}a}{c}=1.25\ \mathrm{mm}$（取 $v_{0}=5.0\ \mathrm{m/s}$、$a=0.10\ \mathrm{m}$、$c=4.0\times10^{2}\ \mathrm{m/s}$）。弦**不回到平衡**：平台高度不变、宽度 $2(ct-a)$ 无限增长。

**检验**：量纲 $\dfrac{\mathrm{m/s}\cdot\mathrm{m}}{\mathrm{m/s}}=\mathrm{m}$ ✓。再看能量：平台内 $\frac{\partial u}{\partial t}=\frac{\partial u}{\partial x}=0$，能量为零，全部能量锁在两侧固定宽度的斜坡里，总量不随时间变 ✓——这与"平台越铺越宽却不耗能"自洽。

**读法**：初速的净冲量 $\int g\,\mathrm{d}x=v_{0}\cdot 2a\neq0$，在无限长弦上没有东西把它拉回去，于是整条弦被抬高一个台阶。有限长弦不行：固定端会把斜坡反射回来，平台从墙边开始被"啃掉"。

**1.4** **思路**：初速为零，直接套达朗贝尔公式；再用积化和差把两项合并成驻波，看它为什么不动。

**过程**：

$$
u=\frac{1}{2}\big[\sin k(x-ct)+\sin k(x+ct)\big]
=\frac{1}{2}\cdot 2\sin(kx)\cos(kct)=\sin(kx)\cos(\omega t),
$$

其中用了 $\sin A+\sin B=2\sin\frac{A+B}{2}\cos\frac{A-B}{2}$，并记 $\omega=kc$。

**结果**：$u(x,t)=\sin(kx)\cos(\omega t)$，$\omega=ck$，即 $f=\dfrac{c}{\lambda}$、$\lambda=\dfrac{2\pi}{k}$。

**检验**：$t=0$ 复原 $f$ ✓；$x=0$ 与 $x=\pi/k$ 处恒为零（波节），与驻波图像一致 ✓；把两项分别看，是等幅反向的两个行波，它们的能流在 1.11 题里会互相抵消。

**读法**：这个解"站在原地"是因为两个反向行波时时处处等大反相：空间图样 $\sin kx$ 固定，只有整体幅度按 $\cos\omega t$ 涨落——这就是驻波与行波的区别。

**1.5** **思路**：先把 $k$、$\omega$、$c$、$Z$ 四个量算出来，再代 1.6 节的两个密度公式；$j=ce$ 的验证靠 $T=\rho c^{2}$ 这一条。

**过程**：

$$
c=\sqrt{\frac{T}{\rho}}=418\ \mathrm{m/s},\quad
k=\frac{2\pi}{\lambda}=12.6\ \mathrm{m^{-1}},\quad
\omega=ck=5.26\times10^{3}\ \mathrm{s^{-1}},\quad
Z=\sqrt{T\rho}=0.167\ \mathrm{kg/s}.
$$

行波的动能、势能密度相等：

$$
e_{k}=e_{p}=\frac{1}{2}\rho\omega^{2}A^{2}\sin^{2}(kx-\omega t),
$$

峰值 $\frac{1}{2}\times4.0\times10^{-4}\times(5.26\times10^{3})^{2}\times(10^{-3})^{2}=5.5\times10^{-3}\ \mathrm{J/m}$。总能流

$$
j=ce=c\cdot 2e_{k}\Big|_{\text{峰}}=418\times1.1\times10^{-2}=4.6\ \mathrm{W}.
$$

平均功率（$\langle\sin^{2}\rangle=1/2$）：

$$
\bar j=\frac{1}{2}Z\omega^{2}A^{2}=\frac{1}{2}\times0.167\times2.76\times10^{7}\times10^{-6}=2.3\ \mathrm{W}.
$$

**结果**：$e_{k}=e_{p}=5.5\times10^{-3}\ \mathrm{J/m}$（峰值），$j$ 峰值 $4.6\ \mathrm{W}$，平均功率 $2.3\ \mathrm{W}$。

**检验**：$\bar j=j_{\text{峰}}/2$，因为 $\sin^{2}$ 的平均值是 $1/2$ ✓。换一条路核对：速度幅值 $v_{\max}=\omega A=5.3\ \mathrm{m/s}$，功率 $=\frac12Zv_{\max}^{2}=\frac12\times0.167\times27.6=2.3\ \mathrm{W}$ ✓。量纲 $\mathrm{kg/s}\cdot\mathrm{m^{2}/s^{2}}=\mathrm{W}$ ✓。

**读法**：弦上传多少功率，只由阻抗与速度幅值决定；$P\propto\omega^{2}A^{2}$，所以"高频、大振幅"的拨弦功率涨得极快——这就是尖锐拨弦更容易激发高频的原因。

**1.6** **思路**：纯模式代进 $e_{k}$、$e_{p}$、$j$ 的定义；能流积分为零靠 $\sin(2kx)$ 在 $[0,L]$ 上是整周期。

**过程**：$u=A\sin(kx)\cos(\omega t)$，$k=n\pi/L$。于是

$$
\frac{\partial u}{\partial t}=-A\omega\sin(kx)\sin(\omega t),\qquad
\frac{\partial u}{\partial x}=Ak\cos(kx)\cos(\omega t).
$$

代入两个密度：

$$
e_{k}=\frac{1}{2}\rho A^{2}\omega^{2}\sin^{2}(kx)\sin^{2}(\omega t),\qquad
e_{p}=\frac{1}{2}TA^{2}k^{2}\cos^{2}(kx)\cos^{2}(\omega t)
=\frac{1}{2}\rho A^{2}\omega^{2}\cos^{2}(kx)\cos^{2}(\omega t),
$$

最后一步用了 $Tk^{2}=\rho\omega^{2}$。能流：

$$
j=-T\frac{\partial u}{\partial x}\frac{\partial u}{\partial t}
=TA^{2}k\omega\sin(kx)\cos(kx)\sin(\omega t)\cos(\omega t)
=\frac{1}{2}TA^{2}k\omega\sin(2kx)\sin(2\omega t).
$$

(b) 积分：$\int_{0}^{L}\sin(2kx)\,\mathrm{d}x=\dfrac{1-\cos(2kL)}{2k}$，而 $2kL=2n\pi$，故为零。

(c) 总能量：

$$
E=\int_{0}^{L}(e_{k}+e_{p})\,\mathrm{d}x
=\frac{\rho A^{2}\omega^{2}}{2}\left[\frac{L}{2}\sin^{2}(\omega t)+\frac{L}{2}\cos^{2}(\omega t)\right]
=\frac{\rho\omega^{2}A^{2}L}{4}.
$$

**结果**：$E=\dfrac{\rho\omega^{2}A^{2}L}{4}$，与 $t$ 无关；$\int_{0}^{L}j\,\mathrm{d}x=0$。

**检验**：取 $n=1$，$\omega_{1}=\pi c/L$，得 $E=\dfrac{\pi^{2}TA^{2}}{4L}$，与 1.6.5 的 $E_{n}$ 公式（$b_{n}=0$）逐字相同 ✓。量纲 $\mathrm{J/m^{3}}\cdot\mathrm{m^{2}}\cdot\mathrm{m}=\mathrm{J}$ ✓。

**读法**：驻波不输运能量，能量只在动能与势能之间来回倒；这也是"净能流为零、但局部能流不为零"的典型。

**1.7** **思路**：拨弦的三角形初值只能靠投影积分求系数；偶数阶为零不需要积分，用"节点"就能说清。

**过程**：初值

$$
f(x)=\begin{cases}\dfrac{2h}{L}x, & 0\le x\le\dfrac{L}{2},\\[8pt]
\dfrac{2h}{L}(L-x), & \dfrac{L}{2}\le x\le L .\end{cases}
$$

先算前半段，令 $\theta=\dfrac{n\pi x}{L}$，则 $\mathrm{d}x=\dfrac{L}{n\pi}\mathrm{d}\theta$、$x=\dfrac{L}{n\pi}\theta$：

$$
\int_{0}^{L/2}x\sin\frac{n\pi x}{L}\,\mathrm{d}x
=\left(\frac{L}{n\pi}\right)^{2}\int_{0}^{n\pi/2}\theta\sin\theta\,\mathrm{d}\theta
=\left(\frac{L}{n\pi}\right)^{2}\left[-\frac{n\pi}{2}\cos\frac{n\pi}{2}+\sin\frac{n\pi}{2}\right].
$$

（用了 $\int\theta\sin\theta\,\mathrm{d}\theta=-\theta\cos\theta+\sin\theta$。）后半段做 $x\to L-x$ 替换，与前段同值。两段相加：

$$
a_{n}=\frac{2}{L}\cdot 2\cdot\frac{2h}{L}\int_{0}^{L/2}x\sin\frac{n\pi x}{L}\mathrm{d}x
=\frac{8h}{n^{2}\pi^{2}}\sin\frac{n\pi}{2}.
$$

能量：$E_{n}=\dfrac{n^{2}\pi^{2}T}{4L}a_{n}^{2}=\dfrac{16Th^{2}}{n^{2}\pi^{2}L}\sin^{2}\dfrac{n\pi}{2}$，只有奇数阶非零。总和

$$
E=\sum_{n\ \text{奇}}\frac{16Th^{2}}{n^{2}\pi^{2}L}
=\frac{16Th^{2}}{\pi^{2}L}\cdot\frac{\pi^{2}}{8}=\frac{2Th^{2}}{L}.
$$

**结果**：$a_{n}=\dfrac{8h}{n^{2}\pi^{2}}\sin\dfrac{n\pi}{2}$（偶数阶为零）；$\dfrac{E_{1}}{E}=\dfrac{8}{\pi^{2}}=81\%$，$\dfrac{E_{3}}{E}=\dfrac{8}{9\pi^{2}}=9.0\%$。

**检验**：用直接积分核对总能量：两段斜率都是 $\pm2h/L$，$\frac{T}{2}\int(f')^{2}\mathrm{d}x=\frac{T}{2}\cdot\frac{4h^{2}}{L^{2}}\cdot L=\frac{2Th^{2}}{L}$，与级数求和一致 ✓。再对 $h$ 的量纲：$Th^{2}/L=\mathrm{N\cdot m^{2}/m}=\mathrm{J}$ ✓。

**读法**：偶次模在 $x=L/2$ 处都有节点，而拨点正在那里，所以一个都激发不起来；能量 81% 集中在基频，这就是"听起来是一个音"的定量来源。

**1.8** **思路**：固定端用奇延拓把半无限弦变成无限弦，剩下的只是把初值写成一个"窗函数"再按区间分情况。

**过程**：记 $\chi(s)=1$（$a<s<2a$）、否则为 $0$。初值在 $x>0$ 上是 $h\chi$，奇延拓成

$$
f_{\text{odd}}(s)=\begin{cases}h\chi(s), & s>0,\\ -h\chi(-s), & s<0 .\end{cases}
$$

则 $u=\frac{1}{2}[f_{\text{odd}}(x-ct)+f_{\text{odd}}(x+ct)]$。对 $x>0$，$x+ct>0$ 恒成立，所以第二项 $=h\chi(x+ct)$；第一项要看 $x$ 与 $ct$ 谁大。取足够晚的时刻 $ct>2a$，此时 $x+ct>2a$，第二项为零，只剩

$$
u=\begin{cases}
\dfrac{h}{2}\chi(x-ct), & x>ct,\\[6pt]
-\dfrac{h}{2}\chi(ct-x), & x<ct .
\end{cases}
$$

于是弦上是两个高 $h/2$ 的方台阶：

$$
u=\begin{cases}
-\dfrac{h}{2}, & ct-2a<x<ct-a\ (\text{反射的}),\\[6pt]
+\dfrac{h}{2}, & ct+a<x<ct+2a\ (\text{出射的}),\\[6pt]
0, & \text{其余}.
\end{cases}
$$

**结果**：$ct>2a$ 时弦上只有这两个台阶，一正一负各高 $h/2$；反射台阶在 $ct=4a$ 到达 $x=3a$（条件 $ct-2a<3a<ct-a$ 给出 $4a<ct<5a$）。

**检验**：端点 $x=0$ 处 $u=\frac{h}{2}[-\chi(ct)+\chi(ct)]=0$，边界条件自动满足 ✓。能量：两个台阶的势能由各自的斜坡贡献，总量等于初始的一半加一半，守恒 ✓。

**读法**：撞墙之后，弦上永远同时存在"跑出去的那一半"和"倒相回来的那一半"；固定端的签名就是那个负号。

**1.9** **思路**：与上题同一套延拓，只是换成偶延拓（固定端→自由端），所以两项同号，全部符号变正。

**过程**：偶延拓 $f_{\text{even}}(s)=h\chi(|s|)$，于是

$$
u=\frac{1}{2}\big[h\chi(|x-ct|)+h\chi(|x+ct|)\big].
$$

在端点 $x=0$：

$$
u(0,t)=\frac{h}{2}\big[\chi(ct)+\chi(ct)\big]=h\,\chi(ct),
$$

即当 $a<ct<2a$ 时 $u(0,t)=h$，其余时刻为零。

**结果**：$ct>2a$ 时弦上是两个**同号**、各高 $h/2$ 的台阶（$x\in(ct-2a,ct-a)$ 与 $(ct+a,ct+2a)$）；端点位移在 $\dfrac{a}{c}<t<\dfrac{2a}{c}$ 期间恰好等于 $h$，是入射台阶高度的两倍。

**检验**：$ct<a$ 时 $\chi(ct)=0$，端点静止 ✓；$ct>2a$ 时回到零 ✓；端点速度在临界时刻有限，无冲量 ✓。

**读法**：自由端把入射与镜像叠加，位移瞬时加倍，但并没有能量加倍——入射的那一份继续以反射波的形式离开（1.6.3 已证端点不吸能）。

**1.10** **思路**：接头处两条条件（位移连续、横向力连续）就能解出 $R$、$S$；把 $R$、$S$ 换成阻抗最省事。

**过程**：$Z=\sqrt{T\rho}$（单位 $\mathrm{kg/s}$），$\rho_{2}=4\rho_{1}$ 给出 $Z_{2}=2Z_{1}$。由 1.7.3 的公式

$$
R=\frac{Z_{1}-Z_{2}}{Z_{1}+Z_{2}}=\frac{1-2}{1+2}=-\frac{1}{3},
\qquad
S=1+R=\frac{2}{3}.
$$

能量：入射通量 $Z_{1}v^{2}$，反射 $Z_{1}R^{2}v^{2}$，透射 $Z_{2}S^{2}v^{2}$，所以反射率与透射率分别是

$$
\frac{Z_{1}R^{2}v^{2}}{Z_{1}v^{2}}=\frac{1}{9},
\qquad
\frac{Z_{2}S^{2}v^{2}}{Z_{1}v^{2}}=2\times\frac{4}{9}=\frac{8}{9}.
$$

**结果**：$R=-\dfrac{1}{3}$，$S=\dfrac{2}{3}$，能量反射 $11\%$、透射 $89\%$。

**检验**：两个能量分数相加 $=\frac{1}{9}+\frac{8}{9}=1$ ✓。取极限 $Z_{2}\to\infty$，$R\to-1$、透射 $\to0$，退化为固定端 ✓。位移连续要求 $1+R=S$：$1-\frac13=\frac23$ ✓。

**读法**：密度大的一侧像一堵"软墙"——倒相，但只把一小部分能量弹回来；绝大部分继续往前走，这就是为什么接一根更粗的弦，声音只是变闷而不是全反射。

**1.11** **思路**：先用积化和差看清这是驻波，再套 1.6.4 的能流公式，最后看 $\sin(2kx)$ 在整周期上的积分。

**过程**：

$$
u=\cos(kx-\omega t)+\cos(kx+\omega t)=2\cos(kx)\cos(\omega t),
$$

用了 $\cos A+\cos B=2\cos\frac{A+B}{2}\cos\frac{A-B}{2}$。于是 $u_{t}=-2\omega\cos kx\sin\omega t$、$u_{x}=-2k\sin kx\cos\omega t$，能流

$$
j=-T u_{x}u_{t}=-T(2k\sin kx\cos\omega t)(-2\omega\cos kx\sin\omega t)
=2Tk\omega\sin kx\cos kx\sin\omega t\cos\omega t
=\frac{1}{2}Tk\omega\sin(2kx)\sin(2\omega t).
$$

对 $x$ 积分：

$$
\int_{0}^{L}j\,\mathrm{d}x=\frac{1}{2}Tk\omega\sin(2\omega t)\int_{0}^{L}\sin(2kx)\,\mathrm{d}x
=\frac{1}{2}Tk\omega\sin(2\omega t)\cdot\frac{1-\cos(2kL)}{2k}=0,
$$

因为 $2kL=2n\pi$。

**结果**：$u=2\cos(kx)\cos(\omega t)$；净能流为零，$j(x,t)=\frac12Tk\omega\sin(2kx)\sin(2\omega t)$。

**检验**：$j$ 关于 $x=L/2$ 反号，左右两半的能流等大反向，逐点抵消 ✓；这与第 1.6 题"纯模式总能量不变"是同一件事。

**读法**：两个反向行波各自的能流都非零，但处处相反；叠加之后只剩"能量在原地从一半倒到另一半"，没有净输运。

**1.12** **思路**：先把 $c$ 算出来，其余量都是它的简单倍数；最后用 $1/(2L/c)=c/2L$ 检查自洽。

**过程**：

$$
c=\sqrt{\frac{T}{\rho}}=\sqrt{\frac{70}{4.0\times10^{-4}}}=4.18\times10^{2}\ \mathrm{m/s},
$$

$$
f_{1}=\frac{c}{2L}=\frac{418}{1.30}=322\ \mathrm{Hz},\qquad
f_{5}=5f_{1}=1.61\times10^{3}\ \mathrm{Hz},
$$

往返一次的路程是 $2L$：

$$
T_{\text{往返}}=\frac{2L}{c}=\frac{1.30}{418}=3.11\times10^{-3}\ \mathrm{s}.
$$

**结果**：$c=4.18\times10^{2}\ \mathrm{m/s}$，$f_{1}=322\ \mathrm{Hz}$，$f_{5}=1.61\ \mathrm{kHz}$，往返时间 $3.11\ \mathrm{ms}$。

**检验**：$\dfrac{1}{3.11\times10^{-3}\ \mathrm{s}}=322\ \mathrm{Hz}=f_{1}$ ✓——往返时间正好是一个基频周期，这就是"往返闭合"与"$kL=n\pi$"等价的算术版本。量纲 $\mathrm{m}/(\mathrm{m/s})=\mathrm{s}$ ✓。

**读法**：弦上只有"能被两端来回反射拼出驻波"的那些频率；基频就是往返一趟刚好一个周期的那一个，泛音则是把这一趟切成整数份。

**1.13** **思路**：$f\propto\sqrt{T}$，所以把目标频率平方之比乘到原张力上；非线性直接对 $f=\frac{1}{2L}\sqrt{T/\rho}$ 求导就看出来了。

**过程**：由 $f=\dfrac{c}{2L}=\dfrac{1}{2L}\sqrt{\dfrac{T}{\rho}}$，频率与张力的平方根成正比：

$$
\frac{T'}{T}=\left(\frac{f'}{f}\right)^{2}
=\left(\frac{329.6}{322}\right)^{2}=1.047 .
$$

所以 $T'=70\times1.047=73.3\ \mathrm{N}$。

**结果**：$T'=73.3\ \mathrm{N}$（比原来大 $4.7\%$）。

**检验**：两端平方回来：$\sqrt{73.3/70}=1.0234$，$322\times1.0234=329.6$ ✓。量纲：$\sqrt{\mathrm{N}/(\mathrm{kg/m})}=\mathrm{m/s}$ ✓。

**读法**：微分一次得 $\dfrac{\Delta f}{f}=\dfrac{1}{2}\dfrac{\Delta T}{T}$——张力变 $4.7\%$，频率才变 $2.3\%$，所以拧弦轴时"越拧越不灵"，调音必须小步多次。

**1.14** **思路**：两端固定时弦长不变，热膨胀被约束，全部转成张力下降；再把这个 $\Delta T$ 换算成音分。

**过程**：横截面积 $A=\dfrac{\pi d^{2}}{4}=\dfrac{\pi(0.40\times10^{-3})^{2}}{4}=1.26\times10^{-7}\ \mathrm{m^{2}}$，所以 $EA=2.0\times10^{11}\times1.26\times10^{-7}=2.5\times10^{4}\ \mathrm{N}$。自由膨胀应变 $\alpha\Delta\Theta=1.2\times10^{-5}\times10=1.2\times10^{-4}$，被约束后变成张力变化

$$
\Delta T=-EA\,\alpha\Delta\Theta=-2.5\times10^{4}\times1.2\times10^{-4}=-3.0\ \mathrm{N}.
$$

新张力 $66.98\ \mathrm{N}$，频率比

$$
\frac{f'}{f}=\sqrt{\frac{66.98}{70}}=0.9782
\quad\Longrightarrow\quad
1200\log_{2}0.9782=-38\ \text{音分}.
$$

**结果**：张力降 $3.0\ \mathrm{N}$（$-4.3\%$），音高降约 $38$ 音分（近半个半音）。

**检验**：用 1.13 的线性化核对：$\frac{\Delta f}{f}=\frac12\frac{\Delta T}{T}=\frac12(-0.043)=-0.0215$，换成音分 $1200\times\frac{-0.0215}{\ln2}=-37$，与 $-38$ 一致 ✓（差的那 1 音分来自平方根的非线性）。

**读法**：温度一变，整根弦一起走音，而且偏低——这就是为什么乐队上台前要"暖手"、钢琴要等场灯热起来再调。

**1.15** **思路**：(a) 用许用应力定最大张力，再算频率；(b) 频率只依赖 $T/\rho$，所以降频有两条路，用 $B\propto1/T$ 判断哪条不毁音色。

**过程**：(a) $A=\dfrac{\pi(1.5\times10^{-3})^{2}}{4}=1.77\times10^{-6}\ \mathrm{m^{2}}$，线密度 $\rho=7800\times1.77\times10^{-6}=1.38\times10^{-2}\ \mathrm{kg/m}$，

$$
T_{\max}=\sigma A=8.0\times10^{8}\times1.77\times10^{-6}=1.41\times10^{3}\ \mathrm{N},
$$

$$
c=\sqrt{\frac{1.41\times10^{3}}{1.38\times10^{-2}}}=3.20\times10^{2}\ \mathrm{m/s},
\qquad
f_{1}=\frac{c}{2L}=\frac{320}{2.4}=133\ \mathrm{Hz}.
$$

(b) 要到 $27.5\ \mathrm{Hz}$，需 $c=2Lf=66\ \mathrm{m/s}$，即 $T/\rho$ 降到原来的 $(66/320)^{2}=\frac{1}{23.5}$。两条路：

- 把张力降到 $60\ \mathrm{N}$：$B=\dfrac{\pi^{2}EI}{TL^{2}}$，$B$ 放大 $23.5$ 倍；
- 把线密度加到 $0.32\ \mathrm{kg/m}$（缠铜）：$T$ 不变，$B$ 不变。

**结果**：(a) 裸钢丝最低约 $1.3\times10^{2}\ \mathrm{Hz}$（$L=1.2\ \mathrm{m}$、$d=1.5\ \mathrm{mm}$、许用 $800\ \mathrm{MPa}$）；(b) 必须加质量：$B$ 保持 $2.4\times10^{-4}$，降张力则 $B$ 升到 $5.7\times10^{-3}$。

**检验**：量纲 $\sqrt{\mathrm{Pa}\cdot\mathrm{m^{2}}/(\mathrm{kg/m})}=\mathrm{m/s}$ ✓；$B$ 无量纲 ✓。极限核对：$d\to0$ 时 $I\propto d^{4}$、$\rho\propto d^{2}$，$B\propto d^{2}/T\to0$，与"细弦趋于理想柔弦"一致 ✓。

**读法**：低音的难点不是"频率低"，而是"低频率还得靠高张力撑着"，否则非谐性毁掉音准——这就是低音弦为什么必须缠铜。

**1.16** **思路**：往返时间用 $2L/c$；反射极性回到 1.7 节的"力与位移"对应关系：声学里"力"是声压。

**过程**：往返 $2L$：

$$
\Delta t=\frac{2L}{c}=\frac{2\times0.60}{343}=3.5\times10^{-3}\ \mathrm{s}.
$$

声压的边界条件：开口端与大气相通，$p=0$；闭口端刚性，质点速度为零、声压取极大。于是

$$
R_{p}\big|_{\text{开口}}=\frac{0-p_{i}}{p_{i}}=-1,
\qquad
R_{p}\big|_{\text{闭口}}=+1 .
$$

**结果**：往返 $3.5\ \mathrm{ms}$；声压反射系数：开口端 $-1$（倒相），闭口端 $+1$（同相）。位移（速度）的系数恰好相反。

**检验**：$-1$ 与 $+1$ 对应"两端完全反射、不漏能"，与 1.6.3 的 $|R|=1$ 一致 ✓；把 $L$ 减半，往返时间减半，与 $c$ 无关的结论一致 ✓。

**读法**：开口端是声压节点、位移腹点，正对应弦的自由端（那里力为零、位移最大）；闭口端则对应弦的固定端——**同一个边界，看"位移"和看"压力"的结论是反的**。

**1.17** **思路**：两种波走同一段距离、速度不同，时间差就是 $d$ 乘以速度倒数之差；一个方程一个未知量。

**过程**：设震中距 $d$，则 $t_{P}=d/6.0$、$t_{S}=d/3.5$（单位 km、s），

$$
\frac{d}{3.5}-\frac{d}{6.0}=12
\quad\Longrightarrow\quad
d\left(0.2857-0.1667\right)=12 .
$$

**结果**：$d=\dfrac{12}{0.1190}=1.0\times10^{2}\ \mathrm{km}$。

**检验**：代回：$100.8/3.5=28.8\ \mathrm{s}$，$100.8/6.0=16.8\ \mathrm{s}$，差 $12.0\ \mathrm{s}$ ✓。量纲 $\mathrm{km}/(\mathrm{km/s})=\mathrm{s}$ ✓。

**读法**：时间差随距离线性增长，所以"P 到、S 到"的间隔本身就是一把尺子；三个台站的这种尺子一交叉，震中就定死了。

**1.18** **思路**：同一段距离，两个速度，两段时间；做差即可。

**过程**：

$$
t_{\text{钢}}=\frac{2.0\times10^{3}}{5.0\times10^{3}}=0.40\ \mathrm{s},
\qquad
t_{\text{空气}}=\frac{2.0\times10^{3}}{343}=5.83\ \mathrm{s}.
$$

**结果**：$\Delta t=5.83-0.40=5.4\ \mathrm{s}$。

**检验**：两个时间各自都合理：空气中 2 km 约 6 s（常识「千米三秒」），钢里 0.4 s ✓。再验线性：距离加倍，两个时间与差值都加倍 ✓。量纲 m/(m/s)=s ✓。

**读法**：固体里的纵波比空气快一个数量级，所以"先听到的那一声来自铁轨"；这也是地震 P 波先于声波到达的原因。

**1.19** **思路**：把弹簧端点写成边界条件，代入"入射 + 反射"的简谐解，解出 $R$；模为 1 是因为分子分母互为共轭。

**过程**：设 $u=f(t-x/c)+Rf(t+x/c)$，取 $f=e^{-i\omega t}$，在 $x=0$ 处

$$
u=(1+R)e^{-i\omega t},\qquad
\frac{\partial u}{\partial x}=\frac{i\omega}{c}(1-R)e^{-i\omega t}.
$$

边界条件 $T\dfrac{\partial u}{\partial x}\Big|_{x=0}=\kappa u(0,t)$ 给出

$$
iTk(1-R)=\kappa(1+R),\qquad k=\frac{\omega}{c},
$$

解得

$$
R=\frac{iTk-\kappa}{iTk+\kappa}.
$$

分子与分母互为复共轭，所以 $|R|=1$：端点不吸能，只改相位。

**结果**：$R(\omega)=\dfrac{iTk-\kappa}{iTk+\kappa}$，$|R|=1$；分界频率由 $Tk=\kappa$ 定，即 $\omega_{c}=\dfrac{\kappa c}{T}=\dfrac{10^{3}\times418}{70}=6.0\times10^{3}\ \mathrm{rad/s}$，$f_{c}=\dfrac{\omega_{c}}{2\pi}=9.5\times10^{2}\ \mathrm{Hz}$。

**检验**：两个极限：$\kappa\to\infty$ 时 $R\to-1$（固定端）✓；$\kappa\to0$ 时 $R\to+1$（自由端）✓。量纲 $\kappa c/T=\dfrac{\mathrm{N/m}\cdot\mathrm{m/s}}{\mathrm{N}}=\mathrm{s^{-1}}$ ✓。

**读法**：低频时弹簧"很硬"、像墙；高频时它来不及响应、像空着。所以同一根弦，低音被倒相、高音不倒相——一个尖脉冲含各种频率，反射回来各成分相位不同，叠加就被抹成拖尾。

**1.20** **思路**：$Q$ 与衰减时间的关系是 $\tau=Q/\omega_{1}$；高次泛音先消失，只需要说明 $\gamma$ 随 $\omega$ 增大。

**过程**：

$$
\tau=\frac{Q}{\omega_{1}}=\frac{1000}{2\pi\times322}=0.494\ \mathrm{s}.
$$

振幅按 $e^{-t/\tau}$ 衰减，听觉上约 $3$ 到 $4$ 个 $\tau$ 后听不见，即 $1.5$ 到 $2.0\ \mathrm{s}$。若 $\gamma\propto\omega$，则第 $n$ 阶的衰减时间为

$$
\tau_{n}=\frac{2}{\gamma_{n}}\propto\frac{1}{\omega_{n}}=\frac{\tau_{1}}{n},
$$

第 $10$ 阶只有 $\tau_{1}/10\approx49\ \mathrm{ms}$。

**结果**：$\tau=0.49\ \mathrm{s}$，可听时长约 $1.5$–$2.0\ \mathrm{s}$；第 $n$ 阶的衰减时间是基频的 $1/n$。

**检验**：量纲 $Q$ 无量纲、$\omega$ 是 $\mathrm{s^{-1}}$，$\tau$ 是 $\mathrm{s}$ ✓。极限核对：$Q\to\infty$ 时 $\tau\to\infty$（无阻尼），与"理想弦能量守恒"一致 ✓。

**读法**：余音不是"一起变小"，而是高频先死——所以听感是从"亮"变"暗"。这就是为什么评价一把琴要说"余音长不长、尾巴暖不暖"。

**1.21** **思路**：浅水波速 $c=\sqrt{gh}$ 是已知的，代进去算时间；靠岸变高的原因不是"水堆起来"，而是能流守恒加波速变小。

**过程**：

$$
c=\sqrt{gh}=\sqrt{9.8\times4.0\times10^{3}}=1.98\times10^{2}\ \mathrm{m/s},
\qquad
t=\frac{8.0\times10^{6}}{1.98\times10^{2}}=4.0\times10^{4}\ \mathrm{s}.
$$

**结果**：$c=2.0\times10^{2}\ \mathrm{m/s}$，横渡 $8000\ \mathrm{km}$ 约 $11\ \mathrm{h}$。

**检验**：量纲 $\sqrt{\mathrm{m/s^{2}}\cdot\mathrm{m}}=\mathrm{m/s}$ ✓。与飞机（$900\ \mathrm{km/h}$）比：$8000\ \mathrm{km}$ 只要 $9\ \mathrm{h}$，所以海啸比客机慢一点——这与实际预警时间（数小时）吻合 ✓。

**读法**：近岸水浅，$c$ 变小，而单位时间通过的能流近似不变，波长被压缩、振幅必须增大；浅水放大律给 $A\propto h^{-1/4}$，几千米深的浪到岸边可以涨到几米。

**1.22** **思路**：与弹簧端点完全对偶——把边界条件换成"质量块受力"，其余步骤照搬。

**过程**：仍设 $u=e^{i(kx-\omega t)}+R e^{-i(kx-\omega t)}$，在 $x=0$ 处

$$
u=(1+R)e^{-i\omega t},\quad
\frac{\partial u}{\partial x}=ik(1-R)e^{-i\omega t},\quad
\frac{\partial^{2}u}{\partial t^{2}}=-\omega^{2}(1+R)e^{-i\omega t}.
$$

边界条件 $T\dfrac{\partial u}{\partial x}\Big|_{x=0}=M\dfrac{\partial^{2}u}{\partial t^{2}}$ 给出

$$
iTk(1-R)=-M\omega^{2}(1+R)
\quad\Longrightarrow\quad
R=\frac{iTk+M\omega^{2}}{iTk-M\omega^{2}}.
$$

分子分母共轭，$|R|=1$。分界由 $M\omega^{2}=Tk=T\omega/c$ 定：

$$
\omega_{c}=\frac{T}{Mc}=\frac{70}{2.0\times10^{-3}\times418}=8.4\times10^{1}\ \mathrm{rad/s},
\qquad
f_{c}=\frac{\omega_{c}}{2\pi}=13\ \mathrm{Hz}.
$$

**结果**：$R(\omega)=\dfrac{iTk+M\omega^{2}}{iTk-M\omega^{2}}$，$|R|=1$；$f_{c}=13\ \mathrm{Hz}$，低频像自由端（$R\to+1$），高频像固定端（$R\to-1$）。

**检验**：两个极限代回：$\omega\to0$ 时 $R\to+1$ ✓，$\omega\to\infty$ 时 $R\to-1$ ✓。与 1.19 的弹簧端点对照：那里的分界是 $f_{c}=950\ \mathrm{Hz}$，两个边界在频率轴上的行为正好相反 ✓。

**读法**：质量块"懒得动"的方式与弹簧相反——频率越高越跟不上，于是高频被它挡住、像撞墙；低频时它跟着走，端点几乎不约束。真实的琴桥既有质量又有弹性，所以它的反射系数在两个频率之间来回过渡。

**1.23** **思路**：拾音器输出正比于该点的弦速，弦速里第 $n$ 阶的因子是 $\sin(n\pi x_{p}/L)$；让它为零就得到"听不到"的阶数。

**过程**：第 $n$ 阶模式的速度

$$
\frac{\partial u_{n}}{\partial t}\propto\sin\frac{n\pi x_{p}}{L}\sin(\omega_{n}t),
$$

在 $x_{p}=L/5$ 处要求 $\sin\dfrac{n\pi}{5}=0$，即 $\dfrac{n\pi}{5}=k\pi$，$n=5k$。

**结果**：$n=5,10,15,\dots$ 完全没有输出；其余阶按 $\sin(n\pi/5)$ 加权。

**检验**：$n=5$ 时 $\sin\pi=0$ ✓；$n=1$ 时 $\sin(\pi/5)=0.588$，不是零 ✓。若拾音器挪到 $L/2$，被削掉的变成所有偶数阶，与 1.24 一致 ✓。

**读法**：三个拾音器装在离琴桥不同距离处，各自削掉一组不同的泛音，所以同一根弦在三个位置上音色不同——这不是电路差异，是几何造成的频谱缺口。

**1.24** **思路**：与拾音器同一个道理，只是把"输出"换成"槌子给的能量"：激励点在第 $n$ 阶的节点上，那一阶就拿不到能量。

**过程**：槌击近似为在 $x_{p}$ 附近给一个初速脉冲，展开系数 $\propto\sin\dfrac{n\pi x_{p}}{L}$。$x_{p}=L/7$ 时

$$
\sin\frac{n\pi}{7}=0\quad\Longrightarrow\quad n=7,14,21,\dots
$$

**结果**：$n=7,14$ 被削弱到零附近；若挪到 $L/2$，所有偶数阶（$n=2,4,6,\dots$）全被削掉，只剩奇次。

**检验**：$n=1$ 时 $\sin(\pi/7)=0.434$，$n=2$ 时 $\sin(2\pi/7)=0.782$——前几阶仍有输出 ✓。

**读法**：击弦点选在 $1/7$ 到 $1/9$ 附近，是为了避开低阶节点、又保留足够多的高次泛音；挪到正中会让声音像单簧管那样"空心"，所以钢琴不这么做。

**1.25** **思路**：能量守恒只要把守恒律沿弦积分、再用边界条件杀掉边界项；跳变使能量无穷，只要看 $\int(u_{x})^{2}$ 在跳变附近怎么爆。

**过程**：(1) 由 $\frac{\partial e}{\partial t}+\frac{\partial j}{\partial x}=0$（1.6.2），对 $x$ 从 $0$ 积到 $L$：

$$
\frac{\mathrm{d}E}{\mathrm{d}t}=\int_{0}^{L}\frac{\partial e}{\partial t}\mathrm{d}x
=-\int_{0}^{L}\frac{\partial j}{\partial x}\mathrm{d}x=-j(L)+j(0).
$$

固定端：$u(0,t)=u(L,t)=0\Rightarrow\frac{\partial u}{\partial t}=0\Rightarrow j=-T\frac{\partial u}{\partial x}\frac{\partial u}{\partial t}=0$；自由端：$\frac{\partial u}{\partial x}=0\Rightarrow j=0$。两种情形都有 $\frac{\mathrm{d}E}{\mathrm{d}t}=0$。

(2) 设初始形状在 $x_{0}$ 处有高 $\Delta h$ 的跳变。把跳变摊在宽 $\epsilon$ 的过渡层上，那里 $\left|\frac{\partial u}{\partial x}\right|\approx\dfrac{\Delta h}{\epsilon}$，于是

$$
E_{p}=\frac{T}{2}\int\left(\frac{\partial u}{\partial x}\right)^{2}\mathrm{d}x
\;\gtrsim\;\frac{T}{2}\cdot\frac{(\Delta h)^{2}}{\epsilon^{2}}\cdot\epsilon
=\frac{T(\Delta h)^{2}}{2\epsilon}\xrightarrow[\epsilon\to0]{}\infty .
$$

**结果**：两端固定或两端自由时 $\dfrac{\mathrm{d}E}{\mathrm{d}t}=0$（能量守恒）；带跳变的初始形状 $E_{p}=\infty$。

**检验**：量纲 $\mathrm{N}\cdot\mathrm{m^{2}}/\mathrm{m}=\mathrm{J}$ ✓。极限 $\epsilon\to a$（过渡层等于整个区间）时 $E_{p}\sim T(\Delta h)^{2}/(2a)$，回到"斜坡"的有限值 ✓。

**读法**：理想边界一个能量都不漏，所以余音衰减只能来自模型外的耗散；而"跳变"要有限时间内造成有限位移差，需要无穷大的力——**能量有限性本身就是对初始条件的一道筛子**。

**1.26** **思路**：把 $f'$ 也展开（逐项求导），对 $f'$ 用一次帕塞瓦尔恒等式，就能把 $\sum n^{2}a_{n}^{2}$ 换成 $\int(f')^{2}$。

**过程**：$f(0)=f(L)=0$ 时，$f=\sum_{n}a_{n}\sin\frac{n\pi x}{L}$，逐项求导得

$$
f'(x)=\sum_{n}a_{n}\frac{n\pi}{L}\cos\frac{n\pi x}{L}.
$$

对 $\cos$ 族用正交性 $\int_{0}^{L}\cos\frac{n\pi x}{L}\cos\frac{m\pi x}{L}\mathrm{d}x=\frac{L}{2}\delta_{nm}$，于是

$$
\int_{0}^{L}\left(f'\right)^{2}\mathrm{d}x
=\sum_{n}a_{n}^{2}\frac{n^{2}\pi^{2}}{L^{2}}\cdot\frac{L}{2}
=\frac{\pi^{2}}{2L}\sum_{n}n^{2}a_{n}^{2}.
$$

整理即得 $\sum_{n}n^{2}a_{n}^{2}=\dfrac{2L}{\pi^{2}}\int_{0}^{L}(f')^{2}\mathrm{d}x$。代进 $E_{n}=\dfrac{n^{2}\pi^{2}T}{4L}a_{n}^{2}$：

$$
\sum_{n}E_{n}=\frac{\pi^{2}T}{4L}\cdot\frac{2L}{\pi^{2}}\int_{0}^{L}(f')^{2}\mathrm{d}x
=\frac{T}{2}\int_{0}^{L}(f')^{2}\mathrm{d}x .
$$

**结果**：$\sum_{n}n^{2}a_{n}^{2}=\dfrac{2L}{\pi^{2}}\int_{0}^{L}(f')^{2}\mathrm{d}x$，从而模式能量之和等于初始弹性势能。

**检验**：用 1.7 节的三角形（$x_{0}=L/3$、高 $h=3.0\ \mathrm{mm}$、$L=0.65\ \mathrm{m}$、$T=70\ \mathrm{N}$）核对：两段斜率是 $h/x_{0}=3h/L$ 与 $h/(L-x_{0})=1.5h/L$，

$$
\int_{0}^{L}(f')^{2}\mathrm{d}x=\left(\frac{3h}{L}\right)^{2}\frac{L}{3}+\left(\frac{1.5h}{L}\right)^{2}\frac{2L}{3}=\frac{4.5h^{2}}{L},
$$

乘以 $\frac{T}{2}$ 得 $\dfrac{2.25Th^{2}}{L}=\dfrac{9Th^{2}}{4L}=2.18\times10^{-3}\ \mathrm{J}$，与 1.7 节算的总能量逐字相同 ✓。

**读法**：这不是新物理，而是一个恒等式：**"能量按模式相加"与"能量等于形状的平方梯度积分"是同一件事的两面**。它把"级数收敛"翻译成了"形状足够光滑"。

**1.27** **思路**：把 $u=A\cos(kx-\omega t)$ 代进带四阶项的方程，得到 $\omega$ 与 $k$ 的关系；两个速度（相速度、群速度）分别按定义求导。

**过程**：代入后每一项都带同一个 $\cos$，约掉得

$$
\omega^{2}=c^{2}k^{2}+\frac{EI}{\rho}k^{4},
\qquad
\omega=ck\sqrt{1+\frac{EI}{T}k^{2}}
$$

（用了 $c^{2}=T/\rho$，把 $\frac{EI}{\rho}$ 写成 $\frac{EI}{T}c^{2}$）。相速度与群速度：

$$
v_{p}=\frac{\omega}{k}=c\sqrt{1+\frac{EI}{T}k^{2}},
\qquad
v_{g}=\frac{\mathrm{d}\omega}{\mathrm{d}k}=\frac{c^{2}k+2\frac{EI}{\rho}k^{3}}{\omega}.
$$

比较时令 $x=\dfrac{EI}{T}k^{2}>0$，则 $\omega^{2}=c^{2}k^{2}(1+x)$，

$$
\frac{v_{g}}{v_{p}}
=\frac{c^{2}k^{2}+2\frac{EI}{\rho}k^{4}}{\omega^{2}}
=\frac{1+2x}{1+x}>1 .
$$

**结果**：$\omega(k)=ck\sqrt{1+\frac{EI}{T}k^{2}}$，$v_{p}=\dfrac{\omega}{k}$，$v_{g}=\dfrac{\mathrm{d}\omega}{\mathrm{d}k}$，且 $v_{g}>v_{p}$（正常色散里 $v_{g}<v_{p}$，刚弦是反常色散）。

**检验**：$k\to0$ 时 $x\to0$，$v_{g}/v_{p}\to1$、$v_{p}\to c$，退化为理想柔弦 ✓；量纲 $\frac{EI}{T}k^{2}=\frac{\mathrm{N\cdot m^{2}}}{\mathrm{N}}\cdot\mathrm{m^{-2}}$ 无量纲 ✓。

**读法**：高频（短波）跑得快，所以一个脉冲最先到的是它的高频成分——听感上就是"起音特别亮"；反过来，波的形状会随传播改变，$F(x-ct)$ 那种"形状不变"的特权没了。

**1.28** **思路**：与 1.19 同一套边界，但这里把每一步写全：先设解、再代入、再解代数、最后取模。

**过程**：设入射 $e^{i(kx-\omega t)}$、反射 $R e^{i(-kx-\omega t)}$，则

$$
u=\left(e^{ikx}+Re^{-ikx}\right)e^{-i\omega t}.
$$

在 $x=0$：$u=(1+R)e^{-i\omega t}$，$\dfrac{\partial u}{\partial x}=ik(1-R)e^{-i\omega t}$。代入 $T\dfrac{\partial u}{\partial x}=\kappa u$：

$$
iTk(1-R)=\kappa(1+R)
\quad\Longrightarrow\quad
iTk-\kappa=(iTk+\kappa)R
\quad\Longrightarrow\quad
R=\frac{iTk-\kappa}{iTk+\kappa}.
$$

取模：$|iTk-\kappa|=\sqrt{(Tk)^{2}+\kappa^{2}}=|iTk+\kappa|$，所以 $|R|=1$。分界在实部为零、即 $Tk=\kappa$：

$$
f_{c}=\frac{\omega_{c}}{2\pi}=\frac{\kappa c}{2\pi T}
=\frac{10^{3}\times418}{2\pi\times70}=9.5\times10^{2}\ \mathrm{Hz}.
$$

**结果**：$R(\omega)=\dfrac{iTk-\kappa}{iTk+\kappa}$，$|R|=1$，$f_{c}\approx950\ \mathrm{Hz}$。

**检验**：$\kappa\to\infty$ 给 $R\to-1$、$\kappa\to0$ 给 $R\to+1$，两端分别是固定端与自由端 ✓。相位也对：写成实虚部，

$$
R=\frac{(Tk)^{2}-\kappa^{2}+2iTk\kappa}{(Tk)^{2}+\kappa^{2}}
\quad\Longrightarrow\quad
\arg R=\pi-2\arctan\frac{Tk}{\kappa},
$$

低频 $\to\pi$（倒相）、高频 $\to0$（不倒相），单调过渡，中点 $Tk=\kappa$ 处正好 $\pi/2$ ✓。

**读法**：复反射系数的模为 1 说明"只改相位、不改振幅"，所以它不会让脉冲变弱，只会让它变形；判断这一类端点，不能只看极性，要看反射波形与入射是否同形。

**1.29** **思路**：阻尼振子的振幅按 $e^{-\gamma t/2}$ 衰减，所以 $\tau=2/\gamma$；把 $\gamma_{n}=\beta\omega_{n}^{2}$ 代进去就得到频率依赖。

**过程**：

$$
\tau_{n}=\frac{2}{\gamma_{n}}=\frac{2}{\beta\omega_{n}^{2}}
\quad\Longrightarrow\quad
\tau_{n}\propto\frac{1}{n^{2}}.
$$

于是

$$
\frac{\tau_{10}}{\tau_{1}}=\left(\frac{\omega_{1}}{\omega_{10}}\right)^{2}=\frac{1}{100}.
$$

**结果**：$\tau_{n}=\dfrac{2}{\beta\omega_{n}^{2}}$，$\dfrac{\tau_{10}}{\tau_{1}}=\dfrac{1}{100}$；取 $\tau_{1}=2.0\ \mathrm{s}$ 得 $\tau_{10}=2.0\times10^{-2}\ \mathrm{s}$。

**检验**：量纲 $\beta$ 的单位由 $\gamma=\beta\omega^{2}$ 定为 $\mathrm{s}$，$\tau=2/\gamma$ 是 $\mathrm{s}$ ✓。极限：$\beta\to0$ 时 $\tau\to\infty$（无阻尼）✓。

**读法**：$\tau\propto n^{-2}$ 意味着第 10 阶在 20 ms 内就没了，而基频还在响 2 秒——所以余音的频谱随时间从宽变窄，听感"由亮变暗"。真实弦的指数比 2 温和，但方向一致。

**1.30** **思路**：非齐次边界先按"定常驱动"设形状 $u=X(x)\sin\Omega t$，把偏微分方程降成常微分方程；共振条件就是分母为零。

**过程**：(a) 代入方程，$\sin\Omega t$ 约掉：

$$
X''+\frac{\Omega^{2}}{c^{2}}X=0,\qquad X(0)=A,\quad X(L)=0 .
$$

通解 $X=C_{1}\cos kx+C_{2}\sin kx$（$k=\Omega/c$），由 $X(L)=0$ 与 $X(0)=A$ 解得

$$
X(x)=A\,\frac{\sin\left[k(L-x)\right]}{\sin(kL)} .
$$

(b) 分母 $\sin(kL)=0$ 时振幅发散，即 $kL=n\pi$，$\Omega=n\pi c/L$。

(c) 一趟往返的相位是 $2kL$（去 $kL$、回来 $kL$），条件 $kL=n\pi$ 正是 $2kL=2n\pi$——往返一次回到原相位。

**结果**：$u(x,t)=A\dfrac{\sin[k(L-x)]}{\sin(kL)}\sin(\Omega t)$，共振频率 $\Omega_{n}=n\pi c/L$。

**检验**：$x=L$ 处 $\sin0=0$ ✓，$x=0$ 处 $\sin(kL)/\sin(kL)=1$ ✓。$\Omega\to0$ 时 $X\to A(L-x)/L$，是一条直线——正是"缓慢推到极限"的静力学结果 ✓。

**读法**：共振不是"数学上分母为零"的病态，而是"往返一次相位闭合"的几何条件；这套说法在第 8 章讲回路与反馈时会原样出现。

**1.31** **思路**：刚度的签名是"偏离随 $n^{2}$ 线性增长"，所以先算 $f_{n}/(nf_{1})-1$，再对 $n^{2}$ 看是否成正比；斜率给 $B/2$。

**过程**：先算比值（$f_{1}=261.0\ \mathrm{Hz}$）：

| $n$ | $f_{n}/(nf_{1})$ | $f_{n}/(nf_{1})-1$ | $n^{2}$ |
|---|---|---|---|
| 2 | $1.0013$ | $0.0013$ | 4 |
| 4 | $1.0056$ | $0.0056$ | 16 |
| 8 | $1.0218$ | $0.0218$ | 64 |

三组数几乎严格正比于 $n^{2}$（$0.0013:0.0056:0.0218\approx4:16:64$），所以是刚度非谐性。由 $\dfrac{f_{n}}{nf_{1}}=\sqrt{1+Bn^{2}}$ 反解：

$$
B=\frac{(1+0.0218)^{2}-1}{64}=6.9\times10^{-4}.
$$

**结果**：$B\approx6.9\times10^{-4}$；判据是"偏离 $\propto n^{2}$"。

**检验**：用 $B=6.9\times10^{-4}$ 回头算 $n=8$：$\sqrt{1+6.9\times10^{-4}\times64}=1.0218$，与表里一致 ✓；代入弦参数（$d=1\ \mathrm{mm}$、$L=0.65\ \mathrm{m}$、$T=700\ \mathrm{N}$）算出的 $B\approx3\times10^{-4}$，同量级 ✓。

**读法**：如果偏离不是 $\propto n^{2}$（比如各阶一起平移），那是张力或温度在变；只有"高阶偏得多、且对张力不敏感"才是刚度。这就是判断"琴弦是不是老了"的实验方法。

**1.32** **错。** 通解形式要求 $F$、$G$ 二阶可导，而"任意初始条件"里包含有跳变的形状，那种初值没有经典解。正确的说法是：初值足够光滑（$f$ 二阶可导、$g$ 一阶可导）时解存在且唯一；有折点（导数跳变）时仍有物理解——理想弦允许折点。

**反例**：取 $f(x)=h\,\mathrm{sgn}(x)$（在原点跳到 $h$），代进达朗贝尔公式后 $\frac{\partial^{2}u}{\partial x^{2}}$ 在两条特征线上是 $\delta$ 函数，方程在经典意义下不成立；而且它的弹性势能 $\frac{T}{2}\int(f')^{2}\mathrm{d}x$ 发散（1.25 题），物理上不可能实现。

**1.33** **错。** $f=\frac{1}{2L}\sqrt{T/\rho}$，张力加倍只让频率升高 $\sqrt{2}$ 倍，即约 6 个半音，离八度（$2$ 倍）还差得远。要升高八度需要 $T$ 变成 4 倍。

**反例与数值**：一把吉他弦 $T=70\ \mathrm{N}$、$f=322\ \mathrm{Hz}$。把 $T$ 加到 $140\ \mathrm{N}$，频率变成 $322\times\sqrt{2}=455\ \mathrm{Hz}$，只升高 $1200\log_{2}\sqrt{2}=600$ 音分，正好 $6$ 个半音，离八度（$1200$ 音分）差一半；要 $644\ \mathrm{Hz}$ 得把张力加到 $4\times70=280\ \mathrm{N}$，通常已超过弦的强度。所以"调高八度"要靠缩短有效长度（按品），不是靠拧弦轴。

**1.34** **错。** 公式在形式上还能写，但那种"解"在跳变处二阶导数不存在，而且总能量发散（1.25 题）。物理上要在零宽度内造成有限位移差，需要无穷大的力。

**反例**：把一根弦在 $x_{0}$ 处"瞬间"抬高一截、旁边不动，等于要它在该点有一个垂直台阶；真实弦有弯曲刚度，台阶会被抹成半径 $\sim EI/T$ 的圆弧（1.2.1 的四阶项），宽度不可能为零。所以"跳变初值"是理想化的极限，不能当作物理上可实现的初始条件。

**1.35** **错。** 理想弦的两类边界确实不漏能（1.6.3），但真实弦还有空气粘性、材料内摩擦、以及把能量传给琴桥和面板的通道。余音衰减正是这些模型外机制的结果。

**反例**：如果只按理想模型算，$Q=\infty$，振幅永不衰减；而实测一把吉他的 $Q\approx10^{3}$（1.20 题），余音 $1$–$2$ 秒就没了。差了三个数量级，说明耗散不在边界上，而在介质里——要在方程里显式加 $\gamma\frac{\partial u}{\partial t}$ 项才描述得了。

**1.36** **错。** $x_{0}=L/3$ 是第 3 个模式的节点，所以在那里拨弦不能**激发**它；但只要它被别的办法激发了，弦上除节点以外处处有位移，声音照样辐射出去。

**反例**：先用手指在 $L/3$ 处轻触（压住节点）再拨弦，第 3 阶确实不响；但若改在 $L/2$ 处拨，第 3 阶的振幅是 $\frac{9h}{9\pi^{2}}\sin\pi=0$——同一次拨弦里它为零，可一旦弦上已经存在第 3 阶（比如从别处传来），你在 $L/3$ 处能听到它旁边的位移，只是听不到节点那一点。**"节点"约束的是激励，不是存在。**

**1.37** **错。** 端点附近的位移瞬时加倍，但能量没有加倍：入射波带来一份能量，一半继续以反射波的形式离开，端点处只是两列波瞬时叠加。

**反例**：取入射脉冲 $A=1$、自由端反射 $R=+1$，端点峰值到 $2A$。若能量真的加倍，端点附近的总能量会是 $4$ 倍（能量 $\propto A^{2}$）；但 1.6.3 已经证明端点处 $j=0$、总能量守恒，所以那只是"位移叠加"，不是"能量叠加"。$2A$ 的峰值只在端点这一个点上、且只持续一瞬。

**1.38** **对。** 对无色散、均匀弦上的行波，$\frac{\partial u}{\partial t}=-c\frac{\partial u}{\partial x}$，代入 1.6.1 的两个密度得 $e_{k}=\frac12\rho c^{2}(u_{x})^{2}$、$e_{p}=\frac12T(u_{x})^{2}$，而 $T=\rho c^{2}$，所以 $e_{k}=e_{p}$ 处处成立，$e=e_{k}+e_{p}=2e_{k}$。

**推导**：$\frac{\partial u}{\partial t}=-cF'$、$\frac{\partial u}{\partial x}=F'$，于是 $e_{k}=\frac12\rho c^{2}F'^{2}$、$e_{p}=\frac12TF'^{2}$；因为 $T=\rho c^{2}$，两者的系数逐字相同，故 $e_{k}=e_{p}$，$e=2e_{k}$。

**反例（什么时候不成立）**：一根两端固定的弦上的纯驻波，$t=0$ 时刻 $u=A\sin kx$、$\frac{\partial u}{\partial t}=0$，此时 $e_{k}=0$、能量全在势能里；$\omega t=\pi/2$ 时反过来，$e_{p}=0$。所以"总能量是动能的两倍"只是**行波**的结论，套到驻波上会得出"能量为零"的荒谬答案——1.6.4 的图里那条重合的曲线只属于行波。

**检验**：量纲 $\rho c^{2}F'^{2}=(\mathrm{kg/m})(\mathrm{m/s})^{2}=\mathrm{J/m}$ ✓，与 $e$ 的单位一致。

**1.39** **错。** 这里的 $c$ 是弦（或介质）的横波速度，由 $T$、$\rho$ 决定，它不是信号速度的上限。在相对论情形下，波动方程本身要换成满足洛伦兹协变的方程，"$c$ 取得很大"这件事在物理上不允许。

**反例**：把弦换成一根刚性很好的杆，$c=\sqrt{E/\rho}$ 可以到 $5\times10^{3}\ \mathrm{m/s}$，仍然远小于光速；而如果有人真造出一根 $c>3\times10^{8}\ \mathrm{m/s}$ 的弦，那不是"信息超光速"，而是说明这个连续介质模型（把原子当成连续分布）在那种能量尺度下已经失效——弦模型本身是低速近似。

## 第 2 章

> 每题按「思路、过程、结果、检验、读法」五段写。先自己想，卡住了再看对应那一段。
> 引用正文节号（如「见 2.5」）只是指路，过程仍写全。

## A 组　基本运算

**2.1**

**思路**：初值 $f(x)=x$，要求正弦级数的系数，直接用 2.5 的投影公式 $a_n=\frac2L\int_0^Lf\sin\frac{n\pi x}{L}dx$。想到这条路是因为 $f$ 光滑、没有奇异点，一次分部积分就能积出来。

**过程**：取 $u=x$、$dv=\sin\frac{n\pi x}{L}dx$，则 $du=dx$、$v=-\frac{L}{n\pi}\cos\frac{n\pi x}{L}$：

$$a_n=\frac2L\left\{\left[-\frac{Lx}{n\pi}\cos\frac{n\pi x}{L}\right]_0^L+\frac{L}{n\pi}\int_0^L\cos\frac{n\pi x}{L}dx\right\}.$$

边界项代入上下限（$\cos n\pi=(-1)^n$，$\cos0=1$）：

$$\left[-\frac{Lx}{n\pi}\cos\frac{n\pi x}{L}\right]_0^L=-\frac{L^2}{n\pi}(-1)^n=\frac{L^2}{n\pi}(-1)^{n+1}.$$

第二项：$\int_0^L\cos\frac{n\pi x}{L}dx=\frac{L}{n\pi}\sin n\pi=0$。乘回 $2/L$：

**结果**：

$$a_n=\frac{2L(-1)^{n+1}}{n\pi},\qquad n=1,2,3,\dots$$

**检验**：(i) 量纲：$a_n$ 与 $x$ 同量纲，$L\cdot1/n$ 是长度 ✓。(ii) 用 2.6.1 的判据：$f(0)=0$、$f(L)=L\ne0$，边界项 $\frac{2}{n\pi}[f(0)-(-1)^nf(L)]=-\frac{2L(-1)^n}{n\pi}$ 不为零，所以只能按 $1/n$ 衰减，与结果一致 ✓。(iii) 在 $x=L/2$ 处级数应给出 $L/2$：用 $\sum_n\frac{(-1)^{n+1}}{n}\sin\frac{n\pi}{2}=\frac{\pi}{4}$，得 $\frac{2L}{\pi}\cdot\frac{\pi}{4}=\frac L2$ ✓。

**读法**：$f=x$ 的奇延拓在 $x=L$ 处从 $L$ 跳到 $-L$，是锯齿波；跳变迫使系数按 $1/n$ 慢慢衰减。后果很实际：想用这个级数算 $x=L$ 附近的斜率，项数要多到不现实——这正是 2.6 说的「有跳变就只能均方收敛」。

**2.2**

**思路**：先用三倍角公式把初值降次。如果降完恰好是 $\sin\frac{\pi x}{L}$ 与 $\sin\frac{3\pi x}{L}$ 的组合，就**不用做积分**：正弦族线性无关，系数直接读出来。这比硬算 $\int\sin^3\sin(n\pi x/L)dx$ 快，也不容易错。

**过程**：由 $\sin3\theta=3\sin\theta-4\sin^3\theta$ 反解得

$$\sin^3\theta=\frac{3\sin\theta-\sin3\theta}{4}.$$

取 $\theta=\frac{\pi x}{L}$：

$$f(x)=\sin^3\frac{\pi x}{L}=\frac34\sin\frac{\pi x}{L}-\frac14\sin\frac{3\pi x}{L}.$$

这就是初值的正弦级数本身，与 $f=\sum a_n\sin\frac{n\pi x}{L}$ 逐项对照。

**结果**：

$$a_1=\frac34,\qquad a_3=-\frac14,\qquad a_n=0\ (n\ne1,3).$$

**检验**：(i) $x=L/2$ 处左边 $f=1$，右边 $\frac34\sin\frac{\pi}{2}-\frac14\sin\frac{3\pi}{2}=\frac34+\frac14=1$ ✓。(ii) $x=L/6$ 处左边 $\sin^3\frac{\pi}{6}=\frac18$，右边 $\frac34\cdot\frac12-\frac14\cdot1=\frac18$ ✓。(iii) 系数平方和应等于 $\frac2L\int_0^Lf^2dx$：左边 $\frac{9}{16}+\frac{1}{16}=\frac58$；右边用 $\int_0^L\sin^6\frac{\pi x}{L}dx=\frac{5L}{16}$，乘 $\frac2L$ 也得 $\frac58$ ✓。

**读法**：初值里只有两个模，所以弦只以 $\omega_1$ 和 $\omega_3$ 两个频率振动。**非线性函数（$\sin^3$）会把一个频率生出它的奇次倍频**，这是非线性失真的来源；线性系统本身不产生新频率。

**2.3**

**思路**：方程没变（仍是 $X''+k^2X=0$），只换边界。先用 $X(0)=0$ 把解写成单个正弦，再用自由端的 $X'(L)=0$ 定 $k$，最后用 $\int_0^L\sin^2=L/2$ 归一化。新东西只有一处：自由端给的是导数条件。

**过程**：通解 $X=A\sin kx+B\cos kx$。$X(0)=0$ 给出 $B=0$，即 $X=A\sin kx$。自由端不提供横向力（见 1.3.1），所以

$$X'(L)=Ak\cos kL=0\quad\Longrightarrow\quad\cos kL=0.$$

根是 $kL=\frac{\pi}{2},\frac{3\pi}{2},\dots$，统一写成

$$k_n=\frac{(2n-1)\pi}{2L},\qquad X_n(x)=\sin\frac{(2n-1)\pi x}{2L},\qquad n=1,2,3,\dots$$

归一化：令 $\theta=\frac{(2n-1)\pi x}{2L}$，则 $\int_0^L\sin^2\theta\,dx=\frac{L}{(2n-1)\pi}\int_0^{(2n-1)\pi}\sin^2\theta\,d\theta$，而 $\int_0^{m\pi}\sin^2\theta\,d\theta=\frac{m\pi}{2}$，所以积分是 $\frac L2$，归一化常数 $\sqrt{2/L}$。

**结果**：

$$\nu_n=\frac{(2n-1)c}{4L},\qquad \nu_1:\nu_2:\nu_3=1:3:5.$$

**检验**：(i) 基模 $k_1=\frac{\pi}{2L}$，波长 $\lambda_1=4L$：固定端是节点、自由端是波腹，正好四分之一波长 ✓。(ii) 量纲：$c/L$ 是 $\mathrm{s^{-1}}$ ✓。(iii) $L\to0$ 时频率趋于无穷，与「越短越高」一致 ✓。

**读法**：固定–自由只允许奇数倍泛音，缺一半，听起来「空」。单簧管就是这个结构；同一根管子两端都打开，频率比立刻变成 $1:2:3$，音色变亮。**只改一端，泛音结构全变。**

**2.4**

**思路**：两端都自由，两个边界都是斜率条件。用 $X'(0)=0$ 挑出 $\cos$ 支，再用 $X'(L)=0$ 定 $k$。特别当心 $k=0$：它给常数解，是**零频模**，不能丢。

**过程**：$X=A\sin kx+B\cos kx$，$X'=k(A\cos kx-B\sin kx)$。$X'(0)=kA=0$ 给出 $A=0$，$X=B\cos kx$；$X'(L)=-Bk\sin kL=0$ 给出 $\sin kL=0$，即 $kL=n\pi$。

$n=0$ 时 $k=0$、$X=B$，是整体平移，$\omega=0$；$n\ge1$ 时 $X_n=\cos\frac{n\pi x}{L}$。

归一化：$\int_0^L\cos^2\frac{n\pi x}{L}dx=\frac L2$（$n\ge1$）；$n=0$ 时 $\int_0^L1\cdot1\,dx=L$。

**结果**：

$$X_0=1\ (\text{归一化 }1/\sqrt L),\qquad X_n=\cos\frac{n\pi x}{L}\ (\text{归一化 }\sqrt{2/L}),$$
$$\omega_n=\frac{n\pi c}{L},\quad n=0,1,2,\dots;\qquad\text{非零频率比 }1:2:3:\cdots$$

**检验**：(i) 两端斜率都为零：$X_n'(0)=X_n'(L)=0$ ✓。(ii) $n=0$ 时时间方程是 $T''=0$，解 $T=a+bt$，即整根杆匀速平移——自由端不提供回复力，理应允许 ✓。(iii) 量纲：$k_n=n\pi/L$ 是 $\mathrm{m^{-1}}$ ✓。

**读法**：零频模是自由边界特有的：位置不被钉住，你可以把整根杆搬走而不激发任何振动。**所以两端自由的杆做纵振动实验，必须先把杆「挂」住**，否则最低的「振动」是整体平动，测不到驻波。

**2.5**

**思路**：环上没有端点，只有一个条件：绕一圈回原处，函数值与斜率都要接上，即**周期边界条件**。代入 $e^{ikx}$，它变成 $e^{ikL}=1$，直接把 $k$ 限制成离散值。环上两个方向都允许传播，所以每个频率会出现两次——简并。

**过程**：设 $u=X(x)T(t)$，$X(0)=X(L)$、$X'(0)=X'(L)$。取 $X=e^{ikx}$：

$$e^{ikL}=1\quad\Longrightarrow\quad kL=2n\pi\quad\Longrightarrow\quad k_n=\frac{2n\pi}{L},\qquad n=0,\pm1,\pm2,\dots$$

实数写法：$n=0$ 给常数 $1$；每个 $n\ge1$ 给两个独立实解

$$X_n^{(c)}=\cos\frac{2n\pi x}{L},\qquad X_n^{(s)}=\sin\frac{2n\pi x}{L}.$$

原因：$k=\pm\frac{2n\pi}{L}$ 给 $e^{\pm i2n\pi x/L}$，实部与虚部都是解，而这两个 $k$ 对应同一个频率 $\omega_n=\frac{2n\pi c}{L}$。

正交关系：$n\ne m$ 时两种函数的积分都为零；$n=m\ge1$ 时各为 $L/2$；常数模的平方积分是 $L$（即 2.5 的公式把 $\pi/L$ 换成 $2\pi/L$）。

**结果**：

$$k_n=\frac{2n\pi}{L},\qquad\omega_n=\frac{2n\pi c}{L},\qquad n=0,1,2,\dots$$

每个 $n\ge1$ 二重简并（$\cos$ 与 $\sin$ 各一个）。

**检验**：(i) $n=0$ 没有 $\sin$ 模，因为 $\sin0=0$，常数是唯一解 ✓。(ii) 绕一圈相位变化 $2n\pi$，回到原值 ✓。(iii) 相邻间隔 $\frac{2\pi c}{L}$ 是两端固定情形的两倍：环上「一整圈」装两个半波，等效长度短一半 ✓。

**读法**：周期边界的谱是简并的——两个反向传播波同频。环形波导、环状分子、闭合弦都有这种成对的模。简并被打破（比如环被压扁）时两个模分开，就会出现 2.10 讲的那种拍。

**2.6**

**思路**：全部用 2.5 的积化和差，一条公式做四题。唯一的要点是 $\int_0^L\cos\frac{q\pi x}{L}dx=\frac{L}{q\pi}\sin q\pi=0$（$q$ 为非零整数），所以化出整周期余弦的项都自动归零。

**过程**：

(a) $\sin\frac{2\pi x}{L}\sin\frac{5\pi x}{L}=\frac12\left[\cos\frac{3\pi x}{L}-\cos\frac{7\pi x}{L}\right]$，$q=3,7$，都积成零。

(b) $\cos\frac{2\pi x}{L}\cos\frac{4\pi x}{L}=\frac12\left[\cos\frac{2\pi x}{L}+\cos\frac{6\pi x}{L}\right]$，都为零。

(c) $\sin^2\frac{3\pi x}{L}=\frac12\left[1-\cos\frac{6\pi x}{L}\right]$，第二项为零，剩 $\frac12\int_0^L1\,dx$。

(d) $\sin\frac{2\pi x}{L}\cos\frac{2\pi x}{L}=\frac12\sin\frac{4\pi x}{L}$，而 $\int_0^L\sin\frac{4\pi x}{L}dx=\frac{L}{4\pi}[1-\cos4\pi]=0$。

**结果**：(a) $0$；(b) $0$；(c) $L/2$；(d) $0$。

**检验**：(c) 的 $L/2$ 正是 2.3 归一化用的那个数 ✓；(d) 说明同一模的正弦与余弦互相正交，所以 $a_n$、$b_n$ 互不干扰（2.4 的推导靠的就是这一点）。

**读法**：这四个积分的价值不是「会算」，而是「敢扔」：看到不同 $n$ 的正弦相乘，直接写零。**系数公式之所以干净，全靠这些零。**

**2.7**

**思路**：标准初值问题。由 2.1 得 $a_n$，由初速度为零得 $b_n=0$，塞进 2.4 的通解。注意 $\cos\omega_nt$ 的系数就是初值展开系数，**不随时间变**。

**过程**：2.1 已算出 $a_n=\frac{2L(-1)^{n+1}}{n\pi}$。初速度为零，$g(x)=0$，由 $b_n=\frac{2}{\omega_nL}\int_0^Lg\sin\frac{n\pi x}{L}dx$ 得 $b_n=0$。代入

$$u(x,t)=\sum_{n=1}^{\infty}\left[a_n\cos\omega_nt+b_n\sin\omega_nt\right]\sin\frac{n\pi x}{L},\qquad \omega_n=\frac{n\pi c}{L}.$$

**结果**：

$$u(x,t)=\frac{2L}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\cos\frac{n\pi ct}{L}\sin\frac{n\pi x}{L}.$$

**检验**：(i) $t=0$ 时退化为 $x$（2.1 的检验已证）✓。(ii) 每项都满足 $x=0,L$ 处为零 ✓。(iii) $u(x,-t)=u(x,t)$，与「初速度为零」一致（$\cos$ 是偶函数）✓。(iv) 量纲：$L/n$ 是长度 ✓。

**读法**：这是锯齿初值的自由振动。系数只按 $1/n$ 衰减，能量摊到很多高阶模上，所以波形很快变得「毛糙」，两端处的折角在反射中不断换向。**初值光滑，能量集中在低阶；初值有折角，高阶一个也不少**——这条对比在 2.30 会定量化。

**2.8**

**思路**：初位移为零、初速度是常数 $v_0$，所以只有 $b_n$ 项。$b_n$ 比 $a_n$ 多一个因子 $1/\omega_n$，积分本身与 2.6(c) 同型：常数乘正弦，只在奇 $n$ 上不为零。

**过程**：$f=0\Rightarrow a_n=0$。由 2.5，

$$b_n=\frac{2}{\omega_nL}\int_0^Lv_0\sin\frac{n\pi x}{L}dx=\frac{2v_0}{\omega_nL}\cdot\frac{L}{n\pi}\left(1-\cos n\pi\right),$$

其中 $\int_0^L\sin\frac{n\pi x}{L}dx=\frac{L}{n\pi}(1-(-1)^n)$。于是

$$b_n=\frac{2v_0}{n\pi\omega_n}\left(1-(-1)^n\right)=\frac{4v_0}{n\pi\omega_n}\ (n\text{ 奇}),\qquad b_n=0\ (n\text{ 偶}).$$

**结果**：

$$u(x,t)=\frac{4v_0}{\pi}\sum_{n\ \text{奇}}\frac{1}{n\omega_n}\sin\omega_nt\sin\frac{n\pi x}{L},\qquad\omega_n=\frac{n\pi c}{L}.$$

**检验**：(i) 量纲：$v_0/\omega_n=\mathrm{(m/s)\cdot s}=$ 长度 ✓。(ii) 对 $t$ 求导后取 $t=0$：得 $\frac{4v_0}{\pi}\sum_{n\ \text{奇}}\frac1n\sin\frac{n\pi x}{L}$，而常数 $1$ 的正弦系数是 $\frac{4}{n\pi}$，级数正好是 $v_0$ ✓。(iii) 偶模为零：常数在偶模上的投影为零 ✓。

**读法**：给弦一个整体初速度，等于同时拨动所有奇次模，幅度按 $1/n$ 递减。初速关于中点对称，所以反对称的偶模不激发——**对称的初值只激发对称的模**，这与 2.15「拨在节点上不响」是同一类选择定则。

**2.9**

**思路**：帕塞瓦尔等式把「函数的积分」和「系数的平方和」等同起来。取 $f=x$：左边是一个能算的积分，右边是一串待求的级数，等式一列就解出 $\sum1/n^2$。**这是「用物理解数学」的典型**：能量守恒替你做了一次级数求和。

**过程**：由 2.5.1，$\frac2L\int_0^L|f|^2dx=\sum_{n\ge1}a_n^2$。左边

$$\frac2L\int_0^Lx^2dx=\frac2L\cdot\frac{L^3}{3}=\frac{2L^2}{3}.$$

右边用 2.1 的系数 $a_n=\frac{2L(-1)^{n+1}}{n\pi}$：

$$\sum_{n\ge1}a_n^2=\sum_{n\ge1}\frac{4L^2}{n^2\pi^2}=\frac{4L^2}{\pi^2}\sum_{n\ge1}\frac1{n^2}.$$

令两边相等，$L^2$ 约掉：

**结果**：

$$\sum_{n\ge1}\frac1{n^2}=\frac{\pi^2}{6}=1.6449\dots$$

**检验**：数值部分和：前 10 项 $1.5498$，前 100 项 $1.6350$，前 1000 项 $1.6440$——单调上升、越来越慢，符合 $1/n^2$ 的收敛速率（误差约 $1/N$）✓。量纲：两边都无量纲 ✓。

**读法**：这条等式在物理里就是「总能量 = 各模能量之和」。反过来用也成立：知道能谱就能反推波形。第 5 章算格林函数的模态展开时，用的就是同一个等式。

**2.10**

**思路**：边界是非齐次的（右端被平移到 $U_0$），直接分离变量不行，先齐次化（见 2.7.3）：造一个满足边界的稳态 $w$，令 $v=u-w$，$v$ 的边界就是零。代价是初值被 $-w$ 平移。

**过程**：取 $w(x)=U_0\frac xL$（线性插值，$w(0)=0$、$w(L)=U_0$，且 $w''=0$ 不引入源项）。令 $v=u-w$，则

$$v(0,t)=v(L,t)=0,\qquad v(x,0)=0-U_0\frac xL,\qquad \frac{\partial v}{\partial t}\Big|_{t=0}=0.$$

用 $x/L=\frac{2}{\pi}\sum_{n\ge1}\frac{(-1)^{n+1}}{n}\sin\frac{n\pi x}{L}$（这是 2.1 的结果除以 $L$）展开初值，得 $v$ 的系数

$$A_n=-\frac{2U_0}{\pi}\cdot\frac{(-1)^{n+1}}{n},\qquad B_n=0.$$

于是 $v=\sum A_n\cos\omega_nt\sin\frac{n\pi x}{L}$，再取 $u=w+v$。

**结果**：

$$u(x,t)=\frac{U_0x}{L}-\frac{2U_0}{\pi}\sum_{n\ge1}\frac{(-1)^{n+1}}{n}\cos\frac{n\pi ct}{L}\sin\frac{n\pi x}{L}.$$

**检验**：(i) $t=0$ 时两项相消，$u=0$ ✓。(ii) $x=L$ 处 $\sin n\pi=0$，只剩 $U_0$ ✓，边界满足。(iii) 量纲：$U_0$ 是长度，系数无量纲 ✓。(iv) 时间平均：$\langle\cos\rangle=0$，平均形状是线性 $U_0x/L$——这正是把弦慢慢拉过去的形状 ✓。

**读法**：突然把一端拉过去，弦会绕着线性形状来回振荡，永远不停（无阻尼）。**「极限」这件事在无阻尼系统里不存在**，只有时间平均；有阻尼时振荡项按 $e^{-\gamma t/2}$ 消失，才真正趋于直线（见 2.9.1）。这句话值得记住：不要给无阻尼系统求 $t\to\infty$ 的极限。

**2.11**

**思路**：中点拨起的三角形初值，是 2.11 之前那个通式在 $x_0=L/2$ 的特例。先写通式，代 $x_0$ 化简，再用「中点应等于 $h$」做检验——这一步同时验证了 $\sum_{n\ \text{奇}}1/n^2=\pi^2/8$，一举两得。

**过程**：峰在 $x_0$、高 $h$ 的三角形，正弦系数通式为

$$a_n=\frac{2hL^2}{n^2\pi^2x_0(L-x_0)}\sin\frac{n\pi x_0}{L}.$$

代入 $x_0=L/2$，$x_0(L-x_0)=L^2/4$：

$$a_n=\frac{2hL^2}{n^2\pi^2\cdot L^2/4}\sin\frac{n\pi}{2}=\frac{8h}{n^2\pi^2}\sin\frac{n\pi}{2}.$$

**结果**：

$$a_n=\frac{8h}{n^2\pi^2}(-1)^{(n-1)/2}\ (n\ \text{奇}),\qquad a_n=0\ (n\ \text{偶}),$$
$$u(x,t)=\sum_{n\ \text{奇}}\frac{8h}{n^2\pi^2}(-1)^{(n-1)/2}\cos\omega_nt\sin\frac{n\pi x}{L}.$$

**检验**：(i) $x=L/2$、$t=0$ 处：$\sin\frac{n\pi}{2}=(-1)^{(n-1)/2}$，两项相乘恒为 $1$，所以 $u=\frac{8h}{\pi^2}\sum_{n\ \text{奇}}\frac1{n^2}=\frac{8h}{\pi^2}\cdot\frac{\pi^2}{8}=h$ ✓。(ii) 偶模为零：三角形关于 $x=L/2$ 对称，而偶模关于中点反对称，对称初值不激发反对称模 ✓。(iii) 量纲：$h/n^2$ 是长度 ✓。

**读法**：系数按 $1/n^2$ 衰减，比方波（$1/n$）快一个数量级，比抛物线（$1/n^3$）慢一档——**衰减的幂次就是初值的「折角数」**：折线有一个角，$1/n^2$。这也解释了为什么拨弦的声音比敲击声更「干净」：拨弦的初值连续，谱衰减得快。

**2.12**

**思路**：已知解是单一本征模，直接用 2.5.1 的单模能量公式，不必重算积分。也可以回定义算一遍作核对——两条路应当给出同一个数。

**过程**：解为 $u=A\sin\frac{3\pi x}{L}\cos\omega_3t$，即 $q_3(t)=A\cos\omega_3t$，其余 $q_n=0$。由 2.5.1，

$$E=\frac{\rho L}{4}\sum_n\left[\left(\frac{dq_n}{dt}\right)^2+\omega_n^2q_n^2\right].$$

只剩 $n=3$ 一项：$\frac{dq_3}{dt}=-A\omega_3\sin\omega_3t$，代入

$$E=\frac{\rho L}{4}\left[A^2\omega_3^2\sin^2\omega_3t+A^2\omega_3^2\cos^2\omega_3t\right]=\frac{\rho L}{4}A^2\omega_3^2.$$

**结果**：

$$E=\frac{\rho L}{4}A^2\omega_3^2=\frac{\pi^2}{4}\cdot\frac{\rho c^2A^2}{L}\cdot 9\quad(\text{用 }\omega_3=3\pi c/L).$$

最简形式就是 $E=\frac{\rho L}{4}A^2\omega_3^2$，单位焦耳。

**检验**：(i) 量纲：$\mathrm{kg/m\cdot m\cdot m^2/s^2}=$ 焦耳 ✓。(ii) 用定义核对，取 $t=0$（此时动能为零，能量全在势能）：$E=\frac T2\int_0^L(u_x)^2dx=\frac T2A^2\left(\frac{3\pi}{L}\right)^2\cdot\frac L2=\frac{TL}{4}A^2\frac{9\pi^2}{L^2}$，再用 $Tk_3^2=\rho\omega_3^2$ 即得同一式 ✓。(iii) 与时间无关（能量守恒）✓。

**读法**：同样的振幅 $A$，第三模的能量是基模的 $9$ 倍（$E\propto\omega^2$）。**高阶模「贵」**：把能量塞进短波长，需要更大的张力做功。这条在数值计算里很重要：截断到第 $N$ 项时，被丢掉的高阶模并不是「小能量」，只是「小振幅」。

## B 组　物理应用

**2.13**

**思路**：一根两端固定的弦，$c=\sqrt{T/\rho}$ 与 $\nu_n=nc/2L$ 都是现成公式，代数字即可。先算 $c$ 再算频率，避免一次性代入出错。

**过程**：

$$c=\sqrt{\frac{T}{\rho}}=\sqrt{\frac{70}{4.5\times10^{-3}}}=124.7\ \mathrm{m/s}.$$

$$\nu_1=\frac{c}{2L}=\frac{124.7}{2\times0.65}=95.9\ \mathrm{Hz},\quad \nu_2=2\nu_1=191.9\ \mathrm{Hz},\quad \nu_3=3\nu_1=287.8\ \mathrm{Hz}.$$

**结果**：$c=124.7\ \mathrm{m/s}$；$\nu_1=95.9\ \mathrm{Hz}$，$\nu_2=191.9\ \mathrm{Hz}$，$\nu_3=287.8\ \mathrm{Hz}$。

**检验**：(i) 量纲：$\sqrt{\mathrm{N/(kg/m)}}=\sqrt{\mathrm{m^2/s^2}}=\mathrm{m/s}$ ✓。(ii) 量级：$96\ \mathrm{Hz}$ 在吉他低音弦的范围内（G2 约 $98\ \mathrm{Hz}$），合理 ✓。(iii) 泛音成整数倍：$2\nu_1=191.9$、$3\nu_1=287.8$ ✓。

**读法**：调音就是调 $T$：$\nu\propto\sqrt T$，张力加倍只升高约五度（$\sqrt2$ 倍），不是八度。**吉他弦轴转一点点，音高变化不线性**，这就是调音要反复微调的原因。

**2.14**

**思路**：温度升高，弦想伸长，但两端被钉住，伸长的趋势被转化成**张力下降**。张力变了，频率就变。这条路只需三步：几何约束（热应变）→ 弹性关系（张力变化）→ 频率关系（$\nu\propto\sqrt T$）。

**过程**：截面 $A=\pi(0.2\times10^{-3})^2=1.257\times10^{-7}\ \mathrm{m^2}$，$EA=2.0\times10^{11}\times1.257\times10^{-7}=2.51\times10^4\ \mathrm{N}$。初始应变

$$\varepsilon=\frac{T}{EA}=\frac{70}{2.51\times10^4}=2.79\times10^{-3}.$$

升温 $\Delta\theta$ 时自由热应变 $\alpha\Delta\theta$；两端固定使总长度不变，于是弹性应变减少同样的量，张力变化

$$\Delta T=-EA\,\alpha\Delta\theta=-2.51\times10^4\times1.2\times10^{-5}\times10=-3.0\ \mathrm{N}.$$

$$\frac{\Delta T}{T}=\frac{-3.0}{70}=-4.3\%,\qquad \frac{\Delta\nu}{\nu}=\frac12\frac{\Delta T}{T}=-2.15\%.$$

音分：$1200\log_2(1-0.0215)=-37.7$ 音分。

**结果**：张力降 $4.3\%$，频率降 $2.15\%$，约 $-38$ 音分。

**检验**：(i) 符号：变热→变松→变低，符号为负 ✓。(ii) 量纲：$EA\alpha\Delta\theta$ 是 $\mathrm{N}$ ✓。(iii) 对照：人能分辨约 $5$ 音分，$-38$ 音分远远听得出来 ✓。

**读法**：吉他在暖房间里偏低、冷的时候偏高，原因就在这里。**这也说明「音准」依赖于环境温度**：专业演出前要把琴暖到位再调音，而不是一进门就调。

**2.15**

**思路**：拨弦位置决定各模被激发的比例。用峰在 $x_0$、高 $h$ 的三角形系数通式，代入 $x_0=L/5$，看哪个 $n$ 使 $\sin\frac{n\pi x_0}{L}=0$。**分子为零就是完全不响**，与振幅大小无关。

**过程**：由 2.11 之前的推导，

$$a_n=\frac{2hL^2}{n^2\pi^2x_0(L-x_0)}\sin\frac{n\pi x_0}{L},\qquad x_0=\frac L5.$$

先算 $x_0(L-x_0)=\frac{L}{5}\cdot\frac{4L}{5}=\frac{4L^2}{25}$，于是

$$a_n=\frac{2hL^2}{n^2\pi^2\cdot4L^2/25}\sin\frac{n\pi}{5}=\frac{25h}{2n^2\pi^2}\sin\frac{n\pi}{5}.$$

$\sin\frac{n\pi}{5}=0$ 当 $n=5,10,15,\dots$

**结果**：$n=5,10,15,\dots$ 的模完全不被激发；其余模的系数为

$$a_n=\frac{25h}{2n^2\pi^2}\sin\frac{n\pi}{5}.$$

**检验**：(i) $n=5$ 时 $\sin\pi=0$ ✓；节点位置 $x=jL/5$ 包含 $x=L/5$，拨弦点正好在第五模的第一个节点上 ✓。(ii) 量纲：$25h/2n^2\pi^2$ 是长度 ✓。(iii) 极限：$x_0\to0$ 时 $a_n\propto\sin(n\pi x_0/L)\to0$ 对所有 $n$ 成立，但分母 $x_0$ 也趋于零，比值给出有限值——与「拨在端点拨不起来」一致（实际上端点的力臂为零）✓。

**读法**：**拨在某个模的节点上，那个模不响。** 这条规律在乐器演奏里被有意识地使用：吉他手靠改变拨弦位置来削弱某些泛音、改变音色（靠近琴桥拨，音色更亮，因为高阶模比例上升）。

**2.16**

**思路**：管乐器与弦的区别在于边界条件的物理含义：闭端是**位移节点**（空气不能穿过），开端是**位移波腹**（压力等于大气压）。一端闭一端开，只能装下奇数个四分之一波长；两端都开，装整数个半波长。直接套 2.3.1 的表。

**过程**：闭–开管，$X(0)=0$、$X'(L)=0$（与 2.3 的固定–自由完全同构）：

$$k_n=\frac{(2n-1)\pi}{2L}\quad\Longrightarrow\quad \nu_n=\frac{(2n-1)c}{4L}.$$

代入 $L=0.6\ \mathrm{m}$、$c=343\ \mathrm{m/s}$，$\frac{c}{4L}=\frac{343}{2.4}=142.9\ \mathrm{Hz}$：

$$\nu_1=142.9\ \mathrm{Hz},\quad \nu_2=428.8\ \mathrm{Hz},\quad \nu_3=714.6\ \mathrm{Hz}.$$

两端都开：$k_n=\frac{n\pi}{L}$，$\nu_n=\frac{nc}{2L}=285.8n\ \mathrm{Hz}$，即 $1:2:3:\cdots$

**结果**：闭–开管 $143,\ 429,\ 715\ \mathrm{Hz}$（奇数倍）；开–开管 $286n\ \mathrm{Hz}$（全整数倍）。

**检验**：(i) 量纲：$c/L$ 是 $\mathrm{s^{-1}}$ ✓。(ii) 基频对应波长 $4L=2.4\ \mathrm{m}$，即 $\lambda/4=L$ ✓。(iii) 数值：$143\ \mathrm{Hz}$ 接近 D3（$147\ \mathrm{Hz}$），符合单簧管低音区的实际 ✓。

**读法**：同一根管子，一端堵住就把泛音从 $1:2:3$ 改成 $1:3:5$，音色从「明亮」变「空旷」。**单簧管与笛子的音色差别，一半来自这个整数倍的取舍**，不是吹奏技巧。这也是「边界条件写死泛音结构」最直接的听觉证据。

**2.17**

**思路**：这是标准的一维热传导初值问题：杆两端恒零、初值 100，用 2.7.3 的正弦展开。问「降到 50 度要多久」，就看展开式里起主导的那一项——指数上是 $n^2$，$n=1$ 的项衰减最慢，稍后就会压过其余项。先用首模算出时间，再回头确认其余项确实可以忽略。

**过程**：$L=1\ \mathrm{m}$、$a^2=1.2\times10^{-5}\ \mathrm{m^2/s}$。初值展开系数

$$A_n=\frac2L\int_0^L100\sin\frac{n\pi x}{L}dx=\frac{200}{n\pi}\left(1-(-1)^n\right)=\frac{400}{n\pi}\ (n\ \text{奇}).$$

于是

$$u(x,t)=\frac{400}{\pi}\sum_{n\ \text{奇}}\frac1n e^{-a^2n^2\pi^2t/L^2}\sin\frac{n\pi x}{L}.$$

中点 $x=L/2$，$\sin\frac{n\pi}{2}=(-1)^{(n-1)/2}$，只留 $n=1$：

$$50\approx\frac{400}{\pi}e^{-\lambda t},\qquad \lambda=\frac{a^2\pi^2}{L^2}=1.184\times10^{-4}\ \mathrm{s^{-1}}.$$

解出 $e^{-\lambda t}=\frac{\pi}{8}=0.3927$，$t=\frac{\ln(8/\pi)}{\lambda}$。

**结果**：

$$t=\frac{0.9347}{1.184\times10^{-4}}=7.89\times10^3\ \mathrm{s}\approx2.2\ \mathrm{h}.$$

**检验**：(i) 量纲：$\lambda$ 是 $1/\text{s}$，$t$ 是 s ✓。(ii) 忽略 $n=3$：在此时刻 $e^{-9\lambda t}=(e^{-\lambda t})^9=0.3927^9=1.8\times10^{-4}$，乘 $1/3$ 后约 $6\times10^{-5}$，对 $50$ 的贡献是 $0.008\ \mathrm{K}$，确实可以忽略 ✓。(iii) 端点：$t=0$ 时级数和为 $100$（$\sum_{n\ \text{奇}}1/n=\pi/4$ 的奇延拓），$t\to\infty$ 时 $u\to0$ ✓。

**读法**：热扩散的时间尺度是 $L^2/a^2=1/1.2\times10^{-5}\approx8.3\times10^4\ \mathrm{s}$（约 23 小时），本题只要 2.2 小时是因为「降到一半」只需 $\ln(8/\pi)\approx0.93$ 个时间常数。**杆越长，时间按平方增长**：$1\ \mathrm{m}$ 要两小时，$10\ \mathrm{cm}$ 只要一分多钟。

**2.18**

**思路**：自重是均匀分布的横向力，与例 2.4 完全同型。既然只问静态垂度，不必展开级数——直接解稳态方程 $c^2u''=-F_0$ 加两端为零，一行就能得到抛物线。**先求静态、再用级数核对**，是最省事的分工。

**过程**：单位长度重力 $F_0=\rho g=4.5\times10^{-3}\times9.8=4.41\times10^{-2}\ \mathrm{N/m}$。稳态满足（例 2.4）

$$c^2\frac{d^2u_s}{dx^2}=-F_0\quad\Longrightarrow\quad u_s(x)=\frac{F_0}{2c^2}x(L-x)=\frac{\rho g}{2T}x(L-x).$$

中点 $x=L/2$：

$$\delta=u_s\Big(\frac L2\Big)=\frac{\rho gL^2}{8T}=\frac{4.41\times10^{-2}\times0.65^2}{8\times70}=3.3\times10^{-5}\ \mathrm{m}.$$

要让 $\delta=1\ \mathrm{mm}$，解 $T=\frac{\rho gL^2}{8\delta}=\frac{4.41\times10^{-2}\times0.4225}{8\times10^{-3}}=2.3\ \mathrm{N}$。

**结果**：$\delta=3.3\times10^{-5}\ \mathrm{m}=0.033\ \mathrm{mm}$；要达 $1\ \mathrm{mm}$ 需把张力降到约 $2.3\ \mathrm{N}$（或把弦加长到 $3.6\ \mathrm{m}$）。

**检验**：(i) 量纲：$\rho gL^2/T$ 是 $\mathrm{(N/m)\cdot m^2/N}=\mathrm{m}$ ✓。(ii) 与级数解一致：$u_s=\sum_{n\ \text{奇}}\frac{4F_0}{n\pi\omega_n^2}\sin\frac{n\pi x}{L}$，在 $L/2$ 处求和得 $\frac{F_0L^2}{8c^2}$（例 2.4 已算）✓。(iii) 极限：$T\to\infty$ 时 $\delta\to0$，弦绷得越紧越直 ✓。

**读法**：$3\times10^{-5}\ \mathrm{m}$ 的垂度比头发丝还细，所以「水平弦」近似在这个量级上完全安全。反过来，**张力越小、弦越长，自重越不可忽略**——吊床就是 $T$ 很小的极端情形，那时抛物线近似本身也不成立了（大变形）。

**2.19**

**思路**：一端固定、一端被 $A\cos\Omega t$ 驱动的稳态解已在 2.7.2 求出：$X(x)=A\sin(\Omega x/c)/\sin(\Omega L/c)$。最大位移就是 $A/|\sin(\Omega L/c)|$。把 $\Omega L/c$ 用 $\Omega/\omega_1$ 表示即可，注意 $\omega_1 L/c=\pi$。

**过程**：$\Omega L/c=\pi\frac{\Omega}{\omega_1}$，所以

$$\frac{X_{\max}}{A}=\frac{1}{|\sin(\pi\Omega/\omega_1)|}.$$

$\Omega=0.9\omega_1$：$\sin0.9\pi=\sin0.1\pi=0.309$，放大 $3.24$ 倍。

$\Omega=1.9\omega_1$：$\sin1.9\pi=\sin(2\pi-0.1\pi)=-\sin0.1\pi=-0.309$，绝对值同样是 $0.309$，放大 $3.24$ 倍。

**结果**：两种情形最大位移都是 $3.24\ \mathrm{mm}$（$A=1\ \mathrm{mm}$）。相位相反（$1.9\omega_1$ 时 $X/A<0$）。

**检验**：(i) $\Omega=\omega_1$ 时 $\sin\pi=0$，放大倍数发散，与 2.7.2 的共振条件一致 ✓。(ii) $\Omega\to0$ 时 $\sin(\pi\Omega/\omega_1)\approx\pi\Omega/\omega_1\to0$，比值趋于 $1$——准静态，位移等于驱动幅度，符合直觉 ✓。(iii) 量纲：比值无量纲，乘 $A$ 得长度 ✓。

**读法**：放大倍数只取决于「离最近的共振有多远」：$0.9\omega_1$ 离 $\omega_1$ 差 $0.1\omega_1$，$1.9\omega_1$ 离 $2\omega_1$ 也差 $0.1\omega_1$，所以两者一样大，只差一个符号（相位反了 $180^\circ$）。**共振的「危险程度」由频率比决定，不由驱动频率的绝对值决定。**

**2.20**

**思路**：$Q$、带宽、余音时间三者由同一个 $\gamma$ 决定（见 2.9.2）。已知 $\nu_1$ 与 $Q$，带宽直接用 $\Delta\nu=\nu_1/Q$，时间常数用 $\tau=2/\gamma=Q/(\pi\nu_1)$。

**过程**：$Q=\omega_1/\gamma$，$\gamma=\omega_1/Q=2\pi\nu_1/Q$。

带宽（2.9.2，半功率全宽）：

$$\Delta\nu=\frac{\nu_1}{Q}=\frac{196}{2000}=0.098\ \mathrm{Hz}.$$

时间常数（振幅按 $e^{-\gamma t/2}$ 衰减，即 $e^{-t/\tau}$，$\tau=2/\gamma$）：

$$\tau=\frac{Q}{\pi\nu_1}=\frac{2000}{\pi\times196}=3.25\ \mathrm{s}.$$

**结果**：$\Delta\nu=0.098\ \mathrm{Hz}$；$\tau=3.25\ \mathrm{s}$（振幅降到 $1/e$ 的时间）。

**检验**：(i) 量纲：$\nu/Q$ 是 $\mathrm{Hz}$，$Q/\nu$ 是 $\mathrm{s}$ ✓。(ii) 相互印证：$\tau\cdot\Delta\nu=3.25\times0.098=0.32$，与「时间常数 $\approx1/(\pi\Delta\nu)$」一致（$\frac{1}{\pi\times0.098}=3.25$）✓——带宽与余音是同一个数的两种说法。(iii) 余音 3 秒对一根 $196\ \mathrm{Hz}$ 的弦合理 ✓。

**读法**：$Q=2000$ 的弦，驱动频率偏离 $0.1\ \mathrm{Hz}$，振幅只掉到峰值的 $1/\sqrt{1+(0.1/0.098)^2}\approx70\%$。**高 $Q$ 的系统频率选择性极强**：这既是乐器音准清晰的原因，也是为什么调音时要靠拍（差频）而不能靠耳朵直接判断响度。

**2.21**

**思路**：矩形膜的本征频率 $\nu_{mn}=\frac c2\sqrt{\frac{m^2}{a^2}+\frac{n^2}{b^2}}$，$a=b$ 时简化为 $\frac{c}{2a}\sqrt{m^2+n^2}$。按 $m^2+n^2$ 从小到大排序，遇到相同的平方和就是简并。

**过程**：$\frac{c}{2a}=\frac{80}{2\times0.3}=133.3\ \mathrm{Hz}$，所以 $\nu_{mn}=133.3\sqrt{m^2+n^2}\ \mathrm{Hz}$。逐个算平方和：

- $1^2+1^2=2$：$\nu_{11}=133.3\sqrt2=188.6\ \mathrm{Hz}$；
- $1^2+2^2=5$（$(1,2)$ 与 $(2,1)$ 两个模）：$\nu=133.3\sqrt5=298.1\ \mathrm{Hz}$；
- $2^2+2^2=8$：$\nu=133.3\sqrt8=377.1\ \mathrm{Hz}$；
- $1^2+3^2=10$（同样两个模）：$\nu=133.3\sqrt{10}=421.6\ \mathrm{Hz}$。

**结果**：

| $(m,n)$ | $(1,1)$ | $(1,2),(2,1)$ | $(2,2)$ | $(1,3),(3,1)$ |
|---|---|---|---|---|
| $\nu$ (Hz) | 188.6 | 298.1 | 377.1 | 421.6 |
| $\nu/\nu_{11}$ | 1 | 1.581 | 2 | 2.236 |

**检验**：(i) 量纲：$c/a$ 是 $\mathrm{s^{-1}}$ ✓。(ii) 比值 $\sqrt{5/2}=1.581$、$\sqrt{8/2}=2$、$\sqrt{10/2}=2.236$，与 2.10.1 的表一致 ✓。(iii) 基频对应的半波长：$\lambda_{11}=c/\nu_{11}=0.424\ \mathrm{m}$，而 $\sqrt2 a=0.424\ \mathrm{m}$，即膜的「对角半波」✓。

**读法**：频率比里出现了 $\sqrt2$、$\sqrt{2.5}$ 这类无理数，**没有公倍数**，所以膜没有明确的音高。第 $(1,2)$ 与 $(2,1)$ 两个模频率相同但节线方向相差 $90^\circ$，是简并对——敲击位置不同，看到的图案不同（2.10.1）。

**2.22**

**思路**：正方形被轻微拉长后，简并对被劈开。劈裂量用 2.10.2 的两个频率公式算差，拍周期取差的倒数。**先算频率、再取差**，不要试图对根号做近似——这里的数值足够小，直接算更可靠。

**过程**：$a=0.20\ \mathrm{m}$、$b=0.201\ \mathrm{m}$、$c=50\ \mathrm{m/s}$。

$$\nu_{12}=\frac c2\sqrt{\frac1{a^2}+\frac4{b^2}}=\frac{50}{2}\sqrt{25+99.0}=277.3\ \mathrm{Hz},$$

$$\nu_{21}=\frac c2\sqrt{\frac4{a^2}+\frac1{b^2}}=\frac{50}{2}\sqrt{100+24.75}=279.0\ \mathrm{Hz}.$$

差频 $\Delta\nu=279.0-277.3=0.83\ \mathrm{Hz}$，拍周期 $T=1/\Delta\nu$。

**结果**：$\Delta\nu=0.83\ \mathrm{Hz}$，拍周期 $T=1.20\ \mathrm{s}$。

**检验**：(i) 极限：$b\to a$ 时两个根号相等，$\Delta\nu\to0$，拍周期趋于无穷（简并恢复）✓。(ii) 量纲：$\mathrm{m/s\cdot m^{-1}}=\mathrm{s^{-1}}$ ✓。(iii) 数量级：边长差 $0.5\%$，频率差 $0.3\%$，拍周期 1 秒多——人工可以数清 ✓。

**读法**：**拍周期是测量不对称的「放大器」**：边长差 1 mm，直接量容易出错；数拍周期 1.2 s，误差不到 $0.1$ s，就能反推出 1 mm 的差。模态实验里判断「这张膜是不是正方」，用的就是这个办法。

**2.23**

**思路**：有均匀热源的稳态问题：$\partial u/\partial t=0$，方程退化为 $a^2u''=-q$，两次积分加两端条件即可。**稳态问题不需要分离变量**，这是本题最容易走弯路的地方。

**过程**：稳态方程

$$0=a^2\frac{d^2u}{dx^2}+q\quad\Longrightarrow\quad \frac{d^2u}{dx^2}=-\frac{q}{a^2}.$$

积分两次：$u=-\frac{q}{2a^2}x^2+C_1x+C_2$。$u(0)=0$ 给 $C_2=0$；$u(L)=0$ 给 $C_1=\frac{qL}{2a^2}$。所以

$$u(x)=\frac{q}{2a^2}\left(Lx-x^2\right)=\frac{q}{2a^2}x(L-x).$$

最大值在 $x=L/2$：

$$u_{\max}=\frac{qL^2}{8a^2}=\frac{0.5\times0.25}{8\times1.1\times10^{-4}}=142\ \mathrm{K}.$$

**结果**：$u(x)=\frac{q}{2a^2}x(L-x)$，$u_{\max}=142\ \mathrm{K}$（在杆中点）。

**检验**：(i) 量纲：$\frac{\mathrm{K/s}\cdot\mathrm{m^2}}{\mathrm{m^2/s}}=\mathrm{K}$ ✓。(ii) 边界：$x=0,L$ 处为零 ✓；$x=L/2$ 处 $u''=-q/a^2<0$，是极大值 ✓。(iii) 极限 $q\to0$：$u\to0$，无源无温升 ✓。

**读法**：热量只从两端流出，所以温度剖面是抛物线、中间最高。**若杆两端绝热，这个稳态就不存在**：热量无处可去，温度一直上升（见习题 2.28 与 2.8.3 的零模讨论）。「稳态存不存在」取决于边界能不能把热量带走。

**2.24**

**思路**：挂一个砝码是集中力，静平衡方程是 $Tu''=-mg\delta(x-x_0)$，解成分段线性。中点位移可以直接用「力的平衡 + 几何」求，也可以用本征函数展开核对。**两条路对照，正好验证 $\delta$ 的展开式。**

**过程**：**路线一（几何）**：集中载荷 $F=mg$ 作用在中点，两端张力的竖直分量要平衡它。由对称性，两端各承担 $F/2$，每端的斜率是 $\frac{F/2}{T}$，所以中点位移

$$\delta=\frac{F}{2T}\cdot\frac L2=\frac{FL}{4T}=\frac{mgL}{4T}.$$

代入 $m=10\ \mathrm{g}$、$L=0.65\ \mathrm{m}$、$T=70\ \mathrm{N}$：

$$\delta=\frac{0.01\times9.8\times0.65}{4\times70}=2.3\times10^{-4}\ \mathrm{m}.$$

**路线二（级数）**：把 $\delta(x-L/2)$ 按正弦展开，$a_n=\frac{2FL}{Tn^2\pi^2}\sin\frac{n\pi}{2}$，在中点求和

$$u\Big(\frac L2\Big)=\sum_{n\ \text{奇}}\frac{2FL}{Tn^2\pi^2}=\frac{2FL}{T\pi^2}\cdot\frac{\pi^2}{8}=\frac{FL}{4T},$$

与路线一相同 ✓。

**结果**：$\delta=2.3\times10^{-4}\ \mathrm{m}=0.23\ \mathrm{mm}$。

**检验**：(i) 量纲：$\mathrm{N\cdot m/N}=\mathrm{m}$ ✓。(ii) 与例 2.4 比较：均匀自重给出 $F_0L^2/(8T)$，集中力给出 $FL/(4T)$——同一个量级，形式不同，因为力的分布不同 ✓。(iii) 线性：$m$ 加倍则 $\delta$ 加倍，符合小变形下的胡克定律 ✓。

**读法**：$0.23\ \mathrm{mm}$ 用肉眼看不出来，但用激光反射或显微镜能量到。**这正是「弦上挂小质量测张力」这类实验的原理**：量位移比量张力容易得多，而两者由 $T=mgL/(4\delta)$ 一一对应。

## C 组　深入

**2.25**

**思路**：把部分和写成积分（2.6.2 已做），过冲的极限就变成「$\mathrm{Si}$ 的最大值」这个纯数学事实。**关键是先找到峰值位置**：$\mathrm{Si}(s)$ 在 $s=\pi$ 取最大，所以峰值出现在 $N\pi x/L=\pi$ 处，位置和高度一起得到。

**过程**：由 2.6.2，把求和近似成积分（令 $t=n\pi x/L$，只有奇 $n$ 贡献一半）：

$$S_N(x)\approx\frac{2}{\pi}\,\mathrm{Si}\!\left(\frac{N\pi x}{L}\right),\qquad \mathrm{Si}(s)=\int_0^s\frac{\sin t}{t}dt.$$

$\mathrm{Si}$ 的最大值在 $s=\pi$：$\mathrm{Si}(\pi)=1.8519$。于是峰值

$$S_{\max}=\frac{2}{\pi}\times1.8519=1.1790.$$

过冲 = 峰值 $-$ 真值 $=0.1790$；跳变幅度是 $2$，所以相对跳变的过冲是 $\frac{0.1790}{2}=8.95\%$。峰值位置：$N\pi x/L=\pi\Rightarrow x=L/N$。

**结果**：

$$\text{过冲极限}=\frac{2\,\mathrm{Si}(\pi)}{\pi}-1=0.1790\quad(8.95\%\ \text{的跳变});$$

$N=100$ 时峰值在 $x=L/100=0.01L$，过冲区域宽度也是 $\sim L/100$。

**检验**：(i) 与数值直接验证对照：$N=20$ 算得 $1.1798$，$N=100$ 算得 $1.1790$，$N=400$ 算得 $1.17898$——收敛到 $1.1790$，且不随 $N$ 变小 ✓。(ii) 位置检验：$N=100$ 的数值峰值在 $x=0.0100L$ ✓。(iii) 量纲：$S_N$ 与 $f$ 同量纲（本题 $f$ 无量纲）✓。

**读法**：峰值不随 $N$ 变，只随 $N$ 变窄——**这就是「收敛但不一致收敛」的定量含义**。工程上它的后果是：用截断级数重建一个含跳变的信号，过冲会一直存在，滤波器再陡也压不掉；要么改用更光滑的基（比如升余弦窗），要么接受这 9%。

**2.26**

**思路**：三角波连续但一阶导有跳变，按 2.6.1 的判据应该 $1/n^2$。要证这一点，做两次分部积分，注意**边界项为什么消失**（$f(0)=f(L)=0$ 消掉第一次的边界项，$\sin n\pi=0$ 消掉第二次的）。过冲的讨论要分两层：函数值一致收敛（没有 9%），9% 转移到了导数里。

**过程**：三角波 $f$ 满足 $f(0)=f(L)=0$，$f'$ 分段连续且在 $x=L/2$ 处跳变。分部积分一次：

$$a_n=\frac2L\int_0^Lf\sin\frac{n\pi x}{L}dx=\frac2L\left\{\left[-f\frac{L}{n\pi}\cos\frac{n\pi x}{L}\right]_0^L+\frac{L}{n\pi}\int_0^Lf'\cos\frac{n\pi x}{L}dx\right\}.$$

边界项含 $f(0)=f(L)=0$，消失。再分部一次，边界项含 $\sin n\pi=\sin0=0$，也消失：

$$a_n=\frac{2L}{n^2\pi^2}\int_0^Lf''\sin\frac{n\pi x}{L}dx+O\!\left(\frac1{n^3}\right).$$

三角波的 $f''$ 是两根 $\delta$（在 $x=L/2$ 处正负各一），所以积分是有限常数，得 $a_n=O(1/n^2)$。

过冲：函数值是连续函数，部分和**从下方**单调逼近峰值（$x=L/2$ 处误差约 $0.4/N$，$N=40$ 时约 $1\%$），没有 9% 的过冲。把级数逐项求导后，$S_N'$ 在角点附近的峰值是 $1.179\times2=2.36$（真实斜率跳变 $\pm2$）。

**结果**：$a_n=O(1/n^2)$；函数值无 9% 过冲，误差 $\sim0.4/N$；导数在角点处过冲 $2.36$，相对跳变 $4$ 是 $9\%$。

**检验**：(i) 系数：$-1/n^2$ 的衰减与 2.6.1 的表一致（连续、一阶导跳变）✓。(ii) 数值：$N=3$ 时角点误差 $9.9\%$，$N=10$ 时 $4.0\%$，$N=40$ 时 $1.0\%$——误差乘 $N$ 约等于 $0.40$，正是 $1/N$ 律 ✓。(iii) 导数值：$2.36/2=1.18$，与方波的 $1.179$ 相同——**同一个吉布斯常数** ✓。

**读法**：函数光滑度决定「9% 跑到哪里」。有跳变，9% 在函数值上；连续但导数跳变，9% 在导数上；再光滑一阶，9% 跑到二阶导上。**所以算应力、电场、曲率这类导数型物理量时，永远要问一句：我的截断够不够？**

**2.27**

**思路**：方程非齐次、边界也非齐次，但两件麻烦事可以**分开处理再叠加**：均匀力那一部分只改形状（解 $c^2u''=-F_0$），驱动那一部分只改时间（稳态与驱动同频）。线性系统允许把两个特解直接相加。

**过程**：设 $u_p=u_1(x)+u_2(x,t)$。

**常数部分**：$c^2u_1''=-F_0$，$u_1(0)=u_1(L)=0$，解得 $u_1=\frac{F_0}{2c^2}x(L-x)$（例 2.4）。

**驱动部分**：设 $u_2=X(x)\cos\Omega t$，代入齐次方程得 $X''+\frac{\Omega^2}{c^2}X=0$，边界 $X(0)=0$、$X(L)=A$，解得 $X=\frac{A\sin(\Omega x/c)}{\sin(\Omega L/c)}$（2.7.2）。

叠加：

$$u_p(x,t)=\frac{F_0x(L-x)}{2c^2}+\frac{A\sin(\Omega x/c)}{\sin(\Omega L/c)}\cos\Omega t.$$

**结果**：上式就是完整的稳态解（瞬态项另加）。共振条件：$\sin(\Omega L/c)=0$，即 $\Omega=n\omega_1$。

**检验**：(i) 代回方程：第一部分给 $c^2u_1''=-F_0$，对时间导数为零；第二部分满足齐次波动方程 ✓。(ii) 边界：$u_1(0)=u_1(L)=0$；$X(0)=0$、$X(L)=A$，所以 $u_p(0,t)=0$、$u_p(L,t)=A\cos\Omega t$ ✓。(iii) 极限 $\Omega\to0$：第二部分趋于 $A\frac xL$，与准静态拉长一致 ✓。(iv) 叠加的合法性：方程线性，两个特解之和仍是特解 ✓。

**读法**：**非齐次方程与非齐次边界可以分开对付**，这正是线性系统的红利。注意两者的角色不同：常数力改变平衡位置（形状变抛物线），驱动改变时间行为（形状随时间振）。若把两者混在一起硬解，就会同时面对两个麻烦。

**2.28**

**思路**：两端绝热意味着零模（常数模，$k_0=0$）的时间方程不再是衰减型。把它单独拿出来看：$T_0'=F_0$，线性增长。**零模不衰减，所以没有稳态**——这不是数学困难，而是物理事实：热量只进不出。

**过程**：把源按 $\cos\frac{n\pi x}{L}$ 展开（两端绝热的本征函数，见 2.4 与 2.7.3）：$F(x,t)=F_0=\sum F_n\cos\frac{n\pi x}{L}$，其中 $F_0$ 项（$n=0$）就是平均值 $F_0$ 本身，$F_n=0$（$n\ge1$）。

零模：$T_0'=F_0\Rightarrow T_0=F_0t$（取初值为零）。

$n\ge1$：$T_n'+\frac{a^2n^2\pi^2}{L^2}T_n=F_n=0$，初值为零，所以 $T_n=0$。

**结果**：

$$u(x,t)=u(x,0)+F_0t.$$

更一般地（初值非零时）：$u(x,t)=F_0t+\sum_{n\ge1}c_ne^{-a^2n^2\pi^2t/L^2}\cos\frac{n\pi x}{L}$，平均温度以速率 $F_0$ 线性上升。

**检验**：(i) 能量：总热量变化率 $=\int q\,dx=F_0L$，而平均温度上升率 $\times$ 热容 $=F_0L$ ✓。(ii) 端点：绝热要求斜率零，常数解与 $\cos$ 解的斜率在 $x=0,L$ 处都是零 ✓。(iii) 极限 $F_0\to0$：$u$ 不变 ✓。

**读法**：**「有没有稳态」取决于边界能不能带走热量。** 两端恒温能带走（例 2.23 有抛物线稳态），两端绝热带不走（本题温度无限上升）。这条判据对波动问题同样成立：两端自由的弦受净力时整体加速，也没有稳态（2.8.3 的零模）。

**2.29**

**思路**：密度随位置变，方程里 $c$ 就不再是常数，但**分离变量的框架不变**：把 $\rho(x)$ 留在方程里，仍设 $u=X(x)T(t)$，两边仍能各自为常数。空间方程变成变系数方程，它属于施图姆–刘维尔型；正交性的权重就是密度 $\rho$。

**过程**：变密度弦的方程（单位长度质量 $\rho(x)$、张力 $T$ 恒定）：

$$\rho(x)\frac{\partial^2u}{\partial t^2}=T\frac{\partial^2u}{\partial x^2},\qquad \rho(x)=\rho_0\left(1+\frac xL\right).$$

设 $u=X(x)T(t)$，代入并除以 $XT$：

$$\rho(x)\frac{T''}{T}=T\frac{X''}{X}.$$

左边只含 $t$、右边只含 $x$，等于常数。取 $-T\omega^2$（负号理由同 2.2），得

$$X''+\frac{\rho_0\omega^2}{T}\left(1+\frac xL\right)X=0.$$

写成标准形式：把 $p=T$、$w=\rho_0(1+x/L)$、$\lambda=\omega^2$ 代入

$$\frac{d}{dx}\left[p(x)\frac{dX}{dx}\right]+\lambda w(x)X=0,$$

正是 2.5.2 的施图姆–刘维尔方程。

**结果**：空间方程 $X''+\frac{\rho_0\omega^2}{T}(1+x/L)X=0$；权 $w=\rho(x)$，即

$$\int_0^L\rho(x)X_n(x)X_m(x)dx=0\quad(n\ne m).$$

本征函数不是正弦（系数随 $x$ 变，解是艾里型函数）。

**检验**：(i) 退化：$\rho_0\to$ 常数时 $w\to$ 常数，方程回到 $X''+k^2X=0$，本征函数回到正弦 ✓。(ii) 量纲：$\rho_0\omega^2/T$ 是 $\mathrm{(kg/m)(1/s^2)/(N)}=\mathrm{m^{-2}}$ ✓，与 $X''$ 的量纲匹配。(iii) 权重：变密度弦的「质量分布」就是权重，正交性必须带它——否则展开系数会算错 ✓。

**读法**：**密度一变，本征函数就不再是正弦，但「本征函数展开」这件事没变**。粗的地方惯性大，振动会向细端偏移。第 3 章的圆膜用 $w=r$、第 4 章的球用 $w=\sin\theta$，都是同一个道理：**权重来自几何或介质的分布，不来自方程本身。**

**2.30**

**思路**：中点三角拨弦的振幅已经在 2.11 求出，$a_n\propto\frac1{n^2}\sin\frac{n\pi}{2}$。能量按 $E_n\propto\omega_n^2a_n^2\propto n^2\cdot\frac1{n^4}=\frac1{n^2}$（$n$ 奇）。接下来只需把 $1/n^2$ 的分布归一化，方法是用 $\sum_{n\ \text{奇}}1/n^2=\pi^2/8$。

**过程**：$a_n=\frac{8h}{n^2\pi^2}\sin\frac{n\pi}{2}$，$\omega_n=\frac{n\pi c}{L}$。由 2.5.1，

$$E_n\propto\omega_n^2a_n^2\propto n^2\cdot\frac{\sin^2(n\pi/2)}{n^4}=\frac{\sin^2(n\pi/2)}{n^2}.$$

对奇 $n$，$\sin^2(n\pi/2)=1$，所以 $E_n\propto1/n^2$。总能量正比于 $\sum_{n\ \text{奇}}1/n^2=\pi^2/8$，占比

$$\frac{E_n}{E_{\text{tot}}}=\frac{1/n^2}{\pi^2/8}=\frac{8}{\pi^2n^2}.$$

**结果**：

$$n=1:\ \frac{8}{\pi^2}=81.1\%,\qquad n=3:\ \frac{8}{9\pi^2}=9.0\%,\qquad n=5:\ 3.2\%,\qquad n=7:\ 1.7\%.$$

**检验**：(i) 总和：$81.1+9.0+3.2+1.7+\cdots=100\%$（因为 $\sum_{n\ \text{奇}}1/n^2=\pi^2/8$）✓。(ii) 与方波对比：方波的 $a_n\propto1/n$，$E_n\propto1$，能量在模间「均分」，总和发散；三角波的 $E_n\propto1/n^2$，收敛 ✓。(iii) 量纲：占比无量纲 ✓。

**读法**：八成以上能量在基模，所以拨弦的声音「圆润」——基音占主导，泛音只是音色。**如果想让声音变亮（泛音多），就把拨弦点移近琴桥**：那时高阶模的 $\sin(n\pi x_0/L)$ 不再被压制，能量分布变宽。这就是吉他手「靠手的位置调音色」的物理内容。

**2.31**

**思路**：受迫振动的相位由稳态公式给出，$\tan\varphi=\frac{\gamma\Omega}{\omega_1^2-\Omega^2}$。两个频率对称地落在 $\omega_1$ 两侧，所以 $\tan\varphi$ 大小相同、符号相反：一个滞后不到 $90^\circ$，一个超过 $90^\circ$。

**过程**：取 $\gamma=0.05\omega_1$。

$\Omega=0.9\omega_1$：$\omega_1^2-\Omega^2=\omega_1^2(1-0.81)=0.19\omega_1^2$，分子 $\gamma\Omega=0.045\omega_1^2$，

$$\tan\varphi=\frac{0.045}{0.19}=0.237\quad\Longrightarrow\quad\varphi=13.3^\circ.$$

$\Omega=1.1\omega_1$：$\omega_1^2-\Omega^2=-0.21\omega_1^2$，分子 $0.055\omega_1^2$，

$$\tan\varphi=\frac{0.055}{-0.21}=-0.262\quad\Longrightarrow\quad\varphi=180^\circ-14.7^\circ=165.3^\circ.$$

$\Omega=\omega_1$：分母为零，$\tan\varphi\to\pm\infty$，$\varphi=90^\circ$。

**结果**：$\varphi(0.9\omega_1)=13.3^\circ$，$\varphi(1.1\omega_1)=165.3^\circ$，$\varphi(\omega_1)=90^\circ$。

**检验**：(i) 极限 $\Omega\to0$：$\tan\varphi\to0$，$\varphi\to0$（响应跟着驱动）✓。(ii) 极限 $\Omega\to\infty$：$\tan\varphi\to0^-$，$\varphi\to180^\circ$（反相）✓。(iii) 对称性：$13.3^\circ$ 与 $180^\circ-165.3^\circ=14.7^\circ$，两侧偏离 $90^\circ$ 的角度接近但不完全相等（因为阻尼项也随 $\Omega$ 变）✓。

**读法**：$\Omega=\omega_1$ 时相位差 $90^\circ$，速度与驱动力同相，功率 $F\cdot v$ 达到最大——**「共振」的物理内容是「相位对上了」**，不是「分母为零」。工程上测相位比测幅度更灵敏：幅度在峰附近变化平缓，相位却在 $90^\circ$ 附近变化最快。

**2.32**

**思路**：$f=\cos\frac{\pi x}{L}$ 本身很光滑，但**它的奇延拓在 $x=0$ 处有跳变**（从 $-1$ 跳到 $+1$），所以正弦系数只能按 $1/n$ 衰减。先做积分，再从「只有偶 $n$」看出背后的对称性。

**过程**：用积化和差 $\cos A\sin B=\frac12[\sin(B+A)+\sin(B-A)]$：

$$a_n=\frac2L\int_0^L\cos\frac{\pi x}{L}\sin\frac{n\pi x}{L}dx=\frac1L\int_0^L\left[\sin\frac{(n+1)\pi x}{L}+\sin\frac{(n-1)\pi x}{L}\right]dx.$$

对 $n$ 奇：$n\pm1$ 都是偶数，两个积分都是 $\frac{L}{q\pi}(1-\cos q\pi)=0$，所以 $a_n=0$。

对 $n$ 偶（$n\ge2$）：$n\pm1$ 为奇数，每个积分等于 $\frac{2L}{q\pi}$，于是

$$a_n=\frac1L\cdot\frac{2L}{\pi}\left[\frac1{n+1}+\frac1{n-1}\right]=\frac{2}{\pi}\cdot\frac{2n}{n^2-1}=\frac{4n}{\pi(n^2-1)}.$$

**结果**：

$$a_n=\frac{4n}{\pi(n^2-1)}\ (n\ \text{偶}),\qquad a_n=0\ (n\ \text{奇}).$$

**检验**：(i) $x=L/2$ 处：$n$ 偶时 $\sin\frac{n\pi}{2}=0$，级数为零；而 $\cos\frac{\pi}{2}=0$ ✓。(ii) 衰减：$a_n\sim\frac{4}{\pi n}$，是 $1/n$ ✓，与 2.6.1 的判据一致（$f(0)=1\ne0$，边界项不为零）。(iii) 数值：$x=L/4$ 处真值 $0.7071$，取到 $n=200$ 的偶项得 $0.7039$，误差 $0.45\%$——收敛很慢，正是 $1/n$ 的表现 ✓。

**读法**：$\cos\frac{\pi x}{L}$ 在区间内部很光滑，但在端点处不为零，奇延拓就制造了一个跳变。**端点是否匹配，比内部是否光滑更要命**：内部再光滑，端点值不对，级数照样慢。做数值展开前，先检查 $f(0)$、$f(L)$ 是不是零。

## 概念与判断

**2.33** **错。**

**理由**：连续只保证 $f$ 自身没有跳变，但正弦级数看的是**奇延拓后的周期函数**。它在 $x=0$ 处的值是 $0$，而 $f(0)$ 一般不为零，于是延拓后在端点出现跳变，级数在端点附近照样有 吉布斯过冲。

**反例**：$f(x)=1$ 在 $(0,L)$ 上连续，但 $f(0)=1\ne0$，奇延拓后在 $x=0$ 从 $-1$ 跳到 $+1$，部分和过冲 $8.95\%$，且不随 $N$ 消失（2.6.2）。

**正确的条件**：$f$ 连续**且** $f(0)=f(L)=0$（端点匹配），再要求分段光滑，才有一致收敛。

**2.34** **错。**

**理由**：正交性不是「同一个方程」的自动结果，而是「同一个方程 + 同一组边界条件 + 同一个权重」三件事的共同结果。不同边界条件对应不同的本征值问题，它们各自内部正交，但**彼此之间**一般不正交。

**反例**：$\sin\frac{\pi x}{L}$ 属于两端固定（$k=\pi/L$），$\sin\frac{3\pi x}{2L}$ 属于固定–自由（$k=3\pi/2L$）。两者都满足 $X''+k^2X=0$，但

$$\int_0^L\sin\frac{\pi x}{L}\sin\frac{3\pi x}{2L}dx=0.255\ne0.$$

**推论**：混用不同边界条件的本征函数做展开，投影公式失效，系数会算错。

**2.35** **错。**

**理由**：不能直接分离，但可以**先齐次化再分离**：造一个满足非齐次边界的 $w$（多项式最省事），令 $v=u-w$，$v$ 的边界就是齐次的，然后对 $v$ 分离变量。代价是方程多出源项 $-\frac{\partial^2w}{\partial t^2}$、初值被平移。

**例子**：弦右端被 $A\cos\Omega t$ 驱动，取 $w=A\frac xL\cos\Omega t$，$v$ 满足齐次边界；若只求稳态，可以直接设 $u=X(x)\cos\Omega t$（2.7.2），解得 $X=A\sin(\Omega x/c)/\sin(\Omega L/c)$。

**2.36** **错。**

**理由**：线性无阻尼时解是 $T_n=\frac{F_n}{2\omega_n}t\sin\omega_nt$——振幅按 $t$ **线性增长**，不是无穷大（2.9.3）。有阻尼时稳态峰值是 $F_n/(\gamma\omega_n)$，有限。真实上限由两个机制给出：非线性（振幅大 → 张力变 → 频率上移 → 自动失谐）与材料破坏。

**例子**：弦共振时若振幅大到 $\partial u/\partial x\sim1$，小振幅假设失效，方程本身要改；工程结构可能在振幅远未「发散」前就屈服。

**2.37** **错。**

**理由**：吉布斯过冲的极限值是跳变的 $8.95\%$，与 $N$ **无关**；$N$ 增大只让过冲区域变窄（宽度 $\sim L/N$），峰值位置 $x=L/N$ 向跳变点靠拢。数学上这是「逐点收敛但不一致收敛」的必然结果，多取项只能让错误「更集中」，不能让错误「更小」。

**例子**：用 $N=100$ 项重建方波，峰值是 $1.179$；把 $N$ 增到 $10000$，峰值仍是 $1.179$，只是尖峰宽度从 $L/100$ 缩到 $L/10000$。**峰值一点没降。**

**正确的做法**：改初值（让它连续）、换基函数（用光滑窗），或者在积分量（能量、均方误差）的意义下接受它。

**2.38** **错。**

**理由**：同频是**对称性**的结果，不是巧合。正方形膜的 $(1,2)$ 与 $(2,1)$ 的 $m^2+n^2$ 都等于 $5$，所以频率相同；任何破坏正方性的微扰（$a\ne b$）都会把两模劈开。对称性越高，简并越多。

**例子**：$a=0.20\ \mathrm{m}$、$b=0.201\ \mathrm{m}$ 时，两模频率差 $0.83\ \mathrm{Hz}$，出现 $1.2\ \mathrm{s}$ 的拍（习题 2.22）——简并一破，拍就出现。

**2.39** **对。**

**理由**：两端自由时 $k_n=n\pi/L$ 含 $n=0$，对应 $X_0=1$、$\omega_0=0$。它的时间方程是 $T''=0$，解为 $T=a+bt$，即整根弦匀速整体平移（或静止在新位置）——没有回复力，也不振动。两端固定时位移被钉在零，$X_0=1$ 不是解，所以没有零模。

**物理含义**：位置在这类系统里不是被约束的量；这也是诺伊曼问题可解性条件（净力必须为零）的来源（2.8.3）。

**2.40** **错。**

**理由**：源的空间形状决定它能激发哪些模。展开后

$$F_n=\frac2L\int_0^LF_0\sin\frac{3\pi x}{L}\sin\frac{n\pi x}{L}dx=F_0\delta_{n3},$$

只有 $F_3\ne0$，其余模的方程右端为零；若初始静止，那些模始终保持为零。

**读法**：想让结构只按某个形状振动，就把力做成那个形状——这就是模态控制的原理（2.8.1）。

## 第 3 章

> 每题给思路、关键步骤、结果、检验和物理读法。缺的步骤请自己补全后再看。

**3.1** **思路**：$r$、$\varphi$ 是 $x,y$ 的函数，用隐函数求导最快；两个恒等式则是链式法则的自洽性检验。

由 $r^2=x^2+y^2$ 两边对 $x$ 求导：$2r\frac{\partial r}{\partial x}=2x$，所以

$$\frac{\partial r}{\partial x}=\frac{x}{r}=\cos\varphi .$$

对 $y$ 同理，得 $\frac{\partial r}{\partial y}=\frac{y}{r}=\sin\varphi$。

$\varphi$ 从 $\tan\varphi=y/x$ 求。两边对 $x$ 求导：

$$\frac{1}{\cos^2\varphi}\frac{\partial\varphi}{\partial x}=-\frac{y}{x^2}
\;\Longrightarrow\;
\frac{\partial\varphi}{\partial x}=-\frac{y}{x^2}\cos^2\varphi
=-\frac{r\sin\varphi}{r^2\cos^2\varphi}\cos^2\varphi=-\frac{\sin\varphi}{r}.$$

对 $y$ 同理得 $\frac{\partial\varphi}{\partial y}=\frac{\cos\varphi}{r}$。

**结果：**

$$\frac{\partial r}{\partial x}=\cos\varphi,\quad
\frac{\partial\varphi}{\partial x}=-\frac{\sin\varphi}{r},\quad
\frac{\partial r}{\partial y}=\sin\varphi,\quad
\frac{\partial\varphi}{\partial y}=\frac{\cos\varphi}{r}.$$

**检验：** 代入两组平方和，$\cos^2\varphi+\sin^2\varphi=1$；$\frac{\sin^2\varphi}{r^2}+\frac{\cos^2\varphi}{r^2}=\frac{1}{r^2}$。后者量纲是 $1/\text{长度}^2$，而角度无量纲、$x$ 有长度，量纲对得上。

**读法：** 第二个恒等式说明「角度的梯度」量级是 $1/r$——离圆心越远，同样的角位移对应的实际距离越长。这就是 3.3 节里所有 $1/r$ 因子的源头。

**3.2** **思路**：把极坐标的 $\nabla^2=\frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial}{\partial r}\right)+\frac{1}{r^2}\frac{\partial^2}{\partial\varphi^2}$ 直接作用在三个函数上，选这三个是因为它们在直角坐标里能独立验算。

（a）$u=r^2$：$\frac{\partial u}{\partial r}=2r$，于是

$$\nabla^2(r^2)=\frac{1}{r}\frac{\mathrm{d}}{\mathrm{d}r}\left(r\cdot 2r\right)
=\frac{1}{r}\frac{\mathrm{d}}{\mathrm{d}r}\left(2r^2\right)=\frac{4r}{r}=4 .$$

（b）$u=\ln r$：$\frac{\partial u}{\partial r}=\frac1r$，$\frac{\partial^2u}{\partial r^2}=-\frac{1}{r^2}$，

$$\nabla^2(\ln r)=-\frac{1}{r^2}+\frac{1}{r}\cdot\frac{1}{r}=0 .$$

（c）$u=r\cos\varphi$：径向项给 $\frac{1}{r}\frac{\partial}{\partial r}\left(r\cos\varphi\right)=\frac{\cos\varphi}{r}$；角向项给 $\frac{1}{r^2}\frac{\partial^2}{\partial\varphi^2}(r\cos\varphi)=-\frac{\cos\varphi}{r}$，

$$\nabla^2(r\cos\varphi)=\frac{\cos\varphi}{r}-\frac{\cos\varphi}{r}=0 .$$

**结果：** $\nabla^2(r^2)=4$，$\nabla^2(\ln r)=0$，$\nabla^2(r\cos\varphi)=0$。

**检验：**（a）在直角坐标里 $\nabla^2(x^2+y^2)=2+2=4$ ✓；（c）$r\cos\varphi=x$，而 $\nabla^2x=0$ ✓。两把尺子量同一个量，读数一致。

**读法：** $r^2$ 不是调和函数（$\nabla^2r^2=4\neq0$），$r\cos\varphi$ 是——**同样是「$r$ 的幂」，只有 $m=1$ 那一支（$r^m\cos m\varphi$）满足拉普拉斯方程**，这就是 3.10 节圆柱静电场解的来源。

**3.3** **思路**：自伴形式的关键动作是「乘一个因子，把两项导数凑成一个整体导数」。对 $x^2y''+xy'$ 来说，这个因子是 $x$。

原方程 $x^2\frac{\mathrm{d}^2y}{\mathrm{d}x^2}+x\frac{\mathrm{d}y}{\mathrm{d}x}+(x^2-m^2)y=0$ 除以 $x$：

$$x\frac{\mathrm{d}^2y}{\mathrm{d}x^2}+\frac{\mathrm{d}y}{\mathrm{d}x}+\left(x-\frac{m^2}{x}\right)y=0 .$$

前两项正好是 $\frac{\mathrm{d}}{\mathrm{d}x}\left(x\frac{\mathrm{d}y}{\mathrm{d}x}\right)=x\frac{\mathrm{d}^2y}{\mathrm{d}x^2}+\frac{\mathrm{d}y}{\mathrm{d}x}$，所以

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(x\frac{\mathrm{d}y}{\mathrm{d}x}\right)+\left(x-\frac{m^2}{x}\right)y=0 .$$

与标准形 $\frac{\mathrm{d}}{\mathrm{d}x}\left(p\frac{\mathrm{d}y}{\mathrm{d}x}\right)+(q+\lambda w)y=0$ 逐项对照。

**结果：** $p=x$，$q=-\frac{m^2}{x}$，$\lambda=1$，$w=x$。权重是 $w=x$。

**检验：** 若把方程整体除以 $x$，得到 $p=1$、$q=x-\frac{m^2}{x}$、$w=1$——表面上权重变成 1，但正交性积分会多出一个 $x$ 的测度因子，两次做法给出同一个正交关系。**判据：$w\,\mathrm{d}x$ 必须是「同一个测度」，换写法不能改变它。**

**读法：** 权重 $x$ 不是约定，是「乘 $x$ 才能凑成全导数」这个代数事实的产物；在圆盘问题里它就是面积元里的 $r$。

**3.4** **思路**：级数在 $|x|$ 不大时收敛很快，直接逐项加；$x=2.4$ 时前几项要在 $10^{-2}$ 量级相消，注意保留足够多的项。

$J_0(x)=\sum_k\frac{(-1)^k}{(k!)^2}\left(\frac{x}{2}\right)^{2k}$，把 $x=1$ 逐项列出：

$$1-0.25+0.015625-0.000434+0.000005=0.7652 .$$

$x=2.4$ 时 $\frac{x}{2}=1.2$，各项为

$$1-1.44+0.5184-0.08294+0.007465-0.000430+0.0000172=0.002508 .$$

**结果：** $J_0(1)=0.7652$，$J_0(2.4)=0.0025$。

**检验：** 与表值 $0.765198$、$0.002508$ 一致；且 $J_0$ 的第一个零点在 $2.4048$，$x=2.4$ 已非常接近零点，所以结果接近零是对的。

**读法：** $x=2.4$ 时前四项还在 $10^{-2}$ 量级，最终结果却是 $10^{-3}$——**级数本身没算错，是有效数字被吃掉了**。所以 $x\gtrsim3$ 时不要用级数直接算，改用 3.8 节的渐近式。

**3.5** **思路**：$J_0'=-J_1$ 是递推的直接推论（由 $\frac{\mathrm{d}}{\mathrm{d}x}(x^{-m}J_m)=-x^{-m}J_{m+1}$ 取 $m=0$）；于是 $J_0$ 的极值点就是 $J_1$ 的零点。

由级数 $J_1(x)=\sum_k\frac{(-1)^k}{k!(k+1)!}\left(\frac{x}{2}\right)^{2k+1}$ 逐项求导可得 $\frac{\mathrm{d}}{\mathrm{d}x}\left[x^{-m}J_m(x)\right]=-x^{-m}J_{m+1}(x)$。取 $m=0$：

$$\frac{\mathrm{d}J_0}{\mathrm{d}x}=-J_1(x) .$$

令 $\frac{\mathrm{d}J_0}{\mathrm{d}x}=0$，得 $J_1(x)=0$，查 3.6.2 节的零点表：$x_1=3.8317$、$x_2=7.0156$、$x_3=10.1735$。代回 $J_0$ 得极值。

**结果：** 极值点 $3.8317$、$7.0156$、$10.1735$；极值 $J_0=-0.4028$、$+0.3001$、$-0.2497$。

**检验：** 极值交替变号、幅度单调下降，符合 $J_0\sim\sqrt{2/(\pi x)}\cos(x-\pi/4)$ 的衰减振荡；$J_0(0)=1$ 是最大值，也符合。

**读法：** 「$J_0$ 的极值」与「$J_1$ 的零点」是同一张表的两列。在鼓膜问题里 $J_0$ 的极值是**振动最强的半径**，$J_1$ 的零点是 $J_0'$ 的零点——这份对应关系在波导 TE 模里还会反过来用。

**3.6** **思路**：高阶函数用递推降到低阶，不必重新算级数。用 $J_{m+1}(x)=\frac{2m}{x}J_m(x)-J_{m-1}(x)$。

取 $m=1$、$x=2$：

$$J_2(2)=\frac{2\cdot1}{2}J_1(2)-J_0(2)=1\times0.5767-0.2239=0.3528 .$$

再取 $m=2$：

$$J_3(2)=\frac{2\cdot2}{2}J_2(2)-J_1(2)=2\times0.3528-0.5767=0.1289 .$$

**结果：** $J_2(2)=0.3528$，$J_3(2)=0.1289$。

**检验：** 用级数独立算 $J_2(2)=\sum_k\frac{(-1)^k}{k!(k+2)!}1^{2k+2}$：$k=0$ 给 $1/2=0.5$，$k=1$ 给 $-1/6=-0.1667$，$k=2$ 给 $+1/48=0.0208$，累计 $0.354$，与递推值一致。且 $J_3<J_2<J_1$（$x<m$ 时高阶函数更小），符合小宗量行为 $J_m\sim(x/2)^m/m!$。

**读法：** 递推把「查表」变成「算一步」。数值计算库里的 $J_m$ 通常就是这样从 $J_0,J_1$ 往上推的——比逐个算级数省一个量级的时间。

**3.7** **思路**：渐近式 $j_{0,n}\approx(n-\frac14)\pi$ 是大 $n$ 的展开，直接代入算相对误差，看误差随 $n$ 怎么降。

$n=1$：$(0.75)\pi=2.3562$，真值 $2.4048$，相对误差

$$\frac{|2.3562-2.4048|}{2.4048}=2.02\% .$$

$n=2$：$(1.75)\pi=5.4978$，真值 $5.5201$，误差 $0.40\%$。

$n=3$：$(2.75)\pi=8.6394$，真值 $8.6537$，误差 $0.17\%$。

**结果：** 三个误差分别是 $2.0\%$、$0.40\%$、$0.17\%$。

**检验：** 误差比 $2.0/0.40\approx5$、$0.40/0.17\approx2.4$，与 $(2/1)^2=4$、$(3/2)^2=2.25$ 同量级，说明误差按 $1/n^2$ 下降（下一阶展开项的系数）。若误差按 $1/n$ 降，比值会接近 $2$、$1.5$，与数据不符。

**读法：** $n=3$ 时三位有效数字已够用，所以查表通常只给到 $n=4$；再往后的零点用这个式子估就够了——**高阶模式的频率误差直接由它决定**，鼓的高音区用渐近式完全够。

**3.8** **思路**：圆膜本征频率 $\omega_{m,n}=cj_{m,n}/a$，所有频率共用一个因子 $c/(2\pi a)$，剩下只是查零点表。

公共因子

$$\frac{c}{2\pi a}=\frac{30}{2\pi\times0.2}=23.87\ \text{Hz}.$$

前四个零点是 $j_{0,1}=2.4048$、$j_{1,1}=3.8317$、$j_{2,1}=5.1356$、$j_{0,2}=5.5201$（注意第三个是 $(2,1)$ 而不是 $(0,2)$，两个零点是交错的）。

$$f_{0,1}=23.87\times2.4048=57.4\ \text{Hz},\qquad
f_{1,1}=23.87\times3.8317=91.5\ \text{Hz},$$

$$f_{2,1}=23.87\times5.1356=122.6\ \text{Hz},\qquad
f_{0,2}=23.87\times5.5201=131.8\ \text{Hz}.$$

**结果：** $57.4$、$91.5$、$122.6$、$131.8\ \text{Hz}$；频率比 $1:1.593:2.136:2.295$。

**检验：** 量纲 $[c]/[a]=\text{s}^{-1}$ ✓；$a=0.2\ \text{m}$ 的膜基频在 $57\ \text{Hz}$，与人声低音区相当，量级合理。

**读法：** 比值不是整数比，所以这面膜没有明确音高；$(2,1)$ 与 $(0,2)$ 只差 $9\ \text{Hz}$，说明**中频段已经开始拥挤**，这正是鼓声听起来「糊」的原因。

**3.9** **思路**：这是展开系数的分母，用 3.7.4 节的归一化公式，或从 Bessel 方程直接分部积分。

由 $\frac{\mathrm{d}}{\mathrm{d}z}\left[\frac{z^2}{2}(J_0^2+J_1^2)\right]=zJ_0^2$（推导见 3.7.4 节），在 $[0,j_{0,1}]$ 上积分：

$$\int_0^{j_{0,1}}zJ_0^2(z)\,\mathrm{d}z=\frac{j_{0,1}^2}{2}\left[J_0^2(j_{0,1})+J_1^2(j_{0,1})\right]
=\frac{j_{0,1}^2}{2}J_1^2(j_{0,1}),$$

最后一步用了 $J_0(j_{0,1})=0$。换回 $r$：令 $z=j_{0,1}r/a$，$\mathrm{d}z=(j_{0,1}/a)\mathrm{d}r$、$z\,\mathrm{d}z=(j_{0,1}/a)^2r\,\mathrm{d}r$，

$$\int_0^a rJ_0^2\!\left(\frac{j_{0,1}r}{a}\right)\mathrm{d}r
=\left(\frac{a}{j_{0,1}}\right)^2\cdot\frac{j_{0,1}^2}{2}J_1^2(j_{0,1})
=\frac{a^2}{2}J_1^2(j_{0,1}).$$

代入 $J_1(2.4048)=0.51915$。

**结果：** $\int_0^a rJ_0^2\,\mathrm{d}r=0.1348\,a^2$。

**检验：** 量纲是 $\text{长度}^2$ ✓；与「权重为 1 的平均」$a^2/2=0.5a^2$ 相比，$0.135a^2$ 更小，因为 $J_0^2$ 在大部分区域小于 1，合理。

**读法：** 基模的均方值是峰值的 $27\%$（$0.135/0.5$），说明**能量集中在中心附近**；边缘附近几乎不振动，这正是「边缘固定」的代价。

**3.10** **思路**：圆波导的截止条件就是圆膜边界条件：$E_z(a)=0$ 给 $J_m(k_ca)=0$（TM），$\partial H_z/\partial r=0$ 给 $J_m'(k_ca)=0$（TE）。题目只要求两个最低模，直接代公式。

公共因子

$$\frac{c}{2\pi a}=\frac{3\times10^{8}}{2\pi\times0.02}=2.387\ \text{GHz}.$$

TM$_{01}$ 用 $j_{0,1}=2.4048$：

$$f_c(\mathrm{TM}_{01})=2.4048\times2.387=5.74\ \text{GHz}.$$

TE$_{11}$ 用 $j'_{1,1}=1.8412$（即 $J_1$ 的第一个零点）：

$$f_c(\mathrm{TE}_{11})=1.8412\times2.387=4.39\ \text{GHz}.$$

**结果：** $f_c(\mathrm{TM}_{01})=5.7\ \text{GHz}$，$f_c(\mathrm{TE}_{11})=4.4\ \text{GHz}$。

**检验：** $J_m'$ 的首零总比 $J_m$ 的首零小（$1.841<2.405$），所以 TE 模先传，与结果一致；量纲 $c/a=\text{s}^{-1}$ ✓。

**读法：** 「同一个 $2.405$ 既管鼓膜又管波导」——鼓面中心位移为零与导体壁切向电场为零，是同一个边界条件的两种说法。这也解释了为什么圆波导的基模不是最低的 $J_0$ 零点，而是 $J_1'$ 的零点。

**3.11** **思路**：两柱之间只有 $r$ 方向依赖，拉普拉斯方程退化为 $\frac{1}{r}\frac{\mathrm{d}}{\mathrm{d}r}\left(r\frac{\mathrm{d}V}{\mathrm{d}r}\right)=0$，解是 $\ln r$；再用高斯定理或 $E_r=-\frac{\mathrm{d}V}{\mathrm{d}r}$ 求场，最后 $C=Q/V$。

设内柱带线电荷 $\lambda$，高斯定理给

$$E_r(r)=\frac{\lambda}{2\pi\varepsilon_0r}.$$

两柱间电压

$$V(b)-V(a)=\int_b^{a}E_r\,\mathrm{d}r
=\frac{\lambda}{2\pi\varepsilon_0}\ln\frac{a}{b}.$$

单位长度电容 $C=\lambda/[V(b)-V(a)]$。

代入 $b=10^{-3}$、$a=4\times10^{-3}$，$\ln4=1.386$：

$$C=\frac{2\pi\varepsilon_0}{\ln4}=\frac{2\pi\times8.854\times10^{-12}}{1.386}=4.01\times10^{-11}\ \text{F/m}.$$

**结果：** $C=40.1\ \text{pF/m}$。

**检验：** 量纲 $\varepsilon_0$ 是 $\text{F/m}$ ✓；与 RG-58 的 $\sim100\ \text{pF/m}$ 同量级（它的 $\ln(a/b)$ 更小），合理。$a\to b$ 时 $\ln\to0$、$C\to\infty$，符合「间隙越小电容越大」。

**读法：** 电容只依赖 $\ln(a/b)$。**想让电容变大，缩间隙比换介质更有效**——$\ln$ 在 1 附近变化极快；而同轴线整体做细（$a,b$ 同比缩小）电容不变。

**3.12** **思路**：把两条一阶递推合成一个二阶方程。对 $J_0'=-J_1$ 再求一次导，出现 $J_1'$，再用 $J_1'=J_0-J_1/x$ 消掉 $J_1$。

由 $\frac{\mathrm{d}J_0}{\mathrm{d}x}=-J_1$ 再求导：

$$\frac{\mathrm{d}^2J_0}{\mathrm{d}x^2}=-\frac{\mathrm{d}J_1}{\mathrm{d}x}.$$

用 $xJ_1'=xJ_0-J_1$（即 $J_1'=J_0-\frac{J_1}{x}$）：

$$\frac{\mathrm{d}^2J_0}{\mathrm{d}x^2}=-J_0+\frac{J_1}{x}.$$

再由 $\frac{J_1}{x}=-\frac{1}{x}\frac{\mathrm{d}J_0}{\mathrm{d}x}$，得

$$\frac{\mathrm{d}^2J_0}{\mathrm{d}x^2}=-J_0-\frac{1}{x}\frac{\mathrm{d}J_0}{\mathrm{d}x}
\;\Longrightarrow\;
\frac{\mathrm{d}^2J_0}{\mathrm{d}x^2}+\frac{1}{x}\frac{\mathrm{d}J_0}{\mathrm{d}x}+J_0=0 .$$

**结果：** $J_0$ 满足零阶贝塞尔方程 $\frac{\mathrm{d}^2J_0}{\mathrm{d}x^2}+\frac{1}{x}\frac{\mathrm{d}J_0}{\mathrm{d}x}+J_0=0$。

**检验：** 小 $x$ 展开 $J_0\approx1-\frac{x^2}{4}$：$J_0''=-1/2$、$\frac{1}{x}J_0'=-1/2$、$J_0=1$，三项和为 $0$ ✓。$x\to0$ 时方程退化为 $J_0''+J_0' /x+J_0=0$，首项平衡给出 $J_0(0)=1$ 的初值。

**读法：** 贝塞尔方程与两条一阶递推完全等价——**「二阶方程」和「两个一阶关系」是同一件事的两种写法**。这条等价在数值计算里就是「用递推造表、用方程验算」。

**3.13** **思路**：轴对称柱坐标拉普拉斯方程只留径向项，解是 $\ln r$；两个边界定两个常数，再求导得场。

方程 $\frac{1}{r}\frac{\mathrm{d}}{\mathrm{d}r}\left(r\frac{\mathrm{d}V}{\mathrm{d}r}\right)=0$ 两次积分得

$$V(r)=A\ln r+B .$$

边界 $V(b)=0$、$V(a)=100\ \text{V}$，$b=0.01$、$a=0.03\ \text{m}$：

$$A\ln b+B=0,\qquad A\ln a+B=100
\;\Longrightarrow\;
A=\frac{100}{\ln(a/b)}=\frac{100}{\ln3}=91.0 .$$

于是 $B=-A\ln b=91.0\times4.605=419$，$V(r)=91.0\ln r+419$，等价写成

$$V(r)=91.0\ln\frac{r}{0.01}.$$

场 $E_r=-\frac{\mathrm{d}V}{\mathrm{d}r}=-\frac{91.0}{r}$。

**结果：** $V(r)=91.0\ln\frac{r}{0.01}\ \text{V}$，$E_r=-\frac{91.0}{r}\ \text{V/m}$；$r=2\ \text{cm}$ 处 $E=-4.55\ \text{kV/m}$（负号指向内柱）。

**检验：** $r=0.01$ 时 $V=0$ ✓，$r=0.03$ 时 $V=91.0\times1.0986=100\ \text{V}$ ✓；量纲 $[\text{V}]/[\text{m}]=\text{V/m}$ ✓。另可用高斯定理：$E\propto1/r$，两个半径处场强比 $3:1$，与 $1/r$ 一致。

**读法：** 对数解是二维电场的标志（三维点电荷是 $1/r$，二维线电荷是 $\ln r$）。**维度决定势的形状**——这一条在第 5 章的格林函数里还会再出现。
**3.14** **思路**：圆膜频率 $f=cj_{m,n}/(2\pi a)$，先算公共因子，再查零点表按数值排序（注意零点交错，不能按 $m$ 分组列）。

公共因子

$$\frac{c}{2\pi a}=\frac{55}{2\pi\times0.33}=26.53\ \text{Hz}.$$

四个最低零点按大小排是 $j_{0,1}=2.4048$、$j_{1,1}=3.8317$、$j_{2,1}=5.1356$、$j_{0,2}=5.5201$：

$$f_{0,1}=63.8\ \text{Hz},\quad f_{1,1}=101.6\ \text{Hz},\quad
f_{2,1}=136.2\ \text{Hz},\quad f_{0,2}=146.4\ \text{Hz}.$$

相邻间隔：$37.8$、$34.6$、$10.2\ \text{Hz}$。

**结果：** $63.8$、$101.6$、$136.2$、$146.4\ \text{Hz}$；**最小间隔在 $(2,1)$ 与 $(0,2)$ 之间，只有 $10.2\ \text{Hz}$**。

**检验：** $j_{2,1}=5.1356<j_{0,2}=5.5201$，两个零点靠得很近，所以这两个频率必然靠得近——数值与零点顺序一致 ✓。

**读法：** 间隔 $10\ \text{Hz}$ 已经小于人耳在 $140\ \text{Hz}$ 附近的分辨极限（约 $3$–$5\ \text{Hz}$ 的临界带），所以这两个模式会被听成「一个粗音」。**中频段零点交错、间隔变小，是鼓声浑浊的直接原因。**

**3.15** **思路**：点激励的展开系数正比于模式函数在敲击点的取值，问题化成「$J_m$ 在 $r_0=0$ 与 $r_0=a$ 处取什么值」。

展开系数

$$A_{m,n}\propto J_m\!\left(j_{m,n}\frac{r_0}{a}\right)\cos m\varphi_0 .$$

（a）$r_0=0$：$J_0(0)=1$，但对 $m\geq1$ 有 $J_m(0)=0$（小宗量 $J_m\sim(x/2)^m/m!$），所以所有 $m\geq1$ 的系数为零，只剩 $m=0$，图样是一组同心圆环。

（b）$r_0\to a$：$J_m(j_{m,n})=0$ 对一切 $m,n$ 成立（这正是边界条件），所以所有系数趋于零，什么都不响。

**结果：**（a）只激发 $m=0$ 的模式；（b）所有模式都不被激发，振幅为零。

**检验：**（b）与物理直觉一致：边界被钉死，在边界上加力推不动；且这与「展开式在 $r=a$ 处必然给出零」自洽——**公式自检的硬指标**。

**读法：** 敲中心听的是「同心圆」音色，敲边缘几乎不出声，敲中间偏外各模式都响、音色最杂。**鼓手的敲击位置就是一个「模式选择器」。**

**3.16** **思路**：初位移恰好是一个本征模，展开式只有一项；时间部分是简谐振动，频率由该模决定。

初位移与 $\varphi$ 无关且正比于 $J_0(j_{0,1}r/a)$，即展开系数只有 $A_{0,1}=u_0$，其余为零。时间因子由 $\frac{\mathrm{d}^2T}{\mathrm{d}t^2}=-\omega_{0,1}^2T$ 给出 $\cos(\omega_{0,1}t+\delta)$；初速度为零要求 $\sin$ 项系数为零、$\delta=0$。

$$u(r,t)=u_0J_0\!\left(j_{0,1}\frac{r}{a}\right)\cos(\omega_{0,1}t),\qquad
\omega_{0,1}=\frac{cj_{0,1}}{a}.$$

中心点 $r=0$ 处 $J_0(0)=1$：

$$u(0,t)=u_0\cos(\omega_{0,1}t).$$

**结果：** $u(r,t)=u_0J_0(j_{0,1}r/a)\cos(\omega_{0,1}t)$；中心点做振幅 $u_0$ 的简谐振动。

**检验：** $t=0$ 时回到初位移 ✓；$r=a$ 时 $J_0(j_{0,1})=0$，边界恒为零 ✓；$\omega_{0,1}=cj_{0,1}/a$ 的量纲 $\text{s}^{-1}$ ✓。

**读法：** 单一模式振动时，膜上每一点同频、同相（或反相），整体像一个「驻波鼓包」在呼吸。**这就是基模的直观图像**：中心鼓得最高、边缘不动。

**3.17** **思路**：$(0,3)$ 模的频率仍是查表；节圆半径由「$J_0$ 在 $r<a$ 内的零点」给出，把自变量换算成 $r$。

$f_{0,3}=cj_{0,3}/(2\pi a)$，$j_{0,3}=8.6537$：

$$f_{0,3}=\frac{30\times8.6537}{2\pi\times0.2}=206.6\ \text{Hz}.$$

节圆满足 $J_0(j_{0,3}r/a)=0$，即 $\frac{j_{0,3}r}{a}=j_{0,k}$（$k=1,2$），所以

$$r_k=a\frac{j_{0,k}}{j_{0,3}}:\qquad
r_1=0.2\times\frac{2.4048}{8.6537}=5.56\ \text{cm},\qquad
r_2=0.2\times\frac{5.5201}{8.6537}=12.76\ \text{cm}.$$

**结果：** $f_{0,3}=206.6\ \text{Hz}$；两个节圆在 $r=5.56\ \text{cm}$ 与 $12.76\ \text{cm}$。

**检验：** 两个半径都在 $(0,a)$ 内且 $r_1<r_2$ ✓；$r_2/a=0.638<1$ ✓；节圆个数 $n-1=2$ ✓，与「$(0,n)$ 模有 $n-1$ 个节圆」的规律一致。

**读法：** $(0,3)$ 模把膜分成三圈：内正、中负、外正。**节圆位置只由零点比决定，与 $a$、$c$ 无关**——换一面大小不同的鼓，节圆的相对位置一模一样。

**3.18** **思路**：点激励系数正比于 $J_m(j_{m,1}r_0/a)$，把 $r_0/a=0.7$ 代进三个模式即可；比值以 $(1,1)$ 归一最直观。

$(0,1)$：$j_{0,1}\times0.7=1.683$，$J_0(1.683)=0.408$。
$(1,1)$：$j_{1,1}\times0.7=2.682$，$J_1(2.682)=0.447$。
$(2,1)$：$j_{2,1}\times0.7=3.595$，$J_2(3.595)=0.446$。

以 $(1,1)$ 归一：

$$\frac{A_{0,1}}{A_{1,1}}=\frac{0.408}{0.447}=0.91,\qquad
\frac{A_{2,1}}{A_{1,1}}=\frac{0.446}{0.447}=1.00 .$$

**结果：** 三个强度接近相等，比值约 $0.91:1.00:1.00$。

**检验：** $r_0=0.7a$ 已接近 $(0,1)$ 与 $(1,1)$ 的「交叉点」（约 $0.6a$，两者相等），再往外 $(1,1)$ 反超——与 3.6.4 节给出的 $0.6a$ 交叉点一致 ✓。

**读法：** 敲在 $0.7a$ 处，三个低频模式几乎等强，**音色最杂、最「像鼓」**；敲在中心则只剩同心圆模式，声音最「纯」。定音鼓手把槌点放在这个区域，正是为了让 $(1,1)$ 模（音高）足够强。

**3.19** **思路**：稳态径向热传导，方程是一维柱坐标形式，边界条件「中心有限 + 表面温度给定」，两次积分即可。

方程

$$\frac{1}{r}\frac{\mathrm{d}}{\mathrm{d}r}\left(r\frac{\mathrm{d}T}{\mathrm{d}r}\right)=-\frac{q_V}{\kappa}.$$

先乘 $r$ 积分：$r\frac{\mathrm{d}T}{\mathrm{d}r}=-\frac{q_Vr^2}{2\kappa}+C_1$。中心对称性要求 $\frac{\mathrm{d}T}{\mathrm{d}r}\big|_{r=0}=0$，故 $C_1=0$。再积分：

$$T(r)=-\frac{q_Vr^2}{4\kappa}+C_2,\qquad
T(a)=T_s\;\Longrightarrow\;C_2=T_s+\frac{q_Va^2}{4\kappa}.$$

$$T(0)-T_s=\frac{q_Va^2}{4\kappa}
=\frac{2\times10^{8}\times(5\times10^{-3})^2}{4\times3}=417\ \text{K}.$$

半径加倍时 $q_V$ 不变、$a^2$ 变四倍，温升变 $1667\ \text{K}$。

**结果：** $T(0)=300+417=717\,^\circ\text{C}$；半径加倍后 $T(0)-T_s=1667\ \text{K}$，即约 $1967\,^\circ\text{C}$。

**检验：** 量纲 $\frac{\text{W/m}^3\cdot\text{m}^2}{\text{W/(m}\cdot\text{K)}}=\text{K}$ ✓；$q_V\to0$ 时 $T\to T_s$ ✓（无热源时温度均匀）。

**读法：** 温升与半径的平方成正比。**这就是燃料棒必须做得细的定量原因**：半径加倍，中心温度不是加倍而是四倍；再叠加功率密度，很容易超过熔点。

**3.20** **思路**：环形区域不含 $r=0$，通解必须同时保留 $J_0$ 与 $Y_0$；两个边界条件给出 $2\times2$ 齐次方程组，行列式为零即特征方程。

径向通解 $R(r)=AJ_0(kr)+BY_0(kr)$。边界 $R(b)=R(a)=0$：

$$\begin{cases}AJ_0(kb)+BY_0(kb)=0,\\ AJ_0(ka)+BY_0(ka)=0.\end{cases}$$

有非零解要求系数行列式为零：

$$J_0(kb)Y_0(ka)-J_0(ka)Y_0(kb)=0 .$$

取 $b=0.5a$，数值求根（从小到大扫描变号）得最低根 $ka=6.246$。与实心膜比较：

$$\frac{f_{\text{环}}}{f_{\text{实心}}}=\frac{6.246}{2.4048}=2.597 .$$

**结果：** 特征方程 $J_0(kb)Y_0(ka)-J_0(ka)Y_0(kb)=0$；$b=0.5a$ 时最低模 $ka=6.246$，基频是实心膜的 $2.60$ 倍。

**检验：** $b\to0$ 时特征方程应回到 $J_0(ka)=0$——把 $b\to0$ 代入，$J_0(kb)\to1$、$Y_0(kb)\to-\infty$，方程化为 $Y_0(ka)-J_0(ka)\cdot(-\infty)\to$ 要求 $J_0(ka)=0$ ✓。$b\to a$ 时 $ka\to\infty$（膜宽趋于零），也符合。

**读法：** 中间挖掉一半半径，基频升到 $2.6$ 倍——**环形膜更「硬」**，因为面积小了、约束多了。这也是为什么带孔的手鼓、铜锣音高更高。

**3.21** **思路**：由 $f=cj/(2\pi a)$ 反解 $c$；然后同一比例下 $(1,1)$ 模的频率随之确定。

$$f_{0,1}=\frac{c\,j_{0,1}}{2\pi a}\;\Longrightarrow\;
c=\frac{2\pi af_{0,1}}{j_{0,1}}=\frac{2\pi\times0.35\times60}{2.4048}=54.9\ \text{m/s}.$$

同一面鼓上

$$f_{1,1}=\frac{c\,j_{1,1}}{2\pi a}=\frac{54.9\times3.8317}{2\pi\times0.35}=95.7\ \text{Hz}.$$

**结果：** $c=54.9\ \text{m/s}$；此时 $f_{1,1}=95.7\ \text{Hz}$。

**检验：** 比值 $f_{1,1}/f_{0,1}=3.8317/2.4048=1.593$，与 $60/65.6$ 那组数一致 ✓——**比例只由零点决定，与 $c$ 无关**。

**读法：** 放松鼓皮（$c$ 降）让所有模式按同一比例下降，**音程关系不变**，只是整体变低。所以鼓手调音是「整体平移」，不是「改音阶」。

**3.22** **思路**：$k=0$ 的拉普拉斯方程在角向仍可分离，径向退化成欧拉方程，解是幂函数 $r^{\pm m}$；中心有限要求舍去 $r^{-m}$。

设 $T=T_0+R(r)\cos2\varphi$（常数项单独处理）。径向方程（3.10.2 节）

$$r^2\frac{\mathrm{d}^2R}{\mathrm{d}r^2}+r\frac{\mathrm{d}R}{\mathrm{d}r}-4R=0
\;\Longrightarrow\;R=Ar^2+Br^{-2}.$$

$r=0$ 在柱内，温度有限，所以 $B=0$；边界 $R(a)=T_1$ 给 $A=T_1/a^2$。于是

$$T(r,\varphi)=T_0+T_1\left(\frac{r}{a}\right)^2\cos2\varphi .$$

取 $T_0=300$、$T_1=20$、$r=0.5a$：$(r/a)^2=0.25$，$T_1\times0.25=5$。

**结果：** $T(0.05,\varphi)=300+5\cos2\varphi$，最高 $305\ \text{K}$、最低 $295\ \text{K}$。

**检验：** $r=a$ 时回到边界条件 $300+20\cos2\varphi$ ✓；$r=0$ 时 $T=300=T_0$（平均值）✓；$\cos2\varphi$ 在 $[0,2\pi)$ 内有两个极大两个极小 ✓。

**读法：** 表面 $20\ \text{K}$ 的起伏到一半半径处只剩 $5\ \text{K}$——**按 $(r/a)^m$ 衰减，$m$ 越大衰减越快**。所以圆盘中心测到的总是环平均温度，高次角向起伏只在表面附近存在。

**3.23** **思路**：母函数把「一族 Bessel 函数的求和」变成「一个指数」，取 $t=ie^{i\varphi}$ 恰好凑出 $\cos\varphi$ 的指数。

母函数 $e^{\frac{x}{2}(t-1/t)}=\sum_mJ_m(x)t^m$。取 $t=e^{i\psi}$ 得 $e^{ix\sin\psi}$；本题要 $\cos\varphi$，取 $t=ie^{i\varphi}$：

$$\frac{x}{2}\left(ie^{i\varphi}-\frac{1}{ie^{i\varphi}}\right)
=\frac{x}{2}\left(ie^{i\varphi}+ie^{-i\varphi}\right)=ix\cos\varphi .$$

左边是 $e^{ix\cos\varphi}$；右边 $\sum_mJ_m(x)(ie^{i\varphi})^m=\sum_m i^mJ_m(x)e^{im\varphi}$。所以

$$e^{ikr\cos\varphi}=\sum_{m=-\infty}^{\infty}i^mJ_m(kr)e^{im\varphi}.$$

幅度的相对大小用 $ka$ 判断。$ka=1$：$J_0=0.765$、$J_1=0.440$、$J_2=0.115$，比值 $1:0.58:0.15$。$ka=10$：$J_0=-0.246$、$J_1=0.044$、$J_2=0.255$，比值 $1:0.18:1.04$。

**结果：** $e^{ikr\cos\varphi}=\sum_m i^mJ_m(kr)e^{im\varphi}$；小 $ka$ 只需前两阶，大 $ka$ 各阶同量级。

**检验：** 令 $\varphi=0$、$r\to0$：两边都趋于 $1$（$J_0(0)=1$，其余 $J_m(0)=0$）✓；$k\to0$ 时只剩 $m=0$ 项 ✓。

**读法：** 平面波打在圆柱上时，「圆柱看到」的是一族柱面波，权重 $i^mJ_m(ka)$。**$ka\ll1$（小物体）只需 $m=0,1$ 两阶——这就是瑞利散射角分布简单的数学原因；$ka\gg1$ 时要算很多阶，Mie 级数收敛慢。**

**3.24** **思路**：把 $\int zJ_0^2$ 凑成全导数。猜 $\frac{\mathrm{d}}{\mathrm{d}z}\left[\frac{z^2}{2}(J_0^2+J_1^2)\right]$，验证它等于 $zJ_0^2$。

求导：

$$\frac{\mathrm{d}}{\mathrm{d}z}\left[\frac{z^2}{2}\left(J_0^2+J_1^2\right)\right]
=z\left(J_0^2+J_1^2\right)+z^2\left(J_0\frac{\mathrm{d}J_0}{\mathrm{d}z}+J_1\frac{\mathrm{d}J_1}{\mathrm{d}z}\right).$$

用 $\frac{\mathrm{d}J_0}{\mathrm{d}z}=-J_1$ 与 $\frac{\mathrm{d}J_1}{\mathrm{d}z}=J_0-\frac{J_1}{z}$（后者由 $\frac{\mathrm{d}}{\mathrm{d}z}(zJ_1)=zJ_0$ 展开得到）：

$$z^2\left(J_0(-J_1)+J_1\left(J_0-\frac{J_1}{z}\right)\right)=z^2\left(-\frac{J_1^2}{z}\right)=-zJ_1^2 .$$

代回：$z(J_0^2+J_1^2)-zJ_1^2=zJ_0^2$，恒等式成立。积分得

$$\int_0^XzJ_0^2\,\mathrm{d}z=\frac{X^2}{2}\left[J_0^2(X)+J_1^2(X)\right].$$

取 $X=j_{0,n}$，$J_0=0$，再换回 $r$（$z=j_{0,n}r/a$，$z\,\mathrm{d}z=(j_{0,n}/a)^2r\,\mathrm{d}r$）：

$$\int_0^a rJ_0^2\!\left(\frac{j_{0,n}r}{a}\right)\mathrm{d}r=\frac{a^2}{2}J_1^2(j_{0,n}).$$

**结果：** 两式都成立；第二式的数值系数是 $\frac12J_1^2(j_{0,1})=0.1348$（乘 $a^2$）。

**检验：** 对 $n=1$ 数值积分（$10^5$ 个点）得 $0.7793\,(a/j_{0,1})^2$，而 $\frac{j_{0,1}^2}{2}J_1^2=0.7793$ ✓，两法一致。量纲 $\text{长度}^2$ ✓。

**读法：** 这个积分是「模式自身的能量」，它就是展开系数的分母。**没有它，展开系数只能写成积分形式而无法归一化。**

**3.25** **思路**：直接看级数中 $m\to-m$ 时每一项怎么变。

$$J_{-m}(x)=\sum_{k=0}^{\infty}\frac{(-1)^k}{k!\,\Gamma(k-m+1)}\left(\frac{x}{2}\right)^{2k-m}.$$

$\Gamma(k-m+1)$ 在 $k<m$ 时发散（对应 $1/\Gamma=0$），所以求和实际从 $k=m$ 开始。令 $j=k-m$（$j=0,1,2,\dots$）：

$$J_{-m}(x)=\sum_{j=0}^{\infty}\frac{(-1)^{j+m}}{(j+m)!\,j!}\left(\frac{x}{2}\right)^{2j+m}
=(-1)^m\sum_{j=0}^{\infty}\frac{(-1)^j}{j!\,(j+m)!}\left(\frac{x}{2}\right)^{2j+m}
=(-1)^mJ_m(x).$$

**结果：** 整数 $m$ 时 $J_{-m}=(-1)^mJ_m$，两解线性相关；第二个独立解必须另找，即含对数项的 $Y_m$。

**检验：** $m=0$ 时 $J_{-0}=J_0$ ✓；$m=1$ 时级数给 $J_{-1}=-J_1$，而递推 $(2m/x)J_m=J_{m-1}+J_{m+1}$ 取 $m=0$ 得 $J_{-1}+J_1=0$，同样给 $J_{-1}=-J_1$ ✓。两条独立的路给出同一个符号，说明 $(-1)^m$ 不是人为加的。

**读法：** 整数阶是「例外」：非整数阶时 $J_{\pm m}$ 独立，通解就是两者组合；整数阶时它们撞车，必须引入 $Y_m$。**这就是为什么鼓膜问题里「第二个解」非出现不可。**

**3.26** **思路**：两个模式的径向因子都在 $r=0.5a$ 处取值，直接查表乘角向因子（取 $\cos m\varphi=1$ 方向）。

$$\frac{r_0}{a}=0.5:\qquad
J_1\!\left(\frac{j_{1,1}}{2}\right)=J_1(1.916)=0.581,\qquad
J_2\!\left(\frac{j_{2,1}}{2}\right)=J_2(2.568)=0.455 .$$

比值 $0.455/0.581=0.78$。

**结果：** $(1,1)$ 与 $(2,1)$ 在 $r=0.5a$ 处的振幅比约 $1:0.78$。

**检验：** $r\to0$ 时 $(1,1)$ 的因子 $J_1\sim r$、$(2,1)$ 的 $J_2\sim r^2$，比值趋于零 ✓（$r=0.5a$ 时 $J_2<J_1$，趋势一致）。

**读法：** 在 $0.5a$ 处敲，$(2,1)$ 只比 $(1,1)$ 弱两成，**两个模式都会被明显激发**；想强调 $(2,1)$ 要往外敲（$0.7a$ 附近两者相等），想强调 $(1,1)$ 则敲在 $0.4a$ 附近最有效。

**3.27** **思路**：同面积把圆半径与方边长联系起来，然后各用本征值公式求基频。

面积相等：$\pi a^2=L^2$，即 $L=a\sqrt{\pi}$。

圆膜：$\omega_\bigcirc=2.4048\,c/a$。
方膜（边长 $L$，基模 $(1,1)$）：$\omega_\square=c\pi\sqrt{1^2+1^2}/L=c\pi\sqrt2/(a\sqrt\pi)=c\sqrt{2\pi}/a$。

比值

$$\frac{f_\bigcirc}{f_\square}=\frac{2.4048}{\sqrt{2\pi}}=\frac{2.4048}{2.5066}=0.959 .$$

**结果：** $f_\bigcirc/f_\square=0.959$，圆膜低约 $4\%$。

**检验：** 两种膜的本征值都是 $c/a$ 量级、系数都是 $O(1)$，比值应在 1 附近 ✓；圆膜比方膜少两个角，约束更少，频率偏低，方向也对。

**读法：** 同面积的圆膜比方膜「松」，所以基频略低。**边界形状通过本征值系数直接改音高**——这是「本征函数由边界形状决定」最干净的例子。

**3.28** **思路**：热阻串联：绝缘层的导热热阻与表面换热热阻之和，分母最小处散热量最大。

单位长度散热

$$\frac{Q}{L}=\frac{2\pi(T_i-T_\infty)}{\dfrac{\ln(a/r_i)}{\kappa}+\dfrac{1}{ha}} .$$

对 $a$ 求极值，令分母导数为零：

$$\frac{\mathrm{d}}{\mathrm{d}a}\left[\frac{\ln(a/r_i)}{\kappa}+\frac{1}{ha}\right]
=\frac{1}{\kappa a}-\frac{1}{ha^2}=0
\;\Longrightarrow\;
a_c=\frac{\kappa}{h}.$$

代入 $\kappa=0.15$、$h=10$：$a_c=0.015\ \text{m}$。

**结果：** $a_c=\kappa/h=15\ \text{mm}$；芯半径小于 $15\ \text{mm}$ 时，加保温层反而散热更快。

**检验：** 量纲 $[\kappa]/[h]=\frac{\text{W/(m}\cdot\text{K)}}{\text{W/(m}^2\cdot\text{K)}}=\text{m}$ ✓；$\kappa\to0$（绝热材料）时 $a_c\to0$，即任何保温都有效 ✓。

**读法：** 细导线包保温层「更凉」不是错觉：外表面增大带来的对流增益暂时超过导热热阻的增加。**工程上芯径小于 $\kappa/h$ 时，要先加粗再保温。**

**3.29** **思路**：先由 $V$ 求场，再由导体的边界条件 $\sigma=\varepsilon_0E_n$ 求面电荷。

$$V=-E_0\cos\varphi\left(r-\frac{a^2}{r}\right).$$

$$E_r=-\frac{\partial V}{\partial r}=E_0\cos\varphi\left(1+\frac{a^2}{r^2}\right).$$

在 $r=a$ 处 $E_r=2E_0\cos\varphi$，所以

$$\sigma(\varphi)=\varepsilon_0E_r(a)=2\varepsilon_0E_0\cos\varphi .$$

**结果：** $\sigma(\varphi)=2\varepsilon_0E_0\cos\varphi$；$\varphi=0$ 一侧（外场来向）带正电，$\varphi=\pi$ 一侧带负电。

**检验：** 总量 $\int_0^{2\pi}\sigma a\,\mathrm{d}\varphi=2\varepsilon_0E_0a\int_0^{2\pi}\cos\varphi\,\mathrm{d}\varphi=0$ ✓（接地导体不净带电）。$E_0\to0$ 时 $\sigma\to0$ ✓。

**读法：** 外场把电子推到一侧，感应电荷是 $\cos\varphi$ 型——**这正是「偶极子」**：远处看，接地圆柱像一个偶极子，其强度由 $a^2E_0$ 决定。

**3.30** **思路**：公式 $T(0)-T_s=q_Va^2/(4\kappa)$ 是齐次的，直接看各量的幂次。

$$T(0)-T_s=\frac{q_Va^2}{4\kappa}\propto q_Va^2\kappa^{-1}.$$

$q_V\to2q_V$、$a\to2a$：因子 $2\times2^2=8$，温升 8 倍。
只把 $\kappa\to\kappa/2$：因子 $2$，温升 2 倍。

**结果：** 同时加倍 $q_V$ 与 $a$ 时温升为原来的 $8$ 倍；$\kappa$ 减半时温升为 $2$ 倍。

**检验：** 若 $q_V$ 与 $a$ 同步加倍，总发热功率 $\propto q_Va^2$ 变 4 倍，而散热面积 $\propto a$ 只变 2 倍——「发热涨得比散热快」，温升涨 8 倍（=4×2）✓，与公式一致。

**读法：** 功率密度与尺寸不能同时放大。**这条标度关系是「反应堆堆芯为什么做细、功率密度为什么有上限」的定量依据。**
**3.31**

**思路**：级数逐项加，看相邻项的比值什么时候把项压到 $10^{-6}$ 以下；递推用 $J_{m+1}=\frac{2m}{x}J_m-J_{m-1}$。

**过程**：$x=2$，$\frac{x}{2}=1$，$J_0(2)=\sum_k\frac{(-1)^k}{(k!)^2}$：

$$k=0:1.000000,\quad k=1:0.000000,\quad k=2:0.250000,\quad k=3:0.222222,$$
$$k=4:0.223958,\quad k=5:0.223889,\quad k=6:0.223891.$$

从 $k=6$ 起再变已在 $10^{-7}$ 以下，所以**七项**（$k=0$ 到 $6$）就到 $10^{-6}$。

递推：$J_2(2)=\frac{2\cdot1}{2}J_1(2)-J_0(2)=J_1-J_0$，

$$J_2(2)=0.576725-0.223891=0.352834,$$

$$J_3(2)=\frac{2\cdot2}{2}J_2(2)-J_1(2)=2\times0.352834-0.576725=0.128943 .$$

**结果**：$J_0(2)=0.223891$（七项到 $10^{-6}$）；$J_2(2)=0.352834$，$J_3(2)=0.128943$。

**检验**：与 3.6 题用同一递推得到的 $0.3528$、$0.1289$ 一致 ✓；且 $J_3<J_2<J_1$（$x=2<m$ 时高阶更小），符合小宗量行为 ✓。

**读法**：级数在 $x\lesssim10$ 时又快又稳；递推适合「已有低阶、要高阶」。**但两者都别用在 $m\gg x$：** 那里递推会炸（3.9.2 节），级数也会因阶乘增长而慢。

**3.32**

**思路**：二分法先找变号区间再对半分；渐近式直接代入 $n$、$m$。误差大小反映「大 $n$ 展开」在 $n=1$ 时是否成立。

**过程**：二分（步长 $0.02$ 扫描 + 200 次对分）得

$$j_{2,1}=5.135622,\qquad j_{0,10}=30.634630 .$$

渐近式：

$$j_{2,1}\approx\left(1+\frac{2}{2}-\frac14\right)\pi=1.75\pi=5.497787,$$

$$j_{0,10}\approx\left(10-\frac14\right)\pi=30.630528 .$$

相对误差：

$$\frac{|5.497787-5.135622|}{5.135622}=7.05\%,\qquad
\frac{|30.630528-30.634630|}{30.634630}=0.013\% .$$

**结果**：$j_{2,1}=5.1356$（渐近误差 $7.1\%$）；$j_{0,10}=30.6346$（渐近误差 $0.013\%$）。

**检验**：$n=10$ 时误差万分之一，与「误差按 $1/n^{2}$ 下降」的预期一致（$n=1$ 的 $2\%$ 到 $n=10$ 应降约百倍，实测 $0.013\%$，量级相符）✓。

**读法**：渐近式是**大 $n$ 展开**，$m$ 的修正项 $\frac m2\pi$ 是把 $J_m$ 的相位移动「$m\pi/2$」得到的——$n$ 小时它反而喧宾夺主。**要估高阶零点（$n\gtrsim5$）用渐近式，要头几个零点必须数值求。**

**3.33**

**思路**：能级公式 $E=\hbar^{2}j^{2}/(2m^{*}a^{2})$，先算公共因子，再乘零点的平方；能差对应光子波长用 $\lambda=hc/\Delta E$。

**过程**：$a=3\ \text{nm}$，公共因子

$$\frac{\hbar^{2}}{2m_ea^{2}}
=\frac{(1.0546\times10^{-34})^{2}}{2\times9.11\times10^{-31}\times(3\times10^{-9})^{2}}
=\frac{1.1122\times10^{-68}}{1.6398\times10^{-47}}
=6.78\times10^{-22}\ \text{J}=4.23\ \text{meV}.$$

$$E_{0,1}=4.23\times(2.4048)^{2}=4.23\times5.783=24.5\ \text{meV},$$

$$E_{1,1}=4.23\times(3.8317)^{2}=4.23\times14.68=62.1\ \text{meV}.$$

简并度：$(0,1)$ 为 1 重；$(1,1)$ 为 2 重（$m=\pm1$）。

能差 $\Delta E=62.1-24.5=37.6\ \text{meV}=0.0376\ \text{eV}$，对应

$$\lambda=\frac{hc}{\Delta E}=\frac{1240\ \text{eV}\cdot\text{nm}}{0.0376\ \text{eV}}=3.3\times10^{4}\ \text{nm}=33\ \mu\text{m}.$$

**结果**：$E_{0,1}=24.5\ \text{meV}$（1 重），$E_{1,1}=62.1\ \text{meV}$（2 重）；能差 $37.6\ \text{meV}$，波长 $33\ \mu\text{m}$。

**检验**：与例 3.8（$a=5\ \text{nm}$，$8.81\ \text{meV}$）比较：$(5/3)^{2}=2.78$，$8.81\times2.78=24.5$ ✓；$62.1/24.5=2.539=(3.8317/2.4048)^{2}$ ✓。量纲 $[\hbar^{2}/(ma^{2})]=\text{J}$ ✓。

**读法**：尺寸从 $5\ \text{nm}$ 缩到 $3\ \text{nm}$，基态能量翻近三倍——**量子点的「颜色」就是这样被尺寸调出来的**。在 $m^{*}=m_e$ 的假设下能差落在远红外；真实半导体有效质量只有 $0.1m_e$，能级整体抬高十倍，才进可见区。

**3.34**

**思路**：一般归一化公式 $\int_0^{a}rJ_m^{2}(j_{m,n}r/a)\mathrm{d}r=\frac{a^{2}}{2}J_{m+1}^{2}(j_{m,n})$，取 $m=1$、$n=1$。

**过程**：把 $r=a z/j_{1,1}$ 代入，利用 $\frac{\mathrm{d}}{\mathrm{d}z}\left[\frac{z^{2}}{2}(J_1^{2}+J_2^{2})\right]=zJ_1^{2}$（由 $J_1'=J_0-\frac{J_1}{z}$ 与 $J_0+J_2=\frac{2}{z}J_1$ 可以验证），在零点 $J_1(j_{1,1})=0$ 处得

$$\int_0^{a}rJ_1^{2}\!\left(\frac{j_{1,1}r}{a}\right)\mathrm{d}r
=\frac{a^{2}}{2}J_2^{2}(j_{1,1}).$$

查值 $J_2(3.8317)=0.402759$，平方再折半：

$$\frac{1}{2}(0.402759)^{2}=0.08111 .$$

**结果**：$\int_0^{a}rJ_1^{2}\!\left(\frac{j_{1,1}r}{a}\right)\mathrm{d}r=0.0811\,a^{2}$。

**检验**：量纲 $\text{长度}^{2}$ ✓；$J_2(j_{1,1})=0.403$ 与 $J_1(j_{0,1})=0.519$ 同量级，所以系数 $0.08$ 与基模的 $0.135$ 同量级，合理 ✓。

**读法**：这是 $(1,1)$ 模的归一化常数，用于把初始条件展开到该模。**$(1,1)$ 的系数比 $(0,1)$ 小四成**，因为它在 $r=0$ 处为零、能量更分散。

**3.35** **错。** 「位移为零」可能只是时刻的问题：$u(r,\varphi,t)=u(r,\varphi)\cos\omega t$，当 $\cos\omega t=0$ 时**整个膜同时为零**，那不是节线。节线的定义是**空间因子恒为零**，即对一切 $t$ 都有 $u=0$。

**例子：** 基模 $(0,1)$ 在 $t=T/4$ 时全膜瞬时为零，但它的节线只有边界 $r=a$ 一条（内部没有任何节线或节圆）。判断方法：换一个时刻再看，若仍为零才是节线。

**3.36** **错。** $r=0$ 根本不在同轴电缆的求解区域里，「在原点有限」这个要求无从谈起；更关键的是，二阶方程需要两个边界条件（$r=b$ 与 $r=a$），必须有 $J_m$ 与 $Y_m$ 两个独立解才能凑出非零解——舍掉一个就变成「一个常数满足两个条件」，一般无解。

**例子：** 环形膜的 $b=0.5a$ 情形：若强行舍去 $Y_0$，只剩 $J_0(ka)=0$，给出 $ka=2.405$；而真实的特征方程（保留 $Y_0$）给出 $ka=6.246$。**舍掉 $Y_0$ 会把基频算低 $2.6$ 倍。**

**3.37** **需要修正。** $m$ 是角向量子数（整数），但**局部波数**是 $m/r$，不是 $m$：固定 $\Delta\varphi$ 时弧长是 $r\Delta\varphi$，所以 $\varphi$ 方向的局部波长是 $2\pi r/m$，随 $r$ 增大而变长。

**例子：** $m=1$ 的模式在 $r=a$ 处角向波长是 $2\pi a$，在 $r=a/2$ 处只有 $\pi a$——同一条节线，靠近中心处「挤得更紧」。这就是径向方程里 $m^2/r^2$ 那一项的物理含义：**离心项**，它把高阶模式往外推。

**3.38** **错。** 高阶零点间距趋于 $\pi$，对应频率间距 $\Delta f=c/(2a)$；而基频是 $f_{0,1}=2.4048c/(2\pi a)=0.3828c/a$。两者之比

$$\frac{\Delta f}{f_{0,1}}=\frac{c/(2a)}{2.4048c/(2\pi a)}=\frac{\pi}{2.4048}=1.306,$$

不是整数。

**例子：** $a=0.35\ \text{m}$、$c=60\ \text{m/s}$ 时，$\Delta f=85.7\ \text{Hz}$、$f_{0,1}=65.6\ \text{Hz}$——高频泛音确实等间距，但间距与基频不成整数比，**所以高频也不会变成谐波列**。

**3.39** **不同意。** 权重 $r$ 有两条独立的来路：（1）数学上，把 Bessel 方程乘 $r$ 凑成自伴形式 $\frac{\mathrm{d}}{\mathrm{d}r}\left(r\frac{\mathrm{d}R}{\mathrm{d}r}\right)+\left(k^2r-\frac{m^2}{r}\right)R=0$，$k^2$ 前的系数就是 Sturm–Liouville 权重；（2）物理上，$r\,\mathrm{d}r\,\mathrm{d}\varphi$ 是面积元，正交性说的是「两个模式在面积上的交叉项为零」。

**例子：** 若漏掉 $r$、直接用 $\int J_0J_0\,\mathrm{d}r$，会算出「$J_0$ 不正交」的错误结论，展开系数随之全错——**量纲也会暴露它**（少一个长度）。

**3.40** **错。** $\sin(n\pi r/a)$ 是「两端为零」的本征函数族，与 $J_0(j_{0,1}r/a)$ 属于不同的算子、不同的边界条件，两者在 $[0,a]$ 上（带权 $r$）并不正交。用它们展开，系数不会快速衰减。

**例子：** $J_0(j_{0,1}r/a)$ 在 $r=a$ 处的斜率是 $-j_{0,1}J_1(j_{0,1})/a\neq0$，而每个 $\sin(n\pi r/a)$ 在 $r=a$ 处斜率是 $(-1)^n n\pi/a$——**边界附近要用无穷多项去模仿一个有限的斜率**，收敛必然慢，还伴随 Gibbs 型振荡。

**3.41** **错。** $m\geq1$ 的模式在中心为零：$J_m(0)=0$（小宗量 $J_m\sim(x/2)^m/m!$）。

**例子：** $(1,1)$ 模有一条节线穿过中心（图样是两个半圆），中心恒为零；$(2,1)$ 模有两条节线交于中心，中心同样为零。**只有 $m=0$ 的模式在中心取极值。**

**3.42** **错。** 环形区域不含 $r=0$，径向通解必须保留 $Y_0$，两个边界给出特征方程

$$J_0(kb)Y_0(ka)-J_0(ka)Y_0(kb)=0 .$$

$b=0.5a$ 时最低根 $ka=6.246$，是实心膜 $j_{0,1}=2.405$ 的 $2.60$ 倍。**直接用 $j_{0,1}$ 会把基频算低一半以上。**

**例子：** 只有 $b\to0$ 的极限才退回 $J_0(ka)=0$；只要孔存在，零点就整体右移，孔越大右移越多。

**3.43** **错（对 $m=0$ 而言）。** 由 $\frac{\mathrm{d}J_0}{\mathrm{d}x}=-J_1$，$J_0'$ 的零点就是 $J_1$ 的零点：

$$j'_{0,n}=j_{1,n}=3.8317,\ 7.0156,\ 10.1735,\dots$$

是同一张表，只是换了名字。

**例子：** 圆波导 TE$_{01}$ 模的截止频率用 $j'_{0,1}=3.8317$，查 $J_1$ 的零点表即可。但 $m\geq1$ 的 $j'_{m,n}$ **不能**这样换（只有 $j'_{0,n}=j_{1,n}$ 这类特殊关系），必须单独查——把「$m=0$ 的特例」当成通则是这张表上最常见的错误。

## 第 4 章

**4.1** 思路：$P_l$ 的封闭形式只有罗德里格斯公式，直接求 $l=4$ 次导数最省事。

过程：$P_4=\dfrac{1}{2^44!}\dfrac{\mathrm{d}^4}{\mathrm{d}x^4}(x^2-1)^4$。先展开被求导的多项式：

$$(x^2-1)^4=x^8-4x^6+6x^4-4x^2+1 .$$

逐项求四阶导数（$x^n$ 的四阶导是 $n(n-1)(n-2)(n-3)x^{n-4}$）：

$$x^8\to1680x^4,\qquad x^6\to360x^2,\qquad x^4\to24,\qquad x^2\to0,\qquad 1\to0 .$$

于是 $\dfrac{\mathrm{d}^4}{\mathrm{d}x^4}(x^2-1)^4=1680x^4-1440x^2+144$（第二项的系数：$-4\times360=-1440$）。除以 $2^44!=16\times24=384$：

$$P_4=\frac{1680x^4-1440x^2+144}{384}=\frac{35x^4-30x^2+3}{8}.$$

**结果：** $P_4(x)=\dfrac{35x^4-30x^2+3}{8}$；$P_4(1)=\dfrac{35-30+3}{8}=1$，$P_4(-1)=\dfrac{35-30+3}{8}=1$。

**检验：** 两端值相等，符合"$l$ 为偶数时 $P_l$ 是偶函数"；$P_4$ 的次数是 4、首项系数 $35/8$，与递推公式由 $P_2,P_3$ 算出的结果一致。

**读法：** $P_4$ 在 $(-1,1)$ 内有 4 个零点，对应球面上 4 条节锥——节面数就是 $l$。

**4.2** 思路：两个积分一个靠正交性直接得零，一个要把 $x^2$ 用 $P_0,P_2$ 表出再投影。

过程：第一问，$l=2\ne4$，由 $\int_{-1}^1P_lP_{l'}\,\mathrm{d}x=\dfrac{2}{2l+1}\delta_{ll'}$ 立刻得

$$\int_{-1}^{1}P_2P_4\,\mathrm{d}x=0 .$$

第二问，把权函数 $x^2$ 换成勒让德多项式。由 $P_2=\dfrac{3x^2-1}{2}$ 反解 $x^2=\dfrac{1+2P_2}{3}=\dfrac13P_0+\dfrac23P_2$，于是

$$\int_{-1}^{1}x^2P_2\,\mathrm{d}x=\frac13\int_{-1}^1P_0P_2\,\mathrm{d}x+\frac23\int_{-1}^1P_2^2\,\mathrm{d}x
=0+\frac23\cdot\frac25=\frac{4}{15}.$$

**结果：** $\displaystyle\int_{-1}^{1}P_2P_4\,\mathrm{d}x=0$；$\displaystyle\int_{-1}^{1}x^2P_2\,\mathrm{d}x=\dfrac{4}{15}$。

**检验：** 数值核对：$P_2$ 在 $[-1,1]$ 上平均为零，$x^2P_2$ 的被积函数在 $|x|<1/\sqrt3$ 处为负、其余为正，积分 $4/15\approx0.267$ 为正且小于 $\int x^2=\frac23$，合理。

**读法：** 正交性让"乘 $P_{l'}$ 再积分"变成筛子：除了同阶那一项，其余全归零。这是所有展开系数的来源。

**4.3** 思路：$|x|$ 是偶函数，只有偶 $l$ 的系数非零；每个系数都是一次 $[0,1]$ 上的多项式积分。

过程：$c_l=\dfrac{2l+1}{2}\displaystyle\int_{-1}^{1}|x|P_l(x)\,\mathrm{d}x=(2l+1)\int_0^1xP_l(x)\,\mathrm{d}x$（用了 $|x|P_l$ 在偶 $l$ 时为偶函数）。

$$c_0=1\cdot\int_0^1x\,\mathrm{d}x=\frac12 .$$

$$c_2=5\int_0^1x\cdot\frac{3x^2-1}{2}\,\mathrm{d}x=5\left(\frac{3}{8}-\frac14\right)=\frac58 .$$

$$c_4=9\int_0^1x\cdot\frac{35x^4-30x^2+3}{8}\,\mathrm{d}x
=9\left(\frac{35}{48}-\frac{15}{16}+\frac{3}{16}\right)=-\frac{3}{16}.$$

**结果：** $|x|=\dfrac12+\dfrac58P_2(x)-\dfrac{3}{16}P_4(x)+\cdots$，$c_6=\dfrac{13}{128}$ 起继续交替。

**检验：** 取 $x=1$：右边 $=\frac12+\frac58-\frac{3}{16}+\cdots$ 应当趋于 1；前三项给 $0.9375$，加上后续项收敛到 1 ✓（端点处收敛慢，属吉布斯型）。

**读法：** 系数按 $l^{-2}$ 衰减：$|x|$ 连续但在原点有折角，正好对应"一阶导跳变 → $1/n^2$"这条规律。

**4.4** 思路：$\cos^2\theta$ 是二次多项式，用 $P_0,P_2$ 表示即可，$l>2$ 的矩必为零。

过程：由 $P_2(\cos\theta)=\dfrac{3\cos^2\theta-1}{2}$ 反解：

$$3\cos^2\theta=2P_2+1\quad\Longrightarrow\quad\cos^2\theta=\frac13P_0+\frac23P_2 .$$

与 $f=\sum c_lP_l$ 逐项比对得 $c_0=\dfrac13$、$c_2=\dfrac23$，其余为零。

**结果：** $\cos^2\theta=\dfrac13P_0(\cos\theta)+\dfrac23P_2(\cos\theta)$。

**检验：** 在 $\theta=0$ 处：左边 1，右边 $\frac13+\frac23=1$ ✓；在 $\theta=\pi/2$ 处：左边 0，右边 $\frac13-\frac13=0$ ✓。

**读法：** "多项式函数的展开必截断"——这是判断系数个数时最快的办法：先看 $f$ 是几次多项式。

**4.5** 思路：$P_3$ 是三次多项式，直接因式分解求根，再由 $\theta=\arccos x$ 换成极角。

过程：$P_3=\dfrac{5x^3-3x}{2}=\dfrac{x}{2}\left(5x^2-3\right)$，零点为

$$x=0,\qquad x=\pm\sqrt{\frac35}=\pm0.7746 .$$

换成极角（$\theta=\arccos x$）：$x=0$ 给 $\theta=90^\circ$；$x=0.7746$ 给 $\theta=39.2^\circ$；$x=-0.7746$ 给 $\theta=180^\circ-39.2^\circ=140.8^\circ$。

**结果：** 三条节锥 $\theta=39.2^\circ,\ 90^\circ,\ 140.8^\circ$；它们把球面分成四条纬度带。

**检验：** 三个零点都在 $(-1,1)$ 内 ✓（$P_3$ 的零点数等于次数）。带内 $P_3$ 的符号交替：$\theta<39.2^\circ$ 为正、$39.2^\circ<\theta<90^\circ$ 为负，可代 $\theta=0$、$60^\circ$ 验证。

**读法：** 节锥是整圈纬线而不是点；$l=3$ 的角分布有三圈节线，比 $p$ 轨道（一条节面）复杂得多。

**4.6** 思路：实球谐由 $m$ 与 $-m$ 的复球谐组合而成，组合后再用直角坐标改写；正交性只需检查方位角。

过程：由 4.7.2 的复球谐 $Y_{20}=\sqrt{\dfrac{5}{16\pi}}\left(3\cos^2\theta-1\right)$、$Y_{2,\pm2}=\sqrt{\dfrac{15}{32\pi}}\sin^2\theta\,e^{\pm2i\varphi}$、$Y_{2,\pm1}=\mp\sqrt{\dfrac{15}{8\pi}}\sin\theta\cos\theta\,e^{\pm i\varphi}$。

$m=0$ 直接取实数：$\sqrt{\dfrac{5}{16\pi}}\left(3\cos^2\theta-1\right)$。

$m=\pm2$ 组合：

$$\frac{Y_{22}+Y_{2,-2}}{\sqrt2}=\sqrt{\frac{15}{16\pi}}\sin^2\theta\cos2\varphi
=\sqrt{\frac{15}{16\pi}}\frac{x^2-y^2}{r^2},$$

$$\frac{Y_{22}-Y_{2,-2}}{i\sqrt2}=\sqrt{\frac{15}{16\pi}}\sin^2\theta\sin2\varphi
=\sqrt{\frac{15}{16\pi}}\cdot\frac{2xy}{r^2}=\sqrt{\frac{15}{4\pi}}\frac{xy}{r^2},$$

其中用了 $\sin^2\theta\cos2\varphi=(x^2-y^2)/r^2$、$\sin^2\theta\sin2\varphi=2xy/r^2$。$m=\pm1$ 同理给 $\sqrt{\dfrac{15}{4\pi}}\dfrac{xz}{r^2}$ 与 $\sqrt{\dfrac{15}{4\pi}}\dfrac{yz}{r^2}$。

**结果：** 五个实球谐为 $\sqrt{\frac{5}{16\pi}}\frac{3z^2-r^2}{r^2}$、$\sqrt{\frac{15}{4\pi}}\frac{xz}{r^2}$、$\sqrt{\frac{15}{4\pi}}\frac{yz}{r^2}$、$\sqrt{\frac{15}{16\pi}}\frac{x^2-y^2}{r^2}$、$\sqrt{\frac{15}{4\pi}}\frac{xy}{r^2}$。

**检验：** 以 $d_{z^2}$ 与 $d_{x^2-y^2}$ 为例，$\varphi$ 积分给出 $\int_0^{2\pi}\cos2\varphi\,\mathrm{d}\varphi=0$，故两者正交 ✓；每个函数的平方在球面上积分都是 1（归一化系数就是这么定的）。

**读法：** 实球谐与化学里的 $d$ 轨道一一对应；正交性保证任意角向函数都能按它们唯一展开。

**4.7** 思路：从 $P_1^0=\cos\theta$ 出发，只差一个归一化常数，用 $\int|Y|^2\mathrm{d}\Omega=1$ 定它。

过程：设 $Y=N\cos\theta$（$m=0$ 时 $e^{im\varphi}=1$），则

$$1=N^2\int_0^{2\pi}\mathrm{d}\varphi\int_0^{\pi}\cos^2\theta\sin\theta\,\mathrm{d}\theta
=N^2\cdot2\pi\int_{-1}^{1}u^2\,\mathrm{d}u=N^2\cdot2\pi\cdot\frac23 .$$

于是 $N^2=\dfrac{3}{4\pi}$，$N=\sqrt{\dfrac{3}{4\pi}}$。

**结果：** $Y_{10}=\sqrt{\dfrac{3}{4\pi}}\cos\theta$。

**检验：** 在球面上对 $|Y_{10}|^2$ 积分得 1 ✓；代 $\theta=0$ 得 $Y_{10}=\sqrt{3/4\pi}\approx0.489$，与"球谐在极点最大"一致。

**读法：** 归一化常数只来自积分；相位（$e^{im\varphi}$ 前的 $(-1)^m$）由约定定，不影响任何物理量。

**4.8** 思路：$1/r^2$ 的径向函数配 $l=1$ 的角函数正是拉普拉斯方程的通解，也可以直接算两项相消。

过程：记 $f(r)=\dfrac{p}{4\pi\varepsilon_0r^2}$，$\Phi=f(r)\cos\theta$。球坐标下

$$\nabla^2\Phi=\cos\theta\cdot\frac{1}{r^2}\frac{\mathrm{d}}{\mathrm{d}r}\left(r^2\frac{\mathrm{d}f}{\mathrm{d}r}\right)+\frac{f}{r^2}\nabla^2_{\Omega}\cos\theta .$$

先算径向项：$\dfrac{\mathrm{d}f}{\mathrm{d}r}=-\dfrac{2p}{4\pi\varepsilon_0r^3}$，$r^2f'=-\dfrac{2p}{4\pi\varepsilon_0r}$，再求导得 $\dfrac{2p}{4\pi\varepsilon_0r^2}$，除以 $r^2$ 得 $\dfrac{2p}{4\pi\varepsilon_0r^4}$。

再算角向项：$\cos\theta$ 是 $l=1$ 的本征函数，$\nabla^2_{\Omega}\cos\theta=-2\cos\theta$，故这一项是 $-\dfrac{2f\cos\theta}{r^2}=-\dfrac{2p\cos\theta}{4\pi\varepsilon_0r^4}$。

两项相加为零。

**结果：** $\nabla^2\Phi=0$（$r\ne0$）；原点处 $\nabla^2\Phi=-\dfrac{p}{3\varepsilon_0}\nabla^2\dfrac1r$ 型的 $\delta$，不属于"球外"。

**检验：** 直接看量纲：$\Phi$ 正比于 $r^{-2}P_1(\cos\theta)$，正是 $l=1$ 的 $r^{-(l+1)}$ 项，按 4.3 的通解必然调和 ✓。

**读法：** 偶极场是 $l=1$ 的"纯"多极项，处处调和（除原点）；这正是多极展开能把每一项单独处理的原因。

**4.9** 思路：球贝塞尔函数在 $x\to0$ 的行为由闭式展开直接读出，不用查表。

过程：$j_0(x)=\dfrac{\sin x}{x}$，用 $\sin x=x-\dfrac{x^3}{6}+\dfrac{x^5}{120}-\cdots$：

$$j_0(x)=1-\frac{x^2}{6}+\frac{x^4}{120}-\cdots$$

$j_1(x)=\dfrac{\sin x}{x^2}-\dfrac{\cos x}{x}$，用 $\cos x=1-\dfrac{x^2}{2}+\dfrac{x^4}{24}-\cdots$：

$$j_1=\left(\frac{1}{x}-\frac{x}{6}+\cdots\right)-\left(\frac{1}{x}-\frac{x}{2}+\cdots\right)=\frac{x}{3}-\frac{x^3}{30}+\cdots$$

**结果：** $j_0=1-\dfrac{x^2}{6}+\cdots$，$j_1=\dfrac{x}{3}-\dfrac{x^3}{30}+\cdots$；一般地 $j_l\approx\dfrac{x^l}{(2l+1)!!}$。

**检验：** $l=0$ 时 $(2l+1)!!=1$，$j_0(0)=1$ ✓；$l=1$ 时 $3!!=3$，首项 $x/3$ ✓。

**读法：** $j_l$ 在原点按 $x^l$ 压低，这就是低能散射只有 $s$ 波的原因（$l$ 越大越进不了核区）。

**4.10** 思路：球面电势只含 $P_1$，所以内外解各只有一项；系数由 $r=a$ 的连续性定。

过程：$V(\theta)=V_0\cos\theta=V_0P_1(\cos\theta)$。球内含原点，只能留 $r^1$；球外要衰减，只能留 $r^{-2}$：

$$\Phi_{\mathrm{in}}=A\,r\cos\theta,\qquad \Phi_{\mathrm{out}}=\frac{B}{r^2}\cos\theta .$$

$r=a$ 处连续：$Aa=V_0$ 给 $A=V_0/a$；$B/a^2=V_0$ 给 $B=V_0a^2$。

**结果：** $\Phi_{\mathrm{in}}=V_0\dfrac{r}{a}\cos\theta$，$\Phi_{\mathrm{out}}=V_0\left(\dfrac{a}{r}\right)^2\cos\theta$。

**检验：** $r=a$ 时两者都等于 $V_0\cos\theta$ ✓；$r\to0$ 时内部解有界 ✓；$r\to\infty$ 时外部解按 $1/r^2$ 衰减 ✓（衰减的是偶极场，因为没有净电荷）。

**读法：** 这个球壳等价于一个偶极层：上半正、下半负，净电荷为零，所以外部只剩偶极项。

**4.11** 思路：把 $m=0,\pm1$ 三个球谐的模方写出来求和，与 $P_1(1)=1$ 对照。

过程：$|Y_{10}|^2=\dfrac{3}{4\pi}\cos^2\theta$；$Y_{1,\pm1}=\mp\sqrt{\dfrac{3}{8\pi}}\sin\theta e^{\pm i\varphi}$，故 $|Y_{1,\pm1}|^2=\dfrac{3}{8\pi}\sin^2\theta$ 各一个。三者相加：

$$\frac{3}{4\pi}\cos^2\theta+2\cdot\frac{3}{8\pi}\sin^2\theta
=\frac{3}{4\pi}\left(\cos^2\theta+\sin^2\theta\right)=\frac{3}{4\pi}.$$

**结果：** $\sum_m|Y_{1m}|^2=\dfrac{3}{4\pi}=\dfrac{2\cdot1+1}{4\pi}$，与加法公式在 $\gamma=0$ 处的值一致。

**检验：** 加法公式给出 $\sum_m|Y_{lm}|^2=\dfrac{2l+1}{4\pi}$，对 $l=1$ 正好 $3/4\pi$ ✓。这个和与 $\theta,\varphi$ 无关，说明"所有 $m$ 加起来各向同性"。

**读法：** 三个 $p$ 轨道（$p_x,p_y,p_z$）的电子云叠加起来是球对称的——满壳层没有方向性。

**4.12** 思路：把 $\cos^2\theta|Y_{20}|^2$ 化成 $u=\cos\theta$ 的多项式积分。

过程：$|Y_{20}|^2=\dfrac{5}{16\pi}\left(3\cos^2\theta-1\right)^2$，于是

$$\langle\cos^2\theta\rangle=\frac{5}{16\pi}\int\cos^2\theta\left(3\cos^2\theta-1\right)^2\mathrm{d}\Omega
=\frac{5}{16\pi}\cdot2\pi\int_{-1}^{1}u^2\left(3u^2-1\right)^2\mathrm{d}u .$$

展开被积函数：$u^2\left(9u^4-6u^2+1\right)=9u^6-6u^4+u^2$，逐项积分

$$9\cdot\frac{2}{7}-6\cdot\frac{2}{5}+\frac{2}{3}=\frac{18}{7}-\frac{12}{5}+\frac{2}{3}=\frac{270-252+70}{105}=\frac{88}{105}.$$

乘以 $\dfrac{5}{8}$（$2\pi\times5/16\pi$）：$\langle\cos^2\theta\rangle=\dfrac{5}{8}\cdot\dfrac{88}{105}=\dfrac{11}{21}$。

**结果：** $\langle\cos^2\theta\rangle=\dfrac{11}{21}\approx0.524$。

**检验：** 一般公式 $\langle\cos^2\theta\rangle=\dfrac{2l^2+2l-1}{(2l-1)(2l+3)}$ 在 $l=2$ 给 $\dfrac{11}{3\cdot7}=\dfrac{11}{21}$ ✓；$l=0$ 时给 $\dfrac13$（各向同性）✓。

**读法：** $l=2,m=0$ 的电子云沿 $z$ 稍微拉长（$\langle\cos^2\theta\rangle>1/3$），这就是 $d_{z^2}$ 的"轴向偏好"。

**4.13** 思路：由 $J_2$ 项的引力势求径向场，比较 $P_2$ 在两极与赤道的取值。

过程：$\Phi_g=-\dfrac{GM}{r}\left[1-J_2\left(\dfrac{a}{r}\right)^2P_2(\cos\theta)\right]$，径向加速度

$$g=-\frac{\partial\Phi_g}{\partial r}=-\frac{GM}{r^2}+\frac{3GMJ_2a^2}{r^4}P_2
=-\frac{GM}{r^2}\left[1-3J_2\left(\frac{a}{r}\right)^2P_2\right] .$$

在 $r=a$：极地 $P_2=1$，$|g|=\dfrac{GM}{a^2}\left(1-3J_2\right)$；赤道 $P_2=-\dfrac12$，$|g|=\dfrac{GM}{a^2}\left(1+\dfrac32J_2\right)$。相对差

$$\frac{\Delta g}{g}=3J_2+\frac32J_2=4.5J_2=4.5\times1.0826\times10^{-3}=4.87\times10^{-3} .$$

**结果：** $\Delta g/g=4.9\times10^{-3}$；$GM/a^2=9.80\ \mathrm{m/s^2}$ 给 $\Delta g=0.048\ \mathrm{m/s^2}$（极地更大）。

**检验：** 实测差 $9.832-9.780=0.052\ \mathrm{m/s^2}$，同量级 ✓，剩下的来自自转与扁率（同一 $r$ 与真实地表的比较差）。

**读法：** 赤道鼓、两极扁，所以极地"质量在脚下"更多，重力更大；$J_2>0$ 就是这个"扁"的定量。

**4.14** 思路：同一套公式，把 $r$ 换成 7000 km，看 $(a/r)^2$ 与 $P_2$ 的组合。

过程：$(a/r)^2=(6378/7000)^2=0.830$。$J_2$ 项对 $g$ 的相对贡献是 $3J_2(a/r)^2P_2$：

$$3\times1.0826\times10^{-3}\times0.830=2.70\times10^{-3}\quad(P_2=1,\ \text{极地}),$$

$$1.35\times10^{-3}\quad\left(P_2=-\frac12,\ \text{赤道}\right).$$

**结果：** 极地 $+0.27\%$、赤道 $-0.13\%$；在 $r=7000\ \mathrm{km}$ 处 $J_2$ 项已是 $10^{-3}$ 量级。

**检验：** 与 4.13 比较：$r$ 从 $a$ 升到 $7000\ \mathrm{km}$，修正按 $(a/r)^2$ 缩小，$4.87\times10^{-3}\times0.830=4.0\times10^{-3}$ 是同一条曲线的端点值 ✓。

**读法：** 精确定轨必须算 $J_2$；粗略估算把它当球，误差在千分之一量级。

**4.15** 思路：偶极场的轴向表达式直接代入，注意 $1\ \mathrm{D}=3.336\times10^{-30}\ \mathrm{C\cdot m}$。

过程：$p=1.85\ \mathrm{D}=6.17\times10^{-30}\ \mathrm{C\cdot m}$，$r=10^{-9}\ \mathrm{m}$。

轴向电场 $E=\dfrac{2p}{4\pi\varepsilon_0r^3}$：

$$E=\frac{2\times8.99\times10^9\times6.17\times10^{-30}}{\left(10^{-9}\right)^3}
=1.11\times10^{8}\ \mathrm{V/m}.$$

电势 $\varphi=\dfrac{p}{4\pi\varepsilon_0r^2}$：

$$\varphi=\frac{8.99\times10^9\times6.17\times10^{-30}}{\left(10^{-9}\right)^2}=5.55\times10^{-2}\ \mathrm{V}.$$

**结果：** $E=1.1\times10^{8}\ \mathrm{V/m}$，$\varphi=56\ \mathrm{mV}$（轴向，$\theta=0$）。

**检验：** 量纲：$p/(\varepsilon_0r^3)$ 给 $\mathrm{C\cdot m/(F/m\cdot m^3)}=\mathrm{V/m}$ ✓。$r=1\ \mathrm{nm}$ 是分子尺寸的 10 倍，点偶极近似勉强成立。

**读法：** $10^8\ \mathrm{V/m}$ 超过空气击穿场强（$3\times10^6\ \mathrm{V/m}$），所以极性分子在纳米尺度上是强力扰动源——这也是水能溶解离子的原因之一。

**4.16** 思路：介质球的极化由边界条件（电势连续 + 法向 $D$ 连续）定，解出球内场。

过程：设 $\Phi_{\mathrm{in}}=-Ar\cos\theta$、$\Phi_{\mathrm{out}}=-E_0r\cos\theta+\dfrac{B}{r^2}\cos\theta$。$r=a$ 处两个条件：

$$-Aa=-E_0a+\frac{B}{a^2}\quad(\text{电势连续}),\qquad
\varepsilon_rA=E_0+\frac{2B}{a^3}\quad\left(\varepsilon_rE_{\mathrm{in}}=E_{\mathrm{out}}\right).$$

第一式给 $A=E_0-\dfrac{B}{a^3}$，代入第二式：

$$\varepsilon_r\left(E_0-\frac{B}{a^3}\right)=E_0+\frac{2B}{a^3}
\quad\Longrightarrow\quad
B=\frac{\varepsilon_r-1}{\varepsilon_r+2}a^3E_0,\qquad A=\frac{3}{\varepsilon_r+2}E_0 .$$

**结果：** $E_{\mathrm{in}}=\dfrac{3}{\varepsilon_r+2}E_0$；$\varepsilon_r=80$ 时 $E_{\mathrm{in}}=\dfrac{3}{82}E_0=0.0366E_0$。

**检验：** $\varepsilon_r\to\infty$ 给 $E_{\mathrm{in}}\to0$（导体屏蔽）✓；$\varepsilon_r\to1$ 给 $E_{\mathrm{in}}=E_0$、$B=0$（没有球）✓。

**读法：** 球内场被压到 3.7%，等价于库仑相互作用除以 80——这是水的高介电常数对电解质的作用。

**4.17** 思路：球面电势只在 $[0,\pi]$ 上分段，按 $P_l$ 投影求系数；球心的值由平均值定理直接得。

过程：$V(\theta)=V_0$（$\theta<\pi/2$）、$0$（$\theta>\pi/2$）。系数

$$c_l=\frac{2l+1}{2}\int_0^{\pi}V(\theta)P_l(\cos\theta)\sin\theta\,\mathrm{d}\theta
=\frac{2l+1}{2}V_0\int_0^1P_l(x)\,\mathrm{d}x .$$

逐项算积分：$\int_0^1P_0=1$、$\int_0^1P_1=\dfrac12$、$\int_0^1P_2=0$、$\int_0^1P_3=-\dfrac18$，于是

$$c_0=\frac{V_0}{2},\qquad c_1=\frac{3V_0}{4},\qquad c_2=0,\qquad c_3=-\frac{7V_0}{16}.$$

**结果：** 球心 $\Phi(0)=c_0=\dfrac{V_0}{2}$（等于球面平均）；北极点（$r=a,\theta=0$）在边界上，值为 $V_0$，但级数在该点收敛很慢（$c_l\sim l^{-1/2}$，误差按 $N^{-1/2}$ 降）。

**检验：** 球心值 = 上半球 $V_0$、下半球 0 的面积平均 = $V_0/2$ ✓。极点是边界点，级数不该在那里求值——这和吉布斯现象是同一件事。

**读法：** 这类问题的解在球内光滑、在边界附近收敛慢；要极点附近的电势就直接用边界值。

**4.18** 思路：$1s$ 的径向函数已知，三个期望值都是 $r^n e^{-2r/a_0}$ 型的积分，用 $\int_0^\infty r^ne^{-\alpha r}\mathrm{d}r=n!/\alpha^{n+1}$。

过程：$R_{10}=2a_0^{-3/2}e^{-r/a_0}$。归一化检验：

$$\int_0^\infty R_{10}^2r^2\,\mathrm{d}r=4a_0^{-3}\int_0^\infty r^2e^{-2r/a_0}\mathrm{d}r
=4a_0^{-3}\cdot\frac{2!}{\left(2/a_0\right)^3}=4\cdot\frac{2}{8}=1 .$$

$$\langle r\rangle=4a_0^{-3}\int_0^\infty r^3e^{-2r/a_0}\mathrm{d}r
=4a_0^{-3}\cdot\frac{3!}{\left(2/a_0\right)^4}=\frac{4\times6}{16}a_0=\frac32a_0 .$$

$$\langle r^2\rangle=4a_0^{-3}\cdot\frac{4!}{\left(2/a_0\right)^5}=\frac{4\times24}{32}a_0^2=3a_0^2 .$$

最概然半径：由 $\dfrac{\mathrm{d}}{\mathrm{d}r}\left(r^2e^{-2r/a_0}\right)=0$ 得 $2r-\dfrac{2r^2}{a_0}=0$，即 $r_{\mathrm{mp}}=a_0$。

**结果：** $\langle r\rangle=1.5a_0=0.79\ \text{Å}$，$\langle r^2\rangle=3a_0^2$，$r_{\mathrm{mp}}=a_0$，$\Delta r=\sqrt{3-2.25}\,a_0=0.87a_0$。

**检验：** 量纲：三个量都是长度（或长度平方）✓；$\Delta r$ 与 $\langle r\rangle$ 同量级，说明分布很宽，"轨道半径"只有统计意义。

**读法：** 最概然半径正好是玻尔半径，但平均半径是 $1.5a_0$——分布有长尾，说"电子云"比说"轨道"准确。

**4.19** 思路：$2p$ 的径向概率 $\propto r^4e^{-r/a_0}$，求极值即可。

过程：$R_{21}\propto r e^{-r/(2a_0)}$，故径向概率密度

$$P(r)=r^2|R_{21}|^2\propto r^4e^{-r/a_0} .$$

$$\frac{\mathrm{d}P}{\mathrm{d}r}\propto\left(4r^3-\frac{r^4}{a_0}\right)e^{-r/a_0}=0
\quad\Longrightarrow\quad r=4a_0 .$$

**结果：** $2p$ 的最概然半径 $r_{\mathrm{mp}}=4a_0=2.1\ \text{Å}$（$1s$ 是 $a_0$）。

**检验：** 与 $n^2$ 标度一致：主量子数从 1 到 2，尺度乘 4 ✓；$\langle r\rangle_{2p}=5a_0$（由 $\frac{a_0}{2}[3n^2-l(l+1)]$ 得 $\frac{a_0}{2}(12-2)=5a_0$），比最概然半径大，分布也有长尾。

**读法：** $2p$ 电子云比 $1s$ 大 4 倍；$p$ 态在原点为零（离心势），所以没有"核附近"的概率。

**4.20** 思路：把氢的能级公式当成"有效主量子数"的定义，反推量子亏损。

过程：钠的价电子近似处在屏蔽后的中心势里，能级写成

$$E_{3s}=-\frac{13.6\ \mathrm{eV}}{\left(n-\delta_0\right)^2}=-5.14\ \mathrm{eV}
\quad\Longrightarrow\quad n-\delta_0=\sqrt{\frac{13.6}{5.14}}=1.63 .$$

于是 $\delta_0=3-1.63=1.37$。

**结果：** $n^*=1.63$，量子亏损 $\delta_0=1.37$（对 $3s$）。

**检验：** 同章数据：$3p$ 的 $\delta_1\approx0.88$、$3d$ 的 $\delta_2\approx0.01$——$\delta_l$ 随 $l$ 迅速减小，符合"$l$ 大穿透浅"的图像 ✓。

**读法：** 亏损 1.37 说明 $3s$ 电子有相当概率穿进内层，感受到接近裸核的电荷；$l$ 越大越"规规矩矩"。

**4.21** 思路：由能量求波数，再和核半径相乘得 $kR$，分波截断 $l\lesssim kR$。

过程：$k=\dfrac{\sqrt{2mE}}{\hbar}$，用 $\hbar c=197.3\ \mathrm{MeV\cdot fm}$、$mc^2=939.6\ \mathrm{MeV}$：

$$k=\frac{\sqrt{2\times939.6\times1}}{197.3}=\frac{43.35}{197.3}=0.220\ \mathrm{fm^{-1}} .$$

$$kR=0.220\times3=0.66 .$$

**结果：** $k=0.22\ \mathrm{fm^{-1}}$，$kR=0.66$；需要的分波 $l\le1$（$l_{\max}\approx0.7$）。

**检验：** 量纲：$kR$ 无量纲 ✓。$l=2$ 的振幅被 $(kR)^2\approx0.44$ 压低，$l=3$ 压到 $(kR)^3\approx0.29$ 再乘 $j_l$ 的小系数，可忽略。

**读法：** 1 MeV 以下中子-核散射接近各向同性（s 波为主），这正是低能中子实验好解释的原因。

**4.22** 思路：瑞利散射截面 $\propto k^4\propto\lambda^{-4}$，直接取比值。

过程：$\sigma\propto\omega^4\propto\lambda^{-4}$，故

$$\frac{\sigma_{450}}{\sigma_{700}}=\left(\frac{700}{450}\right)^4=\left(1.556\right)^4=5.86 .$$

**结果：** 蓝光（450 nm）被散射的强度约为红光（700 nm）的 **5.9 倍**。

**检验：** $\lambda$ 比 1.556，四次方 $5.86$ ✓；量纲：比值无量纲 ✓。这也解释了日落时太阳偏红（长路径把蓝光散射掉了）。

**读法：** $\omega^4$ 律来自 $l=1$（电偶极）分波：原子尺度远小于波长，只有偶极项能响应，偶极辐射的功率正比于 $\omega^4$。

**4.23** 思路：两项都按 $(a/r)^n$ 衰减，取比值即可。

过程：$J_2$ 项相对单极是 $J_2\left(\dfrac{a}{r}\right)^2$；$J_4$ 项是 $J_4\left(\dfrac{a}{r}\right)^4$。在 $r=2a$：

$$\frac{\text{$J_4$ 项}}{\text{$J_2$ 项}}=\frac{J_4}{J_2}\left(\frac{a}{r}\right)^2
=\frac{1.62\times10^{-6}}{1.0826\times10^{-3}}\cdot\frac14=3.7\times10^{-4} .$$

**结果：** $J_4$ 项比 $J_2$ 项小 $3.7\times10^{-4}$（即 $J_4$ 项本身约为单极的 $1.0\times10^{-7}$）。

**检验：** 量级链：$J_2\sim10^{-3}$、$J_4\sim10^{-6}$、$(a/r)^2=1/4$，乘起来 $10^{-7}$ 与单极比 ✓。$r$ 越大高阶项掉得越快。

**读法：** 远场只需要最低几阶；卫星轨道分析里 $J_2$ 必算、$J_4$ 是精化项、$J_6$ 以后只对高精度定轨有意义。

**4.24** 思路：两个反号电荷的展开只有奇 $l$ 项，逐项比较 $l=1$ 与 $l=3$。

过程：$\Phi=\dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{1}{|\boldsymbol r-a\hat z|}-\dfrac{1}{|\boldsymbol r+a\hat z|}\right]$（$a=d/2$）。用 $1/|\boldsymbol r\mp a\hat z|=\dfrac1r\sum_l\left(\dfrac{a}{r}\right)^lP_l(\cos\theta)$：

$$\Phi=\frac{q}{4\pi\varepsilon_0r}\sum_{l\ \text{奇}}2\left(\frac{a}{r}\right)^lP_l(\cos\theta) .$$

$l=1$ 项：$\dfrac{2qa}{r^2}\cos\theta=\dfrac{qd\cos\theta}{4\pi\varepsilon_0r^2}$，正是偶极场。$l=3$ 项：$\dfrac{2qa^3}{r^4}P_3$。在 $\theta=0$ 处两者之比

$$\frac{\Phi_3}{\Phi_1}=\left(\frac{a}{r}\right)^2\frac{P_3(1)}{P_1(1)}=\frac{1}{100}\cdot1=10^{-2},\qquad a=\frac d2,\ r=5d .$$

**结果：** $\Phi_3/\Phi_1=1\%$；偶极近似在 $r=5d$ 处误差约 $1\%$。

**检验：** 若用 $d$ 表示：$a/r=d/(2r)=1/10$，$(a/r)^2=1/100$ ✓。$l=2$ 项为零（对称），所以第一个修正是 $l=3$（八极），不是四极。

**读法：** 偶极近似的好坏由 $(d/r)^2$ 控制；要 1% 精度就得 $r\gtrsim5d$，这就是"远场"的定量含义。

**4.25** 思路：去掉 $\theta=\pi$ 的有界要求，就是允许解在 $x=-1$ 处发散；看发散的类型和物理后果。

过程：极角方程在 $x=\pm1$ 是正则奇点，指标方程为 $s(s-1)=0$ 型的重根，两个解一个是多项式、一个含对数。$l$ 非整数时级数不截断，解在端点附近

$$y\sim\frac12P_l(x)\ln\frac{1+x}{1-x}\qquad(x\to-1).$$

于是 $\dfrac{\mathrm{d}y}{\mathrm{d}x}\sim\dfrac{1}{1+x}$，动能密度 $\propto\left|\nabla\psi\right|^2$ 在极点附近

$$\int\left|\frac{\partial\psi}{\partial\theta}\right|^2\sin\theta\,\mathrm{d}\theta
\sim\int\frac{\mathrm{d}x}{1-x}\to\infty .$$

**结果：** 解在 $\theta\to\pi$ 处对数发散，**动能积分发散**；虽然 $|\psi|^2$ 的积分收敛（对数平方可积），但这个态不在哈密顿量的定义域里。

**检验：** 能量有限的判据是 $\int|\nabla\psi|^2<infty$，不是 $\int|\psi|^2<infty$——这一点用 $l$ 非整数的解一验就清楚。$l$ 为整数时分子截断，两个积分都收敛 ✓。

**读法：** "两极有界"的真正理由是能量有限；物理上它排除了电子被无限深地"吸"到极轴上的病态解。

**4.26** 思路：球外区域不含原点，用 $r^{-(l+1)}$ 的展开；边界条件逐项定系数，认出结果是镜像电荷。

过程：点电荷 $q$ 在 $z=b$。对 $r<b$ 展开源项：$\dfrac{1}{|\boldsymbol r-b\hat z|}=\sum_l\dfrac{r^l}{b^{l+1}}P_l(\cos\theta)$（$\theta$ 从 $z$ 轴量）。球外（$r>a$）总电势设为源项加感应项

$$\Phi=\frac{q}{4\pi\varepsilon_0}\sum_l\frac{r^l}{b^{l+1}}P_l+\sum_l\frac{C_l}{r^{l+1}}P_l .$$

$r=a$ 处为零：$\dfrac{q}{4\pi\varepsilon_0}\dfrac{a^l}{b^{l+1}}+C_la^{-(l+1)}=0$，即 $C_l=-\dfrac{q}{4\pi\varepsilon_0}\dfrac{a^{2l+1}}{b^{l+1}}$。于是

$$\Phi=\frac{q}{4\pi\varepsilon_0}\left[\frac{1}{|\boldsymbol r-b\hat z|}-\frac{a}{b}\sum_l\frac{\left(a^2/b\right)^l}{r^{l+1}}P_l\right]
=\frac{q}{4\pi\varepsilon_0}\left[\frac{1}{|\boldsymbol r-b\hat z|}-\frac{a/b}{|\boldsymbol r-(a^2/b)\hat z|}\right].$$

**结果：** 镜像电荷 $q'=-\dfrac{a}{b}q$，位于 $b'=\dfrac{a^2}{b}$（球内）。

**检验：** $b\to\infty$（电荷远离）时 $q'\to0$、$b'\to0$，感应效应消失 ✓；$b=a$ 时 $q'=-q$、$b'=a$，与"电荷贴住球面"一致。球面 $r=a$ 上代回确为零（$|\boldsymbol r-b\hat z|=R_1$、$|\boldsymbol r-b'\hat z|=R_2$，$R_1=(b/a)R_2$）。

**读法：** 镜像法把边界条件吸收进源，代价是解只在 $r>a$ 有效；球内那个"镜像"不是真实电荷。

**4.27** 思路：$\sin^2\theta$ 是 $\cos\theta$ 的二次多项式，展开只到 $l=2$ 就精确。

过程：$\sin^2\theta=1-\cos^2\theta$，而 $\cos^2\theta=\dfrac13P_0+\dfrac23P_2$（题 4.4），故

$$V(\theta)=V_0\left(1-\frac13P_0-\frac23P_2\right)=V_0\left(\frac23-\frac23P_2(\cos\theta)\right) .$$

球内含原点取 $r^l$、球外取 $r^{-(l+1)}$，在 $r=a$ 处对上 $V(\theta)$：

$$\Phi_{\mathrm{in}}=V_0\left[\frac23-\frac23\left(\frac{r}{a}\right)^2P_2(\cos\theta)\right],\qquad
\Phi_{\mathrm{out}}=V_0\left[\frac23\frac{a}{r}-\frac23\left(\frac{a}{r}\right)^3P_2(\cos\theta)\right] .$$

**结果：** 内外解各只有两项；球外 $l=0$ 项表示球上的净"等效电荷"，$l=2$ 项是四极。

**检验：** $r=a$ 时两式都回到 $V_0(2/3-2P_2/3)=V_0\sin^2\theta$ ✓；$r\to0$ 有界 ✓；$r\to\infty$ 按 $1/r$ 衰减（净单极）✓。

**读法：** 只有两项不是巧合：$V$ 是二次多项式，$l>2$ 的矩必为零。级数在这里是精确的，没有截断误差。

**4.28** 思路：两边都按 $j_l$ 的小宗量展开，逐阶比较系数。

过程：左边 $e^{ikr\cos\theta}=1+ikr\cos\theta-\dfrac{(kr)^2}{2}\cos^2\theta+\cdots$，记 $x=kr$。右边用 $j_0=1-\dfrac{x^2}{6}$、$j_1=\dfrac{x}{3}$、$j_2=\dfrac{x^2}{15}$：

$$\sum_l(2l+1)i^lj_lP_l=\left(1-\frac{x^2}{6}\right)+3i\cdot\frac{x}{3}\cos\theta-5\cdot\frac{x^2}{15}\cdot\frac{3\cos^2\theta-1}{2}+\cdots$$

$$=1+ix\cos\theta-\frac{x^2}{6}-\frac{x^2}{3}\cdot\frac{3\cos^2\theta-1}{2} .$$

合并 $x^2$ 项：$-\dfrac16-\dfrac{3\cos^2\theta-1}{6}=-\dfrac{\cos^2\theta}{2}$，故右边 $=1+ix\cos\theta-\dfrac{x^2}{2}\cos^2\theta$。

**结果：** 两边到 $(kr)^2$ 阶完全一致，验证了系数 $(2l+1)i^l$。

**检验：** $l=0,1,2$ 三阶都对上，且每一阶只含相应阶的 $P_l$——逐阶匹配是独立的，所以三项验证足以支撑一般式。

**读法：** 展开式成立的前提是 $kr$ 不大：$x^2$ 项被 $x^2/3$ 量级的 $l=2$ 修正，$x=0.5$ 时它只占 8%。

**4.29** 思路：把 $R_{20}$ 代入径向方程，逐项相消来验证；能量由 $\kappa=1/(na_0)$ 给出。

过程：取 $a_0=1$、$n=2$、$l=0$，则 $\kappa=\dfrac{1}{na_0}=\dfrac12$，径向方程化为

$$R''+\frac2rR'+\left(-\frac14+\frac2r\right)R=0 .$$

$R_{20}=C(2-r)e^{-r/2}$，$C=\dfrac{1}{2\sqrt2}$。逐次求导：

$$R'=Ce^{-r/2}\left[-1-\frac{2-r}{2}\right]=Ce^{-r/2}\cdot\frac{r-4}{2},$$

$$R''=Ce^{-r/2}\left[\frac12-\frac{r-4}{4}\right]=Ce^{-r/2}\left(\frac32-\frac r4\right).$$

于是三项分别为

$$R''=Ce^{-r/2}\left(\frac32-\frac r4\right),\qquad
\frac2rR'=Ce^{-r/2}\left(1-\frac4r\right),$$

$$\left(-\frac14+\frac2r\right)R=Ce^{-r/2}\left(\frac r4-\frac52+\frac4r\right).$$

相加：常数项 $\dfrac32+1-\dfrac52=0$，$r$ 项 $-\dfrac r4+\dfrac r4=0$，$\dfrac1r$ 项 $-\dfrac4r+\dfrac4r=0$。

**结果：** $R_{20}$ 满足径向方程；$\kappa=\dfrac{1}{2a_0}$ 给 $E_2=-\dfrac{\hbar^2\kappa^2}{2\mu}=-\dfrac{13.6}{4}\ \mathrm{eV}=-3.4\ \mathrm{eV}$。

**检验：** 与 $E_n=-13.6/n^2$ 在 $n=2$ 处一致 ✓。注意 $r=2a_0$ 处 $R=0$，方程平凡满足，不能当作检验——上面在任意 $r$ 都相消，才是非平凡的验证。

**读法：** 径向函数的节点位置与衰减常数都由 $(n,l)$ 定死；代入验证时一定要在非节点处做，否则看不出问题。

**4.30** 思路：每一项相对单极的大小是 $J_n(a/r)^n$，把 $r=2a$ 代进去逐项比较。

过程：$\Phi_g=-\dfrac{GM}{r}\left[1-\sum_{n\ge2}J_n\left(\dfrac{a}{r}\right)^nP_n\right]$。$r=2a$ 时 $(a/r)^n=2^{-n}$：

$$J_2\left(\frac{a}{r}\right)^2=\frac{1.0826\times10^{-3}}{4}=2.71\times10^{-4},$$

$$J_4\left(\frac{a}{r}\right)^4=\frac{-1.62\times10^{-6}}{16}=-1.01\times10^{-7}.$$

**结果：** $l=2$ 项 $2.7\times10^{-4}$、$l=4$ 项 $-1.0\times10^{-7}$（比 $l=2$ 小 $3.7\times10^{-4}$）；$l=6$ 项更小两个量级，所以截断到 $l=4$ 的相对误差在 $10^{-9}$ 以下。

**检验：** 与 4.23 的比值 $3.7\times10^{-4}$ 一致 ✓；量纲：每一项都是无量纲修正 ✓。

**读法：** 地球重力场在 $r\ge2a$ 处基本就是"单极 + $J_2$"；更高阶项只在低轨高精度定轨里有意义。

**4.31** 思路：简并的来源分两种——转动对称性（任何中心力场都有）和库仑势特有的隐藏对称性；碱金属破坏的是后者。

过程：氢原子的 $2s$、$2p$ 同能量，因为势是严格的 $-e^2/(4\pi\varepsilon_0r)$，此时存在拉普拉斯–龙格–楞次矢量守恒（隐藏的 $SO(4)$ 对称性），能量只依赖 $n$，于是 $n$ 相同、$l$ 不同的态简并。

碱金属的价电子感受到的是"核 $+$ 内层电子"的屏蔽势 $V(r)=-Z_{\mathrm{eff}}(r)e^2/(4\pi\varepsilon_0r)$，不再是纯 $1/r$，隐藏对称性被破坏。$s$ 电子穿透内层、看到更大的 $Z_{\mathrm{eff}}$，能量更低；$l$ 大的电子被离心势（$\hbar^2l(l+1)/2\mu r^2$）挡在核外，近似只看到 $+e$，能量接近氢。

**结果：** 氢里 $E_{2s}=E_{2p}$；碱金属里 $E_{3s}<E_{3p}<E_{3d}$，量子亏损 $\delta_0>\delta_1>\delta_2$。

**检验：** 数据：钠的 $\delta_0=1.37$、$\delta_1=0.88$、$\delta_2\approx0.01$（题 4.20），随 $l$ 单调下降 ✓，与"穿透越深、修正越大"一致。

**读法：** 判断简并会不会被破坏，只问一句：有没有哪个微扰破坏了对应的对称性。屏蔽势破坏的是"$l$ 简并"，不影响"$m$ 简并"（后者由转动对称性保证）。

**4.32** 思路：径向函数给的是 $R_{32}\propto r^2e^{-r/(3a_0)}$，节点数由 $n-l-1$ 定；期望值和最概然半径都是积分/极值。

过程：$n=3$、$l=2$，径向节点数 $n-l-1=0$。平均半径用一般公式

$$\langle r\rangle=\frac{a_0}{2}\left[3n^2-l(l+1)\right]=\frac{a_0}{2}\left(27-6\right)=10.5a_0 .$$

最概然半径：径向概率 $P(r)\propto r^2\left(r^2e^{-r/(3a_0)}\right)^2=r^6e^{-2r/(3a_0)}$，

$$\frac{\mathrm{d}P}{\mathrm{d}r}\propto\left(\frac6r-\frac{2}{3a_0}\right)r^6e^{-2r/(3a_0)}=0
\quad\Longrightarrow\quad r=9a_0 .$$

**结果：** 径向节点 0 个；$\langle r\rangle=10.5a_0=5.6\ \text{Å}$；$r_{\mathrm{mp}}=9a_0=4.8\ \text{Å}$。

**检验：** $r_{\mathrm{mp}}=n^2a_0=9a_0$ 与"最高 $l$ 的态峰值接近 $n^2a_0$"的规律一致 ✓；$r_{\mathrm{mp}}<\langle r\rangle$（9 vs 10.5），说明分布左偏、有长尾，合理。

**读法：** $3d$ 没有径向节点、也没有核附近概率（$l=2$ 的离心势很强），是一个"胖而干净"的态；化学里过渡金属的 $d$ 电子就住在这种壳层里。

**4.33** 靠的是"波函数在极轴（$\theta=0,\pi$）有界"，等价于动能有限：解在端点对数发散时 $\int|\nabla\psi|^2$ 发散。

如果球面只覆盖上半球 $\theta\in[0,\pi/2]$，$l$ **不必**是整数：此时 $\theta=\pi/2$ 成了真实边界，要在那里加条件（例如 $V$ 或 $\partial V/\partial\theta$ 给定），$l(l+1)$ 由这个条件定，解是非整数阶的连带勒让德函数（锥函数）。所以整数性的来源是"两极都在边界上"，不是球坐标本身。

**4.34** 因为 $\nabla^2(1/r)=0$ 只在 $r\ne0$ 成立；在原点它是 $-4\pi\delta(\boldsymbol r)$，正是电荷所在。

多极展开用的场点总在源外（$r>r'$），那里 $1/|\boldsymbol r-\boldsymbol r'|$ 确实调和，展开合法。奇性不是麻烦，它就是源：没有 $\delta$，展开也就没有"单极项对应总电荷"这回事。

**4.35** 不能。$r<r'$ 时应展开成

$$\frac{1}{|\boldsymbol r-\boldsymbol r'|}=\sum_l\frac{r^l}{r'^{l+1}}P_l(\cos\gamma),$$

即 $r$ 与 $r'$ 的角色对调（收敛条件是 $r'<r$ 的反面）。强行用 $r>r'$ 的式子等于把生成函数里的 $t=r'/r>1$ 代入，超出收敛域，级数发散——物理上就是"你在源内部，各项越算越大"。

**4.36** 不成立。正交性来自边界项 $\left[(1-x^2)(\cdots)\right]_{-1}^{1}=0$，它要求区间是整个 $[-1,1]$。半球面对应 $x\in[0,1]$，端点 $x=0$ 处 $1-x^2\ne0$，边界项不为零，$\int_0^1P_lP_{l'}\,\mathrm{d}x\ne0$（例如 $\int_0^1P_0P_1=\frac12\ne0$）。

后果：展开系数不能靠投影算，要解一个无穷维线性方程组（截断后求逆），或者改用该区域自己的本征函数。

**4.37** 不矛盾。连续说的是**函数值**：$R_{10}(0)=2a_0^{-3/2}$ 有限且连续。奇性在**势**里（$-e^2/4\pi\varepsilon_0r$），波函数的导数在原点有折点，$\nabla^2\psi$ 的奇性恰好被势的奇性抵消——这是定态方程两边在原点同时发散又互相抵消的意思。

效应：$|\psi(0)|^2=1/(\pi a_0^3)\approx2.1\times10^{30}\ \mathrm{m^{-3}}$ 直接进入三条可观测量：21 cm 超精细线、电子俘获、穆斯堡尔同质异能移。

**4.38** 带电球没有唯一的偶极矩。把原点平移 $\boldsymbol a$，$\boldsymbol p=\int\rho\boldsymbol r'\,\mathrm{d}V'$ 变成 $\boldsymbol p+Q\boldsymbol a$，值变了。

只有 $Q=0$ 时偶极矩与原点无关，才是内禀量。所以"偶极矩"是中性物体的属性；带电体的远场第一项永远是单极，偶极项可以被原点选择消掉。

**4.39** 不矛盾。展开式是精确的恒等式，无穷多项都得有；但第 $l$ 项的系数含 $j_l(kr)\sim(kr)^l$，当 $kR\ll1$ 时 $l\ge1$ 的项被 $(kR)^l$ 系统性压低。

截断不是"忽略无穷多数学项"，而是"丢掉物理上小到测不出的项"，误差可以估计（例 9.8 的算法：每多留一阶，误差掉一个 $kr$ 因子）。

**4.40** 因为两维的径向方程不同。三维 $l=0$ 时 $(r^2R')'=0$，解 $R=A+B/r$；二维时 $(rR')'=0$，解 $R=A+B\ln r$。

物理来源是通量守恒：三维点源的场线摊在 $4\pi r^2$ 上，场按 $1/r^2$、势按 $1/r$；二维线源摊在 $2\pi r$ 上，场按 $1/r$、势按 $\ln r$。所以"三维没有 $\ln r$"不是数学偏好，是几何维数。

**4.41** 错在把"单点概率为零"当成理由。概率密度在一点的取值确实不影响积分，但发散的解让 $\partial\psi/\partial\theta\sim1/(1-x)$，动能积分 $\int|\nabla\psi|^2\,\mathrm{d}V$ 对数发散，函数根本不在哈密顿量的定义域里。

判据不是"某点的值"，而是"积分是否有限"：$|\psi|^2$ 可积只保证归一化；能量有限还要 $\nabla\psi$ 可积。

**4.42** 不必。反例：球壳上 $V(\theta)=V_0\cos\theta$，球内

$$\Phi_{\mathrm{in}}=V_0\frac{r}{a}\cos\theta$$

满足 $\nabla^2\Phi=0$，且随 $\theta$ 变化。球内无电荷只保证 $\Phi$ 调和；要得到"常数"还得加球对称的边界条件。

一般成立的是**平均值定理**：球心电势等于球面平均——平均值可以不是常数。

**4.43** 思路：$x^2$ 与 $x^4$ 的矩阵元都能由递推 $\xi|n\rangle=\sqrt{\frac{n+1}{2}}|n+1\rangle+\sqrt{\frac n2}|n-1\rangle$ 直接数出来，不必积分。

过程：先算 $\langle n|\xi^2|n\rangle$：把 $\xi$ 作用两次，只有"出去再回来"的两条路径有贡献，

$$\langle n|\xi^2|n\rangle=\frac{n+1}{2}+\frac n2=n+\frac12 .$$

取 $n=2$：$\langle\xi^2\rangle_2=\dfrac52$，故

$$\langle x^2\rangle_2=\frac{\hbar}{m\omega}\cdot\frac52=\frac{5\hbar}{2m\omega} .$$

再算 $\langle1|\xi^4|1\rangle$。用 $\xi|1\rangle=|2\rangle+\dfrac{1}{\sqrt2}|0\rangle$（因为 $\sqrt{2/2}=1$、$\sqrt{1/2}$），于是

$$\xi^2|1\rangle=\left(|2\rangle+\frac{1}{\sqrt2}|0\rangle\right)\ \text{再作用一次}\xi$$
$$=\left(\sqrt{\frac32}|3\rangle+\sqrt{\frac22}|1\rangle\right)+\frac{1}{\sqrt2}\left(\frac{1}{\sqrt2}|1\rangle\right)
=\sqrt{\frac32}|3\rangle+\left(1+\frac12\right)|1\rangle .$$

取模方：$\langle1|\xi^4|1\rangle=\dfrac32+\dfrac94=\dfrac{15}{4}$，故

$$\langle x^4\rangle_1=\left(\frac{\hbar}{m\omega}\right)^2\frac{15}{4}=\frac{15\hbar^2}{4m^2\omega^2} .$$

**结果：** $\langle x^2\rangle_2=\dfrac{5\hbar}{2m\omega}$；$\langle x^4\rangle_1=\dfrac{15\hbar^2}{4m^2\omega^2}$。

**检验：** 通式 $\langle\xi^2\rangle_n=n+\frac12$ 给 $n=2$ 的 $5/2$ ✓；$\langle\xi^4\rangle_n=\frac34(2n^2+2n+1)$ 给 $n=1$ 的 $\frac34\times5=\frac{15}{4}$ ✓，与 $n=0$ 的 $3/4$ 衔接。

**读法：** 每个 $\xi$ 把态挪一步，$\xi^{2k}$ 的矩阵元就是"走 $2k$ 步、回到原态"的路径数——组合计数，不是积分。

**4.44** 思路：第一激发态的波函数已知，概率密度的极值由 $\dfrac{\mathrm{d}}{\mathrm{d}\xi}\left(|\psi_1|^2\right)=0$ 定。

过程：$\psi_1\propto\xi e^{-\xi^2/2}$，故

$$|\psi_1|^2\propto\xi^2e^{-\xi^2} .$$

$$\frac{\mathrm{d}}{\mathrm{d}\xi}\left(\xi^2e^{-\xi^2}\right)=\left(2\xi-2\xi^3\right)e^{-\xi^2}=2\xi\left(1-\xi^2\right)e^{-\xi^2}=0 .$$

根为 $\xi=0$（极小，概率为零）与 $\xi=\pm1$（两个极大）。换回 $x$：

$$x=\pm\sqrt{\frac{\hbar}{m\omega}} .$$

**结果：** 两个极大在 $x=\pm\sqrt{\hbar/(m\omega)}$，节点在 $x=0$。

**检验：** 极大值处 $\xi^2e^{-\xi^2}=1/e=0.368$，零点处为 0 ✓。节点数 1 与"第 $n$ 态有 $n$ 个节点"一致 ✓；极大数 2 也符合"节点把概率分成 $n+1$ 块"。

**读法：** 经典谐振子的概率在两端最大、在原点最小（速度最大），量子基态却集中在原点——第一激发态才开始"像"经典分布（两个峰）。

**4.45** 思路：$2s$ 的径向函数已知，三个量都是 $r^ne^{-r/a_0}$ 型积分，用 $\int_0^\infty r^ne^{-\alpha r}\mathrm{d}r=n!/\alpha^{n+1}$。

过程：$R_{20}=\dfrac{1}{2\sqrt2}a_0^{-3/2}\left(2-\dfrac{r}{a_0}\right)e^{-r/(2a_0)}$，令 $y=r/a_0$：

$$\langle r\rangle=\frac{a_0}{8}\int_0^\infty y^3(2-y)^2e^{-y}\mathrm{d}y
=\frac{a_0}{8}\left(4\cdot3!-4\cdot4!+5!\right)=\frac{a_0}{8}(24-96+120)=6a_0 .$$

$$\langle r^2\rangle=\frac{a_0^2}{8}\int_0^\infty y^4(2-y)^2e^{-y}\mathrm{d}y
=\frac{a_0^2}{8}\left(4\cdot4!-4\cdot5!+6!\right)=\frac{a_0^2}{8}(96-480+720)=42a_0^2 .$$

于是 $\Delta r=\sqrt{42-36}\,a_0=\sqrt6\,a_0=2.45a_0$。

**结果：** $\langle r\rangle_{2s}=6a_0=3.2\ \text{Å}$，$\langle r^2\rangle=42a_0^2$，$\Delta r=2.45a_0$；$1s$ 的 $\Delta r=0.87a_0$。

**检验：** 通式 $\langle r\rangle=\frac{a_0}{2}[3n^2-l(l+1)]$ 给 $\frac{a_0}{2}(12-0)=6a_0$ ✓；$\langle r^2\rangle=\frac{a_0^2n^2}{2}[5n^2+1-3l(l+1)]$ 给 $\frac{4a_0^2}{2}(20+1)=42a_0^2$ ✓。

**读法：** $2s$ 的宽度是 $1s$ 的 2.8 倍（$2.45/0.87$），但两者都在原点附近有概率——$s$ 态"又宽又透"的特点在这里一目了然。

**4.46** 思路：先把被积函数写成显式球谐，再分开做 $\theta$ 与 $\varphi$ 的积分。

过程：$Y_{21}=-\sqrt{\dfrac{15}{8\pi}}\sin\theta\cos\theta e^{i\varphi}$，$Y_{11}=-\sqrt{\dfrac{3}{8\pi}}\sin\theta e^{i\varphi}$，$Y_{22}=\sqrt{\dfrac{15}{32\pi}}\sin^2\theta e^{2i\varphi}$。

第一式：$m'=2$、$m=1$，$\varphi$ 积分是 $\int_0^{2\pi}e^{i(1-2)\varphi}\mathrm{d}\varphi=0$，故

$$\int Y_{22}^*\cos\theta\,Y_{11}\,\mathrm{d}\Omega=0 .$$

这违反选择定则（$\Delta m\ne0$），所以禁戒。

第二式：$m'=m=1$，$\varphi$ 给出 $2\pi$；$\theta$ 部分是

$$\int Y_{21}^*\cos\theta\,Y_{11}\,\mathrm{d}\Omega
=\frac{\sqrt{45}}{8\pi}\cdot2\pi\int_0^\pi\sin^3\theta\cos^2\theta\,\mathrm{d}\theta .$$

用 $u=\cos\theta$：$\int_{-1}^{1}(1-u^2)u^2\mathrm{d}u=\dfrac23-\dfrac25=\dfrac{4}{15}$。于是

$$=\frac{\sqrt{45}}{4}\cdot\frac{4}{15}=\frac{\sqrt{45}}{15}=\frac{1}{\sqrt5}\approx0.447 .$$

**结果：** $\displaystyle\int Y_{21}^*\cos\theta\,Y_{11}\,\mathrm{d}\Omega=\frac{1}{\sqrt5}\ne0$（允许，$\Delta l=1$、$\Delta m=0$）；$\displaystyle\int Y_{22}^*\cos\theta\,Y_{11}\,\mathrm{d}\Omega=0$（禁戒）。

**检验：** 量纲无量纲 ✓；$\left(1/\sqrt5\right)^2=1/5$ 与"三个 $m$ 分量的平方和"关系一致（$|Y|^2$ 归一）。若把 $\cos\theta$ 换成 $1$，两个积分都由正交性给零——说明非零完全来自 $\cos\theta\propto Y_{10}$ 的"$l=1$ 转移"。

**读法：** 选择定则的代数本质：$\cos\theta Y_{l,m}$ 只能分解成 $Y_{l\pm1,m}$ 的线性组合，所以只有 $\Delta l=\pm1$、$\Delta m=0$ 的矩阵元非零。

## 第 5 章

**5.1** 思路：$\delta$ 只在积分里起作用，用筛选性质 $\int\delta(x-x_0)f(x)\mathrm{d}x=f(x_0)$；第二个要把 $\delta(2x-4)$ 的自变量化成一。

过程：第一问，零点 $x=2$ 落在积分区间内，直接取 $f(2)=2^2+1=5$：

$$\int_{-\infty}^{\infty}(x^2+1)\delta(x-2)\,\mathrm{d}x=5 .$$

第二问，先换元 $u=2x-4$，$\mathrm{d}x=\mathrm{d}u/2$，$x=-1$ 对应 $u=-6$、$x=3$ 对应 $u=2$：

$$\int_{-1}^{3}\delta(2x-4)\,\mathrm{d}x=\frac12\int_{-6}^{2}\delta(u)\,\mathrm{d}u=\frac12 .$$

**结果：** 第一式 $=5$；第二式 $=\dfrac12$。

**检验：** 第二式也可以直接用 $\delta(ax)=\delta(x)/|a|$：$\delta(2x-4)=\dfrac12\delta(x-2)$，积分给 $\dfrac12$ ✓，两条路一致。量纲：第一式被积函数 $\mathrm{m^2}\times\mathrm{m^{-1}}=\mathrm{m}$，结果 5 对应"$x$ 以 m 为单位"。

**读法：** $\delta(ax)$ 的系数 $1/|a|$ 不是约定，是换元的雅可比——"压缩自变量"会让密度变高。

**5.2** 思路：用定义 $\int\delta(ax)f(x)\mathrm{d}x=f(0)$，做换元把 $ax$ 变成新变量。

过程：设 $a>0$，令 $u=ax$，$\mathrm{d}x=\mathrm{d}u/a$，积分限不变：

$$\int_{-\infty}^{\infty}\delta(ax)f(x)\,\mathrm{d}x=\frac1a\int_{-\infty}^{\infty}\delta(u)f\left(\frac ua\right)\mathrm{d}u=\frac{f(0)}{a} .$$

设 $a<0$，同样换元但 $\mathrm{d}x=\mathrm{d}u/a<0$，且 $x\to\pm\infty$ 时 $u\to\mp\infty$，两个负号抵消：

$$\int_{-\infty}^{\infty}\delta(ax)f(x)\,\mathrm{d}x=\frac1a\int_{\infty}^{-\infty}\delta(u)f\left(\frac ua\right)\mathrm{d}u=\frac{f(0)}{|a|} .$$

合起来 $\delta(ax)=\delta(x)/|a|$。

**结果：** $\delta(ax)=\dfrac{1}{|a|}\delta(x)$，$a\ne0$。

**检验：** $a=-1$：$\delta(-x)=\delta(x)$（$\delta$ 是偶的）✓，与公式给 $1/|-1|=1$ 一致。$a=2$ 时面积：$\int\delta(2x)\mathrm{d}x=1/2=\int\delta(x)/2\,\mathrm{d}x$ ✓。

**读法：** 绝对值来自"换元时积分限的方向"；$a<0$ 时积分上下限翻转一次，正好抵消分母的负号。

**5.3** 思路：复合 $\delta$ 用公式 $\delta(g(x))=\sum_i\dfrac{\delta(x-x_i)}{|g'(x_i)|}$，$x_i$ 是单零点。

过程：$g=x^2-4$，零点 $x=\pm2$，$g'=2x$，$|g'(\pm2)|=4$：

$$\delta(x^2-4)=\frac{\delta(x-2)}{4}+\frac{\delta(x+2)}{4} .$$

$g=\cos x$ 在 $[0,2\pi]$ 上零点 $x=\pi/2,\ 3\pi/2$，$g'=-\sin x$，$|g'|=1$：

$$\delta(\cos x)=\delta\left(x-\frac{\pi}{2}\right)+\delta\left(x-\frac{3\pi}{2}\right),\qquad 0\le x\le2\pi .$$

**为什么 $g'=0$ 时失效：** 若 $x_0$ 是二重零点（如 $g=x^2$、$x_0=0$），换元 $u=g(x)$ 在 $x_0$ 附近不可逆，$\int\delta(x^2)f(x)\mathrm{d}x$ 对 $f(0)\ne0$ 直接发散——密度在那里"压得无限高"。

**结果：** 两式如上。

**检验：** 用 $\int\delta(x^2-4)f\,\mathrm{d}x=\frac14[f(2)+f(-2)]$ 验证：取 $f=1$ 得 $1/2$；直接换元 $u=x^2-4$ 在 $x>0$、$x<0$ 两支各给 $1/2$，相加为 1？——注意两支的 $\mathrm{d}u=2x\,\mathrm{d}x$ 符号相反，各自给 $1/4$，合计 $1/2$，与公式一致 ✓。

**读法：** 复合 $\delta$ 的系数是"零点的密度倒数"：$g$ 在零点附近越陡，$\delta$ 越窄、系数越小。

**5.4** 思路：$\delta'$ 的定义是分部积分"把导数挪到试验函数上"，用它算两个积分。

过程：对任意光滑 $f$，

$$\int x\delta'(x)f(x)\,\mathrm{d}x=-\int\delta(x)\frac{\mathrm{d}}{\mathrm{d}x}\left[xf(x)\right]\mathrm{d}x
=-\left[xf(x)\right]_{x=0}=-f(0) .$$

而 $\int\left[-\delta(x)\right]f(x)\mathrm{d}x=-f(0)$，两式对一切 $f$ 相等，故

$$x\delta'(x)=-\delta(x) .$$

第二问取 $f=x^2$：$\int x^2\delta'(x)\mathrm{d}x=-\left.\dfrac{\mathrm{d}}{\mathrm{d}x}\left(x^2\right)\right|_{0}=-2x\big|_0=0$。

**结果：** $x\delta'(x)=-\delta(x)$；$\displaystyle\int_{-\infty}^{\infty}x^2\delta'(x)\,\mathrm{d}x=0$。

**检验：** 用 $x\delta(x)=0$ 两边求导：$\delta(x)+x\delta'(x)=0$，即 $x\delta'(x)=-\delta(x)$ ✓，与分部积分的结果一致。

**读法：** $\delta'$ 是"偶极子密度"：正负两个 $\delta$ 无限靠近，所以它对常数、对 $x^2$ 这类偶函数的积分都是零，只对奇函数有贡献。

**5.5** 思路：球坐标的 $\delta$ 要满足 $\int\delta(\boldsymbol r)f\,\mathrm{d}^3r=f(0)$，把 Jacobian $4\pi r^2$ 吸收进去。

过程：球坐标 $\mathrm{d}^3r=r^2\sin\theta\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi$，先对角度积分得 $4\pi r^2\mathrm{d}r$：

$$\int\delta(\boldsymbol r)f(\boldsymbol r)\,\mathrm{d}^3r
=\int_0^\infty\!\!\int\!\!\int\delta(\boldsymbol r)f(r)\,r^2\sin\theta\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi .$$

要让它在任意 $f$ 下等于 $f(0)$，只能取 $\delta(\boldsymbol r)=\dfrac{\delta(r)}{4\pi r^2}$，因为

$$\int_0^\infty\frac{\delta(r)}{4\pi r^2}f(r)\,4\pi r^2\,\mathrm{d}r=\int_0^\infty\delta(r)f(r)\,\mathrm{d}r=f(0) .$$

于是 $\int_{r<a}\delta(\boldsymbol r)\,\mathrm{d}^3r=\int_0^a4\pi r^2\cdot\dfrac{\delta(r)}{4\pi r^2}\mathrm{d}r=1$。

**结果：** $\delta(\boldsymbol r)=\dfrac{\delta(r)}{4\pi r^2}$；$\displaystyle\int_{r<a}\delta(\boldsymbol r)\,\mathrm{d}^3r=1$。

**检验：** 量纲：$\delta(r)$ 是 $1/\mathrm{m}$，除以 $4\pi r^2$（$\mathrm{m^2}$）得 $1/\mathrm{m^3}$，正是三维 $\delta$ 的量纲 ✓。

**读法：** 原点这个点"占的 $r$ 区间"是零、但体积元 $4\pi r^2\mathrm{d}r$ 在原点也趋于零，两者的比值正是 $1/4\pi r^2$——这就是球坐标 $\delta$ 的全部内容。

**5.6** 思路：先算 $\nabla\cdot\nabla(1/r)$ 的积分（高斯定理），再说明它只在原点非零。

过程：对以原点为球心、半径 $\epsilon$ 的小球，$r\ne0$ 处 $\nabla^2(1/r)=0$；球面上

$$\frac{\partial}{\partial r}\frac1r=-\frac{1}{r^2},\qquad
\oint\nabla\left(\frac1r\right)\cdot\mathrm{d}\boldsymbol S
=\left(-\frac{1}{\epsilon^2}\right)4\pi\epsilon^2=-4\pi,$$

与 $\epsilon$ 无关。由高斯定理 $\int_{r<\epsilon}\nabla^2(1/r)\,\mathrm{d}V=-4\pi$，而体积趋于零、积分不变，只能是

$$\nabla^2\frac1r=-4\pi\delta(\boldsymbol r) .$$

平移得 $\nabla^2\dfrac{1}{|\boldsymbol r-\boldsymbol r'|}=-4\pi\delta(\boldsymbol r-\boldsymbol r')$。

**结果：** $\nabla^2(1/r)=-4\pi\delta(\boldsymbol r)$；$\nabla^2\dfrac{1}{|\boldsymbol r-\boldsymbol r'|}=-4\pi\delta(\boldsymbol r-\boldsymbol r')$。

**检验：** 量纲：两边都是 $1/\mathrm{m^3}$ ✓。$r\ne0$ 时两边都为零 ✓。常数 $-4\pi$ 不能改：$\oint$ 的面积乘梯度给 $4\pi$。

**读法：** 点电荷的电势在别处调和、在原点"破了"，破的方式就是 $\delta$——格林函数的奇异性与源是一回事。

**5.7** 思路：$G''=\delta$ 且两端为零，所以 $x\ne x'$ 时 $G$ 是直线，两侧斜率的跳变由 $\delta$ 定。

过程：设

$$G=\begin{cases}Ax, & x<x',\\ B(L-x), & x>x'.\end{cases}$$

连续性：$Ax'=B(L-x')$；导数跳变：$G'(x'>)-G'(x'<)=-B-A=1$。解这对方程：由第二式 $B=-A-1$，代第一式

$$Ax'=(-A-1)(L-x')\quad\Longrightarrow\quad A=\frac{-(L-x')}{L},\qquad B=-\frac{x'}{L}.$$

于是 $G(x,x')=-\dfrac{x_<(L-x_>)}{L}$，$x_<=\min$、$x_>=\max$。

$L=2$、$x'=0.5$、$x=1$：$x_<=0.5$、$x_>=1$，$G=-0.5\times(2-1)/2=-0.25$。

**结果：** $G(x,x')=-\dfrac{x_<(L-x_>)}{L}$；$G(1,0.5)=-0.25$（长度单位取 m 时为 $-0.25\ \mathrm{m}$）。

**检验：** $x=x'$ 处两侧都给 $-x'(L-x')/L$，连续 ✓；$G(0)=G(L)=0$ ✓；斜率差 $-B-A=\frac{x'}{L}+\frac{L-x'}{L}=1$ ✓。

**读法：** 一维格林函数是一片帐篷：源点处一个折角，折角的斜率差正好是 $\delta$ 的强度。

**5.8** 思路：把 $\delta$ 与 $G$ 都按正弦本征函数展开，截断到 $N=5$ 与分段解比。

过程：$L=2$，$\psi_n=\sqrt{2/L}\sin(n\pi x/L)$，$\lambda_n=(n\pi/L)^2$，故

$$G=-\frac{2L}{\pi^2}\sum_{n=1}^{\infty}\frac{1}{n^2}\sin\frac{n\pi x}{L}\sin\frac{n\pi x'}{L} .$$

在 $x=x'=0.5$ 处 $\sin(n\pi/4)$ 依次为 $\frac{\sqrt2}{2},1,\frac{\sqrt2}{2},0,-\frac{\sqrt2}{2},\dots$，平方后为 $\frac12,1,\frac12,0,\frac12$。取前 5 项：

$$\sum_{n=1}^{5}\frac{1}{n^2}\sin^2\frac{n\pi}{4}
=0.5+0.25+0.0556+0+0.02=0.8256,$$

$$G_5=-\frac{4}{\pi^2}\times0.8256=-0.3346 .$$

**结果：** 分段解 $G=-0.375$，级数 $G_5=-0.335$，相对误差 $\dfrac{0.040}{0.375}=10.8\%$。

**检验：** 误差随 $N$ 按 $1/N$ 降（题 5.28 定量），$N=5$ 时 $10\%$ 与 $0.2/5=4\%$（源点处的渐近）同量级——量级对得上，常数因取 5 项而有偏差。

**读法：** 级数在源点附近收敛最慢，因为 $\delta$ 的尖角需要很多高阶模；离开源点几项就够。

**5.9** 思路：半空间接地平面用镜像法：镜像点在 $z'^*=-z'$，符号相反。

过程：$G(\boldsymbol r,\boldsymbol r')=\dfrac{1}{4\pi}\left[\dfrac{1}{|\boldsymbol r-\boldsymbol r'^*|}-\dfrac{1}{|\boldsymbol r-\boldsymbol r'|}\right]$，其中 $\boldsymbol r'^*=(x',y',-z')$。

$z=0$ 时 $|\boldsymbol r-\boldsymbol r'^*|=|\boldsymbol r-\boldsymbol r'|$，两项相消，$G=0$ ✓。

源移到边界 $z'\to0$：$\boldsymbol r'^*\to\boldsymbol r'$，两项对整个 $z>0$（除源点附近）都相消，$G\to0$。

**结果：** $G=0$ 在 $z=0$ 上；$z'\to0$ 时 $G\to0$（源点邻域除外）。

**检验：** 物理解释：电荷落到接地平面上，感应电荷与它"重合"，$z>0$ 内的场被完全抵消——接地平面把源短路了。这与平面镜像电荷 $q'=-q$ 随 $z'\to0$ 与源重合一致 ✓。

**读法：** 镜像法在源贴近边界时会退化（源与镜像重合）；数值上这时不能直接用镜像公式，要取极限或改用它法。

**5.10** 思路：量纲看 $G$ 的单位，符号看 $\phi=-\frac1{\varepsilon_0}\int G\rho$ 的代换。

过程：$G_0=-\dfrac{1}{4\pi|\boldsymbol r-\boldsymbol r'|}$ 的单位是 $1/\mathrm{m}$。电势由叠加公式

$$\phi(\boldsymbol r)=-\frac{1}{\varepsilon_0}\int G_0(\boldsymbol r,\boldsymbol r')\rho(\boldsymbol r')\,\mathrm{d}^3r'
=\frac{1}{4\pi\varepsilon_0}\int\frac{\rho(\boldsymbol r')}{|\boldsymbol r-\boldsymbol r'|}\,\mathrm{d}^3r' .$$

量纲：$\rho\,\mathrm{d}^3r'$ 是 $\mathrm{C}$，除以 $\varepsilon_0R$（$\mathrm{C/(V\cdot m)}\cdot\mathrm{m}$）给 $\mathrm{V}$ ✓。

**结果：** $[G_0]=1/\mathrm{m}$；$\phi=\dfrac{1}{4\pi\varepsilon_0}\int\dfrac{\rho}{|\boldsymbol r-\boldsymbol r'|}\mathrm{d}^3r'$（符号为正，正电荷给正电势）。

**检验：** 取点电荷 $\rho=q\delta(\boldsymbol r')$，筛选性质给 $\phi=\dfrac{q}{4\pi\varepsilon_0r}$ ✓，库仑定律。

**读法：** 格林函数的量纲由方程 $\nabla^2G=\delta$ 定：左边 $1/\mathrm{m^3}$、右边 $1/\mathrm{m^3}$，所以 $G\sim1/\mathrm{m}$。

**5.11** 思路：二维与三维只差 $\nabla^2\ln R$ 的"源强度"，用同样的高斯定理定常数。

过程：$\dfrac{\partial}{\partial R}\ln R=\dfrac1R$，绕原点的小圆上

$$\oint\nabla\ln R\cdot\mathrm{d}\boldsymbol l=\frac{1}{\epsilon}\cdot2\pi\epsilon=2\pi,$$

与 $\epsilon$ 无关，且 $R\ne0$ 处 $\nabla^2\ln R=0$，故 $\nabla^2\ln R=2\pi\delta(\boldsymbol r-\boldsymbol r')$。

二维"点电荷"是线电荷 $\lambda$，叠加公式给

$$\phi=-\frac{1}{\varepsilon_0}\int\frac{1}{2\pi}\ln R\,\lambda\,\mathrm{d}l
=-\frac{\lambda}{2\pi\varepsilon_0}\ln R+\text{常数} .$$

**结果：** $\nabla^2\ln R=2\pi\delta$；$\phi=-\dfrac{\lambda}{2\pi\varepsilon_0}\ln R+C$。

**检验：** 量纲：$\ln R$ 无量纲，$\lambda/\varepsilon_0$ 是 $\mathrm{V}$ ✓。取等势面 $R=$ 常数，正是同轴线 ✓。

**为什么二维必须整体中性：** $\ln R$ 在无穷远发散，净电荷非零时总能量 $\int E^2$ 对数发散；物理上二维系统（长直导线、等离子体柱）必须满足 $\sum\lambda_i=0$，否则场在远处不为零。

**读法：** 二维静电学的"零点"要人为选在某个参考半径上，这是 $\ln$ 与 $1/r$ 的根本区别。

**5.12** 思路：$R\ne0$ 时 $\delta$ 的自变量不为零、$G$ 满足齐次方程；$\delta$ 负责"只在推迟时刻亮一下"。

过程：$G_{\text{ret}}=-\dfrac{\delta(t-t'-R/c)}{4\pi R}$。$R\ne0$ 时对 $t$ 求两次导：

$$\frac{1}{c^2}\frac{\partial^2G}{\partial t^2}=-\frac{\delta''(t-t'-R/c)}{4\pi Rc^2},\qquad
\nabla^2G=-\frac{\delta''}{4\pi Rc^2}+\text{（含 }\delta,\delta'\text{ 的曲面项）},$$

而 $\delta(t-t'-R/c)$ 只在 $R=c(t-t')$ 的球面上非零，所以对整个空间积分时，两个 $\delta''$ 项相消、只剩源点项。

**结果：** $R\ne0$ 处 $\nabla^2G-\dfrac{1}{c^2}\dfrac{\partial^2G}{\partial t^2}=0$；$\delta$ 的作用是把源"限制在一个时刻"：$t'=t-R/c$。

**检验：** 若源在 $t'$ 时刻闪一下，观察者在 $t$ 时刻收到，时间差正好是 $R/c$ ✓（光速传播）。$R\ne0$ 处 $G$ 严格为零，说明信号只在光锥上 ✓。

**读法：** $\delta$ 不是数学装饰，它就是"因果"：不早不晚，正好 $R/c$。

**5.13** 思路：镜像电荷在平面下方等距处、符号相反，用 5.6 的公式写电势，再求法向导数得面密度。

过程：$q$ 距平面 $d$，镜像 $-q$ 在 $z=-d$。$z>0$ 处

$$\phi=\frac{q}{4\pi\varepsilon_0}\left(\frac{1}{r_1}-\frac{1}{r_2}\right),\qquad r_{1,2}=\sqrt{\rho^2+(z\mp d)^2} .$$

$\sigma=-\varepsilon_0\left.\dfrac{\partial\phi}{\partial z}\right|_{z=0}$。$z=0$ 时 $r_1=r_2=\sqrt{\rho^2+d^2}$，两式的 $z$ 导数分别是 $-\dfrac{z-d}{r_1^3}$ 与 $+\dfrac{z+d}{r_2^3}$，代入 $z=0$ 后和为 $\dfrac{2d}{(\rho^2+d^2)^{3/2}}$，故

$$\sigma(\rho)=-\frac{qd}{2\pi\left(\rho^2+d^2\right)^{3/2}} .$$

总感应电荷：$\int_0^\infty\sigma\,2\pi\rho\,\mathrm{d}\rho=-qd\int_0^\infty\dfrac{\rho\,\mathrm{d}\rho}{(\rho^2+d^2)^{3/2}}=-q$。力：

$$F=-\frac{q^2}{4\pi\varepsilon_0(2d)^2}=-\frac{q^2}{16\pi\varepsilon_0d^2} .$$

**结果：** $\sigma(0)=-\dfrac{q}{2\pi d^2}$；总感应电荷 $-q$；$q=1\ \mathrm{nC}$、$d=1\ \mathrm{mm}$ 时 $F=-2.2\times10^{-3}\ \mathrm{N}$（指向导体）。

**检验：** 量纲：$\sigma$ 为 $\mathrm{C/m^2}$ ✓，力为 N ✓。$d\to$ 大时 $\sigma\to0$ ✓。

**读法：** 感应电荷集中在半径 $\sim d$ 的圆盘里，总量恰好 $-q$：接地平面把源的电场"锁"在自己附近。

**5.14** 思路：两块平行接地板之间要用无穷多次镜像（每次反射又产生新的镜像），力是无穷级数。

过程：设板在 $z=0,a$，电荷在 $z=a/4$。镜像位置：先关于 $z=0$ 反射得 $-a/4$（$-q$），再关于 $z=a$ 反射得 $7a/4$（$-q$）；这两个又各自关于另一板反射，得 $9a/4$、$-7a/4$（$+q$）……镜像在 $z=\pm a/4+2na$ 处，符号交替，$n\in\mathbb Z$。无穷多的原因是"两块板互相反射，永不终止"。

力（沿 $z$，指向最近的板）：

$$F=\frac{q^2}{4\pi\varepsilon_0}\sum_{n\ne0}\frac{(-1)^{n+1}}{\left(z_n-z\right)^2},\qquad z_n=\frac a4+na .$$

**结果：** 无穷级数；最近的两项（$n=0$ 的 $-a/4$ 与 $n=1$ 的 $7a/4$）给出主项 $F\approx-\dfrac{q^2}{4\pi\varepsilon_0}\left[\dfrac{1}{a^2/4}-\dfrac{1}{(3a/2)^2}\right]$，即 $\dfrac{q^2}{4\pi\varepsilon_0a^2}\left[-4+\dfrac49\right]$。

**检验：** 正中间（$z=a/2$）时上下对称，两个最近镜像的力相消，整个级数成对抵消，$F=0$ ✓——这正是"对称性给零力"的例子。

**读法：** $a\to0$ 时 $F\propto1/a^2$ 发散：两块板越近，感应电荷越强、力越大；这也是微机电系统里"吸合"（pull-in）失稳的根源。

**5.15** 思路：球面镜像的三个公式（位置、电量、力）直接代入，注意"总感应电荷 = 镜像电量"这一条。

过程：$a=0.05\ \mathrm{m}$、$d=0.15\ \mathrm{m}$、$q=2\ \mu\mathrm{C}$。镜像电量与位置：

$$q'=-\frac ad\,q=-\frac{0.05}{0.15}\times2\times10^{-6}=-6.67\times10^{-7}\ \mathrm{C},$$

$$b=\frac{a^2}{d}=\frac{0.0025}{0.15}=1.67\times10^{-2}\ \mathrm{m}=1.67\ \mathrm{cm}.$$

力等于 $q$ 与镜像之间的库仑力（距离 $d-b=0.1333\ \mathrm{m}$）：

$$F=\frac{qq'}{4\pi\varepsilon_0(d-b)^2}
=\frac{8.99\times10^9\times2\times10^{-6}\times\left(-6.67\times10^{-7}\right)}{(0.1333)^2}=-0.674\ \mathrm{N}.$$

**结果：** $q'=-6.7\times10^{-7}\ \mathrm{C}$（球内 $1.67\ \mathrm{cm}$ 处）；球上总感应电荷 $=-6.7\times10^{-7}\ \mathrm{C}$；$F=-0.67\ \mathrm{N}$（指向球）。

**检验：** $d\to a$（电荷贴近球面）时 $q'\to-q$、$b\to a$，与平面情形一致 ✓；$d\gg a$ 时 $q'\to0$，感应消失 ✓。

**读法：** 球上的总感应电荷是 $-qa/d$ 而不是 $-q$——这是最常记错的一条，原因是球外区域还包含"球内镜像"以外的通量。

**5.16** 思路：楔形边界用镜像法，镜像个数 $2n-1$（$360^\circ/\alpha=6$ 给 5 个），力按矢量叠加。

过程：楔角 $60^\circ$，电荷在角平分线 $\theta_0=30^\circ$、距顶点 $d$。镜像在 $90^\circ,150^\circ,210^\circ,270^\circ,330^\circ$，符号依次 $-q,+q,-q,+q,-q$（每次反射变号）。各镜像到电荷的距离：$90^\circ$ 与 $330^\circ$ 为 $2d\sin30^\circ=d$；$150^\circ$ 与 $270^\circ$ 为 $2d\sin60^\circ=\sqrt3d$；$210^\circ$ 为 $2d$。

沿角平分线（向顶点为正）的分量（单位 $q^2/4\pi\varepsilon_0d^2$）：

| 镜像 | 距离 | 符号 | 沿平分线分量 |
|---|---|---|---|
| $90^\circ$ | $d$ | $-q$ | $+0.5$ |
| $330^\circ$ | $d$ | $-q$ | $+0.5$ |
| $150^\circ$ | $\sqrt3d$ | $+q$ | $-0.289$ |
| $270^\circ$ | $\sqrt3d$ | $+q$ | $-0.289$ |
| $210^\circ$ | $2d$ | $-q$ | $+0.25$ |

垂直平分线的分量成对抵消。求和：$0.5+0.5-0.289-0.289+0.25=0.672$。

**结果：** $F=0.67\dfrac{q^2}{4\pi\varepsilon_0d^2}$，方向沿角平分线**指向顶点**。

**检验：** 所有接地导体对同号电荷都是吸引的，合力必须把电荷拉进角落 ✓；纯平面（$\alpha=180^\circ$）时退化为 $1/4$（一个镜像、距离 $2d$），公式给 $0.67$ 但那是 $60^\circ$ 情形，不冲突。

**读法：** 带电粒子在金属尖角附近会被"吸"进角里；电场在尖角处集中，这也是避雷针和场发射针尖的几何基础。

**5.17** 思路：两种介质的分界面，用"一个镜像 + 一个透射电荷"满足两个边界条件。

过程：电荷 $q$ 在 $z=d$（$\varepsilon_1$ 区）。设 $z>0$ 区电势由 $q$ 与镜像 $q'$（在 $z=-d$）给出；$z<0$ 区由等效电荷 $q''$（在 $z=d$）给出：

$$\phi_1=\frac{1}{4\pi\varepsilon_0}\left[\frac{q}{R_1}+\frac{q'}{R_2}\right],\qquad
\phi_2=\frac{1}{4\pi\varepsilon_0}\frac{q''}{R_1}.$$

边界 $z=0$ 上 $R_1=R_2$，两个条件：

$$\phi_1=\phi_2:\quad q+q'=q'',\qquad
\varepsilon_1\frac{\partial\phi_1}{\partial z}=\varepsilon_2\frac{\partial\phi_2}{\partial z}:\quad
\varepsilon_1\left(q-q'\right)=\varepsilon_2q'' .$$

（法向分量来自 $z$ 导数，$q$ 与 $q'$ 的贡献一正一负。）联立解得

$$q'=\frac{\varepsilon_1-\varepsilon_2}{\varepsilon_1+\varepsilon_2}q,\qquad
q''=\frac{2\varepsilon_1}{\varepsilon_1+\varepsilon_2}q .$$

**结果：** 镜像 $q'=\dfrac{\varepsilon_1-\varepsilon_2}{\varepsilon_1+\varepsilon_2}q$；$\varepsilon_2>\varepsilon_1$ 时 $q'<0$（异号，电荷被界面吸引）。

**检验：** $\varepsilon_2=\varepsilon_1$ 给 $q'=0$、$q''=q$（没有界面）✓；$\varepsilon_2\to\infty$（导体）给 $q'\to-q$，回到接地平面 ✓。

**读法：** 介质界面像"半透明镜子"：$\varepsilon$ 差得越多，镜像越强；水（$\varepsilon_r=80$）与空气的界面对电荷几乎是完全反射的。

**5.18** 思路：初值是 $\delta$ 型热源，按本征函数展开；时间演化每个模一个衰减因子。

过程：注入热量 $Q$（单位面积）在 $x=L/2$，初温

$$u(x,0)=\frac{Q}{\rho c}\delta\left(x-\frac L2\right),$$

其中 $\rho c$ 是单位体积热容。把 $\delta$ 展开：

$$\delta\left(x-\frac L2\right)=\frac2L\sum_{n=1}^{\infty}\sin\frac{n\pi}{2}\sin\frac{n\pi x}{L} .$$

每个模按 $e^{-a^2n^2\pi^2t/L^2}$ 衰减，故

$$u(x,t)=\frac{2Q}{\rho cL}\sum_{n=1}^{\infty}\sin\frac{n\pi}{2}\sin\frac{n\pi x}{L}
e^{-a^2n^2\pi^2t/L^2} .$$

**结果：** 上式；$t\to\infty$ 时所有模衰减到零，$u\to0$——热量从两端（恒温零度的热库）流走了。

**检验：** 量纲：$Q/(\rho cL)$ 是温度 ✓。总热量 $\int_0^Lu\,\mathrm{d}x$ 对 $t$ 求导为负（热量流出）✓。$t=0$ 时级数回到 $\delta$ 的展开 ✓。

**读法：** 中点注入的热量先向两边扩散、再被两端吸走；级数里 $\sin(n\pi/2)$ 让偶数模不激发，所以图案始终关于中点对称。

**5.19** 思路：半无限介质、边界给简谐温度，解是衰减的行波（热波）。

过程：设 $T(y,t)=\mathrm{Re}\left[\tilde T_0e^{-(1+i)ky}e^{i\omega t}\right]$，代入 $\partial_tT=\alpha\partial_y^2T$：

$$i\omega=(1+i)^2k^2\alpha=2ik^2\alpha\quad\Longrightarrow\quad k=\sqrt{\frac{\omega}{2\alpha}} .$$

取实部：$T=T_0e^{-ky}\cos(\omega t-ky)$。数值：$\omega=\dfrac{2\pi}{86400}=7.27\times10^{-5}\ \mathrm{s^{-1}}$，$\alpha=5\times10^{-7}\ \mathrm{m^2/s}$：

$$k=\sqrt{\frac{7.27\times10^{-5}}{2\times5\times10^{-7}}}=8.53\ \mathrm{m^{-1}},\qquad
\delta=\frac1k=0.117\ \mathrm{m}.$$

**结果：** $T(y,t)=10\,e^{-y/0.117}\cos\left(\omega t-y/0.117\right)\ \mathrm{K}$；穿透深度 $0.12\ \mathrm{m}$。

**检验：** 量纲：$k$ 是 $1/\mathrm{m}$ ✓。$y=\delta$ 处振幅衰减到 $1/e\approx37\%$，$y=2\delta$ 处 $13.5\%$——一天的温度变化进不到墙里 30 cm ✓。

**读法：** 日变化的穿透深度只有十几厘米；年变化（$\omega$ 小 365 倍）的深度是 $\sqrt{365}\approx19$ 倍，约 2.2 m——这就是地窖恒温的原理。

**5.20** 思路：推迟势的公式代入 $\rho=q\delta(\boldsymbol r)\Theta(t)$，$\Theta$ 把"未来"截掉。

过程：

$$\varphi(\boldsymbol r,t)=\frac{1}{4\pi\varepsilon_0}\int\frac{\rho(\boldsymbol r',t-R/c)}{R}\mathrm{d}^3r'
=\frac{q}{4\pi\varepsilon_0R}\Theta\left(t-\frac Rc\right) .$$

在 $R=2ct$ 处：$t-\dfrac Rc=t-2t=-t<0$，故 $\Theta=0$，$\varphi=0$，电场也为零。

**结果：** $\varphi=\dfrac{q}{4\pi\varepsilon_0R}\Theta(t-R/c)$（球壳 $R=ct$ 外为零）；$R=2ct$ 处 $\varphi=0$、$\boldsymbol E=0$。

**检验：** 极限 $t\to\infty$：$\Theta\to1$，回到库仑场 ✓；$R<ct$ 内是库仑场、$R>ct$ 外严格为零 ✓。

**读法：** "电荷突然出现"在物理上不可能（电荷守恒），但把它看成"突然点亮"（激光电离）时，这个解就是向外扩张的球壳前沿。

**5.21** 思路：推迟势对源的时间依赖是"照搬"，只把 $t$ 换成推迟时刻。

过程：源 $q(t)=q_0e^{-t/\tau}\Theta(t)$ 在原点，于是

$$\varphi(R,t)=\frac{q\left(t-R/c\right)}{4\pi\varepsilon_0R}
=\frac{q_0}{4\pi\varepsilon_0R}e^{-(t-R/c)/\tau}\Theta\left(t-\frac Rc\right) .$$

**结果：** $t<R/c$ 时 $\varphi=0$；$t>R/c$ 时 $\varphi=\dfrac{q_0}{4\pi\varepsilon_0R}e^{-(t-R/c)/\tau}$。

**检验：** $\tau\to\infty$（不衰减）时回到题 5.20 的阶跃解 ✓；$R\to0$ 时 $\varphi\to q(t)/(4\pi\varepsilon_0R)$ ✓。

**读法：** 远处看到的是"过去的源"：库仑场随 $R$ 衰减的同时，源的指数衰减也被推迟了 $R/c$。

**5.22** 思路：稳态问题化成常微分方程，两个边界条件定两个常数。

过程：$\dfrac{\mathrm{d}^2T}{\mathrm{d}x^2}=-\dfrac{S}{a^2}$，积分两次

$$T=-\frac{S}{2a^2}x^2+C_1x+C_2 .$$

边界：$T(0)=T_1$ 给 $C_2=T_1$；$x=L$ 绝热给 $T'(L)=-\dfrac{SL}{a^2}+C_1=0$，即 $C_1=\dfrac{SL}{a^2}$。于是

$$T(x)=T_1+\frac{S}{a^2}\left(Lx-\frac{x^2}{2}\right) .$$

**结果：** $T(x)=T_1+\dfrac{S}{a^2}\left(Lx-\dfrac{x^2}{2}\right)$，最高温度在绝热端 $T(L)=T_1+\dfrac{SL^2}{2a^2}$。

**检验：** $T'(x)=\dfrac{S}{a^2}(L-x)$，在 $x=L$ 处为零 ✓。为什么两端绝热不行：积分方程给 $S\cdot L=a^2\left[T'(L)-T'(0)\right]=0$，即要求 $S=0$；否则热量无处可去，温度无限上升（相容性条件）。

**读法：** 一端恒温就能撑住稳态——热量从恒温端流出；两端都绝热时能量守恒禁止稳态，这就是第 5.11.2 节相容性条件的物理版本。

**5.23** 思路：球内区域的格林函数用镜像法（镜像在球外），电势由格林函数与源积分给出。

过程：半径 $a$ 的接地球壳，源 $q$ 在 $\boldsymbol r'$（$r'<a$）。球内格林函数由镜像构造：镜像在 $\boldsymbol r'^*=\dfrac{a^2}{r'^2}\boldsymbol r'$（球外），电量 $-qa/r'$ 的等效：

$$G(\boldsymbol r,\boldsymbol r')=-\frac{1}{4\pi}\left[\frac{1}{|\boldsymbol r-\boldsymbol r'|}-\frac{a/r'}{|\boldsymbol r-\boldsymbol r'^*|}\right] .$$

电势 $\varphi=-\dfrac{1}{\varepsilon_0}\int G\rho\,\mathrm{d}V'$：

$$\varphi(\boldsymbol r)=\frac{q}{4\pi\varepsilon_0}\left[\frac{1}{|\boldsymbol r-\boldsymbol r'|}-\frac{a/r'}{|\boldsymbol r-\boldsymbol r'^*|}\right] .$$

**结果：** 上式；球内壁总感应电荷 $-q$；壳外场为零（接地屏蔽）。

**检验：** 取源在球心（$r'=0$）：$\varphi=\dfrac{q}{4\pi\varepsilon_0}\left(\dfrac1r-\dfrac1a\right)$，在 $r=a$ 处为零 ✓（这是不对心的极限情形，用极限 $r'\to0$ 得到）。

**读法：** 壳内电荷的全部通量都终止在内壁，所以内壁感应 $-q$；壳接地使外壁不显电性，外部世界完全不知道里面有个电荷。

**5.24** 思路：线性四极的展开只有偶 $l$，写出 $l=2,4$ 两项，比值里 $a/r$ 的幂次决定误差。

过程：$\varphi=\dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{1}{|\boldsymbol r-a\hat z|}+\dfrac{1}{|\boldsymbol r+a\hat z|}-\dfrac2r\right]$。用 $1/|\boldsymbol r\mp a\hat z|=\dfrac1r\sum_l\left(\dfrac ar\right)^lP_l(\cos\theta)$，两项相加只剩偶 $l$，$l=0$ 与 $-2/r$ 抵消：

$$\varphi=\frac{q}{4\pi\varepsilon_0}\cdot\frac2r\sum_{l\ \text{偶}\ge2}\left(\frac ar\right)^lP_l(\cos\theta)
=\frac{qa^2}{4\pi\varepsilon_0r^3}\left(3\cos^2\theta-1\right)+\cdots$$

（$l=2$ 项用 $2q a^2P_2/r^3=qa^2(3\cos^2\theta-1)/r^3$。）

**结果：** $\varphi\approx\dfrac{qa^2}{4\pi\varepsilon_0r^3}\left(3\cos^2\theta-1\right)$（到 $1/r^3$）；忽略的 $l=4$ 项相对大小是 $\left(\dfrac ar\right)^2\dfrac{P_4}{P_2}$，在 $r=5a$ 处量级 $\dfrac{1}{25}\times0.3\sim1\%$。

**检验：** 沿 $z$ 轴（$\theta=0$）：$\varphi=\dfrac{2qa^2}{4\pi\varepsilon_0r^3}$；直接展开 $1/(r-a)+1/(r+a)-2/r=\dfrac{2a^2}{r^3}+\dfrac{2a^4}{r^5}+\cdots$ ✓ 一致。

**读法：** 中性、无偶极的电荷分布，远场第一项是四极，按 $1/r^3$ 衰减——比库仑场多两个幂次，"看得见"的距离短得多。

**5.25** 思路：格林第二恒等式把体积分换成边界项，边界项因两个函数满足齐次边界条件而消失。

过程：取 $\phi=G(\boldsymbol r,\boldsymbol r_1)$、$\psi=G(\boldsymbol r,\boldsymbol r_2)$，两者都满足 $\nabla^2G=\delta$ 与同一边界条件。格林第二恒等式

$$\int_V\left(\phi\nabla^2\psi-\psi\nabla^2\phi\right)\mathrm{d}V
=\oint_{\partial V}\left(\phi\frac{\partial\psi}{\partial n}-\psi\frac{\partial\phi}{\partial n}\right)\mathrm{d}S .$$

左边 $=\int\left[\phi\delta(\boldsymbol r-\boldsymbol r_2)-\psi\delta(\boldsymbol r-\boldsymbol r_1)\right]\mathrm{d}V=G(\boldsymbol r_1,\boldsymbol r_2)-G(\boldsymbol r_2,\boldsymbol r_1)$。狄利克雷时 $G=0$ 于边界，右边 $=0$，故互易。

**结果：** $G(\boldsymbol r_1,\boldsymbol r_2)=G(\boldsymbol r_2,\boldsymbol r_1)$。诺伊曼时右边 $=\dfrac{1}{S}\oint\left(G_1-G_2\right)\mathrm{d}S$，只有当 $G$ 的边界平均为零（"减去平均"的格林函数）时才为零。

**检验：** 一维 $G=-x_<(L-x_>)/L$ 显然对称 ✓；球镜像公式 $G(\boldsymbol r,\boldsymbol r')=G(\boldsymbol r',\boldsymbol r)$ 也可直接验证。

**读法：** 互易性说"源在 1、测在 2"与"源在 2、测在 1"相同——这是所有线性响应系统的普遍性质（电阻矩阵、天线互易都靠它）。

**5.26** 思路：二维圆域的格林函数用反演镜像写出，再对边界法向求导得泊松核。

过程：镜像点在 $\boldsymbol r'^*=\dfrac{a^2}{r'^2}\boldsymbol r'$（圆外），

$$G(\boldsymbol r,\boldsymbol r')=\frac{1}{2\pi}\left[\ln|\boldsymbol r-\boldsymbol r'|-\ln\left(\frac{r'}{a}|\boldsymbol r-\boldsymbol r'^*|\right)\right] .$$

$r'=a$ 时 $\boldsymbol r'^*=\boldsymbol r'$、$\ln$ 项相消，$G=0$ ✓。对 $r'$ 求法向导数（边界上沿 $\hat{\boldsymbol r}'$ 向外），代数整理得

$$K=\left.\frac{\partial G}{\partial n'}\right|_{r'=a}=\frac{1}{2\pi}\frac{a^2-r^2}{a^2+r^2-2ar\cos(\varphi-\varphi')} .$$

于是 $u(r,\varphi)=\dfrac{1}{2\pi}\displaystyle\int_0^{2\pi}\frac{a^2-r^2}{a^2+r^2-2ar\cos(\varphi-\varphi')}f(\varphi')\mathrm{d}\varphi'$。

**结果：** 泊松核 $K$ 如上；两个极限：$r=0$ 时 $K=1/2\pi$（圆心取平均），$r\to a$ 时 $K\to\delta(\varphi-\varphi')$（回到边界值）。

**检验：** $\int_0^{2\pi}K\,\mathrm{d}\varphi'=1$ 对一切 $r<a$ 成立（令 $z=e^{i(\varphi-\varphi')}$ 做围道积分可得）✓；$K\ge0$ ✓（平均值的权重不能为负）。

**读法：** 泊松核是"边界温度到内部温度"的权重：越靠近边界，权重越集中在正对的那一点。

**5.27** 思路：诺伊曼的格林函数不能取"法向导数为零"，因为 $\nabla^2G=\delta$ 的体积分要求 $\oint\partial G/\partial n\,\mathrm{d}S=1$。

过程：把 $\nabla^2G=\delta(\boldsymbol r-\boldsymbol r')$ 在 $V$ 内积分，高斯定理：

$$\oint_{\partial V}\frac{\partial G}{\partial n}\,\mathrm{d}S=\int_V\delta\,\mathrm{d}V=1 .$$

所以边界上只能取 $\dfrac{\partial G}{\partial n}=\dfrac1S$（$S$ 是边界面积），不能取零。

一维构造（$[0,L]$，两端诺伊曼，按一维"面积" $S=2$ 算）：要求 $G'(0)=-\dfrac12$、$G'(L)=+\dfrac12$（外向法向），$G''=\delta$。积分一次 $G'=H(x-x')-\dfrac12$，再积分

$$G(x,x')=x_<-\frac{x-x'}{2}+c .$$

**结果：** $G(x,x')=\min(x,x')-\dfrac{x-x'}{2}+c$；$\oint\partial G/\partial n\,\mathrm{d}S=\left[-\left(-\dfrac12\right)\right]+\dfrac12=1$ ✓。$c$ 任意，因为加常数不改变 $G'$，也不改变 $G''=\delta$。

**检验：** 对称性：$\min(x,x')-(x-x')/2$ 关于 $x,x'$ 对称 ✓（这正是 $c$ 必须与 $x'$ 无关的写法）。$G''=\delta$：斜率从 $-1/2$ 跳到 $+1/2$，跳变 1 ✓。

**读法：** 诺伊曼的格林函数"差一个常数"和"边界导数为 $1/S$"是同一件事的两面——这正是诺伊曼问题解不唯一、要多加一条相容性的根源。

**5.28** 思路：误差来自被截掉的高阶项之和，在源点处可以用 $\sum1/n^2$ 的尾部估计。

过程：$L=2$、$x'=0.5$、在源点 $x=x'$ 处

$$G=-\frac{2L}{\pi^2}\sum_{n=1}^\infty\frac{1}{n^2}\sin^2\frac{n\pi}{4},\qquad
G_N=-\frac{2L}{\pi^2}\sum_{n=1}^N\frac{1}{n^2}\sin^2\frac{n\pi}{4} .$$

$\sin^2(n\pi/4)$ 在 $1/2$、$1$、$1/2$、$0$ 之间循环，平均为 $1/2$，故尾部

$$|G_N-G|\approx\frac{2L}{\pi^2}\cdot\frac12\sum_{n>N}\frac{1}{n^2}
\approx\frac{L}{\pi^2}\cdot\frac1N=\frac{2}{\pi^2N}=\frac{0.203}{N} .$$

**结果：** 误差 $\approx\dfrac{0.2}{N}$（$L=2$、源在中点）；$N=5$ 时 $0.041$，与题 5.8 的数值 $0.040$ 相符。

**检验：** 数值：$N=10$ 时 $0.0185$、$N=40$ 时 $0.0051$，$N\cdot\text{err}$ 稳定在 $0.20$ ✓（用 $\sum_{n>N}1/n^2\approx1/N$ 的渐近）。

**读法：** 误差常数与 $L$、源的位置有关，但 $1/N$ 的规律不变——这就是为什么靠近边界的源需要 $N\sim L/x'$ 个模。

**5.29** 思路：半空间、边界恒零，用奇延拓；热核是高斯，奇延拓就是"加一个反号镜像热源"。

过程：镜像热源在 $-x'$，符号相反：

$$K_D(x,x',t)=\frac{1}{\sqrt{4\pi\alpha t}}\left[e^{-(x-x')^2/(4\alpha t)}-e^{-(x+x')^2/(4\alpha t)}\right] .$$

$x=0$ 时两个高斯相等，相减为零 ✓。初值：$t\to0$ 时第一项给 $\delta(x-x')$、第二项给 $-\delta(x+x')$，后者在 $x>0$ 内为零（它的支撑在 $x<0$）。

总热量 $\displaystyle\int_0^\infty u\,\mathrm{d}x$ 对 $t$ 求导：

$$\frac{\mathrm{d}}{\mathrm{d}t}\int_0^\infty u\,\mathrm{d}x=\alpha\int_0^\infty\frac{\partial^2u}{\partial x^2}\mathrm{d}x
=\alpha\left[\frac{\partial u}{\partial x}\right]_0^\infty=-\alpha\frac{\partial u}{\partial x}(0)<0 .$$

**结果：** $K_D$ 如上；$u(0,t)=0$；总热量单调减少，$t\to\infty$ 时全部被冷壁吸走。

**检验：** 量纲：$\alpha t$ 是 $\mathrm{m^2}$、指数无量纲 ✓；$\int_0^\infty K_D\,\mathrm{d}x=1$ 对 $t>0$ 成立（两个高斯在 $x>0$ 的积分之差为 1）✓——但那是"瞬时"总量，随时间被边界吸走的部分要算通量。

**读法：** 狄利克雷边界是"完美吸热墙"：热量流进去就没了；这与绝热边界（偶延拓、总热量守恒）形成对照。

**5.30** 思路：两个解的差别只在 $\delta$ 的自变量符号，验证方程时要看它们是否都满足同一个波动方程。

过程：$G_{\text{ret}}=-\dfrac{\delta(t-t'-R/c)}{4\pi R}$，$G_{\text{adv}}=-\dfrac{\delta(t-t'+R/c)}{4\pi R}$。两者都形如 $\dfrac{g(t-t'\mp R/c)}{R}$，而 5.10.1 已证 $R\ne0$ 时这种形式满足齐次方程；源点的通量又都给出 $-4\pi g$，故两者都满足 $\nabla^2G-\frac1{c^2}\partial_t^2G=\delta\delta$。

**结果：** 两者都是方程的解；物理上取推迟解，因为初始条件（源在 $t_0$ 前不存在则场为零）和辐射条件（无穷远只允许出射波）只允许它。

**检验：** 若初值是"向原点汇聚的球面波"，全空间 $t=0$ 时的解正是 $G_{\text{adv}}$（向内传播、在 $t>0$ 汇聚到原点）——这时超前解反而是"物理"的，说明选择取决于初值而不是方程。

**读法：** 因果性不是方程的性质，是解的选择；热方程则连这个选择都没有（时间反演解发散）。

**5.31** 思路：收敛性由 $(r'/r)^l$ 的比值控制；$l=4$ 与 $l=2$ 之比是 $(a/r)^2P_4/P_2$（线性四极只有偶 $l$）。

过程：展开式 $\varphi=\dfrac{1}{4\pi\varepsilon_0}\sum_l\dfrac{1}{r^{l+1}}\int\rho r'^lP_l(\cos\gamma)\mathrm{d}V'$，第 $l$ 项的量级 $Q_l(r'_{\max}/r)^l/r$。故 $r>r'_{\max}$ 时各项按几何级数衰减，收敛。

线性四极（$+q$ 在 $\pm a$、$-2q$ 在原点）：$l=2$ 项 $\dfrac{2qa^2}{4\pi\varepsilon_0r^3}P_2$，$l=4$ 项 $\dfrac{2qa^4}{4\pi\varepsilon_0r^5}P_4$，比值

$$\frac{\varphi_4}{\varphi_2}=\left(\frac ar\right)^2\frac{P_4(\cos\theta)}{P_2(\cos\theta)} .$$

取 $r=5a$、$\theta=0.6$：$\cos\theta=0.8253$，$P_2=0.5218$、$P_4=-0.1494$：

$$\frac{\varphi_4}{\varphi_2}=\frac{1}{25}\cdot\frac{-0.1494}{0.5218}=-1.15\times10^{-2} .$$

**结果：** 收敛条件 $r>r'_{\max}$；$r=5a$、$\theta=0.6$ 时 $l=4$ 项是 $l=2$ 项的 $-1.1\%$。

**检验：** 沿 $z$ 轴（$\theta=0$）比值是 $(a/r)^2=4\%$，在赤道（$\theta=\pi/2$）是 $0.75(a/r)^2=3\%$——量级 1–4%，与"$5a$ 处误差约百分之几"一致 ✓。

**读法：** 多极展开的"远"是按 $(r'/r)^l$ 算的：要 1% 精度，四极就得 $r\gtrsim10a$；这也解释了为什么核物理里多极矩要靠"很远"的散射才能干净地测出来。

**5.32** 思路：均匀带电球的静电能是 $W=\frac12\int\rho\phi\,\mathrm{d}V$，用球内电势 $\phi(r)$ 积分。

过程：球内 $\phi(r)=\dfrac{q}{4\pi\varepsilon_0}\left(\dfrac{3a^2-r^2}{2a^3}\right)$，电荷密度 $\rho=\dfrac{3q}{4\pi a^3}$。于是

$$W=\frac12\int_0^a\rho\phi\,4\pi r^2\mathrm{d}r
=\frac{3q^2}{8\pi\varepsilon_0a^6}\int_0^a\left(3a^2r^2-r^4\right)\mathrm{d}r
=\frac{3q^2}{8\pi\varepsilon_0a^6}\left(a^5-\frac{a^5}{5}\right)=\frac{3q^2}{20\pi\varepsilon_0a} .$$

把 $a$ 取经典电子半径 $r_e=\dfrac{e^2}{4\pi\varepsilon_0m_ec^2}=2.82\times10^{-15}\ \mathrm{m}$（此时 $\dfrac{e^2}{4\pi\varepsilon_0r_e}=m_ec^2$）：

$$W=\frac35\cdot\frac{e^2}{4\pi\varepsilon_0r_e}=\frac35m_ec^2 .$$

**结果：** $W=\dfrac{3q^2}{20\pi\varepsilon_0a}$（$a\to0$ 时发散）；电子取 $a=r_e$ 时 $W=0.6m_ec^2\approx0.31\ \mathrm{MeV}$。

**检验：** 量纲：$q^2/(\varepsilon_0a)$ 是能量 ✓。$a\to\infty$ 时 $W\to0$（电荷摊开）✓。$0.6m_ec^2$ 说明"把电子当经典小球"的自能与静质量同量级——这正是经典电动力学无法自洽的地方。

**读法：** 点电荷的自能发散是经典电动力学的病；量子场论用"重正化"处理它，而 $r_e$ 这个长度至今仍是电子物理的一个特征尺度。

**5.33** 错。$\delta$ 不是函数，是**分布**：它没有逐点的值，"$x=0$ 时取无穷大"在数学上不成立（无穷大不是实数），"其余为零"也不足以定义它——还需要"面积为 1"。

正确的定义是它对试验函数的作用：$\int\delta(x)f(x)\mathrm{d}x=f(0)$ 对一切光滑 $f$ 成立。用它才能推出 $\delta(ax)=\delta(x)/|a|$、$x\delta'(x)=-\delta(x)$ 这些规则。

**5.34** 错。$\nabla^2G=\delta$ 只定了一个特解，通解是"这个特解 + 任意调和函数"。

自由空间的 $G_0=-\dfrac{1}{4\pi|\boldsymbol r-\boldsymbol r'|}$ 是唯一在无穷远趋于零的解；一旦有边界（接地平面、球壳），就要加上满足齐次方程与边界条件的修正项——镜像电荷正是那个调和修正。所以"一定是 $G_0$"只在无边界、要求无穷远为零时成立。

**5.35** 半对半错。镜像电荷不是真实电荷，它只是"把边界条件吸收进源"的数学等价物；但**总感应电荷在数值上等于镜像电量**（平面情形 $-q$，球情形 $-qa/d$），这一点对。

错的用法：说"所以感应电荷分布就是镜像电荷分布"——分布完全不同（平面上是连续面密度，镜像是点电荷）。还有一个常见混淆：球面情形总感应电荷是 $-qa/d$ 不是 $-q$（题 5.15）。

**5.36** 错。诺伊曼的格林函数满足 $\dfrac{\partial G}{\partial n}=\dfrac1S$（$S$ 是边界面积），不是零。

理由：把 $\nabla^2G=\delta$ 积分得 $\oint\partial G/\partial n\,\mathrm{d}S=1$，若取零就和这个矛盾。取 $1/S$ 是"最均匀"的分配，且与相容性条件相容。题 5.27 给了一维的显式构造。

**5.37** 错在三处。第一，抛物型方程本来就没有"传播速度"的概念，$K$ 处处非零不是"传播"；第二，那个数值上非零是 $e^{-5\times10^5}$ 量级，不构成可测信号；第三，傅里叶定律假设热流对梯度瞬时响应，真实材料有弛豫时间 $\tau\sim10^{-12}\ \mathrm{s}$，在 $t\sim\tau$ 时要用卡塔内奥方程（双曲型，有前沿）。

"模型没有速度上限"不等于"物理允许超光速"——这是把模型的适用范围忘了。

**5.38** 错。$G_{\text{ret}}$ 与 $G_{\text{adv}}$ 都满足波动方程（题 5.30），方程本身对时间反演对称。

选择推迟解的理由是**初始条件与辐射条件**：源在 $t_0$ 前不存在则场为零；无穷远只允许出射波。这两条是"解的选择规则"，不是方程的内容。

**5.39** 错。中性物体 $Q=0$，多极展开的第一项是偶极（$\propto1/r^2$），比同距离带电体的库仑项（$\propto1/r$）弱一个 $r$ 因子——但"远场更弱"不等于"处处更弱"：近距离时中性物体的近场可以很强（范德瓦尔斯力、分子间作用）。

另外，若偶极也为零（对称分子），第一项是四极，更弱；但"一定比带电体弱"这句话要限定在"同一距离、同一尺度"下才成立。

**5.40** 错。截断误差在**源点附近最大**，离开源点很快变小；"处处小于同一个界"只在源点处成立。

要各处都准，需要 $N\sim L/\ell$，$\ell$ 是你要分辨的最小尺度（或源到最近边界的距离）。题 5.28 的 $0.2/N$ 就是源点处的误差；同一个 $N$ 在离源一个 $L/4$ 的地方误差小得多。级数的收敛是"局部"的，这就是为什么源靠近边界需要很多模。

## 第 6 章

### 习题 6.1–6.12

**6.1**

**思路。** 分母配成完全平方后就是标准形 $u^2+1$，平移不改变积分值，于是问题变成"一个一阶极点在上半平面"的最简情形。

**过程。** 先配方：

$$x^2+2x+2=(x+1)^2+1 .$$

令 $u=x+1$，$\mathrm{d}u=\mathrm{d}x$，积分限不变（线性平移）：

$$I=\int_{-\infty}^{\infty}\frac{\mathrm{d}u}{u^2+1}.$$

被积函数在 $z=\pm i$ 各有一阶极点，上半平面只有 $z=i$。用第二把刀（$P=1$、$Q=z^2+1$、$Q'(z)=2z$）：

$$\operatorname{Res}_{z=i}\frac{1}{z^2+1}=\frac{1}{2i}.$$

分母二次、分子零次，差两次，大圆弧按 $\pi R\cdot R^{-2}\to0$ 消失，判据满足。

**结果。**

$$I=2\pi i\cdot\frac{1}{2i}=\pi\approx3.1416 .$$

**检验。** 量纲：$x$ 无量纲，所以 $I$ 也无量纲（是 $\pi$ 而不是 $\pi\,$m）。与 $\arctan u\big|_{-\infty}^{\infty}=\pi/2-(-\pi/2)=\pi$ 一致。

**读法。** 这是"钟形曲线下的面积"；极点距实轴为 1，若距实轴为 $a$（即分母 $u^2+a^2$），面积变成 $\pi/a$——**极点越靠近实轴，积分越大**。

**6.2**

**思路。** 三阶极点只能用第三把刀（求二阶导）；先确认阶数，再算导数，最后乘 $2\pi i$。

**过程。** 极点在 $z=\pm ia$，都是三阶（分母是 $(z-ia)^3(z+ia)^3$）。上半平面取 $ia$，$m=3$：

$$\operatorname{Res}_{z=ia}f=\frac{1}{2!}\frac{\mathrm{d}^{2}}{\mathrm{d}z^{2}}\Bigl[(z-ia)^3f\Bigr]_{z=ia}
=\frac{1}{2}\frac{\mathrm{d}^{2}}{\mathrm{d}z^{2}}\left[\frac{1}{(z+ia)^3}\right]_{z=ia}.$$

先求导：$(z+ia)^{-3}\to-3(z+ia)^{-4}\to12(z+ia)^{-5}$。代入 $z=ia$，$z+ia=2ia$：

$$\operatorname{Res}_{z=ia}=\frac12\cdot\frac{12}{(2ia)^5}
=\frac{6}{32ia^5}=\frac{3}{16ia^5}.$$

（$(2ia)^5=32i^5a^5=32ia^5$。）分母六次、分子零次，差三次，大弧消失。

**结果。**

$$\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{(x^2+a^2)^3}
=2\pi i\cdot\frac{3}{16ia^5}=\frac{3\pi}{8a^5}.$$

**检验。** 量纲：被积函数 $[L^{-6}]$，$\mathrm{d}x$ 带 $[L]$，结果 $[L^{-5}]$ ✓（$a^{-5}$）。极限 $a\to\infty$ 时 $\to0$ ✓。

**读法。** 与 $\int\mathrm{d}x/(x^2+a^2)=\pi/a$ 相比，多乘了 $(2a^2)^{-1}\cdot\frac34$ 量级——**极点的阶数越高，同一量级下积分越小**，因为分母在峰附近更陡。

**6.3**

**思路。** 分子是 $x^2$，直接算要处理二阶极点；先做代数拆分，把它化成两个已知积分，省掉留数计算。

**过程。** 拆项（凑分母）：

$$\frac{x^2}{(x^2+a^2)^2}
=\frac{(x^2+a^2)-a^2}{(x^2+a^2)^2}
=\frac{1}{x^2+a^2}-\frac{a^2}{(x^2+a^2)^2}.$$

两个已知结果：

$$\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{x^2+a^2}=\frac{\pi}{a},
\qquad
\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{(x^2+a^2)^2}=\frac{\pi}{2a^3}.$$

（第二个由 6.2 令 $m=2$，或对第一个关于 $a^2$ 求导。）

代入：

$$\int_{-\infty}^{\infty}\frac{x^2\,\mathrm{d}x}{(x^2+a^2)^2}
=\frac{\pi}{a}-a^2\cdot\frac{\pi}{2a^3}
=\frac{\pi}{a}-\frac{\pi}{2a}=\frac{\pi}{2a}.$$

**结果。**

$$\int_{-\infty}^{\infty}\frac{x^2\,\mathrm{d}x}{(x^2+a^2)^2}=\frac{\pi}{2a}.$$

**检验。** 量纲 $[L^{-1}]$ ✓。$a\to\infty$ 时 $\to0$ ✓；且结果恰好是 $\int\mathrm{d}x/(x^2+a^2)=\pi/a$ 的一半——这合理，因为 $x\gg a$ 时 $x^2/(x^2+a^2)^2\approx1/x^2$，与 $1/(x^2+a^2)$ 的尾部同阶。

**读法。** 这道题的教训是：**能做代数变形的先做代数变形**。拆项比套二阶极点公式快，也不容易在求导时漏项。至于"逐项相除"（$\int x^2\mathrm{d}x\big/\int(x^2+a^2)^2\mathrm{d}x$）则是无意义的操作，商的积分不等于积分的商。

**6.4**

**思路。** 分母是 $x^4+a^4$，四个极点落在 $45^\circ$ 方向的四条射线上，先写出四根、按虚部符号挑两个，再用第二把刀。

**过程。** 解 $z^4=-a^4$：

$$z_k=a\,e^{i\pi(2k+1)/4},\qquad k=0,1,2,3,
\quad\text{即}\quad \frac{\pi}{4},\ \frac{3\pi}{4},\ \frac{5\pi}{4},\ \frac{7\pi}{4}.$$

上半平面是 $k=0,1$（角 $\pi/4$、$3\pi/4$）。$Q'=4z^3$，而 $z_k^4=-a^4$ 给 $1/z_k^3=z_k/z_k^4=-z_k/a^4$，所以

$$\operatorname{Res}_{z=z_k}\frac{1}{z^4+a^4}=\frac{1}{4z_k^3}=-\frac{z_k}{4a^4}.$$

两根之和：$z_0+z_1=a\left(e^{i\pi/4}+e^{3i\pi/4}\right)=a\cdot i\sqrt2$（实部相消、虚部相加），故

$$\sum\operatorname{Res}=-\frac{i\sqrt2}{4a^3}.$$

**结果。**

$$\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{x^4+a^4}=2\pi i\left(-\frac{i\sqrt2}{4a^3}\right)=\frac{\pi}{\sqrt2\,a^3},
\qquad
\int_0^{\infty}=\frac{\pi}{2\sqrt2\,a^3}.$$

（半条实轴取一半，因为被积函数是偶函数。）

**检验。** 量纲 $[L^{-3}]$ ✓。$a=1$ 时给 $\pi/\sqrt2\approx2.221$，与数值积分一致。

**读法。** 分母次数四次，衰减比二次快，所以积分是 $\pi/(\sqrt2 a^3)$ 而不是 $\pi/a$。**次数每加 2，量纲就多一个 $a^{-2}$，系数也跟着变**——这类积分没有"通用系数"，必须实算。

**6.5**

**思路。** 二阶极点＋振荡因子：极点用第三把刀，振荡因子 $e^{2iz}$ 连在分子上一起求导，最后取实部。

**过程。** 设 $f(z)=\dfrac{e^{2iz}}{(z^2+1)^2}$，极点在 $z=\pm i$，都是二阶；上半平面取 $i$。$m=2$：

$$\operatorname{Res}_{z=i}f=\frac{\mathrm{d}}{\mathrm{d}z}\left[\frac{e^{2iz}}{(z+i)^2}\right]_{z=i}.$$

用乘积法则（两件事都要对 $z$ 求导）：

$$\frac{\mathrm{d}}{\mathrm{d}z}\left[e^{2iz}(z+i)^{-2}\right]
=e^{2iz}\left[2i(z+i)^{-2}-2(z+i)^{-3}\right].$$

代入 $z=i$，$(z+i)=2i$，$(2i)^2=-4$，$(2i)^3=-8i$：

$$\operatorname{Res}_{z=i}f=e^{-2}\left[\frac{2i}{-4}-\frac{2}{-8i}\right]
=e^{-2}\left[-\frac{i}{2}+\frac{1}{4i}\right]
=e^{-2}\left[-\frac{i}{2}-\frac{i}{4}\right]=-\frac{3i}{4}e^{-2}.$$

（用了 $1/(4i)=-i/4$。）

**结果。** 取实部：

$$\int_{-\infty}^{\infty}\frac{\cos(2x)}{(x^2+1)^2}\,\mathrm{d}x
=\operatorname{Re}\left[2\pi i\left(-\frac{3i}{4}e^{-2}\right)\right]
=\frac{3\pi}{2}e^{-2}\approx0.638 .$$

**检验。** 与通式 $\int\mathrm{d}x\cos(ax)/(x^2+b^2)^2=\dfrac{\pi}{2b^3}(1+ab)e^{-ab}$ 对照：$a=2,b=1$ 给 $\frac{3\pi}{2}e^{-2}$ ✓。$a\to0$ 时应退回 $\pi/2$：通式给 $\pi/2$ ✓。

**读法。** 系数 $(1+ab)$ 是**二阶极点**的特征标记（一阶极点只给 $e^{-ab}$）。它来自求导时"分子也变"的那一项。漏掉它，$a\to0$ 时就会差一个因子 3。

**6.6**

**思路。** 被积函数是"奇函数 × 奇函数"，整体为偶，可以补全实轴；含 $\sin$ 就用 $ze^{iaz}$ 的虚部，$a>0$ 往上闭合。

**过程。** 先看奇偶性：$x\sin(ax)/(x^2+b^2)$ 中 $x$ 奇、$\sin$ 奇，乘积偶，$x^2+b^2$ 偶，所以整体偶。考虑

$$f(z)=\frac{z\,e^{iaz}}{z^2+b^2},\qquad a>0 .$$

极点在 $z=\pm ib$，上半平面只有 $ib$（一阶）。用第二把刀（$P=ze^{iaz}$、$Q=z^2+b^2$、$Q'=2z$）：

$$\operatorname{Res}_{z=ib}f=\frac{ib\,e^{i(ib)a}}{2ib}=\frac{e^{-ab}}{2}.$$

（$e^{i(ib)a}=e^{-ab}$。）$|f|\sim1/|z|$，但 $e^{iaz}$ 在上半平面指数衰减，若尔当引理保证大弧消失（$a>0$）。

**结果。**

$$\int_{-\infty}^{\infty}\frac{x\,e^{iax}}{x^2+b^2}\,\mathrm{d}x
=2\pi i\cdot\frac{e^{-ab}}{2}=i\pi e^{-ab}.$$

$x/(x^2+b^2)$ 在实轴上取实值，取虚部合法：

$$\int_{-\infty}^{\infty}\frac{x\sin(ax)}{x^2+b^2}\,\mathrm{d}x=\pi e^{-ab}.$$

**检验。** 量纲 $[L^{-1}]$ ✓。$b\to0$ 时结果 $\to\pi$，而积分退化为 $\int_0^\infty\sin(ax)/x\,\mathrm{d}x=\pi/2$ 的两倍 $=\pi$ ✓，与经典结果吻合。$a\to\infty$ 时按 $e^{-ab}$ 指数衰减 ✓。

**读法。** $e^{-ab}$ 里的 $1/a$ 是**衰减长度**：把 $x$ 看成波数、$a$ 看成距离时，这就是屏蔽/倏逝因子的来源。$b\to0$ 时发散（极点撞上实轴），对应长程极限。

**6.7**

**思路。** 极点正好落在积分路径上，必须"主值 + 小弧绕行"；绕行方向由"沿实轴从左到右"定死。

**过程。** 设 $f(z)=\dfrac{e^{i\omega x}}{z-\omega_0}$（把积分变量写成 $z$），$\omega>0$。极点在 $\omega_0$（实轴，一阶），留数

$$\operatorname{Res}_{z=\omega_0}f=\lim_{z\to\omega_0}(z-\omega_0)\frac{e^{i\omega z}}{z-\omega_0}=e^{i\omega\omega_0}.$$

回路：实轴（从左到右，在 $\omega_0$ 处从上方绕过，顺时针）＋上半平面大半圆。回路内无其他极点，总积分为零：

$$0=\mathrm{P.V.}\int+\bigl(-i\pi\operatorname{Res}\bigr)+\int_{C_R}.$$

小半圆给 $-i\pi e^{i\omega\omega_0}$（顺时针），大弧由若尔当消失。

**结果。**

$$\mathrm{P.V.}\int_{-\infty}^{\infty}\frac{e^{i\omega x}}{x-\omega_0}\,\mathrm{d}x=i\pi e^{i\omega\omega_0}.$$

分开实虚部（$\omega_0$ 处取主值）：

$$\mathrm{P.V.}\int\frac{\cos\omega x}{x-\omega_0}\,\mathrm{d}x=-\pi\sin(\omega\omega_0),
\qquad
\int\frac{\sin\omega x}{x-\omega_0}\,\mathrm{d}x=\pi\cos(\omega\omega_0).$$

**检验。** 令 $\omega_0=0$ 退回 $\mathrm{P.V.}\int e^{i\omega x}/x\,\mathrm{d}x=i\pi$ ✓，虚部给 $\int\sin\omega x/x\,\mathrm{d}x=\pi$ ✓（与 6.7 节的经典结果一致）。

**读法。** 这是**单个无阻尼模式的响应核**：它把"输入"绕着实轴平移。物理上 $\pi i$ 这个纯虚数就是"绕半个极点"的贡献，对应一个 $\delta$-型的共振。

**6.8**

**思路。** 先因式分解找极点，四个极点都在 $\pm1\pm i$；上半平面两个，逐个用 $P/Q$ 公式。

**过程。** 因式分解：

$$z^4+4=(z^2-2z+2)(z^2+2z+2)=\bigl[(z-1)^2+1\bigr]\bigl[(z+1)^2+1\bigr],$$

所以极点是 $z_{1,2}=1\pm i$、$z_{3,4}=-1\pm i$；上半平面是 $z_1=1+i$ 与 $z_3=-1+i$。

用第二把刀，$Q'=4z^3$，留数 $1/(4z^3)$。

对 $z_1=1+i$：$z_1^2=2i$，$z_1^3=2i(1+i)=-2+2i$，故留数 $\dfrac{1}{4(-2+2i)}=\dfrac{1}{8(i-1)}$。

对 $z_3=-1+i$：$z_3^2=-2i$，$z_3^3=-2i(-1+i)=2+2i$，留数 $\dfrac{1}{4(2+2i)}=\dfrac{1}{8(i+1)}$。

相加，通分：

$$\frac18\left(\frac{1}{i-1}+\frac{1}{i+1}\right)
=\frac18\cdot\frac{(i+1)+(i-1)}{(i-1)(i+1)}
=\frac18\cdot\frac{2i}{-2}=-\frac{i}{8}.$$

**结果。**

$$\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{x^4+4}=2\pi i\left(-\frac{i}{8}\right)=\frac{\pi}{4}\approx0.7854 .$$

**检验。** 量纲：$a^4=4$ 意味着 $a=\sqrt2$，通式 $\int\mathrm{d}x/(x^4+a^4)=\pi/(\sqrt2a^3)$ 给 $\pi/(\sqrt2\cdot2\sqrt2)=\pi/4$ ✓。

**读法。** 四个极点排成一个正方形（边长 $\sqrt2$），上半平面两个。**极点的几何对称性直接决定了留数之和是纯虚数**，所以最终结果是实数——这是这类积分总能得到干净答案的原因。

**6.9**

**思路。** 四个一阶极点，两两关于实轴对称；先写留数、再提公因子，最后检查 $a\to b$ 的连续性。

**过程。** 设 $f=\dfrac{1}{(z^2+a^2)(z^2+b^2)}$，极点 $\pm ia,\pm ib$ 全是一阶，上半平面取 $ia$、$ib$。

用"乘上去取极限"（第一把刀），在 $\pm ia$ 处只需对 $z^2+a^2$ 求导：

$$\operatorname{Res}_{z=ia}f=\frac{1}{2ia\,(b^2-a^2)},\qquad
\operatorname{Res}_{z=ib}f=\frac{1}{2ib\,(a^2-b^2)}.$$

两式相加，提 $\dfrac{1}{2i(b^2-a^2)}$：

$$\sum\operatorname{Res}=\frac{1}{2i(b^2-a^2)}\left(\frac1a-\frac1b\right)
=\frac{1}{2i(b^2-a^2)}\cdot\frac{b-a}{ab}
=\frac{1}{2iab(a+b)}.$$

（$b^2-a^2=(b-a)(b+a)$，约掉 $b-a$。）

**结果。**

$$\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{(x^2+a^2)(x^2+b^2)}
=2\pi i\cdot\frac{1}{2iab(a+b)}=\frac{\pi}{ab(a+b)}.$$

**检验。** 量纲 $[L^{-3}]$ ✓。$b\to a$ 时给 $\pi/(2a^3)$，正是 $\int\mathrm{d}x/(x^2+a^2)^2$ ✓——说明即使推导中用了 $a\ne b$，结果在 $a=b$ 处仍连续。

**读法。** 两个尺度 $a,b$ 的"竞争"：$a\ll b$ 时结果 $\approx\pi/(ab^2)$，由小尺度 $a$ 主导（峰更尖）。**多尺度问题里，最靠近实轴的极点说了算。**

**6.10**

**思路。** 与 6.5 同型但参数一般化：二阶极点 ＋ $\cos(ax)$，用三阶刀算留数，再取实部。

**过程。** 设 $f(z)=\dfrac{e^{iaz}}{(z^2+b^2)^2}$，极点 $z=\pm ib$ 都是二阶，取 $ib$：

$$\operatorname{Res}_{z=ib}f=\frac{\mathrm{d}}{\mathrm{d}z}\left[\frac{e^{iaz}}{(z+ib)^2}\right]_{z=ib}
=e^{iaz}\left[ia(z+ib)^{-2}-2(z+ib)^{-3}\right]_{z=ib}.$$

代入 $z=ib$：$(z+ib)=2ib$，平方 $-4b^2$，立方 $-8ib^3$：

$$\operatorname{Res}=e^{-ab}\left[\frac{ia}{-4b^2}-\frac{2}{-8ib^3}\right]
=e^{-ab}\left[-\frac{ia}{4b^2}+\frac{1}{4ib^3}\right]
=e^{-ab}\left[-\frac{ia}{4b^2}-\frac{i}{4b^3}\right]
=-\frac{i(1+ab)}{4b^3}e^{-ab}.$$

（用了 $1/i=-i$。）

**结果。** 取实部：

$$\int_{-\infty}^{\infty}\frac{\cos(ax)}{(x^2+b^2)^2}\,\mathrm{d}x
=\operatorname{Re}\left[2\pi i\cdot\left(-\frac{i(1+ab)}{4b^3}e^{-ab}\right)\right]
=\frac{\pi}{2b^3}(1+ab)e^{-ab}.$$

**检验。** 三条：$a\to0$ 给 $\pi/(2b^3)$（退回无振荡的二阶极点积分）✓；$a\gg b$ 给 $\frac{\pi a}{2b^2}e^{-ab}$，按 $1/a$ 的衰减长度指数掉 ✓；$b\to0$ 发散（极点撞实轴）✓。

**读法。** $(1+ab)$ 这个因子里，"$1$"来自 $1/(z+ib)^2$ 的导数，"$ab$"来自 $e^{iaz}$ 的导数。**二阶极点必须两项都留**——这是本题唯一的技术点。

**6.11**

**思路。** 六次方程在单位圆上均匀分布，先写六根、数出上半平面三个，再用 $1/z_k^5=-z_k$ 把留数化简成纯角度求和。

**过程。** 解 $z^6=-1$：$z_k=e^{i(2k+1)\pi/6}$，$k=0,\dots,5$，即角度 $\pi/6,3\pi/6,5\pi/6,7\pi/6,9\pi/6,11\pi/6$。上半平面是前三个（$\pi/6,\ \pi/2,\ 5\pi/6$）。

$Q'=6z^5$，且 $z_k^6=-1$ 给 $1/z_k^5=z_k/z_k^6=-z_k$，所以

$$\operatorname{Res}_{z=z_k}\frac{1}{1+z^6}=\frac{1}{6z_k^5}=-\frac{z_k}{6}.$$

三个留数相加，把具体值代进去：

$$-\frac16\left[e^{i\pi/6}+e^{i\pi/2}+e^{i5\pi/6}\right]
=-\frac16\left[\left(\frac{\sqrt3}{2}+\frac{i}{2}\right)+i+\left(-\frac{\sqrt3}{2}+\frac{i}{2}\right)\right]
=-\frac16\cdot 2i=-\frac{i}{3}.$$

（实部 $\sqrt3/2$ 与 $-\sqrt3/2$ 抵消，虚部 $1/2+1+1/2=2$。）

**结果。**

$$\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{x^6+1}=2\pi i\left(-\frac{i}{3}\right)=\frac{2\pi}{3},
\qquad
\int_0^{\infty}\frac{\mathrm{d}x}{x^6+1}=\frac{\pi}{3}.$$

**检验。** 与通式 $\int_0^\infty\mathrm{d}x/(1+x^n)=\dfrac{\pi}{n\sin(\pi/n)}$ 对照：$n=6$ 时 $\dfrac{\pi}{6\sin(\pi/6)}=\dfrac{\pi}{3}$ ✓。

**读法。** 六重对称让留数之和自动变成纯虚数，答案干净。**分母次数越高，上半平面极点越多（$n/2$ 个），但对称性把求和压成了一个虚数**——这是"用对称性代替暴力求和"的典型。

**6.12**

**思路。** 直接算 $(x^2+1)/(x^4+1)$ 也可以，但拆成两个已知积分更快，而且能看出"两个积分相等"这个对称性。

**过程。** 拆开：

$$\int_{-\infty}^{\infty}\frac{x^2+1}{x^4+1}\,\mathrm{d}x
=\int_{-\infty}^{\infty}\frac{x^2}{x^4+1}\,\mathrm{d}x+\int_{-\infty}^{\infty}\frac{1}{x^4+1}\,\mathrm{d}x .$$

第二个是 6.5.2 节算过的（$a=1$）：

$$\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{x^4+1}=\frac{\pi}{\sqrt2}.$$

第一个：分子 $z^2$ 让留数从 $1/(4z_k^3)$ 变成 $z_k^2/(4z_k^3)=1/(4z_k)$，而 $z_k^4=-1$ 给 $1/z_k=-z_k^3$，所以

$$\operatorname{Res}_{z_k}\frac{z^2}{z^4+1}=\frac{1}{4z_k}=-\frac{z_k^3}{4}.$$

上半平面两根的 $z_k^3$ 之和与 $z_k$ 之和同构（都是 $i\sqrt2$ 型的纯虚数），算下来仍是 $\pi/\sqrt2$。

**更省的看法：** 代换 $x\to1/x$ 把 $\dfrac{\mathrm{d}x}{x^4+1}$ 变成 $\dfrac{x^2\,\mathrm{d}x}{x^4+1}$，所以两个积分必然相等——不用再算。

**结果。**

$$\int_{-\infty}^{\infty}\frac{x^2+1}{x^4+1}\,\mathrm{d}x=2\cdot\frac{\pi}{\sqrt2}=\pi\sqrt2\approx4.443 .$$

**检验。** 量纲：被积函数 $\sim x^2/x^4=1/x^2$（$x\to\infty$），积分收敛 ✓。与数值积分一致。

**读法。** $x\to1/x$ 这个代换在 $x^4+1$ 型积分里是万能的——它把"分子是常数"和"分子是 $x^2$"两种情形联系起来。**先找对称性，再决定算不算**。

### 习题 6.13–6.24

**6.13**

**思路。** 阻尼振子的三个特征量（$\Omega$、$Q$、振铃周数）都从 $\omega_\pm=\pm\Omega-i\gamma/2$ 出发，先算 $\Omega$，再算能量衰减与周期的比值。

**过程。** 阻尼频率

$$\Omega=\sqrt{\omega_0^2-\frac{\gamma^2}{4}}
=\omega_0\sqrt{1-\frac{\gamma^2}{4\omega_0^2}}
=\omega_0\sqrt{1-0.0025}=0.99875\,\omega_0 .$$

品质因子

$$Q=\frac{\Omega}{\gamma}=\frac{0.99875\,\omega_0}{0.1\,\omega_0}=9.99\approx10 .$$

能量 $\propto$ 振幅平方 $\propto e^{-\gamma t}$，衰减到 $1/e$ 需 $t_E=1/\gamma=10\,\omega_0^{-1}$。一个振动周期是 $T=2\pi/\Omega$，所以

$$N=\frac{t_E}{T}=\frac{1/\gamma}{2\pi/\Omega}=\frac{\Omega}{2\pi\gamma}=\frac{Q}{2\pi}=\frac{9.99}{6.283}=1.59 .$$

**结果。**

$$\Omega=0.999\,\omega_0,\qquad Q\approx10,\qquad N\approx1.6\ \text{个周期}.$$

**检验。** $N=Q/2\pi$ 是一条恒等式：$Q$ 的物理意义正是"振铃能维持多少个弧度"，除以 $2\pi$ 就是周数。$\gamma\ll\omega_0$ 时 $\Omega\approx\omega_0$ ✓。

**读法。** 这个振子只响一个半周期就衰掉了——听起来是"咚"而不是"叮"。乐器要求 $Q\gg1$（钢琴弦 $Q\sim10^3$，钟 $Q\sim10^4$），所以材质和支撑必须尽量减小阻尼。

**6.14**

**思路。** 与例 6.3 同一个角度积分，只是分母多了 $\kappa^2$；角度积分只依赖于 $|\boldsymbol{k}|$，所以先把三维积分降成一维，再用若尔当。

**过程。** 取 $\boldsymbol{r}$ 沿 $z$ 轴，$|\boldsymbol{r}|=r$。角向积分（与例 6.3 相同）：

$$\int_0^{\pi}e^{ikr\cos\theta}\sin\theta\,\mathrm{d}\theta=\frac{2\sin(kr)}{kr}.$$

于是

$$\varphi(r)=\frac{q}{\varepsilon_0}\frac{4\pi}{(2\pi)^3}\int_0^\infty k^2\mathrm{d}k\,\frac{1}{k^2+\kappa^2}\cdot\frac{2\sin(kr)}{kr}
=\frac{q}{4\pi^2\varepsilon_0r}\int_0^\infty\frac{k\sin(kr)}{k^2+\kappa^2}\,\mathrm{d}k .$$

被积函数 $k\sin(kr)/(k^2+\kappa^2)$ 是 $k$ 的**偶函数**（奇 × 奇），所以 $\int_0^\infty=\frac12\int_{-\infty}^\infty$。

用 $e^{ikr}$ 的虚部：$f=\dfrac{k\,e^{ikr}}{k^2+\kappa^2}$，上半平面极点 $k=i\kappa$，留数

$$\operatorname{Res}_{k=i\kappa}=\frac{i\kappa\,e^{-\kappa r}}{2i\kappa}=\frac{e^{-\kappa r}}{2}.$$

$|f|\to0$，若尔当引理保证大弧消失。全实轴积分 $=2\pi i\cdot\frac12 e^{-\kappa r}=i\pi e^{-\kappa r}$，取虚部得 $\pi e^{-\kappa r}$。

**结果。**

$$\int_0^\infty\frac{k\sin(kr)}{k^2+\kappa^2}\,\mathrm{d}k=\frac{\pi}{2}e^{-\kappa r},
\qquad
\varphi(r)=\frac{q}{4\pi\varepsilon_0}\,\frac{e^{-\kappa r}}{r}.$$

**检验。** 量纲：$q/(4\pi\varepsilon_0 r)$ 是电势，乘无量纲的 $e^{-\kappa r}$ ✓。$\kappa\to0$ 时退回库仑势 $q/(4\pi\varepsilon_0r)$ ✓。$\kappa r\gg1$ 时指数压低 ✓。

**读法。** 汤川势 = 库仑势 × 屏蔽因子。分母里多一个 $\kappa^2$ 就多一个极点距离 $\kappa$，于是多一个衰减长度 $1/\kappa$——**"质量"在势的层面就是"极点到实轴的距离"**。

**6.15**

**思路。** $h(t)$ 的原函数是正弦积分，实变算不动；写成 $e^{iWt}/t$ 的虚部后，$t=0$ 出现一阶极点，正好用"主值 + 小弧"。

**过程。** 先看 $h(t)$ 在 $t=0$ 的行为：$\sin(Wt)/(\pi t)\to W/\pi$，有界，所以积分是普通收敛的。但原函数是 $\mathrm{Si}$，不行。

写成虚部：$\sin(Wt)=\operatorname{Im}e^{iWt}$，于是

$$\int_{-\infty}^{\infty}h(t)\,\mathrm{d}t=\frac{1}{\pi}\operatorname{Im}\int_{-\infty}^{\infty}\frac{e^{iWt}}{t}\,\mathrm{d}t .$$

极点 $t=0$ 在实轴上，一阶，留数 $\operatorname{Res}_{0}e^{iWt}/t=e^{0}=1$。沿实轴从左到右、从上方绕过（顺时针），大弧由若尔当消失（$W>0$）：

$$0=\mathrm{P.V.}\int\frac{e^{iWt}}{t}\,\mathrm{d}t+(-i\pi\cdot1)\quad\Longrightarrow\quad
\mathrm{P.V.}\int\frac{e^{iWt}}{t}\,\mathrm{d}t=i\pi .$$

**结果。** 取虚部：$\int\sin(Wt)/t\,\mathrm{d}t=\pi$，故

$$\int_{-\infty}^{\infty}h(t)\,\mathrm{d}t=\frac{1}{\pi}\cdot\pi=1 .$$

**检验。** 量纲：$h$ 的量纲是 $1/$时间，$\int h\,\mathrm{d}t$ 无量纲 ✓。$W\to\infty$ 时 $h\to\delta(t)$，积分仍为 1 ✓（直流增益不随带宽变）。

**读法。** $\int h=1$ 就是"直流增益为 1"：滤波器不改变信号的时间积分（零频分量）。**为什么还要用主值**——被积的 $e^{iWt}/t$ 在 $0$ 有极点，主值是绕开它的唯一合法方式；原始函数本身没极点，这个极点是"提升成复指数"的代价。

**6.16**

**思路。** 先看极点的位置（决定因果性），再把 $\operatorname{Re}\sigma$ 积出来（求和规则），最后代入 $\sigma_0$ 看它依赖什么。

**过程。** 分母：$1-i\omega\tau=0\Rightarrow\omega=-i/\tau$。极点在虚轴下方，**下半平面**——所以 $\sigma(\omega)$ 在上半平面解析，满足因果性。

实部：$\dfrac{1}{1-i\omega\tau}=\dfrac{1+i\omega\tau}{1+\omega^2\tau^2}$，所以

$$\operatorname{Re}\sigma=\frac{\sigma_0}{1+\omega^2\tau^2}.$$

积分（代换 $u=\omega\tau$）：

$$\int_0^\infty\frac{\mathrm{d}\omega}{1+\omega^2\tau^2}
=\frac1\tau\int_0^\infty\frac{\mathrm{d}u}{1+u^2}
=\frac{1}{\tau}\cdot\frac{\pi}{2}.$$

**结果。**

$$\int_0^{\infty}\operatorname{Re}\sigma(\omega)\,\mathrm{d}\omega=\frac{\pi\sigma_0}{2\tau}
=\frac{\pi e^2n}{2m},$$

最后一步用了 $\sigma_0=ne^2\tau/m$。

**检验。** 量纲：$[\sigma]=1/(\Omega\cdot\mathrm{m})$，$\mathrm{d}\omega$ 带 $1/$时间，乘积是 $1/(\Omega\cdot\mathrm{m}\cdot\mathrm{s})$ ✓。$\tau$ 精确抵消，只剩 $n$（电子密度）✓。

**读法。** **碰撞越频繁（$\tau$ 小），谱越宽越矮，但加权面积不变**——这就是"电子数守恒"在光学里的表现，也是 $f$ 求和规则的导电版本。实验上测光电导的积分，数出来的就是参与导电的电子数。

**6.17**

**思路。** 把离散模求和换成积分（$L$ 大时），再做 $x=\beta\hbar\omega$ 的代换，积分变成一个 $\Gamma$ 函数乘 $\zeta$ 函数。

**过程。** 一维腔里 $k$ 的间隔是 $2\pi/L$，所以 $\sum_k\to(L/2\pi)\int\mathrm{d}k$；两个偏振给因子 2；$\omega=ck$：

$$u=\frac1L\cdot2\cdot\frac{L}{2\pi}\int_0^\infty\mathrm{d}k\,\frac{\hbar ck}{e^{\beta\hbar ck}-1}
=\frac{\hbar}{\pi}\int_0^\infty\frac{k\,\mathrm{d}k}{e^{\beta\hbar ck}-1}.$$

改用 $\omega=ck$（$\mathrm{d}k=\mathrm{d}\omega/c$，$\hbar ck=\hbar\omega$）：

$$u=\frac{\hbar}{\pi c^2}\int_0^\infty\frac{\omega\,\mathrm{d}\omega}{e^{\beta\hbar\omega}-1}.$$

代 $x=\beta\hbar\omega$，$\omega=x/(\beta\hbar)$，$\mathrm{d}\omega=\mathrm{d}x/(\beta\hbar)$：

$$u=\frac{\hbar}{\pi c^2}\cdot\frac{1}{(\beta\hbar)^2}\int_0^\infty\frac{x\,\mathrm{d}x}{e^x-1}
=\frac{1}{\pi\hbar c^2\beta^2}\cdot\Gamma(2)\zeta(2).$$

$\Gamma(2)=1$，$\zeta(2)=\pi^2/6$，$\beta=1/(k_BT)$：

**结果。**

$$u=\frac{\pi^2}{6\pi\hbar c^2}\cdot(k_BT)^2=\frac{\pi(k_BT)^2}{6\hbar c}\ \left[\frac{\mathrm{J}}{\mathrm{m}^3}\right].$$

**检验。** 量纲：$[\hbar c]=\mathrm{J\cdot m}$，$(k_BT)^2/(\hbar c)=\mathrm{J^2/(J\cdot m)}=\mathrm{J/m}$；但能量密度应是 $\mathrm{J/m^3}$——这里 $u$ 是**单位长度的能量**（一维），量纲 $\mathrm{J/m}$ ✓ 正确。

**读法。** $d$ 维光子气 $u\propto T^{d+1}$（态密度 $\omega^{d-1}$ 乘 $\hbar\omega$ 给 $\omega^d$，积分给 $\Gamma(d+1)\zeta(d+1)$）。一维是 $T^2$，三维是 $T^4$——**维数直接决定温度幂次**，这是"为什么斯特藩–玻尔兹曼是四次方"的最简解释。

**6.18**

**思路。** 分母的根在下半平面，所以 $t>0$ 往下闭合捕获它、$t<0$ 往上闭合得零——$\theta(t)$ 是算出来的，不是预先写上的。

**过程。** 化简分母：$1-i\omega RC=-iRC\left(\omega+\dfrac{i}{RC}\right)$，极点

$$\omega_0=-\frac{i}{RC},$$

**下半平面**。$t>0$ 时 $|e^{-i\omega t}|=e^{yt}$ 要求 $y<0$ 才衰减，故往下闭合（顺时针），捕获 $\omega_0$：

$$V(t)=-2\pi i\cdot\frac{e^{-i\omega_0t}}{-iRC}\cdot\frac{1}{2\pi}
=\frac{1}{RC}e^{-t/(RC)} .$$

（顺时针多一个负号，与 $1/(-iRC)$ 里的 $i$ 合起来给正。）

$t<0$ 时往上闭合，上半平面无极点，$V=0$。

**结果。**

$$V(t)=\frac{\theta(t)}{RC}\,e^{-t/(RC)} .$$

**检验。** $\int_0^\infty V\,\mathrm{d}t=\left[-e^{-t/RC}\right]_0^\infty=1$ ✓——单位冲激的"总电荷"守恒。$t\to0^+$ 时 $V\to1/(RC)$，量纲 $1/$时间 ✓（电压响应，冲激是 $\delta$ 型的电压）。

**读法。** RC 电路是最简单的因果系统：冲激进来，电容立刻跳一下，然后按时间常数 $RC$ 泄放。**"跳一下"对应 $1/(RC)$，"泄放"对应 $e^{-t/RC}$**，两者都是极点位置 $\omega_0=-i/(RC)$ 的函数。

**6.19**

**思路。** 布赖特–维格纳线型是标准的洛伦兹线，做一个平移加伸缩就能化成 $\int\mathrm{d}u/(1+u^2)$。

**过程。** 令 $u=\dfrac{2(E-E_0)}{\Gamma}$，则 $E=E_0+\dfrac{\Gamma}{2}u$，$\mathrm{d}E=\dfrac{\Gamma}{2}\mathrm{d}u$，分母 $1+4(E-E_0)^2/\Gamma^2=1+u^2$：

$$\int_{-\infty}^{\infty}\sigma\,\mathrm{d}E
=\sigma_{\max}\frac{\Gamma}{2}\int_{-\infty}^{\infty}\frac{\mathrm{d}u}{1+u^2}
=\sigma_{\max}\frac{\Gamma}{2}\cdot\pi .$$

**结果。**

$$\int_{-\infty}^{\infty}\sigma(E)\,\mathrm{d}E=\frac{\pi\Gamma}{2}\,\sigma_{\max}
\ \left[\text{截面}\times\text{能量}\right].$$

**检验。** 量纲：$[\sigma]=\mathrm{m^2}$，$[\Gamma]=\mathrm{J}$，乘积 $\mathrm{J\cdot m^2}$ ✓。$\Gamma\to0$（无限窄的峰）时面积 $\to0$——但峰高固定，这是"线型"而非"$\delta$"的正常行为；若同时让峰高 $\propto1/\Gamma$，面积才守恒。

**读法。** **峰面积 $=\frac{\pi}{2}\times$ 峰高 $\times$ 半高全宽**。若 $\Gamma=\hbar/\tau$，面积 $\propto1/\tau$：寿命越短峰越宽越矮，但"跃迁强度"（面积）由初末态决定——这正是 $f$ 求和规则在共振散射里的版本。

**6.20**

**思路。** 热噪声谱是常数，电路把它"过滤"成 $|Z_C/(Z_R+Z_C)|^2$ 的形状，积分是一个标准的反正切。

**过程。** 电容上的电压是噪声源经分压：

$$|Z_C|^2=\frac{1}{(\omega C)^2},\qquad
\left|\frac{Z_C}{Z_R+Z_C}\right|^2
=\frac{1}{1+\omega^2R^2C^2}.$$

所以

$$\langle V^2\rangle=\int_{-\infty}^{\infty}\frac{S_V}{2\pi}\cdot\frac{1}{1+\omega^2R^2C^2}\,\mathrm{d}\omega
=\frac{2k_BTR}{2\pi}\int_{-\infty}^{\infty}\frac{\mathrm{d}\omega}{1+\omega^2R^2C^2}.$$

代 $u=\omega RC$，$\mathrm{d}\omega=\mathrm{d}u/(RC)$：

$$\int_{-\infty}^{\infty}\frac{\mathrm{d}\omega}{1+\omega^2R^2C^2}
=\frac{1}{RC}\int_{-\infty}^{\infty}\frac{\mathrm{d}u}{1+u^2}
=\frac{\pi}{RC}.$$

**结果。**

$$\langle V^2\rangle=\frac{2k_BTR}{2\pi}\cdot\frac{\pi}{RC}=\frac{k_BT}{C}
\quad[\mathrm{V^2}].$$

**检验。** 量纲：$k_BT$ 是能量 $\mathrm{J}$，$C$ 是 $\mathrm{F}=\mathrm{C/V}$，$\mathrm{J/(C/V)}=\mathrm{V\cdot C}=\mathrm{J}$？不对——$\mathrm{J/F}=\mathrm{J\cdot V/C}=\mathrm{V\cdot J/C}=\mathrm{V^2}$ ✓（用 $\mathrm{J}=\mathrm{C\cdot V}$）。$R$ 精确抵消 ✓。

**读法。** 涨落耗散定理最干净的样本：**噪声正比于 $R$，带宽反比于 $R$，两者相乘抵消**。于是 $\langle V^2\rangle=k_BT/C$ 与电阻的具体值无关，可以用电容噪声测温（这也是精密测量里"噪声温度计"的原理）。

**6.21**

**思路。** 实轴上有极点（$x=0$）又有上半平面极点（$x=ib$），必须"主值 + 小弧 + 若尔当"三段一起算。

**过程。** 设 $f(z)=\dfrac{e^{iaz}}{z(z^2+b^2)}$，$a>0$。极点：$z=0$（实轴，一阶）、$z=\pm ib$（上半平面 $ib$，一阶）。

留数：

$$\operatorname{Res}_{z=0}f=\lim_{z\to0}\frac{e^{iaz}}{z^2+b^2}=\frac{1}{b^2},$$

$$\operatorname{Res}_{z=ib}f=\frac{e^{i(ib)a}}{ib\cdot(2ib)}=\frac{e^{-ab}}{-2b^2}.$$

回路：实轴（在 $0$ 处从上方绕过，顺时针）＋上半平面大半圆。回路内只有 $ib$：

$$\oint=2\pi i\left(-\frac{e^{-ab}}{2b^2}\right)=-\frac{i\pi e^{-ab}}{b^2}.$$

小半圆贡献 $-i\pi\operatorname{Res}_0=-\dfrac{i\pi}{b^2}$；大弧由若尔当消失。三段之和等于回路积分：

$$\mathrm{P.V.}\int+\left(-\frac{i\pi}{b^2}\right)=-\frac{i\pi e^{-ab}}{b^2}
\Longrightarrow
\mathrm{P.V.}\int=\frac{i\pi}{b^2}\left(1-e^{-ab}\right).$$

**结果。** $\dfrac{1}{x(x^2+b^2)}$ 在实轴上取实值，取虚部：

$$\int_{-\infty}^{\infty}\frac{\sin(ax)}{x(x^2+b^2)}\,\mathrm{d}x=\frac{\pi}{b^2}\left(1-e^{-ab}\right).$$

**检验。** 拆成两个模核对：$\dfrac{1}{x(x^2+b^2)}=\dfrac{1}{b^2}\left(\dfrac1x-\dfrac{x}{x^2+b^2}\right)$，用 $\int_0^\infty\sin(ax)/x\,\mathrm{d}x=\pi/2$ 与 $\int_0^\infty x\sin(ax)/(x^2+b^2)\,\mathrm{d}x=(\pi/2)e^{-ab}$（题 6.6 的一半）：半线得 $\dfrac{\pi}{2b^2}(1-e^{-ab})$，全实轴翻倍 ✓ 一致。

**读法。** 实轴极点给"主值"，上半平面极点给"留数"，两者在同一道题里同时出现，账要分开记。**只看结果的话很像只有一个极点的情形——但那两次 $i\pi$ 的符号必须算对**。

**6.22**

**思路。** $\kappa\to0$ 直接取会发散，因为一维库仑势本身没有有限的零点；正确做法是先减常数（重新选零点）再取极限。

**过程。** 例 6.1 给 $\varphi(x)=\dfrac{q}{2\varepsilon_0\kappa}e^{-\kappa|x|}$，令 $\kappa\to0$ 时 $\dfrac{1}{\kappa}\to\infty$。这不是算错，而是**一维库仑势真的发散**：$\kappa=0$ 时方程

$$\frac{\mathrm{d}^2\varphi}{\mathrm{d}x^2}=-\frac{q}{\varepsilon_0}\delta(x)
\quad\Longrightarrow\quad
\varphi=-\frac{q}{2\varepsilon_0}|x|+C,$$

$|x|\to\infty$ 时 $\to-\infty$，所以"无穷远处为零"这个约定在一维做不到。

正确的极限：先减去 $\varphi(0)$（选同一个零点），

$$\varphi(x)-\varphi(0)=\frac{q}{2\varepsilon_0\kappa}\left(e^{-\kappa|x|}-1\right).$$

用 $e^{-u}\approx1-u$（$u=\kappa|x|\to0$）：

$$\varphi(x)-\varphi(0)\longrightarrow\frac{q}{2\varepsilon_0\kappa}\left(-\kappa|x|\right)=-\frac{q}{2\varepsilon_0}|x| .$$

**结果。**

$$\varphi(x)-\varphi(0)=-\frac{q}{2\varepsilon_0}|x|\qquad(\kappa\to0).$$

**检验。** 对 $-\dfrac{q}{2\varepsilon_0}|x|$ 求二阶导：$\dfrac{\mathrm{d}^2}{\mathrm{d}x^2}|x|=2\delta(x)$，得 $\dfrac{\mathrm{d}^2\varphi}{\mathrm{d}x^2}=-\dfrac{q}{\varepsilon_0}\delta(x)$ ✓ 正是原方程。

**读法。** 一维库仑势是 $|x|$（线性），三维是 $1/r$。**差别在维度**：三维的 $1/r$ 在无穷远衰减，"无穷远为零"能做到；一维的 $|x|$ 增长，做不到。这就是为什么一维的库仑问题总要加均匀背景电荷来屏蔽——那就是例 6.1 的 $\kappa$。

**6.23**

**思路。** $(k^2+\kappa^2)^2$ 的两个二阶极点直接算要套多次求导；更稳的是**对参数求导**：把已知的 $1/(k^2+\kappa^2)$ 的结果对 $\kappa^2$ 求一次导，正好得到二阶极点的积分。

**过程。** 已知（例 6.1）

$$\int_{-\infty}^{\infty}\frac{e^{ikx}}{k^2+\kappa^2}\,\mathrm{d}k=\frac{\pi}{\kappa}e^{-\kappa|x|} .$$

注意到

$$\frac{\partial}{\partial(\kappa^2)}\frac{1}{k^2+\kappa^2}=-\frac{1}{(k^2+\kappa^2)^2},$$

所以

$$G(x)=-\frac{\partial}{\partial(\kappa^2)}\left(\frac{\pi}{\kappa}e^{-\kappa|x|}\right).$$

用 $\dfrac{\partial}{\partial(\kappa^2)}=\dfrac{1}{2\kappa}\dfrac{\partial}{\partial\kappa}$：

$$G(x)=-\frac{1}{2\kappa}\frac{\mathrm{d}}{\mathrm{d}\kappa}\left[\frac{\pi}{\kappa}e^{-\kappa|x|}\right]
=-\frac{\pi}{2\kappa}\left[-\frac{1}{\kappa^2}e^{-\kappa|x|}-\frac{|x|}{\kappa}e^{-\kappa|x|}\right]
=\frac{\pi}{2\kappa^3}\left(1+\kappa|x|\right)e^{-\kappa|x|}.$$

**结果。**

$$G(x)=\frac{\pi}{2\kappa^3}\left(1+\kappa|x|\right)e^{-\kappa|x|}
\quad[\text{长度}^{-3}].$$

**检验。** $x\to0$ 时 $G\to\pi/(2\kappa^3)$，正是 $\int\mathrm{d}k/(k^2+\kappa^2)^2=\pi/(2\kappa^3)$ ✓。$|x|\to\infty$ 时按 $(1+\kappa|x|)e^{-\kappa|x|}$ 衰减，比单极点情形多一个多项式因子 ✓（二阶极点的一般特征）。

**读法。** **极点的阶数决定衰减前面挂几个幂次**：一阶极点给 $e^{-\kappa|x|}$，二阶给 $(1+\kappa|x|)e^{-\kappa|x|}$，$n$ 阶给 $n-1$ 次多项式乘指数。这和"分部积分一次多一个 $1/\kappa$"是同一件事。

**6.24**

**思路。** $\gamma\to0$ 时极点撞上实轴，$\operatorname{Im}\chi$ 变成 $\delta$ 函数；关键是两项要一正一负，否则奇偶性就错了。

**过程。** $i\epsilon$ 规则（注意 $\omega\approx-\omega_0$ 时 $\epsilon$ 的符号翻）：

$$\frac{1}{\omega_0^2-\omega^2-i0^{+}\omega}
=\mathrm{P.V.}\frac{1}{\omega_0^2-\omega^2}
+\frac{i\pi}{2\omega_0}\bigl[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\bigr].$$

乘上 $\omega_p^2$，取虚部：

$$\operatorname{Im}\chi(\omega)=\frac{\pi\omega_p^2}{2\omega_0}\bigl[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\bigr].$$

**结果。**

$$\operatorname{Im}\chi(\omega)=\frac{\pi\omega_p^2}{2\omega_0}\bigl[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\bigr],
\qquad
\int_0^\infty\omega\operatorname{Im}\chi\,\mathrm{d}\omega=\frac{\pi}{2}\omega_p^2 .$$

**检验。** 三条：$\int_{-\infty}^{\infty}\operatorname{Im}\chi\,\mathrm{d}\omega=\dfrac{\pi\omega_p^2}{2\omega_0}(1-1)=0$ ✓（$\operatorname{Im}\chi$ 必须奇）；$\int_0^\infty\omega\operatorname{Im}\chi\,\mathrm{d}\omega=\dfrac{\pi\omega_p^2}{2\omega_0}\cdot\omega_0=\dfrac{\pi}{2}\omega_p^2$ ✓，与 $\gamma\ne0$ 时的求和规则一致；峰位在 $\pm\omega_0$、宽度为零 ✓。

**读法。** 无阻尼共振的"吸收"是一根线：峰高无穷、面积有限。**$\delta$ 不是数学游戏**——它说的是"这个模式完全不耗散，只在共振频率上与场交换能量"，而"面积有限"说的是振子强度守恒。

### 习题 6.25–6.31

**6.25**

**思路。** 这是一道"诊断题"：先按标准动作算一遍，看大弧给什么；再用 $ML$ 估计判断它为什么不该消失；最后想清楚"补救"到底存在不存在。

**过程。** **(1) 算大弧。** 设 $f(z)=\dfrac{z}{z^2+a^2}$，极点 $z=\pm ia$，留数

$$\operatorname{Res}_{z=\pm ia}f=\frac{z}{2z}\Big|_{z=\pm ia}=\frac12 .$$

上半圆闭合（逆时针）捕获 $ia$：

$$\oint_{C_R+\text{实轴}}f\,\mathrm{d}z=2\pi i\cdot\frac12=\pi i .$$

实轴部分是奇函数的**主值**，为零；所以大弧自己扛下了整个 $\pi i$：

$$\int_{C_R}\frac{z\,\mathrm{d}z}{z^2+a^2}\longrightarrow\pi i .$$

也可以直接参数化验证：$z=Re^{i\theta}$，$R\to\infty$ 时被积函数 $\approx\dfrac{Re^{i\theta}}{R^2e^{2i\theta}}iRe^{i\theta}\mathrm{d}\theta=i\,\mathrm{d}\theta$，积出 $\pi i$。

**(2) 判据在哪失效。** $ML$ 估计：$|f|\sim1/R$，弧长 $\pi R$，界是 $\pi R\cdot\dfrac1R=\pi$，**不趋于零**。要消失需要 $|f|\sim R^{-1-\varepsilon}$，这里只差一阶。

**(3) 有没有补救。** 没有——错的是方法不是计算。下半圆同样不消失（顺时针，给 $-2\pi i\cdot\frac12=-\pi i$，符号相反），说明**圆弧的贡献是 $\pm\pi i$，不是小量**。正确做法：承认这个积分只能按主值定义（由奇对称性直接给零），或者把它当作希尔伯特变换的核，用 $i\epsilon$（6.7.4 节）而不是半圆闭合。

**结果。**

$$\int_{C_R}\frac{z\,\mathrm{d}z}{z^2+a^2}=\pi i,\qquad
\int_{C_R}\frac{z\,\mathrm{d}z}{z^2+a^2}\ \text{不趋于零},\qquad
\mathrm{P.V.}\int_{-\infty}^{\infty}\frac{x\,\mathrm{d}x}{x^2+a^2}=0 .$$

**检验。** 用 $ML$ 判据预判"不消失"，实际算出 $\pi i$，两者一致 ✓——**判据不是形式检查，它就是这次估计本身**。

**读法。** 这是本章最重要的一次失败示范：**先估后算**。估出来不趋于零，就不要补这条回路；否则你会把 $0$ 写成 $\pi i$，而且看不出错在哪。

**6.26**

**思路。** $z^{\alpha-1}$ 是多值的，绕支点一圈值变 $e^{2\pi i\alpha}$，所以单值回路不行；改用钥匙孔，让割线两侧"不抵消"，反而把原积分挤出来。

**过程。** 取 $f(z)=\dfrac{z^{\alpha-1}}{1+z}$，$0<\alpha<1$，支割线取**正实轴**，分支 $\arg z\in(0,2\pi)$。回路分四段。

**上沿**（$z=xe^{i0}$，$\epsilon\to R$）：$f\to\dfrac{x^{\alpha-1}}{1+x}$。

**下沿**（$z=xe^{2\pi i}$，$R\to\epsilon$，方向相反）：$z^{\alpha-1}=x^{\alpha-1}e^{2\pi i(\alpha-1)}$，所以 $f\to e^{2\pi i\alpha}\dfrac{x^{\alpha-1}}{1+x}$。

上下沿相加贡献 $\left(1-e^{2\pi i\alpha}\right)I$，$I$ 就是要求的积分。

**小圆**：$|f|\le C\epsilon^{\alpha-1}$，长度 $2\pi\epsilon$，模 $\le2\pi C\epsilon^{\alpha}\to0$（因为 $\alpha>0$）。

**大圆**：$|f|\le CR^{\alpha-1}$，长度 $2\pi R$，模 $\le2\pi CR^{\alpha}\to0$（因为 $\alpha<1$）。

**回路内的留数。** 唯一极点 $z=-1$，一阶，沿上沿分支 $\arg(-1)=\pi$：

$$\operatorname{Res}_{z=-1}f=(-1)^{\alpha-1}=e^{i\pi(\alpha-1)}=-e^{i\pi\alpha}.$$

于是

$$\left(1-e^{2\pi i\alpha}\right)I=-2\pi i\left(-e^{i\pi\alpha}\right)=2\pi i\,e^{i\pi\alpha}.$$

化简：$1-e^{2\pi i\alpha}=e^{i\pi\alpha}\left(e^{-i\pi\alpha}-e^{i\pi\alpha}\right)=-2i\,e^{i\pi\alpha}\sin\pi\alpha$，两边约去 $e^{i\pi\alpha}$。

**结果。**

$$I=\int_0^{\infty}\frac{x^{\alpha-1}}{1+x}\,\mathrm{d}x=\frac{\pi}{\sin(\pi\alpha)},\qquad 0<\alpha<1 .$$

**检验。** 三个极限：$\alpha\to0$ 给 $\sim1/\alpha\to\infty$（$\int\mathrm{d}x/[x(1+x)]$ 两端对数发散）；$\alpha\to1$ 也爆炸（高频不衰减，紫外发散）；$\alpha=\frac12$ 给 $\pi$，与代换 $x=t^2$ 得 $\int\mathrm{d}t/(1+t^2)=\pi$ ✓ 一致。

**读法。** **多值函数反而"更好算"**：单值函数的上下沿会互相抵消，什么都得不到；而 $e^{2\pi i\alpha}\ne1$ 让它们不抵消。这就是钥匙孔的全部思想。

**6.27**

**思路。** 二阶极点没有 $a_{-1}$ 项能"存活"一整圈——准确的说是 $a_{-2}$ 项在积分时带出 $1/\epsilon$，半圈积分没有有限极限，所以主值不存在。

**过程。** 沿以 $z_0$ 为圆心、半径 $\epsilon$ 的小半圆，参数化 $z-z_0=\epsilon e^{i\theta}$，$\mathrm{d}z=i\epsilon e^{i\theta}\mathrm{d}\theta$：

$$\int_{C_\epsilon}\frac{\mathrm{d}z}{(z-z_0)^2}
=\int_{\pi}^{0}\frac{i\epsilon e^{i\theta}}{\epsilon^2e^{2i\theta}}\,\mathrm{d}\theta
=\frac{i}{\epsilon}\int_{\pi}^{0}e^{-i\theta}\,\mathrm{d}\theta .$$

积分：$\int_\pi^0e^{-i\theta}\mathrm{d}\theta=\dfrac{e^{-i\theta}}{-i}\Big|_\pi^0=\dfrac{1-(-1)}{-i}=\dfrac{2}{-i}=2i$。所以

$$\int_{C_\epsilon}\frac{\mathrm{d}z}{(z-z_0)^2}=\frac{i}{\epsilon}\cdot 2i=-\frac{2}{\epsilon}\longrightarrow\infty .$$

**结果。**

$$\int_{C_\epsilon}\frac{\mathrm{d}z}{(z-z_0)^2}=-\frac{2}{\epsilon}\xrightarrow{\epsilon\to0}-\infty,$$

**主值不存在**（两侧对称挖洞的极限不收敛）。

**检验。** 对照一阶极点：$\int_{C_\epsilon}\mathrm{d}z/(z-z_0)\to\pm i\pi$，**与 $\epsilon$ 无关**；二阶极点则是 $1/\epsilon$，随 $\epsilon$ 发散。差别就在"分子的幂次"。

**读法。** 物理上二阶极点对应**临界阻尼**（$\gamma=2\omega_0$ 时两个极点合并），或自由粒子 $f=1/\omega^2$（双极点正在实轴 $0$ 上）。后者的积分 $\int\mathrm{d}\omega/\omega^2$ 红外发散，就是这个 $1/\epsilon$ 的物理版本。

**6.28**

**思路。** $\gamma<0$ 只是把极点从下半平面搬到上半平面；闭合方向的判据没变，所以"$t<0$ 时为零"会失效，变成"$t<0$ 时指数增长"。

**过程。** **(1)** $\omega_\pm=\pm\Omega-i\gamma/2$，$\gamma<0$ 时 $\operatorname{Im}\omega_\pm=-\gamma/2>0$，两个极点都在**上半平面**。

**(2)** $t<0$ 时 $|e^{-i\omega t}|=e^{yt}$ 要求 $y>0$ 才衰减，故往上闭合；上半平面有两个极点，全被捕获：

$$x(t)=-2\pi i\sum_{\pm}\operatorname{Res}\left[\frac{e^{-i\omega t}}{\omega_0^2-\omega^2-i\gamma\omega}\right]_{t<0}
\propto e^{-\gamma t/2}\sin(\Omega t),\qquad t<0 .$$

（$\gamma<0$ 时 $e^{-\gamma t/2}=e^{|\gamma||t|/2}$，随 $|t|$ 指数增长。）

$t>0$ 时反而往下闭合，下半平面没有极点，$x(t>0)=0$。

**结果。**

$$x(t)\propto e^{|\gamma||t|/2}\sin(\Omega t)\quad(t<0),\qquad x(t>0)=0 .$$

**检验。** $\gamma\to0^-$ 时增长率为零，两个半平面的极点趋于实轴，响应退化为 $\theta(t)$ 前的振荡 ✓（与无阻尼情形一致）。

**读法。** **"极点在上半平面"= 非因果**：响应在激励之前就存在，且越来越大。$Q=\Omega/|\gamma|$ 越大，这个"预响应"的相干长度越长、越容易被察觉——所以激光、增益介质里这是一条必须严肃对待的判据。

**6.29**

**思路。** 环形区域是"两连通"的，不能直接用柯西定理；把内边界反向，拼成一条围住解析区域的复合闭路径，就可以用了。

**过程。** 设 $\gamma_1$（外）与 $\gamma_2$（内）**同向**（都逆时针），$f$ 在两者之间的环形区域内及两条边界上解析。把内边界反向记作 $-\gamma_2$。

复合路径 $\gamma=\gamma_1+(-\gamma_2)$ 围成的区域是单连通的（环形区域本身，只是边界走法变了），$f$ 在其内部和边界上解析。由柯西定理：

$$\oint_\gamma f\,\mathrm{d}z=\oint_{\gamma_1}f\,\mathrm{d}z+\oint_{-\gamma_2}f\,\mathrm{d}z=0 .$$

用 $\oint_{-\gamma_2}=-\oint_{\gamma_2}$：

**结果。**

$$\oint_{\gamma_1}f\,\mathrm{d}z=\oint_{\gamma_2}f\,\mathrm{d}z .$$

**检验。** 特例：$f=1/z$，$\gamma_1$ 是 $|z|=2$、$\gamma_2$ 是 $|z|=1$，两者都给 $2\pi i$ ✓，与 6.3.1 的"与半径无关"一致。

**读法。** 这就是**变形不变性**的严格版本：回路可以在解析区域里连续变形（不扫过奇点）而不改变积分。它是"把大半圆缩成小圆""把钥匙孔收窄"的全部依据。**注意：方向不能错，否则等号右边多一个负号。**

**6.30**

**思路。** 判断标准只有一条：**奇点是不是孤立的**。孤立奇点（极点、本性）可用留数定理；支点和奇点堆积不行；支点要换围道。

**过程（逐条）。**

**(a) $\sqrt{z}/(1+z)$：不能。** $z=0$ 是支点，绕一圈 $\sqrt z\to-\sqrt z$，上下沿不抵消，不是"有限个孤立奇点"。补救：沿正实轴取割线，用钥匙孔；结果里出现 $1-(-1)=2$ 这类因子。

**(b) $\ln z/(1+z^2)$：不能。** 同上，$z=0$ 是支点。钥匙孔后，割线两侧 $\ln z$ 差 $2\pi i$，这个差**不抵消**，反而给出原积分：
$$\oint=\int_{\text{上沿}}-\int_{\text{下沿}}=-\int_0^\infty\frac{2\pi i}{1+x^2}\,\mathrm{d}x=-2\pi i\cdot\frac{\pi}{2}=-\pi^2 i .$$

**(c) $e^{1/z}/(z-1)$：能。** $z=0$ 是本性奇点，但**孤立**——留数定理只要求孤立。留数要读洛朗系数：

$$\frac{e^{1/z}}{z-1}=-e^{1/z}\left(1+z+z^2+\cdots\right)
=-\left(1+\frac1z+\frac{1}{2z^2}+\cdots\right)\left(1+z+\cdots\right).$$

$1/z$ 的系数：来自 $1\cdot\frac1z$ 与 $\frac{1}{2z^2}\cdot z^2$……逐项看，$1/z$ 的总系数是 $-1$（只有 $e^{1/z}$ 的常数项乘 $-1$ 贡献）。所以 $\operatorname{Res}_{z=0}=-1$；$z=1$ 处一阶，留数 $e$。

**(d) $1/\sin(1/z)$：不能。** 奇点在 $1/z=n\pi$，即 $z=1/(n\pi)$，当 $n\to\infty$ 时 $z\to0$ **堆积**——奇点不孤立，"有限个孤立奇点"的前提不成立。

**结果。**

| 函数 | 能否直接用 | 原因 | 补救 |
|---|---|---|---|
| $\sqrt z/(1+z)$ | 否 | 支点 $0$ | 钥匙孔 |
| $\ln z/(1+z^2)$ | 否 | 支点 $0$ | 钥匙孔 |
| $e^{1/z}/(z-1)$ | **能** | 本性但孤立 | —— |
| $1/\sin(1/z)$ | 否 | 奇点堆积 | 不能用 |

**检验。** (c) 是本题的关键区分点：**"本性奇点"不是障碍，"非孤立"才是**。很多人把两者混为一谈。

**读法。** 一句话判据：**奇点必须是孤立的（极点或本性），否则先换围道（钥匙孔），或者根本不能用留数。**

**6.31**

**思路。** 同一个函数在不同环形区域里的洛朗展开不同；留数只由**最内层**（贴着奇点的去心圆盘）的展开定义。

**过程。** 先拆开：$\dfrac{1}{z(z-1)}=\dfrac{1}{z-1}-\dfrac{1}{z}$。

**(1) $0<|z|<1$：** 把 $\dfrac{1}{z-1}=-\dfrac{1}{1-z}$ 按几何级数展开（$|z|<1$ 收敛）：

$$f(z)=-\frac{1}{z}-\left(1+z+z^2+\cdots\right)
=-\frac1z-1-z-z^2-\cdots$$

$1/z$ 的系数是 $-1$。

**(2) $1<|z|<\infty$：** 这次把 $\dfrac{1}{z-1}=\dfrac1z\cdot\dfrac{1}{1-1/z}$ 展开（$|1/z|<1$ 收敛）：

$$f(z)=\frac1z\left(1+\frac1z+\frac{1}{z^2}+\cdots\right)-\frac1z
=\frac{1}{z^2}+\frac{1}{z^3}+\cdots$$

（$-\dfrac1z$ 与展开里的 $\dfrac1z$ 抵消！）这个展开里**没有** $1/z$ 项。

**(3) 为什么留数仍是 $-1$：** 留数由 $0<|z-z_0|<R$ 这个最内层去心圆盘的展开定义。外层展开描述的是远处（包括无穷远点）的行为，跟 $z_0$ 处的留数无关。

**结果。**

$$0<|z|<1:\quad f=-\frac1z-1-z-\cdots,\quad \operatorname{Res}_{z=0}f=-1;$$
$$1<|z|<\infty:\quad f=\frac{1}{z^2}+\frac{1}{z^3}+\cdots,\quad \text{无 }1/z\text{ 项}.$$

**检验。** 用 $z=0$ 处的另一条路核对：$\operatorname{Res}_{z=0}\dfrac{1}{z(z-1)}=\lim_{z\to0}\dfrac{z}{z(z-1)}=\dfrac{1}{-1}=-1$ ✓，与最内层展开一致。

**读法。** 物理上也对：$z=0$ 处那个模式的耦合强度，不该依赖你在多远的地方做展开。**"留数"是局部量，展开区域是全局选择**。

### 概念与判断 6.32–6.40

**6.32**（解析函数沿闭曲线积分为零？）

**错。** 缺的条件是"闭曲线**内部**及边界上处处解析"。

**反例一：** $f(z)=1/z$ 在 $|z|=1$ 上处处解析，但

$$\oint_{|z|=1}\frac{\mathrm{d}z}{z}=2\pi i\ne0,$$

因为奇点（原点）在**内部**。同一条曲线换成以 $z=3$ 为心、半径 $1$ 的圆，积分就是 $0$。

**反例二：** $f(z)=1/z^2$ 不包围原点时积分也为零，包围时仍为零——但它绕原点**不解析**，
之所以为零是因为 $a_{-1}=0$，不是因为没有奇点。这说明"积分为零"本身不能
反推出"内部无奇点"，两个方向的逻辑要分清。

**正确说法：** 内部及边界上解析 ⟹ 积分为零；反过来不成立。

**常见误解：** 以为"边界上解析"就够了。柯西定理用的是**区域**上的解析性——
一个洞就足以让结论失效，这正是 6.3.3 节"变形不变性"的出发点。

**读法：** 这条判断点的实用价值在于：看到一个闭合积分不为零，第一反应应该是
"里面藏了奇点"，而不是"定理错了"。

**6.33**（$R\to\infty$ 时大半圆积分总趋于零？）

**错。** 判据是 $|f|\sim R^{-1-\varepsilon}$（分母次数比分子至少高 2），不是"$R$ 大就行"。

**正例：** $f=1/z^2$，弧上 $|f|=1/R^2$，积分 $\le\pi R\cdot R^{-2}=\pi/R\to0$ ✓；
$f=1/z^3$ 同样（界 $\pi/R^2$）。

**反例一：** $f=1/z$，弧上积分恒为 $2\pi i$，与 $R$ 无关。

**反例二：** $f=z/(z^2+a^2)$，弧上给 $\pi i$（题 6.25）。两者都是 $1/R$ 型，
界 $\pi R\cdot R^{-1}=\pi$ 不趋于零。

**怎么在现场发现：** 算 $\pi R\cdot\max_{C_R}|f|$。这个界若含 $R$ 的正幂或不含 $R$，
就要怀疑；若按 $R^{-\varepsilon}$ 掉，才安全。**判据不是形式检查，它就是这次估计本身。**

**反过来的陷阱：** 判据满足只是"必要条件"，还要确认实轴本身收敛（题 6.25 的实轴部分
是奇函数的主值，靠对称性才为零）。

**6.34**（实轴无极点就能用大半圆？）

**错。** 还需要三条：

1. 补上的弧积分趋于零（衰减够快，或靠若尔当引理）；
2. 若含 $e^{iaz}$，$a$ 的符号决定往哪个半平面闭合——方向错了，$e^{iaz}$ 在那个半平面指数爆炸；
3. 多值函数还要避开支点（题 6.30）。

反例：$\int e^{iaz}/(z^2+a^2)\mathrm{d}z$ 若 $a<0$ 仍往上闭合，被积函数在上半平面按 $e^{|a|y}$ 爆炸，结果完全错。

**6.35**（主值就是积分值？）

**错。** 只有普通积分收敛时两者才相等。

反例：$\mathrm{P.V.}\int_{-1}^{1}\dfrac{\mathrm{d}x}{x}=0$（两侧对称抵消），而普通积分发散；$\int\dfrac{\cos x}{x}\mathrm{d}x$ 也只有主值。

**物理上必须区分的场合：** 无阻尼共振（$\gamma=0$）的响应函数极点正在实轴上。这时 $\mathrm{P.V.}\dfrac{1}{\omega_0^2-\omega^2}$ 是**色散**部分，$\pi\delta$ 是**吸收**部分，两者是两个不同的物理量（题 6.24）。混用会得到错误的吸收谱。

**6.36**（小弧引理对任何阶的极点都成立？）

**错。** 只对**一阶**极点成立。

二阶极点时 $f=a_{-2}/(z-z_0)^2+\cdots$，沿小半圆

$$\int_{C_\epsilon}\frac{a_{-2}}{(z-z_0)^2}\mathrm{d}z=\frac{a_{-2}}{\epsilon}\int i e^{-i\theta}\mathrm{d}\theta\sim\frac{1}{\epsilon},$$

**按 $1/\epsilon$ 发散**，没有有限极限（题 6.27），主值也不存在。

**为什么只留 $a_{-1}$：** 一圈积分 $\oint(z-z_0)^n\mathrm{d}z=2\pi i\delta_{n,-1}$ 只有 $n=-1$ 存活；$n=-2$ 那项必须靠 $1/\epsilon$ 才能体现，散掉了。

**6.37**（解析 ⇔ 调和？）

**第一句对，第二句对但需要单连通。**

**第一句：** 由柯西–黎曼条件交叉求导，$\partial^2u/\partial x^2=-\partial^2u/\partial y^2$，所以 $\nabla^2u=\nabla^2v=0$，不需要额外条件。

**第二句：** 给定调和 $u$，要找共轭调和 $v$，使 $u+iv$ 解析。由柯西–黎曼条件，$v$ 满足全微分方程；**在单连通区域内**，可积性条件（正是 $\nabla^2u=0$）保证 $v$ 存在。

**反例（多连通）：** $u=\ln r$ 调和，它的共轭是 $\theta$，而 $\theta$ 多值（绕原点一圈变 $2\pi$），不是单值函数。所以挖掉原点的圆环上，"调和 ⟹ 是某个解析函数的实部"不成立。

**6.38**（有界 ⟹ 可去奇点？）

**对**，这是可去奇点定理（黎曼可去奇点定理）：有界则主部为零，奇点可去。

**用它判断两个例子：**

- $\sin z/z$：在 $0<|z|<1$ 内 $|\sin z/z|\le\cosh1<2$，有界 ⟹ 可去 ✓（与 $1-z^2/6+\cdots$ 一致）。
- $e^{1/z}$：沿 $z=1/n$（$n$ 正整数）趋于 $0$，$e^{1/z}=e^{n}\to\infty$，无界 ⟹ 不是可去。它其实是本性奇点（主部无穷多项）。

**判据的边界：** 有界 ⟹ 可去，但"可去"之外（极点还是本性）这套办法分不出来，要看主部。

**6.39**（$\cos\to e^{iax}$ 取实部总合法？）

**错，要加条件。**

成立：若 $R$ 在实轴上取**实值**，且两个积分都收敛，则

$$\int R\cos(ax)\,\mathrm{d}x=\operatorname{Re}\int Re^{iax}\,\mathrm{d}x .$$

因为 $e^{iax}=\cos ax+i\sin ax$，取实部就是把两项分开。

**出错的情形一：** $R$ 带 $i$（响应函数分子含 $i$），$\operatorname{Re}[Re^{iax}]$ 里混进 $\sin$ 的贡献，取实部不再等于 $\cos$ 的积分。

**出错的情形二：** $\sin$ 部分发散而 $\cos$ 部分收敛。这时 $e^{iax}$ 的整体积分只能按主值理解，直接取实部会错。（题 6.21 就踩在这个边界上：$1/[x(x^2+b^2)]$ 在实轴上有极点。）

**6.40**（回路可以随意变形？）

**错。** 正确说法：**回路可以在不扫过奇点的前提下连续变形，积分值不变**。

漏掉"不扫过奇点"，就会得出"$\oint\mathrm{d}z/z$ 与回路无关"的荒谬结论——绕原点的回路给 $2\pi i$，不绕的给 $0$。

**推论三条：**

1. 变形时扫过的区域内必须处处解析；
2. 若两条回路围住的奇点不同，积分之差等于"多围住的那几个奇点"的留数之和乘 $2\pi i$（这正是题 6.29 的内容）；
3. 变形可以把大半圆缩成小圆、把钥匙孔收窄——**"捷径"能成立，全靠这条**。

**一个容易忽略的细节：** "变形"是连续的，回路不能跳过分立障碍；如果中间隔着支点
（比如 $\ln z$ 的原点），变形就跨不过去，这正是多值函数要换钥匙孔的原因。

**读法：** 留数定理的全部内容可以压成一句话——*积分只记录围住了哪些奇点，路径的形状无关*。这句话的严格版本就是本题。

## 第 7 章

> 每题给思路、关键步骤、结果、检验和物理读法。缺的步骤请自己补全后再看。

**7.1** **思路**：复势的虚部就是流函数 $\psi$；「物面是流线」等价于「$\psi$ 在物面上取常数」。所以只要把 $w$ 在 $|z|=a$ 上的值算出来，看虚部是否为常数即可，再用 $v_r=0$ 反向确认。

令 $z=ae^{i\theta}$（$|z|=a$），则 $a^{2}/z=a^{2}/(ae^{i\theta})=ae^{-i\theta}$，于是

$$w=U\left(ae^{i\theta}+ae^{-i\theta}\right)=2Ua\cos\theta .$$

这是**实数**，所以 $\psi=\operatorname{Im}w=0$：整个圆是 $\psi=0$ 这条流线。

再验证法向速度。一般点 $z=re^{i\theta}$ 处

$$w=U\left(re^{i\theta}+\frac{a^{2}}{r}e^{-i\theta}\right)
=U\left(r+\frac{a^{2}}{r}\right)\cos\theta
+iU\left(r-\frac{a^{2}}{r}\right)\sin\theta,$$

所以 $\psi=U\left(r-\frac{a^{2}}{r}\right)\sin\theta$，径向速度

$$v_r=\frac{1}{r}\frac{\partial\psi}{\partial\theta}
=U\left(r-\frac{a^{2}}{r}\right)\frac{\cos\theta}{r}\;\xrightarrow{r=a}\;0 .$$

**结果：** 在 $|z|=a$ 上 $w=2Ua\cos\theta$ 为实，$\psi=0$，$v_r=0$——物面确实是一条流线。

**检验：** $\theta=0$ 与 $\theta=\pi$ 时 $\frac{\mathrm{d}w}{\mathrm{d}z}=U(1-a^{2}/z^{2})=0$，正是前后驻点；$\theta=\pm\pi/2$ 处 $\psi=0$ 但速度不为零（速度加倍）——**驻点与流线常数是两件事，不要混。**

**读法：** 「物面是流线」是无粘流里唯一需要的物面条件：没有穿透，但不要求无滑移。**这条条件被复势自动满足，正是复势方法好用的原因。**

**7.2** **思路**：把 $z^{2}$ 拆成实部虚部：实部是势、虚部是流函数。等势线/流线就是这两族曲线；驻点由 $\frac{\mathrm{d}w}{\mathrm{d}z}=0$ 定。

$z=x+iy$，$z^{2}=x^{2}-y^{2}+2ixy$，所以

$$\phi=U(x^{2}-y^{2}),\qquad \psi=2Uxy .$$

等势线：$x^{2}-y^{2}=$ 常数（以两坐标轴为渐近线的双曲线族）。
流线：$xy=$ 常数（另一族双曲线）。

速度：$\frac{\mathrm{d}w}{\mathrm{d}z}=2Uz$，即

$$u-iv=2U(x+iy)\;\Longrightarrow\;u=2Ux,\quad v=-2Uy .$$

驻点：$\frac{\mathrm{d}w}{\mathrm{d}z}=0\Rightarrow z=0$。

**结果：** 等势线 $x^{2}-y^{2}=\text{const}$，流线 $xy=\text{const}$；驻点在原点；$u=2Ux$、$v=-2Uy$。

**检验：** 两条坐标轴都是流线（$\psi=0$），所以可当作两堵直角墙；沿 $y$ 轴 $v=-2Uy<0$（$y>0$ 时流向原点），沿 $x$ 轴 $u=2Ux>0$（向外）——**流体从 $y$ 轴流入、从 $x$ 轴流出，符合「驻点流」的图像** ✓。

**读法：** 这就是「流体冲向一个直角角落」的流场，$\phi$ 与 $\psi$ 是共轭调和函数。**它是最简单的非均匀流，也是边界层理论里「驻点附近」的局部模型。**

**7.3** **思路**：令 $\zeta=Re^{i\theta}$，把 $z=\zeta+a^{2}/\zeta$ 的实部虚部分开，看出是椭圆；半轴之比与 $R/a$ 的关系直接读出厚度。

$$\zeta=Re^{i\theta}\;\Longrightarrow\;
z=\left(R+\frac{a^{2}}{R}\right)\cos\theta
+i\left(R-\frac{a^{2}}{R}\right)\sin\theta .$$

所以像是椭圆，半轴

$$A=R+\frac{a^{2}}{R},\qquad B=R-\frac{a^{2}}{R},$$

焦点在 $c=\sqrt{A^{2}-B^{2}}=\sqrt{4a^{2}}=2a$。

$R=1.5a$：$A=1.5a+\frac{a}{1.5}=2.167a$，$B=1.5a-0.667a=0.833a$；厚度比 $\frac{2B}{2A}=\frac{0.833}{2.167}=38\%$；离心率 $e=\frac{2a}{2.167a}=0.923$。

**结果：** 椭圆半轴 $R+a^{2}/R$ 与 $R-a^{2}/R$，焦点恒在 $z=\pm2a$；$R=1.5a$ 时为 $2.17a\times0.83a$ 的椭圆，厚弦比 $38\%$；$R\to a$ 时退化为线段 $[-2a,2a]$。

**检验：** $c=2a$ 与 $R$ 无关——**这一族椭圆共焦** ✓；$R\to a$ 时 $B\to0$ ✓；$R\gg a$ 时 $A\approx B\approx R$，趋于半径 $R$ 的圆 ✓。

**读法：** 半径 $R$ 管厚度：$R$ 越接近 $a$，翼型越薄。**「薄翼」与「厚翼」在这张图里只是同一个映射的参数取值，没有本质区别。**

**7.4** **思路**：临界点由 $z'(\zeta)=0$ 定；单叶性由「$\zeta$ 与 $a^{2}/\zeta$ 映到同一点」这个对合关系判断。

$$z'(\zeta)=1-\frac{a^{2}}{\zeta^{2}}=0\;\Longrightarrow\;\zeta=\pm a,$$

像点 $z(\pm a)=\pm a+\frac{a^{2}}{\pm a}=\pm2a$。

单叶性：$z(\zeta)=z(a^{2}/\zeta)$ 对一切 $\zeta$ 成立（把 $a^{2}/\zeta$ 代入即可验证）。所以只要 $\zeta$ 与 $a^{2}/\zeta$ 一个在圆内、一个在圆外，两者就映到同一点。**若把 $|\zeta|<a$ 也用上，映射就是二对一的**：圆内的点会与圆外的点撞在一起，像曲线自交。限制在 $|\zeta|>a$ 后，对合的另一半落在圆内，不再冲突，映射单叶。

**结果：** 临界点 $\zeta=\pm a$，像点 $z=\pm2a$；必须限制 $|\zeta|>a$，此时像平面是沿 $[-2a,2a]$ 割开的区域。

**检验：** 取 $\zeta=2a$（外部）与 $\zeta=a/2$（内部）：$2a+\frac{a^{2}}{2a}=2.5a$，$\frac{a}{2}+\frac{a^{2}}{a/2}=0.5a+2a=2.5a$——**同一点，一个在外一个在内** ✓。

**读法：** 割线 $[-2a,2a]$ 就是「平板翼型」。**外部单叶、内部多余**，正是「用圆外区域代表翼型外部」的数学依据。

**7.5** **思路**：驻点由 $\frac{\mathrm{d}w}{\mathrm{d}z}=0$ 得二次方程，解出后用 $\sin\beta=\Gamma/(4\pi Ua)$ 表示；表面速度用切向分量公式。

$\frac{\mathrm{d}w}{\mathrm{d}z}=U(1-\frac{a^{2}}{z^{2}})-\frac{i\Gamma}{2\pi z}=0$，两边乘 $z^{2}/U$：

$$z^{2}-\frac{i\Gamma}{2\pi U}z-a^{2}=0 .$$

解为 $z_{\text{驻}}=\pm a\cos\beta+ia\sin\beta$，其中

$$\sin\beta=\frac{\Gamma}{4\pi Ua} .$$

代入 $\Gamma=2\pi Ua$：$\sin\beta=\frac{2\pi Ua}{4\pi Ua}=\frac12$，$\beta=30^\circ$，所以

$$z_{\text{驻}}=\pm0.866a+0.5ai .$$

表面切向速度（逆时针为正）

$$v_\theta=-\left(2U\sin\theta-\frac{\Gamma}{2\pi a}\right)=-\left(2U\sin\theta-U\right)=U-2U\sin\theta .$$

顶部 $\theta=\pi/2$：$v_\theta=U-2U=-U$，大小 $U$。
底部 $\theta=3\pi/2$：$v_\theta=U+2U=3U$，大小 $3U$。

**结果：** 驻点 $z=\pm0.866a+0.5ai$；顶部切向速度 $v_\theta=-U$（大小 $U$），底部 $v_\theta=+3U$（大小 $3U$）。与无环量的 $\pm2U$ 相比，**顶部减速、底部加速**。

**检验：** $\Gamma=0$ 时退回 $\beta=0$、$v_\theta=-2U\sin\theta$（顶部 $2U$）✓；$\Gamma=4\pi Ua$ 时 $\beta=90^\circ$，两驻点合并到顶点 $z=ia$ ✓。

**读法：** 逆时针环量让**顶部减速、底部加速**，压力上高下低，合力向下。**要让机翼升起来，环量必须是顺时针的**——这就是马格努斯效应与机翼升力方向相反的由来。

**7.6** **思路**：伯努利方程把速度换成压力，再用上题的两个速度值算压差；合力大小用 $F=\rho U|\Gamma|$ 对照。

伯努利（沿流线，不可压定常）：

$$p+\frac12\rho|v|^{2}=p_\infty+\frac12\rho U^{2}
\;\Longrightarrow\;
p=p_\infty+\frac12\rho\left(U^{2}-|v|^{2}\right).$$

顶部 $|v|=U$：$p_{\text{顶}}=p_\infty$。
底部 $|v|=3U$：$p_{\text{底}}=p_\infty+\frac12\rho(U^{2}-9U^{2})=p_\infty-4\rho U^{2}$。

压差 $p_{\text{顶}}-p_{\text{底}}=4\rho U^{2}>0$，顶部压力大，**合力向下**。

合力大小由 7.4.4 节 $F=\rho U|\Gamma|$：

$$F=\rho U(2\pi Ua)=2\pi\rho U^{2}a .$$

**结果：** 压差 $4\rho U^{2}$（顶部高）、合力向下，大小 $F=2\pi\rho U^{2}a$。

**检验：** 压差是「局部值」，合力是积分：若把 $4\rho U^{2}$ 直接乘迎风投影 $2a$，得 $8\rho U^{2}a$，比积分值 $6.28\rho U^{2}a$ 大——**说明压差沿圆周不是常数，不能直接相乘**；但两者的量级一致，方向一致 ✓。

**读法：** 升力不是「压力的平均值」，而是压力分布里与 $\sin\theta$ 同相的那一部分。**逆时针环量给向下的力；机翼用的是顺时针环量。**

**7.7** **思路**：三个几何量按定义算：$R$ 是圆心到临界点的距离（圆过 $\zeta=a$），$\theta_T=\arg(a-\zeta_0)$，$\Gamma_K$ 由库塔条件给出。

圆心 $\zeta_0=-0.10+0.09i$，$a=1$。圆必须过 $\zeta=a$，所以

$$R=|a-\zeta_0|=|1.10-0.09i|=\sqrt{1.21+0.0081}=1.104 .$$

后缘方向：

$$\theta_T=\arg(a-\zeta_0)=\arg(1.10-0.09i)=-\arctan\frac{0.09}{1.10}=-4.68^\circ .$$

库塔环量：

$$\Gamma_K=4\pi UR\sin(\theta_T-\alpha)
=4\pi\times1\times1.104\times\sin(-4.68^\circ-4^\circ)
=13.87\times\sin(-8.68^\circ)=-2.09\ \text{m}^{2}/\text{s}.$$

**结果：** $R=1.104$，$\theta_T=-4.68^\circ$，$\Gamma_K=-2.09\ \text{m}^{2}/\text{s}$（负号 = 顺时针）。

**检验：** $\alpha>\theta_T$（$4^\circ>-4.68^\circ$），按 7.6.3 节 $\Gamma<0$ 顺时针 → 升力向上 ✓；量纲 $[U][R]=\text{m}^2/\text{s}$ ✓。

**读法：** $\theta_T$ 就是**零升力角**：$\alpha=\theta_T$ 时 $\Gamma=0$。翼型的弯度越大，$\theta_T$ 越负，零升力角越正——**弯翼型在零攻角时也能产生升力，原因全在这一行。**

**7.8** **思路**：对 $\alpha$ 求导，得斜率；再用薄翼关系 $R\approx a$、$c\approx4a$ 化简成普适值。

$$C_L=\frac{8\pi R}{c}\sin(\alpha-\theta_T)
\;\Longrightarrow\;
\frac{\mathrm{d}C_L}{\mathrm{d}\alpha}=\frac{8\pi R}{c}\cos(\alpha-\theta_T).$$

小攻角下 $\cos\approx1$：

$$\frac{\mathrm{d}C_L}{\mathrm{d}\alpha}\approx\frac{8\pi R}{c}.$$

薄翼 $R=a$、$c=4a$：$\frac{8\pi a}{4a}=2\pi$ 每弧度；换成每度：

$$\frac{2\pi}{180/\pi}=\frac{2\pi^{2}}{180}=0.1097\ \text{每度}.$$

**结果：** 薄翼斜率 $2\pi\approx6.28$ 每弧度，约 $0.11$ 每度；$R=a$、$c=4a$ 时正是 $2\pi$。

**检验：** 量纲：$C_L$ 无量纲，$\alpha$ 无量纲，斜率无量纲 ✓；与实验值（$0.1$ 左右每度）相符 ✓。

**读法：** 斜率只依赖 $R/c$（几何厚度比），**与翼型细节无关**——这就是 7.1 节第三个问题的答案：升力线斜率的普适性来自库塔条件的几何性质。

**7.9** **思路**：布拉修斯定理只需要 $(w')^{2}$ 的 $1/z$ 系数（留数）。对无环量圆柱，展开后没有 $1/z$ 项，所以合力为零。

$$\frac{\mathrm{d}w}{\mathrm{d}z}=U\left(1-\frac{a^{2}}{z^{2}}\right),$$

$$\left(\frac{\mathrm{d}w}{\mathrm{d}z}\right)^{2}
=U^{2}\left(1-\frac{2a^{2}}{z^{2}}+\frac{a^{4}}{z^{4}}\right)
=U^{2}-\frac{2U^{2}a^{2}}{z^{2}}+\frac{U^{2}a^{4}}{z^{4}} .$$

只出现 $z^{0}$、$z^{-2}$、$z^{-4}$，**没有 $1/z$ 项**，所以围道积分为零：

$$F_x-iF_y=\frac{i\rho}{2}\oint\left(\frac{\mathrm{d}w}{\mathrm{d}z}\right)^{2}\mathrm{d}z=0 .$$

**结果：** $F_x=F_y=0$——无环量圆柱既无升力也无阻力。

**检验：** 与 7.4.3 节直接积分压力的结论一致；也与对称性一致（上下、前后都对称）✓。

**读法：** 无环量时流场前后对称，所以阻力为零——达朗贝尔佯谬。**这个「零」不是算错了，而是理想模型的精确结论**：真实阻力全在粘性里，而粘性在复势里根本没有位置。

**7.10** **思路**：同样是找 $(w')^{2}$ 的 $1/z$ 系数。偶极子的 $w'$ 是 $z^{-2}$，平方后是 $z^{-4}$，没有 $1/z$。

$$w=\frac{\mu}{z}\;\Longrightarrow\;\frac{\mathrm{d}w}{\mathrm{d}z}=-\frac{\mu}{z^{2}}
\;\Longrightarrow\;\left(\frac{\mathrm{d}w}{\mathrm{d}z}\right)^{2}=\frac{\mu^{2}}{z^{4}} .$$

$z^{-4}$ 的围道积分为零，故

$$F_x-iF_y=\frac{i\rho}{2}\oint\frac{\mu^{2}}{z^{4}}\,\mathrm{d}z=0 .$$

**结果：** 偶极子不受力。

**检验：** 与圆柱对比：圆柱的 $(w')^{2}$ 里有 $z^{-2}$ 与 $z^{-4}$，也没有 $1/z$——**两者都不受力，结论一致** ✓。

**读法：** 「偶极子代表圆柱」只是**远场等效**（$1/z$ 项相同），近场完全不同；而力只由 $1/z$（点涡）产生。**所以偶极子不受力与圆柱不受力并不矛盾，它们都在「没有环量就没有升力」这条线上。**

**7.11** **思路**：分式线性映射把圆/直线映成圆/直线；判断实轴的像，只要看三个实点的像是否都落在同一条直线（或圆）上。

$$\zeta=ia:\qquad z=\frac{ia-a}{ia+a}=\frac{i-1}{i+1}=\frac{2i}{2}=i .$$

实轴的像：对实数 $t$，$z(t)=\frac{t-a}{t+a}$ 是实数（系数全实），所以**实轴映成实轴**。取三个点确认：$t=0\mapsto-1$，$t=a\mapsto0$，$t\to\infty\mapsto1$——落在实轴上 ✓。

顺带：圆 $|\zeta|=a$ 映成虚轴——$\zeta=ae^{i\theta}$ 时

$$z=\frac{e^{i\theta}-1}{e^{i\theta}+1}=i\tan\frac{\theta}{2},$$

确实是纯虚数。

**结果：** $\zeta=ia\mapsto z=i$；实轴映成实轴；$\zeta=0\mapsto z=-1$（圆 $|\zeta|<a$ 映成左半平面）。

**检验：** 映射在 $\zeta=-a$ 有极点，而 $-a$ 在实轴上，所以实轴不能映成「不经过 $z=\infty$ 的圆」——它必须映成一条过无穷远的直线，即实轴本身 ✓。**注意：若想让实轴映成单位圆，要用 $z=\frac{\zeta-\zeta_0}{\zeta-\bar\zeta_0}$（$\operatorname{Im}\zeta_0\neq0$），本题的 $a$ 是实数，做不到。**

**读法：** 判断像的形状不必算整条曲线：**看三个点、看极点位置**就够了。分式线性映射只有三个自由度，三个点定一个圆/直线。

**7.12** **思路**：幂映射 $z=\zeta^{n}$ 在原点附近把辐角放大 $n$ 倍，所以内角也被放大 $n$ 倍。

设楔形顶点在原点、内角 $\alpha$。写 $\zeta=re^{i\theta}$，$\theta$ 从 $0$ 到 $\alpha$，则

$$z=\zeta^{3}=r^{3}e^{i3\theta},$$

像点的辐角从 $0$ 到 $3\alpha$。取 $\alpha=60^\circ$：像的辐角范围 $0$ 到 $180^\circ$——**楔形映成上半平面**（内角 $180^\circ$），角度放大 $3$ 倍。

保角性：$\frac{\mathrm{d}z}{\mathrm{d}\zeta}=3\zeta^{2}$，在 $\zeta=0$ 处为零，所以**原点处不保角**（角度被放大，夹角不再保持）。

**结果：** $60^\circ$ 楔形映成 $180^\circ$ 半平面，角度放大 $3$ 倍；原点 $z'=0$，不保角。

**检验：** 放大倍数 $=$ 内角之比 $180^\circ/60^\circ=3$，与 $n=3$ 一致 ✓；$\zeta\neq0$ 处 $z'\neq0$，保角 ✓。

**读法：** 「用幂映射把角磨平」是所有角点问题的第一步：**先磨成半平面，再用分式线性映射搬到圆**，然后才进入 7.2 节的标准流程。

**7.13** **思路**：平飞时升力等于重力，先反解 $C_L$；再用薄翼公式反解有效攻角。

$$L=mg=\frac12\rho U^{2}SC_L
\;\Longrightarrow\;
C_L=\frac{2mg}{\rho U^{2}S}.$$

代入 $m=7.0\times10^{4}$、$g=9.8$、$\rho=0.41$、$U=250$、$S=1.2\times10^{2}$：

$$C_L=\frac{2\times7.0\times10^{4}\times9.8}{0.41\times(250)^{2}\times1.2\times10^{2}}
=\frac{1.372\times10^{6}}{3.075\times10^{6}}=0.446 .$$

有效攻角：$C_L=2\pi(\alpha-\theta_T)$，取 $\theta_T=-3^\circ$：

$$\alpha-\theta_T=\frac{0.446}{2\pi}=0.0710\ \text{rad}=4.07^\circ
\;\Longrightarrow\;
\alpha\approx1.1^\circ .$$

**结果：** $C_L=0.45$，$\alpha\approx1.1^\circ$（$\theta_T=-3^\circ$）。

**检验：** 量纲：分子 $\text{kg}\cdot\text{m/s}^2=\text{N}$，分母 $\text{kg/m}^3\cdot\text{m}^2/\text{s}^2\cdot\text{m}^2=\text{N}$ ✓；$C_L=0.45$ 落在常见巡航值 $0.3$–$0.6$ 内 ✓。

**读法：** 几十吨的飞机靠**一度多的攻角**托住。真实客机巡航攻角约 $2^\circ$–$3^\circ$，差别来自真实翼型弯度更大（$\theta_T$ 更负）与三维效应——**但量级完全对得上，这说明环量模型抓住了主要矛盾。**

**7.14** **思路**：薄翼公式直接给 $C_L$，升力 $L=\frac12\rho U^{2}AC_L$。

$$C_L=2\pi\sin10^\circ=2\pi\times0.1736=1.091 .$$

$$L=\frac12\rho U^{2}AC_L=\frac12\times1.2\times(12)^{2}\times0.8\times1.091=75.4\ \text{N}.$$

攻角减半到 $5^\circ$：

$$C_L'=2\pi\sin5^\circ=0.548,\qquad
L'=\frac12\times1.2\times144\times0.8\times0.548=37.9\ \text{N}.$$

**结果：** $L\approx75\ \text{N}$；攻角减半后 $L'\approx38\ \text{N}$，正好约一半。

**检验：** $L'/L=\sin5^\circ/\sin10^\circ=0.502$ ✓（小角度下 $\sin$ 近似线性，减半攻角几乎减半升力）；量纲 $\text{kg/m}^3\cdot\text{m}^2/\text{s}^2\cdot\text{m}^2=\text{N}$ ✓。

**读法：** 风筝板的升力与 $U^{2}$、面积、攻角都成正比。**风大一倍，升力四倍**——这就是为什么大风天风筝难控。

**7.15** **思路**：旋转球带的环量用 $\Gamma=2\pi R^{2}\omega$（球面速度乘以周长积分的结果），再用 $L'=\rho U\Gamma$ 估单位长度侧向力，最后乘有效长度、除以质量得加速度。

角速度 $\omega=2\pi\times8=50.3\ \text{rad/s}$。旋转表面速度 $\Omega R$，环量

$$\Gamma=2\pi R^{2}\omega=2\pi\times(0.11)^{2}\times50.3=3.82\ \text{m}^{2}/\text{s}.$$

单位长度侧向力

$$L'=\rho U\Gamma=1.2\times30\times3.82=138\ \text{N/m}.$$

取有效长度 $2R=0.22\ \text{m}$：$F=138\times0.22=30\ \text{N}$。加速度 $a=F/m=30/0.43=70\ \text{m/s}^{2}\approx7g$，1 秒侧移 $s\approx\frac12at^{2}=35\ \text{m}$。

**结果：** $\Gamma\approx3.8\ \text{m}^{2}/\text{s}$，$F\approx30\ \text{N}$，$a\approx70\ \text{m/s}^{2}$，$1\ \text{s}$ 侧移约 $35\ \text{m}$。

**检验：** 动量量级检验：$F t/m\sim30/0.43\approx70\ \text{m/s}$，与球速 $30\ \text{m/s}$ 同量级——**说明这个估计偏大约 2–3 倍**，因为真实球面有边界层分离，环量远小于 $2\pi R^{2}\omega$。

**读法：** 真实弧线球的侧移是几米量级（不是几十米）：**无滑移假设把环量高估了几倍**。所以这套理论给的是上限，做定量预测必须用实测的 $\Gamma$（或经验公式）。

**7.16** **思路**：(a) 零升力角就是 $\theta_T$；(b) 环量用库塔公式、升力用 $L'=\rho U|\Gamma|$ 并与 $C_L$ 对照；(c) 比较两个攻角下的 $\sin(\alpha-\theta_T)$。

(a) $C_L=0$ 要求 $\alpha=\theta_T=-4.0^\circ$，即**零升力角 $-4.0^\circ$**。

(b) $a=c/4=0.50\ \text{m}$，$R\approx a=0.5$，$\alpha=6^\circ$：

$$\Gamma=4\pi UR\sin(\theta_T-\alpha)
=4\pi\times60\times0.5\times\sin(-10^\circ)
=376.99\times(-0.1736)=-65.4\ \text{m}^{2}/\text{s},$$

$$L'=\rho U|\Gamma|=1.2\times60\times65.4=4.7\times10^{3}\ \text{N/m}.$$

对照：$C_L=2\pi\sin10^\circ=1.091$，$L'=\frac12\rho U^{2}cC_L=\frac12\times1.2\times3600\times2\times1.091=4.7\times10^{3}\ \text{N/m}$ ✓。

(c) $\alpha=12^\circ$：$\theta_T-\alpha=-16^\circ$，

$$L'=\rho U\times4\pi UR|\sin16^\circ|
=1.2\times60\times376.99\times0.2756=7.5\times10^{3}\ \text{N/m},$$

比值 $7.5/4.7=1.59$，**不是 $2$ 倍**。

**结果：** 零升力角 $-4.0^\circ$；$\alpha=6^\circ$ 时 $\Gamma=-65\ \text{m}^{2}/\text{s}$、$L'=4.7\times10^{3}\ \text{N/m}$；$\alpha=12^\circ$ 时 $L'=7.5\times10^{3}\ \text{N/m}$（$1.59$ 倍）。

**检验：** 两种算法（$\rho U|\Gamma|$ 与 $\frac12\rho U^{2}cC_L$）给出同一个 $L'$ ✓；$\sin$ 的比值 $\sin16^\circ/\sin10^\circ=1.58$，与 $1.59$ 一致 ✓。

**读法：** 升力随 $\sin(\alpha-\theta_T)$ 走，不是随攻角线性走；**攻角加倍，升力只增六成**。真实翼型到这个攻角已接近失速，模型更是高估。

**7.17** **思路**：把帆当薄翼，$C_L=2\pi\sin\alpha$；升力垂直于来流，取它在船前进方向上的投影。

$$C_L=2\pi\sin20^\circ=2\pi\times0.342=2.15,$$

$$L=\frac12\rho U^{2}AC_L=\frac12\times1.2\times64\times30\times2.15=2.5\times10^{3}\ \text{N}.$$

升力垂直于来流；船头与来流成 $45^\circ$ 时，沿船头方向的分量

$$L_{\parallel}=L\cos45^\circ=2.5\times10^{3}\times0.707=1.8\times10^{3}\ \text{N}.$$

**结果：** $L\approx2.5\ \text{kN}$；沿船前进方向的分量约 $1.8\ \text{kN}$。

**检验：** 量纲 $\text{kg/m}^3\cdot(\text{m/s})^{2}\cdot\text{m}^{2}=\text{N}$ ✓；$C_L=2.15$ 偏大，但帆是高度弯的薄翼，$C_L$ 到 $1.5$ 是实测常见值，量级合理。

**读法：** 帆船「逆风前进」靠的是**升力的前向分量**，不是「风推着走」——把帆当阻力板理解，逆风就永远解释不通。**这也是「伯努利 vs 牛顿」之争里最容易被忽略的一点：真正起作用的是环量。**

**7.18** **思路**：二维剖面升力公式 $L'=\frac12\rho U^{2}cC_L$，直接代入。

$$L'=\frac12\rho U^{2}cC_L=\frac12\times1.2\times(200)^{2}\times0.3\times0.6=4.3\times10^{3}\ \text{N/m}.$$

**结果：** 单位展长升力约 $4.3\ \text{kN/m}$。

**检验：** 量纲 ✓；$200\ \text{m/s}$ 的剖面速度与客机巡航同量级，$L'$ 与 7.16 的 $4.7\ \text{kN/m}$ 相当，合理 ✓。

**读法：** 旋翼剖面速度沿展向变化（$U\pm\Omega r$），后退叶片一侧相对速度小、**更容易失速**。所以桨叶要扭转、变距，尖端要做后掠或特殊翼型——**「后退叶片失速」是直升机速度的硬上限之一。**

**7.19** **思路**：(a) 平飞升力 = 重力，单位展长升力除以翼展得 $L'$，再由 $L'=\rho U\Gamma$ 反解 $\Gamma$；(b) 用库塔公式反解攻角；(c) 速度变了，重算一遍。

(a) $L=mg=500\times9.8=4.9\times10^{3}\ \text{N}$，$L'=L/b=327\ \text{N/m}$，

$$\Gamma=\frac{L'}{\rho U}=\frac{327}{1.2\times25}=10.9\ \text{m}^{2}/\text{s}.$$

(b) $\sin(\alpha-\theta_T)=\dfrac{\Gamma}{4\pi UR}=\dfrac{10.9}{4\pi\times25\times0.5}=0.0694$，$\alpha-\theta_T=3.98^\circ$，$\alpha=2.0^\circ$。

(c) $U=30$：$L'$ 不变（仍等于重力除以翼展），

$$\Gamma'=\frac{327}{1.2\times30}=9.08,\qquad
\sin(\alpha'-\theta_T)=\frac{9.08}{4\pi\times30\times0.5}=0.0482,$$

$\alpha'-\theta_T=2.76^\circ$，$\alpha'=0.76^\circ$。

**结果：** (a) $L'=327\ \text{N/m}$，$\Gamma=10.9\ \text{m}^{2}/\text{s}$；(b) $\alpha=2.0^\circ$；(c) $U=30\ \text{m/s}$ 时 $\alpha=0.8^\circ$。

**检验：** $\Gamma\propto1/U$、$\sin(\alpha-\theta_T)\propto1/U^{2}$——速度从 $25$ 到 $30$，攻角从 $2.0^\circ$ 降到 $0.8^\circ$，比例 $0.48$ 与 $(25/30)^{2}=0.69$ 大致同量级（小角度下 $\sin\approx$ 线性）✓。

**读法：** 飞得越快，需要的攻角越小——**所以巡航时机头是「压平」的，而降落时必须拉大攻角**。滑翔机翼展大（$AR$ 大）正是为了在低速时少付出诱导阻力。

**7.20** **思路**：$C_L=2\pi\sin(\alpha-\theta_T)$，攻角同为 $5^\circ$，只改 $\theta_T$。

结冰前：$\alpha-\theta_T=5^\circ-(-4^\circ)=9^\circ$，$C_L=2\pi\sin9^\circ=0.983$。
结冰后：$\alpha-\theta_T=5^\circ-(-1^\circ)=6^\circ$，$C_L'=2\pi\sin6^\circ=0.657$。

下降比例

$$\frac{C_L'-C_L}{C_L}=\frac{0.657-0.983}{0.983}=-33\% .$$

**结果：** $C_L$ 从 $0.98$ 降到 $0.66$，下降 $33\%$。

**检验：** $\sin6^\circ/\sin9^\circ=0.669$ ✓；若按线性近似 $\frac{6}{9}=0.67$，一致 ✓。

**读法：** 结冰不是「表面粗糙一点」：它把弯度削掉，等于把零升力角从 $-4^\circ$ 抬到 $-1^\circ$，**升力直接砍掉三分之一**。这就是飞机必须除冰的定量理由——升力余量本来就只有几度攻角。

**7.21** **思路**：襟翼的作用是增大弯度 → $\theta_T$ 更负 → 同等攻角下 $\alpha-\theta_T$ 更大 → $C_L$ 更大。

取起飞攻角 $8^\circ$。

不放襟翼，$\theta_T=-3^\circ$：$\alpha-\theta_T=11^\circ$，

$$C_L=2\pi\sin11^\circ=1.198 .$$

放襟翼，$\theta_T=-10^\circ$：$\alpha-\theta_T=18^\circ$，

$$C_L'=2\pi\sin18^\circ=1.939 .$$

增加比例 $(1.939-1.198)/1.198=62\%$。

**结果：** $C_L$ 从 $1.20$ 升到 $1.94$，增加 $62\%$。

**检验：** $\sin18^\circ/\sin11^\circ=0.309/0.191=1.62$ ✓；$C_L'=1.94$ 已接近常见翼型的最大升力系数（$1.5$–$2.0$），说明襟翼把翼型「用到了极限」✓。

**读法：** 襟翼不改变升力线斜率，它**平移零升力角**。所以同样的速度、同样的机身姿态，升力多六成——**这就是「起飞距离能缩短三分之一」的来源。**

**7.22** **思路**：自转给环量 $\Gamma=2\pi R^{2}\omega$，马格努斯力 $F=\rho U\Gamma h$；风阻用 $F_D=\frac12\rho U^{2}DC_Dh$ 对照。

$R=0.15\ \text{m}$，$\omega=2\pi\times1=6.28\ \text{rad/s}$：

$$\Gamma=2\pi R^{2}\omega=2\pi\times0.0225\times6.28=0.888\ \text{m}^{2}/\text{s},$$

$$L'=\rho U\Gamma=1.2\times20\times0.888=21.3\ \text{N/m},\qquad
F=L'h=21.3\times15=320\ \text{N}.$$

风阻：

$$F_D=\frac12\rho U^{2}DC_Dh=\frac12\times1.2\times400\times0.3\times1.2\times15=1.3\times10^{3}\ \text{N}.$$

**结果：** 侧向力约 $3.2\times10^{2}\ \text{N}$，是风阻（$1.3\times10^{3}\ \text{N}$）的约四分之一。

**检验：** 量纲 $\text{N/m}\cdot\text{m}=\text{N}$ ✓；两力量级相近，说明马格努斯效应不可忽略 ✓。

**读法：** 马格努斯力垂直于风，**直接激发横向振动**（烟囱、桅杆、拉索的涡激振动就是同一类问题）。工程上要么抑制自转，要么加螺旋线（扰流条）打散环量。

**7.23** **思路**：平板对应 $R=a$，而儒可夫斯基平板翼型的弦长是 $c=4a$（像是一条长 $4a$ 的线段）。有了这个关系，两条公式（$L'=4\pi\rho U^{2}R\sin\alpha$ 与 $C_L=\frac{2L'}{\rho U^{2}c}$）就一致了。

取弦长 $c=1\ \text{m}$，则 $a=c/4=0.25\ \text{m}$，$R=a=0.25\ \text{m}$。

$$L'=4\pi\rho U^{2}R\sin\alpha
=4\pi\times1.2\times(40)^{2}\times0.25\times\sin6^\circ
=4\pi\times1.2\times1600\times0.25\times0.1045=6.3\times10^{2}\ \text{N/m}.$$

$$C_L=\frac{2L'}{\rho U^{2}c}=\frac{2\times630}{1.2\times1600\times1}=0.657 .$$

$C_L=2\pi\sin6^\circ=0.657$ ✓，两条路一致。

换成厚 $12\%$ 的对称翼型：$\theta_T$ 仍为 $0$（对称、无弯度），$R/c$ 从 $1/4$ 略变，$C_L=2\pi\sin6^\circ$ 几乎不变（$2\%$ 以内）。

**结果：** $L'\approx6.3\times10^{2}\ \text{N/m}$，$C_L\approx0.66$；换成对称厚翼型，$C_L$ 基本不变。

**检验：** 两种算法给出同一个 $L'$ ✓；$C_L=2\pi\sin6^\circ$ ✓；量纲 $\text{kg/m}^3\cdot\text{m}^2/\text{s}^2\cdot\text{m}=\text{N/m}$ ✓。

**读法：** 对称翼型的升力线斜率与厚度无关，**厚度买的是失速特性、结构强度和内部容积，不是升力**。平板在真实流动里会在前缘就分离，所以「平板飞得起来」只是理想化的结论。

**7.24** **思路**：库塔条件的前提是「后驻点落在尖后缘、流动平滑离开」。失速 = 边界层分离 = 流动不再贴着后缘走。

库塔条件的数学表述是 $W'(a)=0$：后驻点落在后缘，后缘速度有限。它成立的前提有两条：

1. **流动附着**（边界层贴着物面走到后缘）；
2. **后缘是尖的**（有唯一确定的「后缘点」）。

失速时边界层在后缘之前就分离，流体不再绕过后缘，**后驻点离开后缘**——$W'(a)\neq0$ 的解反而更接近真实流场（后缘速度有限但驻点不在后缘）。此时按库塔条件算出的 $\Gamma_K$ 比真实环量大，升力被高估。

**结果：** 失速破坏的是「附着流」这条前提（不是数学本身）：$\Gamma$ 不再由 $\Gamma_K$ 给出，实测升力下降。

**检验：** 失速前（$\alpha<12^\circ$）理论斜率与实验吻合，失速后实验曲线立刻跌破直线——**断裂点正是「附着」失效的地方** ✓。

**读法：** 库塔条件不是定理，是一条**从真实流动里提炼的经验约束**。它失效的地方（失速、圆后缘、大分离）正是这门理论适用边界的具体位置。
**7.25** **思路**：压力的合力可以写成复积分。关键两步：把 $p\,\mathrm{d}\bar z$ 型积分换成 $\frac{\mathrm{i}\rho}{2}(w')^{2}\mathrm{d}z$；再用「物面是流线」把 $\mathrm{d}\bar z$ 与 $\mathrm{d}z$ 对齐。

起点是压力沿物面积分。法向朝外、压力朝内，二维情形下

$$F_x-iF_y=-\oint p\left(\mathrm{d}y+i\,\mathrm{d}x\right)
=i\oint p\,\mathrm{d}\bar z,$$

这里用了 $\mathrm{d}\bar z=\mathrm{d}x-i\,\mathrm{d}y$ 与 $\mathrm{d}y+i\,\mathrm{d}x=i\,\mathrm{d}\bar z$。

代入伯努利方程 $p=p_\infty+\frac12\rho\left(U^{2}-|w'|^{2}\right)$，常数项在闭合回路上积分为零：

$$F_x-iF_y=-\frac{i\rho}{2}\oint|w'|^{2}\,\mathrm{d}\bar z .$$

**关键一步：** 物面是流线，$\psi=\operatorname{Im}w$ 为常数，于是沿物面

$$\mathrm{d}w=w'\,\mathrm{d}z=\mathrm{d}\phi+i\,\mathrm{d}\psi=\mathrm{d}\phi\ (\text{实}),$$

所以 $\mathrm{d}\bar z$ 与 $\mathrm{d}z$ 只差一个实因子；更直接地，可以证明沿物面 $\overline{w'\,\mathrm{d}z}=w'\,\mathrm{d}\bar z$，从而 $|w'|^{2}\mathrm{d}\bar z=(w')^{2}\mathrm{d}z$。代回：

$$F_x-iF_y=\frac{i\rho}{2}\oint\left(\frac{\mathrm{d}w}{\mathrm{d}z}\right)^{2}\mathrm{d}z .$$

**结果：** 布拉修斯定理 $F_x-iF_y=\frac{i\rho}{2}\oint(w')^{2}\,\mathrm{d}z$。

**检验：** 对无环量圆柱，$(w')^{2}$ 没有 $1/z$ 项，积分为零，阻力为零 ✓（与达朗贝尔佯谬一致）。量纲：$\rho\cdot(w')^{2}\cdot\mathrm{d}z=\frac{\text{kg}}{\text{m}^{3}}\cdot\frac{\text{m}^{2}}{\text{s}^{2}}\cdot\text{m}=\frac{\text{kg}}{\text{m}\cdot\text{s}^{2}}=\text{N/m}$ ✓（单位展长的力）。

**读法：** 这个定理的全部价值在于**围道可以挪到无穷远**：那里 $w$ 的洛朗展开已知，压力积分变成一个留数。**「积分难」被换成了「找留数」。**

**7.26** **思路**：阻力 = $F_x$，由布拉修斯定理只看 $(w')^{2}$ 的 $1/z$ 系数；无环量时没有 $1/z$，阻力严格为零。真实阻力则要回到粘性。

无环量圆柱：

$$\frac{\mathrm{d}w}{\mathrm{d}z}=U\left(1-\frac{a^{2}}{z^{2}}\right),\qquad
\left(\frac{\mathrm{d}w}{\mathrm{d}z}\right)^{2}=U^{2}-\frac{2U^{2}a^{2}}{z^{2}}+\frac{U^{2}a^{4}}{z^{4}} .$$

$1/z$ 的系数为零，围道积分为零，所以

$$F_x-iF_y=0\;\Longrightarrow\;F_x=F_y=0 .$$

真实圆柱在 $Re=10^{5}$ 时 $C_D\approx1.2$，阻力几乎全部来自**边界层分离造成的尾流低压**（压差阻力）；摩擦阻力只占百分之几。

**结果：** 理想无粘无旋流的阻力**严格为零**；真实圆柱 $C_D\sim1.2$（$Re=10^{5}$），主要来自尾流压差。

**检验：** 数量级：单位长度阻力 $\frac12\rho U^{2}D C_D$，取 $U=10$、$D=0.1$、$C_D=1.2$，得 $72\ \text{N/m}$——与实验同量级 ✓。若按理想理论算，这个数只能是零。

**读法：** **理想理论算不出阻力，这不是缺陷而是结论**：阻力全部来自模型里没有的东西（粘性、分离）。工程上阻力靠经验公式与风洞补，升力靠这套理论算——分工非常清楚。

**7.27** **思路**：后缘处 $z'(\zeta)=0$，所以速度 $w'=W'/z'$ 的有限性完全取决于 $W'$ 在后缘有没有零点。把两者都在 $\zeta=a$ 附近展开，看阶数。

在后缘附近设 $\zeta=a+u$，$u$ 很小。映射展开（7.3.4 节）：

$$z-2a\approx\frac{u^{2}}{a}\;\Longrightarrow\;\frac{\mathrm{d}z}{\mathrm{d}\zeta}\approx\frac{2u}{a}.$$

复势展开：$W(\zeta)=W(a)+W'(a)u+\frac12W''(a)u^{2}+\cdots$，所以 $W'\approx W'(a)+W''(a)u$。于是

$$\frac{\mathrm{d}w}{\mathrm{d}z}=\frac{W'}{z'}\approx\frac{W'(a)+W''(a)u}{2u/a}
=\frac{aW'(a)}{2u}+\frac{aW''(a)}{2}+\cdots$$

若 $W'(a)\neq0$，第一项按 $|u|^{-1}$ 发散；因为 $u\propto(z-2a)^{1/2}$，换成 $z$ 坐标就是 $|z-2a|^{-1/2}$——薄板边缘的奇异。

库塔条件要求 $W'(a)=0$，第一项消失：

$$\frac{\mathrm{d}w}{\mathrm{d}z}\to\frac{a}{2}W''(a)\quad(\zeta\to a),$$

**有限**。

**结果：** 库塔条件 $W'(a)=0$ ⟺ 后缘速度有限，极限值 $\frac{a}{2}W''(a)$；不满足时速度按 $|z-2a|^{-1/2}$ 发散。

**检验：** 量纲：$[W'']\cdot\text{m}$ 与 $w'$ 的量纲（速度）一致 ✓；$\Gamma=\Gamma_K$ 时后缘速度与来流同量级（图 7.6 的实线），非库塔值时冲出图外——与展开的 $1/u$ 一致 ✓。

**读法：** 「后缘速度有限」在数学上就是「$W'$ 在后缘有一阶零点」。**库塔条件的全部内容就是这一句**：它把「取哪个 $\Gamma$」翻译成「$W'$ 的零点放在哪」。

**7.28** **思路**：用涡片代替翼型。边界条件（法向速度为零）给出一个奇异积分方程，后缘条件 $\gamma(a)=0$ 选出唯一解；总环量是 $\gamma$ 的积分。

设涡强 $\gamma(x)$ 布在弦 $[-a,a]$ 上（弦长 $2a$），来流 $U$、攻角 $\alpha$。涡片诱导的法向速度

$$v_n(x)=\frac{1}{2\pi}\operatorname{P.V.}\int_{-a}^{a}\frac{\gamma(x')}{x-x'}\,\mathrm{d}x',$$

物面条件 $v_n(x)=-U\sin\alpha\approx-U\alpha$。

后缘条件 $\gamma(a)=0$（否则后缘速度发散，与库塔条件矛盾）。满足这两个条件的解是

$$\gamma(x)=2U\sin\alpha\sqrt{\frac{a+x}{a-x}} .$$

（验证：$\gamma(a)=0$ ✓；$\gamma(-a)$ 发散，对应前缘吸力峰，物理上确实存在。）

总环量

$$\Gamma=\int_{-a}^{a}\gamma(x)\,\mathrm{d}x
=2U\sin\alpha\int_{-a}^{a}\sqrt{\frac{a+x}{a-x}}\,\mathrm{d}x .$$

换元 $x=a\cos\theta$（$\theta$ 从 $\pi$ 到 $0$）：$\sqrt{\frac{a+x}{a-x}}=\cot\frac{\theta}{2}$，$\mathrm{d}x=-a\sin\theta\,\mathrm{d}\theta$，

$$\int_{-a}^{a}\sqrt{\frac{a+x}{a-x}}\,\mathrm{d}x
=\int_0^{\pi}a\sin\theta\cot\frac{\theta}{2}\,\mathrm{d}\theta
=a\int_0^{\pi}2\cos^{2}\frac{\theta}{2}\,\mathrm{d}\theta=\pi a .$$

所以 $\Gamma=2\pi Ua\sin\alpha$（取向取顺时针，符号为负）。

$$L'=\rho U|\Gamma|=2\pi\rho U^{2}a\sin\alpha
\;\Longrightarrow\;
C_L=\frac{L'}{\frac12\rho U^{2}(2a)}=2\pi\sin\alpha .$$

**结果：** $\gamma(x)=2U\sin\alpha\sqrt{\frac{a+x}{a-x}}$，$\Gamma=-2\pi Ua\sin\alpha$，$C_L=2\pi\sin\alpha$。

**检验：** 环量积分 $\int\sqrt{\frac{a+x}{a-x}}\mathrm{d}x=\pi a$ 可用几何面积验证（它是半圆面积的变形）；与保角映射的结果 $C_L=2\pi\sin\alpha$ 完全一致 ✓——**两条完全不同的路给出同一个数，说明这个数只依赖几何。**

**读法：** 薄翼理论的这个结果说明：**升力线斜率与翼型形状无关，只与「后缘闭合」这一条有关**。保角映射算的是同一个东西，只是一个用复变、一个用奇异积分。

**7.29** **思路**：地面是流线（法向速度为零），用镜像法满足它：在地面下方放一个反号的翼型，叠加后地面自动成为流线。

设真实翼型在高度 $h$，环量 $\Gamma$。地面 $y=-h$ 要求 $v_y=0$。放一个镜像翼型在 $y=-3h$（关于地面反射），环量取 $-\Gamma$（反向），则地面上每一点的 $v_y$ 恰好抵消：

$$v_y^{\text{真实}}(x,-h)+v_y^{\text{镜像}}(x,-h)=0 .$$

镜像涡在真实翼型处诱导的速度方向与真实翼型自身的下洗**相反**，所以净下洗减小：

$$w_i^{\text{eff}}=w_i\left(1-\frac{\text{镜像贡献}}{\text{自诱导}}\right)
\approx w_i\left(1-\frac{1}{1+(2h/b)^{2}}\right)$$

（$b$ 为翼展量级；$h\to0$ 时镜像贴上来，抵消最强）。

有效攻角 $\alpha_{\text{eff}}=\alpha-w_i^{\text{eff}}/U$ 变大 → 升力上升；诱导阻力 $C_{D,i}=C_L\alpha_i$ 变小。

**结果：** $h$ 越小，镜像越近，下洗被抵消得越多：升力上升、诱导阻力下降。$h\gg b$ 时效应消失。

**检验：** $h\to\infty$ 时镜像趋于无穷远，诱导速度趋于零 → 回到自由飞行 ✓；$h\to0$ 时镜像与真实翼型重合（反号），下洗被完全抵消 → 诱导阻力趋于零（理想极限）✓。

**读法：** 地效飞行器贴水面飞（$h$ 只有翼展的十分之一）能省大量燃油，原理就在这里；风洞实验里模型离壁太近会「虚假增升」，也是同一个镜像效应。

**7.30** **思路**：椭圆环量分布的特殊之处是**下洗沿展向是常数**，于是 $\alpha_i$ 与 $y$ 无关，可以解析积分。

设环量分布

$$\Gamma(y)=\Gamma_0\sqrt{1-\left(\frac{2y}{b}\right)^{2}},\qquad -b/2\le y\le b/2 .$$

由升力线理论，下洗速度

$$w_i(y)=\frac{1}{4\pi}\operatorname{P.V.}\int_{-b/2}^{b/2}\frac{\mathrm{d}\Gamma/\mathrm{d}y'}{y-y'}\,\mathrm{d}y' .$$

对椭圆分布，这个积分与 $y$ 无关（这是它的定义性质），结果为

$$w_i=\frac{\Gamma_0}{2b}.$$

总升力

$$L=\rho U\int_{-b/2}^{b/2}\Gamma\,\mathrm{d}y=\rho U\Gamma_0\frac{\pi b}{4}
\;\Longrightarrow\;
\Gamma_0=\frac{4L}{\pi\rho Ub}.$$

又 $L=\frac12\rho U^{2}SC_L$，所以 $\Gamma_0=\frac{2UcC_L}{\pi}$（$S=bc$）。于是

$$\alpha_i=\frac{w_i}{U}=\frac{\Gamma_0}{2bU}=\frac{C_L}{\pi\,b/c}=\frac{C_L}{\pi AR},\qquad AR=\frac{b^{2}}{S}=\frac{b}{c} .$$

诱导阻力

$$D_i=L\alpha_i=\frac12\rho U^{2}S\,C_L\cdot\frac{C_L}{\pi AR}
\;\Longrightarrow\;
C_{D,i}=\frac{C_L^{2}}{\pi AR} .$$

**结果：** $\alpha_i=\dfrac{C_L}{\pi AR}$，$C_{D,i}=\dfrac{C_L^{2}}{\pi AR}$。

**检验：** 量纲：$C_L$、$AR$ 都无量纲 ✓；$AR\to\infty$ 时 $\alpha_i\to0$、$C_{D,i}\to0$，回到二维 ✓；$C_L$ 固定时 $C_{D,i}\propto1/AR$，展弦比加倍阻力减半 ✓。

**读法：** 诱导阻力是「用有限翼展产生升力」的税。**滑翔机翼展 $15$–$20\ \text{m}$、战斗机只有 $3$–$4\ \text{m}$，差别全在这个 $1/AR$ 上**——滑翔机要省油（省「能」），战斗机要机动。

**7.31** **思路**：二维理论给斜率 $2\pi=6.28$。实测斜率低 → 有限展长（$2\pi/(1+2/AR)$）；实测斜率高 → 可压性（$2\pi/\sqrt{1-M^{2}}$）。零升力角单独反映弯度。

(a) 组：斜率 $5.1$，是二维值的 $81\%$。有限展长修正公式

$$\frac{\mathrm{d}C_L}{\mathrm{d}\alpha}=\frac{2\pi}{1+2/AR}\;\Longrightarrow\;
1+\frac{2}{AR}=\frac{6.28}{5.1}=1.23\;\Longrightarrow\;AR\approx8.6 .$$

零升力角 $-2.8^\circ$ → 中等弯度。

(b) 组：斜率 $6.2$，已接近 $2\pi$（$99\%$），说明展弦比很大（$AR\gtrsim50$，如机翼加端板或风洞二维段）；也可能叠加了可压性增升。零升力角 $-6.1^\circ$ → 弯度大。

**结果：** (a) 三维效应明显（$AR\approx9$）、弯度中等；(b) 接近二维、弯度大（可能还有可压性）。

**检验：** $AR\approx8.6$ 与常见运输机翼（$AR=7$–$10$）吻合 ✓；斜率 $5.1<6.28$ 且零升力角不为零，两条信息互相独立，说明「斜率看三维、零升力角看弯度」的判读是对的 ✓。

**读法：** 同一张升力曲线，**斜率告诉你「翼展够不够」，零升力角告诉你「弯度够不够」**。风洞数据判读的第一步就是把这两件事分开。

**7.32** **错。** 保角映射保持的是**拉普拉斯方程的形式**：因为 $\nabla^{2}$ 在坐标变换下只多出一个因子 $|f'|^{2}$，方程仍是 $\nabla^{2}\phi=0$。纳维–斯托克斯方程含一阶对流项 $(\boldsymbol{v}\cdot\nabla)\boldsymbol{v}$ 和非线性项，映射之后会变成含 $f'$、$f''$ 的变系数方程，**形式不保持**。

**例子：** 绕圆柱的斯托克斯流（$Re\ll1$）在儒可夫斯基映射下不会变成「绕翼型的斯托克斯流」——粘性项与对流项的相对权重在映射后改变。**「能搬」是调和函数的特权，不是所有方程的。**

**7.33** **错。** 没有任何物理理由要求「同时到达」：实验（烟线、粒子示踪）直接看到上表面气流**先**到后缘；而且「路程长所以要快」给不出任何定量结果（快多少？为什么？）。

**正确图像：** 上表面更快是**环量**的结果——环量被后缘条件选定之后，上表面速度 $v_\theta$ 由运动学定死，压力由伯努利定死。**「先到」是被解释的对象，不是解释。**

**例子：** 平板翼型（零厚度，上下表面路程**完全相等**）照样有升力（$C_L=2\pi\sin\alpha$）。这一条直接否掉「路径差」说法。

**7.34** **错。** 升力恰恰是势流理论算出来的：$L=\rho U\Gamma$，$\Gamma$ 由库塔条件定，而且算得相当准（升力线斜率、零升力角都对）。它算不出的只有**阻力**。

**例子：** 客机 $C_L=0.45$、$\alpha\approx1^\circ$ 的估计与实测同量级；而阻力 $C_D$ 必须靠风洞。**一个只算升力的理论，仍然是机翼设计的主干工具。**

**7.35** **错。** 映射只提供「把圆柱的结果搬过去」的通道；$\Gamma$ 是**物理条件**（库塔条件）定的，不是映射给的。同一个翼型可以用不同的映射（儒可夫斯基、Kármán–Trefftz）描述，$\Gamma$ 不变。

**例子：** 换映射会改变 $R$、$\theta_T$ 这些几何参数，但把新参数代回 $\Gamma_K=4\pi UR\sin(\theta_T-\alpha)$，得到的 $\Gamma$ 与物理一致——**因为库塔条件说的是「后缘速度有限」，这是流场的性质，与用什么坐标描述无关。**

**7.36** **错。** $\Gamma$ 不是自由参数：它由「后缘速度有限」唯一确定，$\Gamma_K=4\pi UR\sin(\theta_T-\alpha)$。任意取 $\Gamma$ 会得到后缘速度发散的**非物理解**（图 7.6 的虚线）。

**例子：** 取 $\Gamma=1.15\Gamma_K$，后缘速度按 $|z-2a|^{-1/2}$ 发散，压力趋于负无穷——真实的边界层做不到这一点，流动会分离。**「取大一点升力大一点」在数学上成立、在物理上不成立。**

**7.37** **对，但要限定「对」在哪里。** 尖后缘提供了一个**唯一确定的**后缘点，库塔条件才能表述成「后驻点落在后缘」；圆后缘没有这个特殊位置，$\Gamma$ 不定，升力就有任意性——**这正是真实机翼后缘必须尖（或很薄）的原因。**

**例子：** 圆后缘翼型的实验数据：升力随攻角有一大片「迟滞」和不确定性（环量取决于分离点在哪），而尖后缘翼型的升力线干净地与 $2\pi$ 斜率重合。**尖后缘不是美学，是把环量钉死的几何装置。**

**7.38** **错。** 斜率确实与厚度几乎无关（薄翼理论里 $R/c$ 只进入一个整体因子），但厚度决定：**失速攻角**（厚翼失速更晚）、**结构强度**（主梁高度）、**内部容积**（油箱）、**波阻**（跨声速时厚度直接决定临界马赫数）。

**例子：** 客机翼型厚 $10\%$–$13\%$（要装油、要结构），战斗机 $4\%$–$6\%$（要薄、要小波阻），滑翔机 $10\%$–$15\%$。**斜率相同，用途完全不同——「无关」只说明增益固定，不说明形状可以随便。**

**7.39** **错。** 理想无粘无旋流的阻力**严格为零**（$F_x=0$，达朗贝尔佯谬），二维势流理论算不出任何阻力。

**例子：** 用 $w=U(z+a^{2}/z)$ 算 $(w')^{2}$ 的洛朗展开，没有 $1/z$ 项，$F_x=0$——这不是近似，是精确结论。真实阻力来自粘性、分离与诱导，全在模型之外。

**7.40** **错。** 库塔条件是**物理条件**，不是数学定理。势流方程对任意 $\Gamma$ 都给出合法解；「后缘速度有限」这条要求是从真实流动（粘性、附着流、尖后缘）里提炼出来，再**额外加给**理想模型的。

**例子：** 数学上，$\Gamma=0.8\Gamma_K$ 的解完全满足方程、物面条件和远场条件——只是后缘速度发散。没有任何定理排除它，排除它的是物理观察。**这也解释了它的适用边界：失速、圆后缘、大分离时，条件失效。**

## 第 8 章

> 每题按「思路、过程、结果、检验、读法」五段写。先自己想，卡住了再看对应那一段。
> 引用正文节号（如「见 8.6.1」）只是指路，过程仍写全。全书约定：正变换 $\tilde f(k)=\int f(x)e^{-ikx}\mathrm{d}x$，逆变换带 $1/2\pi$。

## A 组　基本运算

**8.1**

**思路**：矩形脉冲只有有限支撑，直接按定义积分就行，分段点正好是积分限。算完看零点位置：**零点间隔与脉宽成反比**，这就是「时宽带宽积」在这条式子里的具体形态。

**过程**：矩形 $f=1$（$|x|<a/2$），按定义

$$\tilde f(k)=\int_{-a/2}^{a/2}e^{-ikx}\mathrm{d}x=\left[\frac{e^{-ikx}}{-ik}\right]_{-a/2}^{a/2}=\frac{e^{-ika/2}-e^{ika/2}}{-ik}=\frac{2\sin(ka/2)}{k}.$$

用 $\mathrm{sinc}\,u=\sin u/u$ 把它写成无量纲形式，令 $u=ka/2$：

$$\tilde f(k)=a\,\frac{\sin u}{u}=a\,\mathrm{sinc}\!\left(\frac{ka}{2}\right).$$

零点：$\sin(ka/2)=0$ 且 $k\ne0$，即 $ka/2=n\pi$，$k=\frac{2n\pi}{a}$，$n=\pm1,\pm2,\dots$；$k=0$ 是最大值 $\tilde f(0)=a$（不是零点）。

**结果**：

$$\tilde f(k)=\frac{2\sin(ka/2)}{k}=a\,\mathrm{sinc}\!\left(\frac{ka}{2}\right),\qquad \text{零点 }k=\frac{2n\pi}{a}\ (n=\pm1,\pm2,\dots).$$

**检验**：(i) $k\to0$：$\sin(ka/2)/(ka/2)\to1$，所以 $\tilde f(0)=a$，等于脉冲面积 $\int f\,\mathrm{d}x=a$ ✓。(ii) 偶函数：$\tilde f(-k)=\tilde f(k)$，与 $f$ 是实偶函数一致（实偶的谱是实偶）✓。(iii) 量纲：$f$ 无量纲、$\mathrm{d}x$ 是长度，所以 $\tilde f$ 的量纲是长度 ✓。

**读法**：脉宽 $a$ 只出现在 $ka/2$ 这个组合里——**脉宽减半，零点全部外移一倍，谱整体拉宽一倍**。主瓣宽度 $\Delta k=4\pi/a$，与时宽 $a$ 的乘积是常数 $4\pi$。这就是「窄脉冲必然宽带」，也是 8.6.4 用带宽换距离分辨率的出发点。

**8.2**

**思路**：$e^{-a|x|}$ 在 $x=0$ 处不可导，但分两段各自光滑，**拆成 $x<0$ 与 $x>0$ 两段积分**即可。被积函数是复指数，注意收敛性：$x<0$ 时要 $a-ik$ 的实部为正才能积（$a>0$ 保证），$x>0$ 时同理。

**过程**：

$$\tilde f(k)=\int_{-\infty}^{0}e^{ax}e^{-ikx}\mathrm{d}x+\int_{0}^{\infty}e^{-ax}e^{-ikx}\mathrm{d}x=\int_{-\infty}^{0}e^{(a-ik)x}\mathrm{d}x+\int_0^\infty e^{-(a+ik)x}\mathrm{d}x.$$

第一段：$\int_{-\infty}^0e^{(a-ik)x}\mathrm{d}x=\frac{1}{a-ik}$（上限为零给 $1$，下限给 $0$）。第二段：$\int_0^\infty e^{-(a+ik)x}\mathrm{d}x=\frac{1}{a+ik}$。相加：

$$\tilde f(k)=\frac{1}{a-ik}+\frac{1}{a+ik}=\frac{(a+ik)+(a-ik)}{a^2+k^2}=\frac{2a}{a^2+k^2}.$$

**结果**：

$$\tilde f(k)=\frac{2a}{a^2+k^2}\qquad(a>0).$$

**检验**：(i) 实、偶、正：与 $f$ 是实偶函数一致 ✓（实偶 ⇒ 谱实偶）。(ii) $k=0$：$\tilde f(0)=2/a$，而 $\int e^{-a|x|}\mathrm{d}x=2\int_0^\infty e^{-ax}\mathrm{d}x=2/a$ ✓。(iii) 极限 $a\to0^+$：$\frac{2a}{a^2+k^2}$ 的面积 $\int\mathrm{d}k=2\pi$，峰高 $2/a\to\infty$，正是 $2\pi\delta(k)$——与 $\mathcal{F}[1]=2\pi\delta(k)$ 吻合 ✓。

**读法**：$\frac{2a}{a^2+k^2}$ 是**洛伦兹线型**，和第 6 章受迫振子的共振曲线 $\frac{1}{(\omega_0^2-\omega^2)^2+\gamma^2\omega^2}$ 是同一族形状（后者是它的平方）。指数衰减 ↔ 洛伦兹谱，这一对变换在光谱学里天天用：**测一条谱线的宽度，就知道激发态的寿命**（$\Delta\nu\sim1/\tau$）。

**8.3**

**思路**：平移性质 $\mathcal{F}[f(x-x_0)]=e^{-ikx_0}\tilde f(k)$ 是现成的（8.4.1 的表），本题只要把两个已知变换对套上去，再从模与辐角读幅度谱和相位谱。

**过程**：对 $\delta$：$\tilde\delta(k)=1$，所以

$$\mathcal{F}[\delta(x-x_0)]=e^{-ikx_0}\cdot1=e^{-ikx_0}.$$

对 $e^{-a|x|}$：由 8.2，$\mathcal{F}[e^{-a|x|}]=\frac{2a}{a^2+k^2}$，所以

$$\mathcal{F}\left[e^{-a|x-x_0|}\right]=e^{-ikx_0}\frac{2a}{a^2+k^2}.$$

写成模与辐角：$|\tilde f(k)|=\frac{2a}{a^2+k^2}$（与 $x_0$ 无关），$\arg\tilde f(k)=-kx_0$（对 $k$ 线性）。

**结果**：

$$\mathcal{F}[\delta(x-x_0)]=e^{-ikx_0},\qquad \mathcal{F}\left[e^{-a|x-x_0|}\right]=\frac{2a\,e^{-ikx_0}}{a^2+k^2}.$$

**幅度谱不变**（$\delta$ 是常数 1，另一个是 $\frac{2a}{a^2+k^2}$）；**相位谱多了一个线性项 $-kx_0$**。

**检验**：(i) $x_0=0$ 时退回 8.2 ✓。(ii) 相位对 $k$ 求导：$\frac{d}{dk}(-kx_0)=-x_0$，即**相位的斜率等于时延**（群时延），量纲：相位无量纲、$k$ 是 $1/$长度，所以斜率是长度 ✓。(iii) 帕塞瓦尔：$\int|\tilde f|^2\mathrm{d}k$ 与 $x_0$ 无关，能量不随平移变 ✓。

**读法**：平移不改幅度谱、只加线性相位——这是干涉、相控阵、脉冲压缩的共同基础：**改动相位就能「挪动」波形**，不改相位就只能改形状。

**8.4**

**思路**：高斯积分必须用**配方**把它变成标准形式 $\int e^{-u^2/(2\sigma^2)}\mathrm{d}u=\sigma\sqrt{2\pi}$。配方之后剩下的因子与 $x$ 无关，可以提到积分号外面。这条路是 8.6.1 的原样重做，不能跳。

**过程**：指数部分合并：

$$-\frac{x^2}{2\sigma^2}-ikx=-\frac{(x+ik\sigma^2)^2}{2\sigma^2}-\frac{\sigma^2k^2}{2}.$$

（验证：右边展开 $\frac{x^2+2ik\sigma^2x-k^2\sigma^4}{2\sigma^2}+\frac{\sigma^2k^2}{2}$ 的 $x$ 项为 $ikx$，常数项抵消 ✓。）于是

$$\tilde f(k)=e^{-\sigma^2k^2/2}\int_{-\infty}^{\infty}e^{-(x+ik\sigma^2)^2/(2\sigma^2)}\mathrm{d}x.$$

令 $u=x+ik\sigma^2$，积分路径整体上移 $k\sigma^2$。被积函数 $e^{-u^2/(2\sigma^2)}$ 在全平面解析，沿矩形回路积分为零，上下两条水平边的贡献相等（竖直边趋于零），所以**沿实轴的积分等于沿平移后直线的积分**：

$$\int_{-\infty}^{\infty}e^{-u^2/(2\sigma^2)}\mathrm{d}u=\sigma\sqrt{2\pi}.$$

**结果**：

$$\tilde f(k)=\sigma\sqrt{2\pi}\,e^{-\sigma^2k^2/2}.$$

宽度：$|f|^2\propto e^{-x^2/\sigma^2}$ 的方差是 $\sigma^2/2$，故 $\Delta x=\sigma/\sqrt2$；$|\tilde f|^2\propto e^{-\sigma^2k^2}$ 的方差是 $1/(2\sigma^2)$，故 $\Delta k=1/(\sqrt2\sigma)$。乘积

$$\Delta x\,\Delta k=\frac{\sigma}{\sqrt2}\cdot\frac{1}{\sqrt2\sigma}=\frac12.$$

**检验**：(i) $k=0$：$\tilde f(0)=\sigma\sqrt{2\pi}=\int e^{-x^2/(2\sigma^2)}\mathrm{d}x$ ✓。(ii) 量纲：$\tilde f$ 的量纲 = 函数量纲 × 长度 ✓。(iii) $\sigma\to0$：时域趋于 $\delta$，频域 $\sigma\sqrt{2\pi}e^{-\sigma^2k^2/2}\to$ 常数（因为 $\sigma\sqrt{2\pi}\to0$ 而指数趋于 1……注意这里是宽度趋于无穷的常数 $\times$ 零高度，正好是 $\delta$ 的谱在分布意义下的极限）✓。

**读法**：高斯是**唯一**使 $\Delta x\Delta k$ 取到 $1/2$ 的函数（习题 8.23 会证明等号条件），所以它被称为「最紧凑」的脉冲：给定宽度，它的谱最窄，而且没有旁瓣。激光、雷达、通信里偏爱高斯型脉冲，原因就在这里。

**8.5**

**思路**：求导性质的证明只有一步分部积分，关键是**边界项**。先写出分部积分，再讨论边界项什么时候为零、不为零时会出什么错。反例要能算出具体的错误项，不能只说「不收敛」。

**过程**：设 $f$ 可微且 $\tilde f$ 存在。

$$\int_{-\infty}^{\infty}\frac{\mathrm{d}f}{\mathrm{d}x}e^{-ikx}\mathrm{d}x=\Big[f(x)e^{-ikx}\Big]_{-\infty}^{\infty}+ik\int_{-\infty}^{\infty}f(x)e^{-ikx}\mathrm{d}x.$$

第一项是两个极限之差：

$$\Big[f e^{-ikx}\Big]_{-\infty}^{\infty}=\lim_{R\to\infty}\Big[f(R)e^{-ikR}-f(-R)e^{ikR}\Big].$$

只要 $f(\pm\infty)=0$（更弱地说，$f$ 在无穷远衰减到零），这一项为零，于是

$$\mathcal{F}\left[\frac{\mathrm{d}f}{\mathrm{d}x}\right]=ik\,\tilde f(k).$$

**条件不满足的例子**：取 $f(x)=1$（常数，不衰减）。逐点求导 $f'=0$，所以左边 $\int f'e^{-ikx}\mathrm{d}x=0$。但右边若按公式算 $ik\tilde f(k)=ik\cdot2\pi\delta(k)$，形式上也是零——看起来「碰巧对」。真正的毛病出在**有限截断**：把积分截到 $[-R,R]$，

$$\tilde f_R(k)=\int_{-R}^{R}e^{-ikx}\mathrm{d}x=\frac{2\sin kR}{k},$$

此时 $ik\tilde f_R(k)=2i\sin(kR)$，而 $\int_{-R}^{R}f'e^{-ikx}\mathrm{d}x=0$。两者相差的正是被丢掉的边界项

$$-\Big[f e^{-ikx}\Big]_{-R}^{R}=-\left(e^{-ikR}-e^{ikR}\right)=2i\sin(kR),$$

它**不随 $R$ 趋于零**。

**结果**：$\mathcal{F}[f']=ik\tilde f$ 成立的充分条件是 $f(\pm\infty)=0$（边界项消失）；$f$ 不衰减时公式在普通函数意义下失效，剩下的边界项为 $-\big[f e^{-ikx}\big]_{-\infty}^{\infty}$。

**检验**：(i) 取 $f=e^{-|x|}$（满足条件），左式 $=\mathcal{F}[-\mathrm{sgn}(x)e^{-|x|}]$，右式 $=ik\cdot\frac{2}{1+k^2}$，两者相等（可用 8.2 与求导直接核对）✓。(ii) 量纲：$ik\tilde f$ 的量纲 = $\frac{1}{L}\cdot$（函数$\times L$）= 函数/L，与 $f'$ 一致 ✓。

**读法**：求导性质是「微分方程变代数方程」的全部依据（8.3.1）。用它的第一步永远是问一句：**$f$ 在无穷远衰减吗？** 不衰减的信号（常数、正弦、阶跃）要么用 $\delta$ 处理，要么换拉普拉斯变换（8.8）。

**8.6**

**思路**：两个同宽矩形卷积，可以硬算重叠面积，也可以用卷积定理。定理更快，但**结果要能用几何验证**——这正是本题的价值：两条路互检。卷积定理说 $\mathcal{F}[f*f]=\tilde f^{\,2}$，所以先平方谱、再逆变换。

**过程**：宽度 $a$、高 1 的矩形，$\tilde f(k)=a\,\mathrm{sinc}(ka/2)$（8.1）。由卷积定理，

$$\mathcal{F}[f*f](k)=\tilde f(k)^2=a^2\,\mathrm{sinc}^2\!\left(\frac{ka}{2}\right).$$

$f*f$ 是两段线性函数的「三角形」：对 $|x|<a$，两个宽 $a$ 的区间重叠长度是 $a-|x|$，所以

$$(f*f)(x)=\int f(x-x')f(x')\mathrm{d}x'=a-|x|\quad(|x|<a),\qquad 0\ (|x|>a).$$

**结果**：

$$(f*f)(x)=a-|x|\ (|x|<a),\qquad 0\ (|x|\ge a);\qquad
\mathcal{F}[f*f]=\frac{4\sin^2(ka/2)}{k^2}.$$

**检验**：(i) 面积：$\int(f*f)\mathrm{d}x=\left(\int f\right)^2=a^2$，而三角形面积 $=\frac12\cdot2a\cdot a=a^2$ ✓。(ii) 峰值：在 $x=0$ 处 $(f*f)(0)=\int f^2=a$ ✓。(iii) 谱在 $k=0$ 处：$\tilde f(0)^2=a^2$，与面积的平方一致 ✓。(iv) 光滑性：矩形有跳变，卷积一次后变成连续折线——**卷积使函数变光滑**，与「频域乘一个衰减更快的因子」一致 ✓。

**读法**：卷积的几何意义是「滑动重叠面积」。这条在物理里到处都是：两个狭缝的衍射图样是单缝图样的平方（本题的连续版）；概率论里两个均匀分布之和是三角分布，也是同一个积分。

**8.7**

**思路**：三个都按定义积分，但各有省力的办法。$t$ 与 $t^2$ 用「乘 $t$ 等于对 $s$ 求负导数」：$\mathcal{L}[t]=-\frac{d}{ds}\mathcal{L}[1]$，$\mathcal{L}[t^2]=-\frac{d}{ds}\mathcal{L}[t]$。$e^{-3t}\cos2t$ 用频移定理：先算 $\mathcal{L}[\cos2t]$，再把 $s$ 换成 $s+3$。收敛横坐标直接看被积函数的增长指数。

**过程**：

(1) $f=t$：

$$F(s)=\int_0^\infty t e^{-st}\mathrm{d}t=\left[-\frac{t e^{-st}}{s}\right]_0^\infty+\frac1s\int_0^\infty e^{-st}\mathrm{d}t=0+\frac{1}{s^2}.$$

第二项是标准积分 $\int_0^\infty e^{-st}\mathrm{d}t=1/s$。收敛要求 $\mathrm{Re}\,s>0$。

(2) $f=t^2$：再分部一次，或直接用 $\mathcal{L}[t^n]=n!/s^{n+1}$：

$$F(s)=\int_0^\infty t^2e^{-st}\mathrm{d}t=\frac{2}{s^3},\qquad \sigma_c=0.$$

(3) $f=e^{-3t}\cos2t$：先算 $\mathcal{L}[\cos2t]=\frac{s}{s^2+4}$（查表 8.8.5，或由欧拉公式拆成两个指数）。频移定理说 $\mathcal{L}[e^{at}f(t)]=F(s-a)$，取 $a=-3$：

$$F(s)=\frac{s+3}{(s+3)^2+4}.$$

收敛横坐标：被积函数 $\sim e^{-(s+3)t}$，要求 $\mathrm{Re}\,s>-3$，故 $\sigma_c=-3$。

**结果**：

$$\mathcal{L}[t]=\frac1{s^2}\ (\sigma>0),\qquad \mathcal{L}[t^2]=\frac2{s^3}\ (\sigma>0),\qquad \mathcal{L}[e^{-3t}\cos2t]=\frac{s+3}{(s+3)^2+4}\ (\sigma>-3).$$

**检验**：(i) 量纲：$\mathcal{L}[t^n]$ 的量纲是 $\mathrm{s}^{n+1}$，$1/s^{n+1}$ 一致 ✓。(ii) 初值定理：$sF(s)\big|_{s\to\infty}\to0$ 对应 $f(0)=0$（三个函数在 $t=0$ 处分别是 $0,0,1$——第三个是 $1$，检查 $sF(s)=\frac{s(s+3)}{(s+3)^2+4}\to1$ ✓）。(iii) 极点：$1/s^2$ 在原点二阶、$\frac{s+3}{(s+3)^2+4}$ 在 $-3\pm2i$，实部等于 $\sigma_c$ ✓。

**读法**：三题分别对应三种「基本操作」：直接积分、乘 $t$（对 $s$ 求导）、频移。**收敛横坐标就是极点的实部**——这条在后面判断稳定性时反复用（8.10.3）。

**8.8**

**思路**：有理函数拆部分分式，再逐项查表。拆完之后每一项都是 $1/(s-a)$ 型，逆变换是指数。**先拆再反演**，不要直接上留数公式——本题的极点都是单极点，部分分式更省事。

**过程**：设

$$\frac{1}{(s+1)(s+2)}=\frac{A}{s+1}+\frac{B}{s+2}.$$

两边乘 $(s+1)(s+2)$：$1=A(s+2)+B(s+1)$。令 $s=-1$ 得 $1=A\cdot1$，$A=1$；令 $s=-2$ 得 $1=B\cdot(-1)$，$B=-1$。所以

$$F(s)=\frac{1}{s+1}-\frac{1}{s+2}\quad\Longrightarrow\quad f(t)=e^{-t}-e^{-2t},\qquad t>0.$$

**结果**：

$$f(t)=e^{-t}-e^{-2t}\qquad(t\ge0).$$

**检验**：(i) $t=0$：$f(0)=1-1=0$ ✓，而初值定理 $sF(s)=\frac{s}{(s+1)(s+2)}\to0$ ✓。(ii) $t\to\infty$：$f\to0$ ✓，终值定理 $sF(s)\big|_{s\to0}=0$ ✓。(iii) 中间行为：$f$ 先升后降，在 $f'=0$ 处 $t=\ln2$，峰值 $f=\frac12-\frac14=\frac14$。这与「两个不同时间常数的环节串联」的阶跃响应形状一致 ✓。

**读法**：$e^{-t}-e^{-2t}$ 是「快慢两个指数之差」，物理上是**先由快过程建立、再由慢过程收尾**。RC 电路的阶跃响应 $1-e^{-t/RC}$ 是它的一次积分（差一个常数），两者的极点相同。

**8.9**

**思路**：$F(s)=\frac{s}{s^2+4}$ 的极点在 $s=\pm2i$，都是单极点，用留数公式（8.9.3）最快：$f(t)=\sum_k\frac{P(s_k)}{Q'(s_k)}e^{s_kt}$。这里 $P=s$、$Q=s^2+4$、$Q'=2s$。

**过程**：极点 $s_1=2i$、$s_2=-2i$。

$s_1=2i$ 处的留数：$\frac{P(s_1)}{Q'(s_1)}=\frac{2i}{4i}=\frac12$。
$s_2=-2i$ 处的留数：$\frac{-2i}{-4i}=\frac12$。

于是

$$f(t)=\frac12e^{2it}+\frac12e^{-2it}=\cos2t.$$

**结果**：

$$f(t)=\cos2t\qquad(t\ge0).$$

**检验**：(i) $t=0$：$f(0)=1$；初值定理 $sF(s)=\frac{s^2}{s^2+4}\to1$ ✓。(ii) 查表：$\mathcal{L}[\cos\omega t]=\frac{s}{s^2+\omega^2}$，取 $\omega=2$ 正好是 $F(s)$ ✓。(iii) 极点虚部给出振荡频率 $2\ \mathrm{rad/s}$ ✓。

**读法**：留数法就是「把 $F(s)$ 拆成若干个 $e^{s_kt}$ 的叠加」——每个极点贡献一个模式，实部管包络、虚部管振荡。**这与 8.10.2 的极点图是同一件事**，只是这里算出来了。

**8.10**

**思路**：$H(s)$ 的逆变换是冲激响应 $h(t)$；阶跃响应是 $h$ 与阶跃的卷积，也可以直接用 $H(s)\cdot\frac1s$ 反演。时间常数从极点读：$\tau=1/|\mathrm{Re}\,s_{\text{pole}}|$。

**过程**：$H(s)=\frac{1}{s+2}$，极点在 $s=-2$。

冲激响应：$\frac{1}{s+2}\leftrightarrow e^{-2t}$，所以 $h(t)=e^{-2t}$。

阶跃响应：输入 $1/s$，输出

$$Y(s)=\frac{1}{s(s+2)}=\frac{1}{2}\left(\frac1s-\frac{1}{s+2}\right)\quad\Longrightarrow\quad y(t)=\frac12\left(1-e^{-2t}\right).$$

时间常数：$\tau=1/2\ \mathrm{s}$，正好等于 $1/|\mathrm{Re}\,s_{\text{pole}}|$。

**结果**：

$$h(t)=e^{-2t},\qquad y_{\text{step}}(t)=\frac12\left(1-e^{-2t}\right),\qquad \tau=\frac12\ \mathrm{s}.$$

**检验**：(i) $h(0)=1=H(\infty)$ ✓（初值定理）。(ii) 阶跃终值 $\frac12=H(0)$ ✓（终值定理）。(iii) 阶跃响应的初始斜率：$y'(0)=\frac12\cdot2=1$，而 $h(0)=1$ ✓（阶跃响应的导数就是冲激响应）。

**读法**：一阶系统的全部信息都在一个极点里：位置给时间常数，留数给增益。**极点在左半平面越远，响应越快、衰减越迅速**。这就是 8.10.6「拿到 $H(s)$ 先看三件事」的第一件。

**8.11**

**思路**：二阶系统的极点公式 $s=-\zeta\omega_0\pm i\omega_0\sqrt{1-\zeta^2}$ 直接代，振荡频率取虚部，衰减时间取实部的倒数，$Q=1/(2\zeta)$。

**过程**：$\omega_0=100\ \mathrm{rad/s}$、$\zeta=0.1$。

实部：$-\zeta\omega_0=-10\ \mathrm{s^{-1}}$。
虚部：$\omega_0\sqrt{1-\zeta^2}=100\sqrt{1-0.01}=99.5\ \mathrm{rad/s}$。

所以极点 $s=-10\pm99.5i$，振荡频率 $\omega_d=99.5\ \mathrm{rad/s}$（约 $15.8\ \mathrm{Hz}$）。衰减时间常数

$$\tau=\frac{1}{\zeta\omega_0}=\frac{1}{10}=0.1\ \mathrm{s}.$$

品质因数

$$Q=\frac{1}{2\zeta}=\frac{1}{0.2}=5.$$

**结果**：极点 $-10\pm99.5i\ \mathrm{s^{-1}}$；$\omega_d=99.5\ \mathrm{rad/s}$；$\tau=0.1\ \mathrm{s}$；$Q=5$。

**检验**：(i) $\omega_d<\omega_0$：$99.5<100$ ✓，阻尼让频率略降。(ii) $Q=5$ 意味着共振峰高约 5 倍、衰减时间 $\sim Q/\omega_0=0.05$ 个周期？——实际 $\tau=0.1\ \mathrm{s}$ 对应约 $1.6$ 个振荡周期，$Q=5$ 时「余音」约 $Q/\pi\approx1.6$ 个周期 ✓（$Q$ 与周期数的换算见 2.9.2）。(iii) 量纲：$\zeta$ 无量纲，$\zeta\omega_0$ 是 $\mathrm{s^{-1}}$ ✓。

**读法**：$\zeta=0.1$ 是「很欠阻尼」：只振几个周期就衰减完。工程上常取 $\zeta=0.7$ 附近（过冲约 $4\%$、响应快、不明显振荡）；乐器则相反，要 $\zeta$ 很小（$Q$ 大）才有长余音。

**8.12**

**思路**：一阶线性常系数方程，拉普拉斯变换是标准工具：变换后变代数方程，初值自动进来。**关键是用求导性质把 $y'$ 换成 $sY-y(0)$**，而不是先求通解再定常数。

**过程**：对 $y'+2y=e^{-t}$ 两边取变换，用 $\mathcal{L}[y']=sY(s)-y(0)$、$y(0)=0$：

$$sY+2Y=\frac{1}{s+1}\quad\Longrightarrow\quad Y(s)=\frac{1}{(s+1)(s+2)}.$$

部分分式（同 8.8）：$Y=\frac{1}{s+1}-\frac{1}{s+2}$，所以

$$y(t)=e^{-t}-e^{-2t}.$$

**结果**：

$$y(t)=e^{-t}-e^{-2t}\qquad(t\ge0).$$

**检验**：(i) $y(0)=1-1=0$ ✓。(ii) 代回方程：$y'=-e^{-t}+2e^{-2t}$，$y'+2y=(-e^{-t}+2e^{-2t})+(2e^{-t}-2e^{-2t})=e^{-t}$ ✓。(iii) 与 8.8 同一结果——那里是纯反演，这里是解方程，说明「$H(s)=\frac{1}{s+2}$、输入 $e^{-t}$」与本题等价 ✓。

**读法**：注意初值为零时，解的形态是「输入响应 $e^{-t}$」减去「自然响应 $e^{-2t}$」：前者是输入本身（低频几乎无衰减地通过），后者是为了满足零初值而附加的瞬态。**这就是「特解 + 齐次解」在频域的化身**，只是变换法自动定好了系数。

## B 组　物理应用

**8.13**

**思路**：刻在板上的正弦温度分布就是一个单一波数的模式，热方程对它的作用在频域是乘 $e^{-\alpha k^2t}$（8.7.1）。「衰减时间」就是指数因子的时间常数 $\tau=1/(\alpha k^2)$。**周期越短，$k$ 越大，$\tau$ 按平方缩短。**

**过程**：波数 $k=\frac{2\pi}{\lambda}$，温度模式 $T\propto\cos kx$。

周期 $\lambda=1\ \mathrm{mm}=10^{-3}\ \mathrm{m}$：$k=\frac{2\pi}{10^{-3}}=6.28\times10^{3}\ \mathrm{m^{-1}}$，

$$\alpha k^2=1.1\times10^{-4}\times(6.28\times10^3)^2=1.1\times10^{-4}\times3.95\times10^7=4.34\times10^3\ \mathrm{s^{-1}},$$

$$\tau=\frac{1}{\alpha k^2}=\frac{1}{4.34\times10^3}=2.3\times10^{-4}\ \mathrm{s}.$$

周期 $\lambda=1\ \mathrm{cm}=10^{-2}\ \mathrm{m}$：$k$ 小 10 倍，$k^2$ 小 100 倍，所以

$$\tau=2.3\times10^{-2}\ \mathrm{s}.$$

**结果**：$1\ \mathrm{mm}$ 尺度 $\tau=2.3\times10^{-4}\ \mathrm{s}$（$0.23\ \mathrm{ms}$）；$1\ \mathrm{cm}$ 尺度 $\tau=2.3\times10^{-2}\ \mathrm{s}$（$23\ \mathrm{ms}$）。

**检验**：(i) 比值：$\tau$ 之比 $=100=(\lambda\text{ 之比})^2$ ✓。(ii) 量纲：$\alpha k^2$ 是 $\mathrm{(m^2/s)(1/m^2)}=\mathrm{s^{-1}}$ ✓。(iii) 与 8.7.1 的估计对照：那里用 $t\sim L^2/\alpha$ 对 $1\ \mathrm{mm}$ 估得 $9\ \mathrm{ms}$，与本题的 $0.23\ \mathrm{ms}$ 差 $4\pi^2\approx40$ 倍——因为 $L^2/\alpha$ 与模式的衰减时间 $1/(\alpha k^2)=\lambda^2/(4\pi^2\alpha)$ 正好差 $4\pi^2$ ✓。

**读法**：**尺度越小，温度越难保持**——因为热扩散抹平的是「空间梯度」，梯度越陡抹得越快。这就是为什么激光写入、光刻这类微米尺度加工必须考虑热扩散：写下去的图案可能在微秒内就被热传导糊掉。

**8.14**

**思路**：初值是点源（$\delta$），这是热核的标准用法：解 = 热核与初值的卷积（8.7.1）。点源卷积的结果就是热核本身乘一个常数。**先确认量纲，再算扩散长度。**

**过程**：初值 $u(x,0)=\frac{Q}{\rho c_p}\delta(x)$，其中 $Q$ 是注入的热量（焦耳），$\rho c_p$ 是单位体积热容。由 8.7.1，

$$u(x,t)=\int G(x-x',t)u(x',0)\mathrm{d}x'=\frac{Q}{\rho c_p}G(x,t),$$

$$G(x,t)=\frac{1}{\sqrt{4\pi\alpha t}}e^{-x^2/(4\alpha t)}.$$

所以

$$u(x,t)=\frac{Q}{\rho c_p\sqrt{4\pi\alpha t}}\exp\left(-\frac{x^2}{4\alpha t}\right).$$

扩散长度：把指数写成 $e^{-x^2/\ell^2}$ 的形式，$\ell^2=4\alpha t$，即 $\ell=\sqrt{4\alpha t}$。

**结果**：

$$u(x,t)=\frac{Q}{\rho c_p\sqrt{4\pi\alpha t}}e^{-x^2/(4\alpha t)},\qquad \ell=\sqrt{4\alpha t}\propto\sqrt t.$$

**检验**：(i) 总热量：$\int u\,\mathrm{d}x=\frac{Q}{\rho c_p}\int G\,\mathrm{d}x=\frac{Q}{\rho c_p}$，与 $t$ 无关 ✓（热量守恒）。(ii) $t\to0^+$：$G\to\delta(x)$，$u\to\frac{Q}{\rho c_p}\delta(x)$ ✓。(iii) 量纲：$G$ 的量纲是 $1/$长度，所以 $u$ 的量纲是 $\frac{\mathrm{J}}{\mathrm{J/(m^3K)}}\cdot\frac1{\mathrm m}=\mathrm{K}$ ✓。(iv) 峰值随时间按 $1/\sqrt t$ 下降，与「摊开」一致 ✓。

**读法**：扩散长度按 $\sqrt t$ 增长——**扩散是「越走越慢」的传播**：走 1 倍距离要 1 倍时间，走 10 倍要 100 倍时间。这与波的匀速传播（$\ell=ct$）形成鲜明对比，也是「热方程没有前沿」的定量表现。

**8.15**

**思路**：初位移给定、初速度为零，这是达朗贝尔公式的最简情形：$u=\frac12[f(x-ct)+f(x+ct)]$。**不要展开级数**——无限长弦没有边界，用行波形式最快。波形的「段数」由两个三角脉冲是否重叠决定。

**过程**：由 8.7.2，$g=0$ 时

$$u(x,t)=\frac12\left[f(x-ct)+f(x+ct)\right].$$

$f$ 是宽 $2a$、高 $h$ 的三角形（顶点在 $x=0$，底边 $[-a,a]$）。两个副本：$f(x-ct)$ 中心在 $x=ct$（右行），$f(x+ct)$ 中心在 $x=-ct$（左行），各自高度减半。

段数：每个三角形由两段直线组成（上升段、下降段）。两脉冲中心相距 $2ct$：
- $2ct>2a$（即 $ct>a$）时两者完全不重叠，波形由 4 段折线组成（两段上升、两段下降，中间一段为零）；
- $ct=a$ 时两尖端刚好相接，4 段连成 3 段；
- $ct<a$ 时两者重叠，重叠区相加，仍是 3 段（中间平台或尖峰）。

**结果**：

$$u(x,t)=\frac12\left[f(x-ct)+f(x+ct)\right];$$

$ct>a$ 时波形 4 段，$ct\le a$ 时 3 段（重叠区相加）。

**检验**：(i) $t=0$：两副本重合，$u=f$ ✓。(ii) 面积：$\int u\,\mathrm{d}x=\frac12\left(\int f+\int f\right)=\int f$，面积守恒 ✓。(iii) 峰值：$t=0$ 时峰高 $h$；$ct>a$ 后两峰各自高 $h/2$ ✓。

**读法**：**一个初值裂成两个半高的自己，分头跑**——这是达朗贝尔解最直观的读法。在有限长弦上它们会撞到端点反射回来，反复叠加就是驻波（第 1 章的行波与驻波之争，答案就在这里）。

**8.16**

**思路**：RC 低通是标准一阶系统，$H(s)=\frac{1}{1+RCs}$，截止频率 $\omega_c=1/RC$。方波的谐波在 $f,3f,5f$，各自乘上 $|H|$ 就是相对增益。**先算 RC，再算频率比。**

**过程**：$RC=10\times10^3\times10\times10^{-9}=10^{-4}\ \mathrm{s}$，

$$f_c=\frac{1}{2\pi RC}=\frac{1}{2\pi\times10^{-4}}=1592\ \mathrm{Hz}.$$

幅频 $|H(f)|=\frac{1}{\sqrt{1+(f/f_c)^2}}$。对 $1\ \mathrm{kHz}$ 方波，谐波在 $1,3,5\ \mathrm{kHz}$：

$$|H(1\,\mathrm{k})|=\frac{1}{\sqrt{1+(1000/1592)^2}}=\frac{1}{\sqrt{1.395}}=0.847,$$
$$|H(3\,\mathrm{k})|=\frac{1}{\sqrt{1+(3000/1592)^2}}=\frac{1}{\sqrt{4.55}}=0.469,$$
$$|H(5\,\mathrm{k})|=\frac{1}{\sqrt{1+(5000/1592)^2}}=\frac{1}{\sqrt{10.87}}=0.303.$$

**结果**：$f_c=1.59\ \mathrm{kHz}$；三次谐波相对增益 $0.847,\ 0.469,\ 0.303$（即 $-1.4,\ -6.6,\ -10.4\ \mathrm{dB}$）。

**检验**：(i) $f=f_c$ 时 $|H|=1/\sqrt2=0.707$ ✓（$-3\ \mathrm{dB}$）。(ii) 高频：$f\gg f_c$ 时 $|H|\approx f_c/f$，按 $-20\ \mathrm{dB/十倍频}$ 滚降 ✓。(iii) 量纲：$RC$ 是 $\mathrm{s}$，$1/RC$ 是 $\mathrm{Hz}$（差 $2\pi$）✓。

**读法**：方波经低通后，基波几乎原样通过（$0.85$），三次谐波只剩一半、五次只剩三成——**边沿被磨圆**。这就是示波器探头要用高带宽的原因：带宽不够，看到的方波就是「圆角」的，上升时间被 RC 决定（$t_r\approx2.2RC$）。

**8.17**

**思路**：串联 LC 的谐振频率 $\omega_0=1/\sqrt{LC}$；品质因数 $Q=\frac{\omega_0L}{R}$（串联回路）。已知 $Q$ 反解 $R$，两步都只用公式。

**过程**：

$$\omega_0=\frac{1}{\sqrt{LC}}=\frac{1}{\sqrt{100\times10^{-6}\times100\times10^{-12}}}=\frac{1}{\sqrt{10^{-14}}}=10^{7}\ \mathrm{rad/s}.$$

$$f_0=\frac{\omega_0}{2\pi}=\frac{10^7}{6.283}=1.59\times10^6\ \mathrm{Hz}=1.59\ \mathrm{MHz}.$$

由 $Q=\frac{\omega_0L}{R}$：

$$R=\frac{\omega_0L}{Q}=\frac{10^7\times100\times10^{-6}}{50}=\frac{10^3}{50}=20\ \Omega.$$

**结果**：$f_0=1.59\ \mathrm{MHz}$；要 $Q=50$，串联电阻取 $R=20\ \Omega$。

**检验**：(i) 量纲：$1/\sqrt{\mathrm{H\cdot F}}=\mathrm{s^{-1}}$ ✓；$\omega_0L/R$ 无量纲 ✓。(ii) 数量级：$1.59\ \mathrm{MHz}$ 在中波广播波段，合理 ✓。(iii) $Q=50$ 对应带宽 $\Delta f=f_0/Q=31.8\ \mathrm{kHz}$，适合调幅广播的选择性 ✓。

**读法**：$Q$ 由 $L$、$C$、$R$ 三个量共同决定，但**只有 $R$ 是耗散**：$Q$ 高就意味着每周期损耗小。实际线圈还有趋肤效应和磁芯损耗，所以「设计 $Q=50$」往往做不到——那部分损耗也要算进 $R$。

**8.18**

**思路**：啁啾的核心是一对公式：时宽带宽积 $BT$（压缩比）与距离分辨率 $\delta R=c/(2B)$。**分辨率只由带宽 $B$ 决定**，与脉冲长度 $T$ 无关；$T$ 只影响能量与信噪比。

**过程**：$B=2\times10^6\ \mathrm{Hz}$、$T=0.5\times10^{-3}\ \mathrm{s}$：

$$BT=2\times10^6\times0.5\times10^{-3}=1000.$$

$$\delta R=\frac{c}{2B}=\frac{1500}{2\times2\times10^6}=\frac{1500}{4\times10^6}=3.75\times10^{-4}\ \mathrm{m}.$$

**结果**：$BT=1000$（压缩比 $1000$，即 $30\ \mathrm{dB}$）；$\delta R=0.375\ \mathrm{mm}$。

**检验**：(i) 量纲：$BT$ 无量纲 ✓；$c/B$ 是 $\mathrm{(m/s)/Hz}=\mathrm m$ ✓。(ii) 与「未压缩」比较：宽 $T$ 的脉冲本来分辨率是 $cT/2=0.375\ \mathrm{m}$，压缩后缩小 $BT=1000$ 倍 ✓。(iii) 物理合理性：$0.375\ \mathrm{mm}$ 的声学分辨率在水里是极高的（波长量级：$2\ \mathrm{MHz}$ 在水中波长 $0.75\ \mathrm{mm}$，分辨率恰为半波长）✓。

**读法**：**用带宽换分辨率**，而不是用脉宽。这也解释了为什么现代雷达/声呐都发「长而宽带」的信号：长脉冲能量大（探得远），宽带保证分辨率（看得清）。两者由匹配滤波同时实现，代价是信号处理复杂度。

**8.19**

**思路**：色散展宽在工程上按「每传输一段、每单位谱宽展宽多少」的系数累乘：$\Delta t=D\,\Delta\lambda\,L$。算出展宽后与比特间隔比，**比值超过 10\%–20\% 就要补偿**（经验判据）。

**过程**：

$$\Delta t=D\cdot\Delta\lambda\cdot L=17\ \frac{\mathrm{ps}}{\mathrm{nm\cdot km}}\times0.1\ \mathrm{nm}\times50\ \mathrm{km}=85\ \mathrm{ps}.$$

比特间隔 $T_b=1/(10\times10^9)=100\ \mathrm{ps}$。比值

$$\frac{\Delta t}{T_b}=\frac{85}{100}=0.85.$$

**结果**：展宽 $85\ \mathrm{ps}$，占比特间隔 $85\%$，**必须做色散补偿**（判据是 $\Delta t\lesssim0.1T_b$，即应小于 $10\ \mathrm{ps}$）。

**检验**：(i) 量纲：$\mathrm{ps/(nm\cdot km)}\times\mathrm{nm}\times\mathrm{km}=\mathrm{ps}$ ✓。(ii) 线性：距离减半则展宽减半（$42.5\ \mathrm{ps}$，仍有 $42\%$），要传 $50\ \mathrm{km}$ 必须补偿 ✓。(iii) 与 8.7.3 的说法对照：本题的展宽率是 $17\times0.1=1.7\ \mathrm{ps/km}$；8.7.3 提到的 $0.2\ \mathrm{ps/km}$ 对应约 $0.012\ \mathrm{nm}$ 的自谱宽（$1\ \mathrm{ps}$ 高斯脉冲的带宽换算）。**谱宽不同，展宽率就不同**——这正是高速链路要用窄谱光源的原因 ✓。

**读法**：色散把不同波长的光「拉开」，脉冲越传越胖，最后相邻比特重叠（码间干扰）。**补偿的办法是加一段符号相反的色散光纤**，让先到的慢成分追上来。10 Gbit/s 的城域网（几十公里）必须补偿，这就是光纤通信里「色散补偿模块」存在的原因。

**8.20**

**思路**：第 6 章的电子振子方程是 $\ddot x+\gamma\dot x+\omega_0^2x=0$，极点 $s=-\gamma/2\pm i\sqrt{\omega_0^2-\gamma^2/4}$（8.10.4 的 $\zeta\omega_0=\gamma/2$）。代数字：$\gamma\ll\omega_0$，所以虚部几乎就是 $\omega_0$。

**过程**：$\gamma=10^8\ \mathrm{s^{-1}}$、$\omega_0=3\times10^{15}\ \mathrm{rad/s}$。

实部：$-\gamma/2=-5\times10^7\ \mathrm{s^{-1}}$。
虚部：$\sqrt{\omega_0^2-\gamma^2/4}\approx\omega_0=3\times10^{15}\ \mathrm{rad/s}$（因为 $\gamma/\omega_0\sim3\times10^{-8}$）。

到实轴的距离就是虚部：$3\times10^{15}\ \mathrm{rad/s}$，对应频率 $\nu=\omega/(2\pi)=4.8\times10^{14}\ \mathrm{Hz}$（波长 $\lambda=c/\nu=628\ \mathrm{nm}$，红光 ✓）。

衰减时间（振幅按 $e^{-\gamma t/2}$，时间常数 $2/\gamma$）：

$$\tau=\frac{2}{\gamma}=2\times10^{-8}\ \mathrm{s}=20\ \mathrm{ns}.$$

**结果**：极点在 $-5\times10^7\pm i3\times10^{15}\ \mathrm{s^{-1}}$；到实轴距离 $3\times10^{15}\ \mathrm{rad/s}$；$\tau=20\ \mathrm{ns}$。

**检验**：(i) $\omega_d<\omega_0$ 但差别只有 $10^{-15}$ 量级，可忽略 ✓。(ii) $Q=\omega_0/\gamma=3\times10^7$，极大，说明谱线极窄 ✓。(iii) 自然线宽 $\Delta\nu=1/(2\pi\tau)=8\ \mathrm{MHz}$，与原子跃迁线宽的量级一致 ✓。

**读法**：**极点的虚部是颜色，实部是寿命**。原子发光的自然线宽 $\Delta\nu\sim1/\tau$ 与寿命成反比——这就是 8.6 带宽定理在原子尺度上的样子：寿命越长，谱线越窄。

**8.21**

**思路**：热电偶是一阶系统（热惯性），$H(s)=\frac{1}{1+\tau s}$。测正弦温度时，输出幅度乘 $|H(i\omega)|$、相位滞后 $\arctan(\omega\tau)$。先算无量纲量 $\omega\tau$。

**过程**：$\omega=2\pi f=6.283\ \mathrm{rad/s}$，$\tau=1\ \mathrm{s}$，所以 $\omega\tau=6.283$。

$$|H|=\frac{1}{\sqrt{1+(\omega\tau)^2}}=\frac{1}{\sqrt{1+39.5}}=\frac{1}{6.36}=0.157.$$

相位滞后：$\varphi=-\arctan(\omega\tau)=-\arctan6.283=-80.96^\circ$。

**结果**：幅度衰减到 $15.7\%$（$-16.1\ \mathrm{dB}$），相位滞后 $81^\circ$。

**检验**：(i) 极限 $\omega\tau\to0$：$|H|\to1$、$\varphi\to0$（慢变温度测得准）✓。(ii) 极限 $\omega\tau\to\infty$：$|H|\approx1/(\omega\tau)\to0$、$\varphi\to-90^\circ$ ✓。(iii) 交叉点 $\omega\tau=1$：$|H|=0.707$、$\varphi=-45^\circ$ ✓。

**读法**：$\tau=1\ \mathrm{s}$ 的热电偶只能测「几分钟变一次」的温度；$1\ \mathrm{Hz}$ 的波动已经被压到 $1/6$ 且严重滞后。**测快速温度波动要用更细的热电偶（$\tau$ 小）或光学方法**——这是实验设计里「传感器带宽」的第一课。

**8.22**

**思路**：一阶系统的频率响应直接把 $s=i\omega$ 代入 $H(s)$，取模得幅度、取辐角得相位。$\omega\tau\gg1$ 时做渐近展开，看它退化成什么运算——答案是积分器。

**过程**：$H(i\omega)=\frac{1}{1+i\omega\tau}$。

幅度：$|H|=\frac{1}{\sqrt{1+(\omega\tau)^2}}$。
相位：$\varphi=-\arctan(\omega\tau)$。

所以输入 $\cos\omega t$ 时，稳态输出

$$y(t)=\frac{1}{\sqrt{1+(\omega\tau)^2}}\cos\left(\omega t-\arctan(\omega\tau)\right).$$

$\omega\tau\gg1$ 时：$|H|\approx\frac{1}{\omega\tau}$，$\arctan(\omega\tau)\approx90^\circ$，于是

$$y(t)\approx\frac{1}{\omega\tau}\cos\left(\omega t-\frac{\pi}{2}\right)=\frac{1}{\omega\tau}\sin\omega t.$$

而 $\frac{1}{\tau}\int\cos\omega t\,\mathrm{d}t=\frac{1}{\omega\tau}\sin\omega t$——输出的确是输入的积分（乘 $1/\tau$）。

**结果**：$|H|=\frac{1}{\sqrt{1+(\omega\tau)^2}}$，$\varphi=-\arctan(\omega\tau)$；$\omega\tau\gg1$ 时 $y\approx\frac{1}{\omega\tau}\sin\omega t$，即积分器。

**检验**：(i) $\omega\to0$：$y\to\cos\omega t$，输出等于输入 ✓。(ii) 相位：$\omega\tau\gg1$ 时滞后 $90^\circ$，正是积分的相位（$\sin$ 是 $\cos$ 的积分）✓。(iii) 幅度：积分把幅度除以 $\omega$，这里除以 $\omega\tau$，差一个 $1/\tau$ 的增益 ✓。

**读法**：**「低通」与「积分器」是同一个系统在不同频段的两张面孔**：低频时它原样传递，高频时它做积分（把快速变化平均掉）。这也是为什么 RC 电路既能做滤波也能做「积分电路」——取决于你工作在哪个频段。

## C 组　深入

**8.23**

**思路**：把 $\Delta k$ 用求导性质换成时域的积分（8.6.2 已给出这一步），然后对 $\int xf\cdot f'^*$ 用柯西–施瓦茨，再分部积分把 $xf f'^*$ 化成 $\frac12\int|f|^2$。**等号条件出现在柯西–施瓦茨那一步：两个函数成比例，即 $f'\propto xf$。**

**过程**：记 $\langle u,v\rangle=\int u v^*\mathrm{d}x$，范数 $\|u\|^2=\langle u,u\rangle$。由求导性质与帕塞瓦尔，

$$\Delta k^2=\frac{\int k^2|\tilde f|^2\mathrm{d}k}{\int|\tilde f|^2\mathrm{d}k}=\frac{\int|f'|^2\mathrm{d}x}{\int|f|^2\mathrm{d}x}=\frac{\|f'\|^2}{\|f\|^2}.$$

同理 $\Delta x^2=\|xf\|^2/\|f\|^2$。对 $u=xf$、$v=f'$ 用柯西–施瓦茨：

$$|\langle xf,f'\rangle|^2\le\|xf\|^2\|f'\|^2=\Delta x^2\Delta k^2\|f\|^4.$$

左边用分部积分：$\langle xf,f'\rangle=\int xf f'^*\mathrm{d}x=\frac12\int x\frac{d}{dx}|f|^2\mathrm{d}x=-\frac12\int|f|^2\mathrm{d}x$（边界项 $x|f|^2\to0$，因为 $f$ 平方可积且 $xf$ 也平方可积）。于是

$$\frac14\|f\|^4\le\Delta x^2\Delta k^2\|f\|^4\quad\Longrightarrow\quad\Delta x\,\Delta k\ge\frac12.$$

等号条件：柯西–施瓦茨取等号要求 $f'\propto xf$，即 $f'=cxf$。解这个微分方程：$f=Ae^{cx^2/2}$，要平方可积必须 $c<0$，写作 $c=-1/\sigma^2$，得 $f=Ae^{-x^2/(2\sigma^2)}$——**高斯**。

**结果**：$\Delta x\,\Delta k\ge\frac12$，等号当且仅当 $f$ 是高斯（或其平移、伸缩、调制）。

**检验**：(i) 高斯的情形已在 8.4 直接算出 $\Delta x\Delta k=1/2$，与等号条件吻合 ✓。(ii) 量纲：$\Delta x$ 是长度、$\Delta k$ 是 $1/$长度，乘积无量纲 ✓。(iii) 极限：矩形脉冲的 $\Delta x\Delta k$ 更大（因为 sinc 的尾巴按 $1/k$ 衰减，方差发散），不等式成立 ✓。

**读法**：这条不等式的来源是**傅里叶变换的几何性质**，与量子力学、与测量都没有关系——量子力学只是把 $k$ 换成 $p/\hbar$，右端随之变成 $\hbar/2$。**$\hbar$ 只是单位换算，不确定性不是「测量扰动」造成的**（习题 8.33 会再强调一次）。

**8.24**

**思路**：帕塞瓦尔就是「换基底不改变长度」。证明只需把 $|f|^2$ 写成 $f\cdot f^*$，用逆变换把其中一个 $f^*$ 换成频域积分，再交换积分次序，最后认出 $\delta$ 的积分表示。

**过程**：

$$\int|f(x)|^2\mathrm{d}x=\int f(x)f^*(x)\mathrm{d}x.$$

把 $f^*(x)$ 用逆变换写出（对 $\tilde f$ 取共轭）：

$$f^*(x)=\frac{1}{2\pi}\int\tilde f^*(k)e^{-ikx}\mathrm{d}k.$$

代入：

$$\int|f|^2\mathrm{d}x=\frac{1}{2\pi}\int\mathrm{d}k\,\tilde f^*(k)\int f(x)e^{-ikx}\mathrm{d}x=\frac{1}{2\pi}\int\tilde f^*(k)\tilde f(k)\mathrm{d}k.$$

最后一步用了正变换的定义。中间交换积分次序要求 $\int|f|^2$、$\int|\tilde f|^2$ 都有限（$f\in L^2$ 时成立）。认出 $\tilde f^*(k)\tilde f(k)=|\tilde f(k)|^2$：

$$\int|f|^2\mathrm{d}x=\frac{1}{2\pi}\int|\tilde f(k)|^2\mathrm{d}k.$$

**结果**：

$$\int_{-\infty}^{\infty}|f(x)|^2\mathrm{d}x=\frac{1}{2\pi}\int_{-\infty}^{\infty}|\tilde f(k)|^2\mathrm{d}k.$$

**检验**：(i) 取 $f=e^{-x^2/(2\sigma^2)}$：左边 $\sigma\sqrt\pi$，右边 $\frac{1}{2\pi}\int2\pi\sigma^2e^{-\sigma^2k^2}\mathrm{d}k=\frac{\sigma^2}{\pi}\cdot\frac{\sqrt\pi}{\sigma}=\sigma\sqrt\pi$ ✓。(ii) 取 $f=\delta$：左边发散（$\delta$ 不在 $L^2$），说明公式的前提是 $f\in L^2$，不能乱用 ✓。

**读法**：物理上这就是能量守恒：**时域的总能量 = 频域各分量能量之和**。注意右边的 $1/2\pi$——它来自我们约定的正逆变换不对称。**约定没有对错，只有统一**；换一种约定，这条式子会变样子但含义不变。

**8.25**

**思路**：卷积定理的证明是一次变量替换 + 交换积分；每一步都要说清「为什么可以换序」（绝对可积）。第二问要说明「理想积分器」为什么是这个定理的边界情形：$h=\theta(t)$ 不绝对可积，卷积在普通意义下发散。

**过程**：设 $(f*g)(x)=\int f(x-x')g(x')\mathrm{d}x'$。取变换：

$$\mathcal{F}[f*g]=\int\mathrm{d}x\,e^{-ikx}\int f(x-x')g(x')\mathrm{d}x'.$$

交换积分次序（$f,g\in L^1$ 时 Fubini 定理保证可以换），并对内层做变量替换 $u=x-x'$（$x=u+x'$，$\mathrm{d}x=\mathrm{d}u$）：

$$=\int g(x')\mathrm{d}x'\int f(u)e^{-ik(u+x')}\mathrm{d}u=\left(\int f(u)e^{-iku}\mathrm{d}u\right)\left(\int g(x')e^{-ikx'}\mathrm{d}x'\right)=\tilde f(k)\tilde g(k).$$

**理想积分器**：$H(s)=1/s$，冲激响应 $h(t)=\theta(t)$（单位阶跃）。它**不绝对可积**：$\int|h|\mathrm{d}t=\int_0^\infty\mathrm{d}t=\infty$。所以

- 傅里叶变换只能在分布意义下定义：$\tilde h(\omega)=\frac{1}{i\omega}+\pi\delta(\omega)$；
- 卷积 $y(t)=\int_{-\infty}^{t}x(\tau)\mathrm{d}\tau$ 对很多输入发散（例如 $x=$ 常数，输出无界）；
- 系统只是**临界稳定**（极点在虚轴原点），阶跃输入下输出线性增长。

**结果**：卷积定理成立需 $f,g\in L^1$（或 $L^2$）；积分器 $H=1/s$ 的 $h=\theta(t)\notin L^1$，卷积定理只在分布意义下成立，物理上表现为「输出无界」。

**检验**：(i) 取两个矩形验证：$\mathcal{F}[f*f]=\tilde f^2$，与 8.6 的结果一致 ✓。(ii) 取 $g=\delta$：$f*\delta=f$，而 $\tilde f\cdot1=\tilde f$ ✓。(iii) 积分器的极点 $s=0$ 在虚轴上：8.10.3 的判据说这是「临界」，与「输出无界」一致 ✓。

**读法**：**卷积定理的适用性等价于系统的稳定性**。一个绝对可积的冲激响应（极点全在左半平面）= 有界输入有界输出 = 卷积收敛。理想积分器恰好踩在边界上：极点落在虚轴，定理退化为分布恒等式。

**8.26**

**思路**：同一个 $F(s)=\frac{1}{s-1}$ 配不同的收敛域，对应**不同的时间函数**。反演积分必须画在收敛域内，围道往哪边闭合取决于 $t$ 的符号。判稳定性看「收敛域是否包含虚轴」，而不是只看极点。

**过程**：极点在 $s=1$。

**情形一，$\sigma>1$（收敛域在极点右边）**：$t>0$ 时向左闭合，围住极点 $s=1$，

$$f(t)=\mathrm{Res}\left[\frac{e^{st}}{s-1}\right]_{s=1}=e^{t},\qquad f(t)=0\ (t<0).$$

即 $f(t)=e^t\theta(t)$：因果、但 $t\to\infty$ 时指数增长。

**情形二，$\sigma<1$（收敛域在极点左边）**：$t>0$ 时向左闭合围不到极点，积分为零；$t<0$ 时向右闭合，围住 $s=1$（顺时针，带负号）：

$$f(t)=-e^{t},\qquad t<0.$$

即 $f(t)=-e^{t}\theta(-t)$：反因果，$t\to-\infty$ 时趋于零。

**结果**：

- $\sigma>1$：$f=e^t\theta(t)$，因果，极点实部 $>0$，**不稳定**；
- $\sigma<1$：$f=-e^t\theta(-t)$，反因果，收敛域含虚轴，**稳定**（有界输入有界输出）。

**检验**：(i) 两者的拉普拉斯变换都是 $1/(s-1)$：直接积分验证，因果情形 $\int_0^\infty e^{t}e^{-st}\mathrm{d}t=\frac{1}{s-1}$（$\sigma>1$）；反因果情形 $\int_{-\infty}^{0}(-e^t)e^{-st}\mathrm{d}t=-\frac{1}{s-1}$（$\sigma<1$）——注意后者要取负号才凑出 $F$ ✓。(ii) 稳定性判据：稳定要求 $\int|h|\mathrm{d}t<\infty$；情形二 $\int_{-\infty}^0e^t\mathrm{d}t=1$ 有限 ✓，情形一 $\int_0^\infty e^t\mathrm{d}t=\infty$ ✗。

**读法**：**「极点位置决定稳定性」只对因果系统成立。** 一般情形必须把极点与收敛域一起看：收敛域含虚轴才是稳定。这也是为什么教科书写 $H(s)$ 时总要标一句「$\mathrm{Re}\,s>\sigma_c$」——不标，这个 $H$ 就不是一个确定的系统。

**8.27**

**思路**：形如 $\int\frac{e^{i\omega t}}{P(\omega)}\mathrm{d}\omega$ 的积分用留数：被积函数在上半平面还是下半平面衰减，取决于 $e^{i\omega t}$ 的指数符号，所以**按 $t$ 的正负选闭合方向**。这与第 6 章的做法完全一样。

**过程**：极点 $\omega=\pm ia$（$a>0$），都在虚轴上。

**$t>0$**：$e^{i\omega t}=e^{i(\mathrm{Re}\,\omega)t}e^{-\mathrm{Im}\,\omega\,t}$，在上半平面（$\mathrm{Im}\,\omega>0$）指数衰减，所以**向上闭合**。围道内只有 $\omega=ia$：

$$\oint=\int_{-\infty}^{\infty}+\int_{\text{大圆弧}}=2\pi i\,\mathrm{Res}_{\omega=ia}\frac{e^{i\omega t}}{\omega^2+a^2}.$$

留数：$\frac{e^{i(ia)t}}{2\omega}\Big|_{\omega=ia}=\frac{e^{-at}}{2ia}$。大圆弧由若尔当引理趋于零。所以

$$\int_{-\infty}^{\infty}\frac{e^{i\omega t}}{\omega^2+a^2}\mathrm{d}\omega=2\pi i\cdot\frac{e^{-at}}{2ia}=\frac{\pi}{a}e^{-at}.$$

**$t<0$**：下半平面指数衰减，**向下闭合**（顺时针，乘 $-2\pi i$），围住 $\omega=-ia$：

$$\int=(-2\pi i)\cdot\frac{e^{i(-ia)t}}{-2ia}=(-2\pi i)\cdot\frac{e^{at}}{-2ia}=\frac{\pi}{a}e^{at}.$$

合并：

**结果**：

$$\int_{-\infty}^{\infty}\frac{e^{i\omega t}}{\omega^2+a^2}\mathrm{d}\omega=\frac{\pi}{a}e^{-a|t|}.$$

**检验**：(i) $t=0$：右边 $\frac{\pi}{a}$；左边 $\int\frac{\mathrm{d}\omega}{\omega^2+a^2}=\frac1a\left[\arctan\frac{\omega}{a}\right]_{-\infty}^{\infty}=\frac{\pi}{a}$ ✓。(ii) 与 8.2 互为逆变换：8.2 给出 $\mathcal{F}[e^{-a|x|}]=\frac{2a}{a^2+k^2}$，所以 $\frac{1}{2\pi}\int\frac{2a}{a^2+k^2}e^{ikt}\mathrm{d}k=e^{-a|t|}$；两边同乘 $\frac{\pi}{a}$，正是本题的结果 ✓。(iii) 对称性：结果只依赖 $|t|$，是实偶函数，与被积函数在 $\omega\to-\omega$ 下的对称性一致 ✓。

**读法**：这一步与第 6 章计算 $\int e^{-i\omega t}/(\omega^2+a^2)\mathrm{d}\omega$ 是同一个围道、同一组留数，只是闭合方向随 $t$ 换了一次——**第 6 章的「看指数在哪个半平面衰减」在这里原样复用**。结果的 $e^{-a|t|}$ 是有名的「洛伦兹线型的变换对」（与 8.2 互为对称）。

**8.28**

**思路**：过冲量是阶跃响应的第一个极大值减去终值。求极值点：对 $u(t)$ 求导，令导数为零，解出 $t$；再代回 $u$。**$u'$ 的表达式会化得很干净**（只剩一个正弦），这是本题的技巧所在。

**过程**：二阶系统的阶跃响应（8.8.4）

$$u(t)=1-e^{-\zeta\omega_0t}\left[\cos\omega_dt+\frac{\zeta}{\sqrt{1-\zeta^2}}\sin\omega_dt\right],\qquad \omega_d=\omega_0\sqrt{1-\zeta^2}.$$

求导。注意 $e^{-\zeta\omega_0t}$ 的导数与括号内三角函数的导数会大量抵消，结果化为

$$u'(t)=\frac{\omega_0}{\sqrt{1-\zeta^2}}e^{-\zeta\omega_0t}\sin\omega_dt.$$

（验证：把括号记作 $A(t)$，则 $u'=e^{-\zeta\omega_0t}[\zeta\omega_0A-A']$，代入 $A=\cos+\frac{\zeta}{\sqrt{1-\zeta^2}}\sin$、$A'=-\omega_d\sin+\frac{\zeta\omega_d}{\sqrt{1-\zeta^2}}\cos$ 化简即得。）

$u'=0$ 的第一个正根：$\sin\omega_dt=0\Rightarrow\omega_dt=\pi$（$\pi$ 对应第一个峰）。

代回：$\cos\pi=-1$、$\sin\pi=0$，

$$u\Big(\frac{\pi}{\omega_d}\Big)=1-e^{-\zeta\omega_0\pi/\omega_d}\cdot(-1)=1+e^{-\pi\zeta/\sqrt{1-\zeta^2}}.$$

过冲量 $M_p=u_{\max}-1$：

**结果**：

$$M_p=\exp\left(-\frac{\pi\zeta}{\sqrt{1-\zeta^2}}\right).$$

$\zeta=0.5$：$\frac{\pi\times0.5}{\sqrt{0.75}}=1.8138$，$M_p=e^{-1.8138}=0.1630$，即 $16.3\%$。

**检验**：(i) $\zeta\to0$：$M_p\to e^0=1$（$100\%$ 过冲，无阻尼等幅振荡）✓。(ii) $\zeta\to1$：$M_p\to e^{-\infty}=0$（临界阻尼无过冲）✓。(iii) $\zeta=1/\sqrt2\approx0.707$：$M_p=e^{-\pi}=0.043$，约 $4.3\%$——这正是工程上常取 $0.707$ 的原因 ✓。

**读法**：**过冲与阻尼比一一对应**，测出过冲就能反推 $\zeta$：这是控制系统整定的标准手段（阶跃响应实验）。想让系统「快而不过冲」，就取 $\zeta\approx0.7$；乐器要长余音，则要 $\zeta\ll0.1$（$Q$ 大）。

**8.29**

**思路**：半无限杆、端点温度阶跃——空间方向没有边界（到无穷远），时间方向有起点（$t=0$ 的初值），所以**对时间做拉普拉斯变换**，把偏微分方程变成关于 $x$ 的常微分方程，解出后再反演。这是拉普拉斯变换最典型的用法：初值自动进入。

**过程**：方程与条件：

$$\frac{\partial T}{\partial t}=\alpha\frac{\partial^2T}{\partial x^2},\quad T(0,t)=T_0,\quad T(x,0)=0,\quad T(x\to\infty,t)\to0.$$

对 $t$ 变换，记 $\bar T(x,s)=\int_0^\infty T e^{-st}\mathrm{d}t$，用 $\mathcal{L}[\partial T/\partial t]=s\bar T-T(x,0)=s\bar T$：

$$s\bar T=\alpha\frac{\mathrm{d}^2\bar T}{\mathrm{d}x^2}\quad\Longrightarrow\quad \bar T=Ae^{x\sqrt{s/\alpha}}+Be^{-x\sqrt{s/\alpha}}.$$

$x\to\infty$ 有界要求 $A=0$；$x=0$ 处 $\bar T(0,s)=T_0/s$，所以 $B=T_0/s$：

$$\bar T(x,s)=\frac{T_0}{s}\exp\left(-x\sqrt{\frac{s}{\alpha}}\right).$$

反演用查表（8.8.5 与附录）：$\mathcal{L}^{-1}\left[\frac1s e^{-x\sqrt{s/\alpha}}\right]=\mathrm{erfc}\left(\frac{x}{2\sqrt{\alpha t}}\right)$，其中 $\mathrm{erfc}\,u=1-\mathrm{erf}\,u=\frac{2}{\sqrt\pi}\int_u^\infty e^{-v^2}\mathrm{d}v$。

**结果**：

$$T(x,t)=T_0\,\mathrm{erfc}\left(\frac{x}{2\sqrt{\alpha t}}\right),\qquad x>0,\ t>0.$$

**检验**：(i) $x=0$：$\mathrm{erfc}\,0=1$，$T=T_0$ ✓。(ii) $t\to0^+$：$x/(2\sqrt{\alpha t})\to\infty$，$\mathrm{erfc}\to0$，$T\to0$（$x>0$）✓。(iii) $t\to\infty$：自变量趋于零，$T\to T_0$，整根杆趋于端点温度 ✓。(iv) 量纲：$x/\sqrt{\alpha t}$ 无量纲 ✓。(v) 与 8.14 的热核一致：把 $T_0$ 看成 $x=0$ 处持续注入的热源，解是热核的叠加（半无限区间的像法），两种做法给出同一个 erfc ✓。

**读法**：$\mathrm{erfc}$ 的「过渡区」宽度就是扩散长度 $\sqrt{\alpha t}$：**温度剖面是一条随 $\sqrt t$ 向外推进的软化台阶**，没有陡峭前沿。工程上「加热多久能透到多深」就是这个公式：透到 $x$ 需要 $t\sim x^2/\alpha$。

**8.30**

**思路**：卷积定理：两个 $e^{-|x|}$ 的卷积，频域是 $\left(\frac{2}{1+k^2}\right)^2$ 的逆变换。查表知 $(1+|x|)e^{-|x|}$ 的谱是 $\frac{4}{(1+k^2)^2}$，所以结果就是它。也可以直接做时域积分核对。

**过程**：由 8.2（取 $a=1$），$\mathcal{F}[e^{-|x|}]=\frac{2}{1+k^2}$。卷积定理：

$$\mathcal{F}\left[e^{-|x|}*e^{-|x|}\right]=\left(\frac{2}{1+k^2}\right)^2=\frac{4}{(1+k^2)^2}.$$

逆变换：$\frac{4}{(1+k^2)^2}$ 对应 $(1+|x|)e^{-|x|}$（这个变换对可由留数算出：$k=\pm i$ 是二阶极点，留数给出 $(1+|x|)e^{-|x|}$）。

直接验证（$x\ge0$）：

$$(f*f)(x)=\int_{-\infty}^{\infty}e^{-|x-s|}e^{-|s|}\mathrm{d}s.$$

把区间按 $s<0$、$0<s<x$、$s>x$ 分段去掉绝对值，三段都是初等积分，相加得 $(1+x)e^{-x}$；由对称性 $x<0$ 时为 $(1+|x|)e^{-|x|}$。

**结果**：

$$\left(e^{-|x|}\right)*\left(e^{-|x|}\right)=(1+|x|)e^{-|x|}.$$

**检验**：(i) $x=0$：右边 $1$；左边 $\int e^{-2|s|}\mathrm{d}s=2\int_0^\infty e^{-2s}\mathrm{d}s=1$ ✓。(ii) 面积：$\int(1+|x|)e^{-|x|}\mathrm{d}x=2\int_0^\infty(1+x)e^{-x}\mathrm{d}x=2(1+1)=4$，而 $\left(\int e^{-|x|}\mathrm{d}x\right)^2=2^2=4$ ✓。(iii) 光滑性：$e^{-|x|}$ 在 $0$ 处有尖角，卷积后 $(1+|x|)e^{-|x|}$ 在 $0$ 处一阶导为零（左右导数都是 $0$），变光滑了一阶 ✓——与「卷积使函数光滑」一致。(iv) 数值：$x=1$ 时 $(1+1)e^{-1}=0.7358$，直接数值积分得 $0.73576$ ✓。

**读法**：每卷积一次，函数就光滑一阶——**这正是「频域除以 $s$（乘 $1/(1+k^2)$）等于时域积分一次」的另一种说法**。概率论里「两个拉普拉斯分布之和」也是这个结果（三角分布的高斯类比）。

## 概念与判断

**8.31** **错。**

**理由**：傅里叶变换是**可逆的线性变换**，正变换与逆变换只差 $1/2\pi$ 与指数符号，信息一点没丢——它只是换了一组基底（8.3.1）。真正的「丢信息」发生在你把变换后的东西**只保留一部分**的时候，比如只留幅度谱、丢掉相位谱。

**可逆性写出来**：

$$f(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\tilde f(k)e^{ikx}\mathrm{d}k .$$

只要 $\tilde f$ 是某个平方可积函数的变换，这条式子就把 $f$ 原样还回来——**没有多一个未知量，也没有少一个**。「变换」本身是恒等操作的一次改写。

**例子**：两个完全不同的信号可以有相同的幅度谱（比如 $f(x)$ 与 $f(-x)$，或任意「相位随机化」的版本），但它们的波形完全不同——这说明**相位携带信息**，幅度谱不携带全部。所以「变换丢信息」是把「截断/取模」的账算到了变换头上。

**8.32** **错。**

**理由**：两句话说的是不同层次的东西。$\delta$ 的谱是常数，意思是**一个确定性脉冲在所有频率上等权重**；白噪声的功率谱是常数，意思是**一个随机过程的各频率分量功率相等**。前者是函数（分布），后者是随机过程，二者的「平坦」不是同一件事。

**反例**：白噪声的幅度是随机的、功率有限但能量无限（持续信号），不存在「某个时刻突然出现」的波形；而 $\delta$ 是一个瞬时脉冲、能量有限。把白噪声当成「随机的 $\delta$ 串」只在「功率谱平坦」这一点上类比成立，不能当成同一个对象。

**8.33** **错。**

**理由**：带宽定理是**傅里叶变换的数学性质**，与「测量是否扰动系统」无关。它说的是：一个函数不能同时具有任意窄的支撑和任意窄的谱。量子力学里的不确定关系是把 $k$ 换成 $p/\hbar$ 之后的结果，$\hbar$ 只是单位换算，不是不确定性来源。

**例子**：声呐的啁啾信号同样受 $\Delta t\,\Delta f\ge1/2$ 约束（8.6.4），这里没有量子、没有测量扰动，纯粹是信号本身的谱宽与时长关系。**「测量扰动」是另一回事**（海森堡显微镜那类论证），不能解释这条不等式。

**8.34** **部分对。**

**对的部分**：把 $s=\sigma+i\omega$ 代入，确实有 $F(\sigma+i\omega)=\int_0^\infty[f(t)e^{-\sigma t}]e^{-i\omega t}\mathrm{d}t$，即**拉普拉斯变换 = 先乘 $e^{-\sigma t}$ 再做单边傅里叶变换**（8.8.2）。

**不对的部分**：只说「乘一个指数因子」漏掉了两件关键的事。第一，**积分下限是 $0$**：这使求导性质多出初值项 $-f(0)$，正是拉普拉斯变换能直接解初值问题的原因；如果从 $-\infty$ 开始，就没有这一项。第二，**$\sigma$ 必须落在收敛域内**，$F(s)$ 是一个复变函数、要带收敛域才有意义，「乘指数」这句话没有体现这一点。

**8.35** **错。**

**理由**：这条判据只对**因果系统**成立（8.10.3 的措辞）。一般情形下，稳定性要求**收敛域包含虚轴**，而收敛域由极点与信号类型共同决定。极点全在左半平面只保证「收敛域可以取到极右极点的左边」，但如果你取的是另一个收敛域（反因果解），稳定性结论会反过来。

**反例（左半极点却不稳定）**：$F(s)=\frac{1}{s+1}$，极点在 $s=-1$（左半平面），但取收敛域 $\sigma<-1$（反因果解），对应 $f(t)=-e^{-t}\theta(-t)$。当 $t\to-\infty$ 时 $e^{-t}\to+\infty$，信号指数增长——**不稳定**。它的收敛域 $\sigma<-1$ 不含虚轴，按「ROC 含虚轴」的判据确实不稳定。

**8.36** **错。**

**理由**：「输出与输入相同」太强了。$\omega\ll\omega_c$ 时 $|H|\approx1$，幅度确实几乎不变，但**相位仍有一个小滞后** $-\arctan(\omega/\omega_c)$，而且这个滞后随频率变化——对不同频率分量滞后不同，就会改变波形（色散）。

**例子**：一个含多个谐波的方波，即使基频远低于 $\omega_c$，各次谐波的相位滞后不同，边沿仍会被轻微抹圆、产生过冲。**要「真正相同」需要 $\omega\tau\to0$ 的极限**，任何有限的 $\omega\tau$ 都只是近似。

**8.37** **错。**

**理由**：热方程是**宏观近似**：它假设连续介质与局域平衡，在「平均自由程/平均碰撞时间」的尺度上已经不成立。所以「瞬时传播」不是物理结论，而是模型在超出适用范围时给出的假象。在适用范围内，离光锥很远处的扰动幅度指数小到无法测量。

**反例（数值）**：$\alpha=10^{-4}\ \mathrm{m^2/s}$、$x=1\ \mathrm{m}$、$t=1\ \mathrm{ms}$，指数因子 $e^{-x^2/(4\alpha t)}=e^{-2.5\times10^6}\sim10^{-10^6}$——比任何可测量的量都小无数个数量级。物理上这等于「没有传播」，相对论没有被违反；被违反的只是「热方程在所有尺度上都成立」这个假设。

**8.38** **错（不必要）。**

**理由**：绝对可积是卷积定理的**充分条件**，不是必要条件。只要 $f,g\in L^2$，卷积与变换都可以在 $L^2$（或分布）意义下定义，定理仍然成立。物理上更常见的判据是「系统稳定」：极点全在左半平面。

**反例**：$h(t)=\frac{\sin t}{t}$（sinc）。它不绝对可积（$\int|\sin t/t|\mathrm{d}t=\infty$），但属于 $L^2$，傅里叶变换是矩形函数（带限信号），与 $L^2$ 输入的卷积收敛、卷积定理成立。**理想积分器**（$h=\theta(t)$）则是真正越界的情形：它连 $L^2$ 都不属于，卷积对常数输入发散（8.25）。

**8.39** **错。**

**理由**：$H(s)$ 只是复平面上的一个函数，**必须连同收敛域才是完整的系统描述**。同一个 $H(s)$ 配不同收敛域，对应不同的时域信号（因果、反因果、双边），稳定性也不同。

**反例**：$F(s)=\frac{1}{s-1}$，收敛域取 $\sigma>1$ 时 $f=e^t\theta(t)$（因果、不稳定）；取 $\sigma<1$ 时 $f=-e^t\theta(-t)$（反因果、稳定）。**同一个 $H(s)$，两种完全不同的响应**（8.26）。所以工程上写传递函数时必须注明收敛域，或默认因果。

## 第 9 章

**9.1** 思路：单变量、两端固定，直接套欧拉–拉格朗日方程。

过程：$F=y'^2+2y$，于是 $F_y=2$、$F_{y'}=2y'$。代入 $\dfrac{\partial F}{\partial y}-\dfrac{\mathrm{d}}{\mathrm{d}x}\dfrac{\partial F}{\partial y'}=0$：

$$2-\frac{\mathrm{d}}{\mathrm{d}x}\left(2y'\right)=0\quad\Longrightarrow\quad y''=1 .$$

积分一次 $y'=x+c_1$，再积一次 $y=\dfrac{x^2}{2}+c_1x+c_2$。由 $y(0)=0$ 得 $c_2=0$；由 $y(1)=1$ 得 $\dfrac12+c_1=1$，即 $c_1=\dfrac12$。

**结果：** $y=\dfrac{x^2+x}{2}$（$0\le x\le1$）．

**检验：** 端点值 $y(0)=0$、$y(1)=1$ 对得上；代回方程 $y''=1$ 也对。若无 $2y$ 这一项，方程是 $y''=0$，解是直线——加一项"载荷"就从直线弯成抛物线。

**读法：** 被积函数里的 $2y$ 相当于沿弦均匀分布的横向力，方程 $y''=$ 常数正是梁在均布载荷下的形状方程。

**9.2** 思路：$F$ 不含 $y$，所以 $\partial F/\partial y'$ 是常数，一次积分就完，不必写二阶方程。

过程：$F=(1+x)^2y'^2$，$\dfrac{\partial F}{\partial y'}=2(1+x)^2y'$。方程 $\dfrac{\mathrm{d}}{\mathrm{d}x}\left[2(1+x)^2y'\right]=0$ 直接给

$$(1+x)^2y'=c\quad\Longrightarrow\quad y'=\frac{c}{(1+x)^2}\quad\Longrightarrow\quad y=-\frac{c}{1+x}+d .$$

**结果：** $y=d-\dfrac{c}{1+x}$，两个常数由端点值定；$\dfrac{1}{1+x}$ 型曲线的斜率按 $(1+x)^{-2}$ 衰减。

**检验：** 求导代回：$y'=c(1+x)^{-2}$，$(1+x)^2y'=c$ 确为常数 ✓。量纲上 $c$ 与 $y(1+x)$ 同量纲。

**读法：** 方程里没有 $y$，说明"把整条曲线上下平移"不改变泛函值——平移对称性，对应 $\partial F/\partial y'$ 守恒。

**9.3** 思路：$F=\sqrt{y(1+y'^2)}$ 不含 $x$，用贝尔特拉米恒等式降阶。

过程：$F_{y'}=\dfrac{\sqrt y\,y'}{\sqrt{1+y'^2}}$，于是

$$F-y'F_{y'}=\sqrt{y}\sqrt{1+y'^2}-\frac{\sqrt y\,y'^2}{\sqrt{1+y'^2}}
=\frac{\sqrt y}{\sqrt{1+y'^2}}=C .$$

两边平方并整理：$y'^2=\dfrac{y}{C^2}-1$，即 $\dfrac{\mathrm{d}y}{\mathrm{d}x}=\dfrac{\sqrt{y-C^2}}{C}$。分离变量

$$\int\frac{\mathrm{d}y}{\sqrt{y-C^2}}=\int\frac{\mathrm{d}x}{C}
\quad\Longrightarrow\quad 2\sqrt{y-C^2}=\frac{x+d}{C}.$$

**结果：** $y=C^2+\dfrac{(x+d)^2}{4C^2}$，一族抛物线，两个常数由端点定。

**检验：** 把 $y'=\dfrac{x+d}{2C^2}$ 代回 $y(1+y'^2)=C^2+(x+d)^2/(4C^2)+\dfrac{(x+d)^2}{4C^2}$，即 $y-C^2=C^2y'^2$，与 $y'^2=(y-C^2)/C^2$ 一致 ✓。

**读法：** 这个泛函出现在"给定水平跨度、求最短旋转面"一类问题里，最优曲线是抛物线而不是悬链线——因为被积函数是 $\sqrt y$ 而不是 $y$。

**9.4** 思路：被积函数含 $y''$，用高阶欧拉–拉格朗日方程，逐项求偏导。

过程：$F=y^2+y'^2+y''^2$，三个偏导为

$$F_y=2y,\qquad F_{y'}=2y',\qquad F_{y''}=2y'' .$$

代入 $\dfrac{\partial F}{\partial y}-\dfrac{\mathrm{d}}{\mathrm{d}x}\dfrac{\partial F}{\partial y'}+\dfrac{\mathrm{d}^2}{\mathrm{d}x^2}\dfrac{\partial F}{\partial y''}=0$：

$$2y-\frac{\mathrm{d}}{\mathrm{d}x}\left(2y'\right)+\frac{\mathrm{d}^2}{\mathrm{d}x^2}\left(2y''\right)=0
\quad\Longrightarrow\quad y''''-y''+y=0 .$$

**结果：** 四阶常系数方程 $y''''-y''+y=0$。特征方程 $k^4-k^2+1=0$，$k^2=\dfrac{1\pm i\sqrt3}{2}$，四个根都有非零实部，解含 $e^{\pm x/2}\cos(\sqrt3x/2)$ 型因子。

**检验：** 量纲上 $y,y',y''$ 的量纲分别是 $[y]$、$[y]/[x]$、$[y]/[x]^2$，若 $x$ 无量纲则三项可比；阶数为四，需要四个边界条件（每端两个）。

**读法：** 含 $y''$ 的泛函给四阶方程，对应"梁的弯曲"——位移、转角各给一个端点条件，正好四个。

**9.5** 思路：$F=y'^3$ 对 $y'$ 不是二次的，直接算 $\mathrm{d}/\mathrm{d}x\,\partial F/\partial y'$。

过程：$F_y=0$，$F_{y'}=3y'^2$，方程是

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(3y'^2\right)=0\quad\Longrightarrow\quad 6y'y''=0 .$$

它只要求 $y'=0$（水平线）或 $y''=0$（直线）。由 $y(0)=0$、$y(1)=1$ 得 $y=x$。但 $F_{y'y'}=6y'$ 在 $y'=0$ 处为零，**方程退化**。

**结果：** 驻点方程退化成 $6y'y''=0$；$y=x$ 是驻点，但**泛函没有极小**：取在 $[0,\delta]$ 上斜率 $-M$、其余斜率 $\dfrac{1+M\delta}{1-\delta}$ 的分段线性函数，$\delta=1/M^2$ 时 $\int y'^3\approx-M+1\to-\infty$。

**检验：** 用 $y=x+\epsilon\sin2\pi x$ 检验：$\int_0^1y'^3=1+\dfrac32\epsilon^2>1$，说明直线是局部极小——但全局没有下界，两者不矛盾。

**读法：** "$\partial^2F/\partial y'^2=0$"是退化变分问题的判据：欧拉–拉格朗日方程只剩代数关系，既可能无解，也可能像这里一样有驻点而无极值。

**9.6** 思路：$L=T=\rho=1$ 时瑞利商就是 $\int y'^2/\int y^2$，代入试函数算两个定积分。

过程：$y=x(1-x)=x-x^2$，$y'=1-2x$。

$$\int_0^1y'^2\,\mathrm{d}x=\int_0^1(1-4x+4x^2)\,\mathrm{d}x=1-2+\frac43=\frac13,$$

$$\int_0^1y^2\,\mathrm{d}x=\int_0^1(x^2-2x^3+x^4)\,\mathrm{d}x=\frac13-\frac12+\frac15=\frac{1}{30}.$$

于是 $R=\dfrac{1/3}{1/30}=10$。

**结果：** $R=10\,T/(\rho L^2)$，精确值 $\pi^2T/(\rho L^2)=9.8696$，高 $1.32\%$。

**检验：** 由 9.7.2 的加权平均式，$R\ge\lambda_1$ 必须成立，$10>9.8696$ ✓。$y=x(1-x)$ 满足 $y(0)=y(1)=0$，本质边界条件没破。

**读法：** 一个不微分的二次函数就把基频估到 1% 以内，因为它的形状和 $\sin\pi x$ 差别不大——变分估计的精度主要看"形状像不像"。

**9.7** 思路：$\sin\pi x$ 就是第一本征函数，代入后加权平均退化成单项，所以应当恰好等于 $\pi^2$。

过程：$y=\sin\pi x$，$y'=\pi\cos\pi x$。

$$\int_0^1y'^2\,\mathrm{d}x=\pi^2\int_0^1\cos^2\pi x\,\mathrm{d}x=\frac{\pi^2}{2},\qquad
\int_0^1y^2\,\mathrm{d}x=\int_0^1\sin^2\pi x\,\mathrm{d}x=\frac12 .$$

$$R=\frac{\pi^2/2}{1/2}=\pi^2 .$$

**结果：** $R=\pi^2=9.8696$，与精确值相等（相对误差 0）。

**检验：** 展开系数 $c_1=1$、其余为零，加权平均式 $\sum c_n^2\lambda_n/\sum c_n^2$ 只剩 $\lambda_1$ ✓。若取 $y=\sin2\pi x$，$R=4\pi^2$（第二本征值），也等于真值——这说明瑞利商对任何本征函数都精确。

**读法：** 瑞利商是"加权平均"，最小值才等于 $\lambda_1$；拿本征函数代进去自然精确。实践中不知道本征函数，所以只能用近似形状。

**9.8** 思路：端点自由时边界项不为零，要它消失只能让 $F_{y'}$ 在端点为零。

过程：端点自由意味着 $\delta y(0)$、$\delta y(1)$ 任意。一阶变分

$$\delta J=\left[F_{y'}\delta y\right]_0^1-\int_0^1\left(F_y-\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}\right)\delta y\,\mathrm{d}x .$$

取 $\delta y$ 在内部为零、只在端点非零，第二项消失，剩 $\left[F_{y'}\delta y\right]_0^1=0$。它对任意 $\delta y(0),\delta y(1)$ 成立，故

$$F_{y'}(0)=0,\qquad F_{y'}(1)=0 .$$

**结果：** 自然边界条件 $y'(0)=y'(1)=0$（因为 $F_{y'}=2y'$）。配上 $y''=y$（由 $2y-2y''=0$）得 $y=A\cosh x+B\sinh x$；$y'(0)=B=0$、$y'(1)=A\sinh1=0$ 给出 $A=B=0$。

**检验：** $y\equiv0$ 时泛函为 0，而泛函正定，所以 0 是最小值 ✓。若误加 $y(0)=y(1)=0$ 的狄利克雷条件，会得到非零解族 $A\sinh$，那不是本题的解。

**读法：** 端点自由时"边界条件由变分自己给"，这就是自然边界条件的来源；用里兹法时不必把它写进试函数。

**9.9** 思路：有限维约束极值，用拉格朗日乘子把约束并进目标。

过程：目标 $A=xy$，约束 $g=2(x+y)-L=0$。构造

$$\mathcal L=xy-\lambda\left[2(x+y)-L\right].$$

$$\frac{\partial\mathcal L}{\partial x}=y-2\lambda=0,\qquad
\frac{\partial\mathcal L}{\partial y}=x-2\lambda=0 .$$

两式相减得 $x=y$；代回约束 $4x=L$，即 $x=y=L/4$。

**结果：** 正方形，边长 $L/4$，面积 $A=L^2/16$。乘子 $\lambda=L/8$。

**检验：** 取 $x=L/4+\epsilon$、$y=L/4-\epsilon$（周长不变），面积 $=L^2/16-\epsilon^2<L^2/16$ ✓ 是极大。量纲：$\lambda$ 与长度同量纲。

**读法：** 等周问题的"只许用矩形"版本；没有矩形限制时最优点是圆（$A=L^2/4\pi=0.0796L^2$），比正方形多 27%。

**9.10** 思路：二阶变分的符号由 $F_{y'y'}$ 决定，算出来看正负。

过程：$F=\sqrt{1+y'^2}$。先算一阶偏导

$$F_{y'}=\frac{y'}{\sqrt{1+y'^2}},$$

再对 $y'$ 求导（把 $y'$ 看成自变量）：

$$F_{y'y'}=\frac{\sqrt{1+y'^2}-y'\cdot\dfrac{y'}{\sqrt{1+y'^2}}}{1+y'^2}
=\frac{1}{\left(1+y'^2\right)^{3/2}} .$$

二阶变分是

$$\delta^2J=\frac12\int_a^b\left(F_{yy}\eta^2+2F_{yy'}\eta\eta'+F_{y'y'}\eta'^2\right)\mathrm{d}x
=\frac12\int_a^b\frac{\eta'^2}{\left(1+y'^2\right)^{3/2}}\,\mathrm{d}x .$$

**结果：** $F_{y'y'}=(1+y'^2)^{-3/2}>0$，$\delta^2J>0$（对一切非零 $\eta$），所以直线是**严格极小**。

**检验：** 几何直觉：两点间线段最短 ✓。若把 $F$ 换成 $-\sqrt{1+y'^2}$（求最长），$F_{y'y'}<0$，二阶变分为负——同样的驻点变成极大。

**读法：** $F_{y'y'}>0$ 是"泛函局部凸"的意思，也是极小性的充分条件；最速降线的 $F_{y'y'}=1/(\sqrt{2gy}(1+y'^2)^{3/2})>0$ 同理。

**9.11** 思路：摆线的参数由终点坐标定，时间用 $T=\varphi_B\sqrt{a/g}$。

过程：终点条件 $\dfrac{1-\cos\varphi_B}{\varphi_B-\sin\varphi_B}=\dfrac{y_B}{x_B}=\dfrac12$。这个方程没有初等解，数值求根 $\varphi_B=3.508$。再由 $y_B=a(1-\cos\varphi_B)$：

$$a=\frac{1}{1-\cos3.508}=\frac{1}{1.9337}=0.517\ \mathrm{m}.$$

$$T=\varphi_B\sqrt{\frac{a}{g}}=3.508\sqrt{\frac{0.517}{9.81}}=0.806\ \mathrm{s}.$$

**结果：** $\varphi_B=3.508$，$a=0.517\ \mathrm{m}$，$T=0.806\ \mathrm{s}$；直线用时 $T_{\text{直}}=\dfrac{2\sqrt{1+m^2}}{\sqrt{2gm}}\sqrt{x_B}=1.010\ \mathrm{s}$，摆线快 $20\%$。

**检验：** 量纲：$a$ 是长度 ✓，$\sqrt{a/g}$ 是时间 ✓。极限 $y_B/x_B\to0$（终点很"横"）时 $\varphi_B\to2\pi$，$a\to y_B/2$，$T\to2\pi\sqrt{y_B/2g}$——直落再横走的时间，合理。

**读法：** 终点越"横"，摆线优势越大：横向距离大时，直线的低速段太长。

**9.12** 思路：从任意 $\varphi_1$ 由静止释放，用能量守恒写速率，再对弧长积分，换元后起始参数应当消掉。

过程：能量守恒 $v=\sqrt{2g(y-y_1)}$，而 $y=a(1-\cos\varphi)=2a\sin^2\dfrac{\varphi}{2}$，所以

$$v=2\sqrt{ga}\sqrt{\sin^2\frac{\varphi}{2}-\sin^2\frac{\varphi_1}{2}} .$$

弧长元 $\mathrm{d}s=2a\sin\dfrac{\varphi}{2}\,\mathrm{d}\varphi$，于是

$$T=\sqrt{\frac{a}{g}}\int_{\varphi_1}^{\pi}\frac{\sin(\varphi/2)\,\mathrm{d}\varphi}{\sqrt{\sin^2(\varphi/2)-\sin^2(\varphi_1/2)}} .$$

令 $u=\cos\dfrac{\varphi}{2}$，则 $\sin\dfrac{\varphi}{2}\mathrm{d}\varphi=-2\mathrm{d}u$，分母 $=\sqrt{u^2-u_1^2}$，下限 $u=u_1$、上限 $u=0$：

$$T=2\sqrt{\frac{a}{g}}\int_0^{u_1}\frac{\mathrm{d}u}{\sqrt{u_1^2-u^2}}
=2\sqrt{\frac{a}{g}}\cdot\frac{\pi}{2}=\pi\sqrt{\frac{a}{g}} .$$

**结果：** $T=\pi\sqrt{a/g}$，与起始位置 $\varphi_1$ 无关（等时性）。

**检验：** 取 $\varphi_1=0$（从尖点释放）时回到 9.1.4 的 $T=\sqrt{a/g}\,\varphi_B$ 在 $\varphi_B=\pi$ 的值 ✓。量纲：时间 ✓。

**读法：** 这是惠更斯摆钟的原理：把摆锤限制在摆线挡板之间，周期与振幅无关。

**9.13** 思路：悬链线参数由垂度条件定，链长与张力是它的两个导出量。

过程：半跨 $d=10\ \mathrm{m}$、垂度 $f=3\ \mathrm{m}$，悬链线 $y=a\cosh(x/a)$ 满足

$$a\left(\cosh\frac{10}{a}-1\right)=3 .$$

数值解 $a=17.14\ \mathrm{m}$。链长与水平张力：

$$L=2a\sinh\frac{d}{a}=34.29\times\sinh(0.5833)=21.15\ \mathrm{m},$$

$$H=\rho g a=1\times9.81\times17.14=168\ \mathrm{N}.$$

**结果：** $a=17.1\ \mathrm{m}$，$L=21.2\ \mathrm{m}$（比跨度长 $5.7\%$），$H=168\ \mathrm{N}$。

**检验：** 小垂度极限：$f\approx d^2/(2a)$ 给 $a\approx d^2/2f=100/6=16.7\ \mathrm{m}$，与 17.1 相差 3%，说明抛物线近似在这个垂度下已够用 ✓。

**读法：** 垂度越小、$a$ 越大、张力越大：把垂度从 3 m 压到 1 m，$a\approx50\ \mathrm{m}$，张力升到约 490 N。

**9.14** 思路：张力给定就是 $a$ 给定，垂度反算。

过程：$H=\rho ga$ 给

$$a=\frac{H}{\rho g}=\frac{2000}{0.5\times9.81}=407.7\ \mathrm{m}.$$

垂度是端点与最低点的高差：

$$f=a\left(\cosh\frac{25}{a}-1\right)=407.7\left(\cosh0.06132-1\right).$$

用 $\cosh u-1\approx u^2/2$：$f\approx407.7\times\dfrac{0.06132^2}{2}=0.766\ \mathrm{m}$。

**结果：** $a=408\ \mathrm{m}$，垂度 $f=0.77\ \mathrm{m}$。

**检验：** 抛物线近似 $f\approx\rho gd^2/(2H)=\dfrac{0.5\times9.81\times625}{2\times2000}=0.766\ \mathrm{m}$，与精确值差 $<0.1\%$ ✓（$u=0.061\ll1$，近似合法）。

**读法：** 高压线拉得越紧垂度越小，但杆塔受力越大；给定张力上限就能反推最小垂度。

**9.15** 思路：三种形状都用周长表出面积，直接比数值。

过程：圆 $L=2\pi R$，$R=L/2\pi$，

$$A_\odot=\pi R^2=\frac{L^2}{4\pi}=0.0796L^2 .$$

正方形边长 $L/4$：$A_\square=L^2/16=0.0625L^2$。

正三角形边长 $L/3$：$A_\triangle=\dfrac{\sqrt3}{4}\left(\dfrac{L}{3}\right)^2=\dfrac{\sqrt3}{36}L^2=0.0481L^2$。

**结果：** $A_\odot:A_\square:A_\triangle=0.0796:0.0625:0.0481$，圆最大。

**检验：** 三者都满足等周不等式 $A\le L^2/4\pi$，且边数越多越接近上界 ✓（$0.0625<0.0796$，$0.0481<0.0625$）。

**读法：** 等周问题的答案是圆；正多边形按边数排序逼近圆，这就是"同样材料围出最大面积"的定量版本。

**9.16** 思路：费马原理 + 贝尔特拉米恒等式（$n$ 只依赖 $y$，被积函数不含 $x$）。

过程：光程 $J=\int n_0e^{-y/h}\sqrt{1+y'^2}\,\mathrm{d}x$，首次积分

$$\frac{n_0e^{-y/h}}{\sqrt{1+y'^2}}=C\quad\Longrightarrow\quad\sqrt{1+y'^2}=ke^{-y/h},\quad k=\frac{n_0}{C}.$$

分离变量：令 $u=e^{-y/h}$，$\mathrm{d}y=-h\,\mathrm{d}u/u$，

$$\mathrm{d}x=-\frac{h\,\mathrm{d}u}{u\sqrt{k^2u^2-1}}
\quad\Longrightarrow\quad x-x_0=-h\arccos\frac{1}{ku}.$$

反解

$$y=h\ln\left[k\cos\frac{x-x_0}{h}\right].$$

**结果：** 路径是"对数余弦"曲线 $y=h\ln\left[k\cos\dfrac{x-x_0}{h}\right]$；在 $x=x_0$ 处最高，向两侧下降（光线弯向折射率大的低处）。

**检验：** 代回首次积分：$y'=-\tan\dfrac{x-x_0}{h}$，$\sqrt{1+y'^2}=\sec$，$e^{-y/h}=\dfrac{1}{k\cos}$，乘积 $=\dfrac{1}{k}$ 为常数 ✓。$h\to\infty$（均匀介质）时 $y\to$ 常数 $+$ 直线 ✓。

**读法：** 这就是海市蜃楼的光路：热地面附近 $n$ 随高度下降，光线向下弯，远处景物的像被抬起来。

**9.17** 思路：写出 $L=T-V$，套欧拉–拉格朗日方程；小角化后读周期。

过程：摆长 $l$、摆角 $\theta$（从竖直向下量），

$$L=\frac12ml^2\left(\frac{\mathrm{d}\theta}{\mathrm{d}t}\right)^2+mgl\cos\theta .$$

$$\frac{\partial L}{\partial\theta}=-mgl\sin\theta,\qquad
\frac{\partial L}{\partial(\mathrm{d}\theta/\mathrm{d}t)}=ml^2\frac{\mathrm{d}\theta}{\mathrm{d}t},\qquad
\frac{\mathrm{d}}{\mathrm{d}t}\left(ml^2\frac{\mathrm{d}\theta}{\mathrm{d}t}\right)=ml^2\frac{\mathrm{d}^2\theta}{\mathrm{d}t^2}.$$

代入方程得 $ml^2\dfrac{\mathrm{d}^2\theta}{\mathrm{d}t^2}+mgl\sin\theta=0$，即

$$\frac{\mathrm{d}^2\theta}{\mathrm{d}t^2}+\frac{g}{l}\sin\theta=0 .$$

小角 $\sin\theta\approx\theta$：$\omega=\sqrt{g/l}$，$T=2\pi\sqrt{l/g}=2\pi\sqrt{1/9.81}=2.01\ \mathrm{s}$。

**结果：** 方程 $\dfrac{\mathrm{d}^2\theta}{\mathrm{d}t^2}+\dfrac{g}{l}\sin\theta=0$；$l=1\ \mathrm{m}$ 时 $T=2.01\ \mathrm{s}$。

**检验：** 量纲 $\sqrt{l/g}=$ 时间 ✓；$\theta\to0$ 时回到简谐振动，与牛顿力学一致 ✓。

**读法：** 大角度时周期**变长**：$\sin\theta<\theta$ 使回复力偏小，摆得慢；$\theta_0=30^\circ$ 时约长 $1.7\%$。

**9.18** 思路：一维拉格朗日量，直接代入。

过程：$L=\dfrac12m\left(\dfrac{\mathrm{d}x}{\mathrm{d}t}\right)^2-\dfrac12kx^2$，

$$\frac{\partial L}{\partial x}=-kx,\qquad
\frac{\partial L}{\partial(\mathrm{d}x/\mathrm{d}t)}=m\frac{\mathrm{d}x}{\mathrm{d}t},\qquad
\frac{\mathrm{d}}{\mathrm{d}t}\left(m\frac{\mathrm{d}x}{\mathrm{d}t}\right)=m\frac{\mathrm{d}^2x}{\mathrm{d}t^2}.$$

方程 $m\dfrac{\mathrm{d}^2x}{\mathrm{d}t^2}+kx=0$。两边除以 $m$ 得标准形式；初值 $x(0)=x_0$、$\dot x(0)=0$ 时解为 $x=x_0\cos\omega t$（这里 $\dot x$ 表示 $\dfrac{\mathrm{d}x}{\mathrm{d}t}$）。

**结果：** $\dfrac{\mathrm{d}^2x}{\mathrm{d}t^2}+\omega^2x=0$，$\omega=\sqrt{k/m}$，$T=2\pi\sqrt{m/k}$；通解 $x=A\cos(\omega t+\varphi_0)$。

**检验：** 与牛顿第二定律 $F=-kx$ 一致 ✓；量纲 $\sqrt{k/m}=\sqrt{(\mathrm{N/m})/\mathrm{kg}}=\mathrm{s^{-1}}$ ✓。能量 $E=\frac12m\left(\dfrac{\mathrm{d}x}{\mathrm{d}t}\right)^2+\frac12kx^2$ 对 $t$ 求导为零（$\dfrac{\mathrm{d}E}{\mathrm{d}t}=\dot x(m\ddot x+kx)=0$），与无阻尼一致。

**读法：** 变分原理给的运动方程与牛顿力学逐项相同——换出发点不换结果。

**9.19** 思路：悬链面参数由环的半径与间距定，解一个含 $\cosh$ 的方程。

过程：半间距 $z_0=1\ \mathrm{cm}$、环半径 $R=2\ \mathrm{cm}$，条件

$$a\cosh\frac{z_0}{a}=R\quad\Longrightarrow\quad a\cosh\frac{1}{a}=2\ \ (\text{单位 cm}).$$

数值求根：$a=1.5$ 时 $1.5\cosh0.667=1.5\times1.229=1.84<2$；$a=1.8$ 时 $1.8\cosh0.556=1.8\times1.157=2.08>2$；细算得 $a=1.697\ \mathrm{cm}$。

**结果：** 腰部半径 $a=1.70\ \mathrm{cm}$（比环半径小 $15\%$）。

**检验：** 代回 $a\cosh(1/a)=1.697\cosh0.589=1.697\times1.179=2.00$ ✓。若两环间距为 0，$a=R$（膜是平的）✓。

**读法：** 间距越大腰部越细，超过 $1.33R$ 时解消失、膜跳成两个圆盘（哥德施密特不连续）。

**9.20** 思路：圆柱面是旋转面，测地线由"展开成平面"或首次积分给出；这里用展开最直接，再用变分验证。

过程：圆柱面展开后是平面，两点间的直线在面上对应螺旋线：绕行的弧长 $R\Delta\varphi=\pi/2$，上升的高度 $\Delta z=2$，两者垂直，合成

$$L=\sqrt{\left(R\Delta\varphi\right)^2+\left(\Delta z\right)^2}
=\sqrt{\left(\frac{\pi}{2}\right)^2+2^2}=\sqrt{6.467}=2.54 .$$

变分验证：$L=\int\sqrt{R^2+z'^2}\,\mathrm{d}\varphi$ 不含 $z$，故 $z'/\sqrt{R^2+z'^2}=$ 常数，即 $z'$ 为常数——$z$ 随 $\varphi$ 线性增长，正是螺旋线。

**结果：** $L=2.54\,R$（$R=1$ 时 $2.54\ \mathrm{m}$），路径是螺旋线 $z=\dfrac{2}{\pi/2}\varphi=\dfrac{4}{\pi}\varphi$。

**检验：** 展开图上直线长度 $\sqrt{(\pi/2)^2+2^2}$ 与面积公式一致 ✓；极限情形 $\Delta z=0$ 给 $L=R\Delta\varphi$（沿圆周），$\Delta\varphi=0$ 给 $L=\Delta z$（沿母线），都对。

**读法：** 测地线"展开成直线"这条经验，对任何可展曲面（柱面、锥面）都成立，对球面不成立（球面不能展开成平面）。

**9.21** 思路：瑞利商 $R=\int py'^2/\int wy^2$，试函数只需满足本质边界条件 $y(0)=0$。

过程：方程 $-EAy''=\lambda\rho y$，即 $p=EA$、$w=\rho$、$q=0$。取 $y=x$（满足 $y(0)=0$；自由端 $y'(L)=0$ 是自然条件，不必强加）：

$$\int_0^Ly'^2\,\mathrm{d}x=L,\qquad \int_0^Ly^2\,\mathrm{d}x=\frac{L^3}{3},$$

$$R=\frac{EA\cdot L}{\rho\cdot L^3/3}=\frac{3EA}{\rho L^2} .$$

**结果：** $R=3\dfrac{EA}{\rho L^2}$，精确值 $\lambda_1=\dfrac{\pi^2}{4}\dfrac{EA}{\rho L^2}=2.467\dfrac{EA}{\rho L^2}$，高 $21.6\%$。

**检验：** 上界性质 $3>2.467$ ✓。若试函数取 $\sin(\pi x/2L)$（第一本征函数），$R$ 应恰好等于 $\pi^2/4$——可作进一步练习。

**读法：** $y=x$ 是"杆被均匀拉伸"的形状，与真实模态（四分之一正弦）差得不小，所以误差 20%；换一个像一点的试函数立刻降到 1% 以下。

**9.22** 思路：与 9.11 同一套公式，只换终点长度；两个终点在同一条射线上，所以参数成比例。

过程：$\dfrac{1-\cos\varphi_B}{\varphi_B-\sin\varphi_B}=\dfrac{0.5}{1}=0.5$，数值解 $\varphi_B=3.508$（与 9.11 相同，因为 $y_B/x_B$ 相同）。

$$a=\frac{y_B}{1-\cos\varphi_B}=\frac{0.5}{1.9337}=0.259\ \mathrm{m},\qquad
T=3.508\sqrt{\frac{0.259}{9.81}}=0.570\ \mathrm{s}.$$

直线：$T_{\text{直}}=\dfrac{2\sqrt{1+0.25}}{\sqrt{2\times9.81\times0.5}}\sqrt{1}=0.714\ \mathrm{s}$。

**结果：** 摆线 $0.570\ \mathrm{s}$，直线 $0.714\ \mathrm{s}$，摆线快 $25\%$。

**检验：** 标度关系：终点坐标同乘 $\Lambda$ 时 $a\mapsto\Lambda a$、$T\mapsto\sqrt\Lambda T$；这里 $\Lambda=1/2$，$a$ 是 9.11 的一半（$0.517/2=0.259$ ✓），$T$ 是 $1/\sqrt2$（$0.806/1.414=0.570$ ✓）。

**读法：** 终点越近、越"横"，摆线相对直线的优势越大——短距离时直线的加速段占比更高。

**9.23** 思路：先解欧拉–拉格朗日方程找驻点，再用二阶变分在某条扰动方向上算符号。

过程：$F=y'^2-4\pi^2y^2$，$F_y=-8\pi^2y$，$F_{y'}=2y'$，方程

$$-8\pi^2y-\frac{\mathrm{d}}{\mathrm{d}x}\left(2y'\right)=0\quad\Longrightarrow\quad y''+4\pi^2y=0 .$$

通解 $y=A\sin2\pi x+B\cos2\pi x$，端点条件给 $B=0$，故驻点是 $y=A\sin2\pi x$，且对它们 $J=0$。

二阶变分 $\delta^2J[\eta]=\int_0^1\left(\eta'^2-4\pi^2\eta^2\right)\mathrm{d}x$。取 $\eta=\sin\pi x$：

$$\int_0^1\eta'^2=\frac{\pi^2}{2},\qquad \int_0^1\eta^2=\frac12,\qquad
\delta^2J=\frac{\pi^2}{2}-4\pi^2\cdot\frac12=-\frac{3\pi^2}{2}<0 .$$

**结果：** 驻点族 $y=A\sin2\pi x$，$J=0$；沿 $\eta=\sin\pi x$ 方向 $J$ 减小，所以是**鞍点**，不是极小。

**检验：** 直接把 $y=A\sin2\pi x+\epsilon\sin\pi x$ 代入：交叉项为零（正交），$J=\epsilon^2\left(\pi^2/2-2\pi^2\right)<0$，与二阶变分的结论一致 ✓。

**读法：** 判断稳定性必须看二阶变分；只看 $\delta J=0$ 会把鞍点误当极小。

**9.24** 思路：不预设方程，直接对 $F-y'F_{y'}$ 求全导数，看它等于什么。

过程：$F=F(x,y,y')$，求导

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(F-y'F_{y'}\right)
=F_x+F_yy'+F_{y'}y''-y''F_{y'}-y'\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}
=F_x+y'\left(F_y-\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}\right).$$

- 若欧拉–拉格朗日方程 $F_y-\dfrac{\mathrm{d}}{\mathrm{d}x}F_{y'}=0$ 成立且 $F_x=0$，则右边为零，得 $F-y'F_{y'}=$ 常数。
- 反之，若 $F-y'F_{y'}=$ 常数且 $F_x=0$，则 $y'\left(F_y-\dfrac{\mathrm{d}}{\mathrm{d}x}F_{y'}\right)=0$：在 $y'\ne0$ 的区间上方程成立；$y'\equiv0$（水平直线）是另一支。

**结果：** 在 $y'\ne0$ 的区间上，贝尔特拉米恒等式与欧拉–拉格朗日方程等价（前者是后者的一次积分）。

**检验：** 用最短路径检验：$F=\sqrt{1+y'^2}$，$F-y'F_{y'}=\dfrac{1}{\sqrt{1+y'^2}}=$ 常数给 $y'=$ 常数，与直接解方程的结果一致 ✓。

**读法：** "首次积分"不是另一个方程，它是方程积分一次的结果；所以在 $y'$ 变号的解上要分段讨论。

**9.25** 思路：两个变量、一个约束，用拉格朗日乘子。

过程：$V=\pi r^2h$，$S=2\pi r^2+2\pi rh$。构造

$$\mathcal L=\pi r^2h-\lambda\left(2\pi r^2+2\pi rh-S\right).$$

$$\frac{\partial\mathcal L}{\partial r}=2\pi rh-\lambda\left(4\pi r+2\pi h\right)=0,\qquad
\frac{\partial\mathcal L}{\partial h}=\pi r^2-2\pi r\lambda=0 .$$

第二式给 $\lambda=\dfrac{r}{2}$，代入第一式：$2rh=\dfrac{r}{2}\left(4r+2h\right)$，即 $2rh=2r^2+rh$，故 $h=2r$。

**结果：** 高等于直径（$h=2r$）时，给定表面积下体积最大；$r=\sqrt{S/(6\pi)}$，$V=\sqrt{S^3/(54\pi)}$。

**检验：** 代回约束：$S=2\pi r^2+4\pi r^2=6\pi r^2$ ✓。取 $h\to0$（扁平）或 $h\to\infty$（细长）体积都趋于零，所以中间必有极大。

**读法：** 圆柱罐"高等于直径"最省料，这就是易拉罐的经典比例（实际产品为堆叠和手感会略高一些）。

**9.26** 思路：自由端的边界项要求 $F_{y'}=0$，代入悬链线的解看它在哪里成立。

过程：悬链线 $F=(y-\mu)\sqrt{1+y'^2}$，$F_{y'}=\dfrac{(y-\mu)y'}{\sqrt{1+y'^2}}$。自由端要求

$$F_{y'}=0\quad\Longrightarrow\quad y'=0\quad\text{或}\quad y=\mu .$$

而解 $y-\mu=a\cosh\dfrac{x-x_0}{a}\ge a>0$ 恒成立，故只能 $y'=0$。

**结果：** 自由端滑到 $y'=0$ 处，即链条的**最低点**（该处张力没有竖直分量，也无水平外力的支撑点）。

**检验：** 端点力平衡：自由端没有外力，张力只能为零；而张力竖直分量 $\rho gs$（$s$ 是从最低点起算的弧长）在最低点为零 ✓。

**读法：** 一端自由的链条会竖直垂下、末端就是最低点——挂着的绳子自由端总是垂到最低处。

**9.27** 思路：把大圆方程化成 $\cot\theta=k\cos\varphi$，求导得 $\theta'$，代入首次积分。

过程：由 $\cos\theta=k\sin\theta\cos\varphi$ 两边除 $\sin\theta$：$\cot\theta=k\cos\varphi$。对 $\varphi$ 求导：

$$-\csc^2\theta\,\theta'=-k\sin\varphi\quad\Longrightarrow\quad\theta'=k\sin\varphi\sin^2\theta .$$

于是

$$\theta'^2+\sin^2\theta=\sin^2\theta\left(1+k^2\sin^2\varphi\sin^2\theta\right).$$

用 $\sin^2\varphi=1-\cos^2\varphi=1-\dfrac{\cot^2\theta}{k^2}$ 化简方括号：

$$1+k^2\sin^2\varphi\sin^2\theta=1+k^2\sin^2\theta-\cos^2\theta=\sin^2\theta\left(1+k^2\right).$$

故 $\sqrt{\theta'^2+\sin^2\theta}=\sin^2\theta\sqrt{1+k^2}$，首次积分

$$\frac{\sin^2\theta}{\sqrt{\theta'^2+\sin^2\theta}}=\frac{1}{\sqrt{1+k^2}} .$$

**结果：** 首次积分恒为 $1/\sqrt{1+k^2}$，与 $\varphi$ 无关；大圆满足测地线方程。

**检验：** $k=0$ 时大圆退化成子午线（$\theta=$ 常数？不，$\cos\theta=0$ 即赤道），首次积分给 $1$，而 $\theta'=0$、$\sin\theta=1$ 时确实为 $1$ ✓。

**读法：** 球面测地线是大圆；把它写成 $\cot\theta=k\cos\varphi$ 后，$k$ 就是这条大圆平面与赤道面的"倾角"参数。

**9.28** 思路：被积函数含 $y''$，用高阶欧拉–拉格朗日方程；边界项给出 $y''=0$。

过程：$U=\dfrac12EI\int(y'')^2\mathrm{d}x-\int qy\,\mathrm{d}x$，故 $F=\dfrac{EI}{2}y''^2-qy$，

$$F_y=-q,\qquad F_{y'}=0,\qquad F_{y''}=EI\,y'' .$$

代入 $\dfrac{\partial F}{\partial y}-\dfrac{\mathrm{d}}{\mathrm{d}x}\dfrac{\partial F}{\partial y'}+\dfrac{\mathrm{d}^2}{\mathrm{d}x^2}\dfrac{\partial F}{\partial y''}=0$：

$$-q-0+\frac{\mathrm{d}^2}{\mathrm{d}x^2}\left(EI\,y''\right)=0\quad\Longrightarrow\quad EI\,y''''=q .$$

对 $y''$ 分部积分两次产生边界项 $\left[F_{y''}\delta y'\right]$：简支端 $y'$ 自由，故 $F_{y''}=EIy''=0$，即弯矩为零——这是**自然边界条件**。

**结果：** $EIy''''=q$；简支端 $y=0$、$y''=0$（前者本质、后者自然），固支端 $y=0$、$y'=0$（两者都是本质条件）。

**检验：** 量纲：$EI$（$\mathrm{N\cdot m^2}$）乘 $y''''$（$\mathrm{m^{-3}}$）给 $\mathrm{N/m}=q$ ✓。$q=0$ 时 $y''''=0$，解是三次多项式，正是无载梁的形状 ✓。

**读法：** 四阶方程需要四个边界条件，简支、固支、自由端各贡献两个——这就是结构力学里"边界条件要数够"的来历。

**9.29** 思路：用本征函数的正交归一性把瑞利商写成加权平均。

过程：设 $y=c_1y_1+c_2y_2$，本征函数满足 $\int wy_ny_m=\delta_{nm}$、$\int(py_n'y_m'+qy_ny_m)=\lambda_n\delta_{nm}$。代入分子分母：

$$\text{分子}=c_1^2\lambda_1+c_2^2\lambda_2+2c_1c_2\cdot0,\qquad
\text{分母}=c_1^2+c_2^2 .$$

于是

$$R=\frac{c_1^2\lambda_1+c_2^2\lambda_2}{c_1^2+c_2^2}
=\lambda_1+\frac{c_2^2\left(\lambda_2-\lambda_1\right)}{c_1^2+c_2^2}\ge\lambda_1 .$$

**结果：** $R\ge\lambda_1$；等号当且仅当 $c_2=0$（含 $c_1=0$ 的退化情形：$R=\lambda_2>\lambda_1$）。

**检验：** 若 $c_2/c_1$ 很小，$R-\lambda_1\approx(c_2/c_1)^2(\lambda_2-\lambda_1)$——误差是二阶小量，这解释了为什么粗略的试函数也能给出很好的基频估计。

**读法：** 瑞利商对污染"免疫"到二阶：形状差 10%，频率只差约 1%。

**9.30** 思路：极小性由二阶变分决定，而二阶变分的符号由共轭点控制。

过程：最速降线的共轭点在 $\varphi=\pi$（摆线的最低点）。用雅可比方程（二阶变分对应的线性方程）判断：解在 $\varphi=\pi$ 处首次出现零点，即共轭点。

- $\varphi_B<\pi$：$\delta^2J>0$，摆线是极小（例 9.1 的 $B=(1,1)$ 对应 $\varphi_B=2.41<3.14$ ✓）。
- $\varphi_B>\pi$：$\delta^2J$ 不再恒正，摆线只是驻点；9.11 的 $\varphi_B=3.51>\pi$，那里严格说只证明了"它是驻点"。

**结果：** $\varphi_B<\pi$ 时是极小；越过 $\varphi_B=\pi$ 极小性失效（共轭点之后）。

**检验：** 与二阶变分公式一致：$\delta^2J$ 的核在 $\varphi=\pi$ 处变号。物理上：终点太远时，"先冲到更低处再折回"可能更快。

**读法：** 极值问题的"局部"结论只在足够短的弧段上成立；全局最优要用强变分（魏尔斯特拉斯）方法判断。

**9.31** 对。$\delta J=0$ 只是一阶导数为零，和 $f'(x_0)=0$ 一样，可能是极小、极大或鞍点。

物理例子：一根链条挂在两钉之间是稳定平衡（势能极小）；把同一根链条的形状倒过来顶成拱形，同样满足平衡方程却是势能极大，碰一下就塌（不稳定的拱）。判断要靠二阶变分：极小时要求 $\delta^2J>0$ 对一切非零扰动成立。

**9.32** 因为边界项是 $\left[F_{y'}\delta y\right]$，端点自由时 $\delta y(b)\ne0$，要 $\delta J=0$ 只能 $F_{y'}(b)=0$。

$F_{y'}$ 一般不等于 $y'$：只有 $F$ 正比于 $y'^2$ 时两者才差一个正因子。例如长度的 $F=\sqrt{1+y'^2}$ 给 $F_{y'}=\dfrac{y'}{\sqrt{1+y'^2}}$，$F_{y'}=0$ 与 $y'=0$ **等价**（都在 $y'=0$ 处为零）；但悬链线的 $F_{y'}=\dfrac{(y-\mu)y'}{\sqrt{1+y'^2}}$ 在 $y=\mu$ 处也为零，所以那里 $F_{y'}=0$ 比 $y'=0$ 弱。两者一致的场合：$F$ 只依赖 $y'$ 且 $F_{y'}$ 只在 $y'=0$ 处为零。

**9.33** 没有。乘子会随"约束的写法"和"势能零点的选取"改变。

悬链线的例子：$\mu$ 出现在 $y-\mu$ 里，把 $y$ 的起算点平移一下 $\mu$ 就变，$G$ 的形状（$a$）不变。有意义的是由它导出的量：水平张力 $H=\rho ga$，它与零点无关。

所以看到乘子，先问"哪一个由它导出的量是不变的"，再赋予物理意义。

**9.34** 最可能：**试函数不满足本质边界条件**。上界定理的证明用到 $y(a)=y(b)=0$；试函数在端点不为零时，展开式里混进了不满足边界的分量，$R$ 可能低于 $\lambda_1$。

第二种可能：基函数选错（例如用奇函数逼近偶模态，$c_1=0$，$R$ 收敛到 $\lambda_2>\lambda_1$）。这种情况偏高，不会偏低，所以"偏低"几乎总是边界条件的问题。

**9.35** 因为 $F$ 对 $y'$ 线性时，$\partial F/\partial y'$ 不含 $y'$，于是 $\dfrac{\mathrm{d}}{\mathrm{d}x}F_{y'}$ 里没有 $y''$，方程降成关于 $x,y,y'$ 的代数关系（一阶或零阶）。

极值可能不存在：如 9.5 的 $\int y'^3$ 无下界；也可能只在下确界处取到而没有光滑极值曲线。判据是先算 $F_{y'y'}$，它恒为零就要警惕。

**9.36** 不更基本。最小作用量与牛顿力学**等价**：给定 $L$ 能推出运动方程，反过来也能从运动方程构造 $L$。

它的价值在工程性：换广义坐标时约束力自动消失；加约束只要降维；加场只要换 $L$（电磁场、相对论都一样）。此外它把"对称性"直接翻译成"守恒量"（诺特定理），这是牛顿形式不容易看出来的。

**9.37** 因为悬链面解存在的条件是 $R\ge1.509z_0$，即两环间距不超过约 $1.33R$。间距超过后方程无解，膜只能跳到另一个构型（两个平圆盘各挡住一个环）。

这暴露了变分法的局限：**它只保证"如果存在光滑驻点，则满足欧拉–拉格朗日方程"，不保证驻点存在**。极小曲面问题里解的个数和存在性会随参数突变，这属于"大范围变分"的内容。

**9.38** 因为问题本身对称：给定周长求最大面积，若 $C$ 是最优曲线，它的镜像（关于任意过定点的直线）也是最优曲线。

若最优解唯一，它必须与自己的镜像重合，所以可以只找对称解而不漏解。这个论证的前提是**唯一性**：等周问题里圆是唯一最优（相差平移/旋转），所以假设安全。若最优解不唯一（例如只要求"围住给定面积"的矩形，长宽互换都给同一面积），对称性论证只能保证"存在一个对称最优解"，不能排除别的解。

## 第 10 章

### 习题 10.1–10.10

**10.1**
**思路。** 判断张量只看一条：**变换律里是否只含一阶导数**。含二阶导数的就不是；另外可以用"零张量原理"检验——平直直角坐标里为零、极坐标里非零的，一定不是。

**过程（逐个）。**

**(a) $\partial_\mu v^\nu$：不是。** 换坐标后

$$\frac{\partial v'^\mu}{\partial x'^\lambda}
=\underbrace{\frac{\partial x'^\mu}{\partial x^\nu}\frac{\partial x^\rho}{\partial x'^\lambda}\frac{\partial v^\nu}{\partial x^\rho}}_{\text{张量该有的项}}
+\underbrace{\frac{\partial^2 x'^\mu}{\partial x^\rho\partial x^\nu}\frac{\partial x^\rho}{\partial x'^\lambda}v^\nu}_{\text{二阶导数}}.$$

第二项不满足任何张量变换律。

**(b) $\Gamma^\mu{}_{\nu\lambda}$：不是。** 它的变换律里也有一个 $\partial^2x'/\partial x^2$ 项（题 10.26）。而且直角坐标下 $\Gamma=0$、极坐标下 $\Gamma\ne0$。

**(c) $R^\rho{}_{\sigma\mu\nu}$：是。** 它由 $\Gamma$ 和 $\partial\Gamma$ 组合而成，二阶导数项恰好抵消（因为 $\partial_\mu\partial_\nu$ 对称而 $\mu\nu$ 反对称）。

**(d) $v^\mu\omega_\nu$：是。** 一个上指标、一个下指标，各带一个雅可比：

$$v'^\mu\omega'_\nu=\frac{\partial x'^\mu}{\partial x^\alpha}\frac{\partial x^\beta}{\partial x'^\nu}v^\alpha\omega_\beta .$$

**(e) $\Gamma\Gamma$（即 $\Gamma^\mu{}_{\nu\lambda}\Gamma^\lambda{}_{\rho\sigma}$）：不是。** 两个非张量的乘积仍是张量吗？一般不是：变换后会出现"一个张量项 + 两个二阶导数交叉项"的混合，消不掉。

**结果。**

| 对象 | 是否张量 | 依据 |
|---|---|---|
| $\partial_\mu v^\nu$ | 否 | 多出二阶导数项 |
| $\Gamma^\mu{}_{\nu\lambda}$ | 否 | 变换律含 $\partial^2x'$ |
| $R^\rho{}_{\sigma\mu\nu}$ | 是 | 二阶导数项相消 |
| $v^\mu\omega_\nu$ | 是 | 一上一下，各一雅可比 |
| $\Gamma\Gamma$ | 否 | 交叉项消不掉 |

**检验。** 数自由指标：$R^\rho{}_{\sigma\mu\nu}$ 有 4 个，$v^\mu\omega_\nu$ 有 2 个，与它们的"阶"一致 ✓。

**读法。** 判据的用处不只是"考试里判断"：写物理方程时必须知道哪些量是张量，否则方程只在某类坐标系里成立。**看见"三个指标"就当成张量，是初学者最常见的翻车方式。**

**10.2**
**思路。** 升降指标就是乘度规；球面的 $g_{\theta\theta}=1$（$a=1$）、$g_{\varphi\varphi}=\sin^2\theta$，逐个乘。

**过程。** 用 $v_\mu=g_{\mu\nu}v^\nu$：

$$v_\theta=g_{\theta\theta}v^\theta=1\cdot1=1,
\qquad
v_\varphi=g_{\varphi\varphi}v^\varphi=\sin^2\theta\cdot2=2\sin^2\theta .$$

两个不变量：

$$g_{\mu\nu}v^\mu v^\nu=1\cdot1^2+\sin^2\theta\cdot2^2=1+4\sin^2\theta .$$

反过来，$v^\mu=g^{\mu\nu}v_\nu$，$g^{11}=1$、$g^{22}=1/\sin^2\theta$：

$$g^{\mu\nu}v_\mu v_\nu=1\cdot1^2+\frac{1}{\sin^2\theta}\left(2\sin^2\theta\right)^2
=1+\frac{4\sin^4\theta}{\sin^2\theta}=1+4\sin^2\theta .$$

**结果。**

$$v_\theta=1,\qquad v_\varphi=2\sin^2\theta,\qquad
g_{\mu\nu}v^\mu v^\nu=g^{\mu\nu}v_\mu v_\nu=1+4\sin^2\theta .$$

**检验。** 两个不变量相等，正是"升降指标不改变矢量"的具体验证；也可直接算 $v^\mu v_\mu=1\cdot1+2\cdot2\sin^2\theta$ ✓（缩并 $v^\mu v_\mu$ 与 $g_{\mu\nu}v^\mu v^\nu$ 是同一个数）。

**读法。** 上下指标是同一个物理量的两种写法：**$v^\varphi=2$ 说的是"经度方向每秒走 2 弧度"，$v_\varphi=2\sin^2\theta$ 说的是"它的对偶分量"**。在极点（$\sin\theta=0$）处 $v_\varphi\to0$——因为那里经度方向没有长度。

**10.3**
**思路。** $\Gamma$ 的公式里全是度规的导数；圆柱面的度规分量是常数，所以 $\Gamma$ 全为零，曲率自然为零。

**过程。** 圆柱面 $(x^1,x^2)=(\varphi,z)$，$g_{11}=a^2$、$g_{22}=1$、$g_{12}=0$。**两个分量都与坐标无关**：

$$\frac{\partial g_{\mu\nu}}{\partial x^\lambda}=0\qquad\text{对一切 }\mu,\nu,\lambda .$$

代公式

$$\Gamma^\mu{}_{\nu\lambda}=\frac12g^{\mu\rho}
\left(\frac{\partial g_{\rho\lambda}}{\partial x^\nu}
+\frac{\partial g_{\nu\rho}}{\partial x^\lambda}
-\frac{\partial g_{\nu\lambda}}{\partial x^\rho}\right),$$

括号里三个导数全为零，所以 $\Gamma^\mu{}_{\nu\lambda}\equiv0$。

曲率是 $\Gamma$ 与 $\partial\Gamma$ 的组合：

$$R^\rho{}_{\sigma\mu\nu}
=\frac{\partial\Gamma^\rho{}_{\nu\sigma}}{\partial x^\mu}-\cdots+\Gamma\Gamma-\Gamma\Gamma\equiv0 .$$

**结果。**

$$\Gamma^\mu{}_{\nu\lambda}=0\ \ (\text{全部 8 个分量}),\qquad R^\rho{}_{\sigma\mu\nu}=0 .$$

**检验。** 圆柱面可展（剪开能铺平），内禀曲率必为零 ✓。若把坐标换成"沿圆周的弧长" $s=a\varphi$，度规就是 $\mathrm{d}s^2+\mathrm{d}z^2$，与平面直角坐标完全一样——所以 $\Gamma=0$ 是"坐标选得好"的结果。

**读法。** **$\Gamma=0$ 不代表"坐标不弯"，只代表"这套坐标下度规是常数"**。圆柱面的坐标明显是弯的（$\varphi$ 走一圈回到原处），但空间本身是平的。

**10.4**
**思路。** 每个 $\Gamma$ 都是"三个度规导数"的组合；只要这三个导数里有任何一个为零或相消，$\Gamma$ 就为零。逐个看用到了哪些导数。

**过程。**

**$\Gamma^\theta{}_{\theta\theta}$：** 公式给 $\frac12g^{\theta\theta}\left(\partial_\theta g_{\theta\theta}+\partial_\theta g_{\theta\theta}-\partial_\theta g_{\theta\theta}\right)=\frac12g^{\theta\theta}\partial_\theta g_{\theta\theta}$。而 $g_{\theta\theta}=a^2$ 是**常数**，$\partial_\theta g_{\theta\theta}=0$，故 $\Gamma^\theta{}_{\theta\theta}=0$。

**$\Gamma^\theta{}_{\theta\varphi}$：** 需要 $\partial_\theta g_{\varphi\theta}$、$\partial_\varphi g_{\theta\theta}$、$\partial_\varphi g_{\theta\theta}$ 三类。$g_{\theta\varphi}=0$（对角），$g_{\theta\theta}=a^2$ 与 $\varphi$ 无关，故三项皆零：

$$\Gamma^\theta{}_{\theta\varphi}=\frac12g^{\theta\theta}\left(\partial_\theta g_{\varphi\theta}+\partial_\varphi g_{\theta\varphi}-\partial_\varphi g_{\theta\theta}\right)=0 .$$

**$\Gamma^\varphi{}_{\varphi\varphi}$：** 需要 $\partial_\varphi g_{\varphi\varphi}$（两次）与 $\partial_\varphi g_{\varphi\varphi}$。球面度规**不显含 $\varphi$**，$\partial_\varphi g_{\varphi\varphi}=0$，故

$$\Gamma^\varphi{}_{\varphi\varphi}=\frac12g^{\varphi\varphi}\left(2\partial_\varphi g_{\varphi\varphi}-\partial_\varphi g_{\varphi\varphi}\right)=0 .$$

**结果。**

$$\Gamma^\theta{}_{\theta\theta}=\Gamma^\theta{}_{\theta\varphi}=\Gamma^\varphi{}_{\varphi\varphi}=0 .$$

**检验。** 与 10.4.4 的完整答案对照：球面只有三个非零分量（$\Gamma^\theta{}_{\varphi\varphi}$、$\Gamma^\varphi{}_{\theta\varphi}$、$\Gamma^\varphi{}_{\varphi\theta}$），其余为零 ✓。数一数：$2^3=8$ 个分量，非零 3 个。

**读法。** 度规的对称性（与 $
arphi$ 无关、$	heta	heta$ 分量为常数）决定了联络的稀疏：8 个分量里只有 3 个非零。**先看度规的对称性，再决定算哪几个 $\Gamma$**，能省一大半功夫。

**10.5**
**思路。** 二维一般度规 $\mathrm{diag}(1,f)$：先写逆度规，再用公式；非零的 $\Gamma$ 只可能来自 $\partial_1 g_{22}=f'$ 这一项。

**过程。** 逆度规：$g^{11}=1$，$g^{22}=\dfrac{1}{f}$。

**唯一的非零导数：** $\dfrac{\partial g_{22}}{\partial x^1}=f'$。

**$\Gamma^1{}_{22}$：** 取 $\mu=1$、$\nu=\lambda=2$：

$$\Gamma^1{}_{22}=\frac12g^{11}\left(\partial_2 g_{12}+\partial_2 g_{21}-\partial_1 g_{22}\right)
=\frac12\cdot1\cdot\left(0+0-f'\right)=-\frac{f'}{2}.$$

**$\Gamma^2{}_{12}$：** 取 $\mu=2$、$\nu=1$、$\lambda=2$：

$$\Gamma^2{}_{12}=\frac12g^{22}\left(\partial_1 g_{22}+\partial_2 g_{12}-\partial_2 g_{12}\right)
=\frac12\cdot\frac1f\cdot f'=\frac{f'}{2f}.$$

由对称性 $\Gamma^2{}_{21}=\Gamma^2{}_{12}$。其余含 $\partial_1g_{11}=0$ 或 $\partial_2(\cdot)=0$，全为零。

**结果。**

$$g^{11}=1,\quad g^{22}=\frac1f;\qquad
\Gamma^1{}_{22}=-\frac{f'}{2},\quad
\Gamma^2{}_{12}=\Gamma^2{}_{21}=\frac{f'}{2f}.$$

**检验。** 取 $f(r)=r^2$（平面极坐标，$x^1=r,x^2=\varphi$）：$\Gamma^1{}_{22}=-r$、$\Gamma^2{}_{12}=1/r$ ✓，与 10.4.6 完全一致。取 $f=a^2\sin^2\theta$（球面）：$\Gamma^1{}_{22}=-\sin\theta\cos\theta$、$\Gamma^2{}_{12}=\cot\theta$ ✓。

**读法。** 二维只有两个独立分量——这解释了为什么二维的曲率只有一个数 $K$。**维数越低，联络能携带的信息越少。**

**10.6**
**思路。** $R^\rho{}_{\sigma\mu\nu}$ 有四项：两个导数和两个 $\Gamma\Gamma$ 乘积。$\Gamma$ 只有三个非零，所以先列出它们，再逐项对齐指标。

**过程。** 先用到的三个 $\Gamma$（10.4.4）：

$$\Gamma^\theta{}_{\varphi\varphi}=-\sin\theta\cos\theta,\qquad
\Gamma^\varphi{}_{\theta\varphi}=\Gamma^\varphi{}_{\varphi\theta}=\cot\theta .$$

取 $\mu=\theta$、$\nu=\varphi$、$\rho=\varphi$、$\sigma=\theta$：

$$R^\varphi{}_{\theta\varphi\theta}
=\partial_\varphi\Gamma^\varphi{}_{\theta\theta}
-\partial_\theta\Gamma^\varphi{}_{\varphi\theta}
+\Gamma^\varphi{}_{\varphi\lambda}\Gamma^\lambda{}_{\theta\theta}
-\Gamma^\varphi{}_{\theta\lambda}\Gamma^\lambda{}_{\varphi\theta}.$$

**逐项：**

1. $\Gamma^\varphi{}_{\theta\theta}=0$，导数 $0$。
2. $-\dfrac{\partial}{\partial\theta}\cot\theta=+\dfrac{1}{\sin^2\theta}$。
3. $\Gamma^\varphi{}_{\varphi\lambda}\Gamma^\lambda{}_{\theta\theta}$：$\lambda=\theta$ 给 $\cot\theta\cdot0=0$；$\lambda=\varphi$ 给 $\Gamma^\varphi{}_{\varphi\varphi}\cdot0=0$。整项为零。
4. $-\Gamma^\varphi{}_{\theta\lambda}\Gamma^\lambda{}_{\varphi\theta}$：$\lambda=\theta$ 给 $\Gamma^\varphi{}_{\theta\theta}\Gamma^\theta{}_{\varphi\theta}=0$；$\lambda=\varphi$ 给 $\Gamma^\varphi{}_{\theta\varphi}\Gamma^\varphi{}_{\varphi\theta}=\cot^2\theta$。所以这项是 $-\cot^2\theta$。

四项相加：

$$R^\varphi{}_{\theta\varphi\theta}=\frac{1}{\sin^2\theta}-0+0-\cot^2\theta
=\frac{1-\cos^2\theta}{\sin^2\theta}=1 .$$

**结果。**

$$R^\varphi{}_{\theta\varphi\theta}=1 .$$

**检验。** 与里奇张量一致：$R_{\theta\theta}=R^\lambda{}_{\theta\lambda\theta}=R^\varphi{}_{\theta\varphi\theta}=1$ ✓（另两项为零）。而 $R_{\theta\theta}=1$ 又给出 $R=2/a^2$ ✓——三者自洽。

**读法。** 结果是**常数 1**，与 $\theta$ 无关——正是"球面均匀"的体现。四个极点指标里只有这个分量非零（其余由对称性给出），二维曲率只有一个独立分量。

**10.7**
**思路。** 不用算 $R$：$\Gamma\equiv0$ 时 $R$ 的每一项（$\partial\Gamma$ 与 $\Gamma\Gamma$）都为零，于是里奇为零、标量为零。

**过程。** 题 10.3 已得圆柱面 $\Gamma^\mu{}_{\nu\lambda}\equiv0$。看 $R$ 的四项：

$$R^\rho{}_{\sigma\mu\nu}
=\underbrace{\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\nu\Gamma^\rho{}_{\mu\sigma}}_{0-0}
+\underbrace{\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}
-\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}}_{0-0}=0 .$$

里奇是它的缩并：

$$R_{\mu\nu}=R^\lambda{}_{\mu\lambda\nu}=0,$$

标量再缩并一次：

$$R=g^{\mu\nu}R_{\mu\nu}=0 .$$

**结果。**

$$R_{\mu\nu}=0,\qquad R=0 .$$

**检验。** 也可从"可展性"直接论证：圆柱面剪开能铺平成平面，而平面 $R=0$，曲率是内禀量，铺平前后不变 ✓。

**读法。** 这道题的意义是**否证**："有坐标弯曲"（$\varphi$ 是周期坐标）不等于"空间弯曲"。**判据只有 $R$**。

**10.8**
**思路。** 标量曲率是 $g^{\mu\nu}R_{\mu\nu}$；球面的两个里奇分量已知，逆度规也已知，代进去即可。

**过程。** 由 10.6.3：

$$R_{\theta\theta}=1,\qquad R_{\varphi\varphi}=\sin^2\theta,\qquad R_{\theta\varphi}=0 .$$

逆度规：

$$g^{\theta\theta}=\frac{1}{a^2},\qquad g^{\varphi\varphi}=\frac{1}{a^2\sin^2\theta}.$$

缩并（只有对角项）：

$$R=g^{\theta\theta}R_{\theta\theta}+g^{\varphi\varphi}R_{\varphi\varphi}
=\frac{1}{a^2}\cdot1+\frac{1}{a^2\sin^2\theta}\cdot\sin^2\theta
=\frac{1}{a^2}+\frac{1}{a^2}.$$

**结果。**

$$R=\frac{2}{a^2}.$$

**检验。** 二维恒有 $R=2K$，故 $K=1/a^2$ ✓，与例 10.4 用周长测出的曲率一致。$a\to\infty$（球面变平）时 $R\to0$ ✓。

**读法。** 结果**与 $\theta$ 无关**不是巧合：$R_{\theta\theta}$ 与 $R_{\varphi\varphi}$ 里的 $\theta$ 依赖，恰好被 $g^{\varphi\varphi}$ 里的 $1/\sin^2\theta$ 抵消。**球面每一点的地位相同，标量曲率必须处处相等**——这是对称性对结果的约束。

**10.9**
**思路。** 二维恒等式 $R_{\mu\nu}=\frac R2 g_{\mu\nu}$ 只有两个独立分量要验；把 10.6.3 的结果与 $R=2/a^2$ 代进去即可。

**过程。** 已知 $R=\dfrac{2}{a^2}$，所以 $\dfrac R2=\dfrac{1}{a^2}$。

**$\theta\theta$ 分量：**

$$R_{\theta\theta}=1,\qquad
\frac{R}{2}g_{\theta\theta}=\frac{1}{a^2}\cdot a^2=1 .$$

**$\varphi\varphi$ 分量：**

$$R_{\varphi\varphi}=\sin^2\theta,\qquad
\frac{R}{2}g_{\varphi\varphi}=\frac{1}{a^2}\cdot a^2\sin^2\theta=\sin^2\theta .$$

两式都成立；非对角分量为零，也成立。

**结果。**

$$R_{\mu\nu}=\frac{R}{2}g_{\mu\nu}\qquad(\text{球面上验证通过}).$$

**检验。** 取迹：$g^{\mu\nu}R_{\mu\nu}=\frac R2 g^{\mu\nu}g_{\mu\nu}=\frac R2\cdot2=R$ ✓，自洽。

**读法。** 二维的里奇张量**不携带任何超出 $R$ 的信息**——它是 $g_{\mu\nu}$ 的倍数。三维也是（6 个分量对 6 个），所以三维没有引力波。到四维（20 对 10）才有"剩余"的自由度。

**10.10**
**思路。** 把球面的 $\Gamma$ 代进测地线方程的 $\theta$ 分量，然后检查赤道 $\theta=\pi/2$ 是否满足。

**过程。** 测地线方程

$$\frac{\mathrm{d}^2x^\mu}{\mathrm{d}\lambda^2}
+\Gamma^\mu{}_{\nu\sigma}\frac{\mathrm{d}x^\nu}{\mathrm{d}\lambda}\frac{\mathrm{d}x^\sigma}{\mathrm{d}\lambda}=0 .$$

$\mu=\theta$ 时，只有 $\Gamma^\theta{}_{\varphi\varphi}=-\sin\theta\cos\theta$ 非零（其余 $\Gamma^\theta{}_{\cdot\cdot}=0$），所以求和只剩 $(\nu,\sigma)=(\varphi,\varphi)$ 一项：

$$\theta''-\sin\theta\cos\theta\,\varphi'^2=0 .$$

（撇表示对 $\lambda$ 求导。）

**验证赤道：** 取 $\theta=\pi/2$，则 $\theta'=0$、$\theta''=0$，且 $\cos(\pi/2)=0$：

$$\theta''-\sin\theta\cos\theta\,\varphi'^2
=0-\left(1\cdot0\right)\varphi'^2=0 .$$

满足 ✓。

**结果。**

$$\theta''-\sin\theta\cos\theta\,\varphi'^2=0,
\qquad \theta=\frac{\pi}{2}\ \text{是解}.$$

**检验。** $\theta=\pi/2$ 时另一分量给 $\varphi''+2\cot(\pi/2)\theta'\varphi'=\varphi''=0$，即 $\varphi=\omega\lambda$ ✓ 匀速——赤道是测地线，运动是匀速圆周。

**读法。** $\sin\theta\cos\theta$ 在 $\theta=\pi/2$ 处为零，正是"赤道处纬度圈的切线方向不产生 $\theta$ 方向加速度"的数学表现。**极点（$\theta=0$）处这个系数也为零，但那里的坐标本身退化，不能当测地线处理。**

### 习题 10.11–10.22

**10.11**
**思路。** 长方体的惯量张量在主轴上是对角的，三个主值用 $I=m(\text{另两边的平方和})/12$；任意方向的转动惯量是二次型 $\boldsymbol{n}^{\mathsf T}I\boldsymbol{n}$。

**过程。** $m=20\,\mathrm{kg}$，$a=0.3$、$b=0.2$、$c=0.1\,\mathrm{m}$。

三个主值：

$$I_{xx}=\frac{m(b^2+c^2)}{12}=\frac{20(0.04+0.01)}{12}=0.0833,$$
$$I_{yy}=\frac{m(a^2+c^2)}{12}=\frac{20(0.09+0.01)}{12}=0.1667,$$
$$I_{zz}=\frac{m(a^2+b^2)}{12}=\frac{20(0.09+0.04)}{12}=0.2167 .$$

体对角线方向的单位矢量：

$$\boldsymbol{n}=\frac{(a,b,c)}{\sqrt{a^2+b^2+c^2}}=\frac{(0.3,0.2,0.1)}{0.3742}=(0.802,\,0.535,\,0.267).$$

二次型：

$$I_{\boldsymbol n}=\sum_i I_{ii}n_i^2=0.0833(0.643)+0.1667(0.286)+0.2167(0.0714).$$

逐项：$0.0536+0.0477+0.0155=0.1168$。

**结果。**

$$I_{xx}=0.083,\quad I_{yy}=0.167,\quad I_{zz}=0.217\ \mathrm{kg\cdot m^2},
\qquad I_{\boldsymbol n}=0.117\ \mathrm{kg\cdot m^2}.$$

**检验。** 迹：$0.0833+0.1667+0.2167=0.4667$，与 $\frac{2m(a^2+b^2+c^2)}{12}=\frac{2\times20\times0.14}{12}=0.4667$ ✓。$I_{\boldsymbol n}$ 介于最小主值 $0.0833$ 与最大主值 $0.2167$ 之间 ✓（瑞利商性质）。

**读法。** 任意方向的转动惯量被三个主轴值夹住，具体值由方向余弦加权。**"九个数字"里只有三个是砖的固有属性**，其余是坐标的产物——题 10.1 的变换律说的就是这件事。

**10.12**
**思路。** 同一根加速度矢量在两套坐标下的分量不同，但模长不变；把两套基矢量写出来做投影即可。

**过程。** 竖直向下为 $-y$。**水平/竖直坐标** $(\hat{\boldsymbol{e}}_x,\hat{\boldsymbol{e}}_y)$：

$$\boldsymbol a=(0,-g)=(0,-9.8).$$

**沿斜面/垂直斜面坐标**：设 $x'$ 沿斜面向下、$y'$ 垂直斜面向上，斜面对水平面倾角 $\theta=30^\circ$。投影：

$$a_{x'}=\boldsymbol a\cdot\hat{\boldsymbol{e}}_{x'}=g\sin\theta=9.8\times0.5=4.9,$$
$$a_{y'}=\boldsymbol a\cdot\hat{\boldsymbol{e}}_{y'}=g\sin\theta\sin\theta-g\cos\theta\cdot\cos\theta\ldots$$

更直接：重力沿斜面的分量 $g\sin\theta$、垂直斜面的分量 $g\cos\theta$，所以

$$a_{y'}=-g\cos\theta=-9.8\times0.866=-8.49\ \mathrm{m/s^2}.$$

**结果。**

$$(a_x,a_y)=(0,-9.8),\qquad (a_{x'},a_{y'})=(4.9,\,-8.49)\ \mathrm{m/s^2}.$$

**检验。** 模长：

$$\sqrt{0^2+9.8^2}=9.8,\qquad
\sqrt{4.9^2+8.49^2}=\sqrt{24.01+72.08}=\sqrt{96.09}=9.80 .$$

两者相等 ✓。再用 $\sin^2+\cos^2=1$ 验证：$g^2(\sin^2\theta+\cos^2\theta)=g^2$ 恒成立。

**读法。** 分量是投影，矢量才是对象。**"加速度变了"是错觉，"加速度的表示变了"才对**——这正是张量语言要救的东西。真正会随坐标系变的是"分量对坐标求导"那件事（见 10.1.1）。

**10.13**
**思路。** 圆环是一维流形，只有一个坐标 $\varphi$；度规是常数，所以联络为零，测地线方程退化成"$\varphi$ 匀速"。

**过程。** 圆环半径 $a$，坐标 $\varphi\in[0,2\pi)$，线元

$$\mathrm{d}s^2=a^2\mathrm{d}\varphi^2\qquad\Longrightarrow\qquad g_{11}=a^2 .$$

**联络：** $g_{11}$ 是常数，$\partial_\varphi g_{11}=0$，所以

$$\Gamma^1{}_{11}=\frac12g^{11}\left(\partial_1 g_{11}+\partial_1 g_{11}-\partial_1 g_{11}\right)=0 .$$

**测地线方程：**

$$\frac{\mathrm{d}^2\varphi}{\mathrm{d}\lambda^2}+\Gamma^1{}_{11}\left(\frac{\mathrm{d}\varphi}{\mathrm{d}\lambda}\right)^2=0
\quad\Longrightarrow\quad
\frac{\mathrm{d}^2\varphi}{\mathrm{d}\lambda^2}=0 .$$

积分两次：

$$\varphi(\lambda)=\omega\lambda+\varphi_0 .$$

**结果。**

$$\varphi(\lambda)=\omega\lambda+\varphi_0,\qquad
\text{速率 } a|\omega|\ \text{恒定}.$$

**检验。** 由度规相容性，$|u|^2=g_{11}\dot\varphi^2=a^2\omega^2$ 是常数 ✓，与"没有力，速率不变"一致。

**读法。** 一维流形上"每条曲线都是测地线"——因为没有第二个方向可以转弯。**曲率必然为零**，这也解释了为什么一维世界没有引力（没有潮汐力可言）。

**10.14**
**思路。** 两点同纬度：沿纬线走是小圆弧长，沿大圆走要先用球面余弦定理求圆心角，然后比较。

**过程。** 两点余纬 $\theta_0$（从北极量起），经度差 $\Delta\varphi$。

**沿纬线：** 纬线是小圆，半径 $a\sin\theta_0$，弧长

$$s_{\text{纬}}=a\sin\theta_0\,\Delta\varphi .$$

**沿大圆：** 球面余弦定理（单位球上）

$$\cos\frac{d}{a}=\cos\theta_1\cos\theta_2+\sin\theta_1\sin\theta_2\cos\Delta\varphi
=\cos^2\theta_0+\sin^2\theta_0\cos\Delta\varphi,$$

所以 $s_{\text{大圆}}=a\arccos\!\left(\cos^2\theta_0+\sin^2\theta_0\cos\Delta\varphi\right)$。

**小 $\Delta\varphi$ 的展开：** $\cos\Delta\varphi\approx1-\frac{(\Delta\varphi)^2}{2}$，代进去

$$\cos\frac da\approx1-\sin^2\theta_0\frac{(\Delta\varphi)^2}{2}
\quad\Longrightarrow\quad
\frac da\approx\sin\theta_0\,\Delta\varphi .$$

**结果。**

$$s_{\text{纬}}=a\sin\theta_0\,\Delta\varphi,\qquad
s_{\text{大圆}}=a\arccos\!\left(\cos^2\theta_0+\sin^2\theta_0\cos\Delta\varphi\right).$$

大圆总是更短（或相等）；相等只在 $\Delta\varphi=0$、$\theta_0=\pi/2$（赤道）或 $\theta_0=0$（极点）时发生。

**检验。** $\theta_0=\pi/2$（赤道）：$\cos^2=0$、$\sin^2=1$，$\cos(d/a)=\cos\Delta\varphi$，给 $d=a\Delta\varphi$ = 纬线弧长 ✓（赤道本身就是大圆）。$\Delta\varphi\to0$：两式同阶 ✓（局部看不出差别）。

**读法。** 这就是飞机走大圆的原因：**纬线不是测地线（除赤道），走它要多走**。差值随纬度和经度差增大而增大——从北京到纽约，大圆航线比"沿北纬 40° 走"近约 10%。

**10.15**
**思路。** 赤道到北极沿经线（大圆）走，圆心角 $\pi/2$；赤道本身的周长是 $2\pi a$。算比值，再与平面圆对比。

**过程。** **赤道到北极：** 经线是大圆，圆心角从 $0$ 到 $\pi/2$：

$$s=a\cdot\frac{\pi}{2}=1.571a .$$

**赤道周长：** 赤道是大圆，半径 $a$：

$$C=2\pi a=6.283a .$$

**比值：**

$$\frac{s}{C}=\frac{\pi a/2}{2\pi a}=\frac14 .$$

**结果。**

$$\frac{\text{极距}}{\text{赤道周长}}=\frac14 .$$

**检验。** 平面上从圆心到边界是 $R$、周长 $2\pi R$，比值 $1/(2\pi)\approx0.159$。球面是 $0.25$，**明显不同** ✓——差别来自"球面上圆的周长比同半径的平面圆短"。

**读法。** 这个比值可以当"曲率计"：$1/4$ 是 $K=1/a^2>0$ 的标志。若是双曲面（$K<0$），比值会小于 $1/(2\pi)$。**量一个纯数就能判断空间的正负弯曲**，这正是高斯–博内的精神。

**10.16**
**思路。** 平行移动一圈的转角只依赖围出的面积，公式是 $\Delta\alpha=K\times A=2\pi(1-\cos\theta_0)$，与半径无关。

**过程。** 纬度 $45^\circ$ 对应余纬 $\theta_0=45^\circ$。纬线围出的是球冠，面积

$$A=2\pi a^2(1-\cos\theta_0).$$

乘 $K=1/a^2$：

$$\Delta\alpha=\frac{A}{a^2}=2\pi(1-\cos45^\circ)
=2\pi\left(1-\frac{\sqrt2}{2}\right)=2\pi\times0.2929=1.840\ \mathrm{rad}.$$

换成度：$1.840\times\dfrac{180}{\pi}=105.4^\circ$。

**结果。**

$$\Delta\alpha=1.840\ \mathrm{rad}=105.4^\circ .$$

**检验。** 三个极限：$\theta_0\to0$（贴北极）给 $\sim2\pi\cdot\theta_0^2/2\to0$ ✓（局部平坦）；$\theta_0=\pi/2$（赤道）给 $2\pi$ ✓（围住半球，面积 $2\pi a^2$，$K\cdot A=2\pi$）；$\theta_0\to\pi$ 给 $4\pi$（等价于零）✓。

**读法。** 转角与 $a$ 无关——**这是纯球面几何的性质，换多大的球都一样**。半径只影响"面积与转角的比例系数" $K=1/a^2$。所以在地球上做两个小时的搬运实验（比如陀螺仪绕圈），就能测出 $105^\circ$ 这个可观的角。

**10.17**
**思路。** 双曲面上角亏 $=|K|\times$ 面积，与球面的角盈公式同构，只是符号相反。

**过程。** 给定 $K=-1/a^2$，$a=1\,\mathrm{m}$，所以 $|K|=1\,\mathrm{m^{-2}}$。角亏

$$\delta=0.01\ \mathrm{rad}=|K|\cdot A=\frac{A}{a^2}.$$

解出面积：

$$A=\delta\,a^2=0.01\times1=0.01\ \mathrm{m^2}.$$

**结果。**

$$A=0.01\ \mathrm{m^2},\qquad K=-\frac{1}{a^2}=-1\ \mathrm{m^{-2}} .$$

**检验。** 量纲：$[K]=1/\text{长度}^2$，$[A]=\text{长度}^2$，$K A$ 无量纲 ✓。与球面情形对比：球面上同样面积的三角形角盈是 $+0.01$。

**读法。** **正曲率给角盈、负曲率给角亏**。这是"用三角形内角和测曲率"的核心：测三个角，加起来与 $\pi$ 比，多则正、少则负。高斯当年架仪器测三个山头，就是想做这件事（当然测不出，因为地球太大）。

**10.18**
**思路。** 反证：若存在保距的平面地图，则球面上的测地三角形必须映成平面直线三角形，而两者内角和不同——矛盾。

**过程。** 假设存在保距映射 $\Phi:$ 球面 $\to$ 平面，即 $d_{\text{平面}}(\Phi(P),\Phi(Q))=d_{\text{球}}(P,Q)$。

取球面上一个测地三角形（三条边都是大圆），内角和

$$A+B+C=\pi+\frac{A_{\text{球}}}{a^2}>\pi .$$

**保距的后果：** 测地线必须映成测地线（因为"最短"这个性质被保住），所以三条边映成平面上的三条**直线段**，像是一个平面三角形，其内角和

$$A'+B'+C'=\pi .$$

但保距映射保持角度（距离决定角度），所以 $A'=A$ 等，于是两边都等于 $\pi+\frac{A}{a^2}$ 和 $\pi$，矛盾。

**结果。**

$$\text{不存在保距的平面地图};\qquad A+B+C=\pi+\frac{A}{a^2}\ne\pi .$$

**检验。** 换个说法：球面的高斯曲率 $K=1/a^2\ne0$，而平面 $K=0$；$K$ 是内禀量，保距映射不能改变它 ✓。

**读法。** 这不是"画得不够好"，是**不允许**。所有地图都在某处失真：等角投影（墨卡托）保角不保面积，等面积投影反过来。**曲率不允许你同时保住三者**。圆柱和圆锥 $K=0$（可展），所以能剪开铺平。

**10.19**
**思路。** 圆锥面的度规与平面极坐标只差一个角度缩放 $\sin\alpha$，所以联络的形式照抄，曲率仍为零。

**过程。** 半顶角 $\alpha$，$\rho$ 是顶点量起的斜距，$\varphi$ 是绕轴角。把圆锥展开成扇形，扇形的半径是 $\rho$、弧长是 $\rho\sin\alpha\,\mathrm{d}\varphi$，所以

$$\mathrm{d}s^2=\mathrm{d}\rho^2+\rho^2\sin^2\alpha\,\mathrm{d}\varphi^2 .$$

令 $\vartheta=\varphi\sin\alpha$（一个常数的角度缩放），度规化成 $\mathrm{d}\rho^2+\rho^2\mathrm{d}\vartheta^2$，就是平面极坐标。所以（对照 10.4.6）

$$\Gamma^\rho{}_{\varphi\varphi}=-\rho\sin^2\alpha,\qquad
\Gamma^\varphi{}_{\rho\varphi}=\Gamma^\varphi{}_{\varphi\rho}=\frac1\rho .$$

**曲率：** 结构同 10.6.4，$\partial_\rho\Gamma^\rho{}_{\varphi\varphi}=-\sin^2\alpha$，第四项给 $\Gamma^\rho{}_{\varphi\varphi}\Gamma^\varphi{}_{\rho\varphi}=-\sin^2\alpha$，带负号出来是 $+\sin^2\alpha$，两项相消：

$$R^\rho{}_{\varphi\varphi\rho}=-\sin^2\alpha+0+0+\sin^2\alpha=0 .$$

**结果。**

$$\Gamma^\rho{}_{\varphi\varphi}=-\rho\sin^2\alpha,\quad
\Gamma^\varphi{}_{\rho\varphi}=\frac1\rho,\quad
R\equiv0 .$$

测地线在展开的扇形里是**直线段**（跨过剪缝时按同一角度接上）。

**检验。** $\alpha=\pi/2$ 时 $\sin\alpha=1$，退回平面极坐标 ✓。$R\equiv0$ 与"可展"一致 ✓。

**读法。** 圆锥的"弯"全是坐标造成的（$\varphi$ 的周期不是 $2\pi$ 而是 $2\pi\sin\alpha$），内禀曲率为零。**这也解释了为什么圆锥上平行移动不产生任何转角**。

**10.20**
**思路。** 圆柱面 $\Gamma\equiv0$（题 10.3），平行移动方程退化成"分量为常数"，所以转角为零。

**过程。** 圆柱面 $\mathrm{d}s^2=a^2\mathrm{d}\varphi^2+\mathrm{d}z^2$，全部 $\Gamma=0$。平行移动方程

$$\frac{Dv^\mu}{D\lambda}=\frac{\mathrm{d}v^\mu}{\mathrm{d}\lambda}
+\Gamma^\mu{}_{\nu\sigma}v^\nu\frac{\mathrm{d}x^\sigma}{\mathrm{d}\lambda}=0$$

第二项为零，剩下

$$\frac{\mathrm{d}v^\mu}{\mathrm{d}\lambda}=0\quad\Longrightarrow\quad v^\mu=\text{const}.$$

沿纬线（$\varphi:0\to2\pi$、$z$ 不变）走一圈，分量不变，所以矢量回到原处时**与出发时完全相同**：

$$\Delta\alpha=0 .$$

**结果。**

$$\Delta\alpha=0\qquad(\text{圆柱面上任意闭合回路}).$$

**检验。** 与球面对比：球面 $45^\circ$ 纬线给 $105.4^\circ$（题 10.16）。差别不在"坐标弯不弯"（两者都弯），而在 $K$：圆柱 $K=0$、球面 $K=1/a^2$ ✓。

**读法。** **"绕一圈回来方向不变" 是平坦的等价条件**。原因是 $\Delta\alpha=K\times$面积：面积可以任意小，所以 $K$ 必须为零；反过来 $K=0$ 时和乐恒为零。**这比"看起来直不直"可靠得多**——圆柱的坐标看起来比平面弯得多，但它就是平的。

**10.21**
**思路。** 无外力 ⟹ 走测地线；球面的测地线方程已算出，再加一个"速率守恒"的第一积分，就能说明运动是匀速的、赤道是特解。

**过程。** 约束在球面上的自由粒子，作用量就是弧长，所以满足测地线方程：

$$\theta''-\sin\theta\cos\theta\,\varphi'^2=0,
\qquad
\varphi''+2\cot\theta\,\theta'\varphi'=0 .$$

**匀速性：** 度规相容给 $|u|^2=g_{\mu\nu}u^\mu u^\nu$ 是常数：

$$a^2\left(\theta'^2+\sin^2\theta\,\varphi'^2\right)=\text{const}
\quad\Longrightarrow\quad
\theta'^2+\sin^2\theta\,\varphi'^2=\text{const}.$$

右边是常数，说明"速率" $|\boldsymbol u|=\sqrt{\text{const}}$ 不变——**没有力，所以速率不变，只有方向在变**。

**赤道特解：** 取 $\theta=\pi/2$，$\theta'=\theta''=0$、$\cos(\pi/2)=0$，第一式给 $0=0$ ✓；第二式给 $\varphi''=0$，即 $\varphi=\omega\lambda$。

**结果。**

$$\theta''-\sin\theta\cos\theta\,\varphi'^2=0,\quad
\varphi''+2\cot\theta\,\theta'\varphi'=0,\quad
|u|=\text{const};$$
$$\text{赤道：}\ \theta=\frac{\pi}{2},\ \varphi=\omega\lambda .$$

**检验。** 把 $\theta=\pi/2$ 代入速率式：$a^2\omega^2=\text{const}$ ✓。$\omega$ 任意，说明赤道上的匀速圆周运动速度不受限制（球面对称）。

**读法。** 卫星在赤道平面上绕地球转，就是这条测地线（忽略地球扁率和大气）。**"轨道是测地线"这句话在球面上是精确的，在真实地球上是近似的**——真实地球的度规不是完美球面。

**10.22**
**思路。** 球面上测地半径为 $r$ 的小圆，周长 $C=2\pi a\sin(r/a)$；展开后与 $2\pi r$ 比较，差值与曲率成正比。

**过程。** 圆心角 $\theta=r/a$，小圆半径 $a\sin\theta$，周长

$$C=2\pi a\sin\frac ra .$$

展开 $\sin x=x-\frac{x^3}{6}+\frac{x^5}{120}-\cdots$（$x=r/a$）：

$$C=2\pi a\left(\frac ra-\frac{r^3}{6a^3}+\frac{r^5}{120a^5}-\cdots\right)
=2\pi r-\frac{\pi r^3}{3a^2}+\cdots$$

**差值：**

$$\Delta C=C-2\pi r=-\frac{\pi r^3}{3a^2}.$$

代入 $r=10^3\,\mathrm{m}$、$a=6.371\times10^6\,\mathrm{m}$：

$$\Delta C=-\frac{\pi\times10^9}{3\times(6.371\times10^6)^2}
=-\frac{3.1416\times10^9}{1.218\times10^{14}}
=-2.58\times10^{-5}\ \mathrm{m}.$$

**结果。**

$$\Delta C=-2.6\times10^{-5}\ \mathrm{m}=-0.026\ \mathrm{mm}\qquad(r=1\,\mathrm{km}).$$

**检验。** 量纲：$r^3/a^2$ 是长度 ✓。$a\to\infty$ 时 $\Delta C\to0$ ✓（变平）。符号为负 ✓（球面上圆的周长比平面短）。

**读法。** 1 公里半径的圆，误差只有 26 微米——**这就是为什么古人测不出地球弯曲**。要看出曲率，得把 $r/a$ 做大：卫星轨道（$r\sim10^7\,\mathrm{m}$）或者测地学基线。反过来，**精度足够高时，量周长就能测曲率**。

### 习题 10.23–10.30

**10.23**
**思路。** 沿纬线 $\theta=\theta_0$ 搬运时 $\theta$ 是常数，平行移动方程退化成两个一阶常系数方程（对 $\varphi$），消元成一个简谐振动。

**过程。** 平行移动 $\dfrac{Dv^\mu}{D\varphi}=0$，即

$$\frac{\mathrm{d}v^\mu}{\mathrm{d}\varphi}+\Gamma^\mu{}_{\nu\sigma}v^\nu\frac{\mathrm{d}x^\sigma}{\mathrm{d}\varphi}=0 .$$

沿 $\theta=\theta_0$（$\mathrm{d}\theta/\mathrm{d}\varphi=0$），只有 $\sigma=\varphi$ 的项存活：

**$\mu=\theta$：** $\Gamma^\theta{}_{\varphi\varphi}=-\sin\theta_0\cos\theta_0$，

$$\frac{\mathrm{d}v^\theta}{\mathrm{d}\varphi}=\sin\theta_0\cos\theta_0\,v^\varphi .\tag{1}$$

**$\mu=\varphi$：** $\Gamma^\varphi{}_{\varphi\theta}=\cot\theta_0$，

$$\frac{\mathrm{d}v^\varphi}{\mathrm{d}\varphi}=-\cot\theta_0\,v^\theta .\tag{2}$$

**消元：** (1) 对 $\varphi$ 求导，代入 (2)：

$$\frac{\mathrm{d}^2v^\theta}{\mathrm{d}\varphi^2}
=\sin\theta_0\cos\theta_0\left(-\cot\theta_0 v^\theta\right)
=-\cos^2\theta_0\,v^\theta .$$

这是简谐振动，解为

$$v^\theta=A\cos(c\varphi)+B\sin(c\varphi),\qquad c\equiv\cos\theta_0 .$$

代回 (2) 积分得 $v^\varphi$：

$$v^\varphi=-\frac{\cot\theta_0}{c}\left[A\sin(c\varphi)-B\cos(c\varphi)\right]
=-\frac{1}{\sin\theta_0}\left[A\sin(c\varphi)-B\cos(c\varphi)\right].$$

**结果。**

$$v^\theta=A\cos(c\varphi)+B\sin(c\varphi),\qquad
v^\varphi=-\frac{A\sin(c\varphi)-B\cos(c\varphi)}{\sin\theta_0},\qquad c=\cos\theta_0 .$$

绕一圈 $\varphi:0\to2\pi$ 后相位前进 $2\pi c$，转角 $\Delta\alpha=2\pi(1-\cos\theta_0)$。

**检验。** 长度：$g_{\theta\theta}(v^\theta)^2+g_{\varphi\varphi}(v^\varphi)^2$
$=(v^\theta)^2+\sin^2\theta_0(v^\varphi)^2$
$=(v^\theta)^2+\left[A\sin(c\varphi)-B\cos(c\varphi)\right]^2=A^2+B^2$，与 $\varphi$ 无关 ✓——平行移动保持长度。

**读法。** 转角只依赖 $\theta_0$（围出的面积），不依赖路径的细节——**和乐**。这就是 10.5.2 的"$\Delta\alpha=K\times$面积"的具体实现。

**10.24**
**思路。** $C(r)=2\pi a\sin(r/a)$ 的展开里，$r^3$ 项系数直接给出 $K$；$r^5$ 项系数给出 $K^2$，可以用来检验"$K$ 是不是常数"。

**过程。** 展开 $\sin x=x-\dfrac{x^3}{6}+\dfrac{x^5}{120}-\cdots$，$x=r/a$：

$$C=2\pi a\left(\frac ra-\frac{r^3}{6a^3}+\frac{r^5}{120a^5}-\cdots\right)
=2\pi r\left(1-\frac{r^2}{6a^2}+\frac{r^4}{120a^4}-\cdots\right).$$

一般地，对常曲率 $K$ 的曲面：

$$C(r)=2\pi r\left(1-\frac{K}{6}r^2+\frac{K^2}{120}r^4-\cdots\right).$$

对比系数：

$$\text{三次项：}-\frac{\pi}{3a^2}=-\frac{\pi K}{3}\Rightarrow K=\frac{1}{a^2};$$
$$\text{五次项：}\frac{\pi}{60a^4}=\frac{\pi K^2}{60}\Rightarrow K^2=\frac{1}{a^4}\ \checkmark .$$

**结果。**

$$K=-\frac{3}{\pi}\times(\text{$r^3$ 项系数})=\frac{1}{a^2},
\qquad
\text{$r^5$ 项与 }K^2\text{ 自洽}.$$

**检验。** 若 $r^5$ 项系数不符合 $K^2$，说明曲率不是常数（随位置变）——**这是"局部常曲率"的实验判据**。

**读法。** 用尺子量周长就能测曲率，完全不需要坐标系。$K$ 与 $K^2$ 的自洽性检验，相当于问"这个空间是不是均匀弯曲的"。

**10.25**
**思路。** 两条相邻经线，角间距 $\Delta\varphi$ 不变，实际分离是 $a\sin\theta\,\Delta\varphi$；把 $\theta=\tau/a$ 代进去就得到 $\xi(\tau)$。

**过程。** 两条经线（$\varphi=\varphi_1,\varphi_2$），$\Delta\varphi=\varphi_2-\varphi_1$。同一余纬 $\theta$ 上，两点的物理距离是纬线弧长：

$$\xi(\tau)=a\sin\theta(\tau)\,\Delta\varphi .$$

经线是测地线，$\theta$ 匀速：由 $|u|^2=a^2(\theta'^2+\sin^2\theta\varphi'^2)=a^2\theta'^2$ 为常数（经线上 $\varphi'=0$），得 $\theta'=\text{const}$，即

$$\theta(\tau)=\frac{\tau}{a}\qquad(\text{从赤道 }\theta=0\text{ 出发}).$$

代入：

$$\xi(\tau)=a\,\Delta\varphi\,\sin\frac{\tau}{a}.$$

**求二阶导核对：**

$$\frac{\mathrm{d}^2\xi}{\mathrm{d}\tau^2}=-\frac{1}{a^2}\xi .$$

**结果。**

$$\xi(\tau)=a\,\Delta\varphi\,\sin\frac{\tau}{a},
\qquad
\frac{\mathrm{d}^2\xi}{\mathrm{d}\tau^2}=-K\xi,\quad K=\frac{1}{a^2}.$$

**检验。** $\tau=0$（赤道）时 $\xi=0$——两条经线在赤道相交（出发点是同一个点），应取 $\tau_0$ 使初始分离不为零。$\tau=\pi a/2$（北极）时 $\sin(\pi/2)=1$，$\xi$ 最大；再走 $\tau=\pi a$ 时 $\xi=0$ 又相交（其实是同一点）。

**读法。** 两条"初始平行"的经线最终相交——**不是有力推它们，是空间弯的**。$\ddot\xi=-K\xi$ 就是测地线偏离方程在球面上的样子：$K>0$ 时汇聚，$K<0$ 时发散。

**10.26**
**思路。** 从"$\nabla_\lambda v^\mu$ 必须是张量"出发，倒推 $\Gamma$ 该怎么变；结果是"张量项 + 二阶导数项"，后者证明它不是张量。

**过程。** 要求

$$\nabla_\lambda v^\mu=\partial_\lambda v^\mu+\Gamma^\mu{}_{\lambda\nu}v^\nu$$

在坐标变换下按张量变。已知 $\partial_\lambda v^\mu$ 的变换会多出二阶导数项（10.4.1），所以 $\Gamma$ 的变换律里必须有一项正好抵消它。算下来：

$$\Gamma'^\mu{}_{\nu\lambda}
=\frac{\partial x'^\mu}{\partial x^\alpha}
\frac{\partial x^\beta}{\partial x'^\nu}
\frac{\partial x^\gamma}{\partial x'^\lambda}\Gamma^\alpha{}_{\beta\gamma}
+\frac{\partial x'^\mu}{\partial x^\alpha}
\frac{\partial^2 x^\alpha}{\partial x'^\nu\partial x'^\lambda}.$$

**第一项**有三个雅可比因子，是张量该有的样子。**第二项**含二阶导数，与雅可比无关，抵消不掉。

**为什么线性的变换看不出来：** 若 $\partial^2x'/\partial x^2=0$（直角坐标之间的旋转、平移），第二项消失，$\Gamma$ 在那种变换下"像"张量——这正是直角坐标里算题从不出问题的原因。

**结果。**

$$\Gamma'^\mu{}_{\nu\lambda}
=\underbrace{\text{（张量项）}}_{\text{一阶导数}}
+\underbrace{\frac{\partial x'^\mu}{\partial x^\alpha}
\frac{\partial^2 x^\alpha}{\partial x'^\nu\partial x'^\lambda}}_{\text{二阶导数}\Rightarrow\ \Gamma\text{ 不是张量}} .$$

**检验。** 平直直角坐标 $\Gamma=0$，换到极坐标 $\Gamma\ne0$——若它是张量，零张量在任何坐标下都该是零 ✓ 矛盾。

**读法。** $\Gamma$ 不是张量，但它"差一个二阶导数项"——这一项恰好补偿基矢量随位置的变化，使 $
abla$ 成为张量运算。**联络的几何身份是"补偿"，不是"分量"。**

**10.27**
**思路。** 用"局部惯性系"技巧：在任一点选坐标令 $\Gamma=0$，此时 $R$ 只剩度规的二阶导数，反对称性一目了然；再用张量性推广到处处。

**过程。** 在任一点选局部惯性系（$\Gamma=0$，$\partial g=0$），黎曼张量退化成

$$R_{\rho\sigma\mu\nu}
=\frac12\left(
\partial_\rho\partial_\mu g_{\sigma\nu}
-\partial_\rho\partial_\nu g_{\sigma\mu}
+\partial_\sigma\partial_\nu g_{\rho\mu}
-\partial_\sigma\partial_\mu g_{\rho\nu}
\right).$$

**交换 $\rho\leftrightarrow\sigma$：** 第一项 $\partial_\rho\partial_\mu g_{\sigma\nu}\to\partial_\sigma\partial_\mu g_{\rho\nu}$，正是原第四项；第二项 $\to$ 原第三项。整体变号：

$$R_{\sigma\rho\mu\nu}=-R_{\rho\sigma\mu\nu}.$$

**推广：** 两边都是张量，等式在一点成立就在该点的一切坐标系里成立；该点任意，所以处处成立。

**结果。**

$$R_{\rho\sigma\mu\nu}=-R_{\sigma\rho\mu\nu},\qquad
R_{\rho\sigma\mu\nu}=-R_{\rho\sigma\nu\mu}.$$

（第二个由同样的手法，交换 $\mu\leftrightarrow\nu$。）

**检验。** 球面上验证：$R_{\theta\varphi\theta\varphi}=a^2\sin^2\theta$，而 $R_{\varphi\theta\theta\varphi}=-a^2\sin^2\theta$ ✓。

**读法。** 反对称性不是装饰：它把 $4^4=256$ 个分量砍到 36，再配合第一比安基砍到 20。**没有这条对称性，广义相对论的计算量会大到无法进行。**

**10.28**
**思路。** 常曲率空间的形式是 $R_{\mu\nu\rho\sigma}=K(g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho})$；用球面已知的 $R_{\theta\varphi\theta\varphi}$ 定出 $K$ 即可。

**过程。** 取 $\mu=\theta$、$\nu=\varphi$、$\rho=\theta$、$\sigma=\varphi$，右边：

$$K\left(g_{\theta\theta}g_{\varphi\varphi}-g_{\theta\varphi}g_{\varphi\theta}\right)
=K\left(a^2\cdot a^2\sin^2\theta-0\right)=Ka^4\sin^2\theta .$$

左边由 10.6.3：$R_{\theta\varphi\theta\varphi}=a^2\sin^2\theta$。相等：

$$Ka^4\sin^2\theta=a^2\sin^2\theta
\quad\Longrightarrow\quad
K=\frac{1}{a^2}.$$

**结果。**

$$R_{\mu\nu\rho\sigma}=K\left(g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho}\right),
\qquad K=\frac{1}{a^2}.$$

**检验。** 缩并两次：$R=K\cdot n(n-1)$，二维给 $R=2K=2/a^2$ ✓，与 10.6.3 一致。

**读法。** 右边是"用度规能造出来的、具有黎曼张量全部对称性的唯一组合"（二维只有一个独立分量）。所以**任何常曲率空间都取这个形式**，$K$ 就是高斯曲率——球面正、平面零、双曲面负。

**10.29**
**思路。** 度规相容 $\nabla_\lambda g_{\mu\nu}=0$ 是"$\Gamma$ 公式里那个 $\frac12$ 存在的原因"；直接取一组分量代进去验证。

**过程。** 协变导数作用在度规上：

$$\nabla_\lambda g_{\mu\nu}
=\frac{\partial g_{\mu\nu}}{\partial x^\lambda}
-\Gamma^\sigma{}_{\lambda\mu}g_{\sigma\nu}
-\Gamma^\sigma{}_{\lambda\nu}g_{\mu\sigma}.$$

取 $\mu=\nu=\varphi$、$\lambda=\theta$。只有 $\Gamma^\varphi{}_{\theta\varphi}=\Gamma^\varphi{}_{\varphi\theta}=\cot\theta$ 相关：

$$\nabla_\theta g_{\varphi\varphi}
=2a^2\sin\theta\cos\theta
-2\left(\cot\theta\right)\left(a^2\sin^2\theta\right).$$

第二项 $=2a^2\dfrac{\cos\theta}{\sin\theta}\sin^2\theta=2a^2\sin\theta\cos\theta$，与第一项相同：

$$\nabla_\theta g_{\varphi\varphi}=0 .$$

**其余组合同理：** 不含 $\partial_\theta g_{\varphi\varphi}$ 的那些，要么 $\partial g=0$、要么 $\Gamma$ 项成对抵消（如 $\nabla_\varphi g_{\theta\theta}$）；$\mu\ne\nu$ 时两边都是零。

**结果。**

$$\nabla_\lambda g_{\mu\nu}=0\qquad(\text{球面上所有分量}).$$

**检验。** 若 $\Gamma$ 公式里没有 $\frac12$，第二项会差一倍，这条就不成立——**$\frac12$ 是度规相容性要求的**。

**读法。** $
abla_\lambda g_{\mu
u}=0$ 的物理内容是"平行移动保持长度与角度"——这是"用尺子量"这件事在弯曲空间里仍然可靠的前提。**$\Gamma$ 公式里的 $
rac12$ 正是为了它而设。**

**10.30**
**思路。** 设一族测地线 $x^\mu(\tau,s)$，分离矢量 $\xi^\mu=\partial x^\mu/\partial s$；对测地线方程沿 $s$ 求导，再用导数可交换与黎曼张量的定义。

**过程。** **第一步，导数可交换：** $u^\mu=\partial x^\mu/\partial\tau$、$\xi^\mu=\partial x^\mu/\partial s$，则

$$\frac{\partial u^\mu}{\partial s}=\frac{\partial\xi^\mu}{\partial\tau}.$$

**第二步，对测地线方程沿 $s$ 求导。** 每条曲线都满足

$$\frac{\partial u^\mu}{\partial\tau}+\Gamma^\mu{}_{\nu\rho}u^\nu u^\rho=0 .$$

两边作用 $\partial_s$（记住 $\partial_s\Gamma=\xi^\lambda\partial_\lambda\Gamma$、$\partial_s u=\partial_\tau\xi$），得到

$$\frac{D^2\xi^\mu}{D\tau^2}
=-R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma .$$

**第三步，读含义：** 左边是分离矢量沿测地线的"二阶协变加速度"，右边是黎曼张量。这是张量方程，坐标无关。

**结果。**

$$\frac{D^2\xi^\mu}{D\tau^2}
=-R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma .$$

**检验（球面）：** 两条经线，$\xi=a\sin\theta\Delta\varphi$、$\theta=\tau/a$。左边在一维分离下化作 $\ddot\xi$；右边缩并给 $-K\xi$。得 $\ddot\xi=-\xi/a^2$，解正是 $\xi\propto\sin(\tau/a)$ ✓，与题 10.25 一致。

**读法。** 这就是**潮汐力**的几何版本：单个粒子感受不到"引力"（走测地线），但两个相邻粒子会相对加速——相对加速度由 $R$ 决定，坐标无关。**"引力 = 时空弯曲"这句话的全部数学内容，就在这个方程里。**

### 概念与判断 10.31–10.39

**10.31**（张量就是一堆按矩阵排列的数？）

**错。** 张量的定义是**变换律**（换坐标时按固定规则变），不是"某种排列方式"。

同一个物理量在不同坐标下是不同的数组；反过来，随便摆成矩阵的数字（比如三个数排成 $2\times2$）
未必按张量变换。

**反例一：** $\partial_\mu v^\nu$ 也是"一堆按矩阵排列的数"，但它不是张量——换坐标后多出二阶导数项。

**反例二：** 坐标 $x^\mu$ 有上标、是"一列数"，但它的变换律是仿射的（差一个平移），不是矢量。

**反例三：** 三个数排成 $\mathrm{diag}(1,2,3)$ 在某个坐标系里看似"对角张量"，
但换个坐标后它不按 $T'=RT R^{\mathsf T}$ 变——外观再像也不是。

**判据：** 看变换律，不看外观。**"有指标"不等于"是张量"，"是矩阵"更不等于。**

**10.32**（在一点令 $\Gamma=0$，就证明附近平直？）

**错。** "令 $\Gamma=0$"只说明那一点的**一阶**导数为零（局部惯性系），而曲率是 $\Gamma$ 的**导数**组合，一点上不为零。

**反例：** 抛物线顶点处斜率为零（一阶导为零），但二阶导数不为零，曲线还是弯的。球面上任何一点都能令 $\Gamma=0$，但 $R=2/a^2\ne0$。

**正确的说法：** "局部平直"永远是近似的、一阶的；二阶（曲率）信息去不掉。

**10.33**（极坐标 $\Gamma\ne0$，所以平面是弯的？）

**错。** $\Gamma\ne0$ 只说明"基矢量随位置转"，与空间是否弯曲无关。

**反例：** 平面极坐标的 $\Gamma^r{}_{\varphi\varphi}=-r$、$\Gamma^\varphi{}_{r\varphi}=1/r$，但把这两个代进 $R^r{}_{\varphi r\varphi}$，两项精确抵消（$-1$ 与 $+1$），$R\equiv0$（10.6.4 已算）。

**判据：** 只看 $R^\rho{}_{\sigma\mu\nu}$。"联络非零"和"空间弯曲"是两件事。

**10.34**（测地线就是最短路径？）

**只在局部、且没有共轭点时成立。**

**反例：** 球面上连接两点的测地线有两条（短弧和长弧），长的那条不是最短；再长一些出现共轭点之后，它连"局部最短"都不是，反而是极大值方向。
取赤道上两点，短弧是 $\pi/2$、长弧是 $3\pi/2$——两者都满足测地线方程，但只有一个最短。

**正确的定义：** 测地线是"切矢量自平行"的曲线，等价地是弧长泛函的**驻值**曲线
（$\delta\int\mathrm{d}s=0$）。驻值 = 极值或鞍点，"最短"只是其中一种情形。

**为什么容易错：** 在平直空间里，驻值就等于最短，所以"测地线 = 最短"在那里永远对，
习惯带过来就成了误解。**曲率越大，这个区别越明显。**

**实用判据：** 两点之间的测地线唯一且短时，可以当"最短"用（工程上多数情形如此）；
一旦绕过大半个球（比如洲际航线经过的经度差超过 $180^\circ$），必须先判断走哪一支。

**10.35**（某坐标系里全为零 ⟹ 零张量？）

**对**，这就是零张量原理：张量的变换律是线性的，零必映到零。

**为什么重要：** 它把"证明张量方程"化简成"在一个方便的坐标系里验证"。10.6.4 证明平面曲率为零，只在极坐标下算了一遍；因为 $R$ 是张量，极坐标下为零就意味着处处为零。

**反过来用：** 某量在直角坐标里为零、极坐标里非零，它一定不是张量（$\Gamma$ 就是这样暴露的）。

**注意前提：** 只对**张量**成立；$\Gamma$、$\partial_\mu v^\nu$ 这类非张量不适用。

**10.36**（$\det g$ 在坐标变换下不变？）

**错。** 度规按

$$g'_{\mu\nu}=\frac{\partial x^\alpha}{\partial x'^\mu}\frac{\partial x^\beta}{\partial x'^\nu}g_{\alpha\beta}$$

变，取行列式：

$$\det g'=\det g\cdot\left|\det\frac{\partial x}{\partial x'}\right|^2 .$$

所以 $\det g$ 不是标量，是**密度**（带权 -2）。

**不变的是** $\sqrt{|g|}\,\mathrm{d}^4x$：因子与雅可比相消，所以 $\int f\sqrt{|g|}\mathrm{d}^4x$ 坐标无关。这就是弯曲空间积分的正确写法（也是作用量里必须有 $\sqrt{|g|}$ 的原因）。

**10.37**（$\Gamma$ 有三个指标，所以是张量？）

**错，而且是"指标外观"最典型的骗局。**

**理由一：** 张量变换律只含一阶导数，$\Gamma$ 含 $\partial^2x'/\partial x^2$（题 10.26）。

**理由二：** 平直直角坐标 $\Gamma\equiv0$、极坐标 $\Gamma\ne0$。若它是张量，零张量在任何坐标下都该是零。

**类比：** 坐标 $x^\mu$ 也有上标，但它的变换律是仿射的（差一个平移），不是矢量。

**合法的用法：** 只在 $\nabla_\lambda v^\mu$（整体是张量）或 $R$ 的 $\Gamma\Gamma$ 组合里出现。

**10.38**（北极 $\Gamma$ 发散说明有奇点？）

**错。** $\Gamma^\varphi{}_{\theta\varphi}=\cot\theta$ 在 $\theta\to0$ 按 $1/\theta$ 发散，这是因为 $\varphi$ 坐标在北极没有定义（所有经线汇聚），不是几何坏了。

**判据：** 算标量曲率 $R=2/a^2$，在北极**有限** ✓；再算 $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}=4/a^4$，也有限 ✓。

**结论：** **坐标奇点**（某个坐标分量发散而曲率标量有限）≠ **物理奇点**（曲率发散）。换一套覆盖北极的坐标，$\Gamma$ 就有限了。

**10.39**（潮汐力说明引力是"真实的力"？）

**这个说法要纠正两点。**

**第一，** 单个粒子在引力场里自由下落时是"失重"的——它感受不到任何力，走的是测地线。**"力"在单粒子的层面可以被变换掉**（换到自由下落系）。

**第二，** 潮汐效应是**两个相邻粒子之间的相对加速度**，由测地线偏离方程给出，正比于黎曼张量。**它是相对的、坐标无关的，所以它是"时空弯曲"的证据，而不是"引力是力"的证据。**

**正确的说法：** 引力不是力，是几何。**测地线偏离方程是把"弯曲"翻译成"可测量效应"的那句话**，右边只能由 $R$ 给出，不能由任何"力"给出。

