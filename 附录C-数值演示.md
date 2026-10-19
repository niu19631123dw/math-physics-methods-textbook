# 附录 C 数值演示

> 公式说得再漂亮，也不如亲眼看见一次。这一页的代码都很短，可以逐段跑。

依赖：`numpy`、`scipy`、`matplotlib`。没有这些库时，`pip install numpy scipy matplotlib`。

## C.1 Gibbs 现象

用前 $N$ 个奇次谐波逼近方波，看跳变附近的过冲。**过冲幅度不随 $N$ 减小**，这是第 1 章 J1.4 的可视化。

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 2000)

def square_partial(x, N):
    s = np.zeros_like(x)
    for n in range(1, 2 * N, 2):          # 只取奇次谐波
        s += (4 / (np.pi * n)) * np.sin(n * x)
    return s

plt.figure(figsize=(8, 4))
plt.plot(x, np.sign(np.sin(x)), 'k--', lw=1, label='square')
for N in (5, 25, 100):
    plt.plot(x, square_partial(x, N), label=f'N={N}')
plt.ylim(-1.4, 1.4)
plt.legend()
plt.title('Gibbs overshoot: ~9% regardless of N')
plt.show()
```

跑一下你会发现：三条曲线在跳变处的峰值都停在 $1.18$ 附近（约 18% 过冲，相对半幅是 9%）。**加项不会去掉它。**

## C.2 弦的简正模与叠加

第 1 章的 $u(x,t)=\sum a_n\cos\omega_nt\sin(n\pi x/L)$。这里只画空间形状，看「在 $L/3$ 处拨弦」会激发哪些模式。

```python
import numpy as np
import matplotlib.pyplot as plt

L = 1.0
x = np.linspace(0, L, 400)
x0 = L / 3

h = 0.1                       # 拨弦高度

plt.figure(figsize=(8, 4))
for n in range(1, 7):
    a_n = (2 * h * L**2) / (n**2 * np.pi**2 * x0 * (L - x0)) \
          * np.sin(n * np.pi * x0 / L)
    plt.plot(x, a_n * np.sin(n * np.pi * x / L), label=f'n={n}')
plt.legend(ncol=2)
plt.title('Mode amplitudes for plucking at x = L/3')
plt.show()
```

**看 $n=3$ 那条线**：它在 $x=L/3$ 处正好过零，所以根本不会被激发。这就是「在节点处拨弦，该模不响」。

## C.3 鼓的频率比

第 2 章的核心结论：鼓的频率比是 Bessel 零点比。

```python
import numpy as np
from scipy.special import jn_zeros

for m in range(3):
    j = jn_zeros(m, 4)
    print(f'm={m}:', np.round(j / jn_zeros(0, 1)[0], 4))
```

输出是 `m=0: [1. 2.295 3.598 4.903]`（已按 $j_{0,1}$ 归一化）。**这些数没有公倍数**，所以鼓声没有明确音高。对比正方形膜的 $\sqrt{(m^2+n^2)/2}$：

```python
import numpy as np
mn = [(1, 1), (1, 2), (2, 2), (1, 3), (2, 3), (3, 3)]
ratios = [np.sqrt((m**2 + n**2) / 2) for m, n in mn]
print(np.round(ratios, 4))      # [1.  1.5811 2.  2.2361 2.5495 3. ]
```

对比一下就能看出：正方形膜有 $1:\sqrt{5/2}:2:\sqrt5$ 这种「还算整齐」的比例；圆膜的零点比更乱，没有任何简单的整数或根式关系。

## C.4 热核：扩散怎么抹平细节

第 3 章的热核 $G(x,t)=\frac{1}{\sqrt{4\pi\alpha t}}e^{-x^2/4\alpha t}$。

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 500)
for t in (0.01, 0.05, 0.2, 1.0):
    G = np.exp(-x**2 / (4 * t)) / np.sqrt(4 * np.pi * t)
    plt.plot(x, G, label=f't={t}')

plt.legend()
plt.title('Heat kernel spreading: width ~ sqrt(t), peak ~ 1/sqrt(t)')
plt.show()
```

**面积恒为 1，宽度按 $\sqrt t$ 增长，峰值按 $1/\sqrt t$ 下降。** 这就是「扩散不是传播，是摊开」。

## C.5 用 FFT 看混叠

第 5 章 J5.3：采样率不够时，高频会伪装成低频。下面用 $1.3\ \text{kHz}$ 信号、$1\ \text{kHz}$ 采样。

```python
import numpy as np
import matplotlib.pyplot as plt

fs = 1000.0                 # 采样率
t = np.arange(0, 1.0, 1 / fs)
f_true = 1300.0             # 真实频率
x = np.cos(2 * np.pi * f_true * t)

# 频谱
X = np.fft.rfft(x)
freq = np.fft.rfftfreq(len(x), 1 / fs)
peak = freq[np.argmax(np.abs(X))]
print('apparent peak:', peak, 'Hz')   # 会是 300 Hz
```

**输出是 300 Hz**，因为 $1300-1000=300$。看频谱你完全看不出它其实是 1300 Hz。这就是为什么采样定理不是「建议」。

## C.6 验证一个留数积分

第 4 章的 $\int_{-\infty}^{\infty}\frac{\cos(ax)}{1+x^2}dx=\pi e^{-a}$。数值积分对一下：

```python
import numpy as np
from scipy.integrate import quad

for a in (0.5, 1.0, 2.0):
    val, _ = quad(lambda x: np.cos(a * x) / (1 + x**2), -50, 50)
    print(f'a={a}: numeric={val:.6f}, exact={np.pi*np.exp(-a):.6f}')
```

两者在 $10^{-3}\sim10^{-2}$ 量级内一致（具体取决于 $a$：$a$ 越小，截断误差越大）。**注意积分上限取 50 而不是无穷**——数值积分需要截断，而截断误差本身就是一个判断点：$\cos(ax)/(1+x^2)$ 在 $x$ 大时按 $1/x^2$ 衰减，截断到 50 的误差约 $1/50$ 量级，够用；但如果被积函数按 $1/x$ 衰减，这个截断就完全不够。

## C.7 一个可以自己做的练习

把 C.1 的方波换成一个三角波（初始位移连续，但导数不连续），观察：

1. 过冲还在不在？
2. 收敛速度比方波快还是慢？

提示：三角波的 Fourier 系数按 $1/n^2$ 衰减，而方波按 $1/n$ 衰减。**收敛速度由函数的「光滑程度」决定**——这是判断「我该取多少项」的直接依据，比任何经验公式都可靠。
