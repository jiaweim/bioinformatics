# 统计常用术语

- [统计常用术语](#统计常用术语)
  - [1. 概述](#1-概述)
  - [2. 中心位置](#2-中心位置)
  - [3. 分散程度](#3-分散程度)
  - [4. 期望值](#4-期望值)
  - [5. 变异系数](#5-变异系数)
  - [6. 频率](#6-频率)

2024-05-07 ⭐
@author Jiawei Mao
***

## 1. 概述

生物统计学：从样本估计总体——**以小博大**。

术语：

- 总体（population）：研究的对象，或感兴趣的对象，如一座山的橙子；
- 总体大小（population size）：N，比如一座山上有 527692 个橙子，不过大多时候不知道具体值；
- 变量（variable）：感兴趣的属性，例如橙子的甜度；
- 观测值（observation）：变量的具体值，如测到的橙子的具体甜度，总体的观测值有 N 个；
- 样本（sample）：总体的子集，要有**代表性**，才能从样本估计总体；
- 样本大小（sample size）：n，比如 100 个橙子；

如何拿到有**代表性的样本**：

- 抽样技术（sampling technique）
- 实验设计（experimental design）

拿到有代表性样本后：

- 计算样本观测值的一些特性；
- 从计算的特性，推测总体的参数；

从**样本**计算出来的值，如平均值，方差，称为**统计量**（statistic）。

对应总体的特性，如平均值，方差，称为**参数**（parameter）。

|特性|样本统计量（statistic）|总体参数（parameter）|
|---|---|---|
|平均值|$\overline{X}$|$\mu$|
|方差|$s^2$|$\sigma^2$|

## 2. 中心位置

样本均值：

$$
\overline{X}=\frac{\sum_{i=1}^n X_i}{n}
$$

总体均值：

$$
\mu=\frac{\sum_{i=1}^N X_i}{N}
$$

中位数（median）：将观测值从小到大进行排序，取中间值

- 如果有奇数观测值，取最中间的观测值；
- 如果有偶数个观测值，取中间两个的平均值。

众数（mode）：出现次数最多的观测值。

## 3. 分散程度

**范围（range）**：最小值到最大值的范围。

**方差**（variance）：指示观测值参差不齐的程度

$$
V(X)=\sigma_X^2=\frac{\sum_{i=1}^N (X_i-\mu)^2}{N}=\frac{SS}{N}
$$

> SS: sum of square，所以 variance 又称为 mean square。

**标准差**（standard deviation）：方差的单位不大好，所以引入标准差 

$$
\sigma_X=+\sqrt{\sigma_X^2}
$$

只取正值，因为分散程度，最小为 0，对应没有分散。标准差的单位与观测值单位一样。

**方差的性质：**

$$
V(X+C)=V(X)
$$

$$
V(CX)=C^2V(X)
$$

> C 为常数，带入公式很容易证明上面两个性质。

**样本的方差：**

$$
s_X^2=\frac{\sum_{i=1}^n(X_i-\overline{X})^2}{n-1}
$$

> n-1 称为自由度（degree of freedom）

## 4. 期望值

**期望值（expected value）：** 总体参数只有一个，而统计量随着样本不同而不同。对所有可能样本**统计量**的平均值。

以平均值为例，其期望值为：

$$
E(\overline{X})=\frac{\sum \overline{X}_i}{m}
$$

所有样本大小相同。如果期望值和总体参数相等：

$$
E(\overline{X})=\mu
$$

就称 $\overline{X}$ 是 $\mu$ 的**无偏估值（unbiased estimator）**。

**方差的期望：**

$$
E(s^2)=\frac{s_1^2+s_2^2+\cdots+s_m^2}{m}
$$

我们希望方差的期望值等于 $\sigma^2$，这样 $s^2$ 就是 $\sigma^2$ 的无偏估计。为满足该要求，样本方差的分母只能是 $n-1$ （省略了推导）。

## 5. 变异系数

变异系数（coefficient of variation, CV）：

$$
CV=\frac{s}{\overline{X}}\times 100\%
$$

$s$ 和 $\overline{X}$ 的单位与观测值相同，两者相处，得到一个无量纲的 CV。

CV 可以用来比较不同单位观测值的分散程度。

## 6. 频率

频率（frequency, f）：观测值出现的次数。

相对频率（relative frequency, r.f.）

相对累计频率（relative cumulative frequency, r.c.f.）

示例：

|$X_i$|f|r.f.|r.c.f.|
|---|---|---|---|
|18|3|30%|30%|
|19|2|20%|50%|
|20|2|20%|70%|
|21|3|30%|100%|
||$\sum =10$|||

**频率图示：**

frequency histogram -> frequency curve: 随着观测值变密集，直到连续，从 histogram 转变到 curve。
