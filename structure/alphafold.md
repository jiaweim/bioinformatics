# AlphaFold

- [AlphaFold](#alphafold)
  - [AlphaFold 蛋白结构数据库](#alphafold-蛋白结构数据库)
  - [CASP](#casp)
  - [AlphaFold 框架](#alphafold-框架)
    - [基本原理](#基本原理)
    - [AlphaFold 优点总结](#alphafold-优点总结)
    - [Recycling 的必要性](#recycling-的必要性)
    - [如何评估预测结果](#如何评估预测结果)
    - [AlphaFold 缺点](#alphafold-缺点)
    - [ColabFold 使用](#colabfold-使用)
    - [完整版使用](#完整版使用)
  - [使用](#使用)
    - [ColabFold 版本](#colabfold-版本)
    - [应用场景](#应用场景)
  - [硬件要求](#硬件要求)
  - [参考](#参考)

## AlphaFold 蛋白结构数据库

AlphaFold 是由 DeepMind 开发的一款人工智能系统，它可以根据蛋白质的氨基酸序列预测蛋白质的 3D 结构。实验表明，该方法具有较高的准确性。

DeepMind 和 EMBL-EBI 合作创建了 AlphaFold DB，从而将预测结果免费提供给科学界。第一版包含人蛋白质组合其它几个重要生物的蛋白质组。第二版增加了大部分人工注释的 UniProt 蛋白（Swiss-Prot），并计划在 2022 年扩大数据库，以涵盖目前所有的蛋白质（UniRef90 包含 1 亿多个）。

AlphaFold DB 目前提供下表所示的预测的蛋白结构数据库。

可以在蛋白对应页面下载单个蛋白的结构，例如 https://alphafold.ebi.ac.uk/entry/F4HVG8

也可以使用下表提供的链接下载整个物种的蛋白结构数据库。对所有物种的预测结构，可以在 FTP 站点下载：http://ftp.ebi.ac.uk/pub/databases/alphafold/

|Species|Common Name|Reference Proteome|Predicted Structures|Download|
|---|---|---|---|---|
|Arabidopsis thaliana|Arabidopsis|UP000006548|27,434|Download (3642 MB)|
|Caenorhabditis elegans|Nematode worm|UP000001940 |19,694|Download (2601 MB)|
|Candida albicans|C. albicans|UP000000559 |5,974|Download (965 MB)|
|Danio rerio|Zebrafish|UP000000437 |24,664|Download (4141 MB)|
|Dictyostelium discoideum|Dictyostelium|UP000002195 |12,622|Download (2150 MB)|
|Drosophila melanogaster|Fruit fly|UP000000803 |13,458|Download (2174 MB)|
|Escherichia coli|E. coli|UP000000625 |4,363|Download (448 MB)|
|Glycine max|Soybean|UP000008827 |55,799|Download (7142 MB)|
|Homo sapiens|Human|UP000005640 |23,391|Download (4784 MB)|
|Leishmania infantum|L. infantum|UP000008153 |7,924|Download (1481 MB)|
|Methanocaldococcus jannaschii|M. jannaschii|UP000000805 |1,773|Download (171 MB)|
|Mus musculus|Mouse|UP000000589 |21,615|Download (3547 MB)|
|Mycobacterium tuberculosis|M. tuberculosis|UP000001584 |3,988|Download (421 MB)|
|Oryza sativa|Asian rice|UP000059680 |43,649|Download (4416 MB)|
|Plasmodium falciparum|P. falciparum|UP000001450 |5,187|Download (1132 MB)|
|Rattus norvegicus|Rat|UP000002494 |21,272|Download (3404 MB)|
|Saccharomyces cerevisiae|Budding yeast|UP000002311 |6,040|Download (960 MB)|
|Schizosaccharomyces pombe|Fission yeast|UP000002485 |5,128|Download (776 MB)|
|Staphylococcus aureus|S. aureus|UP000008816 |2,888|Download (268 MB)|
|Trypanosoma cruzi|T. cruzi|UP000002296 |19,036|Download (2905 MB)|
|Zea mays|Maize|UP000007305 |39,299|Download (5014 MB|

## CASP

蛋白质结构预测的关键评估（Critical Assessment of protein Structure Prediction, CASP）旨在推进从蛋白序列预测蛋白质结构的方法。CASP 通过盲预测提供预测方法的客观测试。

![](images/2022-01-19-10-17-01.png)

CASP 比赛已进行 14 届，从1994年开始，每 2 年一次。第 15 届预计在 2022 年春开始。这些实验的完整数据可以在官网找到：https://www.predictioncenter.org/ 。

![](images/2022-01-17-16-23-34.png)

- 2014 (MSA): PSICOV, David Jones, UCL
- 2016 (Deel Learning/ResNet): RaptorX-Contact, Jinbo Xu, TTIC, Chicago
- 2020 (Transformer): AlphaFold2, DeepMind

## AlphaFold 框架

AlphaFold 骨架准确性中位数为 0.96 Å RMSD$_{95}$（95% 残基覆盖率下 $C_{\alpha}$ 的均方根偏差）（95% CI=0.85 Å - 1.16 Å）,而次优的方法骨架精度中位数为 2.8 Å RMSD$_{95}$（95% CI=2.7Å - 4.0Å）。

### 基本原理

![](images/2022-01-19-10-28-33.png)

![](images/2022-01-19-10-31-01.png)

![](images/2022-01-19-10-33-00.png)

![](images/2022-01-19-10-34-31.png)

![](images/2022-01-19-10-36-10.png)

![](images/2022-01-19-10-37-19.png)

![](images/2022-01-19-10-37-39.png)

![](images/2022-01-19-10-38-22.png)

![](images/2022-01-19-10-39-30.png)

![](images/2022-01-19-10-41-44.png)

![](images/2022-01-19-10-47-08.png)

### AlphaFold 优点总结

- **基于 recycling 的迭代优化**。这一点在很多领域已经得到过应用，比如计算机视觉中的姿态估计（post estimation）
- **广泛应用的 Attention 架构**。将二维的表横着做 Attention、再竖着做 Attention，对于图可以在局部做 Attention，不断精化了 Embedding 过程；Structure module 中也继续用到了 Attention
- **实现了端到端（end-to-end）架构**。完整建立了用于蛋白质结构预测的端到端架构，让模型能够在提升准确度的同时，融合结构的优化步骤
- **半监督学习扩展训练集（Self Distillation）**。用带标签的数据先训练一遍，再用无标签的数据预测一遍形成新的数据集，然后再混合继续训练。这种方法曾经在 Google Brain 的 noist student 使用过，在这里再次得到应用
- 类似 BERT 的 mask 结构。Mask 对各种输入添加噪音以增加模型的鲁棒性，这在 BERT 类模型中非常常见

![](images/2022-01-19-10-49-31.png)

![](images/2022-01-19-10-51-54.png)

![](images/2022-01-19-10-54-11.png)

![](images/2022-01-19-11-07-13.png)

### Recycling 的必要性

有的蛋白很快就能够折叠，有的蛋白很慢。

![](images/2022-01-19-11-15-19.png)

![](images/2022-01-19-11-16-02.png)

推荐默认使用三轮循环，如果三轮循环效果很差，此时可以考虑增加 Recycling。

![](images/2022-01-19-11-17-30.png)

![](images/2022-01-19-11-21-33.png)

![](images/2022-01-19-11-23-50.png)

![](images/2022-01-19-11-25-17.png)

![](images/2022-01-19-11-26-51.png)

![](images/2022-01-19-11-46-25.png)

![](images/2022-01-19-12-40-57.png)

### 如何评估预测结果

常用于评估 AlphaFold 建模精度的指标。

**pLDDT**：每个氨基酸的预测准确度：

- 低于 50，表示非常不准确或为无规则蛋白
- 低于 70，表示可信度低
- 高于 90，可信度极高

PAE：反应每对氨基酸距离与真实值的预测差值：

- 越低越好，单位为 Angstrom
- 在反应多 Domain 或 Complex 结构精度是效果很好
- 只有 pTM 模型和 Multimer 模型才有 PAE 打分。

![](images/2022-01-19-12-48-03.png)

![](images/2022-01-19-12-49-17.png)

![](images/2022-01-19-12-59-49.png)

不能用来预测 RBD|ACE2 的结合。

![](images/2022-01-19-13-01-58.png)

预测 S 蛋白，S 蛋白是同源三聚体，效果不好。

![](images/2022-01-19-13-03-58.png)

### AlphaFold 缺点

吃硬件：对于传统的计算生物学和生物信息学而言，一般的软件用一个普通的电脑即可跑通。而AlphaFold2 的部署，需要 “3TB储存空间、85GB内存、和 Navidia GPU”，这不是一个普通的电脑能带动的。

过于大的蛋白质或者蛋白质复合体，可能会跑不动。

对PDB数据存在一定程度上的过拟合：AlphaFold2是完全基于PDB数据库训练并测试，但是对于PDB没有的蛋白质（只能通过实验手段单独确定结构的蛋白质）泛化能力比较低

目前AlphaFold2只能预测静态解：实际上很多蛋白质的结构是高度动态的，而并非一个静态的稳定的结构。

AlphaFold 对超级复合物准确，但对膜蛋白的误差较大。

### ColabFold 使用

https://colab.research.google.com/github/deepmind/alphafold/blob/main/notebooks/AlphaFold.ipynb

使用 Colab 笔记本可以使用简化的 AlphaFold V2.1.0 版本预测蛋白质的结构。

与 AlphaFold V2.1.0 相比，这个 Colab 没有使用模板（同源结构）和 [BFD 数据库](https://bfd.mmseqs.com/)的选定部分。DeepMind 团队在最近的几千个 PDB 结构上验证了这些变化，大部分预测结果和 AlphaFold 几乎完全相同，但由于MSA 较小、缺乏模板，小部分的精度有很大下降。要获得最佳的结果，建议使用完全开源的 AlphaFold，或者 AlphaFold 蛋白质结构数据库 。

### 完整版使用

RTX2080ti 小一些蛋白跑起来还行，但序列长度到 500 就可能会挂，最好有 V100，A100 显存 10G 以上，多多益善。

如果没有 GPU，推荐使用 ColabFold。

## 使用

![](images/2022-01-19-13-04-53.png)

![](images/2022-01-19-13-05-48.png)

![](images/2022-01-19-13-07-13.png)

### ColabFold 版本

ColabFold 本身的优点：

- 使用方便，打开网页即可使用，不需要配置资源
- 支持很多功能：调整 recycling；选择是否需要模板，AMBER 优化；选择更快的序列比对算法 MMseq2；建模蛋白质异源复合物（hetero oligomer）；建模蛋白质多聚体（homo oligomer）
- Jupyter Notebook 形式，运行方便
- 优秀的可视化方法

ColabFold 的缺点：

- Colab 现在已经限制 GPU 资源，没有 GPU 不能运行 AlphaFold
- ColabFold 本身不支持高通量结构预测：MMseq2 在远程服务器运行，Colab 仍然使用串行流程

如果想使用 ColabFold，也可以试试本地版本的 ColabFold，能够使用更多的资源：

https://github.com/YoshitakaMo/localcolabfold

Mirdita,M. et al. (2021) ColabFold - Making protein folding accessible to all.

![](images/2022-01-19-13-09-04.png)



### 应用场景

![](images/2022-01-19-13-11-58.png)

![](images/2022-01-19-13-14-02.png)

![](images/2022-01-19-13-25-11.png)

## 硬件要求

参考：https://github.com/deepmind/alphafold

DeepMind 在 Google 云上的配置：

- 12 vCPUs, vCPU 即 virtual centralized processing unit，虚拟 CPU
- **85 GB** of RAM
- **100 GB** boot disk, 
- the databases on an additional **3 TB** disk
- 1 个 A100 GPU

NVIDIA A100：https://www.nvidia.cn/data-center/a100/

NVIDIA A100 Tensor Core GPU 可针对 AI、数据分析和 HPC 应用场景，在不同规模下实现出色的加速，有效助力全球高性能弹性数据中心。NVIDIA A100 由 NVIDIA Ampere 架构提供支持，提供 40GB 和 80GB 两种配置。作为 NVIDIA 数据中心平台的引擎，A100 的性能比上一代产品提升高达 20 倍，并可划分为七个 GPU 实例，以根据变化的需求进行动态调整。A100 80GB 将 GPU 内存增加了一倍，提供超快速的内存带宽（每秒超过 2TB），可处理超大模型和非常庞大的数据集。

价格：http://www.itsto.com/product/tesla_gpu.html

![](images/2022-01-14-16-23-05.png)

也有用 4 张 Tesla V100S 32GB 配置环境，单张价格：

![](images/2022-01-14-16-25-08.png)

> 玩不起，我不配。。。

## 参考

- https://alphafold.ebi.ac.uk/download
- https://www.predictioncenter.org/
- https://www.bilibili.com/video/BV1fm4y1D7Wz
