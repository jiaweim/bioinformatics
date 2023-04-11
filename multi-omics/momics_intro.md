# 多组学概述

- [多组学概述](#多组学概述)
  - [简介](#简介)
  - [Genomics](#genomics)
    - [测序技术](#测序技术)
  - [Epigenomics](#epigenomics)
    - [表观基因组学方法](#表观基因组学方法)
  - [Transcriptomics](#transcriptomics)
    - [RNA-seq](#rna-seq)
  - [Proteomics](#proteomics)
  - [Multi-omics](#multi-omics)
    - [Genomics and proteomics](#genomics-and-proteomics)
    - [Transcriptomics and proteomics](#transcriptomics-and-proteomics)
  - [参考](#参考)

***

## 简介

多组学（multi-omics）被认为是提供现代个性化精准医疗的关键一步。与对个体基因组测序来检查疾病的基因组学不同，多组学需求同时、全面覆盖更多生物分子，包括表观遗传 markers、mRNAs、蛋白以及代谢物。通过测量和集成这些信息随着时间的变化，我们能以更详细和动态的方式检查疾病相关的分子机制，并得到新颖的、更具针对性的治疗方法。

DNA 包含遗传指令，当这些指令不对，通过基因组测序来分析这种差异显然很有价值。但是，如果指令是对的，只是无法访问它？或者可以访问，还是无法读取或解释？此时就需要多组学。

人类基因组大阅读包含 25000 个基因，每个基因通常编码一个蛋白来指定特定的生物学功能。然而，在给定时间，这些基因只有一部分表达，以确保细胞发挥应有的功能。

当一个基因被开启，它所持有的信息被转录为 mRNA，mRNA 充当载体将这些信息从细胞核运输到细胞质，然后通过细胞机器翻译成预期的蛋白质。如果指令存在错误（如 DNA 突变），这种错误通常会在蛋白质上得到体现，可能导致蛋白质的功能完全或部分小时，从而导致生物学缺陷。

然而，功能缺失的程度可能很难仅从基因组来判断。此外，即使 DNA 中没有突变，表达水平（基因被开启的程度）在决定健康或疾病方面同样重要。

多组学通过整合从 DNA 到生物功能的每一步的信息，分析细胞中更多种类的生物分子来探索这方面的内容。包括：

- 基因组（genome）：基因是否存在，以及是否正确编码
- 表观基因组（epigenome）：表示哪些基因更容易被表达
- 转录组（transcriptome）：揭示基因不同变体表达的程序
- 蛋白质组（proteome）：基因正确翻译成蛋白质的程度
- 代谢组（metabolome）：蛋白功能正确的程度

多组学具有在分子水平上提供更详细信息的潜力，使我们能够更好确定疾病的机制并做出更具针对性的医疗干预。从基础研究的角度来看，多组学能帮助更好了解调控网络和细胞信号通路如何运行，以及它们如何在疾病中变得功能失调，对于发现新的药物靶点至关重要。

更重要的是，多组学还提供了不同细胞和组织类型随时间变化的动态视图，不像基因组只能提供一个静态快照。这对于我们了解环境因素（如饮食、生活方式和年龄）与遗传因素相结合如何随着时间的推移对健康和疾病的影响非常重要。

与人类基因组计划一样，研究人员已经开始绘制一个参考 “人类多组”，旨在描述人一生 200 多种细胞类型的正常情况表观遗传状态、mRNA 水平、蛋白质以及代谢物水平。这显然比基因组测序复杂多了，也会产生更大的数据集。

已有少数个人多组学分析示例，但在准确性和规模上仍处于起步阶段，在实现可靠的参考人类多组之前，需要更广、更深度的研究。随着时间的推移，除了参考组之外，我们可以为每个人定期测量个人多组学数据，以便确定一些关键分子的基线水平以及与基线的偏差，从而提供早期疾病诊断。

这将是在 21 世纪提供预防性、个性化、精确医疗，以及带来的公共卫生和经济效益的关键。许多技术已经存在，但是与基因组学一样，临床应用的主要障碍是时间和成本。它们会随着技术的进步而减少，同样与基因组学一样，只要有政府支持，这可以大大加速。

## Genomics

基因组学研究基因组中编码信息的结构和功能，包括单核苷酸变体（Single Nucleotide Variants, SNVs）、插入、缺失、拷贝数变异（Copy Number Variations, CNVs）、重复、颠倒等。

### 测序技术

目前测序方法主要分为两类：short-read 和 long-read。

short-read 使用下一代测序（next-generation sequencing, NGS），又称为第二代大规模并行测序，Illumina 最流行。

long-read 测序，也称为第三代测序，使用 Oxford Nanopore Technologies and Pacific Biosciences 开发的技术。

short-read 的优势在于：速度、低沉本、可扩展、准确性更高。

long-read 的优势在于：基因组从头测序，isoform 全长测序。

## Epigenomics

表观基因组学研究 DNA 或 DNA 相关蛋白质的修饰，如 DNA 甲基化、染色质相互作用以及组蛋白修饰。DNA 的表观遗传调控可以决定细胞命运和功能，表观基因组可以根据环境而变化，更重要的是，这些 DNA 的变化可以传递。

这些变化可以作为癌症、代谢综合征、心血管疾病等的标志物。它们可以是组织特异性的、细胞特异性的，甚至可以是亚细胞结构特异性的，在健康和疾病状态都可以发生这种变化。

### 表观基因组学方法

- **甲基化测序（Methylation sequencing）**

胞嘧啶（C）甲基化影响基因表达和染色质重塑，可以从单核苷酸分辨率水平研究基因组的甲基化状态。

- **ChIP-seq**

染色质免疫沉淀测序（Chromatin immunoprecipitation sequencing, ChIP-seq）将免疫沉淀分析与测序相结合，以鉴定转录引起和其它蛋白质在全基因组水平与 DNA 的结合位点。

- **ATAC-seq**

通过测序分析转座酶可达染色质（Assay for transposase-accessible chromatin with sequencing, ATAC-seq）确定整个基因组染色质可达性。有助于揭示染色质组装和其它影响基因表达的因素。

- **HiC/3C/Capture-C**

分析染色质相互作用。Hi-C 扩展 3C-Seq 来绘制染色质接触全基因组，也被用于原位染色质相互作用的研究。Capture-C 通过磁珠捕获生物素片段。

## Transcriptomics

转录组学研究基因组产生的 RNA 转录本，以及这些转录本如何在调控过程中发生变化。它是基因型和表型之间的桥梁，是基因和蛋白质之间的纽带。

### RNA-seq

RNA-seq 是分析疾病状态、生物学过程等转录组的首选方法。RNA-seq 动态范围宽，对基因表达的变化非常敏感、测量准确，可用于各种物种。然而，测序平台和**读取深度**之间缺乏标准化，这可能会影响分析的可重复性。

全转录组分析捕获已知和新特征，使研究人员能够在更多的转录本中发现生物标志物，以更全面的了解感兴趣的**表型**。

## Proteomics

单纯从基因组无法获得最直观的信息，蛋白质包含更多内容。蛋白质组是高度动态的，可以根据内部和外部因素进行修饰，并且随着环境的变化，细胞也会生成不同的蛋白质。这也是为什么蛋白质组学被描述为蛋白质环境的快照。

## Multi-omics

### Genomics and proteomics

基因组和蛋白质组的结合，将基因型与表型直接联系起来，可以阐明生物学过程，帮助了解疾病机制，为开发新的治疗方法提供信息。

免疫细胞在人体内不断循环，在一个复杂而动态的网络中连接和通信。这种持续的通信对维持我们的免疫系统和抵抗疾病直观重要，但它还与自身免疫性疾病有关。

2022 年的一项研究^[Shilts, J.; Severin, Y.; Galaway, F.; Müller-Sienerth, N.; Chong, Z.-S.; Pritchard, S.; Teichmann, S.; Vento-Tormo, R.; Snijder, B.; Wright, G. J. A Physical Wiring Diagram for the Human Immune System. Nature 2022, 608 (7922), 397–404. https://doi.org/10.1038/s41586-022-05028-x.]，研究人员开发了一个相互作用组（interactome）图，通过将蛋白-蛋白相互作用数据与不同人体组织的单细胞基因组数据集成，详细描述了构成免疫系统的连接网络。这张图系统记录和描述了免疫系统的细胞内连接，从细胞-细胞到表面蛋白的生物物理特性。

### Transcriptomics and proteomics

转录组学和蛋白质组学的结合，有助于了解基因表达如何影响蛋白功能和表型。

2022 年发表的这篇文章^[Lee, T. A.; Han, H.; Polash, A.; Cho, S. K.; Lee, J. W.; Ra, E. A.; Lee, E.; Park, A.; Kang, S.; Choi, J. L.; Kim, J. H.; Lee, J. E.; Min, K.-W.; Yang, S. W.; Hafner, M.; Lee, I.; Yoon, J.-H.; Lee, S.; Park, B. The Nucleolus Is the Site for Inflammatory RNA Decay during Infection. Nat Commun 2022, 13 (1), 5203. https://doi.org/10.1038/s41467-022-32856-2.] 使用蛋白质组和转录组来证明核仁在感染期间调节促炎基因的 RNA 周转中所起的作用。

## 参考

- https://www.institute.global/insights/tech-and-digitalisation/beyond-human-genome-what-multi-omics
- https://frontlinegenomics.com/an-overview-of-omics-technologies-in-multi-omics/