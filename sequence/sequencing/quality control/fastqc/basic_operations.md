# FastQC 基本操作

- [FastQC 基本操作](#fastqc-基本操作)
  - [打开序列文件](#打开序列文件)
  - [评估结果](#评估结果)

***

## 打开序列文件

在交互模式，选择 `File > Open` 打开一个或多个序列文件。

FastQC 支持以下格式文件：

- FastQ (所有编码变体)
- Casava FastaQ 文件
- Colorspace FastQ
- GZip compressed FastQ
- SAM
- BAM
- SAM/BAM Mapped only (normally used for colorspace data)

> **NOTE**
> Casava FastaQ 文件格式与常规 fastq 相同，只是将单个样本的数据拆分成多个文件。FastQC 会合并文件，为每个样本提供一个报告。此外，Casava FastaQ 会标记质量交叉的序列，在该模式 FastQC 会排除这些标记的序列。

FastQC 默认会根据输入文件名称猜测文件格式。以 .sam 或 .bam 记为的文件作为 sam/bam 文件打开，其它文件以 FastQ 格式处理。

## 评估结果

FastQC 的分析由一系列分析模块执行。
