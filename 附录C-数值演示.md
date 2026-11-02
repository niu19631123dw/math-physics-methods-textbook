# 附录 C 数值演示

> 这本书里很多结论，用十行代码就能自己验证一遍。这一页给五个最小实验：每个都能在一分钟内跑完（只需要 numpy），跑出来的数字与正文的结论对照，比背公式有用。

## C.1 级数在跳变处过冲多少（第 2 章）

方波的傅里叶部分和

$$S_N(x)=\sum_{n=1,3,5,\dots}^{N}\frac{4}{n\pi}\sin(nx)$$

在 $x=\pi/2$ 附近过冲。跑一下：

```python
import numpy as np
x = np.linspace(-np.pi, np.pi, 400001)
for N in (5, 25, 101):
    S = sum(4/(n*np.pi)*np.sin(n*x) for n in range(1, N+1, 2))
    print(N, round(S.max(), 4))
```

输出（约）：`5 1.1884`、`25 1.1795`、`101 1.1790`。方波的跳变高度是 2，过冲量约 $0.179$，占跳变的 $8.95\%$。**无论 $N$ 多大，这个百分比都不变**——这就是吉布斯现象：峰值不收敛到 1，只收敛到 $1.0895$。正文说「收敛不等于一致收敛」，指的就是这件事。

## C.2 鼓膜的频率比（第 3 章）

圆膜的本征频率正比于 $J_m$ 的零点。用级数算 $J_0$ 的零点：

```python
import numpy as np, math
def J0(x, N=40):
    return sum((-1)**k*(x/2)**(2*k)/math.factorial(k)**2 for k in range(N))

zeros = []
x = 0.1
while len(zeros) < 4:
    if J0(x)*J0(x+0.001) < 0:
        lo, hi = x, x+0.001
        for _ in range(60):
            mid = (lo+hi)/2
            if J0(lo)*J0(mid) <= 0: hi = mid
            else: lo = mid
        zeros.append((lo+hi)/2)
    x += 0.001
print([round(z, 4) for z in zeros])
print([round(z/zeros[0], 4) for z in zeros])
```

输出 $j_{0,n}\approx$ `2.4048, 5.5201, 8.6537, 11.7915`，比值 `1, 2.2954, 3.5985, 4.9033`。

**对照：** 弦的频率比是 $1:2:3:4$，整数倍；圆膜是 $1:2.295:3.599:4.903$，**不是整数倍**。所以鼓声听起来「没有音高」，而弦有。这不是错觉，是零点间距的数学后果。

## C.3 波包为什么会展宽（第 8 章）

高斯波包的宽度随时间增长，但**两种过程的增长方式不一样**。自由粒子（色散型）：

$$\sigma(t)=\sigma_0\sqrt{1+\left(\frac{t}{t_0}\right)^2},\qquad t_0=\frac{2m\sigma_0^2}{\hbar};$$

扩散（抛物型）：

$$\sigma(t)=\sigma_0\sqrt{1+\frac{t}{t_0}},\qquad t_0=\frac{\sigma_0^2}{2\alpha}.$$

**平方在括号里还是在根号里，就是"波包"与"扩散"的区别**：前者长时间按 $t$ 线性展宽，后者按 $\sqrt t$。下面数值地看频谱宽度：

```python
import numpy as np
x = np.linspace(-20, 20, 200001)
for s in (0.5, 1.0, 2.0):
    f = np.exp(-x**2/(4*s*s))
    F = np.abs(np.fft.fftshift(np.fft.fft(f)))
    k = np.fft.fftshift(np.fft.fftfreq(len(x), d=x[1]-x[0]))*2*np.pi
    m = np.sum(F**2)
    print(s, round(np.sqrt(np.sum(F**2*k**2)/m), 4), round(1/(2*s), 4))
```

最后一列是理论值 $\Delta k=1/(2\sigma)$（按标准差定义）。**$\sigma$ 缩小一半，$\Delta k$ 就放大一倍**——带宽定理不是不等式巧合，是傅里叶变换的内禀性质。

## C.4 迭代法解拉普拉斯方程（第 2、5 章）

边值问题不一定非要解析解。把区域切成网格，用「每点等于四邻平均」迭代：

```python
import numpy as np
n = 61
u = np.zeros((n, n))
u[0, :] = 100.0          # top edge at 100, others at 0
for it in range(4000):
    u[1:-1, 1:-1] = 0.25*(u[:-2, 1:-1] + u[2:, 1:-1] + u[1:-1, :-2] + u[1:-1, 2:])
print(round(u[n//2, n//2], 2))
```

输出约 `24.8`。正方形区域、三边为 0、一边为 100 时，解析解的中心值是 25（可用分离变量验证）；网格越密、迭代越久，数值解越靠近它。**差的这一点就是离散化误差**，它不会随迭代消失，只会随网格变细变小。**这就是松弛法的全部内容**：它与第 2 章的级数解是同一个问题的两种算法，一个给公式，一个给数。

## C.5 瑞利商有多准（第 9 章）

用试探函数 $u=x(L-x)$ 估两端固定弦的基频。瑞利商

$$R[u]=\frac{\displaystyle\int_0^L\left(\frac{\mathrm{d}u}{\mathrm{d}x}\right)^2\mathrm{d}x}{\displaystyle\int_0^L u^2\,\mathrm{d}x}$$

对 $u=x(L-x)$ 算出 $R=10/L^2$，而精确值是 $\pi^2/L^2\approx9.8696/L^2$：

```python
import numpy as np
L = 1.0
x = np.linspace(0, L, 200001)
u = x*(L-x)
du = L - 2*x
print(round(np.trapezoid(du**2, x)/np.trapezoid(u**2, x), 4), round(np.pi**2, 4))
```

（`np.trapezoid` 是 numpy 2.x 的名字，旧版写 `np.trapz`。）输出 `10.0` 对 `9.8696`：**偏高 1.3%。**

瑞利商永远给上界（变分原理的直接后果），所以估出来的基频总是偏高。这个性质很有用：换个更合理的试探函数，估值只会更靠近真值，不会越过它。
