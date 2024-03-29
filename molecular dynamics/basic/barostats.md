# 恒压方法

- [恒压方法](#恒压方法)
  - [简介](#简介)
  - [Berenedsen barostat](#berenedsen-barostat)
  - [Andersen barostat](#andersen-barostat)
  - [Parrinello-Rahman barostat](#parrinello-rahman-barostat)
  - [参考](#参考)

Last updated: 2022-11-22, 14:18
****

## 简介

分子动力学（MD）是一种模拟分子运行的计算技术。为了评估模拟结果的质量，可恶意将模拟结果与真实实验结果进行比较。如果模拟结果与实验数据接近，则认为模拟结果正确。

在实验室中，化学反应一般在恒压下进行，为了模拟这类数据，需要模拟系统在恒压下随时间的变化。可以认为这类算法在实验中实现了一个气压调节器（barostat），该方法允许瞬间的压力波动，但是压力均值保持恒定。

分子动力学中使用最广泛的系综是 NPT 系综，其原子数（N）、压力（P）和温度（T）是守恒的。因此，恒压算法（barostat）往往与恒温算法（thermostat）一起实现，以便模拟恒温、恒压过程。

## Berenedsen barostat

在 MD 中调节压力和调节温度的思想类似。不过，调节压力需要缩放模拟盒子的体积（V）而不是原子速度。减小盒子尺寸，系统压力增大；反之则压力减小。

从实现角度来看，则是通过缩放原子的坐标来实现体积的缩放。

这就是 Berenedsen 恒压算法的核心思想。假设系统与一个按缩放因子 $\lambda$ 缩放的压力池耦合，在每个时间步：

$$V_i^{new}=V_i^{old}\cdot \lambda$$

缩放体积 $\lambda$ 相当于缩放原子坐标 $\lambda ^{1/3}$。即：

$$r_i^{new}=r_i^{old}\lambda^{1/3}$$

压力 $P$ 在时间上的变化与浴池 $P_{bath}$ 和系统 $P(t)$ 时间的压力差成正比：

$$\frac{\partial P(t)}{\partial t} = \frac{1}{\tau}(P_{bath}- P(t))$$

其中 $\tau$ 表示两个子系统之间的耦合常数，值越大耦合越弱。Berenedsen 稳压器中缩放因子的表达式为：

$$\lambda = \left( 1-  \frac{k\delta t}{\tau}(P(t)- P_{bath})\right)$$

其中 $k$ 是常数，表示物质的等温可压缩性，值越大表示更容易压缩。压力差越大，缩放因子 $\lambda$ 越大。

> **NOTE**: Berenedsen 的主要优点在于可以调节系统和压力浴之间的耦合强度。其主要缺点是，无法从 NPT 系综中正确采样。
> 所以 Berenedsen 一般用在平衡阶段，而不适合生产运行。

## Andersen barostat

Andersen barostat 是一种扩展系统方法，类似于 Nosè-Hoover 恒温方法。通过在运动方程中加入一个额外的自由度，将系统与压力浴耦合。

> **NOTE**: Andersen 恒压方法满足 NPT 系综，因此可以与恒温方法一起，执行 NPT 生产运行。
> 不过，这个方案只支持各向同性变形，即盒子在所有方向的修改是一致的。

## Parrinello-Rahman barostat

Parrinello-Rahman 对 Andersen 进行了扩展，允许改变盒子的形状和大小，即引入了盒子的各向异性变形。

> **NOTE**: Parrinello-Rahman 一般和 Nosè-Hoover 恒温方法一起使用，实现 NPT 系综的生产运行。
> Parrinello-Rahman 是目前在 MD 中使用最多的恒压方法。

## 参考

- https://www.compchems.com/barostats-in-molecular-dynamics/
