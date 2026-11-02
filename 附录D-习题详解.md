# 附录 D 习题详解

> 每题给关键步骤、中间结果和最终答案。缺的步骤请自己补全后再看。

## 第 1 章

**1.1** 由链式法则，$\frac{\partial u}{\partial t}=-cF'(x-ct)$，$\frac{\partial u}{\partial x}=F'(x-ct)$，代入即得 $\frac{\partial u}{\partial t}+c\frac{\partial u}{\partial x}=-cF'+cF'=0$。反过来，这个一阶方程等价于「沿 $\mathrm{d}x/\mathrm{d}t=c$ 的路线 $u$ 不变」，而「沿一族平行直线取常值」的函数只能写成 $x-ct$ 的函数。所以两个说法是同一件事：一阶方程的解就是右行波。

**1.2** $u(x,t)=\frac{h}{2}\left[\exp\left(-\frac{(x-ct)^2}{a^2}\right)+\exp\left(-\frac{(x+ct)^2}{a^2}\right)\right]$。对称性保证极大值点只在 $x=0$ 或分裂出的两个峰上。$ct\ll a$ 时两个高斯几乎重合，峰在 $x=0$，高 $h\exp(-c^2t^2/a^2)$，随时间掉但仍在中间。$ct\gg a$ 时两峰分开，各高 $h/2$，位于 $x=\pm ct$。分岔发生在 $ct\approx0.78a$：令 $e^{-\tau}=\frac{1}{2}(1+e^{-4\tau})$（$\tau=c^2t^2/a^2$），解出 $\tau\approx0.61$。所以峰值从 $h$ 连续降到 $h/2$，位置从 $0$ 分岔到 $\pm ct$。

**1.3** $u=\frac{v_0}{2c}\times\left([x-ct,x+ct]\text{ 与 }[-a,a]\text{ 的重叠长度}\right)$。$ct>a$ 时：$|x|<ct-a$ 处 $u=v_0a/c$；$ct-a<|x|<ct+a$ 处 $u=\frac{v_0}{2c}(a+ct-|x|)$；$|x|>ct+a$ 处 $u=0$。全局最大位移 $v_0a/c$。弦**不回到平衡**：平台高度不变、宽度 $2(ct-a)$ 无限增长，两侧斜坡向外跑。平台内 $\frac{\partial u}{\partial t}=\frac{\partial u}{\partial x}=0$，能量全在斜坡里，总量恒定。物理解释：初速的净冲量不为零，无限长弦上没有力把它拉回原位。

**1.4** $u(x,t)=\sin(kx)\cos(\omega t)$，其中 $\omega=ck$。用积化和差，$u=\frac{1}{2}\sin(kx-\omega t)+\frac{1}{2}\sin(kx+\omega t)$：两个等幅反向行波。频率 $f=\omega/2\pi=ck/2\pi=c/\lambda$，波长就是 $2\pi/k$。它「原地不动」是因为两个反向行波在同一处叠加，空间图样 $\sin(kx)$ 固定，只有整体幅度按 $\cos\omega t$ 涨落；波节处永远为零。

**1.5** $k=2\pi/\lambda=12.6\ \mathrm{m^{-1}}$，$\omega=ck=418\times12.57=5.26\times10^{3}\ \mathrm{s^{-1}}$。由 1.6.4，$e_k=e_p=\frac{1}{2}\rho\omega^{2}A^{2}\sin^{2}(kx-\omega t)$。峰值：$\frac12\times4.0\times10^{-4}\times2.76\times10^{7}\times10^{-6}=5.5\times10^{-3}\ \mathrm{J/m}$。$j=ce$，峰值 $2c e_k^{\max}=418\times1.1\times10^{-2}=4.6\ \mathrm{W}$。平均功率 $\bar j=\frac{1}{2}Z\omega^{2}A^{2}$，$Z=\sqrt{T\rho}=0.167\ \mathrm{kg/s}$，得 $\bar j=2.3\ \mathrm{W}$。

**1.6** (a) $e_k=\frac{1}{2}\rho A^{2}\omega^{2}\sin^{2}(kx)\sin^{2}(\omega t)$，$e_p=\frac{1}{2}\rho A^{2}\omega^{2}\cos^{2}(kx)\cos^{2}(\omega t)$，$j=\frac{1}{2}TA^{2}k\omega\sin(2kx)\sin(2\omega t)$。(b) $\int_0^L\sin(2kx)\mathrm{d}x=0$（因 $k=n\pi/L$，两个整周期），故净能流为零。(c) $E=\int_0^L(e_k+e_p)\mathrm{d}x=\frac{\rho\omega^{2}A^{2}L}{4}\left(\sin^{2}\omega t+\cos^{2}\omega t\right)=\frac{\rho\omega^{2}A^{2}L}{4}$，与 $t$ 无关。

**1.7** $a_n=\frac{2}{L}\int_0^L f\sin\frac{n\pi x}{L}\mathrm{d}x=\frac{8h}{n^{2}\pi^{2}}\sin\frac{n\pi}{2}$。$\sin\frac{n\pi}{2}=0$ 对偶数 $n$，所以所有偶次为零—中点拨弦对偶数模式是节点。$E_n=\frac{16Th^{2}}{n^{2}\pi^{2}L}$，总能量 $E=\frac{2Th^{2}}{L}$，故 $\frac{E_1}{E}=\frac{8}{\pi^{2}}=0.81$，$\frac{E_3}{E}=\frac{0.81}{9}=0.09$。奇数阶能量按 $1/n^{2}$ 衰减。

**1.8** 令 $\chi(s)=1$（$a<s<2a$）、否则为 $0$。奇延拓后 $u=\frac{h}{2}\left[\chi(x-ct)+\chi(x+ct)\right]$（$x>ct$），$u=\frac{h}{2}\left[-\chi(ct-x)+\chi(x+ct)\right]$（$x<ct$）。分段：$ct<a$ 时只有一个向墙走的平台；$a<ct<2a$ 时墙边出现负平台；$ct>2a$ 时入射平台完全进入 $x<0$，弦上只剩 $-\frac{h}{2}$ 的反射平台（$ct-2a<x<ct-a$）与 $+\frac{h}{2}$ 的右行平台（$a+ct<x<2a+ct$）。反射平台到达 $x=3a$ 要 $ct-a=3a$，即 $ct=4a$；入射平台到达 $x=3a$ 在 $ct=a$。

**1.9** 偶延拓：$u=\frac{h}{2}\left[\chi(x-ct)+\chi(x+ct)\right]$，两项同号。端点处 $u(0,t)=\frac{h}{2}\left[\chi(-ct)+\chi(ct)\right]=h\,\chi(ct)$，所以当 $a<ct<2a$ 时端点位移正好等于 $h$（是入射平台高度 $\frac h2$ 的两倍）。随后反射平台以 $+\frac h2$ 向右离开。

**1.10** $Z=\sqrt{T\rho}$，故 $Z_2=2Z_1$。$R=\frac{Z_1-Z_2}{Z_1+Z_2}=-\frac{1}{3}$，$S=1+R=\frac{2}{3}$。能量反射率 $R^{2}=\frac{1}{9}=11\%$；透射率 $Z_2S^{2}/Z_1=2\times\frac{4}{9}=\frac{8}{9}=89\%$，两者相加为 1。密度大的弦相当于「较硬的墙」，反射倒相。

**1.11** 积化和差：$\cos(kx-\omega t)+\cos(kx+\omega t)=2\cos(kx)\cos(\omega t)$，是驻波。由 1.6.4 的结果，$j=\frac{1}{2}Tc\,k\omega\sin(2kx)\sin(2\omega t)$。$\int_0^L\sin(2kx)\mathrm{d}x=0$，故净能流为零：两个反向行波各自的能流大小相等方向相反，逐点抵消，只剩局部的来回倒腾。

**1.12** $c=\sqrt{T/\rho}=418\ \mathrm{m/s}$；$f_1=c/(2L)=322\ \mathrm{Hz}$；$f_5=5f_1=1.61\ \mathrm{kHz}$；往返时间 $2L/c=1.30/418=3.11\ \mathrm{ms}$。$1/3.11\ \mathrm{ms}=322\ \mathrm{Hz}=f_1$，正是「往返一次 = 一个基频周期」。

**1.13** $f\propto\sqrt{T}$，故 $T'=T(f'/f)^{2}=70\times(329.6/321.8)^{2}=73.4\ \mathrm{N}$，增加约 $4.9\%$。非线性来自平方根：$\frac{\Delta f}{f}=\frac{1}{2}\frac{\Delta T}{T}$，张力变化 $5\%$ 只换来频率变化 $2.5\%$。所以弦轴转一点点，音高只动一点点，而且越接近目标越难调—这正是调音要「小步多次」的原因。

**1.14** 长度被两端约束，热膨胀转化为张力下降：$\Delta T=-EA\alpha\Delta\Theta$。$A=\pi d^{2}/4=1.26\times10^{-7}\ \mathrm{m^{2}}$，$EA=2.5\times10^{4}\ \mathrm{N}$，$\Delta T=-2.5\times10^{4}\times1.2\times10^{-5}\times10=-3.0\ \mathrm{N}$，$T'=67\ \mathrm{N}$。$f'/f=\sqrt{67/70}=0.978$，音分 $1200\log_2 0.978=-38$。真实情况还要加上琴颈与琴身的热膨胀（会补偿一部分）以及湿度对张力的影响，所以实测偏移通常小于这个估计。

**1.15** (a) $A=1.77\times10^{-6}\ \mathrm{m^{2}}$，$\rho_{\rm lin}=1.38\times10^{-2}\ \mathrm{kg/m}$，$T=\sigma A=1.41\times10^{3}\ \mathrm{N}$，$c=320\ \mathrm{m/s}$，$f_1=c/2L=133\ \mathrm{Hz}$。(b) 要到 $27.5\ \mathrm{Hz}$，$T/\rho$ 要降 $(133/27.5)^{2}=23$ 倍。降张力到 $60\ \mathrm{N}$ 可以做到，但 $B=\pi^{2}EI/(TL^{2})\propto1/T$ 会增大 23 倍，非谐性变得不可接受；改把线密度加到 $0.32\ \mathrm{kg/m}$（缠铜），$T$ 保持不变，$f$ 降到 $27.5\ \mathrm{Hz}$ 而 $B$ 不变（$d=1.5\ \mathrm{mm}$ 时约 $2.4\times10^{-4}$）。所以必须加质量，不能减张力。

**1.16** $\Delta t=2L/c=1.20/343=3.5\ \mathrm{ms}$。声压的反射系数：开口端 $p=0$，$R=-1$（倒相）；闭口端速度为零、声压最大，$R=+1$（同相）。位移（速度）的符号正好相反。「开口端是声压节点」与 1.7 节的自由端是同一件事：自由端的条件是力为零，声学里「力」对应声压，所以压力释放 = 自由端，此时位移（速度）取极大，与弦的自由端完全同构。

**1.17** 设震中距 $d$，则 $d/3.5-d/6.0=12$，即 $d(0.2857-0.1667)=12$，$d=101\ \mathrm{km}$。S 波振幅大但到得晚，P 波到得早但弱；两者都用才能定震中，单用 S 波无法定发震时刻。

**1.18** 钢中：$2000/5000=0.40\ \mathrm{s}$；空气中：$2000/343=5.83\ \mathrm{s}$；时间差 $5.4\ \mathrm{s}$。这个「先到的是固体里的纵波」是 1.5 节「同一段路程、不同速度」的最朴素演示。

**1.19** 设入射 $f(t-x/c)$、反射 $Rf(t+x/c)$。端点条件 $T\frac{\partial u}{\partial x}\Big|_{x=0}=\kappa u(0,t)$ 对简谐波给出 $iTk(1-R)=\kappa(1+R)$，解出 $R=\dfrac{iTk-\kappa}{iTk+\kappa}$。分子与分母互为共轭，所以 $|R|=1$：端点不吸能，只改相位。分界在 $Tk=\kappa$，即 $\omega_c=\kappa c/T$；代入 $\kappa=10^{3}\ \mathrm{N/m}$、$T=70\ \mathrm{N}$、$c=\sqrt{T/\rho}=418\ \mathrm{m/s}$，得 $\omega_c=6.0\times10^{3}\ \mathrm{rad/s}$、$f_c\approx9.5\times10^{2}\ \mathrm{Hz}$。低于它像撞固定端（倒相），高于它像撞自由端（不倒相）。(c) 脉冲含各种频率，各成分的反射相位不同，叠加之后就从尖脉冲拖成一段尾巴。

**1.20** $\tau=Q/\omega_1=1000/(2\pi\times322)=0.49\ \mathrm{s}$，振幅按 $e^{-t/\tau}$ 衰减，听觉上 3 到 4 个 $\tau$，即 $1.5$ 到 $2\ \mathrm{s}$。若 $\gamma\propto\omega$，则 $\tau_n=2/\gamma_n\propto1/\omega_n$，第 $n$ 阶的衰减时间是基频的 $1/n$：第 10 阶只有 $49\ \mathrm{ms}$。所以余音在几十毫秒后就只剩低阶，听感由亮变暗。

**1.21** $c=\sqrt{9.8\times4000}=198\ \mathrm{m/s}$，$t=8.0\times10^{6}/198=4.0\times10^{4}\ \mathrm{s}=11\ \mathrm{h}$。近岸水浅，$c=\sqrt{gh}$ 变小，而能流 $c\times$（单位宽度的能量）近似守恒，波长被压缩、振幅必须增大；浅水波的格林定律给出振幅 $\propto h^{-1/4}$，所以几千米深的浪到岸边可以放大到几米。

**1.22** 在 $x=0$ 处 $u=(1+R)f$、$\frac{\partial u}{\partial x}=\frac{R-1}{c}f'$，质量块的运动方程给出 $T\frac{\partial u}{\partial x}=M\frac{\partial^{2}u}{\partial t^{2}}$。取 $f=e^{-i\omega t}$ 代入，得 $iTk(1-R)=-M\omega^{2}(1+R)$，于是 $R=\dfrac{iTk+M\omega^{2}}{iTk-M\omega^{2}}$，分子分母共轭，$|R|=1$。分界在 $M\omega^{2}=Tk$，即 $\omega_c=T/(Mc)$；代入 $M=2.0\ \mathrm{g}$、$T=70\ \mathrm{N}$、$c=418\ \mathrm{m/s}$，得 $\omega_c=8.4\times10^{1}\ \mathrm{rad/s}$、$f_c\approx13\ \mathrm{Hz}$。低频时质量块很容易被推着走，端点几乎不约束（$R\to+1$，像自由端）；高频时它来不及响应（$R\to-1$，像固定端）。

**1.23** 拾音器输出正比于该点的弦速 $\frac{\partial u}{\partial t}\propto\sin\frac{n\pi x_p}{L}$。$x_p=L/5$ 时 $\sin\frac{n\pi}{5}=0$ 对 $n=5,10,15,\dots$，这些泛音没有输出。三个拾音器装在离琴桥不同距离处，各自削掉的泛音组不同，所以同一根弦在三个位置上的音色不同—这不是电路差异，是几何造成的频谱缺口。

**1.24** $x_p=L/7$ 时 $\sin\frac{n\pi}{7}=0$ 对 $n=7,14$，第 7 泛音被削弱。若挪到 $L/2$，所有偶数阶全为零，只剩奇次谐波，音色会像单簧管那样「空心」。钢琴需要宽的频谱来支撑力度变化的音色，所以击弦点选在 $1/7$ 到 $1/9$ 附近，既避开低阶节点，又保留足够多的高次泛音。

**1.25** 由 1.6.2，$\frac{\mathrm{d}E}{\mathrm{d}t}=-j(L)+j(0)$。固定端 $u_t=0$、自由端 $u_x=0$，两种情形 $j=-Tu_xu_t$ 在端点都为零，故 $\frac{\mathrm{d}E}{\mathrm{d}t}=0$。跳变：把高 $\Delta h$ 的跳变摊在宽 $\epsilon$ 的过渡层上，$\frac{\partial u}{\partial x}\sim\Delta h/\epsilon$，弹性势能 $\frac{T}{2}\int(u_x)^{2}\mathrm{d}x\sim\frac{T}{2}\frac{\Delta h^{2}}{\epsilon^{2}}\epsilon=\frac{T\Delta h^{2}}{2\epsilon}\to\infty$。物理上要在零宽度内造成 $\Delta h$ 的位移，需要无穷大的力。

