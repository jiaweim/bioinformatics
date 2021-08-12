# MHC 预测数据集

- [MHC 预测数据集](#mhc-预测数据集)
  - [数据集](#数据集)
    - [KD](#kd)
    - [IC50](#ic50)
    - [EC50](#ec50)
    - [t1/2](#t12)
    - [binary](#binary)
  - [MHC-I](#mhc-i)
    - [HLA质谱数据集](#hla质谱数据集)
    - [Kim 数据集](#kim-数据集)
    - [SysteMHC 数据集](#systemhc-数据集)
    - [Sarkizova 数据集](#sarkizova-数据集)
    - [NetMHC-3.0](#netmhc-30)
    - [NetMHCpan-3.0](#netmhcpan-30)
    - [基准测试](#基准测试)

2021-06-02, 13:18
***

## 数据集

结合亲和力是生物分子与其配体（如药物、抑制剂）之间结合力的强度。结合力通常通过平衡解离常数（K）来表示。K值
越小，亲和力越大；K值越大，生物分子与其配体就越难结合。

### KD

thermodynamic constant.

### IC50

Inhibitory concentration to outcompete 50% of a high affinity reference ligand, can approximate KD.
半抑制浓度，或称半 抑制率，即 IC50.

### EC50

concentration needed to half-saturate the receptor, approximates KD.

### t1/2

half-life of binding

### binary

peptides solely classified as positive or negative for binding based on some threshold that is consistent with the curated reference.

## MHC-I

### HLA质谱数据集

Abelin, J. G. et al. Mass Spectrometry Profiling of HLA-Associated Peptidomes in Mono-allelic Cells Enables More Accurate Epitope Prediction. Immunity 46, 315–326 (2017).

Immunity 影响因子 31，医学顶刊。

人类白细胞抗原（Human leukocyte antigen, HLA）I 类糖蛋白 HLA-A, -B 和 -C 在人体类几乎所有核细胞的表面表达，是呈递肽段给 T 细胞受体检测的必要蛋白。HLA 基因是人类最具多态性的基因，迄今为止，已经鉴定到超过 10,000 个 HLA-I 类等位基因变异。据估计，每个 HLA 等位基因结合并呈递给 T 细胞的 unique 多肽大约有 ~1,000-10,000 条，而人类蛋白编码基因编码大概 1,000 万 9-mer 肽段。鉴于 HLA 结合多样性，准确预测一个肽段是否能与特定 HLA 等位基因结合非常具有挑战性。

通过对 HLA 部分等位基因的研究，肽段与 HLA 分子结合的规则已经被广泛研究，并已经被基于神经网络的现代算法编码。然而，目前使用的主流算法几乎完全使用合成肽段生化亲和力数据来训练的。这带来几个问题。首先，生化亲和力测试实验的通量有限，因为只有非常小比例的肽段会结合，因此要找到 10 条结合力强的肽段，可能要合成至少 1000 条肽段。偏差抽样可以提高概率，但是也会导致结果带有偏差或缺失 subdominant motifs。与此同时，其它无意识形式的偏差，如长度分布的概念，或对肽段合成或溶解性的限制，很难避免。最重要的是，这些方法并不一定考虑与 HLA 结合之前肽段的加工和运输过程。

基于质谱的方法可以对肽段加工和呈递进行相对公正的表征，理论上可以解决上述大部分问题。然而，以往的 LC-MS/MS 方法需要大量的细胞样本，从而限制了通量，而且数据的多等位基因特性使得 motif 学习更为复杂。

在这篇文章里，开发了一个集实验和计算为一体的 HLA 相关内源肽 LC-MS/MS 分析流程，只需要很少的细胞量，提供单等位基因分辨率。

目前唯一可用的单等位基因方法是基于从生物反应器中培养的细胞系中分离可溶性 HLA，这个过程不容易实现，需要几个数据集的输入材料。而该方法从表达单一 HLA 等位基因的细胞中分离多肽，以提高算法对 HLA-I 呈递肽段的预测能力。

### Kim 数据集

Kim, Y. et al. Dataset size and composition impact the reliability of performance benchmarks for peptide-MHC binding predictions. BMC Bioinformatics 15, 241 (2014).

主要组织相容性复合体（Major Histocompatibility Complex, MHC）分子属于免疫系统用来识别外来抗原（如病原体）的蛋白质家族。在人类中，MHCs 被称为人类白细胞抗原（human leukocyte antigen, HLA）。MHC 分子附着在细胞表面，将细胞内源或外源的肽段呈递给 T 细胞识别，触发细胞杀伤或下游信号事件。因此，多肽与MHC分子结合是 T 细胞识别的必要条件。因此，准确预测肽段-MHC 结合力对自身免疫疾病、过敏和癌症的治疗和诊断都有着重要作用。

由于多肽-MHC 结合力在确定 T 细胞表位中的重要性，人们花费了大量精力收集实验测量的结合亲和力数据，并将它们提供给科学界。随着数据的积累，出现了许多MHC-I 结合肽段预测工具。为了比较它们的预测性能，进行了许多大规模的基准测试分析。对 MHC-I 预测，已有算法达到交叉验证的平均 AROC （area under receiver operating characteristic curves）达到 0.9，具有很高的预测性能，表明预测方法已经相对成熟。

尽管预测多肽-MHC 结合力的方法取得了很大进展，仍然存在一些重要问题。首先，交叉验证的预测性能是对真实应用的估计，这些估计的准确性有待确认。其次，序列相似性对这些估计的准确性影响有多大，训练数据集和测试数据集中间存在的相似肽段是否会导致估计的预测性能过大？第三，是否有其它因素引起盲验证和交叉验证性能之间的偏差？

为了更好地理解影响交叉验证预测性能准确性的因素，准备了如下三个数据集。

- 

### SysteMHC 数据集

Shao, W. et al. The SysteMHC Atlas project. Nucleic Acids Research 46, D1237–D1247 (2018).



### Sarkizova 数据集

Sarkizova, S. et al. A large peptidome dataset improves HLA class I epitope prediction across most of the human population. Nat Biotechnol 38, 199–209 (2020).

HLA 抗原表位的预测对肿瘤免疫治疗和疫苗的研发具有重要意义。然而，目前预测算法的预测能力有限，部分原因是它们缺乏广泛覆盖 HLA 等位基因的高质量表位数据集。为了对大部分人群都能预测 HLA-I 相关内源肽，该研究使用质谱鉴定到从 HLA-A, -B, -C 和 -G 等单等位基因细胞系中分离出的 >185,000 条肽段。

HLA 基因是人类多态性最高的基因，目前已超过 16,200 不同的 HLA-I 等位基因。和 HLA-I 分子结合的短肽段（长度 8-11）由细胞内蛋白产生，这些蛋白质首先被蛋白酶体（proteasome）和肽酶（peptidase）依次酶切，然后由细胞表面 HLA-I 蛋白呈递给细胞毒性 T 细胞。

考虑到 HLA 结合偏好，能够准确预测一个肽段是否由特定的 HLA 等位基因呈递是一个重要问题。预测肽段和 HLA 等位基因，特别是 HLA-A 和 HLA-B 等位基因结合力的计算模型的准确性一直在提高。在癌症领域，这些工具越来越多地与下一代肿瘤 DNA 测序结合使用，以识别由肿瘤特异性体细胞突变产生的免疫原性肿瘤新生抗原。因此，这些工具加速了表位发现过程，使得我们可以集中研究与 MHC-I 具有强烈结合力的表位上。然而，即使目前使用最广泛的算法 NetMHCpan，一旦预测的亲和结合力降低（半最大抑制浓度 > 100nM），表位预测的假阳性率会迅速增加。另外，这些算法均预测肽段和单个 HLA 分子的结合力（抗原呈递的最后一步），没有考虑细胞内肽段前提的可用性，或者说它们被蛋白酶处理的过程。最后，由于之前的研究主要集中在高加索（Caucasian）人群高度表达的少数等位基因上，现有算法在预测高加索人群不常见的等位基因以及其它人群的表位准确性较低。

使用 LC-MS/MS 检测和测序 HLA 结合多肽具有独特优势，可以直接获取细胞内源性加工和呈递的肽段信息。有研究表明，使用细胞工程技术使细胞只表达单个 HLA 等位基因，从中分离出的HLA 结合肽段可以揭示等位基因特异性的肽段 motif，并可用于训练内源性等位基因特异性的肽段呈递预测。这篇文章对数据集进行扩展，从 >24,000 肽段扩展到 16 个细胞系 95 个等位基因的186,464 条洗脱肽段。该数据集使我们可以比较 HLA-I 等位基因对肽段长度的偏好，揭示内源性 HLA 配体的多样性和复杂性。



### NetMHC-3.0

Lundegaard, Claus, Kasper Lamberth, Mikkel Harndahl, Søren Buus, Ole Lund, and Morten Nielsen. “NetMHC-3.0: Accurate Web Accessible Predictions of Human, Mouse and Monkey MHC Class I Affinities for Peptides of Length 8–11.” _Nucleic Acids Research_ 36, no. suppl_2 (July 1, 2008): W509–12. [https://doi.org/10.1093/nar/gkn202](https://doi.org/10.1093/nar/gkn202).

### NetMHCpan-3.0

### 基准测试

Trolle, Thomas, Imir G. Metushi, Jason A. Greenbaum, Yohan Kim, John Sidney, Ole Lund, Alessandro Sette, Bjoern Peters, and Morten Nielsen. “Automated Benchmarking of Peptide-MHC Class I Binding Predictions.” _Bioinformatics_ 31, no. 13 (July 1, 2015): 2174–81. [https://doi.org/10.1093/bioinformatics/btv123](https://doi.org/10.1093/bioinformatics/btv123).
细胞毒性 T 淋巴细胞（cytotoxic T-cell lymphocytes, CTLs）在
