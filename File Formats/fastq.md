# FASTQ

## 简介

FASTQ 是文本文件，其中包含通过 flow cell 上质控参数的簇 cluster 的测序数据。 对于每个通过质控参数的簇，一个序列被写入相应样本的 R1 FASTQ 文件，而对于双端测序运行，另外一个序列也被写入该样本的 R2 FASTQ 文件。 FASTQ文件中的每个条目包含4行：

序列标识符，其中包含有关测序运行和簇的信息；

序列（碱基信号； A，C，T，G和N）；

分隔符，只是一个加号（+）；

读取碱基的质量值。 这些是Phred +33编码的，使用ASCII字符表示数字质量值。

FASTQ文件中单个记录条目的示例：

```fastq
@SIM:1:FCX:1:15:6329:1045 1:N:0:2
TCGCACTCAACGCCCTGCATATGACAAGACAGAATC
+
<>;##=><9=AAAAAAAAAA9#:<#<;<<<????#=
```

## 参考

- https://help.basespace.illumina.com/files-used-by-basespace/fastq-files
- https://en.wikipedia.org/wiki/FASTQ_format
- https://knowledge.illumina.com/software/general/software-general-reference_material-list/000002211