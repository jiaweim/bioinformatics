# FastQC

- [FastQC](#fastqc)
  - [简介](#简介)
  - [安装](#安装)
  - [卸载](#卸载)
  - [使用](#使用)
  - [参考](#参考)


## 简介

大多数测序仪都会生成 QC 报告，但这通常只专注于识别测序仪本身产生的问题。FastQC 旨在提供发现测序器和起始文库问题的报告。

FastQC 有两种运行模式：用户少量 FastQ 文件分析的交互式程序；用于集成到更大分析管道的非交互模式。

FastQC 的主要功能：

- 读取 BAM、SAM 和 FastQ 文件
- 提供一个快速概览，说明数据哪些地方可能有问题
- 数据的图形和表格摘要
- 将结果导出为 HTML 格式
- 脱机操作，在不运行交互式程序的情况下自动生成报告

## 安装

- apt-get 安装

```bash
# 更新 apt 数据库
$ sudo apt-get update
# 安装
$ sudo apt-get -y install fastqc
```

- apt 安装

```bash
$ sudo apt update
$ sudo apt -y install fastqc
```

- 从源码安装

```bash
# 下载
$ wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.12.1.zip
# 解压
$ unzip fastqc_v0.12.1.zip
$ cd FastQC/
# 修改权限
$ chmod 755 fastqc
```

## 卸载

- 卸载 fastqc

```bash
$ sudo apt-get remove fastqc
```

- 卸载 fastqc 及其依赖项

```bash
$ sudo apt-get -y autoremove fastqc
```

- 移除 fastqc 配置和数据

```bash
$ sudo apt-get -y purge fastqc
```

- 移除 fastqc 配置、数据以及所有依赖项

```bash
$ sudo apt-get -y autoremove --purge fastqc
```

## 使用



## 参考

- https://github.com/s-andrews/FastQC
- https://www.bioinformatics.babraham.ac.uk/projects/fastqc/
- https://installati.one/install-fastqc-ubuntu-22-04/