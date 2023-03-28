# FastQC

## 简介

FastQC 用于检查高通量测序数据集的质量。它对 fastq, bam 或 sam 格式的原始序列文件运行一组分析，生成一个总结报告。

FastQC 的主要功能：

- 读取 BAM、SAM 和 FastQ 文件
- 提供一个快速概览，说明数据哪些地方可能有问题
- 数据的图形和表格摘要
- 将结果导出为 HTML 格式
- 脱机操作，在不运行交互式程序的情况下自动生成报告

## 安装

```bash
# 下载
$ wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.12.1.zip
# 解压
$ unzip fastqc_v0.12.1.zip
$ cd FastQC/
# 修改权限
$ chmod 755 fastqc


```

## 参考

- https://github.com/s-andrews/FastQC
- https://www.bioinformatics.babraham.ac.uk/projects/fastqc/
