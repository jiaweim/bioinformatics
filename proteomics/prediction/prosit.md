# Prosit

- [Prosit](#prosit)
  - [方法](#方法)
    - [合成肽段](#合成肽段)
      - [Generation](#generation)
      - [Data acquisition](#data-acquisition)
    - [统计](#统计)
    - [碎裂模型](#碎裂模型)
    - [保留时间模型](#保留时间模型)
    - [外部数据处理](#外部数据处理)
    - [DIA 数据分析](#dia-数据分析)
    - [Metaproteomics](#metaproteomics)

2022-02-07, 15:27
***

## 方法

### 合成肽段

#### Generation

为了实现对人类蛋白质组的广泛覆盖，创建并使用了 4 组肽段集：

1. Isoform 肽段集，对 Swiss-Prot 注释的所有 isoform 生成 7-30 长度的特有肽段（和标准形式的差异肽段），该肽段集包含 **123,514** 条肽段，覆盖 9,354 个 isoforms；
2. Missing gene addon 肽段集，包含 53,683 条肽段（7-30 个残基）；
3. 29,141 肽段集（7-40 个残基），在串联质量标签中经常鉴定到的肽段，不过在本研究中没有进行标记；
4. 重新合成了 12,760 条肽段，这些肽段包含在 proteotypic 肽段集中，但是在 LC-MS/MS 中没检测到。

所有肽段序列和对应的蛋白在 [STable 1](D:\repo\prosit\STable-1.xlsx) 中。

制备过程大致为，合成的肽库每个大约包含 1,000 条肽段。质量接近的肽段（± 10 p.p.m）尽可能分散到长度相近的不同肽段池中。所有的肽段都是在纤维素膜上使用基于 Fmoc 的固相合成策略合成。在预先设计的 1000 个肽库中，将粗肽从膜上分离出来，干燥。

将干燥的肽段在室温下涡旋 30min 溶于 100% 二甲亚砜（DMSO）至 10 pmol/µl。然后使用 1% 甲酸（HPLC 级水）将 DMSO 稀释到 10%，这样肽段浓度为 1 pmol/µl，储存在 -20 °C 备用。

#### Data acquisition

将 10 µl 肽库原液转移到 96 孔板，每针加入 100 fmol 两种保留时间标准试剂（Pierce RT 标准和 PROCAL）。使用装备 C18 色谱柱的 Dionex 3000 高效液相色谱系统（Thermo Fisher Scientific）对肽段池中的每种肽段进行分析，每种肽段进样量估摸在 200 fmol。分离系统包括 75µmx2cm 的 trap 柱（填充 5µm 的 Reprosil Pur ODS-3）和 75µmx40cm 的分析柱（填充 3µm 的 C18 Reprosil Gold 120）。

使用 Orbitrap Fusion Lumos 质谱分析。每个肽段池用首先用下面两种碎裂方法：

- HCD（NCE 28，FTMS）
- CID（NCE 35，ITMS）

对以上鉴定中的全长肽段，附加三种碎裂方法：

- 3xHCD (NCE 25,30,35)
- 2xIT_2xHCD (CID NCE 35 ITMS, HCD NCE 28 ITMS, HCD NCE 20 FTMS, HCD NCE 23 FTMS)
- EtciD NCE 35 FTMS, EthcD NCE 28 FTMS

获得的 RAW 文件用 MaxQuant v1.5.3.30 对 pool-specific 数据库检索（STable 1）。如果没有额外说明，搜库参数为：Cys 上carbamidomethylated 固定修饰，可变修饰 methionine oxidation。first search tolerance 20 ppm, main search tolerance 4.5 ppm, PSM 和 protein FDR 设置为 1%。

合成肽段谱图：https://www.ebi.ac.uk/pride/archive/projects/PXD010595

### 统计

**谱图相似度计算**

使用所有理论上可能的碎片离子强度计算谱图相似度，忽略 m/z 维度。

对两个肽段 $S_a$ 和 $S_b$，长度分别为 $n_a$ 和 $n_b$，母离子电荷为 $z_a$ 和 $z_b$，由向量 $V_a$ 和 $V_b$ 表示。向量 $V_a$ 和 $V_b$ 长度相同，包含 $S_a$ 和 $S_b$ 中所有的 b, y 离子强度，对应长度为 $max(n_a, n_b)-1$，碎片离子价态最大为 $min(max(z_a, z_b), 3)$。碎片例子强度以 base-peak 归一化，未观测或预测到的强度设置为 0。

例如，当 $S_a=PEPTIDE, z_a=2$, $S_b=PPTD, z_b=3$，则有 $n_a=7$, $n_b=4$, $V_a$ 和 $V_b$ 的长度均为 18 ($(7-1)\times 3$)。

对所有实验谱图和预测谱图构建该向量，并使用该向量计算相似度。计算方法如下：

L2 norm 定义：

$$\lvert V\rvert_2 = \sqrt{\sum_{i=0}^n \lvert V_i \rvert^2}$$

平均偏差定义：

$$\tilde{V}=V-\frac{1}{n}\sum_{i=0}^n V_i$$

L2 normed vector:

$$\hat{V}=\frac{V}{\lvert V\rvert _2}$$

使用 `scipy.stats.pearsonr` 实现的 Pearson correlation (R)，其定义如下：

$$R(V_a, V_b)=\frac{\tilde{V}_a\cdot\tilde{V}_b}{\lvert \tilde{V}_a \rvert _2 \cdot \lvert \tilde{V}_b \rvert _2}$$

### 碎裂模型

**模型结构**

peptide encoder 包含三层，如下图所示：

![](images/2022-02-10-15-39-28.png)



### 保留时间模型

### 外部数据处理

### DIA 数据分析

### Metaproteomics