**1.26** $f$ 满足 $f(0)=f(L)=0$，逐项求导得 $f'=\sum a_n\frac{n\pi}{L}\cos\frac{n\pi x}{L}$。用 $\int_0^L\cos\frac{n\pi x}{L}\cos\frac{m\pi x}{L}\mathrm{d}x=\frac{L}{2}\delta_{nm}$，得 $\int_0^L(f')^{2}\mathrm{d}x=\frac{\pi^{2}}{2L}\sum n^{2}a_n^{2}$，即 $\sum n^{2}a_n^{2}=\frac{2L}{\pi^{2}}\int_0^L(f')^{2}\mathrm{d}x$。代入 $E_n$ 的表达式求和：$E=\frac{\pi^{2}T}{4L}\sum n^{2}a_n^{2}=\frac{T}{2}\int_0^L(f')^{2}\mathrm{d}x$，与 1.6.1 的势能公式一致。用例 1.4 的三角形：$\int(f')^{2}=\frac{h^{2}}{x_0}+\frac{h^{2}}{L-x_0}=\frac{9h^{2}}{2L}$（$x_0=L/3$），乘以 $T/2$ 得 $\frac{9Th^{2}}{4L}$，与例 1.4 的结果逐字相同。

**1.27** 代 $u=A\cos(kx-\omega t)$ 得 $\omega^{2}=c^{2}k^{2}+\frac{EI}{\rho}k^{4}$，即 $\omega=ck\sqrt{1+\frac{EI}{T}k^{2}}$。相速度 $v_p=\frac{\omega}{k}=c\sqrt{1+\frac{EI}{T}k^{2}}$；群速度 $v_g=\frac{\mathrm{d}\omega}{\mathrm{d}k}=\frac{c^{2}k+2(EI/\rho)k^{3}}{\omega}$。令 $x=\frac{EI}{T}k^{2}>0$，则 $\frac{v_g}{v_p}=\frac{1+2x}{1+x}>1$。高频（大 $k$）跑得快，所以脉冲到达时高频先到、低频后到，形成「啁啾」；这就是钢琴击弦瞬间听起来特别「亮」的原因，也是色散的定义。

**1.28** 设 $u=e^{i(kx-\omega t)}+Re^{i(-kx-\omega t)}$，在 $x=0$ 处 $u=(1+R)e^{-i\omega t}$，$\frac{\partial u}{\partial x}=ik(1-R)e^{-i\omega t}$。代入边界 $T\partial_x u=\kappa u$：$iTk(1-R)=\kappa(1+R)$，解出 $R=\frac{iTk-\kappa}{iTk+\kappa}$。分子分母互为共轭，故 $|R|=1$：不吸能、只改相位。分界在 $Tk=\kappa$，即 $\omega_c=\kappa c/T$。代入 $\kappa=10^{3}\ \mathrm{N/m}$、$c=418\ \mathrm{m/s}$、$T=70\ \mathrm{N}$：$\omega_c=6.0\times10^{3}\ \mathrm{rad/s}$，$f_c=950\ \mathrm{Hz}$。低于它像固定端（倒相），高于它像自由端（不倒相）。

**1.29** 振幅按 $e^{-\gamma_n t/2}$ 衰减，故 $\tau_n=2/\gamma_n=2/(\beta\omega_n^{2})$，于是 $\tau_{10}/\tau_1=\omega_1^{2}/\omega_{10}^{2}=1/100$。若 $\tau_1=2.0\ \mathrm{s}$，则 $\tau_{10}=0.020\ \mathrm{s}$。高次泛音先消失，耳朵接收到的频谱随时间从宽变窄，听感就是「由亮变暗」。真实乐器的指数比 $2$ 温和（$\gamma\propto\omega^{0.6}$ 量级），但方向相同。

**1.30** (a) 设 $u=X(x)\sin\Omega t$，代入方程得 $X''+\frac{\Omega^{2}}{c^{2}}X=0$，$X(0)=A$、$X(L)=0$。解为 $X(x)=A\frac{\sin\left[k(L-x)\right]}{\sin(kL)}$，$k=\Omega/c$。(b) 当 $\sin(kL)\to0$ 即 $kL=n\pi$、$\Omega=n\pi c/L$ 时振幅发散（无阻尼极限），这就是共振。(c) $\sin(kL)$ 正是「往返一次的闭合因子」：往返相位为 $2kL$，令其为 $2\pi$ 的整数倍就得到 $kL=n\pi$，与驻波条件完全一致。

**1.31** (a) 判据：$\frac{f_n}{nf_1}-1$ 与 $n^{2}$ 成正比，且比例常数对前 8 阶一致。用 $f_1=261.0$ 算出 $f_8/(8f_1)=2133.6/2088=1.0218$，$f_4/(4f_1)=1049.8/1044=1.0056$，$f_2/(2f_1)=522.7/522=1.0013$：比值分别对应 $n^{2}=64,16,4$，与 $n^{2}$ 成正比，是典型的刚度非谐性。(b) 由 $f_n/(nf_1)=\sqrt{1+Bn^{2}}$，取 $n=8$：$B=(1.0218^{2}-1)/64=6.8\times10^{-4}$；用 $n=4$ 得 $B=7.0\times10^{-4}$，取 $B\approx6.9\times10^{-4}$。(c) 若张力沿弦线性变化，波速 $c(x)$ 随位置变，各阶频率的偏移不与 $n^{2}$ 成正比，而且 $f_1$ 本身会随温度、湿度漂移；区分办法是人为改变张力（或温度）再测一遍：整体平移说明是张力问题，而「高阶偏得多、且对张力不敏感」才是刚度。

**1.32** 错。通解的形式要求 $F$、$G$ 二阶可导，而「任意初始条件」里包含有跳变的形状，那种初值没有经典解（能量无穷，见 1.6.5）。正确的说法是：初值足够光滑时解存在且唯一；有折点（导数跳变）时仍有物理解（理想弦允许折点）；有跳变则没有。

**1.33** 错。$f\propto\sqrt{T}$，张力加倍只让频率升高 $\sqrt{2}$ 倍，约 6 个半音，不到一个八度。要升高八度得把张力变成 4 倍，那通常会超过弦的强度。

**1.34** 错。公式在形式上还能写，但那样的「解」在跳变处的二阶导数不存在，而且总能量发散（习题 1.25）。物理上要在零宽度内造成有限跳变，需要无穷大的力，所以这种初始条件不可能实现。

**1.35** 错。理想弦的两类边界确实不漏能（1.6.3），但真实弦还有空气粘性、材料内摩擦，以及琴桥把能量传给面板并辐射出去。余音衰减正是这些模型外机制的结果，想描述它必须在方程里显式加阻尼。

**1.36** 错。$x_0=L/3$ 是第 3 个模式的节点，所以在那里拨弦不能**激发**它；但只要它被激发了，弦上除节点以外处处都有位移，声音照样辐射。节点的意义是「激励不到」，不是「不存在」。

**1.37** 错。端点附近位移瞬时加倍，但能量没有加倍：入射波带来一份能量，一半继续以反射波的形式带走，端点处只是两列波瞬时叠加。「加倍」是位移的，不是能量的。

**1.38** 对。对无色散均匀弦上的行波，$e_k=e_p$ 处处成立（1.6.4），所以 $e=e_k+e_p=2e_k$。注意这只对行波成立；驻波里两者不相等，一般时刻 $e_p$ 可以远大于 $e_k$。

**1.39** 错。这里的 $c$ 是弦（或介质）的横波速度，由 $T$、$\rho$ 决定，不是信号速度的上限。在相对论情形下，波动方程本身要换成满足洛伦兹协变的方程，「$c$ 很大」这件事在物理上不允许；弦的模型只是非相对论近似。

## 第 2 章

> 每题给关键步骤、中间结果和最终答案。缺的步骤请自己补全后再看。

## A 组

**2.1** 分部积分（$u=x$，$dv=\sin$）：

$$a_n=\frac{2}{L}\left[-\frac{Lx}{n\pi}\cos\frac{n\pi x}{L}\right]_0^L+\frac{2}{n\pi}\int_0^L\cos\frac{n\pi x}{L}\,dx=\frac{2L(-1)^{n+1}}{n\pi}.$$

第二项积分为零。衰减：$f(0)=0$ 而 $f(L)=L\ne0$，2.6.1 的边界项 $\frac{2}{n\pi}[f(0)-(-1)^nf(L)]=-\frac{2L(-1)^n}{n\pi}$ 不为零，所以只能按 $1/n$ 衰减。**读法：** 端点值不匹配，是这一章最常见的慢收敛来源。

**2.2** 用三倍角公式 $\sin^3\theta=\frac34\sin\theta-\frac14\sin3\theta$，取 $\theta=\pi x/L$：

$$f(x)=\frac34\sin\frac{\pi x}{L}-\frac14\sin\frac{3\pi x}{L}.$$

正弦展开唯一，直接读出 $a_1=\frac34$，$a_3=-\frac14$，其余为零。**原因：** 初值本身已经是本征函数的组合，投影是恒等操作，不会「混」出别的模。

**2.3** $X=\sin kx$，$X'(L)=k\cos kL=0$ 给出 $kL=(2n-1)\pi/2$：

$$k_n=\frac{(2n-1)\pi}{2L},\qquad X_n=\sin\frac{(2n-1)\pi x}{2L},\qquad \int_0^LX_n^2dx=\frac L2 .$$

归一化常数 $\sqrt{2/L}$。频率比 $1:3:5$，$\nu_n=(2n-1)c/(4L)$。

**2.4** $X=\cos kx$ 自动满足 $X'(0)=0$；$X'(L)=-k\sin kL=0$ 给出 $k_n=n\pi/L$，$n=0,1,2,\dots$ 归一化：$n=0$ 时 $X_0=1$，常数 $\sqrt{1/L}$；$n\ge1$ 时 $\sqrt{2/L}$。零模 $k=0$、$\omega=0$ 是整体平移（或匀速平动），没有回复力。非零频率比 $1:2:3$。

**2.5** 周期边界。$X=e^{ikx}$，$e^{ikL}=1$ 给出 $k=2n\pi/L$，$n=0,\pm1,\dots$ 实数写法：$n=0$ 给常数 $1$；每个 $n\ge1$ 给 $\cos\frac{2n\pi x}{L}$ 与 $\sin\frac{2n\pi x}{L}$ 两个独立解，所以二重简并。原因：$k=\pm2n\pi/L$ 对应两个反向传播的行波，环上两个方向的波都允许。正交关系 $\int_0^LX_nX_m\,dx=\frac L2\delta_{nm}$（常数模除外）。

**2.6** (a) 0（$n\ne m$）；(b) 0（$n\ne m$）；(c) $L/2$；(d) 0（被积函数是 $\frac12\sin\frac{4\pi x}{L}$，整周期积分为零）。

**2.7** 由 2.1，$a_n=\frac{2L(-1)^{n+1}}{n\pi}$；$b_n=0$（初速为零）。所以

$$u(x,t)=\frac{2L}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\cos\omega_nt\sin\frac{n\pi x}{L}.$$

**2.8** $b_n=\frac{2}{\omega_nL}\int_0^Lv_0\sin\frac{n\pi x}{L}dx=\frac{2v_0}{n\pi\omega_n}\left(1-(-1)^n\right)$，即偶 $n$ 为零、奇 $n$ 为 $\frac{4v_0}{n\pi\omega_n}$。于是

$$u(x,t)=\frac{4v_0}{\pi}\sum_{n\ \text{奇}}\frac{1}{n\omega_n}\sin\omega_nt\sin\frac{n\pi x}{L}.$$

偶模不激发，因为常数在偶模上的投影 $\int_0^L\sin\frac{n\pi x}{L}dx=\frac{L}{n\pi}(1-(-1)^n)$ 为零。

**2.9** 帕塞瓦尔（2.5.1）：$\frac2L\int_0^Lx^2dx=\sum a_n^2$。左边 $=\frac{2L^2}{3}$；右边 $=\sum\frac{4L^2}{n^2\pi^2}=\frac{4L^2}{\pi^2}\sum\frac{1}{n^2}$。相等给出

$$\sum_{n\ge1}\frac{1}{n^2}=\frac{\pi^2}{6}.$$

**2.10** 稳态线性解 $w=U_0x/L$，初值 $v(x,0)=-U_0x/L$。由 $x/L=\frac{2}{\pi}\sum\frac{(-1)^{n+1}}{n}\sin\frac{n\pi x}{L}$：

$$u(x,t)=\frac{U_0x}{L}-\frac{2U_0}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\cos\omega_nt\sin\frac{n\pi x}{L}.$$

$t=0$ 时两项相消，$u=0$。**$t\to\infty$ 没有极限：** 无阻尼，振荡永不停止；时间是平均趋于 $\frac{U_0x}{L}$。有阻尼时才会真正趋于线性。

**2.11** 三角初值（峰 $h$ 在 $x_0=L/2$）。用 2.11 前的公式（把 $x_0$ 代入 $a_n=\frac{2hL^2}{n^2\pi^2x_0(L-x_0)}\sin\frac{n\pi x_0}{L}$）：

$$a_n=\frac{8h}{n^2\pi^2}\sin\frac{n\pi}{2}=\begin{cases}\dfrac{8h}{n^2\pi^2}(-1)^{(n-1)/2}, & n\ \text{奇}\\ 0, & n\ \text{偶}.\end{cases}$$

中点：$\sum a_n\sin\frac{n\pi}{2}=\frac{8h}{\pi^2}\sum_{n\ \text{奇}}\frac{1}{n^2}=\frac{8h}{\pi^2}\cdot\frac{\pi^2}{8}=h$。$\checkmark$

**2.12** 由 2.5.1，$q_3=A\cos\omega_3t$，其余 $q_n=0$，所以

$$E=\frac{\rho L}{4}\left[\left(\frac{dq_3}{dt}\right)^2+\omega_3^2q_3^2\right]=\frac{\rho L}{4}A^2\omega_3^2.$$

核对：$\frac{dq_3}{dt}=-A\omega_3\sin\omega_3t$，两项相加用 $\sin^2+\cos^2=1$，得 $A^2\omega_3^2$。$\checkmark$ 注意能量与 $n^2$ 成正比：高阶模存同样的位移，能量大得多。

## B 组

**2.13** $c=\sqrt{T/\rho}=\sqrt{70/4.5\times10^{-3}}=124.7\ \mathrm{m/s}$。$\nu_n=nc/2L$：

$$\nu_1=95.9\ \mathrm{Hz},\qquad \nu_2=191.9\ \mathrm{Hz},\qquad \nu_3=287.8\ \mathrm{Hz}.$$

**2.14** 弦截面 $A=\pi(0.2\times10^{-3})^2=1.26\times10^{-7}\ \mathrm{m^2}$，$EA=2.5\times10^4\ \mathrm{N}$，应变 $T/EA=2.8\times10^{-3}$。升温受约束，热应变 $-\alpha\Delta\theta=-1.2\times10^{-4}$，所以

$$\frac{\Delta T}{T}=\frac{-\alpha\Delta\theta}{T/EA}=-4.3\%,\qquad \frac{\Delta\nu}{\nu}=\frac12\frac{\Delta T}{T}=-2.15\%.$$

音分：$1200\log_2(1-0.0215)\approx-38$ 音分，超过可察觉的 5 音分约八倍。**读法：** 吉他在暖房间里偏低，正是这个符号。

**2.15** 由例 2.1 之前的公式，$a_n=\frac{2hL^2}{n^2\pi^2x_0(L-x_0)}\sin\frac{n\pi x_0}{L}$。$x_0=L/5$ 时 $\sin\frac{n\pi}{5}=0$ 对 $n=5,10,15,\dots$ 成立，这些模完全不响；$n=5$ 的节点在 $x=L/5,2L/5,\dots$，拨弦点正好落在第一个节点上。

**2.16** 闭–开管：$k_n=(2n-1)\pi/2L$，$\nu_n=(2n-1)c/4L$：

$$\nu_1=143\ \mathrm{Hz},\qquad \nu_2=429\ \mathrm{Hz},\qquad \nu_3=715\ \mathrm{Hz}.$$

两端都开：$k_n=n\pi/L$，$\nu_n=nc/2L=286n\ \mathrm{Hz}$，变成全整数倍。**读法：** 这就是单簧管（闭–开）与笛子（开–开）音色差别的来源。

**2.17** 由例 2.3 的思路（$L=1$、$a^2=1.2\times10^{-5}$），中点

$$u\Big(\frac L2,t\Big)=\frac{400}{\pi}\sum_{n\ \text{奇}}\frac{(-1)^{(n-1)/2}}{n}e^{-a^2n^2\pi^2t}.$$

$n=1$ 项为主：$\frac{400}{\pi}e^{-\lambda t}=50$ 给出 $e^{-\lambda t}=\pi/8$，$\lambda=a^2\pi^2=1.18\times10^{-4}\ \mathrm{s^{-1}}$，于是

$$t=\frac{\ln(8/\pi)}{\lambda}=7.9\times10^3\ \mathrm{s}\approx2.2\ \mathrm{h}.$$

**2.18** 由例 2.4，稳态 $u_s=\rho g x(L-x)/(2T)$，中点垂度

$$\delta=\frac{\rho gL^2}{8T}=\frac{4.5\times10^{-3}\times9.8\times0.65^2}{8\times70}=3.3\times10^{-5}\ \mathrm{m}.$$

要 $\delta=1\ \mathrm{mm}$：$T=\rho gL^2/(8\delta)=2.3\ \mathrm{N}$（或把 $L$ 加到 $3.6\ \mathrm{m}$）。**读法：** 弦的张力下降 30 倍，重力才变得重要。

**2.19** 稳态 $X/A=1/\sin(\Omega L/c)$，其中 $\Omega L/c=\pi\Omega/\omega_1$。

$$\Omega=0.9\omega_1:\ \frac{1}{|\sin0.9\pi|}=3.24;\qquad \Omega=1.9\omega_1:\ \frac{1}{|\sin1.9\pi|}=3.24.$$

两者都是 $3.24\ \mathrm{mm}$。原因：$\sin0.9\pi=\sin0.1\pi$、$\sin1.9\pi=-\sin0.1\pi$，两个驱动频率到各自共振频率（$\omega_1$ 与 $2\omega_1$）的距离都是 $0.1\omega_1$，所以放大倍数相同，只差一个符号（相位相反）。

**2.20** $\Delta\nu=\nu_1/Q=196/2000=0.098\ \mathrm{Hz}$；时间常数

$$\tau=\frac{2}{\gamma}=\frac{Q}{\pi\nu_1}=\frac{2000}{\pi\times196}=3.25\ \mathrm{s}.$$

**2.21** $\nu_{mn}=\frac c2\sqrt{m^2/a^2+n^2/b^2}=\frac{80}{2\times0.3}\sqrt{m^2+n^2}=133.3\sqrt{m^2+n^2}$：

| $(m,n)$ | $(1,1)$ | $(1,2),(2,1)$ | $(2,2)$ | $(1,3),(3,1)$ |
|---|---|---|---|---|
| $\nu$ (Hz) | 188.6 | 298.1 | 377.1 | 421.6 |
| 比值 | 1 | 1.581 | 2 | 2.236 |

**2.22** $\nu_{12}=\frac{50}{2}\sqrt{\frac{1}{0.2^2}+\frac{4}{0.201^2}}=277.3\ \mathrm{Hz}$，$\nu_{21}=279.0\ \mathrm{Hz}$，差 $0.83\ \mathrm{Hz}$，拍周期 $1/0.83=1.2\ \mathrm{s}$。

**2.23** 稳态满足 $a^2u''=-q$，两端为零：$u(x)=\frac{q}{2a^2}x(L-x)$，最高在中点

$$u_{\max}=\frac{qL^2}{8a^2}=\frac{0.5\times0.25}{8\times1.1\times10^{-4}}=142\ \mathrm{K}.$$

**2.24** 集中载荷 $F=mg$ 在 $x_0=L/2$，静平衡方程为 $Tu''=-F\delta(x-x_0)$，解是分段线性，中点位移

$$\delta=\frac{FL}{4T}=\frac{0.01\times9.8\times0.65}{4\times70}=2.3\times10^{-4}\ \mathrm{m}.$$

级数核对：$a_n=\frac{2FL}{Tn^2\pi^2}\sin\frac{n\pi}{2}$，求和得 $\frac{FL}{T\pi^2}\sum_{n\ \text{奇}}\frac{1}{n^2}=\frac{FL}{T\pi^2}\cdot\frac{\pi^2}{8}=\frac{FL}{4T}$。$\checkmark$

## C 组

**2.25** 由 2.6.2，$S_N(x)\approx\frac{2}{\pi}\mathrm{Si}(N\pi x/L)$。$\mathrm{Si}(s)$ 在 $s=\pi$ 取最大 $\mathrm{Si}(\pi)=1.8519$，所以

$$S_{\max}=\frac{2}{\pi}\mathrm{Si}(\pi)=1.1790,\qquad \text{过冲}=\frac{2}{\pi}\mathrm{Si}(\pi)-1=0.1790.$$

跳变幅度是 $2$，所以过冲占跳变的 $8.95\%$。峰值在 $N\pi x/L=\pi$，即 $x=L/N$；宽度也约为 $L/N$。$N=100$ 时峰值在 $x=0.01L$，宽度 $\approx0.01L$。

**2.26** 分部积分两次（$f$ 连续、端点为零，故边界项消失）：

$$a_n=\frac{2}{L}\int_0^Lf\sin\frac{n\pi x}{L}dx=-\frac{2L}{n^2\pi^2}\int_0^Lf''\sin\frac{n\pi x}{L}dx\propto\frac{1}{n^2}.$$

函数值：一致收敛，在角点从下方逼近，误差约 $0.4/N$（$N=40$ 约 $1\%$），**没有** 9\% 的过冲。导数：$S_N'$ 在角点附近的峰值是 $S_{\max}'=1.179\times2=2.36$（真实跳变 $\pm2$），过冲 $\frac{2.36-2}{4}=9\%$，不随 $N$ 消失。

**2.27** 稳态由两部分叠加：

$$u_p(x,t)=\frac{F_0x(L-x)}{2c^2}+\frac{A\sin(\Omega x/c)}{\sin(\Omega L/c)}\cos\Omega t .$$

检验：(i) 第一部分满足 $c^2u''=-F_0$ 且在 $x=0,L$ 为零；(ii) 第二部分满足齐次方程与 $u(0)=0$、$u(L)=A\cos\Omega t$；(iii) $\Omega\to0$ 时第二部分趋于 $Ax/L$；(iv) $\Omega=n\omega_1$ 时发散（共振）。完整解还要加上满足齐次方程与边界、抵消初始条件的瞬态项。

**2.28** 展开后零模方程 $T_0'=F_0$，给出 $T_0=F_0t$；其余

$$T_n'+\frac{a^2n^2\pi^2}{L^2}T_n=F_n\quad\Longrightarrow\quad T_n\to\frac{F_n}{a^2k_n^2}\ (\text{稳态}).$$

所以

$$u(x,t)=F_0t+\sum_{n\ge1}\frac{F_n}{a^2k_n^2}\left(1-e^{-a^2k_n^2t}\right)\cos\frac{n\pi x}{L}.$$

没有稳态：平均温度按 $F_0t$ 一直上升，热量只进不出。几何形状趋于稳定，整体温度在漂移。

**2.29** 变密度弦：$\rho_0(1+x/L)\frac{\partial^2u}{\partial t^2}=T\frac{\partial^2u}{\partial x^2}$。设 $u=XT$：

$$\frac{T''}{T}=\frac{T}{\rho_0(1+x/L)}\frac{X''}{X}=-\omega^2\quad\Longrightarrow\quad X''+\frac{\rho_0\omega^2}{T}\left(1+\frac xL\right)X=0 .$$

这是施图姆–刘维尔形式：$(pX')'+\lambda wX=0$，其中 $p=T$、$w=\rho_0(1+x/L)$、$\lambda=\omega^2$。系数随 $x$ 变，本征函数不是正弦（是艾里型函数），正交性的权重是 $w=\rho(x)$：$\int_0^L\rho(x)X_nX_m\,dx=0$。**读法：** 弦越粗的地方「惯性越大」，本征函数向细端偏移。

**2.30** 三角初值（峰 $h$ 在 $L/2$）：$a_n=\frac{8h}{n^2\pi^2}\sin\frac{n\pi}{2}$，$n$ 奇。能量 $E_n\propto\omega_n^2a_n^2\propto n^2\cdot\frac{1}{n^4}=\frac{1}{n^2}$。总和中 $\sum_{n\ \text{奇}}\frac{1}{n^2}=\frac{\pi^2}{8}$，所以

$$n=1:\ \frac{8}{\pi^2}=81.1\%,\qquad n=3:\ 9.0\%,\qquad n=5:\ 3.2\%.$$

**读法：** 八成以上的能量在基模，泛音按 $1/n^2$ 递减，所以拨弦的声音「圆润」；若用方波型初值（$a_n\propto1/n$，能量 $\propto1/n^2$ 但系数分布更宽）或拨在靠近端点处，高频比例会明显上升，音色变尖。

**2.31** $\tan\varphi=\frac{\gamma\Omega}{\omega_1^2-\Omega^2}$。取 $\gamma=0.05\omega_1$：

$$\Omega=0.9\omega_1:\ \tan\varphi=\frac{0.045}{0.19}=0.237,\quad \varphi=13.3^\circ;$$

$$\Omega=1.1\omega_1:\ \tan\varphi=\frac{0.055}{-0.21}=-0.262,\quad \varphi=165.3^\circ.$$

$\Omega=\omega_1$ 时分母为零，$\tan\varphi\to\infty$，$\varphi=90^\circ$：响应恰好落后四分之一周期，速度与驱动力同相，功率 $F\cdot v$ 最大。

**2.32** $a_n=\frac2L\int_0^L\cos\frac{\pi x}{L}\sin\frac{n\pi x}{L}dx$。用积化和差，$n$ 奇时两项都是整周期余弦，积分为零；$n$ 偶时

$$a_n=\frac{4n}{\pi(n^2-1)},\qquad n=2,4,6,\dots$$

只有偶 $n$：因为 $\cos(\pi x/L)$ 的奇延拓在 $x=0$ 从 $-1$ 跳到 $+1$，对称性只允许偶模。按 $1/n$ 衰减：端点跳变（2.6.1）。$x=L/2$ 处 $\sin\frac{n\pi}{2}=0$（$n$ 偶），级数为零，而 $\cos\frac{\pi}{2}=0$，两边一致。$\checkmark$

## 概念与判断

**2.33** 错。需要 $f$ 连续**且**周期延拓后连续（端点值匹配），再假定分段光滑。反例：$f=1$ 在 $(0,L)$ 上，端点跳变，部分和过冲 9\%，不一致收敛。

**2.34** 错。必须同一方程、同一边界条件、同一权重。反例：$\sin\frac{\pi x}{L}$（两端固定）与 $\sin\frac{3\pi x}{2L}$（固定–自由）都满足 $X''+k^2X=0$，但 $\int_0^L\sin\frac{\pi x}{L}\sin\frac{3\pi x}{2L}dx=0.255\ne0$。

**2.35** 错。先齐次化：取满足非齐次边界的 $w$（线性插值最常用），令 $v=u-w$，$v$ 满足齐次边界。代价是方程多出源项 $-\frac{\partial^2w}{\partial t^2}$、初值被平移，别忘把 $w$ 加回去。

**2.36** 错。线性无阻尼时振幅按 $\frac{F_n}{2\omega_n}t$ 线性增长，不是无穷大；有阻尼时峰值是 $\frac{F_n}{\gamma\omega_n}$；真实上限由非线性（大振幅使张力变大、频率上移、自动失谐）或材料破坏决定。

**2.37** 错。吉布斯过冲的极限是跳变的 $8.95\%$，与 $N$ 无关；$N$ 增大只让过冲区域变窄（宽度 $L/N$）。要消除它，只能改初值（让它连续），不能靠多取项。

**2.38** 错。简并来自对称性：$a=b$ 时 $(1,2)$ 与 $(2,1)$ 的 $m^2+n^2$ 都等于 5。$a\ne b$ 时（哪怕差 1\%）频率就劈开，出现拍。

**2.39** 对。零频模 $X_0=1$ 是整根弦的平移（或匀速平动），没有回复力，$\omega=0$。两端固定时位移被钉住，$X(0)=0$ 把常数解排除，所以没有零模。**物理差别：** 自由弦可以整体「飘走」，固定弦不行；这也是诺伊曼问题可解性条件（净力必须为零）的来源。

**2.40** 错。展开后 $F_n=\frac{2}{L}\int_0^LF_0\sin\frac{3\pi x}{L}\sin\frac{n\pi x}{L}dx=F_0\delta_{n3}$，只有 $n=3$ 的方程右端非零，其余模满足齐次方程（初始静止就始终为零）。**读法：** 力的空间形状就是它能激发的模态形状，这就是模态控制的原理。

## 第 3 章

> 每题给关键一步、中间结果与最终答案。缺的步骤请自己补全后再看。

**3.1** 由 $r^2=x^2+y^2$ 与 $\tan\varphi=y/x$ 求导：

$$\frac{\partial r}{\partial x}=\frac{x}{r}=\cos\varphi,\qquad
\frac{\partial\varphi}{\partial x}=-\frac{y}{r^2}=-\frac{\sin\varphi}{r},\qquad
\frac{\partial r}{\partial y}=\sin\varphi,\qquad
\frac{\partial\varphi}{\partial y}=\frac{\cos\varphi}{r}.$$

于是 $\cos^2\varphi+\sin^2\varphi=1$，以及 $\sin^2\varphi/r^2+\cos^2\varphi/r^2=1/r^2$。**第二个式子说明「角度的梯度」量纲是 1/长度，那个 $1/r$ 就是弧长的账。**

**3.2**

$$\nabla^2(r^2)=\frac{1}{r}\frac{\mathrm{d}}{\mathrm{d}r}\left(r\cdot2r\right)=4,$$

$$\nabla^2(\ln r)=\left(-\frac{1}{r^2}\right)+\frac{1}{r}\cdot\frac{1}{r}=0,$$

$$\nabla^2(r\cos\varphi)=\frac{1}{r}\frac{\partial}{\partial r}\left(r\cos\varphi\right)+\frac{1}{r^2}\frac{\partial^2}{\partial\varphi^2}\left(r\cos\varphi\right)
=\frac{\cos\varphi}{r}-\frac{\cos\varphi}{r}=0.$$

第三个式子的结果与 $x=r\cos\varphi$ 是调和函数一致。

**3.3** 方程除以 $x$ 后乘 $x$ 整理（即直接提取全导数）：

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(x\frac{\mathrm{d}y}{\mathrm{d}x}\right)+\left(x-\frac{m^2}{x}\right)y=0 .$$

与 $\frac{\mathrm{d}}{\mathrm{d}x}\left(p\frac{\mathrm{d}y}{\mathrm{d}x}\right)+(q+\lambda w)y=0$ 对比：$p=x$、$q=-m^2/x$、$\lambda=1$、$w=x$。**权重是 $x$，因为把方程前两项凑成 $\frac{\mathrm{d}}{\mathrm{d}x}\left(x\frac{\mathrm{d}y}{\mathrm{d}x}\right)$ 时必须乘的那个因子就是 $x$。** 若把方程整体除以 $x$，权重变成 1，但那时 $p=1$、$q$ 与 $w$ 都随之改变，正交性的权重仍等价于 $x$。

**3.4** 逐项：$J_0(1)=1-0.25+0.015625-0.000434+0.000005=0.7652$，与表值一致。

$x=2.4$ 时各项是

$$1-1.44+0.5184-0.08294+0.007465-0.000430+0.0000172=0.002508 .$$

与表值 $0.0025$ 一致。**注意前四项还在 $10^{-2}$ 量级，最终结果却是 $10^{-3}$，靠的是 $10^{-2}$ 量级的相消。** 所以 $x$ 再大一些就不能用级数直接算（有效数字被吃光），要改用渐近式。

**3.5** 由递推 $J_0'=-J_1$，$J_0$ 的极值点在 $J_1$ 的零点：$x=3.8317$、$7.0156$、$10.1735$。相应极值为 $J_0=-0.4028$、$+0.3001$、$-0.2497$。**极值交替变号、幅度按 $1/\sqrt{x}$ 衰减**（$0.4028\to0.3001\to0.2497$）。

**3.6** 用 $J_{m+1}=\frac{2m}{x}J_m-J_{m-1}$：

$$J_2(2)=\frac{2\cdot1}{2}J_1(2)-J_0(2)=0.5767-0.2239=0.3528,$$

$$J_3(2)=\frac{2\cdot2}{2}J_2(2)-J_1(2)=2(0.3528)-0.5767=0.1289 .$$

**3.7** 渐近式给 $2.356$、$5.498$、$8.639$，真值 $2.405$、$5.520$、$8.654$，相对误差

$$2.0\%,\qquad0.40\%,\qquad0.17\% .$$

误差大致按 $1/n^2$ 下降（$2.0/0.40\approx5$，$0.40/0.17\approx2.4$，与 $(2/1)^2=4$、$(3/2)^2=2.25$ 同量级）。$n=3$ 时三位有效数字已经够用。

**3.8** 公共因子 $c/(2\pi a)=30/(2\pi\times0.2)=23.87\ \text{Hz}$：

$$f_{0,1}=57.4\ \text{Hz},\quad f_{1,1}=91.5\ \text{Hz},\quad f_{2,1}=122.6\ \text{Hz},\quad f_{0,2}=131.8\ \text{Hz}.$$

比值 $1:1.593:2.136:2.295$。**与整数比无关，所以这面膜没有明确音高。**

**3.9** 用 3.7.4 节的归一化：

$$\int_0^a rJ_0^2\!\left(j_{0,1}\frac{r}{a}\right)\mathrm{d}r=\frac{a^2}{2}J_1^2(j_{0,1})
=\frac{a^2}{2}(0.51915)^2=0.1348\,a^2 .$$

**3.10** $c/(2\pi a)=3\times10^{8}/(2\pi\times0.02)=2.387\ \text{GHz}$：

$$f_c(\mathrm{TM}_{01})=2.4048\times2.387=5.74\ \text{GHz},\qquad
f_c(\mathrm{TE}_{11})=1.8412\times2.387=4.39\ \text{GHz}.$$

**TE 模比 TM 模低**，因为 $J_m'$ 的首零比 $J_m$ 的小。

**3.11** $\ln(a/b)=\ln4=1.386$，

$$C=\frac{2\pi\varepsilon_0}{\ln4}=4.01\times10^{-11}\ \text{F/m}=40.1\ \text{pF/m}.$$

**只依赖比值 $a/b$**：同轴线整体做细，电容不变。

**3.12** 由 $\frac{\mathrm{d}J_0}{\mathrm{d}x}=-J_1$ 再求一次导：

$$\frac{\mathrm{d}^2J_0}{\mathrm{d}x^2}=-\frac{\mathrm{d}J_1}{\mathrm{d}x}
=-\left(J_0-\frac{J_1}{x}\right)=-J_0+\frac{J_1}{x}.$$

而 $\frac{1}{x}\frac{\mathrm{d}J_0}{\mathrm{d}x}=-\frac{J_1}{x}$。两项相加，$\pm J_1/x$ 抵掉，只剩 $-J_0$，即

$$\frac{\mathrm{d}^2J_0}{\mathrm{d}x^2}+\frac{1}{x}\frac{\mathrm{d}J_0}{\mathrm{d}x}+J_0=0 .$$

**这说明贝塞尔方程不是凭空来的：它等价于两条一阶递推。** 反过来，从方程加上递推也能重建全部 $J_m$。

**3.13** 由 $\frac{1}{r}\frac{\mathrm{d}}{\mathrm{d}r}\left(r\frac{\mathrm{d}V}{\mathrm{d}r}\right)=0$ 得 $V=A\ln r+B$。边界 $V(b)=0$、$V(a)=100\ \text{V}$：

$$A=\frac{100}{\ln3}=91.0,\qquad V(r)=91.0\ln\frac{r}{0.01},$$

$$E(r)=-\frac{\mathrm{d}V}{\mathrm{d}r}=-\frac{91.0}{r}\ \text{V/m},\qquad E(0.02)=-4.55\ \text{kV/m}.$$

负号表示场指向内柱。

**3.14** $c/(2\pi a)=55/(2\pi\times0.33)=26.53\ \text{Hz}$：

$$f_{0,1}=63.8,\quad f_{1,1}=101.6,\quad f_{2,1}=136.2,\quad f_{0,2}=146.4\ \text{Hz}.$$

最小间隔是 $(2,1)$ 与 $(0,2)$ 之间的 $10.2\ \text{Hz}$。**这正是「$j_{2,1}$ 与 $j_{0,2}$ 交错」的直接后果（3.6.2 节）。**

**3.15** （a）中心 $r_0=0$：$J_m(0)=0$ 对一切 $m\geq1$，所以系数为零，只剩 $m=0$。（b）边界 $r_0=a$：$J_m(j_{m,n})=0$ 对一切 $m,n$，所有系数为零，什么都不响——因为边界被固定死了。两个结论用的都是 $J_m$ 的零点，一个在原点、一个在 $x=j_{m,n}$。

**3.16** 初位移正好是一个模式，所以只有一项：

$$u(r,t)=u_0J_0\!\left(j_{0,1}\frac{r}{a}\right)\cos(\omega_{0,1}t),\qquad \omega_{0,1}=\frac{cj_{0,1}}{a}.$$

中心点 $J_0(0)=1$，所以 $u(0,t)=u_0\cos\omega_{0,1}t$——**中心点振幅最大，且没有节圆通过它。**

**3.17** $f_{0,3}=\frac{c\,j_{0,3}}{2\pi a}=\frac{30\times8.6537}{2\pi\times0.2}=206.6\ \text{Hz}$。

节圆半径 $r_k=a\,j_{0,k}/j_{0,3}$：$r_1=0.2779a=5.56\ \text{cm}$，$r_2=0.6379a=12.76\ \text{cm}$。

**模有两个节圆、没有节线**，所以图样是同心的三圈（内正、中负、外正）。

**3.18** 强度因子 $J_m(j_{m,1}r_0/a)$，$r_0/a=0.7$：

$$J_0(1.683)=0.408,\qquad J_1(2.682)=0.447,\qquad J_2(3.595)=0.446 .$$

以 $(1,1)$ 归一：$(0,1):(1,1):(2,1)=0.91:1:1.00$。

**读法：** $0.7a$ 处三个模式几乎等强，所以敲出来的音色最「杂」；越靠外，低阶模式越弱，声音越尖。

**3.19**

$$T(0)=T_s+\frac{q_Va^2}{4\kappa}=300+\frac{2\times10^{8}\times25\times10^{-6}}{12}=300+417=717\,^\circ\text{C}.$$

半径加倍：$T(0)-T_s\propto a^2$，变成 $1667\ \text{K}$，即 $1967\,^\circ\text{C}$，早已超过铀的熔点。

**3.20** 区域 $b<r<a$ 不含原点，通解 $R=AJ_0(kr)+BY_0(kr)$，两个边界条件给出

$$J_0(kb)Y_0(ka)-J_0(ka)Y_0(kb)=0 .$$

数值求根（$b=0.5a$）得最低根 $ka=6.246$，于是

$$\frac{f_{\text{环}}}{f_{\text{实心}}}=\frac{6.246}{2.4048}=2.60 .$$

**中间挖掉一半半径，基频升到 2.6 倍**：环形膜面积小、约束多，更「硬」。

**3.21** $c=\frac{2\pi af}{j_{0,1}}=\frac{2\pi\times0.35\times60}{2.4048}=54.9\ \text{m/s}$。此时

$$f_{1,1}=\frac{3.8317\times54.9}{2\pi\times0.35}=95.7\ \text{Hz}.$$

**放松鼓皮把基频降下来，所有模式按同一比例降，音程关系不变**（3.6.5 节）。

**3.22** 内部解 $T=300+20(r/a)^2\cos2\varphi$（例 3.5）。$r=0.5a$ 时 $(r/a)^2=0.25$：

$$T(0.05,\varphi)=300+5\cos2\varphi .$$

最高 $305\ \text{K}$、最低 $295\ \text{K}$。

**表面 $20\ \text{K}$ 的起伏到半径一半处只剩 $5\ \text{K}$**，按 $(r/a)^2$ 衰减。

**3.23** 取 $t=ie^{i\varphi}$，母函数左边为 $e^{ix\cos\varphi}$，右边为 $\sum_mJ_m(x)i^me^{im\varphi}$：

$$e^{ikr\cos\varphi}=\sum_{m=-\infty}^{\infty}i^mJ_m(kr)e^{im\varphi}.$$

$ka=1$：$|J_0|=0.765$、$|J_1|=0.440$、$|J_2|=0.115$，比值 $1:0.58:0.15$。
$ka=10$：$|J_0|=0.246$、$|J_1|=0.044$、$|J_2|=0.255$，比值 $1:0.18:1.04$。

**读法：** $ka\ll1$ 时只有 $m=0,1$ 两个分量有分量，对应瑞利散射的「偶极 + 单极」角分布；$ka\gg1$ 时高阶项与 $m=0$ 同量级，必须算很多阶（米氏级数收敛慢）。**「需要几阶」由 $ka$ 决定，不由 $m$ 决定。**

**3.24** 由 $\int zJ_0\,\mathrm{d}z=zJ_1$（因为 $\frac{\mathrm{d}}{\mathrm{d}z}(zJ_1)=zJ_0$）：

$$\int_0^aJ_0\!\left(j_{0,1}\frac{r}{a}\right)r\,\mathrm{d}r
=\frac{a^2}{j_{0,1}}J_1(j_{0,1})=\frac{0.51915}{2.4048}a^2=0.2159\,a^2 .$$

圆盘上「权重为 1」的平均值是 $a^2/2=0.5a^2$，所以振幅加权的平均位移是峰值的 $0.2159/0.5=0.432$。

**读法：** 基模的平均位移只有峰值的 $43\%$，因为 $J_0$ 在边缘附近迅速掉到零。**用「平均位移」估计峰值会低估一倍多。**

**3.25** 级数中 $x^{2k-m}/k!(k-m)!$ 在 $m\to-m$ 时给出 $(-1)^m$ 的额外因子，故 $J_{-m}=(-1)^mJ_m$，两者线性相关。二阶方程需要两个独立解，于是必须引入含对数项的第二解 $Y_m$；它在原点发散（3.5.2 节）。**整数阶是「例外」，非整数阶时 $J_{\pm m}$ 本来就独立。**

**3.26** 在 $r=0.5a$、$\cos m\varphi=1$ 方向：

$$J_1\!\left(\frac{j_{1,1}}{2}\right)=J_1(1.916)=0.581,\qquad
J_2\!\left(\frac{j_{2,1}}{2}\right)=J_2(2.568)=0.455,$$

比值 $0.455/0.581=0.78$。**两者接近，说明 $0.5a$ 处敲击会同时激发这两个模式；要强调 $(2,1)$ 得往更外侧敲，要强调 $(1,1)$ 则在 $0.4a$ 附近最有效。**

**3.27** 同面积：$\pi a^2=L^2$，$L=a\sqrt{\pi}$。方膜基频 $\omega_\square=c\pi\sqrt{2}/L=c\sqrt{2\pi}/a$，圆膜 $\omega_\bigcirc=2.4048c/a$：

$$\frac{f_\bigcirc}{f_\square}=\frac{2.4048}{\sqrt{2\pi}}=0.959 .$$

**圆膜比方膜低 4%**：圆形边界「更松」，同样面积下约束少一点。

**3.28** 单位长度散热量

$$\frac{Q}{L}=\frac{2\pi(T_i-T_\infty)}{\dfrac{\ln(a/r_i)}{\kappa}+\dfrac{1}{ha}} .$$

令分母对 $a$ 的导数为零：$\frac{1}{\kappa a}-\frac{1}{ha^2}=0$，得临界半径

$$a_c=\frac{\kappa}{h}=\frac{0.15}{10}=15\ \text{mm}.$$

**当芯半径小于 $15\ \text{mm}$ 时，加保温层反而增大散热**（外表面面积增加带来的对流增益超过导热热阻）。细导线包保温层「更凉」就是这个原因。

**3.29** 先求场：$E_r=-\frac{\partial V}{\partial r}=E_0\cos\varphi\left(1+\frac{a^2}{r^2}\right)$。在 $r=a$ 处 $E_r=2E_0\cos\varphi$，所以

$$\sigma(\varphi)=\varepsilon_0E_r(a)=2\varepsilon_0E_0\cos\varphi .$$

$\varphi=0$（外场指来的一侧）带正电，$\varphi=\pi$ 带负电，两侧各半。

**验算：** 感应电荷的总量为零（$\int_0^{2\pi}\cos\varphi\,\mathrm{d}\varphi=0$），符合「接地导体不净带电」。

**3.30** $T(0)-T_s=\dfrac{q_Va^2}{4\kappa}$。

$q_V\to2q_V$、$a\to2a$：分子变成 $2\times4=8$ 倍，**温升 8 倍**。只把 $\kappa$ 减半：**温升 2 倍**。

**这就是「功率密度与尺寸不能同时放大」的定量版本**：燃料棒半径加一倍，中心温度不是加倍而是八倍。

**3.31** 错。「位移为零」是瞬时的：$u=0$ 也可能只是 $\cos\omega t=0$ 的时刻，全膜同时过零。节线的定义是**恒为零**，即空间因子在那一点为零。判据：换一个时刻再看，若还是零才是节线。

**3.32** 错。$r=0$ 根本不在同轴电缆的求解区域里，「在原点有限」这个要求无从谈起；更重要的是二阶方程需要两个边界条件（$r=b$ 与 $r=a$），只有两个独立解才凑得出非零解。舍掉 $Y_m$ 会得到「一个常数满足两个条件」，一般无解。

**3.33** 需要修正。$m$ 是角向的**量子数**（整数），但局部的「每米波数」是 $m/r$：固定 $\Delta\varphi$ 时弧长是 $r\Delta\varphi$，所以 $\varphi$ 方向的局部波长是 $2\pi r/m$，随 $r$ 增大而变长。**这就是径向方程里 $m^2/r^2$ 那一项的物理含义：离心项。**

**3.34** 错。高阶零点间距趋于 $\pi$，对应频率间距 $\Delta f=c/(2a)$；而基频是 $2.4048c/(2\pi a)=0.3828c/a$。比值 $\Delta f/f_{0,1}=1.306$ 不是整数，所以「等间距」不等于「谐波列」。**等间距只是说相邻峰的距离固定，与基频成不成整数比是另一件事。**

**3.35** 不同意。两条理由：（1）数学上它来自把方程乘 $r$ 凑成自伴形式 $\frac{\mathrm{d}}{\mathrm{d}r}\left(r\frac{\mathrm{d}R}{\mathrm{d}r}\right)+\cdots$，系数 $r$ 就是施图姆–刘维尔权重；（2）物理上 $r\,\mathrm{d}r\,\mathrm{d}\varphi$ 是面积元，正交性说的是两个模式在面积上的交叉项为零。**两条理由其实是同一件事：拉普拉斯算子关于面积元自伴。**

**3.36** 错。$\sin(n\pi r/a)$ 是「两端为零」的本征函数族，与 $J_0(j_{0,1}r/a)$ 属于不同的边界条件与不同的算子，两者在 $[0,a]$ 上（带权 $r$）并不正交。硬展开虽然形式上可以（完备性），但系数不衰减得快，边界附近还必然出现 吉布斯型振荡。**要展开就必须用同一族本征函数。**

**3.37** 错。$m\geq1$ 的模式在中心为零：$J_m(0)=0$。例如 $(1,1)$ 模中心是节线上的点（一条直径穿过中心），位移在中心恒为零。**只有 $m=0$ 的模式在中心取极值。**

**3.38** 错。环形区域不含 $r=0$，径向通解是 $AJ_0(kr)+BY_0(kr)$，两个边界条件给出特征方程

$$J_0(kb)Y_0(ka)-J_0(ka)Y_0(kb)=0 .$$

$b=0.5a$ 时最低根 $ka=6.246$，是实心膜 $j_{0,1}=2.405$ 的 $2.60$ 倍。**用 $j_{0,1}$ 会把基频算低一半以上。**

**3.39** 错（对 $m=0$ 而言）。因为 $\frac{\mathrm{d}J_0}{\mathrm{d}x}=-J_1$，$J_0'$ 的零点就是 $J_1$ 的零点：

$$j'_{0,n}=j_{1,n}=3.8317,\ 7.0156,\ 10.1735,\dots$$

**是同一张表，只是换了名字。** 但 $m\geq1$ 的 $j'_{m,n}$ 不能这样换（只有 $j'_{1,n}=j_{2,n}$ 这类特殊关系），要单独查。

## 第 4 章

**4.1** 由 $P_4=\dfrac{1}{2^44!}\dfrac{\mathrm{d}^4}{\mathrm{d}x^4}(x^2-1)^4$，而 $(x^2-1)^4=x^8-4x^6+6x^4-4x^2+1$。求四阶导得 $1680x^4-1440x^2+144$，除以 $16\cdot24=384$：

$$P_4=\frac{35x^4-30x^2+3}{8}.$$

$P_4(1)=(35-30+3)/8=1$，$P_4(-1)=(35-30+3)/8=1$。两端的值相等，因为 $l=4$ 是偶数，$P_4$ 是偶函数。

**4.2** 第一个积分：$l=2\ne4$，由正交性直接得 $\int_{-1}^1P_2P_4\,\mathrm{d}x=0$。

第二个：用 $x^2=\frac13P_0+\frac23P_2$（4.5.3 的结果），

$$\int_{-1}^{1}x^2P_2\,\mathrm{d}x=\frac23\int_{-1}^{1}P_2^2\,\mathrm{d}x=\frac23\cdot\frac25=\frac{4}{15}.$$

这里用了归一化 $\int P_2^2=2/5$，$P_0P_2$ 项由正交性为零。

**4.3** $f=|x|$ 是偶函数，只有偶 $l$ 的系数非零：

$$c_l=\frac{2l+1}{2}\cdot2\int_0^1xP_l(x)\,\mathrm{d}x=(2l+1)\int_0^1xP_l\,\mathrm{d}x .$$

$c_0=\int_0^1x\,\mathrm{d}x=\frac12$；$c_2=5\int_0^1x\frac{3x^2-1}{2}\,\mathrm{d}x=5\left(\frac38-\frac14\right)=\frac58$；$c_4=9\int_0^1x\frac{35x^4-30x^2+3}{8}\,\mathrm{d}x=9\left(\frac{35}{48}-\frac{15}{16}+\frac{3}{16}\right)=-\frac{3}{16}$。

$$|x|=\frac12+\frac58P_2(x)-\frac{3}{16}P_4(x)+\cdots$$

读法：所有系数同号交替且按 $l^{-2}$ 衰减（$f$ 连续但导数在 $0$ 处跳跃），所以收敛不慢也不快。

**4.4** 由 $P_2=(3\cos^2\theta-1)/2$ 反解：

$$\cos^2\theta=\frac{1+2P_2(\cos\theta)}{3}=\frac13P_0+\frac23P_2 .$$

$c_0=1/3$，$c_2=2/3$，其余为零。$\cos^2\theta$ 是二次多项式，$l>2$ 的矩必为零——多项式展开一定截断。

**4.5** $P_3=\frac12(5x^3-3x)=\frac{x}{2}(5x^2-3)=0$，得 $x=0$ 或 $x=\pm\sqrt{3/5}=\pm0.7746$。

$$\theta=90^\circ,\qquad \theta=\arccos 0.7746=39.2^\circ,\qquad \theta=180^\circ-39.2^\circ=140.8^\circ .$$

三条节锥（$\theta$ 为常数的纬线圈）把球面分成四条纬度带，每带内 $P_3$ 的符号不变。

**4.6** 由 $Y_{20}=\sqrt{5/16\pi}(3\cos^2\theta-1)$、$Y_{22}=\sqrt{15/32\pi}\sin^2\theta e^{2i\varphi}$，取实组合 $(Y_{22}+Y_{2,-2})/\sqrt2$：

$$Y_{20}=\sqrt{\frac{5}{16\pi}}\frac{3z^2-r^2}{r^2},\quad Y_{21}^{c}=\sqrt{\frac{15}{4\pi}}\frac{xz}{r^2},\quad Y_{21}^{s}=\sqrt{\frac{15}{4\pi}}\frac{yz}{r^2},$$
$$Y_{22}^{c}=\sqrt{\frac{15}{16\pi}}\frac{x^2-y^2}{r^2},\quad Y_{22}^{s}=\sqrt{\frac{15}{4\pi}}\frac{xy}{r^2}.$$

正交性验证：$\int Y_{20}Y_{22}^{c}\,\mathrm{d}\Omega\propto\int_{-1}^1(3u^2-1)(1-u^2)\,\mathrm{d}u\cdot\int_0^{2\pi}\cos2\varphi\,\mathrm{d}\varphi$。第二个因子为零，所以整个积分为零。**一般规律：两个球谐的方位角部分若一个是常数（$m=0$）而另一个含 $\cos m\varphi$ 或 $\sin m\varphi$（$m\ne0$），对 $\varphi$ 的积分必然为零，与极角部分无关。**

**4.7** 设 $Y=N\cos\theta$（$P_1^0=\cos\theta$）。归一化：

$$1=N^2\int\cos^2\theta\,\mathrm{d}\Omega=N^2\cdot2\pi\int_{-1}^{1}u^2\,\mathrm{d}u=N^2\cdot\frac{4\pi}{3},$$

所以 $N=\sqrt{3/4\pi}$，即 $Y_{10}=\sqrt{3/4\pi}\cos\theta$。$N$ 是实数且取正，相位约定只剩一个符号自由度。

**4.8** 记 $f(r)=p/(4\pi\varepsilon_0r^2)$，则 $\Phi=f(r)\cos\theta$。角向部分是 $l=1$ 的本征函数，$\nabla^2_{\Omega}\cos\theta=-2\cos\theta$。于是

$$\nabla^2\Phi=\cos\theta\frac{1}{r^2}\frac{\mathrm{d}}{\mathrm{d}r}\left(r^2\frac{\mathrm{d}f}{\mathrm{d}r}\right)+f\frac{\nabla^2_{\Omega}\cos\theta}{r^2} .$$

$f\propto r^{-2}$ 给 $\frac{1}{r^2}(r^2f')'=2/r^4$，第二项是 $-2f/r^2=-2/r^4$，两项相消：$\nabla^2\Phi=0$（$r\ne0$）。

**4.9** 由 $j_0=\sin x/x$ 与 $j_1=\sin x/x^2-\cos x/x$，用小 $x$ 的泰勒展开：

$$j_0(x)=1-\frac{x^2}{6}+\frac{x^4}{120}-\cdots,\qquad j_1(x)=\frac{x}{3}-\frac{x^3}{30}+\cdots$$

两者在小 $x$ 时分别按 $x^0$ 与 $x^1$ 起头，与一般式 $j_l\approx x^l/(2l+1)!!$ 一致（$1!!=1$，$3!!=3$）。

**4.10** $V=V_0P_1$ 只含 $l=1$。球内留 $r^1$：$\Phi_{\mathrm{in}}=V_0(r/a)\cos\theta$；球外留 $r^{-2}$：$\Phi_{\mathrm{out}}=V_0(a/r)^2\cos\theta$。两式在 $r=a$ 都回到 $V_0\cos\theta$，在各自的奇点（原点、无穷远）行为正确。

**4.11** $|Y_{10}|^2=\frac{3}{4\pi}\cos^2\theta$，$|Y_{1,\pm1}|^2=\frac{3}{8\pi}\sin^2\theta$，两者相加

$$\frac{3}{4\pi}\cos^2\theta+2\cdot\frac{3}{8\pi}\sin^2\theta=\frac{3}{4\pi}\left(\cos^2\theta+\sin^2\theta\right)=\frac{3}{4\pi},$$

与加法公式在 $\gamma=0$ 处给出的 $\frac{2l+1}{4\pi}=\frac{3}{4\pi}$ 一致。**这就是「三个 p 轨道加起来各向同性」。**

**4.12** $\int P_2^2\,\mathrm{d}x=2/5$，而

$$\int_{-1}^{1}x^2P_2^2\,\mathrm{d}x=\frac14\int_{-1}^{1}\left(9x^6-6x^4+x^2\right)\mathrm{d}x=\frac14\left(\frac{18}{7}-\frac{12}{5}+\frac23\right)=\frac{22}{105} .$$

$$\langle\cos^2\theta\rangle=\frac{22/105}{2/5}=\frac{11}{21}\approx0.524 .$$

与 $l=2,m=0$ 的一般公式 $\dfrac{2l^2+2l-1}{(2l-1)(2l+3)}=\dfrac{11}{21}$ 一致。

**4.13** 由 $\Phi_g=-\frac{GM}{r}[1-J_2(a/r)^2P_2]$ 得 $g=-\partial\Phi_g/\partial r=-\frac{GM}{r^2}[1-3J_2(a/r)^2P_2]$。在 $r=a$：极地 $P_2=1$，$|g|=\frac{GM}{a^2}(1-3J_2)$；赤道 $P_2=-\frac12$，$|g|=\frac{GM}{a^2}(1+\frac32J_2)$。相对差

$$\frac{\Delta g}{g}\approx4.5J_2=4.9\times10^{-3},$$

$GM/a^2=9.80\ \mathrm{m/s^2}$，故 $\Delta g\approx0.048\ \mathrm{m/s^2}$。实测 $0.052$，余下部分来自自转与扁率。

**4.14** $r=7000\ \mathrm{km}$，$(a/r)^2=(6378/7000)^2=0.830$。$J_2$ 项对 $g$ 的相对贡献是 $3J_2(a/r)^2P_2$：极地 $2.7\times10^{-3}$，赤道 $-1.35\times10^{-3}$。也就是千分之一到千分之三——对精确定轨必须算，对粗略估算可以当球。
**4.15** 偶极轴上（$\theta=0$）的场强是 $E=2p/(4\pi\varepsilon_0r^3)$：

$$E=\frac{2\times8.99\times10^9\times6.2\times10^{-30}}{(10^{-9})^3}=1.1\times10^{8}\ \mathrm{V/m},$$

$$\Phi=\frac{p}{4\pi\varepsilon_0r^2}=\frac{8.99\times10^9\times6.2\times10^{-30}}{10^{-18}}=5.6\times10^{-2}\ \mathrm{V}.$$

$10^8\ \mathrm{V/m}$ 是强场（空气击穿约 $3\times10^6\ \mathrm{V/m}$），说明极性分子在纳米尺度上能强烈扰动周围。注意 $r=1\ \mathrm{nm}$ 已是分子尺寸的十倍，点偶极近似勉强可用。

**4.16** 介质球内场 $E_{\mathrm{in}}=3E_0/(\varepsilon_r+2)$。$\varepsilon_r=80$ 给

$$\frac{E_{\mathrm{in}}}{E_0}=\frac{3}{82}=0.037 .$$

球内场被压到 $3.7\%$，等价于库仑相互作用除以 $80$——这就是水的高介电常数对电解质溶液的作用。

**4.17** 球心电势等于球面平均：$\Phi(0)=V_0/2$。北极点按边界条件应为 $V_0$。但级数在极点收敛很慢：系数 $c_l\sim l^{-1/2}$，部分和按 $N^{-1/2}$ 逼近，$N=19$ 时只到 $0.82V_0$、$N=39$ 时 $0.875V_0$。**要算极点附近的电势，别用级数，直接用边界值。**

**4.18** $\langle r\rangle=\frac32a_0=0.79\ \text{Å}$，$\langle r^2\rangle=3a_0^2$，最概然半径 $r_{\mathrm{mp}}=a_0$（由 $\frac{\mathrm{d}}{\mathrm{d}r}(r^2e^{-2r/a_0})=0$ 得）。涨落

$$\Delta r=\sqrt{\langle r^2\rangle-\langle r\rangle^2}=\sqrt{3-2.25}\,a_0=0.87a_0 .$$

$\Delta r$ 与 $\langle r\rangle$ 同量级，说明「轨道半径」只有统计意义。

**4.19** $2p$ 的径向概率 $\propto r^4e^{-r/a_0}$。由 $\frac{\mathrm{d}}{\mathrm{d}r}(r^4e^{-r/a_0})=0$ 得 $4r^3=r^4/a_0$，即 $r_{\mathrm{mp}}=4a_0$。$1s$ 是 $a_0$，比值 $4=n^2$——主量子数越大，电子云的整体尺度按 $n^2$ 增长。

**4.20** 令 $13.6/(n^*)^2=5.14$，得 $n^*=\sqrt{13.6/5.14}=1.63$。量子亏损

$$\delta_0=n-n^*=3-1.63=1.37 .$$

$\delta_0$ 这么大说明 $3s$ 电子穿进内层很深，感受到的有效核电荷远大于 1。对比 $3p$ 的 $\delta_1\approx0.88$、$3d$ 的 $\delta_2\approx0.01$：$l$ 越大，穿透越浅。

**4.21** $k=\sqrt{2mE}/\hbar$，用 $\hbar c=197.3\ \mathrm{MeV\cdot fm}$、$mc^2=939.6\ \mathrm{MeV}$：

$$k=\frac{\sqrt{2\times939.6\times1}}{197.3}=0.22\ \mathrm{fm^{-1}},\qquad kR=0.22\times3=0.66 .$$

$l_{\max}\approx kR\approx0.7$，所以只需 $l=0,1$；$l=2$ 的振幅被 $(kR)^2\approx0.4$ 压低，再高一阶更小。

**4.22** 瑞利散射截面 $\propto\lambda^{-4}$：

$$\frac{\sigma_{450}}{\sigma_{700}}=\left(\frac{700}{450}\right)^4=1.556^4\approx5.9 .$$

蓝光被散射近 6 倍强，所以天空偏蓝、直射阳光偏红（日落时路径长，蓝光被散射掉更多）。

**4.23** $J_2$ 项 $\propto J_2(a/r)^2$，$J_4$ 项 $\propto J_4(a/r)^4$。在 $r=2a$：

$$\frac{\text{$J_4$ 项}}{\text{$J_2$ 项}}=\frac{J_4}{J_2}\left(\frac{a}{r}\right)^2=\frac{1.6\times10^{-6}}{1.08\times10^{-3}}\cdot\frac14=3.7\times10^{-4} .$$

$r$ 越远，高阶项掉得越快，这就是「远场只需最低几阶」的定量版本。

**4.24** 精确电势是两团电荷的叠加，按 $r>r'$ 展开只有奇 $l$：

$$\Phi=\frac{q}{4\pi\varepsilon_0r}\sum_{l\ \text{奇}}2\left(\frac{d}{2r}\right)^lP_l(\cos\theta) .$$

$l=1$ 给 $qd\cos\theta/(4\pi\varepsilon_0r^2)$（偶极项）；$l=3$ 项与它之比在 $\theta=0$ 处是

$$\frac{\Phi_3}{\Phi_1}=\frac{1}{4}\left(\frac{d}{r}\right)^2\frac{P_3(1)}{P_1(1)}=\frac{1}{4}\cdot\frac{1}{25}=2.5\times10^{-3} .$$

误差 $0.25\%$。注意 $l=2$ 项为零（对称的正负电荷对没有四极矩），所以第一个修正来自八极。

**4.25** 不能。有界性只在 $\theta=0$ 一侧起作用时，$l$ 可以连续取值，解在 $\theta\to\pi$ 一侧是

$$y\sim\frac12P_l(x)\ln\frac{1+x}{1-x}\qquad(x\to-1),$$

对数发散。概率积分 $\int|y|^2\sin\theta\,\mathrm{d}\theta$ 其实收敛（对数平方可积），**但动能积分发散**：$\partial y/\partial\theta\sim1/(1-x)$，而 $\int|\nabla\psi|^2\,\mathrm{d}V\propto\int(1-x)^{-1}\mathrm{d}x$ 对数发散。所以「有界」在这里等价于「能量有限」，不能放松。

**4.26** 球外（$a<r<b$ 与 $r>b$ 分开写，或在 $r>a$ 内整体展开）：

$$\Phi=\frac{q}{4\pi\varepsilon_0}\left[\frac{1}{|\boldsymbol r-b\hat{\boldsymbol z}|}-\frac{a/b}{|\boldsymbol r-(a^2/b)\hat{\boldsymbol z}|}\right] .$$

推导：对 $r<b$ 用 $r'<r$ 的形式展开点电荷的场，再加上球面上的感应项 $\sum C_lr^{-(l+1)}P_l$；边界 $r=a$ 上逐项为零给出 $C_l=-\frac{q}{4\pi\varepsilon_0}\frac{a^{2l+1}}{b^{l+1}}$。把 $C_l$ 写成 $(a/b)(a^2/b)^l$ 就认出第二项也是一个点电荷：**镜像电荷 $q'=-qa/b$，位于 $b'=a^2/b$**。它与 4.10.2 的偶极结果一致（$b\to\infty$ 时 $q'\to\infty$、$b'\to\infty$，合成有限偶极）。

**4.27** $V=V_0\sin^2\theta=V_0(1-\cos^2\theta)=V_0\left(\frac23-\frac23P_2(\cos\theta)\right)$。只有 $c_0=\frac23V_0$、$c_2=-\frac23V_0$：

$$\Phi_{\mathrm{in}}=V_0\left[\frac23-\frac23\left(\frac{r}{a}\right)^2P_2(\cos\theta)\right],\qquad
\Phi_{\mathrm{out}}=V_0\left[\frac23\frac{a}{r}-\frac23\left(\frac{a}{r}\right)^3P_2(\cos\theta)\right] .$$

只有两项，因为 $\sin^2\theta$ 是 $\cos\theta$ 的二次多项式，$l>2$ 的矩恒为零。级数在这里是**精确的**，不存在截断误差。

**4.28** 记 $x=kr$。左边 $=1+ix\cos\theta-\frac{x^2}{2}\cos^2\theta+\cdots$；右边用 $j_0=1-\frac{x^2}{6}$、$j_1=\frac{x}{3}$、$j_2=\frac{x^2}{15}$：

$$1-\frac{x^2}{6}+3i\cdot\frac{x}{3}\cos\theta-5\cdot\frac{x^2}{15}\cdot\frac{3\cos^2\theta-1}{2}
=1+ix\cos\theta-\frac{x^2}{2}\cos^2\theta .$$

最后一步用了 $\frac16+\frac{3\cos^2\theta-1}{6}=\frac{\cos^2\theta}{2}$。三阶全对，说明 $A_l=(2l+1)i^l$ 没错。

**4.29** 取 $a_0=1$、$\kappa=1/2$，$l=0$ 的径向方程是 $R''+\frac2rR'+\left(-\frac14+\frac2r\right)R=0$。把 $R_{20}=\frac{1}{2\sqrt2}(2-r)e^{-r/2}$ 代入，逐项相消（数值上残差 $<10^{-9}$）。能量由 $E=-\hbar^2\kappa^2/(2\mu)$ 给出：

$$E_2=-\frac{\hbar^2}{8\mu a_0^2}=-\frac{13.6}{4}\ \mathrm{eV}=-3.4\ \mathrm{eV},$$

与 $-13.6/n^2$ 在 $n=2$ 处一致。

**4.30** $r=2a$ 处：$J_2$ 项相对单极是 $J_2(a/r)^2=1.08\times10^{-3}/4=2.7\times10^{-4}$；$J_4$ 项是 $1.6\times10^{-6}/16=1.0\times10^{-7}$，比 $J_2$ 项小 $3.7\times10^{-4}$。再下一阶 $J_6$ 更小两个量级。所以只留到 $l=4$，相对误差在 $10^{-6}$ 以下——地球重力场在 $r\ge2a$ 处基本就是「单极 + $J_2$」。

**4.31** 氢原子里 $2s$、$2p$ 同能量，因为库仑势是严格的 $1/r$，存在额外的隐藏对称性（拉普拉斯–龙格–楞次矢量守恒），使能量只依赖 $n$。

碱金属里，内层电子把核电荷屏蔽成 $Z_{\mathrm{eff}}(r)/r$，不再是 $1/r$，隐藏对称性被破坏。$s$ 电子穿透内层，看到更大的 $Z_{\mathrm{eff}}$，能量更低；$l$ 大的电子被离心势挡在外面，只看到近似 $1/r$，能量接近氢。于是 $E_{3s}<E_{3p}<E_{3d}$，简并解除。

**4.32** $n=3,l=2$：径向节点数 $n-l-1=0$；$\langle r\rangle=\frac{a_0}{2}\left[3n^2-l(l+1)\right]=\frac{a_0}{2}(27-6)=10.5a_0$。最概然半径由 $\frac{\mathrm{d}}{\mathrm{d}r}(r^4e^{-2r/(3a_0)})=0$ 定：$\frac4r=\frac{2}{3a_0}$，得 $r_{\mathrm{mp}}=6a_0$。

注意 $r_{\mathrm{mp}}<\!\langle r\rangle$：$d$ 态的分布比 $s$ 态窄（没有内层穿透），所以两者更接近。
**4.33** 靠的是「波函数在极轴（$\theta=0,\pi$）有界」，等价于能量有限：解在端点对数发散时动能积分发散（见 4.25）。

如果球面只覆盖上半球 $\theta\in[0,\pi/2]$，$l$ **不必**是整数。此时 $\theta=\pi/2$ 成了一个真实的边界，要在那里加边界条件（例如 $V$ 连续或给定），本征值 $l(l+1)$ 由这个条件定，解是非整数阶的连带勒让德函数（锥函数）。**整数性的来源是「两极都在区域边界上」，不是球坐标本身。**

**4.34** $\nabla^2(1/r)=0$ 只在 $r\ne0$ 成立；在原点它是 $-4\pi\delta(\boldsymbol r)$，正是电荷所在。多极展开用的场点总在源外（$r>r'$），那里 $1/|\boldsymbol r-\boldsymbol r'|$ 确实调和，展开合法。**奇性不是麻烦，它就是源。**

**4.35** 不能。$r<r'$ 时应展开成

$$\frac{1}{|\boldsymbol r-\boldsymbol r'|}=\sum_l\frac{r^l}{r'^{l+1}}P_l(\cos\gamma),$$

即 $r$ 与 $r'$ 的角色对调。强行用 $r>r'$ 的式子等于把生成函数里的 $t=r'/r>1$ 代入，超出收敛域，级数发散（物理上：你在源内部，各项越算越大）。

**4.36** 不成立。正交性来自边界项 $[(1-x^2)(\cdots)]_{-1}^{1}=0$，它要求区间是整个 $[-1,1]$。半球面对应 $x\in[0,1]$，端点 $x=0$ 处 $1-x^2\ne0$，边界项不为零，$\int_0^1P_lP_{l'}\,\mathrm{d}x\ne0$。后果：展开系数不能靠投影算，要解一个无穷维线性方程组（截断后求逆），或者改用该区域自己的本征函数。

**4.37** 不矛盾。连续说的是**函数值**：$R_{10}(0)=2a_0^{-3/2}$ 有限且连续。原点处的奇性在**势**里（$-e^2/4\pi\varepsilon_0r$），波函数的导数在那里有折点，$\nabla^2\psi$ 的原点奇性恰好被势的奇性抵消——这正是定态方程两边在原点同时发散、又互相抵消的意思。效应：21 cm 超精细线、电子俘获、穆斯堡尔同质异能移，都正比于 $|\psi(0)|^2$。

**4.38** 带电球没有唯一的偶极矩。把原点平移 $\boldsymbol a$，$\boldsymbol p=\int\rho\boldsymbol r'\,\mathrm{d}V'$ 变成 $\boldsymbol p+Q\boldsymbol a$，值变了。只有 $Q=0$ 时偶极矩与原点无关，才是内禀量。**所以「偶极矩」是中性物体的属性**；带电体的远场第一项永远是单极，偶极项可以被原点选择消掉。

**4.39** 不矛盾。展开式是精确的恒等式，无穷多项都得有；但第 $l$ 项的系数含 $j_l(kr)\sim(kr)^l$，当 $kR\ll1$ 时 $l\ge1$ 的项被 $(kR)^l$ 系统性地压低。截断不是「忽略无穷多数学项」，而是「丢掉物理上小到测不出的项」，误差可以估计（4.9.3、例 4.8）。

**4.40** 因为两维的径向方程不同。三维 $l=0$ 时 $(r^2R')'=0$，解 $R=A+B/r$；二维时 $(rR')'=0$，解 $R=A+B\ln r$。物理来源是通量守恒：三维点源的场线摊在 $4\pi r^2$ 上，场按 $1/r^2$、势按 $1/r$；二维线源摊在 $2\pi r$ 上，场按 $1/r$、势按 $\ln r$。

**4.41** 错在把「单点概率为零」当成理由。概率密度在一点取什么值确实不影响积分，但发散的解让 $\partial\psi/\partial\theta\sim1/(1-x)$，动能积分 $\int|\nabla\psi|^2\,\mathrm{d}V$ 对数发散，函数根本不在哈密顿量的定义域里。**判据不是「某点的值」，而是「积分是否有限」。**

**4.42** 不必是常数。反例：球壳上 $V(\theta)=V_0\cos\theta$，球内

$$\Phi_{\mathrm{in}}=V_0\frac{r}{a}\cos\theta$$

满足 $\nabla^2\Phi=0$，且随 $\theta$ 变化。正确的说法是：球内无电荷只保证 $\Phi$ 调和；要得到「常数」还得加上球对称的边界条件。一般成立的是**平均值定理**——球心电势等于球面平均，而球面平均可以不是常数。

## 第 5 章

> 每题给关键一步、中间结果与最终答案。缺的步骤请自己补全后再看。

**5.1** 第一式由筛选性质直接得 $(2^2+1)=5$。第二式先做缩放：$\delta(2x-4)=\delta\big(2(x-2)\big)=\frac12\delta(x-2)$，而 $x=2$ 落在积分区间 $[-1,3]$ 内，所以结果是 $\frac12$。

**5.2** 换元 $t=ax$，$\mathrm{d}x=\mathrm{d}t/a$。$a>0$ 时上下限不变：

$$\int f(x)\delta(ax)\,\mathrm{d}x=\frac1a\int f(t/a)\delta(t)\,\mathrm{d}t=\frac{f(0)}{a}.$$

$a<0$ 时 $\mathrm{d}t=a\,\mathrm{d}x<0$，上下限交换，多出一个负号，结果 $f(0)/|a|$。两式合起来就是 $\delta(ax)=\delta(x)/|a|$。**那个绝对值是"积分方向"的账，不是约定。**

**5.3** $\delta(x^2-4)$：$g=x^2-4$，单根 $x=\pm2$，$|g'|=|2x|=4$，所以 $\big[\delta(x-2)+\delta(x+2)\big]/4$。

$\delta(\cos x)$ 在 $[0,2\pi]$ 内：单根 $x=\pi/2,\,3\pi/2$，$|g'|=|\sin x|=1$，所以 $\delta(x-\pi/2)+\delta(x-3\pi/2)$。

$g'=0$ 处（如 $\delta(x^2)$ 的 $x=0$）线性化退化，$\delta(g)$ 不能用这个公式——物理上那是经典转折点，要换成艾里函数。

**5.4** 对任意测试函数，$\int x\delta'(x)f\,\mathrm{d}x=-\int(xf)'\delta\,\mathrm{d}x=-[xf]_{x=0}=0$，而 $\int(-\delta)f=-f(0)$，故 $x\delta'(x)=-\delta(x)$。

第二式：$\int x^2\delta'(x)\,\mathrm{d}x=-\dfrac{\mathrm{d}}{\mathrm{d}x}(x^2)\Big|_{x=0}=-2x\big|_{0}=0$。**注意不是 $\delta$ 的系数，而是测试函数导数在 0 处的值。**

**5.5** 用球坐标，$\mathrm{d}^3r=r^2\sin\theta\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi$：

$$\int\frac{\delta(r)}{4\pi r^2}f\,r^2\sin\theta\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi=\frac{1}{4\pi}\Big(\int_0^\infty\delta(r)f\,\mathrm{d}r\Big)\Big(\oint\mathrm{d}\Omega\Big)=f(0).$$

$\oint\mathrm{d}\Omega=4\pi$，与前面的 $1/4\pi$ 相消。取 $f=1$、$a>0$：$\int_{r<a}\delta(\boldsymbol{r})\,\mathrm{d}^3r=1$。若写成 $\delta(r)$，这个积分会给出 $4\pi a^2\cdot\frac{1}{4\pi a^2}$ 之外的多余因子，值变成 $4\pi$——所以必须带 $1/(4\pi r^2)$。

**5.6** $r\ne0$ 时 $\nabla^2(1/r)=\frac{1}{r^2}\frac{\mathrm{d}}{\mathrm{d}r}\big(r^2\cdot(-1/r^2)\big)=0$。取半径 $R$ 的球面：

$$\oint\frac{\partial}{\partial r}\frac1r\,\mathrm{d}S=\oint\Big(-\frac{1}{R^2}\Big)R^2\,\mathrm{d}\Omega=-4\pi,$$

与 $R$ 无关，故源是 $-4\pi\delta(\boldsymbol{r})$。平移得

$$\nabla^2\frac{1}{|\boldsymbol{r}-\boldsymbol{r}'|}=-4\pi\delta(\boldsymbol{r}-\boldsymbol{r}').$$

**5.7** $G=-\dfrac{x_<(L-x_>)}{L}$。$L=2$、$x'=0.5$、$x=1$：$x_<=0.5$、$x_>=1$，

$$G(1,0.5)=-\frac{0.5\times(2-1)}{2}=-0.25.$$

在 $x=x'$ 处两边都等于 $-x'(L-x')/L$（连续）；导数左为 $-(L-x')/L$、右为 $x'/L$，差 $=1$，正是二阶导的 $\delta$。

**5.8** $L=2$ 时 $\psi_n=\sin(n\pi x/2)$、$\lambda_n=(n\pi/2)^2$，

$$G=-\frac{4}{\pi^2}\sum_{n=1}^{\infty}\frac{1}{n^2}\sin\frac{n\pi x}{2}\sin\frac{n\pi x'}{2}.$$

取 $x=x'=0.5$：精确值 $-0.375$。部分和：$N=1$ 给 $-0.2026$，$N=3$ 给 $-0.3265$，$N=5$ 给 $-0.3346$（相对误差 $11\%$），$N=200$ 才到 $-0.3740$。**误差按 $1/N$ 下降，不是指数下降**——因为 $G$ 在 $x=x'$ 处有尖角。

**5.9** 镜像是 $z=-z'$：

$$G=-\frac{1}{4\pi R_1}+\frac{1}{4\pi R_2},\qquad R_{1,2}=\sqrt{(x-x')^2+(y-y')^2+(z\mp z')^2}.$$

$z=0$ 时 $R_1=R_2$，$G=0$。源移到边界上（$z'=0$）时镜像与源重合，两项相消，区域内 $G\equiv0$：**接地导体表面的电荷被表面感应电荷完全中和**，净电荷为零，所以区域里没有场。要算"贴着边界"的场，得把源放到 $z'=\epsilon$ 再取极限，结果是 $\epsilon$ 阶的小量。

**5.10** $[G_0]=1/L$，因为 $[\nabla^2]=1/L^2$、$[\delta^{(3)}]=1/L^3$。点电荷：

$$\phi=-\frac{1}{\varepsilon_0}\int G_0\,q\delta(\boldsymbol{r}-\boldsymbol{r}_0)\,\mathrm{d}^3r'=+\frac{q}{4\pi\varepsilon_0|\boldsymbol{r}-\boldsymbol{r}_0|}.$$

两个负号（$G_0$ 的、公式的）相消，结果为正，与库仑定律一致。**这就是检验符号约定的标准动作。**

**5.11** 取半径 $r$ 的圆周：

$$\oint\frac{\partial\ln r}{\partial r}\,\mathrm{d}l=\oint\frac1r\,r\,\mathrm{d}\varphi=2\pi,$$

与 $r$ 无关，故 $\nabla^2\ln R=2\pi\delta^{(2)}$。线电荷 $\lambda$ 的电势：

$$\phi=-\frac{1}{\varepsilon_0}\int\frac{1}{2\pi}\ln R\,\lambda\delta^{(2)}\,\mathrm{d}^2r'=-\frac{\lambda}{2\pi\varepsilon_0}\ln r.$$

$\ln r$ 在远处无界，所以只有 $\sum\lambda=0$ 时才有"远处为零"的解——这就是二维问题必须整体中性的原因。

**5.12** 令 $G=g(t-t'-R/c)/R$，则 $\nabla^2G=\frac{1}{R}\partial^2(RG)/\partial R^2=\frac{1}{c^2R}g''$，而 $\frac{1}{c^2}\partial^2G/\partial t^2=\frac{1}{c^2R}g''$，两者相等，故 $R\ne0$ 处满足齐次方程。$\delta(t-t'-R/c)$ 的作用：只有在 $t=t'+R/c$ 这一个时刻 $\delta$ 才不为零，**所以源的一次闪烁只在一个时刻、一个半径的球面上被看到**——这就是"以光速传播"和因果性的数学表述。

**5.13** $d=1\,\mathrm{mm}$、$q=1\,\mathrm{nC}$：

$$\sigma(\rho)=-\frac{qd}{2\pi(\rho^2+d^2)^{3/2}},\qquad \sigma(0)=-\frac{q}{2\pi d^2}=-1.6\times10^{-4}\ \mathrm{C/m^2}.$$

总感应电荷 $-q$（与 $d$ 无关）。受力

$$F=-\frac{q^2}{16\pi\varepsilon_0d^2}=-2.2\times10^{-3}\ \mathrm{N}.$$

比 $d=1\,\mathrm{cm}$ 时大一百倍，符合 $d^{-2}$。

**5.14** 镜像有两族：$+q$ 在 $z=2na+d$（$n\ne0$），$-q$ 在 $z=2na-d$（$n\in\mathbb{Z}$）。无穷多的原因：一块板产生的镜像会被另一块板再次反射，来回无限次。

受力（沿 $+z$）：

$$F_z=\frac{q^2}{16\pi\varepsilon_0}\left[-\frac{1}{d^2}+\frac{1}{(a-d)^2}-\frac{1}{(a+d)^2}+\frac{1}{(2a-d)^2}-\cdots\right].$$

第一项是最近镜像的吸引，其余是往返回路。取 $d=a/4$：括号 $\approx(-16+1.78-0.64+0.33-\cdots)/a^2\approx-14.7/a^2$，净力向下（吸向近板），级数按 $1/n^2$ 收敛。$a\to0$ 时 $F\sim-1/a^2$ 发散（板贴到一起）。**正中间 $d=a/2$ 时上下对称，力恒为零。**

**5.15** $q'=-qa/d=-6.7\times10^{-7}\,\mathrm{C}$，$b=a^2/d=1.7\,\mathrm{cm}$。总感应电荷等于 $q'$（$-0.67\,\mu\mathrm{C}$），**不是 $-q$**。力

$$F=\frac{qq'}{4\pi\varepsilon_0(d-b)^2}=-0.67\ \mathrm{N},$$

吸引力，比同距离的平面情形弱（球的曲率让感应电荷更分散）。

**5.16** $\alpha=60^\circ=\pi/3$，$2n-1=5$ 个镜像：$+q$ 在 $150^\circ$、$270^\circ$，$-q$ 在 $-30^\circ$、$90^\circ$、$210^\circ$（源在 $30^\circ$、距顶点 $d$）。垂直平分线方向的分量成对抵消，合力沿角平分线指向顶点：

$$F=\frac{q^2}{4\pi\varepsilon_0d^2}\times0.673.$$

数值来自 $\sum_i Q_i\cos\theta_i/R_i^2$ 的逐项求和：最靠近的两个 $-q$ 贡献最大（距离 $d$），两个 $+q$ 在 $\sqrt3d$ 处把它们削弱一部分。

**5.17** 设电荷在 $z>0$ 的 $\varepsilon_1$ 中，距界面 $d$。$z>0$ 区域的电势等效于"$q$ 加上 $q'$"，都在 $\varepsilon_1$ 中：

$$q'=q\frac{\varepsilon_1-\varepsilon_2}{\varepsilon_1+\varepsilon_2}.$$

$\varepsilon_2>\varepsilon_1$ 时 $q'<0$（界面把场"拉"向自己一侧，等效于异号镜像），$\varepsilon_2\to\infty$ 给出 $q'=-q$（导体极限），$\varepsilon_2=\varepsilon_1$ 给出 $q'=0$（没有界面）。

**5.18** 用镜像（两端恒零，奇延拓）：

$$T(x,t)=\frac{Q}{\rho c_p}\sum_{n=-\infty}^{\infty}\Big[K\big(x-\tfrac{L}{2}-2nL,t\big)-K\big(x+\tfrac{L}{2}-2nL,t\big)\Big].$$

$t\to\infty$ 时只剩最低模：

$$T\approx\frac{2Q}{\rho c_pL}\sin\frac{\pi x}{L}\,e^{-\alpha\pi^2t/L^2}\to0.$$

热量从两端流走了（两端温度固定为零，等于两个无限大的热库），所以杆内总热量单调减少，最终归零。

**5.19** 半无限介质、表面温度 $T_0\cos\omega t$，解是衰减的行波：

$$T(x,t)=T_0\,e^{-x/\delta}\cos\!\Big(\omega t-\frac{x}{\delta}\Big),\qquad \delta=\sqrt{\frac{2\alpha}{\omega}}.$$

$\omega=2\pi/86400=7.3\times10^{-5}\,\mathrm{s^{-1}}$，$\alpha=5\times10^{-7}$：$\delta=\sqrt{2\times5\times10^{-7}/7.3\times10^{-5}}\approx0.12\ \mathrm{m}$。

**日变化的穿透深度约 12 cm**（振幅降到 $1/e$），相位滞后 $x/\delta$ 弧度。这解释了为什么地下 1 m 处几乎没有日温差、却有明显的年温差（年的 $\omega$ 小 365 倍，$\delta$ 大 19 倍）。

**5.20** $\varphi=\dfrac{q}{4\pi\varepsilon_0R}\Theta(t-R/c)$。$R=2ct>ct$，在球壳之外，$\Theta=0$，所以 $\varphi=0$、$\boldsymbol{E}=0$。**"电荷出现了"这个消息还没传到那里。**

**5.21** 推迟时刻的源是 $q_0e^{-(t-R/c)/\tau}$（只要 $t-R/c>0$）：

$$\varphi(R,t)=\frac{q_0}{4\pi\varepsilon_0R}\,e^{-(t-R/c)/\tau}\,\Theta\!\Big(t-\frac{R}{c}\Big).$$

两个因子各管一件事：$\Theta$ 管"到没到"，指数管"到的时候源已经衰减了多少"。$R\ll c\tau$ 时退化为准静态的 $q(t)/(4\pi\varepsilon_0R)$。

**5.22** 稳态：$\alpha T''+S/(\rho c_p)=0$，即 $T''=-S/k$（$k=\alpha\rho c_p$ 是导热系数）。积分两次并用 $T(0)=T_1$、$T'(L)=0$：

$$T(x)=T_1+\frac{S}{k}\Big(Lx-\frac{x^2}{2}\Big).$$

通量条件检验：$x=L$ 端绝热（零通量），$x=0$ 端流出 $kT'(0)=SL$，恰好等于总产热 $SL$。**所以稳态存在。** 两端都绝热时没有出口，通量条件 $\oint=0$ 与总产热 $SL\ne0$ 矛盾，稳态不存在（温度线性上升）。

**5.23** 壳内：$\phi(\boldsymbol{r})=-\dfrac{q}{\varepsilon_0}G(\boldsymbol{r},\boldsymbol{r}_0)$，$G$ 是腔体的狄利克雷格林函数，边界上为零。壳上总感应电荷由高斯定理得 $-q$（把闭合曲面取在壳内紧贴壳壁处，内部只有 $q$）。壳外：壳接地给 $\phi|_{\text{外表面}}=0$，外部无源，由唯一性 $\phi\equiv0$。**这就是静电屏蔽的完整说法：屏蔽靠的是"边界值给定 + 无源 + 唯一性"，不是靠导体"挡"住场。**

**5.24** $Q=0$、$\boldsymbol{p}=0$、$Q_{zz}=4qa^2$、$Q_{xx}=Q_{yy}=-2qa^2$，

$$\varphi=\frac{qa^2}{4\pi\varepsilon_0r^3}\big(3\cos^2\theta-1\big).$$

下一项是 $l=4$：$\varphi_4=\dfrac{q}{4\pi\varepsilon_0}\dfrac{2a^4P_4(\cos\theta)}{r^5}$。与 $l=2$ 项之比为 $(a/r)^2|P_4|/|P_2|$。$r=5a$、$\theta=0.6$ 时 $P_2=0.5218$、$P_4=-0.1488$，比值 $=0.04\times0.285=1.1\%$。

**5.25** 取 $u=G(\boldsymbol{r},\boldsymbol{r}_1)$、$v=G(\boldsymbol{r},\boldsymbol{r}_2)$，用格林第二恒等式。左边 $=G(\boldsymbol{r}_2,\boldsymbol{r}_1)-G(\boldsymbol{r}_1,\boldsymbol{r}_2)$，右边 $=\oint(u\partial_nv-v\partial_nu)\mathrm{d}S$。狄利克雷时 $u=v=0$，右边为零，得互易性。诺伊曼时右边 $=\frac1S\oint(u-v)\mathrm{d}S$，只有 $u-v$ 的边界平均为零时才消失；而 $u-v$ 本身可以差一个常数，所以诺伊曼情形要先约定"边界平均为零"（即固定那个常数），互易性才成立。

**5.26** $G=\frac{1}{2\pi}\big[\ln R-\ln\big(\frac{r'}{a}R^*\big)\big]$，$R^*=|\boldsymbol{r}-\boldsymbol{r}'^*|$，$\boldsymbol{r}'^*=\frac{a^2}{r'^2}\boldsymbol{r}'$。对 $r'$ 求导并在 $r'=a$ 取值得

$$\frac{\partial G}{\partial r'}\Big|_{r'=a}=\frac{1}{2\pi}\cdot\frac{a^2-r^2}{a(a^2+r^2-2ar\cos(\varphi-\varphi'))},$$

乘上边界测度 $a\,\mathrm{d}\varphi'$ 后 $a$ 消掉，得泊松核。

检验：$r=0$ 时核为 $1/2\pi$，$u$ 等于边界平均；$r\to a$ 时核在 $\varphi'=\varphi$ 附近尖锐成峰，宽度 $a-r$、积分仍为 1，故 $u\to f(\varphi)$。**这就是 5.2.1 说的"面积 1、宽度趋零"的又一副面孔。**

**5.27** 对 $\nabla^2G=\delta$ 积分并用高斯定理：$\oint\partial G/\partial n\,\mathrm{d}S=1$。若取 $\partial G/\partial n=0$，左边为零，矛盾。

一维 $[0,L]$：条件是 $-G'(0)+G'(L)=1$（两个端点各贡献一项，相当于 $S=2$）。取

$$G(x,x')=\frac{|x-x'|}{2}+C,$$

则 $G''=\delta(x-x')$，$G'(0)=-1/2$、$G'(L)=+1/2$，$-G'(0)+G'(L)=1$ ✔。常数 $C$ 任意——**这正是诺伊曼解"差一个常数"的格林函数版本**。

**5.28** 在源点处

$$G_N(x',x')-G(x',x')=-\frac{2L}{\pi^2}\sum_{n>N}\frac{\sin^2(n\pi x'/L)}{n^2}.$$

被截掉的尾巴 $\sum_{n>N}n^{-2}\approx1/N$（积分判别法），系数 $2L/\pi^2$ 与 $\sin^2$ 的平均值 $1/2$ 合起来给

$$\big|G_N-G\big|\approx\frac{L}{\pi^2}\cdot\frac{1}{N}\approx\frac{0.10}{N}\quad(L=1),$$

与图 5.3(b) 的数值斜率一致。**机制：$G$ 有尖角，尖角的傅里叶系数按 $1/n^2$ 衰减，截断误差按 $1/N$ 衰减——这是"函数不光滑"的直接代价。**

**5.29** $K_D=K(x-x',t)-K(x+x',t)$。$x=0$ 时两项相等，$K_D=0$ ✔。总热量

$$\int_0^\infty K_D\,\mathrm{d}x=\frac12\big[\mathrm{erf}(\infty)-\mathrm{erf}(\infty)\big]+\cdots=\frac12-\frac12\mathrm{erf}\Big(\frac{x'}{\sqrt{4\alpha t}}\Big),$$

随 $t$ 单调下降（$t\to0$ 时为 1，$t\to\infty$ 时为 0）。**边界是个无底的热库，热量从那里漏光。**

**5.30** 两者都满足方程：源点附近的通量计算只依赖 $g$ 在 $t=t'$ 的取值，向外（$t-R/c$）与向内（$t+R/c$）的球面波给出同一个 $-4\pi g$。物理上取推迟解，靠的是初始条件与辐射条件（无穷远只允许出射波）。

若初始条件就是"向原点汇聚的球面波"，那个解在汇聚前正是超前解的形式——它从无穷远"预谋"好了要汇聚，物理上对应极端精细调节的初值。真实系统不会这样。

**5.31** 级数第 $l$ 项 $\propto(r'/r)^l$。$r>r'_{\max}$ 时比值 $<1$，级数被几何级数控制，收敛。$l=4$ 项：线性四极是"两个 $+q$ 加一个 $-2q$"，展开后只剩偶 $l$：

$$\varphi_4=\frac{q}{4\pi\varepsilon_0}\cdot\frac{2a^4P_4(\cos\theta)}{r^5}.$$

与 $l=2$ 项之比 $=(a/r)^2|P_4/P_2|$。$r=5a$、$\theta=0.6$：$0.04\times(0.1488/0.5218)=1.1\%$。

**5.32** 均匀带电球（半径 $a$、总电荷 $q$）的静电能：

$$W=\frac{\varepsilon_0}{2}\int|\boldsymbol{E}|^2\,\mathrm{d}V=\frac{q^2}{8\pi\varepsilon_0}\int_a^\infty\frac{\mathrm{d}r}{r^2}=\frac{q^2}{8\pi\varepsilon_0a}$$

（球内部分的能量另算，若电荷只分布在表面就是它；均匀分布时 $W=3q^2/(20\pi\varepsilon_0a)$，差别是常数因子，发散行为相同）。$a\to0$ 时 $W\to\infty$。

取 $a=r_e=e^2/(4\pi\varepsilon_0m_ec^2)=2.82\times10^{-15}\,\mathrm{m}$、$q=e$：

$$\frac{W}{m_ec^2}=\frac{3}{20}\cdot\frac{e^2}{4\pi\varepsilon_0r_e}\cdot\frac{1}{m_ec^2}=\frac35=0.6.$$

**自能与静止质量同量级**，说明"点电子 + 经典电磁场"这套模型在 $r_e$ 处就自相矛盾了：要么电子有结构，要么需要量子场论。这不是算错了，是模型的边界。

**5.33** 错。两点：一，"在 0 处取无穷大"不是一个函数值，$\delta$ 不是函数；二，"其余为零但积分为 1"在普通函数里不可能。正确说法只有积分（或极限）意义：$\int f\delta=f(0)$，或者 $\delta=\lim_{\epsilon\to0}\delta_\epsilon$。**判断标准：这个式子里 $\delta$ 是不是在积分号内？**

**5.34** 错。$\nabla^2G=\delta$ 只是方程，解要靠边界条件定。无边界、且要求 $G\to0$ 于无穷远时，解才是 $-1/(4\pi R)$。有导体壳、有界面时，$G$ 完全不同（5.6、5.8 的例子）。**这句话漏掉了"对什么边界条件"这半句。**

**5.35** 半对。"感应电荷总量等于镜像电荷量"对平面成立（$-q$），对球不成立（$-qa/d\ne-q$），所以这句话作为普遍命题是错的。

镜像电荷不是真实电荷：它只是一个"位于区域外、用来凑边界条件"的数学源。区域内部（导体一侧）根本没有场，说那里有电荷没有意义。**它的价值是等价，不是存在。**

**5.36** 错。由 $\oint\partial G/\partial n\,\mathrm{d}S=\int\nabla^2G\,\mathrm{d}V=1$，诺伊曼的 $G$ 必须满足 $\partial G/\partial n=1/S\ne0$。取零法向导数与高斯定理直接矛盾，方程无解。

**5.37** 错在两步。其一，那个"非零"是 $e^{-x^2/(4\alpha t)}$ 量级，$x=1\,\mathrm{m}$、$t=1\,\mathrm{s}$ 时约 $e^{-5\times10^5}$，不可观测。其二，说"超光速"要先有可测量的信号；抛物型方程本来就没有速度上限，"前沿速度无穷大"是模型的性质而不是物理的传播。真正的判据是：当 $t$ 接近弛豫时间 $\tau\sim10^{-12}\,\mathrm{s}$、或尺度接近平均自由程时，傅里叶定律失效，方程要换成双曲型。

**5.38** 错。超前解同样满足波动方程（把它代进去，$R\ne0$ 处齐次方程成立，源点通量也一致）。排除它的是初始条件与辐射条件，不是方程。**方程对时间反演对称，是边界/初始条件破坏了对称性。**

**5.39** 错。第一，中性物体 $Q=0$ 时首项是偶极或四极，按 $1/r^2$、$1/r^3$ 衰减，而带电体是 $1/r$——远场上带电体确实更强。但"总比"不成立：近距离（$r$ 与源尺度可比）时多极展开根本不能用，中性物体近场的局部电场可以远强于远处的一个小带电体。第二，偶极矩可以很大（例如极性分子、带电平行板），抵消 $1/r$ 的差距。

**5.40** 错。级数在源点是**点态不收敛**的（那里是 $\delta$ 的奇异性），误差集中在源点附近，且随 $N$ 只按 $1/N$ 下降（5.28）。所以"$N$ 够大就处处精确"不成立：要么在源附近永远有 $O(1/N)$ 的误差，要么改用别的表示（镜像、分段解、数值）。**判断方法：把误差画出来，看它是否集中在某一点。**

## 第 6 章

### 习题 6.1–6.12

**6.1** 配方：$x^2+2x+2=(x+1)^2+1$，平移 $u=x+1$ 不改变积分值。极点在 $z=-1\pm i$，上半平面取 $z=-1+i$，一阶，留数 $1/(2z+2)\big|_{z=-1+i}=1/(2i)$。结果

$$\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{x^2+2x+2}=2\pi i\cdot\frac{1}{2i}=\pi .$$


**6.2** 极点在 $z=\pm ia$，都是三阶。$m=3$，需要二阶导：

$$\operatorname{Res}_{z=ia}\frac{1}{(z^2+a^2)^3}=\frac{1}{2!}\frac{\mathrm{d}^2}{\mathrm{d}z^2}\left[\frac{1}{(z+ia)^3}\right]_{z=ia}
=\frac{1}{2}\cdot\frac{12}{(2ia)^5}=\frac{3}{16ia^5}.$$

（$\frac{\mathrm{d}^2}{\mathrm{d}z^2}(z+ia)^{-3}=12(z+ia)^{-5}$，$(2ia)^5=32ia^5$，故 $\frac12\cdot\frac{12}{32ia^5}=\frac{3}{16ia^5}$。）于是

$$\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{(x^2+a^2)^3}=2\pi i\cdot\frac{3}{16ia^5}=\frac{3\pi}{8a^5}.$$


**6.3** 先做代数变形避开二阶极点公式：$\dfrac{x^2}{(x^2+a^2)^2}=\dfrac{1}{x^2+a^2}-\dfrac{a^2}{(x^2+a^2)^2}$。用 6.5 的 $\int\mathrm{d}x/(x^2+a^2)=\pi/a$ 与例 4 类的 $\int\mathrm{d}x/(x^2+a^2)^2=\pi/(2a^3)$：

$$\int_{-\infty}^{\infty}\frac{x^2\,\mathrm{d}x}{(x^2+a^2)^2}=\frac{\pi}{a}-a^2\cdot\frac{\pi}{2a^3}=\frac{\pi}{2a}.$$

**不能"逐项相除"**：$\int x^2\mathrm{d}x/\int(x^2+a^2)^2$ 没有任何意义，商的积分不等于积分的商。


**6.4** 极点是 $z^4=-a^4$ 的四个解，$z_k=ae^{i\pi(2k+1)/4}$，上半平面取 $k=0,1$。留数 $1/(4z_k^3)=-z_k/(4a^4)$（用 $z_k^4=-a^4$）。两个之和 $-(z_1+z_2)/(4a^4)=-i\sqrt2/(4a^3)$。全实轴

$$\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{x^4+a^4}=2\pi i\left(-\frac{i\sqrt2}{4a^3}\right)=\frac{\pi}{\sqrt2\,a^3},$$

半条实轴（偶函数）给一半：$\dfrac{\pi}{2\sqrt2\,a^3}$。


**6.5** 二阶极点 $z=\pm i$，取 $z=i$，用 $P=e^{2iz}$、$Q=(z^2+1)^2$，$Q$ 在 $i$ 有二阶零点，改用三阶刀的等价形式：

$$\operatorname{Res}_{z=i}\frac{e^{2iz}}{(z^2+1)^2}=\frac{\mathrm{d}}{\mathrm{d}z}\left[\frac{e^{2iz}}{(z+i)^2}\right]_{z=i}
=e^{-2}\left[\frac{2i}{(2i)^2}-\frac{2}{(2i)^3}\right]
=e^{-2}\left(-\frac{i}{2}-\frac{1}{4i}\right).$$

用 $1/(4i)=-i/4$，括号 $=-i/2-i/4=-3i/4$，所以留数 $=-3ie^{-2}/4$。于是

$$\int_{-\infty}^{\infty}\frac{\cos(2x)}{(x^2+1)^2}\,\mathrm{d}x=\operatorname{Re}\left[2\pi i\left(-\frac{3i}{4}e^{-2}\right)\right]=\frac{3\pi}{2}e^{-2}.$$

注意被积函数虽然是偶函数，但这里积的是**全实轴**，不需要再取半；若问 $\int_0^{\infty}$ 才是它的一半 $\frac{3\pi}{4}e^{-2}$。

（用一般公式 $\int\mathrm{d}x\cos(ax)/(x^2+b^2)^2=\frac{\pi}{2b^3}(1+ab)e^{-ab}$ 核对：$a=2,b=1$ 给 $\frac{3\pi}{2}e^{-2}$。）


**6.6** 被积函数 $x\sin(ax)/(x^2+b^2)$ 是偶函数（奇×奇）。用 $ze^{iaz}/(z^2+b^2)$，上半平面极点 $ib$，留数 $\dfrac{ib\,e^{-ab}}{2ib}=\dfrac{e^{-ab}}{2}$。大弧由若尔当消失（$a>0$）。于是

$$\int_{-\infty}^{\infty}\frac{xe^{iax}}{x^2+b^2}\,\mathrm{d}x=2\pi i\cdot\frac{e^{-ab}}{2}=i\pi e^{-ab}.$$

取虚部即得 $\pi e^{-ab}$（$x/(x^2+b^2)$ 实值，取虚部合法）。


**6.7** $f=e^{i\omega x}/(x-\omega_0)$，$\omega>0$，极点在实轴 $\omega_0$ 处，一阶，留数 $e^{i\omega\omega_0}$。实轴从左到右、从上方绕过（顺时针）给 $-i\pi$ 乘留数，大弧由若尔当消失。回路内无其他极点：

$$\mathrm{P.V.}\int_{-\infty}^{\infty}\frac{e^{i\omega x}}{x-\omega_0}\,\mathrm{d}x=i\pi e^{i\omega\omega_0}.$$

实部是 $\cos$ 的主值积分 $-\pi\sin(\omega\omega_0)$，虚部是 $\sin$ 的 $\pi\cos(\omega\omega_0)$。


**6.8** $x^4+4=(x^2-2x+2)(x^2+2x+2)$，极点在 $z=\pm1\pm i$，上半平面两个一阶极点。$Q'=4z^3$，留数 $1/(4z^3)$。$z_1=1+i$：$z_1^2=2i$，$z_1^3=2i(1+i)=2i-2$，留数 $1/(8i-8)$。$z_2=-1+i$：$z_2^2=-2i$，$z_2^3=-2i(-1+i)=2i+2$，留数 $1/(8i+8)$。相加

$$\frac{1}{8}\left(\frac{1}{i-1}+\frac{1}{i+1}\right)=\frac{1}{8}\cdot\frac{2i}{-2}=-\frac{i}{8}.$$

于是 $\int=2\pi i(-i/8)=\pi/4$。


**6.9** $f=1/[(z^2+a^2)(z^2+b^2)]$，极点 $\pm ia,\pm ib$ 都是一阶。留数：$\pm ia$ 处 $\dfrac{1}{2z(z^2+b^2)}$，即 $\dfrac{1}{\pm2ia(b^2-a^2)}$；$\pm ib$ 处 $\dfrac{1}{\pm2ib(a^2-b^2)}$。上半平面两个相加，提 $\dfrac{1}{2i(b^2-a^2)}$ 后括号为 $\dfrac1a-\dfrac1b=\dfrac{b-a}{ab}$，于是总和 $=\dfrac{1}{2iab(a+b)}$，

$$\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{(x^2+a^2)(x^2+b^2)}=2\pi i\cdot\frac{1}{2iab(a+b)}=\frac{\pi}{ab(a+b)}.$$

$a\to b$ 时极限为 $\pi/(2b^3)$，正是 $\int\mathrm{d}x/(x^2+b^2)^2$，与二阶极点公式一致—所以这个公式在 $a=b$ 处虽然推导用了 $a\ne b$，结果连续。


**6.10** 极点 $z=\pm ib$ 都是二阶，取上半平面的 $ib$。用三阶刀：

$$\operatorname{Res}_{z=ib}\frac{e^{iaz}}{(z^2+b^2)^2}
=\frac{\mathrm{d}}{\mathrm{d}z}\left[\frac{e^{iaz}}{(z+ib)^2}\right]_{z=ib}
=-\frac{i(1+ab)}{4b^3}e^{-ab}.$$

（$(2ib)^2=-4b^2$、$(2ib)^3=-8ib^3$；求导后两项都要保留，正是它们给出 $1+ab$。）于是

$$\int_{-\infty}^{\infty}\frac{\cos(ax)}{(x^2+b^2)^2}\,\mathrm{d}x
=\operatorname{Re}\left[2\pi i\cdot\left(-\frac{i(1+ab)}{4b^3}e^{-ab}\right)\right]
=\frac{\pi}{2b^3}(1+ab)e^{-ab}.$$

**两个极限：** $a\to0$ 给 $\pi/(2b^3)$，正是 $\int\mathrm{d}x/(x^2+b^2)^2$；$a\gg b$ 时化为 $\frac{\pi a}{2b^2}e^{-ab}$，指数衰减的衰减长度是 $1/a$。这两条能抓住"漏掉 $(1+ab)$"或"漏掉 $b$ 的幂次"的错误。


**6.11** 极点是 $z^6=-1$ 的六个解，$z_k=e^{i(2k+1)\pi/6}$，上半平面取 $k=0,1,2$（角 $\pi/6,\ \pi/2,\ 5\pi/6$）。留数用第二把刀，$Q'=6z^5$，而 $z_k^6=-1$ 给 $1/z_k^5=z_k/z_k^6=-z_k$：

$$\operatorname{Res}_{z=z_k}\frac{1}{1+z^6}=-\frac{z_k}{6}.$$

三个之和：

$$-\frac{1}{6}\left(e^{i\pi/6}+e^{i\pi/2}+e^{i5\pi/6}\right)
=-\frac{1}{6}\left(\left(\frac{\sqrt3}{2}+\frac{i}{2}\right)+i+\left(-\frac{\sqrt3}{2}+\frac{i}{2}\right)\right)
=-\frac{i}{3}.$$

（实部两两抵消，虚部 $1/2+1+1/2=2$。）于是

$$\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{x^6+1}=2\pi i\left(-\frac{i}{3}\right)=\frac{2\pi}{3},
\qquad
\int_0^{\infty}=\frac{\pi}{3}.$$

与通式 $\int_0^\infty\mathrm{d}x/(1+x^n)=\dfrac{\pi}{n\sin(\pi/n)}$ 在 $n=6$ 处一致（$\sin(\pi/6)=1/2$）。


**6.12** 不要直接算。拆成两个已知的：

$$\int_{-\infty}^{\infty}\frac{x^2+1}{x^4+1}\,\mathrm{d}x
=\int_{-\infty}^{\infty}\frac{x^2}{x^4+1}\,\mathrm{d}x
+\int_{-\infty}^{\infty}\frac{1}{x^4+1}\,\mathrm{d}x .$$

第一个用 6.5.2 的方法：极点 $e^{i(2k+1)\pi/4}$，上半平面两个，留数 $-z_k/4$；分子 $z^2$ 让它变成 $-z_k^3/4=-z_k\cdot z_k^2/4$。算下来

$$\int_{-\infty}^{\infty}\frac{x^2}{x^4+1}\,\mathrm{d}x=\frac{\pi}{\sqrt2},
\qquad
\int_{-\infty}^{\infty}\frac{1}{x^4+1}\,\mathrm{d}x=\frac{\pi}{\sqrt2}.$$

（两式相等不是巧合：代换 $x\to1/x$ 把 $\mathrm{d}x/(x^4+1)$ 换成 $x^2\mathrm{d}x/(x^4+1)$。）相加：

$$\int_{-\infty}^{\infty}\frac{x^2+1}{x^4+1}\,\mathrm{d}x=\pi\sqrt2 .$$


### 习题 6.13–6.24

**6.13** $\Omega=\omega_0\sqrt{1-\gamma^2/(4\omega_0^2)}=\omega_0\sqrt{1-0.0025}=0.99875\,\omega_0$。品质因子 $Q=\Omega/\gamma\approx9.99\approx10$。能量 $\propto e^{-\gamma t}$，衰减到 $1/e$ 需 $t=1/\gamma=10/\omega_0$。一个周期是 $2\pi/\Omega$，故

$$N=\frac{1/\gamma}{2\pi/\Omega}=\frac{\Omega}{2\pi\gamma}=\frac{Q}{2\pi}\approx1.59 .$$

不足两个周期。$Q$ 的物理意义就是"振铃能维持多少个弧度"：$Q\approx10$ 意味着约 10 rad，即 1.6 周。


**6.14** 角度积分与例 6.3 相同，给出 $2\sin(kr)/(kr)$，但分母多一个 $k^2+\kappa^2$：

$$\varphi(r)=\frac{q}{4\pi^2\varepsilon_0r}\int_0^{\infty}\frac{k\sin(kr)}{k^2+\kappa^2}\,\mathrm{d}k .$$

被积函数是 $k$ 的偶函数（$k\sin kr$ 偶），所以 $\int_0^\infty=\frac12\int_{-\infty}^\infty$。用 6.6 节：$f=k/(k^2+\kappa^2)$，极点 $i\kappa$，留数 $\dfrac{i\kappa e^{-\kappa r}}{2i\kappa}=\dfrac{e^{-\kappa r}}{2}$，故全实轴积分 $=i\pi e^{-\kappa r}$，取虚部得 $\pi e^{-\kappa r}$。于是

$$\int_0^{\infty}\frac{k\sin(kr)}{k^2+\kappa^2}\,\mathrm{d}k=\frac{\pi}{2}e^{-\kappa r},
\qquad
\varphi(r)=\frac{q}{4\pi\varepsilon_0}\frac{e^{-\kappa r}}{r}.$$

与例 6.1 对比：三维是 $e^{-\kappa r}/r$，一维是 $e^{-\kappa|x|}$。**三维多一个 $1/r$，所以 $\kappa\to0$ 时三维给出有限的库仑势，一维却发散**—这是维度决定力程的又一个例子。


**6.15** $h(t)=\sin(Wt)/(\pi t)$ 在 $t=0$ 有界（$=W/\pi$），所以 $\int_{-\infty}^\infty$ 是普通收敛积分，但**原函数是正弦积分**，只能靠留数。写成虚部：$\sin(Wt)=\operatorname{Im}e^{iWt}$，考虑 $\int e^{iWt}/t\,\mathrm{d}t$，$t=0$ 有一阶极点，需绕（从上方，顺时针）：

$$\mathrm{P.V.}\int_{-\infty}^{\infty}\frac{e^{iWt}}{t}\,\mathrm{d}t=i\pi
\quad\Longrightarrow\quad
\int_{-\infty}^{\infty}\frac{\sin(Wt)}{t}\,\mathrm{d}t=\pi .$$

所以 $\int h\,\mathrm{d}t=\pi/\pi=1$。**"为什么还要用主值"**：$\sin(Wt)/t$ 本身在 $0$ 有界，但它不是我们直接积的对象—我们积的是 $e^{iWt}/t$，后者在 $0$ 有极点。这个"提升成复指数后多出极点"的现象，与例 6.3 是同一件事。物理上 $\int h=1$ 就是说：单位冲激的"总面积"经过滤波器不变，直流增益为 1。


**6.16** $\sigma(\omega)=\sigma_0/(1-i\omega\tau)$。极点在 $1-i\omega\tau=0$，即 $\omega=-i/\tau$，**下半平面**，所以因果性满足（上半平面解析）。$\operatorname{Re}\sigma=\sigma_0/(1+\omega^2\tau^2)$，于是

$$\int_0^{\infty}\operatorname{Re}\sigma(\omega)\,\mathrm{d}\omega=\sigma_0\int_0^{\infty}\frac{\mathrm{d}\omega}{1+\omega^2\tau^2}=\frac{\pi\sigma_0}{2\tau}.$$

这个积分与 $f$ 求和规则同源：它等于 $\frac{\pi e^2n}{2m}$（把 $\sigma_0=ne^2\tau/m$ 代入即得），只依赖电子密度，与碰撞时间无关。**碰撞越频繁（$\tau$ 小），谱越宽越矮，但加权面积不变**—这就是"电子数守恒"在光学里的表现。


**6.17** $\sum_k\to(L/2\pi)\int\mathrm{d}k$，$\omega=ck$，两个偏振给因子 2：

$$u=\frac{1}{L}\cdot2\cdot\frac{L}{2\pi}\int_0^{\infty}\mathrm{d}k\,\frac{\hbar ck}{e^{\beta\hbar ck}-1}
=\frac{\hbar}{\pi}\int_0^{\infty}\frac{\omega\,\mathrm{d}\omega}{e^{\beta\hbar\omega}-1}.$$

代 $x=\beta\hbar\omega$：$u=\dfrac{1}{\pi\hbar c\beta^2}\displaystyle\int_0^{\infty}\frac{x\,\mathrm{d}x}{e^x-1}=\dfrac{1}{\pi\hbar c\beta^2}\cdot\Gamma(2)\zeta(2)=\dfrac{\pi(k_BT)^2}{6\hbar c}$。

与三维的 $u\propto T^4$ 对比：**$d$ 维光子气的能量密度 $\propto T^{d+1}$**（态密度 $\omega^{d-1}$，乘 $\omega$ 给 $\omega^d$，积分给 $\Gamma(d+1)\zeta(d+1)$）。一维是 $T^2$，三维是 $T^4$。维数直接决定温度幂次，这是"为什么三维斯特藩–玻尔兹曼定律是四次方"的最简解释。


**6.18** 分母 $1-i\omega RC=-iRC(\omega+i/(RC))$，极点 $\omega_0=-i/(RC)$，**下半平面**。$t>0$ 时 $e^{-i\omega t}$ 要求 $y<0$ 才衰减，所以往下闭合，顺时针，捕获这个极点：

$$V(t)=-2\pi i\cdot\frac{e^{-i\omega_0t}}{-iRC}\cdot\frac{1}{2\pi}
=\frac{1}{RC}e^{-t/(RC)},\qquad t>0 .$$

$t<0$ 时往上闭合，上半平面无极点，$V=0$。合起来 $V(t)=\dfrac{\theta(t)}{RC}e^{-t/RC}$。检验：

$$\int_0^{\infty}\frac{e^{-t/RC}}{RC}\,\mathrm{d}t=1 .$$

（单位冲激的"总电荷"守恒—电容最终充到电压 1，电量 $C\cdot1=C$，而冲激给的总电荷是 $\int\delta\,\mathrm{d}t=1$ 乘上……这里取的是单位冲激的电压响应，积分归一于 1。）


**6.19** 代换 $u=2(E-E_0)/\Gamma$：

$$\int_{-\infty}^{\infty}\frac{\sigma_{\max}\,\mathrm{d}E}{1+4(E-E_0)^2/\Gamma^2}
=\sigma_{\max}\frac{\Gamma}{2}\int_{-\infty}^{\infty}\frac{\mathrm{d}u}{1+u^2}
=\frac{\pi\Gamma}{2}\sigma_{\max}.$$

**峰面积 $=\frac{\pi}{2}\times$ 峰高 $\times$ 宽度**（半高全宽 $=\Gamma$）。若 $\Gamma=\hbar/\tau$，则面积 $\propto1/\tau$：**寿命越短，峰越宽、越矮，但"面积"（跃迁强度）不变**—这正是 $f$ 求和规则在共振散射里的版本。反过来，测到很窄的峰（小 $\Gamma$）就意味着长寿命的共振态。


**6.20** 电容上的电压方差

$$\langle V^2\rangle=\int_{-\infty}^{\infty}\frac{S_V(\omega)}{2\pi}|Z_C|^2\,\mathrm{d}\omega ,$$

其中阻抗分压给 $|Z_C/(Z_R+Z_C)|^2=1/(1+\omega^2R^2C^2)$。于是

$$\langle V^2\rangle=\frac{2k_BTR}{2\pi}\int_{-\infty}^{\infty}\frac{\mathrm{d}\omega}{1+\omega^2R^2C^2}
=\frac{k_BTR}{\pi}\cdot\frac{\pi}{RC}=\frac{k_BT}{C}.$$

$R$ 精确抵消。**这是涨落耗散定理最干净的一个例子：** 噪声正比于 $R$，带宽（积分）反比于 $R$，两者相乘抵消。结果是"温度计"式的公式 $\langle V^2\rangle=k_BT/C$，与电阻的具体值无关，所以可以用电容噪声测温。


**6.21** 用 $e^{iaz}/[z(z^2+b^2)]$（$a>0$）。上半平面极点：$z=ib$（一阶）；实轴极点：$z=0$（一阶）。实轴从左到右，$z=0$ 处从上方绕过（顺时针），$z=ib$ 在回路内。

三个留数/贡献：

$$\operatorname{Res}_{z=0}=\frac{1}{b^2},\qquad
\operatorname{Res}_{z=ib}=\frac{e^{-ab}}{ib\cdot2ib}=-\frac{e^{-ab}}{2b^2}.$$

回路内只有一个极点，$\oint=2\pi i\operatorname{Res}_{ib}=-\dfrac{i\pi e^{-ab}}{b^2}$；小半圆给 $-i\pi\operatorname{Res}_0=-\dfrac{i\pi}{b^2}$；大弧由若尔当消失。于是

$$\mathrm{P.V.}\int_{-\infty}^{\infty}\frac{e^{iax}}{x(x^2+b^2)}\,\mathrm{d}x
=-\frac{i\pi e^{-ab}}{b^2}+\frac{i\pi}{b^2}=\frac{i\pi}{b^2}\left(1-e^{-ab}\right).$$

$x(x^2+b^2)$ 在实轴上取实值，取虚部得

$$\int_{-\infty}^{\infty}\frac{\sin(ax)}{x(x^2+b^2)}\,\mathrm{d}x=\frac{\pi}{b^2}\left(1-e^{-ab}\right).$$

**拆成两个模核对：** $\dfrac{1}{x(x^2+b^2)}=\dfrac{1}{b^2}\left(\dfrac1x-\dfrac{x}{x^2+b^2}\right)$，用 $\int_0^\infty\sin(ax)/x\,\mathrm{d}x=\pi/2$ 与 $\int_0^\infty x\sin(ax)/(x^2+b^2)\,\mathrm{d}x=(\pi/2)e^{-ab}$（题 6.6 的一半），半线结果 $\dfrac{\pi}{2b^2}(1-e^{-ab})$，全实轴翻倍，一致。

### 习题 6.25–6.32


**6.22** 例 6.1 的结果是 $\varphi(x)=\dfrac{q}{2\varepsilon_0\kappa}e^{-\kappa|x|}$，直接令 $\kappa\to0$ 发散。原因是**一维库仑势没有有限的零点**：$\kappa=0$ 时方程是 $\mathrm{d}^2\varphi/\mathrm{d}x^2=-\dfrac{q}{\varepsilon_0}\delta(x)$，解是 $\varphi=-\dfrac{q}{2\varepsilon_0}|x|+C$，$|x|\to\infty$ 时发散，所以"势在无穷远为零"这个约定在一维做不到。

正确的做法是先减掉同一个常数（选定零点），再取极限：

$$\varphi(x)-\varphi(0)=\frac{q}{2\varepsilon_0\kappa}\left(e^{-\kappa|x|}-1\right)
\longrightarrow\frac{q}{2\varepsilon_0\kappa}\left(-\kappa|x|\right)
=-\frac{q}{2\varepsilon_0}|x| .$$

（用了 $e^{-\kappa|x|}\approx1-\kappa|x|$。）

**与三维对照：** 汤川势 $\dfrac{q}{4\pi\varepsilon_0}\dfrac{e^{-\kappa r}}{r}$ 在 $\kappa\to0$ 时趋于 $\dfrac{q}{4\pi\varepsilon_0 r}$，有限。**差别在维度**：三维的 $1/r$ 在无穷远衰减，一维的 $|x|$ 增长。所以"力程无限"在一维表现为势无界，在三维表现为 $1/r$。这也解释了为什么一维的库仑问题总要加一个背景（均匀正电荷）来屏蔽——那就是例 6.1 的 $\kappa$。


**6.23** 分母是 $(k^2+\kappa^2)^2$，两个二阶极点 $k=\pm i\kappa$。直接算要套多次求导，容易出错；更稳的办法是**对参数求导**。

已知（例 6.1）

$$\int_{-\infty}^{\infty}\frac{e^{ikx}}{k^2+\kappa^2}\,\mathrm{d}k=\frac{\pi}{\kappa}e^{-\kappa|x|}.$$

注意到 $\dfrac{\partial}{\partial(\kappa^2)}\dfrac{1}{k^2+\kappa^2}=-\dfrac{1}{(k^2+\kappa^2)^2}$，所以

$$G(x)=-\frac{\partial}{\partial(\kappa^2)}\left(\frac{\pi}{\kappa}e^{-\kappa|x|}\right)
=-\frac{1}{2\kappa}\frac{\partial}{\partial\kappa}\left(\frac{\pi}{\kappa}e^{-\kappa|x|}\right)
=\frac{\pi}{2\kappa}\left(\frac{1}{\kappa^2}+\frac{|x|}{\kappa}\right)e^{-\kappa|x|}.$$

即

$$G(x)=\frac{\pi}{2\kappa^3}\left(1+\kappa|x|\right)e^{-\kappa|x|}.$$

**核对：** $\kappa|x|\to0$ 时 $G\to\pi/(2\kappa^3)$（有限），与 $\int\mathrm{d}k/(k^2+\kappa^2)^2=\pi/(2\kappa^3)$ 一致；$|x|$ 大时按 $(1+\kappa|x|)e^{-\kappa|x|}$ 衰减，比单个极点多一个多项式因子——**极点的阶数决定衰减前面挂几个幂次**，这是二阶极点的一般特征。


**6.24** 由 6.7.4 节的 $i\epsilon$ 规则（注意两项一正一负）：

$$\frac{1}{\omega_0^2-\omega^2-i0^{+}\omega}
=\mathrm{P.V.}\frac{1}{\omega_0^2-\omega^2}
+\frac{i\pi}{2\omega_0}\bigl[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\bigr].$$

乘上 $\omega_p^2$，取虚部：

$$\operatorname{Im}\chi(\omega)=\frac{\pi\omega_p^2}{2\omega_0}\bigl[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\bigr].$$

**三条检验：**

1. $\displaystyle\int_{-\infty}^{\infty}\operatorname{Im}\chi\,\mathrm{d}\omega=\frac{\pi\omega_p^2}{2\omega_0}(1-1)=0$。**必须为零**，因为 $\operatorname{Im}\chi$ 是 $\omega$ 的奇函数（响应函数满足 $\chi(-\omega)=\bar\chi(\omega)$）；不选一正一负就破坏这条对称性。
2. $\displaystyle\int_0^{\infty}\omega\operatorname{Im}\chi\,\mathrm{d}\omega=\frac{\pi\omega_p^2}{2\omega_0}\cdot\omega_0=\frac{\pi}{2}\omega_p^2$，与 $\gamma\to0$ 之前的结果一致——**吸收总强度与阻尼宽度无关**。
3. 峰的位置在 $\pm\omega_0$、宽度为零、高度无穷：无阻尼共振的"吸收"就是一根线。


### 习题 6.25–6.31

**6.25** (1) 两个极点 $z=\pm ia$ 的留数**都是** $1/2$（$z/(2z)=1/2$，与 $z$ 无关）。上半圆闭合：$\oint=2\pi i\cdot\frac12=\pi i$，实轴部分（主值，奇函数）为零，所以

$$\int_{C_R}\frac{z\,\mathrm{d}z}{z^2+a^2}\longrightarrow\pi i .$$

也可以直接算：$z=Re^{i\theta}$ 时被积函数 $\approx i\,\mathrm{d}\theta$，积出 $\pi i$。

(2) 判据在 $|f|\sim1/R$ 处失效：$ML$ 估计给 $\pi R\cdot(1/R)=\pi$，不趋于零。**判据不是形式检查，它就是这次估计本身。**

(3) **没有"补救"**，因为错的是方法不是计算：无论上半圆还是下半圆都不消失（下半圆给 $-2\pi i\cdot\frac12=-\pi i$，符号相反），圆弧的贡献正是 $\pm\pi i$，不是小量。正确做法是承认这个积分**只能按主值定义**，而它的主值由奇对称性直接给零；或者把它看作希尔伯特变换 $\mathrm{P.V.}\int f(x)/(x-x_0)\mathrm{d}x$ 的一个核，那时需要 $i\epsilon$（6.7.4 节）而不是半圆闭合。**教训：先估后算；估出来不消失，就不要补这条回路。**


**6.26** 取 $f(z)=z^{\alpha-1}/(1+z)$，$0<\alpha<1$，割线取正实轴，$\arg z\in(0,2\pi)$。四段：

- 上沿：$z=xe^{i0}$，$f=\dfrac{x^{\alpha-1}}{1+x}$，从 $\epsilon$ 到 $R$；
- 下沿：$z=xe^{2\pi i}$，$z^{\alpha-1}=x^{\alpha-1}e^{2\pi i(\alpha-1)}$，$f=e^{2\pi i\alpha}\dfrac{x^{\alpha-1}}{1+x}$，从 $R$ 到 $\epsilon$，方向相反；
- 小圆：$|f|\le C\epsilon^{\alpha-1}$，长度 $2\pi\epsilon$，积分的模 $\le2\pi C\epsilon^{\alpha}\to0$；
- 大圆：$|f|\le CR^{\alpha-1}$，长度 $2\pi R$，模 $\le2\pi CR^{\alpha}/R\to0$。

上下沿相加给 $\left(1-e^{2\pi i\alpha}\right)I$，$I$ 是要求的积分。回路内唯一极点 $z=-1$，留数 $(-1)^{\alpha-1}=e^{i\pi(\alpha-1)}=-e^{i\pi\alpha}$（沿上沿分支 $\arg(-1)=\pi$）。于是

$$\left(1-e^{2\pi i\alpha}\right)I=-2\pi i\,e^{i\pi\alpha}
\quad\Longrightarrow\quad
I=\frac{-2\pi ie^{i\pi\alpha}}{e^{i\pi\alpha}(-2i\sin\pi\alpha)}=\frac{\pi}{\sin(\pi\alpha)}.$$

**三个极限。** $\alpha\to0$：$\pi/\sin(\pi\alpha)\sim1/\alpha\to\infty$，对应 $\int\mathrm{d}x/[x(1+x)]$ 的两端对数发散（$1/f$ 噪声的红外灾难）。$\alpha\to1$：同样爆炸，对应紫外发散（被积函数在高频不衰减）。$\alpha=\frac12$：$I=\pi$，与代换 $x=t^2$ 得到 $\int\mathrm{d}t/(1+t^2)=\pi$ 一致。**中间有限、两端发散**，这就是幂律谱的典型行为。


**6.27** 沿 $C_\epsilon$：$z-z_0=\epsilon e^{i\theta}$，$\mathrm{d}z=i\epsilon e^{i\theta}\mathrm{d}\theta$，

$$\int_{C_\epsilon}\frac{\mathrm{d}z}{(z-z_0)^2}
=\int\frac{i\epsilon e^{i\theta}}{\epsilon^2e^{2i\theta}}\,\mathrm{d}\theta
=\frac{i}{\epsilon}\int e^{-i\theta}\,\mathrm{d}\theta\sim\frac{1}{\epsilon}.$$

半圈给 $i(1-(-1))/\epsilon=2i/\epsilon$，模按 $1/\epsilon$ 发散。**物理对应：** 临界阻尼振子的响应函数在 $\gamma=2\omega_0$ 时两个极点合并成二阶极点（$\omega_\pm=-i\gamma/2$，$\Omega=0$），对应"响应 $\propto te^{-\gamma t/2}$"而不是振荡；另一个更极端的例子是自由粒子 $f=1/\omega^2$（无回复力、无阻尼），双极点正在实轴 $0$ 上，积分 $\int\mathrm{d}\omega/\omega^2$ 在红外发散，对应一维自由粒子的红外灾难。


**6.28** (1) $\gamma<0$ 时 $\operatorname{Im}\omega_\pm=-\gamma/2>0$，两个极点进入**上半平面**。$\chi$ 在上半平面不再解析（极点在那里），色散关系的前提失效。

(2) $t<0$ 时回路往上闭合，上半平面有两个极点，被捕获，响应不为零且按 $e^{|\gamma||t|/2}$ **指数增长**：

$$x(t)\propto e^{-\gamma t/2}\sin(\Omega t),\quad t<0 .$$

即"在被踢之前就已经在振荡并且越来越大"，非因果。

(3) $Q=\Omega/|\gamma|$ 是"增长时间 $1/|\gamma|$ 内的弧度数"。$Q$ 大时系统在 $\sim Q/2\pi$ 个周期内还保持很好的振荡，同时那个"预响应"也是同样长的相干振荡—它在 $t<0$ 上积累的振幅与 $t>0$ 上的一样可观。所以**高 $Q$ 系统的非因果性最容易被察觉**（低 $Q$ 系统的预响应只存在 $\sim1/|\gamma|$ 的短时间内，容易被噪声掩埋）。这也解释了为什么激光/增益介质里"极点进上半平面"是一个必须严肃对待的判据，而不是学究式的挑剔。

### 概念与判断 6.33–6.41


**6.29** 设 $\gamma_1$（外）与 $\gamma_2$（内）同向，$f$ 在两者之间的环形区域内解析。把内边界**反向**记作 $-\gamma_2$，则 $\gamma_1+(-\gamma_2)$ 围成的区域是单连通的，$f$ 在其内部和边界上解析。由柯西定理

$$\oint_{\gamma_1}f\,\mathrm{d}z+\oint_{-\gamma_2}f\,\mathrm{d}z=0
\quad\Longrightarrow\quad
\oint_{\gamma_1}f\,\mathrm{d}z=\oint_{\gamma_2}f\,\mathrm{d}z .$$

**关键的两点：** (i) 环形区域是"两连通"的，不能直接用柯西定理，必须先把内边界反向拼成一条复合闭路径；(ii) 方向不能错——若 $\gamma_2$ 取成反向，等号右边会多一个负号。

**推论：** 回路可以在解析区域里连续变形（不扫过奇点）而不改变积分值。这就是 6.3.3 节"变形不变性"的严格版本，也是把大半圆缩成小圆、把钥匙孔收窄的依据。


**6.30** (a) $\sqrt{z}/(1+z)$：**不能**直接用。$z=0$ 是支点，不是孤立奇点；绕一圈函数值变号，上下沿不抵消。补救：取沿正实轴的支割线，用钥匙孔回路；结果里会出现 $1-e^{i\pi}=-2$ 这类因子。

(b) $\ln z/(1+z^2)$：**不能**直接用，理由同上（$z=0$ 支点）。补救：同样的钥匙孔，割线两侧 $\ln z$ 差 $2\pi i$，那个差不抵消，反而贡献出原积分。

(c) $e^{1/z}/(z-1)$：**能**。$z=0$ 是本性奇点，但它是**孤立**的——留数定理只要求孤立，不要求是极点。留数要读洛朗系数：$e^{1/z}/(z-1)=-e^{1/z}(1+z+z^2+\cdots)$，$1/z$ 的系数来自 $e^{1/z}$ 的常数项乘 $-1$，即 $-1$。（$z=1$ 处是一阶极点，留数 $e$。）

(d) $1/\sin(1/z)$：**不能**。$z=0$ 附近有无穷多个奇点（$1/z=n\pi$ 的解堆积到 $0$），奇点**不孤立**，留数定理"有限个孤立奇点"的前提不成立。

**判据一句话：奇点必须是孤立的（极点或本性），否则先换围道（钥匙孔），或者根本不能用留数。**


**6.31** 先把 $f$ 拆开：$\dfrac{1}{z(z-1)}=\dfrac{1}{z-1}-\dfrac{1}{z}$。

**(1) $0<\lvert z\rvert<1$：** 把 $\dfrac{1}{z-1}=-\dfrac{1}{1-z}$ 按几何级数展开，

$$f(z)=-\frac{1}{z}-1-z-z^2-\cdots
\qquad (0<\lvert z\rvert<1),$$

$1/z$ 的系数是 $-1$。

**(2) $1<\lvert z\rvert<\infty$：** 这次把 $\dfrac{1}{z-1}=\dfrac{1}{z}\cdot\dfrac{1}{1-1/z}$ 展开，

$$f(z)=\frac{1}{z^2}+\frac{1}{z^3}+\frac{1}{z^4}+\cdots
-\frac{1}{z}
=\frac{1}{z^2}+\frac{1}{z^3}+\cdots$$

（$-\dfrac{1}{z}$ 与 $\dfrac{1}{z}$ 抵消！）这个展开里**没有** $1/z$ 项。

**(3) 为什么留数仍是 $-1$：** 留数由**贴着奇点的那一个**展开定义，也就是 $0<\lvert z-z_0\rvert<R$ 这个最内层的去心圆盘。外层展开描述的是远处（包括无穷远点）的行为，跟 $z_0$ 处的留数无关。物理上也对：$z=0$ 处那个模式的耦合强度，不该依赖你在多远的地方做展开。


### 概念与判断 6.32–6.40

**6.32** 不对。缺的条件是"闭曲线内部及边界上处处解析"。反例：$f=1/z$ 在 $|z|=1$ 上解析、在环外解析，但积分 $2\pi i\ne0$，因为原点（奇点）在内部。正确说法是"内部无奇点则积分为零"。


**6.33** 不对。正例：$f=1/z^2$，弧上 $\sim1/R^2$，积分 $\sim1/R\to0$。反例：$f=1/z$，弧上积分恒为 $2\pi i$（与 $R$ 无关）；$f=z/(z^2+a^2)$，弧上给 $\pi i$。判据是 $|f|\sim1/R^{1+\varepsilon}$，即分母次数比分子至少高 2。


**6.34** 不对。除了实轴无极点，还需要：(i) 补上的弧上积分趋于零（衰减够快，或靠若尔当引理）；(ii) 若含 $e^{iaz}$，$a$ 的符号决定往哪个半平面闭合，方向错了被积函数在那个半平面指数爆炸；(iii) 多值函数还要避开支点。方向选错时，回路内的极点数变了，答案会差出 $2\pi i$ 乘某个留数，或者干脆发散。


**6.35** 不对。只有在普通积分收敛时两者才相等。反例：$\mathrm{P.V.}\int_{-1}^{1}\mathrm{d}x/x=0$，而普通积分发散；$\int\cos x/x\,\mathrm{d}x$ 只有主值。物理上：无阻尼共振（$\gamma=0$）的吸收是一个 $\delta$ 函数，只能用 $i\epsilon$ 和主值来定义，这时"主值"和"积分值"是两个不同的物理量（色散部分 vs 吸收部分），混用会得到错误的吸收谱。


**6.36** 不对，只对**一阶**极点成立。二阶极点时 $f=a_{-2}/(z-z_0)^2+\cdots$，沿小半圆的积分按 $1/\epsilon$ 发散，半圈贡献不存在有限极限，主值也不存在。这与 6.4.2 的"阶数决定一切"一致：留数是 $a_{-1}$，只有它在一圈积分后存活，二阶极点的 $a_{-2}$ 需要 $1/\epsilon$ 才能体现，散掉了。


**6.37** 第一句对，第二句对但**需要单连通**。

**第一句：** 由柯西–黎曼条件交叉求导，$\partial^2u/\partial x^2=-\partial^2u/\partial y^2$，所以 $\nabla^2u=\nabla^2v=0$。这一步只用到解析（二阶导数连续），不需要额外条件。

**第二句：** 给定调和函数 $u$，要找共轭调和函数 $v$ 使 $u+iv$ 解析。由柯西–黎曼条件，$v$ 必须满足 $\partial v/\partial y=\partial u/\partial x$、$\partial v/\partial x=-\partial u/\partial y$，这是全微分方程；**在单连通区域内**可积性条件（$\partial^2u/\partial x^2+\partial^2u/\partial y^2=0$，正是调和性）保证 $v$ 存在且只差一个常数。在**多连通**区域（比如挖掉原点的圆环）不一定存在——反例是 $u=\ln r$，它的"共轭"是 $\theta$，而 $\theta$ 是多值的，绕原点一圈变 $2\pi$。

**读法：** "解析函数 = 二维调和场"这句话在单连通区域里是双向的；一旦区域有洞，$\ln z$ 就出来了，而它正是支点（6.7.5 节）的来源。


**6.38** 对，这是**可去奇点定理**（黎曼可去奇点定理）：有界则主部为零，奇点可去。

用来判断两个例子：

- $\sin z/z$：在 $0<\lvert z\rvert<1$ 内 $\lvert\sin z/z\rvert\le\cosh1<2$，有界 ⟹ 可去奇点 ✓（与 $\sin z/z=1-z^2/6+\cdots$ 一致）。
- $e^{1/z}$：在 $z\to0$ 沿途取 $z=1/n$（$n$ 为正整数），$e^{1/z}=e^{n}\to\infty$，无界 ⟹ 不是可去奇点。事实上是本性奇点（主部无穷多项）。

**判据的实用价值：** 看见"$\lvert f\rvert$ 有界"就敢判可去，不用展开级数。判断极点还是本性则要看主部——本性问题这套办法给不出答案。


**6.39** 不对，要加条件。

**成立的写法：** 若 $R$ 在实轴上取**实值**，且 $\int R(x)\cos(ax)\mathrm{d}x$ 与 $\int R(x)\sin(ax)\mathrm{d}x$ 都收敛，则

$$\int R(x)\cos(ax)\,\mathrm{d}x=\operatorname{Re}\int R(x)e^{iax}\,\mathrm{d}x .$$

因为 $e^{iax}=\cos ax+i\sin ax$，取实部就是把两项分开，而两项各自合法。

**出错的情形：** $R$ 带 $i$（比如响应函数的分子含 $i$）。这时 $\operatorname{Re}[R e^{iax}]$ 里混进了 $\sin$ 的贡献，取实部不再等于 $\cos$ 的积分。正确做法是先把 $R$ 的实部虚部分开，或者对 $R e^{iax}$ 整体算完再取需要的组合。

**还有一种情形：** $\sin$ 部分发散而 $\cos$ 部分收敛（或反过来）。这时 $e^{iax}$ 的整体积分只能按主值理解，直接取实部会得到错误的结果——必须先确认两部分各自的收敛性。


**6.40** 错。正确的说法是：**回路可以在不扫过奇点的前提下连续变形，积分值不变**。

漏掉"不扫过奇点"这一条，就会得出"$\oint 1/z\,\mathrm{d}z$ 与回路无关"的结论，而实际上绕原点的回路给 $2\pi i$、不绕的给 $0$。

**推论两条：** (i) 变形时回路扫过的区域内必须处处解析；(ii) 若两条回路围住的奇点不同，它们的积分之差等于"多围住的那几个奇点"的留数之和乘 $2\pi i$。**回路不是随便变的，它只能在不碰奇点的前提下变。**

## 第 7 章

**7.1** 在 $|z|=a$ 上令 $z=ae^{i\theta}$，则 $a^{2}/z=ae^{-i\theta}$，于是 $w=U(2a\cos\theta)$ 是实数，$\psi=\operatorname{Im}w=0$。物面是 $\psi=0$ 这条流线，法向速度为零，正是无穿透条件。反过来，$|z|=a$ 上 $v_r=0$ 也可以直接从 $z'$ 算出，两条路一致。

**7.2** $\phi=U(x^{2}-y^{2})$，$\psi=2Uxy$。等势线是双曲线族 $x^{2}-y^{2}=$ 常数，流线是 $xy=$ 常数（另一族双曲线，渐近线为两坐标轴）。驻点在原点，速度 $u=2Ux$、$v=-2Uy$：沿 $x$ 轴流入、沿 $y$ 轴流出。物理上这是"流体从两边挤进一个直角角落再流出"的驻点流，两坐标轴是壁面。

**7.3** 像为椭圆，半轴 $A=R+a^{2}/R$、$B=R-a^{2}/R$，焦点恒在 $z=\pm2a$（$A^{2}-B^{2}=4a^{2}$）。$R=1.5a$ 时 $A=2.17a$、$B=0.83a$，厚度比 $2B/2A=38\%$。$R\to a$ 时 $B\to0$，退化为平板 $-2a\le x\le2a$。

**7.4** $z'=1-a^{2}/\zeta^{2}=0$ 给出 $\zeta=\pm a$，像点 $z=\pm2a$。在 $|\zeta|<a$ 内，因 $z(\zeta)=z(a^{2}/\zeta)$ 而二对一，映射不单叶：圆内的点会映到与圆外相同的像上，"翼型"会自交成两条曲线。所以只能取圆外 $|\zeta|>a$，这时映射单叶，像平面是割开线段 $[-2a,2a]$ 的区域。

**7.5** $\Gamma=2\pi Ua$ 时 $\sin\beta=1/2$、$\beta=30^\circ$，驻点为 $z=\pm0.866a+0.5ai$。切向速度 $v_\theta=-(2U\sin\theta-\Gamma/2\pi a)$：顶部 $\theta=\pi/2$ 得 $-U$（大小 $U$），底部得 $-3U$（大小 $3U$）。

**7.6** $p_{\text{顶}}=\frac12\rho(U^{2}-U^{2})+p_\infty=p_\infty$，$p_{\text{底}}=\frac12\rho(U^{2}-9U^{2})+p_\infty=p_\infty-4\rho U^{2}$。压差 $4\rho U^{2}$，顶部压力大、底部小，合力向下。由 7.4.4，$|F|=\rho U|\Gamma|=2\pi\rho U^{2}a$，与 7.4.3 的积分结果一致。

**7.7** $R=|1.10-0.09i|=1.104$，$\theta_T=\arg(1.10-0.09i)=-4.68^\circ$，$\Gamma_K=4\pi UR\sin(\theta_T-\alpha)=4\pi\times1\times1.104\times\sin(-8.68^\circ)=-2.09$。负号即顺时针，与升力向上的方向一致。

**7.8** $\frac{\mathrm{d}C_L}{\mathrm{d}\alpha}=\frac{8\pi R}{c}\cos(\alpha-\theta_T)\approx\frac{8\pi R}{c}$。薄翼 $R=a$、$c=4a$ 时得 $2\pi$ 每弧度 $=0.110$ 每度。这就是"升力线斜率与翼型无关"的定量版本。

**7.9** $\frac{\mathrm{d}w}{\mathrm{d}z}=U(1-a^{2}/z^{2})$，平方得 $U^{2}(1-2a^{2}/z^{2}+a^{4}/z^{4})$，只有 $z^{0}$、$z^{-2}$、$z^{-4}$ 三个幂次，**没有 $1/z$ 项**，留数为零，故 $F_x-iF_y=0$。

**7.10** $w=\mu/z$ 时 $\frac{\mathrm{d}w}{\mathrm{d}z}=-\mu/z^{2}$，平方后是 $\mu^{2}/z^{4}$，留数为零，所以不受力。这与圆柱不受力并不矛盾：偶极子只是"远场等效于一个圆柱"的近似，它本身没有环量；而力只由 $1/z$ 项（点涡）产生。

**7.11** $\zeta=ia$ 时 $z=\dfrac{ia-a}{ia+a}=\dfrac{i-1}{i+1}=i$。实轴 $\zeta=t$ 满足 $|t-a|=|t+a|$，故 $|z|=1$，实轴映成单位圆；$\zeta=0$ 映成 $z=-1$。这是一次"半平面→圆盘"的标准搬运。

**7.12** 内角 $60^\circ$ 的楔形被映成半平面（内角 $180^\circ$），角度放大 $3$ 倍。原点处 $z'=3\zeta^{2}=0$，不保角，这正是"幂映射用来造角"的机制。

**7.13** $C_L=\dfrac{2mg}{\rho U^{2}S}=0.44$。由 $C_L=2\pi(\alpha-\theta_T)$ 得 $\alpha-\theta_T=0.070\ \mathrm{rad}=4.0^\circ$，取 $\theta_T=-3^\circ$ 则 $\alpha=1.0^\circ$。真实客机巡航攻角约 $2^\circ$–$3^\circ$，差别来自真实翼型的 $\theta_T$ 更负（弯度更大）。

**7.14** $C_L=2\pi\sin10^\circ=1.09$，$L=\frac12\rho U^{2}AC_L=\frac12\times1.2\times144\times0.8\times1.09=75\ \mathrm{N}$。攻角减半到 $5^\circ$：$C_L=0.55$，$L=38\ \mathrm{N}$，约减半（比一半略多，因为 $\sin$ 不是线性的）。

**7.15** $\omega=2\pi\times8=50\ \mathrm{rad/s}$，$\Gamma=2\pi R^{2}\omega=3.8\ \mathrm{m^{2}/s}$，$L'=\rho U\Gamma=1.2\times30\times3.8=1.4\times10^{2}\ \mathrm{N/m}$。取有效长度 $2R=0.22\ \mathrm{m}$ 得 $F=30\ \mathrm{N}$，$a=70\ \mathrm{m/s^{2}}\approx7g$，$1\ \mathrm{s}$ 侧移 $35\ \mathrm{m}$。实际值小得多：无滑移假设把环量高估了几倍，真实球面的边界层会分离，$\Gamma$ 只有这个值的三分之一左右。

**7.16** (a) 零升力角就是 $\theta_T=-4.0^\circ$：$\alpha$ 取这个值时 $C_L=0$。(b) $a=c/4=0.50\ \mathrm{m}$，$\Gamma=4\pi UR\sin(\theta_T-\alpha)=4\pi\times60\times0.5\times\sin(-10^\circ)=-65.5\ \mathrm{m^{2}/s}$；$L'=\rho U|\Gamma|=1.2\times60\times65.5=4.7\times10^{3}\ \mathrm{N/m}$。核对：$C_L=L'/(\frac12\rho U^{2}c)=4.7\times10^{3}/4320=1.09$，与 $2\pi\sin10^\circ=1.09$ 一致。(c) $\alpha=12^\circ$ 时 $\theta_T-\alpha=-16^\circ$，$L'=1.2\times60\times377\times\sin16^\circ=7.5\times10^{3}\ \mathrm{N/m}$，只有原来的 $1.59$ 倍。因为升力随 $\sin(\alpha-\theta_T)$ 走，不是随角度线性；真实翼型到这个攻角已经接近失速。

**7.17** $C_L=2\pi\sin20^\circ=2.15$，$L=\frac12\times1.2\times64\times30\times2.15=2.5\times10^{3}\ \mathrm{N}$。升力垂直于来流；当船头与来流成 $45^\circ$ 时，升力沿船头方向的分量是 $L\sin45^\circ=1.7\ \mathrm{kN}$，而侧向分量由龙骨抵消。**帆船"逆风前进"靠的是升力的前向分量，不是"风推着走"。**

**7.18** $L'=\frac12\rho U^{2}cC_L=\frac12\times1.2\times4\times10^{4}\times0.3\times0.6=4.3\times10^{3}\ \mathrm{N/m}$。旋翼剖面的相对速度沿展向变化（$U\pm\Omega r$），后退叶片那一侧速度小、容易失速，所以桨叶要扭转、变距，并限制前进比。

**7.19** (a) 平飞时升力等于重力：$L=mg=4.9\times10^{3}\ \mathrm{N}$，单位展长 $L'=L/b=3.3\times10^{2}\ \mathrm{N/m}$，$\Gamma=L'/(\rho U)=327/(1.2\times25)=10.9\ \mathrm{m^{2}/s}$。(b) $\sin(\alpha-\theta_T)=\dfrac{\Gamma}{4\pi UR}=\dfrac{10.9}{4\pi\times25\times0.5}=0.069$，得 $\alpha-\theta_T=4.0^\circ$，即 $\alpha=2.0^\circ$——与滑翔机实际的小攻角同量级。(c) $U=30\ \mathrm{m/s}$ 时 $\Gamma$ 降到 $9.1$，而 $\sin(\alpha-\theta_T)=\Gamma/(4\pi UR)$ 的分母也变大，得 $2.8^\circ$，攻角降到约 $0.8^\circ$。**升力系数按 $1/U^{2}$ 掉，所以飞得越快、越要压平机头。**

**7.20** $\alpha=5^\circ$：结冰前 $C_L=2\pi\sin(5^\circ+4^\circ)=0.98$，结冰后 $C_L=2\pi\sin(5^\circ+1^\circ)=0.66$，下降 $33\%$。**结冰不是"表面粗糙一点"，它直接把升力砍掉三分之一**——这就是飞机要除冰的原因。

**7.21** 起飞攻角取 $8^\circ$：不放襟翼 $\theta_T=-3^\circ$，$C_L=2\pi\sin11^\circ=1.20$；放襟翼 $\theta_T=-10^\circ$，$C_L=2\pi\sin18^\circ=1.94$，增加 $62\%$。同一速度下升力增加六成，起飞滑跑距离因此大幅缩短。

**7.22** $\omega=2\pi\ \mathrm{rad/s}$，$\Gamma=2\pi R^{2}\omega=2\pi\times0.0225\times6.28=0.89$，$L'=\rho U\Gamma=1.2\times20\times0.89=21\ \mathrm{N/m}$，总侧向力 $L'h=3.2\times10^{2}\ \mathrm{N}$。不转时的风阻为 $\frac12\rho U^{2}DC_Dh=\frac12\times1.2\times400\times0.3\times1.2\times15=1.3\times10^{3}\ \mathrm{N}$。**马格努斯力只有风阻的四分之一，但方向垂直于风，对细长结构（烟囱、桅杆、拉索）的横向振动很重要。**

**7.23** 平板（弦长 $c$、$R=a=c/4$）：$L'=4\pi\rho U^{2}R\sin\alpha=\pi\rho U^{2}c\sin\alpha$，$C_L=2\pi\sin6^\circ=0.66$，$L'=\pi\times1.2\times1600\times1\times0.105=6.3\times10^{2}\ \mathrm{N/m}$。换成 $12\%$ 厚的对称翼型：零升力角仍为零、斜率仍是 $2\pi$（因为对称、$R/c$ 因子几乎不变），**$C_L$ 基本不变**；厚度改善的是失速特性与结构，不是升力。

**7.24** 失速意味着后缘分离：流动不再从后缘平滑离开，"后驻点落在后缘"这条前提不成立。库塔条件失效后，实际环量小于 $\Gamma_K$ 并随攻角下降，升力线在 $15^\circ$ 左右折断。**所以失速不是"升力算大了"，而是"库塔条件这个模型假设整体失效"。**

**7.25** 压力沿物面积分给出 $F_x-iF_y=-i\oint p\,\mathrm{d}\bar z$（用 $\mathrm{d}\bar z=\mathrm{d}x-i\,\mathrm{d}y$ 与外法向的关系）。代入伯努利 $p=p_\infty+\frac12\rho(U^{2}-|w'|^{2})$，常数项在闭合回路上积分为零。物面是流线，$\psi$ 为常数，故 $\mathrm{d}w=w'\mathrm{d}z$ 是实微分，$\mathrm{d}\bar z$ 与 $\mathrm{d}z$ 可互换，得 $\oint|w'|^{2}\mathrm{d}\bar z=\oint(w')^{2}\mathrm{d}z$。合起来就是布拉修斯公式 $\frac{i\rho}{2}\oint(w')^{2}\mathrm{d}z$。

**7.26** 无环量时 $(w')^{2}=U^{2}(1-2a^{2}/z^{2}+a^{4}/z^{4})$，没有 $1/z$ 项，回路积分恒为零，阻力严格为零。真实圆柱在 $Re=10^{5}$ 时 $C_D\approx1.2$，几乎全部来自边界层分离造成的尾流低压（压差阻力），摩擦阻力只占很小一部分。**理想理论连"阻力存在"这件事都说不出来。**

**7.27** 在 $\zeta=a$ 附近，$z-2a\approx(\zeta-a)^{2}/a$，且 $\frac{\mathrm{d}w}{\mathrm{d}z}=\frac{W'(\zeta)}{z'(\zeta)}$、$z'\approx\frac{2}{a}(\zeta-a)$。若 $W'(a)=0$，则 $W'\approx W''(a)(\zeta-a)$，两者相除后极限为 $\frac{a}{2}W''(a)$——**有限**。若不满足库塔条件，$W'(a)\neq0$，速度按 $|\zeta-a|^{-1}\propto|z-2a|^{-1/2}$ 发散，即 7.3.2 的薄板边缘指数。

**7.28** 设涡强 $\gamma(x)$ 分布，诱导速度为 $\frac{1}{2\pi}\int\frac{\gamma(x')\mathrm{d}x'}{x-x'}$，物面法向速度为零给出积分方程，后缘条件 $\gamma(a)=0$ 定出解 $\gamma(x)=2U\sin\alpha\sqrt{\frac{a+x}{a-x}}$。总环量 $\Gamma=\int_{-a}^{a}\gamma\,\mathrm{d}x=-2\pi Ua\sin\alpha$，故 $L'=\rho U|\Gamma|=2\pi\rho U^{2}a\sin\alpha$，$C_L=L'/(\frac12\rho U^{2}\cdot2a)=2\pi\sin\alpha$。与保角映射的结果一致。

**7.29** 地面可以用镜像法处理：在地面下方放一个反号的镜像翼型（环量取反号），它对真实翼型诱导的速度方向与地面相反，抵消掉一部分下洗。$h$ 越小，镜像越近，下洗抵消越多，**有效攻角变大、升力上升、诱导阻力下降**。这就是地效飞行器贴水面飞的原因；也是风洞实验里模型离壁太近会"虚假增升"的原因。

**7.30** 椭圆环量分布 $\Gamma(y)=\Gamma_0\sqrt{1-(2y/b)^{2}}$ 给出沿展向常数的下洗 $w_i=\Gamma_0/(2b)$，故 $\alpha_i=w_i/U=\frac{C_L}{\pi AR}$，诱导阻力 $C_{D,i}=C_L\alpha_i=\frac{C_L^{2}}{\pi AR}$。**$AR$ 越大，$C_{D,i}$ 越小**——这就是滑翔机翼展很长、而战斗机翼展很短的原因。

**7.31** 二维理论的斜率是 $6.28$ 每弧度。(a) 组斜率 $5.1$，比二维低 $19\%$，符合有限展长的修正（$2\pi/(1+2/AR)$，对应 $AR\approx8$）；零升力角 $-2.8^\circ$ 说明弯度中等。(b) 组斜率 $6.2$ 接近二维值，说明展弦比很大（或做了端板修正）；零升力角 $-6.1^\circ$ 说明弯度大。**判据：斜率看三维效应，零升力角看弯度，两者独立。**

**7.32** 错。保角映射保持的是拉普拉斯方程的形式，因为 $\nabla^{2}$ 在坐标变换下只多出一个因子 $|f'|^{2}$。纳维–斯托克斯方程含有一阶对流项和非线性项，映射后会变成变系数方程，形式不保持。**"能搬"是拉普拉斯方程的专属特权。**

**7.33** 错。没有任何物理理由要求"同时到达"，实验直接看到上表面气流先到；而且这个说法给不出定量结果。上表面更快的原因是环量：环量被后缘条件选定之后，上表面的速度就定了。

**7.34** 错。升力恰恰是势流理论算出来的：$L=\rho U\Gamma$，$\Gamma$ 由库塔条件定。它算不出的是阻力。**一个只能算升力的理论，对设计机翼仍然不可或缺。**

**7.35** 错。映射只提供"把圆的结果搬过去"的通道，环量是物理条件（库塔条件）定的。换一个映射、同一个翼型，$\Gamma$ 不变。

**7.36** 错。$\Gamma$ 由"后缘速度有限"唯一确定。任意取 $\Gamma$ 会得到后缘速度发散的解（图 7.6 的虚线），那是非物理的。

**7.37** 对，但要说清"对"在哪儿：尖后缘提供了一个**确定的**后驻点位置，把 $\Gamma$ 钉死；圆后缘没有这个特殊位置，库塔条件无法表述，环量就不定，升力也就有任意性。这就是真实机翼后缘必须尖的原因。

**7.38** 错。斜率确实与形状无关，但厚度决定失速攻角、结构强度、内部油箱容积和波阻；弯度决定零升力角。**"斜率无关"只说明增益固定，不说明形状可以随便。**

**7.39** 错。理想无粘无旋流的阻力严格为零（7.4.3 的积分给出 $F_x=0$）。真实阻力来自粘性、分离和诱导，这套理论一个字都算不出来。

**7.40** 错。库塔条件是**物理条件**，来自真实流动（粘性、附着流、尖后缘）的观察，数学上没有任何东西禁止 $\Gamma$ 取别的值。它的地位是"把实验事实翻译成一条数学约束"，所以它有适用范围（大雷诺数、附着流、尖后缘），也有失效的时候（失速、圆后缘）。

## 第 8 章

**8.1** 直接积分：

$$\tilde f(k)=\int_{-a/2}^{a/2}e^{-ikx}\,\mathrm{d}x=\frac{e^{-ika/2}-e^{ika/2}}{-ik}
=a\,\mathrm{sinc}\!\left(\frac{ka}{2}\right).$$

零点在 $ka/2=n\pi$，即 $k=2\pi n/a$。**脉宽 $a$ 出现在分母上**：$a$ 减半，第一个零点从 $2\pi/a$ 移到 $4\pi/a$，谱整体拉宽一倍。这就是「时域压窄、频域拉宽」在这条式子里的具体位置。

**8.2**

$$\tilde f(k)=\int_{-\infty}^{0}e^{(a-ik)x}\,\mathrm{d}x+\int_{0}^{\infty}e^{-(a+ik)x}\,\mathrm{d}x
=\frac{1}{a-ik}+\frac{1}{a+ik}=\frac{2a}{a^2+k^2}.$$

结果实、偶、正——与 $f$ 是实偶函数一致（实偶的谱是实偶）。

**8.3** 由平移性质 $\mathcal{F}[f(x-x_0)]=e^{-ikx_0}\tilde f(k)$：

$$\mathcal{F}[\delta(x-x_0)]=e^{-ikx_0},\qquad
\mathcal{F}\left[e^{-a|x-x_0|}\right]=e^{-ikx_0}\frac{2a}{a^2+k^2}.$$

**幅度谱完全不变，只多了一个线性相位 $-kx_0$。** 平移在频域里只改相位，这是干涉、相控阵、脉冲压缩的共同基础。

**8.4** 见 8.6.1 节的配方计算，结果 $\sigma\sqrt{2\pi}\,e^{-\sigma^2k^2/2}$。$|f|^2$ 的方差 $\sigma^2/2$，$|\tilde f|^2$ 的方差 $1/(2\sigma^2)$，两者开方相乘：

$$\Delta x\,\Delta k=\frac{\sigma}{\sqrt2}\cdot\frac{1}{\sqrt2\,\sigma}=\frac12 .$$

**8.5** 分部积分：$\int f'e^{-ikx}\mathrm{d}x=[fe^{-ikx}]_{-\infty}^{\infty}+ik\int fe^{-ikx}\mathrm{d}x$。要得到 $ik\tilde f$，必须让方括号为零，即 $f(\pm\infty)=0$。

反例：$f(x)=e^{ax}$（$a>0$）在 $x\to+\infty$ 发散，变换根本不存在，等式无从谈起。更细致的例子是阶跃 $f=\theta(x)$：$f'=\delta$，$\mathcal{F}[f']=1$，而 $ik\mathcal{F}[\theta]=ik\left[\frac{1}{ik}+\pi\delta(k)\right]=1$——等式在分布意义下**仍然成立**，因为 $k\delta(k)=0$ 把边界项「吸收」进去了。**结论：边界项不为零时，等式要么失效（增长函数），要么要靠 $\delta$ 修正（阶跃、常数）。**

**8.6** 两个宽 $a$ 的矩形卷积是三角形：

$$(f*f)(x)=a-|x|,\qquad |x|<a .$$

它的变换是 $[a\,\mathrm{sinc}(ka/2)]^2$，正是两个 sinc 的乘积，卷积定理成立。三角形比矩形光滑（连续），所以谱衰减更快（$1/k^2$ 对 $1/k$）——**时域越光滑，频域衰减越快**，这条规律在傅里叶级数里已经见过。

**8.7** $\mathcal{L}[t]=1/s^2$（$\sigma_c=0$），$\mathcal{L}[t^2]=2/s^3$（$\sigma_c=0$）。

$$\mathcal{L}[e^{-3t}\cos2t]=\frac{s+3}{(s+3)^2+4},\qquad \sigma_c=-3 .$$

最后一条用了频移性质 $\mathcal{L}[e^{at}f(t)]=F(s-a)$：把 $s/(s^2+4)$ 里的 $s$ 换成 $s+3$。

**8.8**

$$\frac{1}{(s+1)(s+2)}=\frac{1}{s+1}-\frac{1}{s+2}
\quad\Longrightarrow\quad
f(t)=e^{-t}-e^{-2t}\ (t>0).$$

$f(0)=1-1=0$；$f(\infty)=0$。两个极限都对。

**8.9** 极点 $s=\pm2i$：

$$\operatorname{Res}_{2i}=\frac{2i\,e^{2it}}{4i}=\frac{e^{2it}}{2},\qquad
\operatorname{Res}_{-2i}=\frac{-2i\,e^{-2it}}{-4i}=\frac{e^{-2it}}{2},$$

$$f(t)=\frac{e^{2it}+e^{-2it}}{2}=\cos 2t .$$

**8.10** $h(t)=e^{-2t}$，阶跃响应

$$y(t)=\int_0^{t}e^{-2\tau}\,\mathrm{d}\tau=\frac{1-e^{-2t}}{2}.$$

时间常数 $\tau=1/2$，等于「极点到虚轴距离的倒数」：$|s_0|=2$。**这条对应关系（$\tau=1/|\sigma|$）比任何公式表都好用。**

**8.11** $s=-\zeta\omega_0\pm i\omega_0\sqrt{1-\zeta^2}=-10\pm i99.5$。

振荡频率 $99.5\ \text{rad/s}$（比 $\omega_0$ 略小），衰减时间 $1/(\zeta\omega_0)=0.1\ \text{s}$，$Q=1/(2\zeta)=5$。

**8.12** 变换：$sY+2Y=\frac{1}{s+1}$，故 $Y=\frac{1}{(s+1)(s+2)}$。部分分式

$$Y=\frac{1}{s+1}-\frac{1}{s+2}
\quad\Longrightarrow\quad
y(t)=e^{-t}-e^{-2t}\ (t>0).$$

检查：$y(0)=0$ ✓；$y'+2y=-e^{-t}+2e^{-2t}+2e^{-t}-2e^{-2t}=e^{-t}$ ✓。

**8.13** $\tau=1/(\alpha k^2)$。$1\ \text{mm}$ 周期：$k=6.28\times10^{3}\ \text{m}^{-1}$，$\alpha k^2=4.34\times10^{3}\ \text{s}^{-1}$，$\tau=2.3\times10^{-4}\ \text{s}$。$1\ \text{cm}$ 周期：$k$ 小十倍，$\tau$ 大百倍，$2.3\times10^{-2}\ \text{s}$。

**小尺度温度不均匀消失得快，大尺度能存很久**——所以激光加热只影响表面薄层，而大铸件的内部温度要几小时才均匀。

**8.14** 初值 $\tilde u(k,0)=Q/(\rho c_p)$，故

$$u(x,t)=\frac{Q}{\rho c_p}\cdot\frac{1}{\sqrt{4\pi\alpha t}}e^{-x^2/(4\alpha t)}.$$

扩散长度 $\ell=\sqrt{4\alpha t}$，按 $\sqrt{t}$ 增长。**这意味着扩散「跑不远」：时间加倍，距离只乘 $1.41$。**

**8.15** $g=0$，达朗贝尔解只剩两项：

$$u(x,t)=\frac{1}{2}\left[f(x-ct)+f(x+ct)\right].$$

两个半幅三角波分别向左右以 $c$ 跑。$t<a/c$ 时两个波还重叠在原点附近，$t>a/c$ 时完全分开，各走各的，形状不变。**波动方程不抹平、不展宽（无色散时）**，与热方程形成对照。

**8.16** $RC=10^{4}\times10^{-8}=10^{-4}\ \text{s}$，$f_c=1/(2\pi RC)=1592\ \text{Hz}$。

$$|H(f)|=\frac{1}{\sqrt{1+(f/f_c)^2}}:\quad
1\ \text{kHz}:0.85,\quad 3\ \text{kHz}:0.47,\quad 5\ \text{kHz}:0.30 .$$

方波的高次谐波被逐级削弱，边沿变圆，但基频基本保留——**$1\ \text{kHz}$ 方波还能看出方波的轮廓**，只是角变圆了。

**8.17** $\omega_0=1/\sqrt{LC}=1/\sqrt{10^{-4}\times10^{-10}}=10^{7}\ \text{rad/s}$，$f_0=1.59\ \text{MHz}$。

$Q=\omega_0L/R\Rightarrow R=\omega_0L/Q=10^{7}\times10^{-4}/50=20\ \Omega$。

**8.18** $BT=2\times10^{6}\times0.5\times10^{-3}=1000$，$\delta R=c/(2B)=1500/(4\times10^{6})=3.75\times10^{-4}\ \text{m}$，即 $0.38\ \text{mm}$。

**8.19** 展宽 $\Delta t=17\ \text{ps/(nm}\cdot\text{km)}\times0.1\ \text{nm}\times50\ \text{km}=85\ \text{ps}$。

比特间隔 $100\ \text{ps}$，展宽 $85\ \text{ps}$——**脉冲已经糊到相邻比特里**，必须补偿（色散补偿光纤或电子均衡）。

**8.20** 极点在 $\omega$ 平面是 $\omega=-i\gamma/2\pm\omega_0$，换成 $s$ 平面是 $s=-\gamma/2\pm i\omega_0$。到虚轴距离 $\gamma/2=5\times10^{7}\ \text{s}^{-1}$，衰减时间 $1/(\gamma/2)=20\ \text{ns}$。

振荡频率 $3\times10^{15}\ \text{rad/s}$（可见光，$\lambda\approx628\ \text{nm}$）。$Q=\omega_0/\gamma=3\times10^{7}$——**这就是原子谱线极窄的原因**。

**8.21** $\omega\tau=2\pi\times1\times1=6.28$，

$$|H|=\frac{1}{\sqrt{1+(\omega\tau)^2}}=\frac{1}{6.36}=0.157,\qquad
\varphi=-\arctan(6.28)=-81^\circ .$$

幅度只剩 $16\%$，滞后 $81^\circ$。**用时间常数 $1\ \text{s}$ 的传感器测 $1\ \text{Hz}$ 的波动，测到的基本是「平均温度」而不是波动。** 想测 $1\ \text{Hz}$，$\tau$ 要做到 $0.01\ \text{s}$ 量级。

**8.22** 令 $s=i\omega$：

$$|H|=\frac{1}{\sqrt{1+(\omega\tau)^2}},\qquad
\varphi=-\arctan(\omega\tau).$$

输出 $y=\dfrac{1}{\sqrt{1+(\omega\tau)^2}}\cos\left(\omega t-\arctan\omega\tau\right)$。

$\omega\tau\gg1$ 时 $|H|\approx1/(\omega\tau)\to0$，输出趋于零（高频被滤掉）；$\omega\tau\ll1$ 时 $|H|\approx1$、$\varphi\approx0$，输出几乎等于输入。

**8.23** 记 $\|f\|^2=\int|f|^2$。由 $\Delta k^2=\|f'\|^2/\|f\|^2$（求导性质 + 帕塞瓦尔），

$$\Delta x^2\Delta k^2=\frac{\int x^2|f|^2\int|f'|^2}{\|f\|^4}
\geq\frac{\left|\int x f^*f'\right|^2}{\|f\|^4},$$

第二步是柯西–施瓦茨。而 $\int x f^*f'=\frac12\int x(|f|^2)'=-\frac12\|f\|^2$（分部积分，边界项为零），代入得 $\Delta x^2\Delta k^2\geq1/4$。

等号要求 $f'\propto xf$，解是高斯。**高斯基是唯一达到下界的形状。**

**8.24** 用 $\delta$ 的积分表示：

$$\int|f|^2\mathrm{d}x=\int f^*(x)\left[\frac{1}{2\pi}\int\tilde f(k)e^{ikx}\mathrm{d}k\right]\mathrm{d}x
=\frac{1}{2\pi}\int\tilde f(k)\left[\int f^*(x)e^{ikx}\mathrm{d}x\right]\mathrm{d}k
=\frac{1}{2\pi}\int|\tilde f(k)|^2\mathrm{d}k .$$

中间一步交换积分次序，方括号里正是 $\tilde f^*(k)$。

**8.25** 证明见 8.4.2 节（两行）。理想积分器 $H(s)=1/s$，冲激响应 $h(t)=\theta(t)$：

$$\int_{-\infty}^{\infty}|h(t)|\,\mathrm{d}t=\int_0^{\infty}\mathrm{d}t=\infty,$$

**不绝对可积，傅里叶变换不存在**（只有分布意义下的 $1/(i\omega)+\pi\delta(\omega)$）。所以「输出 = 输入与 $h$ 的卷积」这个式子对一般输入不成立；但对零均值的输入（不含直流）仍成立——**因为积分器对直流是发散的。** 这就是为什么示波器不能测纯直流。

**8.26**

| 收敛域 | 时域信号 | 因果性 | 稳定性 |
|---|---|---|---|
| $\sigma>1$ | $e^{t}\theta(t)$ | 因果 | 不稳定（增长） |
| $\sigma<1$ | $-e^{t}\theta(-t)$ | 反因果 | 不稳定（$t\to-\infty$ 增长） |

两种都发散，但方式不同。**这说明「看极点判稳定」必须配合收敛域**：极点 $s=1$ 只告诉你「有 $e^{t}$ 这个成分」，至于它出现在 $t>0$ 还是 $t<0$，由收敛域决定。

**8.27** $t>0$ 时 $e^{i\omega t}$ 在上半平面衰减，向上闭合，围住 $\omega=ia$：

$$\int=2\pi i\cdot\frac{e^{i(ia)t}}{2ia}=\frac{\pi}{a}e^{-at}.$$

$t<0$ 时向下闭合，围住 $\omega=-ia$，结果 $\frac{\pi}{a}e^{at}$。合并：

$$\int_{-\infty}^{\infty}\frac{e^{i\omega t}}{\omega^2+a^2}\,\mathrm{d}\omega=\frac{\pi}{a}e^{-a|t|}.$$

与第 6 章的围道技巧完全一致：**用 $e^{i\omega t}$ 在哪个半平面衰减来决定闭合方向**，$t=0$ 处的「不连续」由两个半平面各贡献一半拼出来。

**8.28** 二阶系统阶跃响应

$$y(t)=1-\frac{e^{-\zeta\omega_0t}}{\sqrt{1-\zeta^2}}\sin\left(\omega_0\sqrt{1-\zeta^2}\,t+\varphi\right),\qquad \cos\varphi=\zeta .$$

对 $t$ 求导令其为零，得第一个峰在 $\omega_d t_p=\pi$，代回：

$$M_p=y(t_p)-1=\exp\left(-\frac{\pi\zeta}{\sqrt{1-\zeta^2}}\right).$$

$\zeta=0.5$：$\exp(-\pi\times0.5/0.866)=\exp(-1.814)=0.163$，过冲 $16.3\%$。

**8.29** 对 $t$ 做变换，$T(x,0)=0$：

$$s\bar T=\alpha\frac{\partial^2\bar T}{\partial x^2}
\quad\Longrightarrow\quad
\bar T=A e^{-x\sqrt{s/\alpha}},\qquad A=\frac{T_0}{s},$$

（取衰减解，舍去 $e^{+x\sqrt{s/\alpha}}$。）反变换查表：

$$T(x,t)=T_0\,\mathrm{erfc}\!\left(\frac{x}{2\sqrt{\alpha t}}\right).$$

检查：$x=0$ 时 $\mathrm{erfc}(0)=1$，$T=T_0$ ✓；$t\to\infty$ 时 $\mathrm{erfc}\to0$ ✓（热量扩散进去，远处升温）。

**8.30** $\mathcal{F}[e^{-|x|}]=2/(1+k^2)$，所以

$$\mathcal{F}\left[e^{-|x|}*e^{-|x|}\right]=\frac{4}{(1+k^2)^2}.$$

反变换得

$$(e^{-|x|})*(e^{-|x|})=(1+|x|)e^{-|x|}.$$

**验算：** 两边在 $x=0$ 处分别是 $\int e^{-2|t|}\mathrm{d}t=1$ 与 $1$ ✓；$x\to\infty$ 时两边都按 $|x|e^{-|x|}$ 衰减 ✓。

**8.31** 错。变换是可逆的（在平方可积函数上还是等距同构，见帕塞瓦尔定理）。**信息一个字都没少，只是换了一组坐标。** 唯一会「丢」的情形是数值实现：采样、截断、量化，那是离散化的代价，不是变换的性质。

**8.32** 错。白噪声是**随机过程**：每个频率的幅度是随机的、相位是随机的，谱是「常数」只在统计平均的意义下成立。$\delta$ 是确定性脉冲，谱严格是常数 1、相位为零。**两者的功率谱形状相同，但一个可预测、一个不可预测**——这是本质区别。

**8.33** 错。带宽定理是傅里叶变换的数学性质，与「测量是否扰动系统」无关。量子力学里 $\Delta x\Delta p\geq\hbar/2$ 可以被解释成测量扰动，但那是一种**诠释**，不是定理的内容；定理只说不存在同时无限窄和无限纯的波包。

**8.34** 对一半。拉普拉斯变换确实是「乘 $e^{-\sigma t}$ 之后做单边傅里叶变换」，但**必须配合两个额外条件**：积分下限是 $0$（否则初值项不存在），并且要指定收敛域（否则反演不唯一）。只记住「乘个指数」会漏掉这两条，而这两条恰恰是拉普拉斯变换区别于傅里叶变换的全部价值。

**8.35** 错。只对**因果系统**成立。反因果系统的同一个 $H(s)$（极点分布相同）可以稳定也可以不稳定，取决于收敛域。另外「极点全在左半平面」还要求没有虚轴上的重极点（那是临界情形）。

**8.36** 错。幅度确实接近 1（$\omega\ll\omega_c$ 时 $|H|\approx1$），但**相位仍按 $-\omega/\omega_c$ 变化**。相位滞后会让不同频率成分错位，方波的边沿因此变形——「幅度没衰减」不等于「不失真」。

**8.37** 错。热方程是宏观近似（连续介质、局域平衡），在「扰动传播得比光快」这件事有意义之前，它已经失效了。而且热方程给出的「超光速」部分是指数小的：$e^{-x^2/(4\alpha t)}$ 在 $x>ct$ 时小到无法测量。**物理上不能观测的东西，不必要求方程禁止它。**

**8.38** 错（一半）。卷积定理要求 $h$ 有傅里叶变换（绝对可积或平方可积）。理想积分器 $h=\theta(t)$ 不满足，所以严格说它的「传递函数」只在分布意义下存在。但对零均值的输入，卷积仍然收敛——**条件落在输入上，而不是 $h$ 上**。这是「定理的前提被违反但结论仍可用」的典型情形，用之前必须检查输入。

**8.39** 错。$H(s)$ 必须配收敛域才有唯一的时域信号。同一个代数表达式，收敛域在极点左边还是右边，对应的信号一个是因果的、一个是反因果的（见 8.28 题）。**$H(s)$ 是复变函数，不是有理分式；丢掉收敛域就等于丢掉了因果性。**

## 第 9 章

**9.1** $F=y'^2+2y$，$\partial F/\partial y=2$、$\partial F/\partial y'=2y'$，方程为 $2-\frac{\mathrm{d}}{\mathrm{d}x}(2y')=0$，即 $y''=1$。积分两次 $y=\frac12x^2+c_1x+c_2$。由 $y(0)=0$ 得 $c_2=0$；由 $y(1)=1$ 得 $c_1=\frac12$。极值曲线

$$y=\frac{x^2+x}{2} .$$

（这是一个开口向上的抛物线段，与 $F$ 里那项 $2y$ 相当于"均匀载荷"一致。）

**9.2** $F=(1+x)^2y'^2$ 不含 $y$，所以 $\partial F/\partial y'=2(1+x)^2y'=\text{常数}$，即 $(1+x)^2y'=c$。直接积分：

$$y'=\frac{c}{(1+x)^2}\quad\Longrightarrow\quad y=-\frac{c}{1+x}+d .$$

两个常数由端点定。**为什么可以这样：** $\partial F/\partial y=0$ 时方程退化成"某个量对 $x$ 的导数为零"，一次积分就完了，这正是 9.3.4 第 4 步。

**9.3** $F=\sqrt{y(1+y'^2)}$ 不含 $x$，用贝尔特拉米恒等式：

$$F-y'\frac{\partial F}{\partial y'}=\frac{\sqrt{y}}{\sqrt{1+y'^2}}=C
\quad\Longrightarrow\quad y'^2=\frac{y-C^2}{C^2} .$$

于是 $\mathrm{d}x=C\,\mathrm{d}y/\sqrt{y-C^2}$，积分得 $x+d=2C\sqrt{y-C^2}$，即

$$y=C^2+\frac{(x+d)^2}{4C^2} .$$

**极值曲线是抛物线。** （这个泛函出现在"给定水平跨度、求长度最短的旋转面"一类问题里，所以它的解偏向抛物型而不是悬链型。）

**9.4** $F=y^2+y'^2+y''^2$，三个偏导是 $F_y=2y$、$F_{y'}=2y'$、$F_{y''}=2y''$，代入高阶方程

$$2y-\frac{\mathrm{d}}{\mathrm{d}x}(2y')+\frac{\mathrm{d}^2}{\mathrm{d}x^2}(2y'')=0
\quad\Longrightarrow\quad
y''''-y''+y=0 .$$

特征方程 $k^4-k^2+1=0$，四个根 $k^2=\frac12\pm\frac{\sqrt3}{2}i$，解是指数乘三角的组合。

**9.5** $F=y'^3$，$F_y=0$、$F_{y'}=3y'^2$，方程 $\frac{\mathrm{d}}{\mathrm{d}x}(3y'^2)=0$，即 $6y'y''=0$。它只要求"$y'=0$ 或 $y''=0$"，所以任何直线都满足，$y=x$ 是其中一个。

**这个泛函没有极小。** 取在 $[0,\delta]$ 上 $y'\approx-M$、在 $[\delta,1]$ 上 $y'\approx(1+M\delta)/(1-\delta)$ 的分段线性函数（满足 $y(0)=0$、$y(1)=1$），取 $\delta=1/M^2$，则

$$\int_0^1y'^3\approx-M^3\delta+\left(\frac{1+M\delta}{1-\delta}\right)^3(1-\delta)\approx-M+1\longrightarrow-\infty .$$

**这就是退化变分问题：** $\partial^2F/\partial y'^2=6y'$ 在 $y'=0$ 处为零，方程降阶，泛函没有下界，欧拉–拉格朗日方程的"解"只是个驻点方程的空壳。

**9.6** $L=T=\rho=1$ 时 $R=\int_0^1y'^2\mathrm{d}x\big/\int_0^1y^2\mathrm{d}x$。$y=x(1-x)$：$\int y'^2=\int(1-2x)^2\mathrm{d}x=\frac13$，$\int y^2=\int x^2(1-x)^2\mathrm{d}x=\frac1{30}$，

$$R=\frac{1/3}{1/30}=10 .$$

精确值 $\pi^2=9.8696$，相对误差 $+1.32\%$，且在上方 ✓（上界定理）。

**9.7** $y=\sin\pi x$：$\int_0^1y'^2=\pi^2\int\cos^2\pi x\,\mathrm{d}x=\frac{\pi^2}{2}$，$\int_0^1y^2=\int\sin^2\pi x\,\mathrm{d}x=\frac12$，

$$R=\frac{\pi^2/2}{1/2}=\pi^2 .$$

**恰好相等，因为 $\sin\pi x$ 就是第一本征函数本身。** 由 9.7.2 的加权平均式，$c_1=1$、其余 $c_n=0$，加权平均退化成 $\lambda_1$ 本身。

**9.8** $F=y'^2+y^2$，$F_{y'}=2y'$。两端自由的自然边界条件是

$$y'(0)=0,\qquad y'(1)=0 .$$

欧拉–拉格朗日方程：$2y-\frac{\mathrm{d}}{\mathrm{d}x}(2y')=0$，即 $y''=y$，通解 $y=A\cosh x+B\sinh x$。由 $y'(0)=B=0$、$y'(1)=A\sinh1=0$ 得 $A=B=0$。

**唯一的驻点是 $y\equiv0$。** 这符合直觉：泛函是正定的，最小值 $0$ 由零函数取到，物理上对应"没有扰动"。

**9.9** 目标 $A=xy$，约束 $2(x+y)=L$。拉格朗日函数

$$\mathcal L=xy-\lambda\left[2(x+y)-L\right] .$$

$$\frac{\partial\mathcal L}{\partial x}=y-2\lambda=0,\qquad
\frac{\partial\mathcal L}{\partial y}=x-2\lambda=0
\quad\Longrightarrow\quad x=y .$$

正方形，面积 $L^2/16$。**这是等周问题在"只许用矩形"约束下的版本**——约束把可行集合从"所有闭曲线"缩到了"矩形"，最优点也从圆退化成了正方形。

**9.10** $F=\sqrt{1+y'^2}$，

$$F_{y'}=\frac{y'}{\sqrt{1+y'^2}},\qquad
F_{y'y'}=\frac{1}{\left(1+y'^2\right)^{3/2}}>0 .$$

二阶变分

$$\delta^2J=\frac12\int_a^b\frac{\eta'^2}{\left(1+y'^2\right)^{3/2}}\,\mathrm{d}x>0 .$$

**严格为正，所以直线是严格极小**——与"两点间线段最短"一致。

**9.11** 终点条件：$\dfrac{1-\cos\varphi_B}{\varphi_B-\sin\varphi_B}=\dfrac{y_B}{x_B}=\dfrac12$。数值解 $\varphi_B=3.508$。

$$a=\frac{y_B}{1-\cos\varphi_B}=\frac{1}{1.9337}=0.517\ \mathrm{m},\qquad
T=\varphi_B\sqrt{\frac{a}{g}}=3.508\sqrt{\frac{0.517}{9.81}}=0.805\ \mathrm{s}.$$

直线：$T=2\sqrt{1+m^2}\sqrt{x_B}/\sqrt{2gm}$，$m=\frac12$、$x_B=2$，得 $1.010\ \mathrm{s}$。

**摆线快 $20\%$。** 终点越"横"（$y_B/x_B$ 越小），摆线的优势越大——横着走时直线太浪费速度。

**9.12** 从 $\varphi_1$ 由静止释放，速率由能量守恒给出

$$v=\sqrt{2g\left(y-y_1\right)}=\sqrt{4ga\left[\sin^2\frac{\varphi}{2}-\sin^2\frac{\varphi_1}{2}\right]} .$$

而 $\mathrm{d}s=2a\sin\frac{\varphi}{2}\mathrm{d}\varphi$，所以

$$T=\int_{\varphi_1}^{\pi}\frac{2a\sin(\varphi/2)\,\mathrm{d}\varphi}{2\sqrt{ga}\sqrt{\sin^2(\varphi/2)-\sin^2(\varphi_1/2)}}
=\sqrt{\frac{a}{g}}\int_{\varphi_1}^{\pi}\frac{\sin(\varphi/2)\,\mathrm{d}\varphi}{\sqrt{\sin^2(\varphi/2)-\sin^2(\varphi_1/2)}} .$$

令 $u=\cos\frac{\varphi}{2}$，则 $\sin\frac{\varphi}{2}\mathrm{d}\varphi=-2\mathrm{d}u$，分母 $=\sqrt{u^2-u_1^2}$，

$$T=2\sqrt{\frac{a}{g}}\int_0^{u_1}\frac{\mathrm{d}u}{\sqrt{u_1^2-u^2}}
=2\sqrt{\frac{a}{g}}\cdot\frac{\pi}{2}=\pi\sqrt{\frac{a}{g}} .$$

**与 $\varphi_1$ 无关。** 等时性得证。

**9.13** 垂度条件 $a\left(\cosh\frac{10}{a}-1\right)=3$，数值解 $a=17.2\ \mathrm{m}$。

$$L=2a\sinh\frac{10}{a}=34.4\times\sinh(0.581)=21.1\ \mathrm{m},$$

比跨度长 $5.5\%$。水平张力

$$H=\rho ga=1\times9.81\times17.2=169\ \mathrm{N}.$$

**读法：** 垂度 $3\ \mathrm{m}$ 时张力约 $170\ \mathrm{N}$；把垂度压到 $1\ \mathrm{m}$（$a\approx52\ \mathrm{m}$），张力升到约 $510\ \mathrm{N}$，是原来的三倍。

**9.14** 由 $H=\rho ga$ 反解参数：

$$a=\frac{H}{\rho g}=\frac{2000}{0.5\times9.81}=408\ \mathrm{m} .$$

垂度

$$f=a\left(\cosh\frac{25}{a}-1\right)=408\left(\cosh0.0613-1\right)=408\times0.001881=0.77\ \mathrm{m}.$$

**读法：** 张力给定后垂度就定了，且近似 $f\approx\rho gd^2/(2H)$（抛物线近似）。这里 $f\approx0.5\times9.81\times625/(2\times2000)=0.77\ \mathrm{m}$ ✓ 与精确值差不到 $1\%$。

**9.15** 圆：$L=2\pi R$，$A=\pi R^2=\dfrac{L^2}{4\pi}=0.0796L^2$。

正方形：边长 $L/4$，$A=\dfrac{L^2}{16}=0.0625L^2$。

正三角形：边长 $L/3$，$A=\dfrac{\sqrt3}{4}\cdot\dfrac{L^2}{9}=\dfrac{\sqrt3}{36}L^2=0.0481L^2$。

**排序：圆 $>$ 正方形 $>$ 正三角形。** 等周不等式说圆是全局最大，这三个数按"接近圆的程度"排列——边数越多越接近。

**9.16** 费马原理，$F=n(y)\sqrt{1+y'^2}=n_0e^{-y/h}\sqrt{1+y'^2}$ 不含 $x$，贝尔特拉米恒等式给

$$\frac{n_0e^{-y/h}}{\sqrt{1+y'^2}}=C\quad\Longrightarrow\quad
\sqrt{1+y'^2}=ke^{-y/h},\quad k=\frac{n_0}{C} .$$

分离变量：$\mathrm{d}x=-\dfrac{h\,\mathrm{d}u}{u\sqrt{k^2u^2-1}}$（$u=e^{-y/h}$），积分得

$$y=h\ln\left[k\cos\frac{x-x_0}{h}\right] .$$

**路径是"对数余弦"曲线**：中间高、两侧低，光线朝折射率大的方向（低处）弯——这就是蜃景的光路。

**9.17** $L=\frac12ml^2\left(\frac{\mathrm{d}\theta}{\mathrm{d}t}\right)^2+mgl\cos\theta$，得 $\frac{\mathrm{d}^2\theta}{\mathrm{d}t^2}+\frac{g}{l}\sin\theta=0$。小角时 $\sin\theta\approx\theta$，$T=2\pi\sqrt{l/g}=2\pi\sqrt{1/9.81}=2.01\ \mathrm{s}$。

**大角度时周期变长。** 因为 $\sin\theta<\theta$（$\theta>0$），回复力比线性近似小，摆得慢。$\theta_0=30^\circ$ 时约长 $1.7\%$。

**9.18** $L=\frac12m\left(\frac{\mathrm{d}x}{\mathrm{d}t}\right)^2-\frac12kx^2$。

$$\frac{\partial L}{\partial x}=-kx,\qquad
\frac{\partial L}{\partial(\mathrm{d}x/\mathrm{d}t)}=m\frac{\mathrm{d}x}{\mathrm{d}t}
\quad\Longrightarrow\quad
m\frac{\mathrm{d}^2x}{\mathrm{d}t^2}+kx=0 .$$

$$\omega=\sqrt{\frac{k}{m}},\qquad x=A\cos(\omega t+\varphi_0) .$$

**与牛顿力学一致**：$F=-kx$。

**9.19** 悬链面 $r=a\cosh(z/a)$，环处 $r=R=2\ \mathrm{cm}$、$z=z_0=1\ \mathrm{cm}$：

$$a\cosh\frac{1}{a}=2\quad(\text{单位 cm}).$$

数值解 $a=1.69\ \mathrm{cm}$。**腰部半径 $1.69\ \mathrm{cm}$**，比环小 $15\%$——膜在中间收腰。

**9.20** 圆柱面上 $z'=\mathrm{d}z/\mathrm{d}\varphi$ 为常数（例 9.3.5 的做法），所以

$$L=\sqrt{\left(R\Delta\varphi\right)^2+\left(\Delta z\right)^2}=\sqrt{\left(\frac{\pi}{2}\right)^2+2^2}=\sqrt{2.467+4}=2.54 .$$

**测地线把"绕"和"升"合成为一个直线段**——展开成平面就一目了然。

**9.21** 方程 $-EAy''=\lambda\rho y$，$y(0)=0$、$y'(L)=0$。试函数 $y=x$ 满足本质边界条件 $y(0)=0$（自由端不必满足，自然边界条件会自动照顾）：

$$R=\frac{EA\int_0^L1\,\mathrm{d}x}{\rho\int_0^Lx^2\,\mathrm{d}x}=\frac{EA\cdot L}{\rho\cdot L^3/3}=\frac{3EA}{\rho L^2} .$$

精确值 $\lambda_1=\dfrac{\pi^2}{4}\dfrac{EA}{\rho L^2}=2.467\dfrac{EA}{\rho L^2}$。试函数高 $21.6\%$ ✓（上界）。

**9.22** $\dfrac{1-\cos\varphi_B}{\varphi_B-\sin\varphi_B}=0.5$ 给出 $\varphi_B=3.508$（与 9.11 相同，因为 $B$ 在同一条射线上）。

$$a=\frac{0.5}{1.9337}=0.259\ \mathrm{m},\qquad T=3.508\sqrt{\frac{0.259}{9.81}}=0.570\ \mathrm{s}.$$

直线：$2\sqrt{1.25}/\sqrt{9.81}=0.714\ \mathrm{s}$。**摆线快 $25\%$。** 注意 $a$ 和 $T$ 分别是 9.11 的 $1/2$ 与 $1/\sqrt2$——**摆线问题有标度不变性**：终点坐标同乘 $\Lambda$，$a$ 乘 $\Lambda$、时间乘 $\sqrt\Lambda$。

**9.23** $F=y'^2-4\pi^2y^2$，方程 $-8\pi^2y-\frac{\mathrm{d}}{\mathrm{d}x}(2y')=0$，即 $y''+4\pi^2y=0$。通解 $y=A\sin2\pi x+B\cos2\pi x$，端点条件给 $B=0$，所以驻点族

$$y=A\sin2\pi x,\qquad J[y]=0 .$$

二阶变分 $\delta^2J[\eta]=\int_0^1\left(\eta'^2-4\pi^2\eta^2\right)\mathrm{d}x$。取 $\eta=\sin\pi x$（满足 $\eta(0)=\eta(1)=0$）：

$$\delta^2J=\frac{\pi^2}{2}-4\pi^2\cdot\frac12=-\frac{3\pi^2}{2}<0 .$$

**二阶变分为负，所以这些驻点是鞍点，不是极小。**

**9.24** 直接求导（不预设欧拉–拉格朗日方程）：

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(F-y'F_{y'}\right)
=F_x+F_yy'+F_{y'}y''-y''F_{y'}-y'\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}
=F_x+y'\left(F_y-\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}\right) .$$

- 若欧拉–拉格朗日方程成立且 $F_x=0$，右边为零，得 $F-y'F_{y'}=$ 常数。
- 反之，若 $F-y'F_{y'}=$ 常数且 $F_x=0$，则 $y'\left(F_y-\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}\right)=0$。在 $y'\ne0$ 处方程成立；$y'\equiv0$（水平直线）处另作讨论。

**两者在 $y'\ne0$ 的区间上等价。** 所以贝尔特拉米恒等式不是"另一个方程"，是方程的一次积分。

**9.25** $V=\pi r^2h$，$S=2\pi r^2+2\pi rh$。

$$\mathcal L=\pi r^2h-\lambda\left(2\pi r^2+2\pi rh-S\right).$$

$$\frac{\partial\mathcal L}{\partial r}=2\pi rh-\lambda(4\pi r+2\pi h)=0,\qquad
\frac{\partial\mathcal L}{\partial h}=\pi r^2-2\pi r\lambda=0 .$$

第二式给 $\lambda=r/2$，代入第一式：$2rh=(r/2)(4r+2h)$，即 $2rh=2r^2+rh$，故 $h=2r$。**等直径等高的罐头用料最省（按侧面积+两端算）。**

**9.26** 自由端的边界项要求 $F_{y'}=0$，而

$$F_{y'}=\frac{(y-\mu)y'}{\sqrt{1+y'^2}} .$$

悬链线上 $y-\mu=a\cosh\frac{x-x_0}{a}>0$ 处处不为零，所以只能 $y'=0$。**自由端停在最低点，那里切线水平。**

物理上：自由端的张力只能沿切线，而端点没有东西拉它，所以该处张力必须为零；张力为零的点正是链条的最低点（竖直线段之外的部分会垂下来）。**结论：一端自由的链条会竖直垂下，末端就是最低点。**

**9.27** 大圆写成 $\cos\theta=k\sin\theta\cos\varphi$，两边除以 $\sin\theta$ 得 $\cot\theta=k\cos\varphi$。记 $u=\cot\theta$，则 $u=k\cos\varphi$，求导得 $-\csc^2\theta\,\theta'=-k\sin\varphi$，即

$$\theta'=k\sin\varphi\,\sin^2\theta .$$

代入首次积分。先算分母：

$$\theta'^2+\sin^2\theta=\sin^2\theta\left(1+k^2\sin^2\varphi\sin^2\theta\right) .$$

用 $\sin^2\varphi=1-\cos^2\varphi=1-\cot^2\theta/k^2$ 化简方括号：

$$k^2\sin^2\varphi\sin^2\theta=k^2\sin^2\theta-\cos^2\theta
\quad\Longrightarrow\quad
1+k^2\sin^2\varphi\sin^2\theta=\sin^2\theta\left(1+k^2\right) .$$

所以 $\sqrt{\theta'^2+\sin^2\theta}=\sin^2\theta\sqrt{1+k^2}$，首次积分

$$\frac{\sin^2\theta}{\sqrt{\theta'^2+\sin^2\theta}}=\frac{1}{\sqrt{1+k^2}} ,$$

**与 $\varphi$ 无关** ✓。大圆满足测地线方程。

**9.28** $F=\frac12EI(y'')^2-qy$（载荷项取 $-qy$，因为外力做功要减）。

$$F_y=-q,\qquad F_{y'}=0,\qquad F_{y''}=EI\,y'' .$$

高阶方程：$-q-0+\frac{\mathrm{d}^2}{\mathrm{d}x^2}\left(EI\,y''\right)=0$，即

$$EI\,y''''=q(x) .$$

**简支端的 $y''=0$ 是自然边界条件**：分部积分两次后，边界项里出现 $\delta y'$，它任意，于是 $F_{y''}=EIy''=0$，即弯矩为零。固定端 $y'=0$ 则是本质条件，必须事先给定。

**9.29** 设 $y=c_1y_1+c_2y_2$，本征函数带权正交归一、且 $\int(py_n'y_m'+qy_ny_m)=\lambda_n\delta_{nm}$。于是

$$R=\frac{c_1^2\lambda_1+c_2^2\lambda_2}{c_1^2+c_2^2}
=\lambda_1+\frac{c_2^2\left(\lambda_2-\lambda_1\right)}{c_1^2+c_2^2}\ge\lambda_1 .$$

**等号当且仅当 $c_2=0$**（$y\propto y_1$）。这个式子还给出误差的估计：多出的量按 $\left(c_2/c_1\right)^2$ 计，所以只要试函数与 $y_1$ 的"污染"小，估计就准——**这就是为什么稍微改进试函数就能把误差从 $10^{-2}$ 降到 $10^{-5}$。**

**9.30** 不一定。摆线的共轭点在 $\varphi=\pi$（最低点）：$\varphi_B<\pi$ 时二阶变分恒正，摆线是极小；$\varphi_B>\pi$ 之后二阶变分不再恒正，**摆线只是驻点，极小性失效**。

9.1.4 的 $\varphi_B=2.41<\pi$，所以那里确实是极小 ✓；而习题 9.11 的 $\varphi_B=3.51>\pi$，已经越过共轭点——那个答案给出的时间仍然是最速降线的时间，但严格说只证明了"它是驻点"。

**注意：9.13 的 $\varphi_B=3.508>\pi=3.1416$，所以那个例子其实已经越过了共轭点**——严格说，它只保证是"驻点"，极小性需要另证（实际上最速降线问题里这类解仍是弱极小，但强极小要用魏尔斯特拉斯的方法判断，本章不展开）。

**9.31** 因为 $\delta J=0$ 只是一阶导数为零，和 $f'(x)=0$ 一样，可能是极小、极大或鞍点。**物理例子：** 一根链条挂在两钉之间是稳定平衡（势能极小）；把同一根链条的形状"倒过来"顶成拱形，同样满足平衡方程，却是势能极大——碰一下就塌。判断要靠二阶变分。

**9.32** 因为边界项是 $\left[F_{y'}\delta y\right]$。端点自由时 $\delta y(b)\ne0$，要 $\delta J=0$ 就必须 $F_{y'}(b)=0$。

$F_{y'}$ 一般不等于 $y'$：只有 $F$ 正比于 $y'^2$（比如长度的被积函数 $\sqrt{1+y'^2}$ 在小斜率极限下）才近似成正比。**最短路问题里 $F_{y'}=y'/\sqrt{1+y'^2}=0$ 与 $y'=0$ 等价**（因为 $y'=0$ 时 $F_{y'}=0$，反之亦然），但一般情形不等价——比如悬链线的 $F_{y'}=(y-\mu)y'/\sqrt{1+y'^2}$，$y'=0$ 只是它的一个零点。

**9.33** 没有唯一意义。乘子会随"约束的写法"和"势能零点的选择"改变。悬链线里 $\mu$ 可以任意平移（把 $y$ 的起算点挪一下），但由它导出的水平张力 $H=\rho ga$ 有绝对意义。**看到一个乘子，先问"哪一个由它导出的量是不变的"。**

**9.34** 最可能是**试函数不满足本质边界条件**。上界性质的前提是 $y(a)=y(b)=0$；端点不为零时，展开里混进了不满足边界的分量，$R$ 可以低于 $\lambda_1$。第二可能是基函数选错（比如用奇函数逼近偶模态，$c_1=0$，$R$ 收敛到 $\lambda_2>\lambda_1$——这种情况反而偏高）。

**9.35** 因为 $\partial^2F/\partial y'^2=0$ 时，$\frac{\mathrm{d}}{\mathrm{d}x}\left(\partial F/\partial y'\right)$ 里没有 $y''$，方程降成关于 $x,y,y'$ 的代数关系。这时它不再是一个二阶微分方程，而是"某个代数约束"，通常无解或只有特殊解。

**极值可能不存在**（如 9.6 的 $\int y'^3$ 无下界），也可能只在下确界处取到（没有光滑极值曲线）。判据：先算 $F_{y'y'}$，它恒为零就要警惕。

**9.36** 不更基本。最小作用量与牛顿定律**等价**——给定 $L$ 能推出运动方程，反过来也能从运动方程构造 $L$。它的价值在三个具体的好处：换广义坐标时约束力自动消失；加约束只要降维；加场（电磁、相对论）只要换 $L$。**变分原理是把"对称性"直接翻译成"方程"的语言，不是更深的物理。**

**9.37** 因为悬链面解存在需要 $R\ge1.509z_0$。间距超过 $1.33R$ 后方程无解，膜只能跳到另一个构型（两个平圆盘）。这说明**变分法只保证"如果存在光滑驻点，它满足欧拉–拉格朗日方程"，不保证驻点存在**。极值问题可能无解，或者解在参数越过临界点时发生不连续跳变。

**9.38** 因为问题本身对称：给定周长和"面积最大"，如果把一条最优曲线镜像或旋转，得到的还是一条最优曲线。若最优解唯一，它必须与自己关于任意轴的镜像重合，所以可以先找对称解。**这个论证的前提是"解唯一"**。如果不唯一（比如矩形长宽互换），对称性论证就只能说"存在一个对称的最优解"，不能排除别的。等周问题里圆是唯一最优，所以假设安全。

## 第 10 章

### 习题 10.1–10.10

**10.1** (a) $\partial_\mu v^\nu$ **不是**：换坐标后多出 $\partial^2x'/\partial x^2$ 项。(b) $\Gamma^\mu{}_{\nu\lambda}$ **不是**：变换律含二阶导数，且平直直角坐标下为零、极坐标下非零。(c) $R^\rho{}_{\sigma\mu\nu}$ **是**：二阶导数项在反对称组合里抵消。(d) $v^\mu\omega_\nu$ **是**：一上一下，各带一个雅可比。(e) $\Gamma\Gamma$ **不是**：两个非张量的乘积，变换后出现二阶导数的交叉项。


**10.2** $a=1$ 时 $g_{\theta\theta}=1$、$g_{\varphi\varphi}=\sin^2\theta$，所以

$$v_\theta=g_{\theta\theta}v^\theta=1,\qquad
v_\varphi=g_{\varphi\varphi}v^\varphi=2\sin^2\theta .$$

两个不变量：

$$g_{\mu\nu}v^\mu v^\nu=1\cdot1^2+\sin^2\theta\cdot2^2=1+4\sin^2\theta,$$

$$g^{\mu\nu}v_\mu v_\nu=1\cdot1^2+\frac{1}{\sin^2\theta}(2\sin^2\theta)^2=1+4\sin^2\theta .$$

相等 ✓。这是"升降指标不改变矢量"的具体验证。


**10.3** 圆柱面 $g_{11}=a^2$、$g_{22}=1$，**两个都是常数**，所有导数都为零，代入

$$\Gamma^\mu{}_{\nu\lambda}=\frac12g^{\mu\rho}\left(
\frac{\partial g_{\rho\lambda}}{\partial x^\nu}
+\frac{\partial g_{\nu\rho}}{\partial x^\lambda}
-\frac{\partial g_{\nu\lambda}}{\partial x^\rho}\right)$$

得 $\Gamma\equiv0$。于是 $R^\rho{}_{\sigma\mu\nu}$ 的每一项都含 $\Gamma$ 或其导数，全部为零，曲率为零。**圆柱面是可展曲面，内禀平坦**——它能平铺成一张纸。


**10.4** 逐项看：$\Gamma^\theta{}_{\theta\theta}=\frac12g^{\theta\theta}(\partial_\theta g_{\theta\theta}+\partial_\theta g_{\theta\theta}-\partial_\theta g_{\theta\theta})=0$，因为 $g_{\theta\theta}=a^2$ 是常数；$\Gamma^\theta{}_{\theta\varphi}$ 含 $\partial g_{\theta\varphi}=0$（度规对角）和 $\partial_\varphi g_{\theta\theta}=0$；$\Gamma^\varphi{}_{\varphi\varphi}=\frac12g^{\varphi\varphi}(2\partial_\varphi g_{\varphi\varphi}-\partial_\varphi g_{\varphi\varphi})=0$，因为度规不显含 $\varphi$。


**10.5** $g^{11}=1$、$g^{22}=1/f$。非零分量只有两个：

$$\Gamma^1{}_{22}=\frac12g^{11}\left(-\frac{\partial g_{22}}{\partial x^1}\right)=-\frac{f'}{2},
\qquad
\Gamma^2{}_{12}=\Gamma^2{}_{21}=\frac12g^{22}\frac{\partial g_{22}}{\partial x^1}=\frac{f'}{2f}.$$


**10.6** 取 $\rho=\varphi$、$\sigma=\theta$、$\mu=\theta$、$\nu=\varphi$：

$$R^\varphi{}_{\theta\varphi\theta}
=\frac{\partial\Gamma^\varphi{}_{\theta\theta}}{\partial\varphi}
-\frac{\partial\Gamma^\varphi{}_{\varphi\theta}}{\partial\theta}
+\Gamma^\varphi{}_{\varphi\lambda}\Gamma^\lambda{}_{\theta\theta}
-\Gamma^\varphi{}_{\theta\lambda}\Gamma^\lambda{}_{\varphi\theta}.$$

第一项为零（$\Gamma^\varphi{}_{\theta\theta}=0$）；第二项 $=-\dfrac{\partial}{\partial\theta}\cot\theta=+\dfrac{1}{\sin^2\theta}$；第三项为零；第四项 $\lambda=\varphi$ 给 $\Gamma^\varphi{}_{\theta\varphi}\Gamma^\varphi{}_{\varphi\theta}=\cot^2\theta$。所以

$$R^\varphi{}_{\theta\varphi\theta}=\frac{1}{\sin^2\theta}-\cot^2\theta=1 .$$


**10.7** $\Gamma\equiv0$ ⟹ 它的导数也为零 ⟹ $R^\rho{}_{\sigma\mu\nu}\equiv0$ ⟹ $R_{\mu\nu}\equiv0$ ⟹ $R=g^{\mu\nu}R_{\mu\nu}=0$。一步都不用算。


**10.8** 用 10.6.3 的两个里奇分量：

$$R=g^{\theta\theta}R_{\theta\theta}+g^{\varphi\varphi}R_{\varphi\varphi}
=\frac{1}{a^2}\cdot1+\frac{1}{a^2\sin^2\theta}\cdot\sin^2\theta
=\frac{1}{a^2}+\frac{1}{a^2}=\frac{2}{a^2}.$$

**与 $\theta$ 无关的原因：** 球面上每一点的地位相同（均匀且各向同性），标量曲率是标量，不可能依赖坐标；$R_{\theta\theta}$ 与 $R_{\varphi\varphi}$ 里那些 $\theta$ 依赖，正好被逆度规里的 $\sin^2\theta$ 抵消。


**10.9** 二维恒等式 $R_{\mu\nu}=\frac{R}{2}g_{\mu\nu}$ 的两边：

$$\theta\theta:\quad R_{\theta\theta}=1,\qquad \frac{R}{2}g_{\theta\theta}=\frac{1}{a^2}\cdot a^2=1;$$

$$\varphi\varphi:\quad R_{\varphi\varphi}=\sin^2\theta,\qquad
\frac{R}{2}g_{\varphi\varphi}=\frac{1}{a^2}\cdot a^2\sin^2\theta=\sin^2\theta .$$

两式都成立 ✓。**二维时里奇张量不携带超出 $R$ 的信息**，这是 2 维的特殊性质。


**10.10** $\mu=\theta$ 分量：

$$\theta''-\sin\theta\cos\theta\,\varphi'^2=0 .$$

代 $\theta=\pi/2$：$\theta''=0$，$\cos(\pi/2)=0$，左边 $=0-0\cdot\varphi'^2=0$ ✓。所以赤道满足测地线方程（同理任何 $\theta=$ 常数的面只有在 $\cos\theta=0$ 时才是测地线，这正好挑出赤道）。

### 习题 10.11–10.20


### 习题 10.11–10.22

**10.11** $m=20$，$a,b,c=0.3,0.2,0.1$：

$$I_{xx}=\frac{20(0.2^2+0.1^2)}{12}=0.0833,\quad
I_{yy}=\frac{20(0.3^2+0.1^2)}{12}=0.167,\quad
I_{zz}=\frac{20(0.3^2+0.2^2)}{12}=0.217\ \mathrm{kg\cdot m^2}.$$

体对角线方向单位矢量 $\boldsymbol{n}=(0.802,0.535,0.267)$，

$$I_{\boldsymbol{n}}=\boldsymbol{n}^{\mathsf T}I\boldsymbol{n}
=0.0833(0.802)^2+0.167(0.535)^2+0.217(0.267)^2=0.117\ \mathrm{kg\cdot m^2}.$$

它介于 $I_{xx}$ 与 $I_{yy}$ 之间——**任意方向的转动惯量都被三个主轴值夹住**（瑞利商的性质）。


**10.12** 竖直向下为 $-y$。水平/竖直坐标：$\boldsymbol{a}=(0,-g)$。沿斜面/垂直斜面（$x'$ 沿斜面向下，$y'$ 垂直向上）：

$$a_{x'}=g\sin30^\circ=4.9,\qquad a_{y'}=-g\cos30^\circ=-8.49\ \mathrm{m/s^2}.$$

模长：$\sqrt{0+g^2}=\sqrt{4.9^2+8.49^2}=9.8=g$ ✓。**分量变了，矢量没变。**


**10.13** 圆环上只有 $\varphi$ 一个坐标，$\mathrm{d}s^2=a^2\mathrm{d}\varphi^2$，度规分量是常数，$\Gamma\equiv0$。测地线方程

$$\frac{\mathrm{d}^2\varphi}{\mathrm{d}\lambda^2}=0
\quad\Longrightarrow\quad
\varphi=\omega\lambda+\varphi_0 .$$

**匀速圆周运动就是圆环上的测地线。** 一维流形上任何曲线都是测地线（没有"转弯"的余地），曲率必然为零——这也解释了为什么一维世界没有引力。


**10.14** 设两点纬度都是 $\theta_0$（从北极量起的余纬），经度差 $\Delta\varphi$。

**沿纬线走：** 纬线是小圆，半径 $a\sin\theta_0$，所以距离

$$s_{\text{纬}}=a\sin\theta_0\,\Delta\varphi .$$

**沿大圆走：** 用球面余弦定理，圆心角 $d/a$ 满足

$$\cos\frac{d}{a}=\cos^2\theta_0+\sin^2\theta_0\cos\Delta\varphi,
\qquad s_{\text{大圆}}=a\arccos(\cdots).$$

**比较：** 对小 $\Delta\varphi$，两式都 $\approx a\sin\theta_0\Delta\varphi$（局部看不出差别）；$\Delta\varphi$ 大时大圆明显更短。$90^\circ$ 纬度、$\Delta\varphi=90^\circ$ 时：纬线距离 $=\frac{\pi}{2}\cdot\frac{a}{\sqrt2}=1.11a$，大圆距离 $=\frac{\pi}{3}a=1.05a$。

**读法：** 这就是飞机走大圆的原因——**纬线不是测地线（除赤道），走它要多走路**。差值随纬度升高、经度差增大而增大。


**10.15** 赤道到北极：沿经线（大圆）走，圆心角 $\pi/2$，距离

$$s_1=a\cdot\frac{\pi}{2}=1.571a .$$

赤道周长：赤道是大圆，$C=2\pi a=6.283a$。比值

$$\frac{s_1}{C}=\frac{1}{4}.$$

**平面直觉是多少？** 平面上从圆心到边界是 $R$，周长 $2\pi R$，比值 $1/(2\pi)\approx0.159$。

**差在哪：** 球面上"到边界的距离/周长"是 $1/4$，平面是 $1/(2\pi)$。这不是测量误差，是曲率：**球面上圆的周长比同半径的平面圆短**（$C=2\pi a\sin(r/a)<2\pi r$），所以比值偏大。量一下这个比值，就能判断空间弯不弯。


**10.16** 纬度 $45^\circ$ 对应余纬 $\theta_0=45^\circ$。转角

$$\Delta\alpha=2\pi(1-\cos45^\circ)=2\pi\left(1-\frac{\sqrt2}{2}\right)=0.586\pi=1.840\ \mathrm{rad}=105.4^\circ .$$

**读法两条：**

1. **这个角只依赖余纬，与地球半径无关。** 所以"沿纬线搬一圈转 $105^\circ$"是球面几何的普适结论，换个大小的球也一样。半径只影响"面积与转角"的比例系数（$K=1/a^2$）。
2. **$45^\circ$ 纬线围出的球冠面积**是 $2\pi a^2(1-\cos45^\circ)$，乘 $K=1/a^2$ 正好是这个角——与 10.5.2 的 $\Delta\alpha=K\times$面积一致。


**10.17** 双曲面上 $K=-1/a^2$，角亏与面积的关系仍是"曲率 $\times$ 面积"，但符号相反：

$$\text{角亏}=|K|\times\text{面积}=\frac{\text{面积}}{a^2}.$$

角亏 $0.01\,\mathrm{rad}$、$a=1\,\mathrm{m}$：

$$\text{面积}=0.01\times a^2=0.01\ \mathrm{m^2}.$$

**读法：** 正曲率给"角盈"（内角和 $>\pi$），负曲率给"角亏"（$<\pi$）。**测一个三角形的内角和，就能判断空间的正负**——这是高斯当年做大地测量时想做的事（他在三个山头之间测三角形，想判断地球表面的曲率，当然测不出来，因为地球太大）。


**10.18** 反证。设存在一个保持距离的平面地图，即球面上任意两点的距离等于地图上对应两点的距离。

取球面上一个测地三角形（三条边都是大圆）。**在球面上**，它的内角和是

$$A+B+C=\pi+\frac{\text{面积}}{a^2}>\pi .$$

**在地图上**，三条边都是平面上的直线段（因为保距，测地线必须映成直线），而平面三角形的内角和恰好等于 $\pi$。

同一个三角形，内角和既是 $>\pi$ 又是 $=\pi$，矛盾。所以**不存在保距的平面地图**。

**读法：** 这不是"画得不够好"，是**不允许**。所有世界地图都在某处失真——等角投影（墨卡托）保角不保面积，等面积投影保面积不保角。曲率不允许你把三者同时保住。球面是"不可展曲面"，而圆柱、圆锥是"可展"的（$K\equiv0$），所以能剪开铺平。


**10.19** 圆锥面（半顶角 $\alpha$，从顶点量起的斜距 $\rho$）：

$$\mathrm{d}s^2=\mathrm{d}\rho^2+\rho^2\sin^2\alpha\,\mathrm{d}\varphi^2 .$$

这与平面极坐标 $\mathrm{d}r^2+r^2\mathrm{d}\vartheta^2$ 形状相同，只要把角度缩放成 $\vartheta=\varphi\sin\alpha$。所以：

- **非零的 $\Gamma$：** $\Gamma^\rho{}_{\varphi\varphi}=-\rho\sin^2\alpha$，$\Gamma^\varphi{}_{\rho\varphi}=1/\rho$。
- **曲率：** 结构完全照搬 10.6.4 的计算（把 $\varphi$ 换成 $\varphi\sin\alpha$），两项仍精确抵消，$R\equiv0$。

**测地线在展开图上是直线。** 把圆锥沿一条母线剪开铺平，锥面变成平面上的一个扇形（圆心角 $2\pi\sin\alpha$），测地线变成扇形里的直线段——**"直线"跨过剪开的那条缝时要按同样的角度接上**，这就是锥面上测地线"绕着顶点拐弯"的原因。

**读法：** 圆锥是可展曲面，所以它的"弯曲"全是坐标造成的，不是内禀的。这也解释了为什么圆锥上的平行移动不产生任何转角。


**10.20** 圆柱面 $\mathrm{d}s^2=a^2\mathrm{d}\varphi^2+\mathrm{d}z^2$，全部 $\Gamma=0$（10.3 节题）。平行移动方程退化成

$$\frac{\mathrm{d}v^\mu}{\mathrm{d}\lambda}=0,$$

即分量是常数。沿纬线走一圈回来，**矢量一模一样，转角为零**。

**与球面对比：** 球面上同样走一圈，转角是 $2\pi(1-\cos\theta_0)\ne0$（例 10.3）。差别不在"坐标弯不弯"（两者都弯），而在**曲率是不是零**：圆柱面 $K=0$，球面 $K=1/a^2$。

**"回到原处方向不变" 是平坦的等价条件：** 若对任何闭合回路平行移动都不产生转角，则由 $\Delta\alpha=K\times$面积，面积任意小时必须 $K=0$。反过来 $K=0$ 时和乐恒为零（局部可积）。**这就是"平坦"的几何定义**，比"看起来直不直"可靠得多。


**10.21** 约束在球面上的自由粒子，作用量就是弧长，所以它走测地线：

$$\theta''-\sin\theta\cos\theta\,\varphi'^2=0,
\qquad
\varphi''+2\cot\theta\,\theta'\varphi'=0 .$$

**匀速性：** 由度规相容性，$g_{\mu\nu}u^\mu u^\nu=a^2\left(\theta'^2+\sin^2\theta\,\varphi'^2\right)$ 是常数。对常数开方（沿曲线 $\mathrm{d}s/\mathrm{d}\lambda$ 为常数），得"速率" $|\boldsymbol{u}|$ 恒定——**球面上没有力，所以速率不变，只有方向在变**。

**赤道特解：** 取 $\theta=\pi/2$，则 $\theta'=\theta''=0$、$\cos(\pi/2)=0$，第一式给 $0=0$；第二式给 $\varphi''=0$，即 $\varphi=\omega\lambda$。**绕赤道匀速转圈是测地线运动**——卫星在赤道平面上绕地球转，就是这个解。

**非赤道的解：** 一般解是倾斜的大圆。用两个第一积分（能量与角动量）可以把它解成 $\theta(\lambda)$ 的椭圆积分——这正是"球面上的自由粒子沿大圆运动"的完整答案。


**10.22** 球面上测地半径为 $r$ 的小圆，周长 $C(r)=2\pi a\sin(r/a)$。展开：

$$C(r)=2\pi r-\frac{\pi r^3}{3a^2}+\cdots$$

与平面值 $2\pi r$ 的差是

$$\Delta C=-\frac{\pi r^3}{3a^2}.$$

**数值（$r=1\,\mathrm{km}$，$a=R_\oplus=6371\,\mathrm{km}$）：**

$$\Delta C=-\frac{\pi\times(10^3)^3}{3\times(6.371\times10^6)^2}
=-\frac{3.14\times10^9}{1.218\times10^{14}}
=-2.6\times10^{-5}\ \mathrm{m},$$

即**负 0.026 毫米**。

**读法两条：**

1. **符号为负**：球面上圆的周长比同半径的平面圆短，因为"边"往回收（正曲率）。
2. **量级小得可怕**：1 公里半径的圆，误差只有 26 微米。这就是为什么古人测不出地球弯曲——**要看出曲率，得把 $r/a$ 做大**，比如用卫星轨道（$r\sim10^7\,\mathrm{m}$）或者测地学基线。


### 习题 10.23–10.30

**10.23** 现在把两个方程都解出来。由例 10.3 已得

$$v^\theta=A\cos(c\varphi)+B\sin(c\varphi),\qquad c\equiv\cos\theta_0 .$$

代入 $\dfrac{\mathrm{d}v^\varphi}{\mathrm{d}\varphi}=-\cot\theta_0\,v^\theta$ 积分：

$$v^\varphi=-\frac{\cot\theta_0}{c}\left[A\sin(c\varphi)-B\cos(c\varphi)\right]+\text{const}
=-\frac{1}{\sin\theta_0}\left[A\sin(c\varphi)-B\cos(c\varphi)\right].$$

（积分常数取零，相当于把初值吸收进 $A,B$。）

**长度不变：** $g_{\theta\theta}(v^\theta)^2+g_{\varphi\varphi}(v^\varphi)^2$ 用 $\sin^2\theta_0$ 归一，

$$(v^\theta)^2+\sin^2\theta_0(v^\varphi)^2
=(v^\theta)^2+\left[A\sin(c\varphi)-B\cos(c\varphi)\right]^2=A^2+B^2,$$

与 $\varphi$ 无关 ✓——**平行移动保持长度，这是度规相容性的直接后果**。


**10.24** $\sin x=x-\dfrac{x^3}{6}+\dfrac{x^5}{120}-\cdots$，代 $x=r/a$：

$$C(r)=2\pi a\left(\frac ra-\frac{r^3}{6a^3}+\frac{r^5}{120a^5}-\cdots\right)
=2\pi r-\frac{\pi}{3a^2}r^3+\frac{\pi}{60a^4}r^5-\cdots$$

一般地 $C(r)=2\pi r\left(1-\dfrac{K}{6}r^2+\dfrac{K^2}{120}r^4-\cdots\right)$。所以

$$K=-\frac{6}{2\pi r}\times\frac{\text{三次项系数}}{1}\cdot\ldots
\quad\Longrightarrow\quad
K=\frac{3}{\pi}\cdot\frac{\text{（}r^3\text{ 项系数）}}{1}\Big/\pi\cdot\ldots$$

更直接：三次项系数是 $-\pi K/3$，所以 $K=-3\times(\text{三次项系数})/\pi$。对球面代入得 $K=1/a^2$ ✓。**高次项可以检验"$K$ 是不是常数"**：若 $r^5$ 项系数不符合 $K^2$ 的规律，说明曲率随位置变。


**10.25** 用测地线偏离方程。球面上取两条经线，初始相距 $\xi_0=a\sin\theta_0\,\Delta\varphi$。分离矢量的分量只有 $\varphi$ 方向，$\xi^\varphi=\Delta\varphi$（常数，因为经线之间的角间距不变）。物理距离是

$$\xi(\tau)=a\sin\theta(\tau)\,\Delta\varphi,
\qquad \theta(\tau)=\frac{\tau}{a}.$$

（经线是测地线，$\theta=\tau/a$ 匀速。）所以

$$\xi(\tau)=a\,\Delta\varphi\,\sin\frac{\tau}{a}.$$

它满足 $\dfrac{\mathrm{d}^2\xi}{\mathrm{d}\tau^2}=-\dfrac{1}{a^2}\xi$，**这正是测地线偏离方程在球面上的样子**：$\dfrac{D^2\xi^\mu}{D\tau^2}=-R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$ 缩并后给出 $\ddot\xi=-K\xi$。$\xi$ 在 $\tau=\pi a$（北极）处为零——两条经线相交，如图 10.5 所示。


**10.26** 从协变导数出发。要求 $\nabla_\lambda v^\mu$ 是张量，而 $\partial_\lambda v^\mu$ 不是，所以 $\Gamma^\mu{}_{\lambda\nu}v^\nu$ 的变换律里必须有一个与 $\partial^2x'/\partial x^2$ 相反的项。逐项算下来：

$$\Gamma'^\mu{}_{\nu\lambda}
=\frac{\partial x'^\mu}{\partial x^\alpha}
\frac{\partial x^\beta}{\partial x'^\nu}
\frac{\partial x^\gamma}{\partial x'^\lambda}\Gamma^\alpha{}_{\beta\gamma}
+\frac{\partial x'^\mu}{\partial x^\alpha}
\frac{\partial^2 x^\alpha}{\partial x'^\nu\partial x'^\lambda}.$$

**第一项**是张量该有的样子（三个雅可比因子）。**第二项含二阶导数**，它不可能由一阶导数组合出来，所以 $\Gamma$ 不是张量。

**这一项从哪来：** 它正是"基矢量随位置变"的数学痕迹。若变换是线性的（$\partial^2x'/\partial x^2=0$，比如直角坐标之间的转动），第二项消失，$\Gamma$ 在这种变换下"像"张量——这正是为什么在直角坐标里算题从来不出问题的原因。


**10.27** 用"局部惯性系"这个技巧：在任意一点，总可以选一套坐标使 $\Gamma=0$（10.4.3 的前提）。在那套坐标里，黎曼张量只剩导数项：

$$R_{\rho\sigma\mu\nu}
=\frac12\left(
\frac{\partial^2g_{\sigma\mu}}{\partial x^\rho\partial x^\nu}
-\frac{\partial^2g_{\sigma\nu}}{\partial x^\rho\partial x^\mu}
+\frac{\partial^2g_{\rho\nu}}{\partial x^\sigma\partial x^\mu}
-\frac{\partial^2g_{\rho\mu}}{\partial x^\sigma\partial x^\nu}
\right).$$

（这一步是把 $\Gamma=0$ 的 $R^\rho{}_{\sigma\mu\nu}$ 用度规写出来，再用 $\partial g=0$ 化简。）

**交换 $\rho\leftrightarrow\sigma$：** 第一项与第四项互换并变号，第二项与第三项互换并变号，整体变号：

$$R_{\rho\sigma\mu\nu}=-R_{\sigma\rho\mu\nu}.$$

**从一点推广到处处：** 上式是在"局部惯性系"里证的，但两边都是张量，等式在一点成立就在该点的一切坐标系里成立；而这一点是任意的，所以处处成立。**这个"在局部惯性系里证、再用张量性推广"的手法，是张量计算里最常用的招数。**


**10.28** 要证 $R_{\mu\nu\rho\sigma}=K\left(g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho}\right)$。

**先验证球面。** 取 $\mu=\theta$、$\nu=\varphi$、$\rho=\theta$、$\sigma=\varphi$，右边是

$$K\left(g_{\theta\theta}g_{\varphi\varphi}-g_{\theta\varphi}g_{\varphi\theta}\right)
=K\left(a^2\cdot a^2\sin^2\theta-0\right)=Ka^4\sin^2\theta .$$

左边是 10.6.3 算出的 $R_{\theta\varphi\theta\varphi}=a^2\sin^2\theta$。两边相等要求

$$Ka^4\sin^2\theta=a^2\sin^2\theta
\quad\Longrightarrow\quad
K=\frac{1}{a^2}.$$

**为什么这个形式对一般常曲率空间也对：** 右边是"用度规能造出来的、具有黎曼张量全部对称性的唯一组合"（在二维只有一个独立分量，三维也是）。所以任何常曲率空间都取这个形式，$K$ 就是高斯曲率。

**顺带核对标量曲率：** 缩并两次，$R=K\cdot n(n-1)$；二维给 $R=2K=2/a^2$ ✓ 与 10.6.3 一致。


**10.29** 协变导数作用在度规上：

$$\nabla_\lambda g_{\mu\nu}
=\frac{\partial g_{\mu\nu}}{\partial x^\lambda}
-\Gamma^\sigma{}_{\lambda\mu}g_{\sigma\nu}
-\Gamma^\sigma{}_{\lambda\nu}g_{\mu\sigma}.$$

取 $\mu=\nu=\varphi$、$\lambda=\theta$。只有 $\Gamma^\varphi{}_{\theta\varphi}=\Gamma^\varphi{}_{\varphi\theta}=\cot\theta$ 相关：

$$\nabla_\theta g_{\varphi\varphi}
=\frac{\partial g_{\varphi\varphi}}{\partial\theta}
-2\Gamma^\varphi{}_{\theta\varphi}g_{\varphi\varphi}
=2a^2\sin\theta\cos\theta-2(\cot\theta)\left(a^2\sin^2\theta\right).$$

第二项 $=2a^2\sin\theta\cos\theta$，两项精确抵消：

$$\nabla_\theta g_{\varphi\varphi}=0 .$$

**其余组合同理：** 不含导数的那些，$\partial g=0$ 且 $\Gamma$ 项要么为零、要么成对抵消（如 $\nabla_\varphi g_{\theta\theta}$）；含 $\partial_\theta g_{\varphi\varphi}$ 的只有上面这一种。所以 $\nabla_\lambda g_{\mu\nu}=0$ 在整个球面上成立。

**意义：** 这是"度规相容"的具体验证——平行移动不改变长度和角度。$\Gamma$ 公式里那个 $\frac12$ 正是为了让这条成立而设计的。


**10.30** 设一族测地线 $x^\mu(\tau,s)$，$\tau$ 是仿射参数，$s$ 标记不同的曲线。定义

$$u^\mu=\frac{\partial x^\mu}{\partial\tau},\qquad
\xi^\mu=\frac{\partial x^\mu}{\partial s}.$$

**第一步，两个导数可交换：** $\dfrac{\partial u^\mu}{\partial s}=\dfrac{\partial\xi^\mu}{\partial\tau}$（偏导次序无关）。

**第二步，对测地线方程沿 $s$ 求导。** 每一条都是测地线：

$$\frac{\partial u^\mu}{\partial\tau}+\Gamma^\mu{}_{\nu\rho}u^\nu u^\rho=0 .$$

对 $s$ 求导，用第一步把 $\partial_s u^\mu$ 换成 $\partial_\tau\xi^\mu$，再把 $\partial_s$ 的导数用 $\partial_s x^\lambda=\xi^\lambda$ 展开（链式法则），得到

$$\frac{D^2\xi^\mu}{D\tau^2}
=-R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma .$$

**第三步，读出每一项的含义：** 左边是分离矢量沿测地线的"二阶协变加速度"；右边是黎曼张量乘上切矢量与分离矢量。**这是一个张量方程**（两边都是张量），所以它在任何坐标系里都成立——这正是它比"潮汐力"这种说法更可靠的地方。

**检验（球面）：** 两条经线，$\xi=a\sin\theta\,\Delta\varphi$，$\theta=\tau/a$。右边缩并后给 $\ddot\xi=-K\xi$；左边是 $\ddot\xi$（在一维分离的情形下协变导数简化为普通二阶导）。代入 $K=1/a^2$ 得 $\ddot\xi=-\xi/a^2$，解正是 $\xi\propto\sin(\tau/a)$ ✓——与 10.25 的结果一致。


### 概念与判断 10.31–10.39

**10.31** 错。张量是"按固定规则变换的量"，不是"某种排列方式"。同一个物理量在不同坐标下是不同的数组；反过来，随便摆成矩阵的数字（比如三个数排成 $2\times2$）未必按张量变换。判据是变换律，不是外观。


**10.32** 错。"在一点令 $\Gamma=0$"只说明那一点的**一阶**导数为零（局部惯性系），而曲率是 $\Gamma$ 的**导数**组合，一点上不为零。类比：抛物线顶点处斜率为零，但二阶导数不为零，曲线还是弯的。**"局部平直"永远是近似的、一阶的。**


**10.33** 错。极坐标下 $\Gamma\ne0$ 只说明"坐标的基矢量在转"，与空间是否弯曲无关。判据是 $R^\rho{}_{\sigma\mu\nu}$：把极坐标的 $\Gamma$ 代进去，两项精确抵消，$R\equiv0$（10.6.4 已算）。**"联络非零"和"空间弯曲"是两件事。**


**10.34** 只在"局部、且两点之间没有共轭点"时成立。反例：球面上连接两点的两条测地线，长的那条不是最短；再比如圆柱面上绕圈的测地线可以任意长。**测地线的正确定义是"切矢量自平行"，"最短"是它的一个局部性质。**


**10.35** 对。这是**零张量原理**：张量的变换律是线性的，零必映到零。

**为什么重要：** 它把"证明一个张量方程"变成"在一个坐标系里验证它"。比如 10.6.4 里证明平面的曲率为零，只在极坐标下算了一遍；因为 $R$ 是张量，它在极坐标为零就意味着处处为零，不需要再到直角坐标里验证。

**反过来用：** 如果某个量在直角坐标里为零、在极坐标里非零，它一定不是张量（$\Gamma$ 就是这样暴露的）。

**注意前提：** 这句话只对**张量**成立。非张量的量（比如 $\Gamma$、$\partial_\mu v^\nu$）在某坐标系里为零，不说明它在别处也为零。


**10.36** 错。度规分量按

$$g'_{\mu\nu}=\frac{\partial x^\alpha}{\partial x'^\mu}
\frac{\partial x^\beta}{\partial x'^\nu}g_{\alpha\beta}
$$

变换，取行列式得

$$\det g'=\det g\cdot\left|\det\frac{\partial x}{\partial x'}\right|^2 .$$

所以 $\det g$ 不是标量，而是"带权"的量（密度）。**在坐标变换下不变的是** $\sqrt{\lvert g\rvert}\,\mathrm{d}^4x$：体积元前面的因子与雅可比相消，所以

$$\int f\sqrt{\lvert g\rvert}\,\mathrm{d}^4x$$

是坐标无关的。这就是弯曲空间里积分的正确写法（也是作用量原理里必须有 $\sqrt{\lvert g\rvert}$ 的原因）。

**记法：** $\det g<0$（洛伦兹号差）时要用 $\lvert g\rvert$。


**10.37** 错，而且错在最容易被指标外观骗的地方。

**理由一（变换律）：** 张量的变换律只含一阶导数（雅可比因子）。$\Gamma$ 的变换律含有 $\partial^2x'/\partial x^2$ 那一项，所以它不是张量。

**理由二（零张量原理）：** 平直空间的直角坐标里 $\Gamma\equiv0$；换到同一空间的极坐标，$\Gamma\ne0$。若 $\Gamma$ 是张量，零张量在任何坐标下都该是零——矛盾。

**"能带上下标" 是障眼法：** 记号上 $\Gamma$ 有三个指标，可以做形式上的升降，但这么做的结果**依赖坐标系**，没有几何意义。就像"坐标本身"也有上标 $x^\mu$，但 $x^\mu$ 不是矢量（它的变换律是仿射的，不是线性的）。

**能出现在方程里的合法方式：** (i) 作为协变导数的一部分（$\nabla_\lambda v^\mu$ 整体是张量）；(ii) 两个 $\Gamma$ 的组合，比如 $R$ 里那些二次项。单独的 $\Gamma$ 只能写"在某坐标系下成立"的式子。


**10.38** 错。$\Gamma^\varphi{}_{\theta\varphi}=\cot\theta$ 在 $\theta\to0$ 发散，是因为 $\varphi$ 这个坐标在北极没有定义（所有经线汇聚），不是几何坏了。判据还是那一条：算标量曲率 $R=2/a^2$，在北极有限 ✓。**坐标奇点的特征是"某个坐标分量发散而曲率标量有限"**，这与真奇点（曲率发散）完全不同。


**10.39** 需要纠正两点。

**第一，"潮汐力"不是作用在单个粒子上的力。** 单个粒子在引力场里自由下落时是"失重"的——它感受不到任何力，走的是测地线。潮汐效应是**两个相邻粒子之间的相对加速度**，由测地线偏离方程给出，正比于黎曼张量。

**第二，正因为它是相对的、坐标无关的，它才是"时空弯曲"的证据，而不是"引力是力"的证据。** 力可以被变换掉（换到自由下落系），潮汐效应不能——它是曲率。

**正确的说法：** 引力在广义相对论里不是力，是时空的几何；"物体被引力拉向地球"在数学上是"物体沿弯曲时空的测地线运动"。**测地线偏离方程是把"弯曲"翻译成"可测量效应"的那句话**，而它的右边只能由 $R$ 给出，不能由任何"力"给出。

