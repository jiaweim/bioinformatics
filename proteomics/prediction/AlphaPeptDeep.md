# AlphaPeptDeep

## 摘要

## 简介



## 结果

### AlphaPeptDeep 概述和模型训练

AlphaPeptDeep 框架的目标是能够**轻松构建和训练深度学习模型**，预测依赖于肽段序列的属性。

![](images/2022-12-08-16-22-03.png)

> **Fig.1 AlphaPeptDeep 框架概述**。**a.** 用氨基酸序列编码肽段属性，在 AlphaPeptDeep 中用来训练网络（左）。训练好的模型可提高肽段鉴定灵敏度和准确度。**b.** AlphaPeptDeep 框架读取并嵌入肽段序列。其中 Meta embedding 指元数据嵌入，包括母离子价态、碰撞能量，仪器类型和其它非序列输入。表盘表示可预测不同的性质（RT，CCS，MS2 强度），Custom 指其它肽段属性。底部列出了 AlphaPeptDeep 框架更详细的功能。

第一个难点是嵌入，即将氨基酸序列和 PTM 映射到张量空间。

- 氨基酸，使用长为 27 的 one-hot 编码
- PTM，使用 C, H, N, O, S, P 原子数构成 6D 向量，其它原子使用线性层映射到 2D 向量，最后用 8D 向量表示 PTM。

对构建模型，AlphaPeptDeep 提供了的 API，支持常见的 LSTM、CNN 和 Transformer 等。

对训练和迁移学习，AlphaPeptDeep 提供了通用的训练接口 `model.train()`，对训练后模型的保存，提供了 `model.save()` 方法。AlphaPeptDeep 会同时保存 NN 架构的源码和超参数。

AlphaPeptDeep 在 model shop 模块中提供了多个基于 transformer 和 LSTM 的模型模板。为了演示如何使用 AlphaPeptDeep，建立了一个分类器来预测肽段在 LC 梯度的前半部分还是后半部分出来，训练花了 ~ 16 min，采用标准 HeLa 数据集接近 350K PSMs，模型精度达到 95%（SFig.2）。

![](images/2022-12-11-11-15-30.png)

> **Fig.2** MS2 模型包含 4 个 transformeer 层，RT/CCS 模型由一个 CNN 层与两个

## 讨论

## 方法

## 补充

![](images/2022-12-08-18-44-11.png)

> SFig.1 AlphaPeptDeep 提供了两种嵌入氨基酸的方式：（1）one-hot;（2）torch.Embedding。one-hot 编码先将氨基酸进行 one-hot 编码，然后通过 linear layer 映射到嵌入张量；torch.Embedding 直接从氨基酸 ID 映射到嵌入张量。
> 使用化学组成表示修饰。对 PTM 的嵌入，前面 6 个为C, H, N, O, S 和 P 原子数，对其它原子，则使用一个 linear layer 映射到 2D 向量，所以修饰最后表示为 8-D 向量。

![](images/2022-12-11-10-39-19.png)

> SFig.2 建立深度学习模型，预测肽段在 LC 梯度的前半段还是后半段洗脱（`is_first_half_lc`）。使用 MaxQuant 1% FDR 搜库结果共 351,804 PSM，2h 梯度。如果 PSM 在前 1h 出来，`is_first_half_lc` 设为 1，否则设为 0。将 PSM 分为两部分，80% 用于训练，20% 用于测试，保证序列层次没有交集。16 min 完成训练，在 70,018 测试 PSM 精度达到 95%。



## 参考

- Zeng,W.-F. et al. (2022) AlphaPeptDeep: a modular deep learning framework to predict peptide properties for proteomics. Nat Commun, 13, 7238.
