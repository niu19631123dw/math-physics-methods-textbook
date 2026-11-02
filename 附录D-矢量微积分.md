# 附录 D 矢量微积分与积分定理

> 第 5 章的格林函数反复用到「通量 = 源」和「边界值决定内部」，这一页把背后的定理补齐。读第 5 章之前先扫一遍，卡住时再回来查。

## E.1 三个算子

| 算子 | 作用 | 记号 | 一句话 |
|---|---|---|---|
| 梯度 | 标量 → 矢量 | $\nabla f$ | 指向 $f$ 增长最快的方向，大小是增长率 |
| 散度 | 矢量 → 标量 | $\nabla\cdot\boldsymbol{F}$ | 单位体积内「源」的强度 |
| 旋度 | 矢量 → 矢量 | $\nabla\times\boldsymbol{F}$ | 单位面积上的环量，描述涡旋 |

在直角坐标下：

$$\nabla f=\left(\frac{\partial f}{\partial x},\ \frac{\partial f}{\partial y},\ \frac{\partial f}{\partial z}\right),$$

$$\nabla\cdot\boldsymbol{F}=\frac{\partial F_x}{\partial x}+\frac{\partial F_y}{\partial y}+\frac{\partial F_z}{\partial z},$$

$$\nabla\times\boldsymbol{F}=\left(\frac{\partial F_z}{\partial y}-\frac{\partial F_y}{\partial z},\
\frac{\partial F_x}{\partial z}-\frac{\partial F_z}{\partial x},\
\frac{\partial F_y}{\partial x}-\frac{\partial F_x}{\partial y}\right).$$

**记住物理意义比记住公式重要：** 散度问「这里有没有源」，旋度问「这里有没有打转」。拉普拉斯算子就是「先梯度再散度」：

$$\nabla\cdot(\nabla f)=\nabla^2 f=\frac{\partial^2 f}{\partial x^2}+\frac{\partial^2 f}{\partial y^2}+\frac{\partial^2 f}{\partial z^2}.$$

## E.2 高斯定理

$$\int_V\nabla\cdot\boldsymbol{F}\,\mathrm{d}V=\oint_{\partial V}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}.$$

**读法：体积内源的总量，等于穿过边界的总通量。** 如果某个区域内没有源（$\nabla\cdot\boldsymbol{F}=0$），那么进去多少就出来多少。它的直接推论是**连续性方程**：电荷密度 $\rho$ 与电流密度 $\boldsymbol{J}$ 满足

$$\frac{\partial\rho}{\partial t}+\nabla\cdot\boldsymbol{J}=0,$$

也就是「电荷不会凭空产生或消失」。把 $\rho$ 换成质量密度、$\boldsymbol{J}$ 换成质量流，同一式子就是流体力学里的质量守恒。

## E.3 从高斯定理推出库仑定律

设原点有点电荷 $q$，场是球对称的。取半径 $r$ 的球面，由对称性 $\boldsymbol{E}=E(r)\,\hat{\boldsymbol{e}}_r$，通量

$$\oint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}=4\pi r^2E(r).$$

高斯定理右边是 $q/\varepsilon_0$，所以

$$4\pi r^2E(r)=\frac{q}{\varepsilon_0}
\quad\Longrightarrow\quad
E(r)=\frac{q}{4\pi\varepsilon_0r^2}.$$

**库仑定律不是孤立实验事实的简单记录，它等价于「点源 + 球对称 + 高斯定理」。** 反过来，如果你从库仑定律出发，也就顺带验证了高斯定理。

## E.4 格林恒等式

对 $u\nabla^2v-v\nabla^2u$ 用高斯定理（取 $\boldsymbol{F}=u\nabla v-v\nabla u$），得到 **格林第二恒等式**：

$$\int_V\left(u\nabla^2v-v\nabla^2u\right)\mathrm{d}V
=\oint_{\partial V}\left(u\frac{\partial v}{\partial n}-v\frac{\partial u}{\partial n}\right)\mathrm{d}S .$$

**这就是第 5 章「格林函数能表示任意源」的数学来源。** 取 $v=G$、$\nabla^2G=\delta(\boldsymbol{r}-\boldsymbol{r}')$，左边只剩 $u(\boldsymbol{r}')$ 加一个体积分，右边是边界上的项。边界项消失（狄利克雷条件：$u$ 与 $G$ 在边界上都为零）后，就得到

$$u(\boldsymbol{r}')=\int_V G(\boldsymbol{r},\boldsymbol{r}')\,\nabla^2u(\boldsymbol{r})\,\mathrm{d}V,$$

也就是「源乘以格林函数再积分」。

