# Trimmomatic

- [Trimmomatic](#trimmomatic)
  - [简介](#简介)
  - [使用](#使用)
  - [参考](#参考)

***

## 简介

Trimmomatic 是一个功能强大的测序原始数据过滤软件，由于与 Illumina 公司各平台产出的高通量测序数据具有较高的适配度，故被广泛使用。和 FASTX-Toolkit 类似，Trimmomatic 也可以实现接头序列去除，低质量 reads 过滤，reads 低质量未端裁切等操作，同时支持对单端测序数据和双端测序数据的处理。

## 使用

使用（以双端测序数据为例）：

```bash
$ java [-jar path to trimmomatic.jar] [PE] [-threads threads] [-phred33/-phred64]
    [-trimlog logFile] <input 1> <input 2> 
    <paired output 1> <unpaired output 1>
    <paired output 2> <unpaired output 2>
    [stepl] [step2] ...[stepN]
```

参数说明：

- `[-jar path to trimmomatic.jar]`: trimmomatic.jar 主程序路径
- `[PE]`:PE 为双端测序,若单端测序则为 SE。
- `[-threads threads]`:程序运行使用的线程数。
- [-phred33/-phred64]: fastq 文件的质量分数编码方式，若不设置这个参数，则软件会自行判断。
- `input 1><input 2>`:双端测序的两个 fastq 输人文件。
- `<paired output 1> < unpaired output 1 > < paired output 2 > < unpairedoutput 2>`：四个输出文件，包括含有双端匹配 reads 的两个输出文件和含有未能双端匹配 reads 的两个输出文件。
- `[stepl] [step2]···[stepN]`:一些过滤操作，常用参数如下:
  - [ILLUMINACLIP: fastaWithAdaptersEtc: seed mismatches: palindrome clipthreshold: simple clip threshold: minAdapterLength: keepBothReads]: 去除 reads 中的接头序列或者其他在 Ilumina 测序中引人的特异性序列。其中 `fastaWithAdaptersEtc` 为包含接头序列的文件路径。
  - [SLIDINGWINDOW: WindowSize: requiredQuality]: 应用滑窗策略对 reads 的质量值进行计算，并在质量值低于值时对 reads 进行切。其中 `WindowSize` 为窗口大小，`requiredQuality` 为窗口碱基平均质量阈值。
  - [LEADING:quality]: reads 起始端低质量碱基裁切数目。`quality` 为碱基质量值阙值。
  - [TRAILING:quality]: reads 末尾端低质量碱基裁切数目。`quality` 为碱基质量值阈值。
  - [CROP:length]:不考虑碱基质量，从 reads 的起始开始保留设定长度的碱基，其余全部切除。length 为 reads 从末尾端裁切之后保留下来的长度。
  - [HEADCROP:length]:不考虑碱基质量，从 reads 的末尾开始保留设定长度的碱基，其余全部切除。length 为 reads 从起始端裁切之后保留的长度。
  - [MINLEN:length]：最短 reads 长度，若 reads 经过前面的过滤步骤保留下来的长度低于这个阈值，则 reads 被整条丢弃。length 为最短 reads 长度。

## 参考

- https://github.com/usadellab/Trimmomatic