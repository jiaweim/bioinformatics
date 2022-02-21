# 流感疫苗的生信分析

- [流感疫苗的生信分析](#流感疫苗的生信分析)
  - [简介](#简介)
  - [方法](#方法)
    - [IAV 毒株筛选](#iav-毒株筛选)
    - [NP，M1 和 HA 序列的系统发育分析](#npm1-和-ha-序列的系统发育分析)
    - [CTL 表位的鉴定和预测](#ctl-表位的鉴定和预测)
    - [CTL 表位的保护分析](#ctl-表位的保护分析)
  - [多表位疫苗序列](#多表位疫苗序列)
  - [TLR](#tlr)
  - [ImmSim](#immsim)
  - [参考](#参考)

2022-01-26, 15:14
***

## 简介

甲型流感病毒（Influenza A Virus, IAV）是一种高度传染性的病原体，其死亡率和发病率都很高。IAV 是单链 RNA 病毒，会导致急性传染性呼吸道疾病。2017 年 WHO 评估季节性流感可能会导致每年 29万-65万 人死亡，流感引发的呼吸系统疾病增加了全球的社会和经济负担。由于其聚合酶易错特性，IAV 高度易变、进化快速，对已有药物如 Amantadine (金刚烷胺)、Oseltamivir 和 Zanamivir 产生耐药性。更重要的是，流感病毒可以与 HA 基因重组，从而跨越物种屏障，产生新的流感毒株，大多数人对这种毒株缺乏免疫力。

接种疫苗是遏制 IAV 传播的最好方法。然而，由于缺乏有效预测流行毒株的方法，导致疫苗和流行病毒不匹配。例如，2009 年的 H1NI 大流行毒株，2013 年的 H7N9 大流行，都说明了病毒的不可预测性。迄今为止，FDA 批准的季节性疫苗包括三价灭活流感疫苗（IIVs），重组流感疫苗（RIV）和活病毒疫苗（LAIV）。尽管疫苗已经上市，但随着时间的推移，疫苗特异性抗体的减弱和流感病毒的抗原漂移，需要每年重新接种。目前可用的疫苗在所有年龄段对流感大流行和季节性毒株都无法完全保护。

根据流感病毒内部高度保守的基质蛋白 1（M1）、基质蛋白 2（M2）和核蛋白（NP），流感病毒可以分为 A, B, C, D 四类。根据血凝素（hemagglutinin, HA）和神经氨酸酶（neuraminidase, NA）表面糖蛋白的抗原性，IAV 可以可以进一步细分为各种亚型。HA 和 NA 表面蛋白是免疫接种引起的免疫应当的主要靶点，尤其是体液免疫。IAV 基质蛋白 M1 的胞外结构域是甲型流感的另一个重要疫苗靶点。然而，疫苗的生产周期长，导致在大流行期间无法获得。

与传统的减毒疫苗或灭活疫苗不同，亚单位疫苗缺乏传染性颗粒，因此比前者更安全。亚单位疫苗在各种抗疾病中使用日益增多，例如，Recombivax Hb 是一种乙型肝炎病毒表面抗原组成的重组亚单位疫苗，可用于预防所有已知乙型肝炎病毒亚型引起的感染。

最近，已出现几种提高流感疫苗的免疫圆形和有效性的方法。如计算优化光谱反应抗原（Computationally Optimized Broadly Reactive Antigen, COBRA）用于开发针对引发非人灵长类动物、小鼠和雪貂的多重 H5N1 亚型抗体反应。

这篇文章的思路是将不同抗原表位与 IAV 的保守表位结合起来，期望可能引起广泛的保护性免疫反应，从而开发通用流感疫苗。为了实现该目的，我们选择了三种 IAV 蛋白，即 HA, M1 和 NP 作为研制通用亚单位疫苗的候选。

- HA 是 IAV 的表面糖蛋白，是一个主要的抗原决定因素，其序列变异最大。
- M1 和 NP 是序列相对保守的多功能结构蛋白。

对纯化的病毒进行质谱分析显示，M1、NP 好 HA 分别有 2200, 530, 294 个拷贝，是病毒粒子中丰度最高的几种蛋白。此外，结构蛋白 NP 和 M1 是发展强交叉保护性 T 细胞发型的病毒特异性 CD8+ 细胞毒性 T 细胞（CTL）的靶点。

这里报告了一种高效构建重组亚单位疫苗的生信方法。为此，分析了 50 个 IAV 菌株的基因序列，包括 H1N1, H2N2, H3N2, H5N1 和 H7N9，这些菌株来自亚洲（印度、中国、东南亚）、非洲、澳大利亚、北美和南美 1918-2016 年的毒株。从选择的所有亚型中筛选合适的 CTL、辅助 T 淋巴细胞（HTL）和 B 淋巴细胞（BCL）表位。这些表位与两种佐剂和合适的连接剂一起构建了一个 79.5 kDa 的疫苗。季节性 H1N1 和 H3N2 流感病毒感染后诱导的 CTLs 已经会和 H5N1 亚型的 IAV 发生交叉反应，因此，这种疫苗结构可能引发针对不同亚型 IAV 的细胞介导的体液免疫反应，包括目前流行毒株和新进化的毒株。

## 方法

### IAV 毒株筛选

本研究选择的 50 个毒株包括四次 IAV 大流行（1918, 1957, 1968 和 2009）的代表性毒株，以及过去百年来自世界不同地区的季节性传播毒株。这些毒株属于 IAV 的 5 个亚型，即 H1N1、H2N2、H3N2、H5N1 和 H7N9。其中 H1N1、H2N2 和 H3N2 毒株已知在人类中引起广泛疾病，另两种亚型毒株对家禽具有高致病性，并在不同时期跨越物种屏障感染人类。从 NCBI 流感数据库中获得 50 株 IAV 的 HA、NP 和 M1 蛋白的氨基酸序列。

https://www.ncbi.nlm.nih.gov/genomes/FLU/Database/nph-select.cgi?go=database

除了 Brevig Mission 1918 H1N1 (Accession ID: AAD17218.1) 和 Guiyang 1957 H2N2 (Accession ID: ACD85231.1)（这两没有完整蛋白序列），其它蛋白都使用完整序列预测表位。

还分析了欧洲的不同亚型 IAV 毒株，(A/Bretagne/7608/2009 (H1N1)，A/Germany/2018/H3N2，A/Netherlands/56/1963 (H2N2))，由于使用它们预测的表位与来自亚洲的菌株预测的表位相似，因此没有纳入研究。

### NP，M1 和 HA 序列的系统发育分析

先使用 clustalΩ 对氨基酸序列进行多序列比对，然后使用 FastTree v.2 生成发育树（默认参数），其中采用基于 Jones-Taylor-Thornton (JTT) 替换模型的最大似然法和 1000 个 bootstrap 重复。

### CTL 表位的鉴定和预测

使用 NetCTL 1.2 server (https://services.healthtech.dtu.dk/service.php?NetCTL-1.2) 预测 HA, M1 和 NP 蛋白中的 CTL 表位。

对这三个蛋白质的所有 50 个菌株的氨基酸序列，以 FASTA 格式提交到 NetCTL 服务器。采用默认参数，为每种类型的蛋白质选择 4 个 MHC-I 类型（A1, A2, A3, B7）。据报道，这组 MHC-I 类涵盖了不同民族人口的 83.0-88.5%。

### CTL 表位的保护分析

使用 IEDB 保守分析工具（conservancy analysis tool）(http://tools.iedb.org/conservancy/ )分析 HA, M1 和 NP 蛋白序列的 CTL 表位在 50 个菌株中的保守性。以 M1 和 


## 多表位疫苗序列

对高打分的肽段序列，用 GPGPG 和 AAY 将这些潜在表位连接起来。


什么软件做分子对接？

晶体结构，

TLR3 的晶体结构 1ZIW.pdb

TLR8 的晶体结构 3W3G.pdb

MHC-I 的晶体结构 2X4O.pdb

MHC-II 的晶体结构 1T5W.pdb

## TLR

Arumugam,S. and Varamballi,P. (2021) In-silico design of envelope based multi-epitope vaccine candidate against Kyasanur forest disease virus. Sci Rep, 11, 17118.

TLR 在病毒感染后的固有免疫应当中发挥重要作用，特别是 TLR2 被报道用来识别病毒包膜蛋白。

TLR2 的 PDB ID：2Z7X 作为目标蛋白。

ClusPro 2.0 server 和 PatchDock 用于对接。

## ImmSim

**HLA 选择**

A0201
A0101

B0702
B0801

DRB10701
DRB11501

Simulation Vlume:

Inject time step: 9,93,177


## 参考

- Sharma,S. et al. (2021) Immunoinformatics approach for a novel multi-epitope subunit vaccine design against various subtypes of Influenza A virus. Immunobiology, 226, 152053.