**诺伊曼条件不一样。** 那里 $\partial G/\partial n$ 不能取零（否则与高斯定理矛盾，见 5.7 节），所以边界项不会消失，它会留下一个边界平均值——这正是第 5 章「诺伊曼问题的解差一个常数」的来源。

## E.5 法线方向约定

$\partial/\partial n$ 是沿**外法线**的方向导数。对 $z>0$ 的半空间，边界 $z=0$ 的外法线指向 $-z$ 方向，所以

$$\frac{\partial\phi}{\partial n}=-\frac{\partial\phi}{\partial z}.$$

导体表面的感应电荷要用**从导体指向场区**的法向（这里是 $+z$），否则符号会反：

$$\sigma=\varepsilon_0E_z\Big|_{z=0}=-\varepsilon_0\left.\frac{\partial\phi}{\partial z}\right|_{z=0}.$$

**两个法向正好相反，这是符号最容易翻车的地方。** $\sigma=\varepsilon_0E_n$ 里的 $n$ 指「从导体指向场区」；格林公式里的 $\partial/\partial n$ 指「从区域指向外」。符号算错，十有八九是把这两个 $n$ 当成了同一个——先问清楚这个 $n$ 属于哪一侧，再决定负号。

## E.6 常用恒等式

$$\nabla\cdot(\nabla\times\boldsymbol{A})=0,\qquad
\nabla\times(\nabla f)=0.$$

「旋度的散度为零」「梯度的旋度为零」——这两条在物理里分别对应「没有磁单极」和「静电场无旋」。

$$\nabla\cdot(f\boldsymbol{A})=f\,\nabla\cdot\boldsymbol{A}+\boldsymbol{A}\cdot\nabla f,$$

$$\nabla\times(f\boldsymbol{A})=f\,\nabla\times\boldsymbol{A}+\nabla f\times\boldsymbol{A},$$

$$\nabla\cdot(\boldsymbol{A}\times\boldsymbol{B})=\boldsymbol{B}\cdot(\nabla\times\boldsymbol{A})-\boldsymbol{A}\cdot(\nabla\times\boldsymbol{B}).$$

## E.7 斯托克斯定理

$$\int_S(\nabla\times\boldsymbol{F})\cdot\mathrm{d}\boldsymbol{S}=\oint_{\partial S}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{l}.$$

**读法：穿过曲面的旋度总量，等于沿边界的环量。** 安培环路定理、法拉第电磁感应定律，都是它的特例。第 7 章绕流里的环量

$$\Gamma=\oint\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}$$

也是同一个对象——那里环量的大小决定升力。

## E.8 弯曲空间中的高斯定理

前面各节都默认直角坐标。在弯曲空间（或任意坐标系）里，散度要改用协变导数：

$$\nabla_\mu v^\mu=\frac{1}{\sqrt{|g|}}\frac{\partial}{\partial x^\mu}\left(\sqrt{|g|}\,v^\mu\right),$$

其中 $g=\det g_{\mu\nu}$。积分要用不变量体积元 $\sqrt{|g|}\,\mathrm{d}^nx$。于是高斯定理写成

$$\int_V\nabla_\mu v^\mu\,\sqrt{|g|}\,\mathrm{d}^nx
=\oint_{\partial V}v^\mu n_\mu\,\sqrt{|h|}\,\mathrm{d}^{n-1}x,$$

$h$ 是边界上的诱导度规。

**为什么 $\sqrt{|g|}$ 是必须的？** 因为 $\Gamma^\mu{}_{\mu\nu}=\partial_\nu\ln\sqrt{|g|}$，正是它把普通散度和协变散度联系起来。**没有这个因子，弯曲空间里的高斯定理就不成立。**

这是第 5 章格林函数方法在弯曲时空里的推广方式——第 10 章的联络，正是为这一步准备的。

## E.9 一张对照表

| 直角坐标写法 | 分量写法 | 什么时候用 |
|---|---|---|
| $\nabla f$ | $(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\frac{\partial f}{\partial z})$ | 要算具体分量时 |
| $\nabla\cdot\boldsymbol{F}$ | $\frac{\partial F_x}{\partial x}+\frac{\partial F_y}{\partial y}+\frac{\partial F_z}{\partial z}$ | 写守恒律、验证「无源」时 |
| $\nabla\times\boldsymbol{F}$ | 见 E.1 | 讨论涡旋、环量时 |
| $\nabla^2 f$ | $\frac{\partial^2 f}{\partial x^2}+\frac{\partial^2 f}{\partial y^2}+\frac{\partial^2 f}{\partial z^2}$ | 写方程时（本书统一用 $\nabla^2$） |

**本书的规矩：** 算子记号 $\nabla$、$\nabla^2$ 可以用；但**只要写出分量，偏导数就要写全**，不写 $F_{x,x}$ 这种省略。
