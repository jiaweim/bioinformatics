# 使用深度学习从肽段序列预测肽段的 LC-MS/MS 属性

- [使用深度学习从肽段序列预测肽段的 LC-MS/MS 属性](#使用深度学习从肽段序列预测肽段的-lc-msms-属性)
  - [摘要](#摘要)
  - [简介](#简介)
  - [实验步骤](#实验步骤)
    - [数据来源](#数据来源)
  - [参考](#参考)

2022-02-07, 19:18
***

## 摘要

使用 LSTM 循环神经网络模型预测：

- 索引保留时间（Indexed retention times, iRT）
- MS1 价态分布（SM1 charge state distribution）
- MS/MS谱峰强度。

使用 $10^5$ 量级的数据集用于训练 iRT 和价态分布模型。使用 $2\times 10^6$ 实验谱图预测 HCD 碎片例子强度。采用简单的深度学习结构模型就能高精度地预测这三种关键的 LC-MS/MS 属性。

提出两种特征化方案，并证明能有效编码修饰。iRT 预测模型和 HCD 离子强度预测模型的精度已达到目前文献报道的最先进水平。MS1 价态分布预测模型也具有较高水平。这些预测模型可用来提高 DDA 和 DIA中 肽段的鉴定和定量，也可以辅助 MRM 和 PRM 实验设计。

## 简介

从肽段的氨基酸序列直接预测 LC-MS/MS 行为将为下一代蛋白质组研究的发展提供动力。目前主要用实验手段获得 LC-MS/MS 特征，其成本高，精度也不均一。这项工作旨在使用常见的深度学习模型来解决这些问题，通过实验数据来训练模型。使用深度学习模型预测三个关键的 LC-MS/MS 特征：

- indexed retention times (iRT)
- precursor charge state distributions
- MS/MS sequence ion intensities

这些属性可以直接用于增强 DDA 和 DIA 肽段鉴定和定量，也可以辅助 MRM 和 PRM 实验设计。

这项工作的核心是判断完全由肽段决定的 LC-MS/MS 关键属性。所选择的三个属性符号标准。

- 母离子价态分布还没有被广泛用于肽段的鉴定和定量。
- iRT 校准策略可用于建立一个通用的尺度来校准实验保留时间。溶剂梯度、柱温、进样量等实验条件可以整合到 iRT 与 RT 的校准函数中。
- MS1 价态分布会随着实验条件而变化。其中质量分析仪的电荷检测方法影响最大。不过，对常见的质量分析仪，MS1 价态分布相对其它许多实验条件都是稳定的。
- 对 MS/MS 序列离子强度的预测，不同的离子类型在质谱中的碎裂方法可能不同，碎片例子强度还会随着质量分析仪的变化而变化。谱图还会受激发能量（activation energe）和激发时间的影响。不过，在常用仪器和标准方法下，MS/MS 谱图是稳定的。

深度监督学习模型能够完成分类和回归任务，iRT 和谱图预测模型是典型的回归离子，电荷状态预测模型可以看作电荷分类概率的分类方法。这里展示的三个预测模型代表了 LC-MS/MS 中三个数据级别：

- 用于 LC 行为的 iRT
- 用于 MS1 的电荷状态分布
- MS/MS 水平的 HCD 序列离子强度

它们的输出维度也不同：iRT 是标量，电荷状态分布是向量，HCD 序列离子强度是二维矩阵，其中一个维度取决于肽段长度。这三个模型的核心都是双向 LSTM 层，证明深度学习模型对各种问题的适用性。和其它领域一样，基于深度学习的肽段性质预测模型的性能主要取决于大量、高质量数据的可用性。例如，我们的 HCD 序列离子强度预测模型是建立在从整个蛋白质组学界收集的大量高质量谱图上。

## 实验步骤

### 数据来源

**iRT 数据**由 HeLa 和 HEK293 细胞裂解液进行三次 DIA 技术重复获得，柱长 1m，采集时间 4h。鉴定假阳性控制在 1%，将重复鉴定的肽段和不同电荷的肽段汇总，使用汇总的 iRT 的中位数。肽段长度要求不大于 40，iRT 模型总的肽段数为 125,793，随机选择其中 10% 作为测试集，余下 90% 作为 iRT 模型的训练集。

**电荷状态分布数据**：电荷状态分布模型是从 ProteomeExchange 下载的 DDA 数据。这些数据包括 0.5-4h 单针数据和高 pH 分级样本数据。使用 PAVA （一个 Visual Basic 程序）将raw 数据文件导出为 peak list。使用 MSGF+ 搜索二级谱，蛋白质序列库采用 human proteome (UP000005640)，包含 71,778 条序列（下载时间 20180206）。Trypsin 最大漏切数设为 5，Cys 固定修饰 carbamidomethylation，Met 可变修饰 oxidation，肽段 N-端 glutamine 可变修饰 pyro-glu，蛋白 N-端可变修饰 acetylation，Glu 和 Asp 的 deamidation 可变修饰。母离子 tolerance 10 ppm，仪器设置为 "Q Exactive"。将 peptide EValue 阈值设置为 0.045，获得 1% 的肽段 FDR。





## 参考

- Guan,S. et al. (2019) Prediction of LC-MS/MS Properties of Peptides from Sequence by Deep Learning. Molecular & Cellular Proteomics, 18, 2099–2107.
- Xu,R. et al. (2020) A Comprehensive Evaluation of MS/MS Spectrum Prediction Tools for Shotgun Proteomics. PROTEOMICS, 20, 1900345.
- Bruderer,R. et al. (2017) Optimization of Experimental Parameters in Data-Independent Mass Spectrometry Significantly Increases Depth and Reproducibility of Results*. Molecular & Cellular Proteomics, 16, 2296–2309.
