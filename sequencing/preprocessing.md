# 数据分析前的准备

## 简介

原始数据在分析前需要做一些准备工作：

- 测序数据的质控和过滤
- 将读段比对参考基因组
- 局部重比对
- 标记重复
- 碱基质量的重新评估

## FastQC

测序所得的原始数据不能直接用于研究分析。原始数据的测序质量偏低、基因组文库污染、原始数据重复片段过多等。因此需要对原始数据进行质量上的把控。

就以上功能，FastQC 最强大，它能为 fastq, bam, sam 格式文件提供精确有效的质量报告。

