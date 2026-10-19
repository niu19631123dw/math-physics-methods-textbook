# 附录 E 矢量微积分与积分定理

> 第 3 章的 Green 函数反复用到「通量 = 源」和「边界值决定内部」，这一页把背后的定理补齐。

## E.1 三个算子

| 算子 | 作用 | 记号 | 一句话 |
|---|---|---|---|
| 梯度 | 标量 → 矢量 | $\nabla f$ | 指向 $f$ 增长最快的方向，大小是增长率 |
| 散度 | 矢量 → 标量 | $\nabla\cdot\mathbf F$ | 单位体积内「源」的强度 |
| 旋度 | 矢量 → 矢量 | $\nabla\times\mathbf F$ | 单位面积上的环量，描述涡旋 |

在直角坐标下：

$$\nabla f=\left(\partial_xf,\ \partial_yf,\ \partial_zf\right),$$

$$\nabla\cdot\mathbf F=\partial_xF_x+\partial_yF_y+\partial_zF_z,$$

$$\nabla\times\mathbf F=\left(\partial_yF_z-\partial_zF_y,\ \partial_zF_x-\partial_xF_z,\ \partial_xF_y-\partial_yF_x\right).$$

**记住物理意义比记住公式重要：** 散度问「这里有没有源」，旋度问「这里有没有打转」。

## E.2 Gauss 定理

$$\int_V\nabla\cdot\mathbf F\,dV=\oint_{\partial V}\mathbf F\cdot d\mathbf S.$$

**读法：体积内源的总量，等于穿过边界的总通量。** 如果某个区域内没有源（$\nabla\cdot\mathbf F=0$），那么进去多少就出来多少。

它的直接推论是**连续性方程**：电荷密度 $\rho$ 与电流密度 $\mathbf J$ 满足

$$\partial_t\rho+\nabla\cdot\mathbf J=0,$$

也就是「电荷不会凭空产生或消失」。

## E.3 从 Gauss 定理推出库仑定律

设原点有点电荷 $q$，场是球对称的。取半径 $r$ 的球面，由对称性 $\mathbf E=E(r)\hat{\mathbf r}$，通量

$$\oint\mathbf E\cdot d\mathbf S=4\pi r^2E(r).$$

高斯定理右边是 $q/\varepsilon_0$，所以

$$4\pi r^2E(r)=\frac{q}{\varepsilon_0}
\quad\Longrightarrow\quad
E(r)=\frac{q}{4\pi\varepsilon_0r^2}.$$

**库仑定律不是孤立实验事实的简单记录，它等价于「点源 + 球对称 + Gauss 定理」。** 反过来，如果你从库仑定律出发，也就顺带验证了 Gauss 定理。

## E.4 Green 恒等式

对 $u\nabla^2v-v\nabla^2u$ 用 Gauss 定理（取 $\mathbf F=u\nabla v-v\nabla u$），得到 **Green 第二恒等式**：

$$\int_V\left(u\nabla^2v-v\nabla^2u\right)dV
=\oint_{\partial V}\left(u\frac{\partial v}{\partial n}-v\frac{\partial u}{\partial n}\right)dS.$$

**这就是第 3 章「Green 函数能表示任意源」的数学来源。** 取 $v=G$、$\nabla^2G=\delta(\mathbf r-\mathbf r')$，左边只剩 $u(\mathbf r')$ 加一个体积分，右边是边界上的项。边界项消失（Dirichlet 或 Neumann 条件）后，就得到

$$u(\mathbf r')=\int_V G(\mathbf r,\mathbf r')\nabla^2u(\mathbf r)\,dV,$$

也就是「源乘以 Green 函数再积分」。

## E.5 法线方向约定

$\partial/\partial n$ 是沿**外法线**的方向导数。对 $z>0$ 的半空间，边界 $z=0$ 的外法线指向 $-z$ 方向，所以

$$\frac{\partial\phi}{\partial n}=-\frac{\partial\phi}{\partial z}.$$

于是导体表面的感应电荷密度

$$\sigma=\varepsilon_0 E_n
=-\varepsilon_0\frac{\partial\phi}{\partial z}.$$

**符号算错，十有八九是法线方向取反了。** 判断方法：外法线永远指向「区域外面」；区域在 $z>0$，外法线就是 $-z$。

## E.6 常用恒等式

$$\nabla\cdot(\nabla\times\mathbf A)=0,\qquad
\nabla\times(\nabla f)=0.$$

「旋度的散度为零」「梯度的旋度为零」——这两条在物理里分别对应「没有磁单极」和「静电场无旋」。

$$\nabla\cdot(f\mathbf A)=f\nabla\cdot\mathbf A+\mathbf A\cdot\nabla f,$$

$$\nabla^2\mathbf A=\nabla(\nabla\cdot\mathbf A)-\nabla\times(\nabla\times\mathbf A).$$

## E.7 Stokes 定理

$$\int_S(\nabla\times\mathbf F)\cdot d\mathbf S=\oint_{\partial S}\mathbf F\cdot d\mathbf l.$$

**读法：穿过曲面的旋度总量，等于沿边界的环量。** 安培环路定理、法拉第电磁感应定律，都是它的特例。第 4 章绕流里的环量

$$\Gamma=\oint\mathbf v\cdot d\mathbf l$$

也是同一个对象。

## E.8 弯曲空间中的 Gauss 定理

前面各节都默认直角坐标。在弯曲空间（或任意坐标系）里，散度要改用协变导数：

$$\nabla_\mu v^\mu=\frac{1}{\sqrt{|g|}}\partial_\mu\left(\sqrt{|g|}\,v^\mu\right),$$

其中 $g=\det g_{\mu\nu}$。积分要用不变量体积元 $\sqrt{|g|}\,d^nx$。于是 Gauss 定理写成

$$\int_V\nabla_\mu v^\mu\,\sqrt{|g|}\,d^nx
=\oint_{\partial V}v^\mu n_\mu\,\sqrt{|h|}\,d^{n-1}x,$$

$h$ 是边界上的诱导度规。

**为什么 $\sqrt{|g|}$ 是必须的？** 因为 $\Gamma^\mu_{\mu\nu}=\partial_\nu\ln\sqrt{|g|}$，正是它把普通散度和协变散度联系起来。**没有这个因子，弯曲空间里的 Gauss 定理就不成立。**

这就是第 3 章 Green 函数方法在弯曲时空里的推广方式——第 7 章的联络，正是为这一步准备的。
