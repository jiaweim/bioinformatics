# MUSCLE

- [MUSCLE](#muscle)
  - [简介](#简介)
  - [Linux 版本安装](#linux-版本安装)
  - [使用](#使用)
  - [命令](#命令)
    - [align](#align)
    - [super5](#super5)
  - [概念](#概念)
    - [Alignment replicate](#alignment-replicate)
    - [MSA ensemble](#msa-ensemble)
    - [Stratified ensemble](#stratified-ensemble)
    - [Guide tree permutations](#guide-tree-permutations)
  - [参考](#参考)

## 简介

MUSCLE（**MU**ltiple **S**equence **C**omparison by **L**og-**E**xpectation）据陈比 ClustalW2 和 T-Coffee 具有更好的平均精度和速度。

## Linux 版本安装

https://github.com/rcedgar/muscle/releases

下载 muscle5.1.linux_intel64，下载后，添加运行权限：

```sh
chmod 777 muscle5.1.linux_intel64
```

然后就能运行了。

## 使用

使用 `align` 命令比对，例如：

```sh
muscle -align sequences.fasta -output alignment.fasta
```

如果你只需要一个高质量的 MSA，使用这个命令就够了。

如果序列特别长，需要较多的内存或时间，则建议使用 `super5` 命令。

## 命令

### align

使用 PPP 算法比对序列。

```sh
muscle -align seqs.fa -output aln.afa
muscle -align seqs.fa -output aln.afa -perturb 3 -perm abc
muscle -align seqs.fa -output stratified_ensemble.efa -stratified
muscle -align seqs.fa -output stratified_replicate.@.afa -stratified
muscle -align seqs.fa -output diversified_ensemble.efa -diversified
```

`align` 使用 PPP 算法比对序列。输入必须为 FASTA 格式。

### super5

使用 Super5 算法比对序列。示例：

```sh
muscle -super5 seqs.fa -output aln.afa
muscle -super5 seqs.fa -output aln.afa -perturb 3 -perm abc
muscle -super5 seqs.fa -output replicate.@.afa -perturb 3 -perm all
muscle -super5 seqs.fa -output replicates.efa -perturb 3 -perm all
```

`super5` 命令使用 Super5 算法比对序列。

输入支持 FASTA 格式。默认生成单个比对，输出比对 FASTA 格式。Super5 通常用于大型序列比对，处理 PPP 算法太慢的情况。

该命令不直接支持生成完整的

|选项|说明|
|---|---|
|`-perturb SEED`|生成 HMM 扰动的随机整数 seed，默认 SEED=0 使用默认HMM参数|
|`-perm PERM`|Specifies the guide tree permutation. PERM can be none, abc, acb and bca, default is none.|
|-consiters N|Number of consistency iterations. Default 2.|
|-refineiters N|Number of refinement iterations. Default 100.|
|-nt|Input sequences use nucleotide alphabet (default auto-detect).|
|-amino|Input sequences use amino acid alphabet (default auto-detect).
|-threads N|Number of threads. Default is the number of CPU cores, or 20 if the CPU has more than 20 cores.|

## 概念

### Alignment replicate

replicate 表示 MSA ensemble 中的一个 MSA。

### MSA ensemble

MSA 集合（ensemble）表示相同序列的可选 MSA 集合。ensemble 中的一个 MSA 称为 replicate。

### Stratified ensemble

stratified ensemble 对每个 perturbation 参数包含四个 replicates。

**HMM 扰动（perturbation）**

PPP 算法使用随机量调整其隐马尔可夫模型（hidden Markov model, HMM）参数。这些调整称为扰动。调整的幅度设置为最大值不会降低基准测试精度。

### Guide tree permutations

引导树排列是为了在不影响精度的前提下，将实质性变化引入由渐进对齐产生的系统误差中。优化精度要求在添加发散序列前，将密切相关的序列先对齐，这就要求引导树的连接顺序应该保持在叶子附近。实质性变化要求以不同的顺序加入较大的群体。


## 参考

- [MUSCLE 官网](http://www.drive5.com/muscle/)
- https://www.ebi.ac.uk/Tools/msa/muscle/
