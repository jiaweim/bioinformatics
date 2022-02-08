# Prediction of LC-MS/MS Properties of Peptides from Sequence by Deep Learning

2022-02-07, 19:18
***

## 简介

预测三个 LC-MS/MS 特征：

- indexed retention times (iRT)
- precursor charge state distributions
- MS/MS sequence ion intensities

其中，母离子价态分布还没有被广泛用于肽段的鉴定和定量。

这些 LC-MS/MS 属性的共有特征仅由肽段序列确定。

iRT 校准策略可用于建立一个通用的刻度来校准实验保留时间。溶剂梯度、柱温、进样量等实验条件可以整合到 iRT 与 RT 的校准函数中。

MS1 价态分布会随着实验条件而变化。其中质量分析仪的电荷检测方法影响最大。不过，对常见的质量分析仪，MS1 价态分布相对其它许多实验条件都是稳定的。

对 MS/MS 序列离子强度的预测，不同的离子序列在质谱中的碎裂方法可能不同，碎片例子强度还会随着质量分析仪的变化而变化。谱图还会受激活能量（activation energe）和激活时间的影响。不过，在常用仪器和标准方法下，MS/MS 谱图是稳定的。

在以上的限制条件下，我们训练具有出色精度的预测 LC-MS/MS 关键属性的深度学习模型。深度监督学习模型能够完成分类和回归任务，iRT 和谱图预测模型是典型的回归离子，电荷状态预测模型可以看作电荷分类概率的分类方法。这里展示的三个预测模型代表了 LC-MS/MS 中三个数据级别：

- 用于 LC 行为的 iRT
- 用于 MS1 的电荷状态分布
- MS/MS 水平的 HCD 序列离子强度

它们的输出维度也不同：iRT 是标量，电荷状态分布是向量，HCD 序列离子强度是二维矩阵，其中一个维度取决于肽段长度。

这三个模型的核心都是双向 LSTM 层，证明深度学习模型对各种问题的适用性。和其它深度学习产生重大影响的领域一样，肽段性质预测模型的性能主要取决于大量和高质量数据的可用性。例如，我们的 HCD 序列离子强度预测模型是建立在从整个蛋白质组学界收集的大量高质量谱图上。

## 实验步骤

### 数据来源

**iRT 数据**由 HeLa 和 HEK293 细胞裂解液进行三次 DIA 技术重复获得，柱长 1m，采集时间 4h。鉴定假阳性控制在 1%，将重复鉴定的肽段和不同电荷的肽段汇总，使用汇总的 iRT 的中位数。肽段长度要求不大于 40，iRT 模型总的肽段数为 125,793，随机选择其中 10% 作为测试集，余下 90% 作为 iRT 模型的训练集。



## 参考

- Guan,S. et al. (2019) Prediction of LC-MS/MS Properties of Peptides from Sequence by Deep Learning. Molecular & Cellular Proteomics, 18, 2099–2107.
- Xu,R. et al. (2020) A Comprehensive Evaluation of MS/MS Spectrum Prediction Tools for Shotgun Proteomics. PROTEOMICS, 20, 1900345.
- Bruderer,R. et al. (2017) Optimization of Experimental Parameters in Data-Independent Mass Spectrometry Significantly Increases Depth and Reproducibility of Results*. Molecular & Cellular Proteomics, 16, 2296–2309.
