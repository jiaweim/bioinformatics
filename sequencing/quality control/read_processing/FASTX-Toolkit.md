# FASTX-Toolkit

- [FASTX-Toolkit](#fastx-toolkit)
  - [简介](#简介)
  - [FASTX Trimmer](#fastx-trimmer)
  - [FASTX Clipper](#fastx-clipper)
  - [参考](#参考)

Last updated: 2023-03-29, 10:17
****

## 简介

在得到测序的质控报告后，需要根据报告对原始测序数据进行预处理，以便在后续序列比对中得到更可信的结果。

有许多短序列处理工具可供使用，包括 [FASTX-Toolkit](http://hannonlab.cshl.edu/fastx_toolkit/)[，Trimmomatic](https://github.com/usadellab/Trimmomatic), [SOAPnuke](https://github.com/BGI-flexlab/SOAPnuke), [fastp](https://github.com/OpenGene/fastp) 等，另外也有一些综合性更强的应用工具和平添，包括 Biopython 和 Galaxy。

FASTX-Toolkit 包含短序列 fasta/fastq 文件预处理的命令行工具集合，既可以网页上操作，也可以通过命令行运行。FASTX-Toolkit 预处理任务包括：

- FASTQ-to-FASTA
- FASTQ/A Collapser
- FASTQ/A Trimmer
- FASTQ/A Clipper
- FASTQ/A Reverse-Complement

其中 Trimmer 和 Clipper 这两个功能最常用。

## FASTX Trimmer

Trimmer 能够剪切质量不达标的序列，使序列更短小精悍。命令格式：

```bash
fastx_trimmer [-h] [-f N] [-l N] [-z] [-v] [-i INFILE] [-o OUTFILE]
```

参数说明：

- `-h`：显示帮助信息
- `-f N`：序列从第几个碱基开始保留，默认 1
- `-l N`：序列最后保留多少个碱基，默认整条序列全部保留
- `-z`：调用 gzip 软件，输出文件自动压缩
- `-i`：输入文件
- `-o`：输出文件

## FASTX Clipper

Clipper 主要用于过滤 reads 和去除 adapter：

```bash
fastx_clipper [-h] [-a ADAPTER] [-d] [-l N] [-n] [-c] [-C] [-o] [-v] [-z] [-i INFILE] [-o OUTFILE]
```

参数说明：

- `-h`: 获取帮助信息
- `-a ADAPTER`：接头序列信息
- `-n`：如果 reads 中有 N，保留 reads，默认不保留
- `-z`：调用 Gzip 软件，输出的文件自动压缩
- `-l N`：丢弃短于 N 的核酸序列，默认 5
- `-o`：输出路径
- `-v`：输出序列的数目
- `-d`: 输出 DEBUG 文件
- `-c`：只保留含有接头序列的 reads
- `-C`：只保留不含接头序列的 reads
- `-i INFILE`：输入文件
- `-o OUTFILE`：输出路径

## 参考

- http://hannonlab.cshl.edu/fastx_toolkit/