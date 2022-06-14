# Clustal Omega

- [Clustal Omega](#clustal-omega)
  - [简介](#简介)
  - [使用](#使用)
  - [命令说明](#命令说明)
    - [输入序列](#输入序列)
    - [聚类](#聚类)
    - [输出格式](#输出格式)
    - [其它选项](#其它选项)
  - [实例](#实例)
  - [参考](#参考)

Last updated: 2022-06-14, 15:28
@author Jiawei Mao
****

## 简介

Clustal Omega （CO）是一个用于蛋白质、DNA 和 RNA 的通用多序列比对（MSA）工具。

在默认模式下，用户提供要比对的序列文件，CO 将这些序列聚类成一个引导树，并用该引导树指导序列的“渐进式”对齐。CO 还提供了对齐已有 alignments、序列和已有 alignment 对齐的工具。

Clustal Omega 使用隐马尔可夫模型（HMM）作为比对引擎，使用 mBed 的增强版生成引导树，mBed 可以在 O(N*log(N)) 时间内聚类大量序列。然后使用 HHalign 根据引导树对越来越大的 alignment 进行对齐。

## 使用

命令：

```shell
Usage: clustalo [-hv] [-i {<file>,-}] [--hmm-in=<file>]... [--hmm-batch=<file>] [--dealign] [--profile1=<file>] [--profile2=<file>] [--is-profile] [-t {Protein, RNA, DNA}] [--infmt={a2m=fa[sta],clu[stal],msf,phy[lip],selex,st[ockholm],vie[nna]}] [--distmat-in=<file>] [--distmat-out=<file>] [--guidetree-in=<file>] [--guidetree-out=<file>] [--pileup] [--full] [--full-iter] [--cluster-size=<n>] [--clustering-out=<file>] [--trans=<n>] [--posterior-out=<file>] [--use-kimura] [--percent-id] [-o {file,-}] [--outfmt={a2m=fa[sta],clu[stal],msf,phy[lip],selex,st[ockholm],vie[nna]}] [--residuenumber] [--wrap=<n>] [--output-order={input-order,tree-order}] [--iterations=<n>] [--max-guidetree-iterations=<n>] [--max-hmm-iterations=<n>] [--maxnumseq=<n>] [--maxseqlen=<l>] [--auto] [--threads=<n>] [--pseudo=<file>] [-l <file>] [--version] [--long-version] [--force] [--MAC-RAM=<n>]
```

A typical invocation would be: clustalo -i my-in-seqs.fa -o my-out-seqs.fa -v

Iteration:
  --iterations, --iter=<n>  Number of (combined guide-tree/HMM) iterations
  --max-guidetree-iterations=<n> Maximum number of guidetree iterations
  --max-hmm-iterations=<n>  Maximum number of HMM iterations

Limits (will exit early, if exceeded):
  --maxnumseq=<n>           Maximum allowed number of sequences
  --maxseqlen=<l>           Maximum allowed sequence length

Miscellaneous:
  --auto                    Set options automatically (might overwrite some of your options)
  --threads=<n>             Number of processors to use
  --pseudo=<file>           Input file for pseudo-count parameters
  -l, --log=<file>          Log all non-essential output to this file
  -h, --help                Print this help and exit
  -v, --verbose             Verbose output (increases if given multiple times)
  --version                 Print version information and exit
  --long-version            Print long version information and exit
  --force                   Force file overwriting

## 命令说明

### 输入序列

|命令|说明|
|---|---|
|`-i, --in, --infile={<file>,-}`|序列文件，`-` 表示从 stdin 读取序列|
|`--hmm-in=<file>`|HMM 输入文件|
|`--dealign`|Dealign 输入序列|
|`--profile1, --p1=<file>`|预对齐序列文件（对齐的列保持固定）|
|`--profile2, --p2=<file>`|预对齐序列文件（对齐的列保持固定）|
|`--is-profile`|disable check if profile, force profile (default no)|
|`-t, --seqtype={Protein, RNA, DNA}`|序列类型，默认 `auto`|
|`--infmt=`|指定输入序列格式，默认 `auto`|

`--infmt` 支持选项包括：{a2m=fa[sta],clu[stal],msf,phy[lip],selex,st[ockholm],vie[nna]}。

Clustal-Omega 支持 3 种类型的输入序列：

1. 包含未对齐或已对齐序列的文件
2. 对齐序列的 profiles （包含多序列 alignment）
3. HMM

支持以上输入的有效组合。

### 聚类

  --distmat-in=<file>       Pairwise distance matrix input file (skips distance computation)
  --distmat-out=<file>      Pairwise distance matrix output file
  --guidetree-in=<file>     Guide tree input file (skips distance computation and guide-tree clustering step)
  --guidetree-out=<file>    Guide tree output file
  --pileup                  Sequentially align sequences
  --full                    Use full distance matrix for guide-tree calculation (might be slow; mBed is default)
  --full-iter               Use full distance matrix for guide-tree calculation during iteration (might be slowish; mBed is default)
  --cluster-size=<n>        soft maximum of sequences in sub-clusters
  --clustering-out=<file>   Clustering output file
  --trans=<n>               use transitivity (default: 0)
  --posterior-out=<file>    Posterior probability output file
  --use-kimura              use Kimura distance correction for aligned sequences (default no)
  --percent-id              convert distances into percent identities (default no)

**mBed-like Clustering Iteration**

在后续迭代过程中使用 mbed-like 聚类。


### 输出格式

|命令|说明|
|---|---|
|`-o, --out, --outfile={file,-}`|输出文件，默认 stdout|
|`--outfmt={a2m=fa[sta],clu[stal],msf,phy[lip],selex,st[ockholm],vie[nna]}`|MSA 输出文件格式，默认 fasta|
|`--residuenumber, --resno`|in Clustal format print residue numbers (default no)|
|`--wrap=<n>`|number of residues before line-wrap in output|
|`--output-order={input-order,tree-order}`|MSA 输出顺序，默认和输入相同 `input-order`|

Clustal-Omega 支持多种输出格式，通过 `--outfmt` 设置输出格式：

- Fasta 格式：`--outfmt=a2m` 或 `--outfmt=fa` 或 `--outfmt=fasta`
- Clustal 格式：`--outfmt=clu` 或 `outfmt=clustal`
- Msf 格式：`--outfmt=msf`
- Phylip 格式：`--outfmt=phy` 或 `--outfmt=phylip`
- Selex 格式：`--outfmt-selex`
- `Stockholm` 格式：`--outfmt=st` 或 `--outfmt=stockholm`
- Vienna 格式：

### 其它选项

|选项|说明|
|---|---|
|`--auto`|自动设置选项（可能会覆盖其它选项）|
|`--threads=<n>`|使用线程数|
|`-l, --log=<file>`|
|`-v, --verbose`|详细输出，increase if given multiple times|
|`--force`|默认不覆盖文件，使用该选项强制覆盖文件|

## 实例

- 比对

```shell
./clustalo -i globin.fa
```

读取 globin.fa 序列文件，对齐序列，将结果以 fasta/a2m 格式输出到屏幕。

- 输出 sto 格式

```shell
./clustalo -i globin.fa -o globin.sto --outfmt=st
```

如果文件 globin.sto 不存在，Clustal-Omega 读取 globin.fa 序列文件，对齐序列，将结果保存到 Stockholm 格式的 globin.sto 文件中。如果 globin.sto 文件存在，Clustal-Omega 在读取 globin.fa 文件前就终止任务退出。

- 输出 aln 格式

```shell
./clustalo -i globin.fa -o globin.aln --outfmt=clu --force
```

读取 globin.fa 序列文件，对齐序列，将结果保存到 Clustal 格式的 globin.aln 文件中，如果 globin.aln 文件存在，则覆盖该文件。

- 输出引导树和距离矩阵

```shell
./clustalo -i globin.fa --distmat-out=globin.mat --guidetree-out=globin.dnd --force
```

读取序列文件 globin.fa，对齐序列，将结果以 fasta 格式输出到屏幕，将 guide-tree 输出到 globin.dnd，距离矩阵输出到 globin.mat，覆盖已有文件。

- 自定义输入引导树

```shell
./clustalo -i globin.fa --guidetree-in=globin.dnd
```

读入文件 globin.fa 和 globin.dnd，跳过距离计算和引导树创建，使用 globin.dnd 中的引导树。

- 自定义 HMM 文件

```shell
./clustalo -i globin.fa --hmm-in=PF00042.hmm
```

读取序列文件 globin.fa 和 HMM 文件 PF00042.hmm（HMMer2 或 HMMer3 格式）。然后执行对齐，在 MSA 过程中将 PF00042.hmm 中的 pseudo-count 信息转移到 sequences/profiles。

- dealign 生成 HMM

```shell
./clustalo -i globin.sto
```

读取 Stockholm 格式的 alignment 文件 globin.sto。将 alignment 转换为 HMM，去对齐后重新对齐序列，在 MSA 过程中转义 pseudo-count 信息到 sequences/profiles。使用 full distance matrix 构建引导树。

- dealign 后 re-align

```shell
./clustalo -i globin.sto  --dealign
```

相对上例，没有生成 HMM，也没有转义 pseudo-count 信息。因此输出和没有对齐的输入一样。等同于 `./clustalo -i globin.fa`

```shell
./clustalo -i globin.fa --iter=2
```

读取文件 globin.fa，根据 k-tuple distances 创建 UPGMA 引导树，执行初始对齐。该初始对齐被转换为 HMM，


## 参考

- http://www.clustal.org/omega/
