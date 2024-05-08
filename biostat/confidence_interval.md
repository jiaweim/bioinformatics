# 置信区间

## 简介

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

## 构造置信区间

先从简单的 z-分布介绍，实际应用将 z-分布换成 t-分布即可。

$$
z=\frac{\overline{Y}-\mu}{\sigma/\sqrt{n}}
$$

查 z-表，我们知道：

$$
P(-1.96\le z\le 1.96)=0.95
$$

待入 $z$：

$$
P(-1.96\le \frac{\overline{Y}-\mu}{\sigma/\sqrt{n}}\le 1.96)=0.95
$$

$$
P(-1.96\cdot\frac{\sigma}{\sqrt{n}}\le \overline{Y}-\mu\le 1.96\cdot\frac{\sigma}{\sqrt{n}})=0.95
$$

