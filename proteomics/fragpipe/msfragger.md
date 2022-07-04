# MSFragger

- [MSFragger](#msfragger)
  - [简介](#简介)
  - [使用要求](#使用要求)
    - [输入文件](#输入文件)
    - [硬件](#硬件)
    - [软件](#软件)
  - [安装](#安装)
  - [参数设置](#参数设置)
  - [运行 MSFragger](#运行-msfragger)
  - [参考](#参考)

## 简介

MSFragger 是一个超快数据库检索工具，用于基于质谱的蛋白质组学肽段鉴定。MSFragger 的速度使其特别适合分析大型数据集（包括 timsTOF 数据），用于无酶约束检索，以及开放检索。

使用 MSFragger 的方式有三种：

1. 在 FragPipe 中使用
2. 在 ProteomeDiscoverer 中使用
3. 作为单独的 JAR 使用，或通过 philosopher

MSFragger 用跨平台的 Java 实现，兼容标准开放的质谱数据格式（mzXML/mzML）。独立的 JAR 和 ProteomeDiscoverer 节点现在也支持 Thermo RAW 文件。MSFragger 输出 PEPXML 或 tsv 格式，很容易与下游数据分析兼容。

## 使用要求

### 输入文件

MSFragger 支持 .mzML, Thermo .raw 和 Bruker timsTOF .d 谱图文件格式。

### 硬件

MSFragger 由于内存片段索引技术，需要大量内存。建议至少 8-16 GB 内存，对复杂的 closed 检索和 open 检索，需要更多内存。

MSFragger 对处理器的要求取决于搜索的复杂性。对 open 检索（500 Da 母离子质量窗口），使用人蛋白质组，采用 tryptic 酶切，单核一小时大约能搜 40,000 张 MS/MS 谱图。MSFragger 支持多线程检索，在 28 核工作站单个文件只要 2 分钟。

### 软件

**操作系统**

MSFragger 已经在 Mac OS X, Windows 7 和许多 Linux 发行版上进行了测试。注意，需要 64 位操作系统，这样才能访问超过 4 GB 内存。

**Java**

MSFragger 使用 Java 1.8 编写，需要安装 Java。

## 安装

MSFragger 是 Java 程序，其实不用安装。不过只在 Windows 上使用过，对 Linux 上的操作不熟悉。因此需要尝试一番。

## 参数设置

## 运行 MSFragger



## 参考

- https://github.com/Nesvilab/MSFragger/wiki
