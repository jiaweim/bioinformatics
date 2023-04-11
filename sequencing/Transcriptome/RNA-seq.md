# RNA 测序（RNA-Seq）

- [RNA 测序（RNA-Seq）](#rna-测序rna-seq)
  - [转录组测序的目的和数据特点](#转录组测序的目的和数据特点)
    - [转录组测序的目的](#转录组测序的目的)
    - [转录组测序数据的特点](#转录组测序数据的特点)
  - [转录组测序的工作流程](#转录组测序的工作流程)
    - [实验设计](#实验设计)
    - [RNA 完整性检查](#rna-完整性检查)
    - [RNA 的提取和 cDNA 文库的构建](#rna-的提取和-cdna-文库的构建)
    - [CDNA 测序](#cdna-测序)
    - [测序数据质量控制](#测序数据质量控制)
    - [序列回帖/组装](#序列回帖组装)
    - [基因表达水平的量化](#基因表达水平的量化)
      - [RPKM](#rpkm)
      - [FPKM](#fpkm)
      - [TPM](#tpm)
    - [差异表达分析](#差异表达分析)
      - [单样本中 reads 产生的过程](#单样本中-reads-产生的过程)
      - [基于负二项分布的差异表达分析](#基于负二项分布的差异表达分析)

***

## 转录组测序的目的和数据特点

转录组是特定的细胞、细胞类型或者组织在特定条件下所产生的全部 mRNA 和非编码 RNA 的总体。

转录组学在组学水平上研究细胞中基因的表达和调控规律，即在 DNA 水平上对基因的表达情况进行研究。转录组研究能够揭示转录本可变剪切、转录后修饰及基因融合，能够检测核苷酸水平的突变、基因的差异表达等。

单细胞转录组技术是在单个细胞水平上对转录组进行高通量测序分析的技术。

### 转录组测序的目的

转录组测序的功能：

- 不同条件下，基因表达可能存在差异，利用 RNA-Seq 技术可以检测哪些基因对外部条件的变化敏感。例如，通过在给药组和对照组中检测基因表达水平并进行差异化分析来鉴定哪些基因具有显著的药物敏感性，可为相关疾病的机制研究和药物靶点的研发提供数据支持。
- RNA-Seq 可以在全基因组水平检测基因的表达，可用于发现新的转录本和可变剪切等。有些基因的分子特征只能在很低的水平上观测到，而 RNA-Seq 对低水平基因具有更高的敏感性。
- RNA-Seq 测序还可以挖掘 RNA 层面上影响蛋白质序列的变异。

### 转录组测序数据的特点

特点：

- 首先，基因的编码区由外显子和内含子组成，部分较短的外显子可能会被较大的内含子分开，转录组 reads 回帖的算法需要考虑此类因素。
- 其次，不同细胞组织中的 RNA 分布变化很大，通常在 $10^5$ 到 $10^7$ 数量级；而且全部 reads 中高表达的基因占比可能较大；来自线粒体的基因也会产生转录本。
- 另外，相比于双链 DNA，单链 RNA 极易降解，因此对实验操作的要求也相对较高。
- 最后，RNA-Seq 数据也会出现重复 reads，是由于PCR 放大还是真的来自高表达基因，还需要分辨。

因此，针对转录组测序数据的特点，需要开发专门的比对回帖、基因定性和定量分析的算法和工具。

## 转录组测序的工作流程

RNA-Seq 测序的工作流程可分为生化和生物信息分析两部分：

- RNA-Seq 生化流程包括 RNA 分离、转换成短的 cDNA、在每个 cDNA 上加上测序接头，然后建库测序。
- 生物信息分析主要包括 reads 回帖、每个基因表达量的计算、表达量的正则化、差异基因表达分析、基因功能富集分析和其他下游分析等。

### 实验设计

根据实验目的和样本特征设计实验方案，包括：

- RNA 的提取方法
- 测序平台
- RNA质量评估
- 是否需要单独提取 mRNA
- 是否涉及重复实验
- 采用单端测序还是双端测序

### RNA 完整性检查

RNA 样本的总量与样本的完整性是评价样品质量的关键。RNA 的完整性由 **RIN**（RNA Integrity Number）表示，数值范围从 1 到 10：

- 1 表示 RNA 降解严重，样本中 mRNA 的量已经偏离真实;

RIN 值通过电泳图上 28S 和 18S rRNA 的条带比 (28S/18S) 来估算。对用于测序的样本，建议其 RIN 不小于 7。

### RNA 的提取和 cDNA 文库的构建

利用 RNA 分子的长度，可以将 miRNA 分子分离并富集(聚丙烯酷胺凝胶电泳 PAGE技术)。mRNA 通常利用其 polyA 序列进行捕获和富集。RNA 分离和富集后，转化为 cDNA，制备 cDNA 测序文库。

文库是包含特定待测序的所有序列的集合。文库制备首先将待测序的样本片段化，然后再将这些片段化后的短序列的双端加上接头，从而将所有待测序序列制备成内部序列不同但拥有相同接头的集合。然后进行序列簇的生成，通过桥式 PCR 的方式，将相似的序列聚集在一起形成序列簇，用于测序。

### CDNA 测序

在体系中加人包含有特定荧光标记的 dNTP，dNTP 包含一个叠氮基团，当延伸遇到叠氮基团时停止，同时根据荧光颜色读取正在合成的核酸。不断重复以上步骤，最终得到序列的碱基排列信息。

### 测序数据质量控制

样品制备、文库制备和测序过程通常会存在诸多偏差。通过质量控制可以部分消除这些偏差的影响。最常使用的工具为 FastQC。

### 序列回帖/组装

按照是否有参考序列，转录组测序后可进行序列的回帖或组装。

- 有参考基因组时，将序列回帖到参考基因组或转录组，获得不同已知转录本的表达水平。
- 无参考基因组时，先将序列组装为长序列，然后将这个组装好的长序列作为参考序列，将 reads 与之回帖并进行定量分析。

有参与无参的区别在于转录和表达水平的定量是同时完成还是依次完成的。

### 基因表达水平的量化

基因表达量可以用回帖到该基因的 reads 的计数 (counts)来表示。回帖到一个基因上的 reads 计数与三个因素有关：

1. 基因的长度，原则上，基因的外显子越长，来自这个基因的 reads 数目越多；
2. reads 的总数，不同的测序深度下，回帖到转录组的 reads 总数不一样；
3. 基因的转录速率(表达量、mRNA 的丰度)，在总 reads 数目和基因长度致的情况下，高表达基因会有更多的 reads 计数。

因此，用 reads 计数来定量表示基因表达量，需要校正基因长度和 reads 总数的信息。目前有三种表示方法，分别是 RPKM、FPKM 和 TPM。

#### RPKM

RPKM 为 Reads Per Kilobase per Million 的缩写，意为每百万 reads，回帖到外显子每千碱基长度的 reads 个数，其定义为：

$$RPKM=\frac{C}{(L/10^3)(N/10^6)}$$

其中：

- C 为回帖到该基因外显子上的 reads 总数;
- L 为该基因外显子长度(kb);
- N 为所有回帖到转录组的 reads 总数 (Million)。

#### FPKM

FPKM 为 Fragments Per Kilobase of exon model per Million mapped fragments 的缩写，即每百万 reads，回帖到外显子每千碱基长度的片段数目，定义如下：

$$FPKM=\frac{C}{(L/10^3)(N/10^6)}$$

其中：

- C 为回帖到该基因外显子的片段总数
- L 表示该基因外显子长度(kb); 
- N 为回帖到转录组的片段总数 (Million)。

对于 single-end 测序数据，FPKM 和 RPKM 的结果一致。在 paired-end 测序数目中，FPKM 计算的是回帖到基因的 reads 对数。

#### TPM

TPM 即 Transcripts Per Million。TPM 的计算分三步: 

1. 用回帖到每个基因的 reads 数除以该基因的长度，即得到每千碱基的 reads 数(Reads PerKilobase,RPK);
2. 把一个样本中所有的 RPK 值加起来,除以 10,得到缩放系数(permillion scaling factor);
3. 用每个基因的 RPK 值除以上一步的缩放系数,得到 TPM。

$$RPK=\frac{readsmappedtogene\times 10^3}{genelength(basepair)}$$

$$TPM=RPK\times\frac{1}{\sum(RPK)}\times 10^6$$

用TPM表示表达量时,每个样本中所有 TPM 的总和相同,使得比较每个样本中对应基因的 reads 的比例更合理。相比之下，RPKM 和 FPKM 的每个样本标准化后的 reads 的总和可能不同，导致不同样本之间表达量的直接比较可能会有偏差。

### 差异表达分析

#### 单样本中 reads 产生的过程

来自 RNA-Seq 的 Read 计数 (read counts) 可用一个采样过程来描述。假设 $\mu_i$ 表示基因 i 的真实表达量，该基因长度为 $L_i$，那么，一个 read 来自基因 i 的概率 $p_i$ 为：

$$p_i=\mu_i L_i/\sum_{i=1}^G \mu_i L_i$$

其中 G 表示所有基因。

如果总的 reads 数为 N，$Y_i$ 表示来自基因 i 的 read 计数，则可假设 $Y_i$ 服从泊松分布，即：

$$Y_i | \lambda_i \text{\textasciitilde} Poisson(\lambda_i)$$

其中，$\lambda_i=Np_i$。

#### 基于负二项分布的差异表达分析

假设样本 j 中，来自基因 i 的 read 个数为 $K_{ij}$，$K_{ij}$ 服从负二项分布（NB）：

$$K_{ij} \text{\textasciitilde} NB(\mu_{ij},\sigma_{ij}^2)$$

$$$$

，中,来自基因;的 red计数为K;，K服从负二项分布(NB),即式(8-,(8-8)。
Kj~NB(uij，号)Pr(Ky=k)=(ktr-l)p*(1-p)
81
(88)
Pr 为基因i在;样本中,有k个 read计数的概率。
负二项分布比泊松分布更适合用来刻画 read 计数的分布。在泊松分布中,其方差和值相等,即基因表达水平在样本间的变异程度随均值线性变化。在实际处理 RNA-Seq的read计数的分布时发现,一个基因 read 计数值在各样本间的方差，比其均值具有更快的变化率,即具有分散性特征。
假设有A 和B 两类样本,基因i在A 类样本中的 read 计数为 KA，在 B样本中read计数为 KB,Kis 为基因在两类样本中 read 计数之和,见式(8-9)。