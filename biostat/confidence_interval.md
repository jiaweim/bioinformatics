# 置信区间

- [置信区间](#置信区间)
  - [1. 简介](#1-简介)
  - [2. 构造置信区间](#2-构造置信区间)
  - [3. 示例](#3-示例)

2024-05-08 🧡
@author Jiawei Mao
***

## 1. 简介

用样本的统计量估计总体参数，总体参数不可能正好等于样本统计量，而且单个值无法计算概率。

但是，我们可以计算总体参数落在某个区间的概率，这个估计过程称为**区间估计**（interval estimation）。显然：

- 区间越宽，越容易包含总体参数，但是估计精度越低；
- 区间越窄，估计精度越高，但是总体参数落在区间内的概率越低。

区间包含总体参数的概率称为 **confidence coefficient**。

confidence coefficient 其实就是 $1-\alpha$。

理想的置信区间（confidence interval）：

- 区间窄：精度高
- confidence coefficient 高：准确性高

下面以 $\mu$ 为例介绍如何构造 $\mu$ 的置信区间。

## 2. 构造置信区间

先从简单的 z-分布介绍，实际应用将 z-分布换成 t-分布即可。

$$
z=\frac{\overline{Y}-\mu}{\sigma/\sqrt{n}}
$$

查 z-表，我们知道：

$$
P(-1.96\le z\le 1.96)=0.95
$$

代入 $z$：

$$
P(-1.96\le \frac{\overline{Y}-\mu}{\sigma/\sqrt{n}}\le 1.96)=0.95
$$

$$
P(-1.96\cdot\frac{\sigma}{\sqrt{n}}\le \overline{Y}-\mu\le 1.96\cdot\frac{\sigma}{\sqrt{n}})=0.95
$$

$$
P(-1.96\cdot\frac{\sigma}{\sqrt{n}}-\overline{Y}\le-\mu\le 1.96\cdot\frac{\sigma}{\sqrt{n}}-\overline{Y})=0.95
$$

全部乘以 -1：

$$
P(\overline{Y}+1.96\cdot\frac{\sigma}{\sqrt{n}}\ge\mu\ge\overline{Y} -1.96\cdot\frac{\sigma}{\sqrt{n}})=0.95
$$

这就得到了 $\mu$ 的 95% 置信区间。

将其整理一下：

$$
P(\overline{Y} -1.96\cdot\frac{\sigma}{\sqrt{n}}\le\mu\le\overline{Y}+1.96\cdot\frac{\sigma}{\sqrt{n}})=0.95
$$

那么，如何理解这个式子？

对服从正态分布的 $N(\mu, \sigma^2)$ 所有观测值的总体：

$$
Y_1,\cdots,Y_N
$$

其样本均值 $\overline{Y}$ 服从正态分布 $N(\mu_{\overline{Y}},\sigma^2_{\overline{Y}}=\frac{\sigma^2}{n})$。

只要 $\overline{Y}$ 落在 $\mu_{\overline{Y}}\plusmn 1.96\cdot\frac{\sigma}{\sqrt{n}}$ 范围，都将总体平均值 $\mu$ 包含在其中。

但是，我们手头上其实没有 $\sigma$，所以从 z-分布转到 t-分布。

$$
t=\frac{\overline{Y}-\mu}{s/\sqrt{n}}
$$

最终的置信区间为：

$$
P(\overline{Y} -t(0.025)\cdot\frac{s}{\sqrt{n}}\le\mu\le\overline{Y}+t(0.025)\cdot\frac{s}{\sqrt{n}})=0.95
$$

写成更一般的式子：

$$
P(\overline{Y} -t(\alpha/2)\cdot\frac{s}{\sqrt{n}}\le\mu\le\overline{Y}+t(\alpha/2)\cdot\frac{s}{\sqrt{n}})=1-\alpha
$$

> 不用背这个公式，从 t-test 很容易转换为出来。

在指定 $\alpha$ 下，置信区间越小越好：

- $n$ 可控，样本量越大，置信区间越小，等价于估计越精确。

## 3. 示例

某种动物产卵的平均天数 $\mu$。

$n=6$ 个动物，产卵天数分别为：25,30,40,25,35,25。$\overline{Y}=30$, $s^2=40$。

$\text{df}=n-1=5$。

现在用置信区间估计平均产卵天数。

取 $\alpha=0.05$：

$$
P(\overline{Y} -t(\alpha/2)\cdot\frac{s}{\sqrt{n}}\le\mu\le\overline{Y}+t(\alpha/2)\cdot\frac{s}{\sqrt{n}})=1-\alpha\\
P(30 -2.571\cdot\frac{\sqrt{40}}{\sqrt{6}}\le\mu\le30+2.571\cdot\frac{\sqrt{40}}{\sqrt{6}})=0.95\\
P(23.4\le\mu\le 36.6)=0.95
$$
