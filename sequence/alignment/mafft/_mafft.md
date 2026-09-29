# MAFFT

MAFFT 是一款适用于类 Unix 系统的多序列比对程序。它提供多种比对算法：

- `L-INS-i`：高精度，适用于 200 条以内的序列
- `FFT-NS-2`：快速，适用于 30000 条以内的序列

## 安装

### 自动安装

1. 更新软件包列表

```bash
sudo apt update
```

2. 安装 MAFFT

```bash
sudo apt install mafft
```

3. 验证安装

```bash
$ mafft --version
v7.525 (2024/Mar/13)
```

## 使用

```bash
mafft [options] input [> output]
linsi input [> output]
ginsi input [> output]
einsi input [> output]
fftnsi input [> output]
fftns input [> output]
nwns input [> output]
nwnsi input [> output]
mafft-profile group1 group2 [> output]
```

`input`, `group1` 和 `group2` 都必须使用 FASTA 格式。

### 注重准确性的方法

- **L-INS-i**

可能是最准确的方法；推荐用于 200 条以内的序列；结合局部双序列比对信息的迭代优化方法：

```bash
mafft --localpair --maxiterate 1000 input [> output]
linsi input [> output]
```

- **G-INS-i**

适用于长度相似的序列；推荐用于 200 条以内的序列；结合了全局双序列比对信息的迭代优化方法： 

```bash
mafft --globalpair --maxiterate 1000 input [> output]
ginsi input [> output]
```

- **E-INS-i**

适用于包含较大不可比对区域（unalignable regions）的序列；推荐用于 200 条以内的序列：

```bash
mafft --ep 0 --genafpair --maxiterate 1000 input [> output]
einsi input [> output]
```

**提示：** 对于 E-INS-i 方法，建议使用 `--ep 0` 选项，以允许产生较大的缺口（gaps）。

### 注重速度的方法

- **FFT-NS-i**

迭代优化方法；仅进行两轮迭代：

```bash
mafft --retree 2 --maxiterate 2 input [> output]
fftnsi input [> output]`
```

 

- **FFT-NS-i**（迭代优化方法；最多进行 1000 轮迭代）： `mafft --retree 2 --maxiterate 1000 input [> output]`
- **FFT-NS-2**（快速；渐进式方法）： `mafft --retree 2 --maxiterate 0 input [> output]` `fftns input [> output]`
- **FFT-NS-1**（非常快速；推荐用于 2000 条以上的序列；使用粗略引导树的渐进式方法）： `mafft --retree 1 --maxiterate 0 input [> output]`
- **NW-NS-i**（不使用 FFT 近似的迭代优化方法；仅进行两轮迭代）： `mafft --retree 2 --maxiterate 2 --nofft input [> output]` `nwnsi input [> output]`
- **NW-NS-2**（快速；不使用 FFT 近似的渐进式方法）： `mafft --retree 2 --maxiterate 0 --nofft input [> output]` `nwns input [> output]`
- **NW-NS-PartTree-1**（推荐用于约 10,000 至 50,000 条序列；采用 PartTree 算法的渐进式方法）： `mafft --retree 1 --maxiterate 0 --nofft --parttree input [> output]`

## 选项

### 算法

- **`--auto`** 根据数据大小，自动从 L-INS-i、FFT-NS-i 和 FFT-NS-2 中选择合适的策略。默认关闭（off，即始终使用 FFT-NS-2）。
- **`--6merpair`** 

基于共享 6-mer（6个碱基/氨基酸的片段）的数量来计算距离。默认开启（on）。

- **`--globalpair`** 使用 Needleman-Wunsch 算法计算所有双序列比对。比 `--6merpair` 更准确但更慢。适用于可全局比对的序列集。最多适用于约 200 条序列。建议与 `--maxiterate 1000` 组合使用（即 G-INS-i）。默认关闭（off，使用 6-mer 距离）。
- **`--localpair`** 

使用 Smith-Waterman 算法计算所有双序列比对。比 `--6merpair` 更准确但更慢。适用于可局部比对的序列集。最多适用于约 200 条序列。建议与 `--maxiterate 1000` 组合使用（即 L-INS-i）。默认关闭（off，使用 6-mer 距离）。

- **`--genafpair`** 使用带有广义仿射空位罚分（generalized affine gap cost）的局部算法计算所有双序列比对（Altschul 1998）。比 `--6merpair` 更准确但更慢。适用于预期存在较大内部空位的情况。最多适用于约 200 条序列。建议与 `--maxiterate 1000` 组合使用（即 E-INS-i）。默认关闭（off，使用 6-mer 距离）。
- **`--fastapair`** 使用 FASTA 程序（Pearson and Lipman 1988）计算所有双序列比对。需要安装 FASTA。默认关闭（off，使用 6-mer 距离）。
- **`--weighti`** *数值* 从双序列比对中计算出的一致性项（consistency term）的加权因子。仅在选择了 `--globalpair`、`--localpair`、`--genafpair`、`--fastapair` 或 `--blastpair` 时有效。默认值：2.7。
- **`--retree`** *数值* 在渐进式比对阶段构建引导树的次数。仅在使用 6-mer 距离时有效。默认值：2。
- **`--maxiterate`** *数值* 执行迭代优化的循环次数。默认值：0。
- **`--fft`** 在组间比对（group-to-group alignment）中使用 FFT（快速傅里叶变换）近似。默认开启（on）。
- **`--nofft`** 在组间比对中不使用 FFT 近似。默认关闭（off）。
- **`--noscore`** 在迭代优化阶段不检查比对得分。默认关闭（off，即检查得分）。
- **`--memsave`** 使用 Myers-Miller (1988) 算法。默认情况下，当比对长度超过 10,000 个氨基酸/核苷酸（aa/nt）时会自动开启。
- **`--parttree`** 结合 6-mer 距离使用快速建树方法（PartTree, Katoh and Toh 2007）。推荐在输入大量序列（大于约 10,000 条）时使用。默认关闭（off）。
- **`--dpparttree`** 使用基于动态规划（DP）距离的 PartTree 算法。比 `--parttree` 略准确但更慢。推荐在输入大量序列（大于约 10,000 条）时使用。默认关闭（off）。
- **`--fastaparttree`** 使用基于 FASTA 距离的 PartTree 算法。比 `--parttree` 略准确但更慢。推荐在输入大量序列（大于约 10,000 条）时使用。需要安装 FASTA。默认关闭（off）。
- **`--partsize`** *数值* PartTree 算法中的分区数量。默认值：50。
- **`--groupsize`** *数值* 限制生成的比对不超过该数值的序列条数。仅在带有 `--*parttree` 选项时有效。默认值：输入的序列总数。

### 参数设置

- **`--op`** *数值* 

组间比对（group-to-group alignment）时的空位开启罚分（Gap opening penalty）。默认值：1.53。

- **`--ep`** *数值* 组间比对时的偏移值（Offset value），其作用类似于空位延伸罚分（gap extension penalty）。默认值：0.123。
- **`--lop`** *数值* 局部双序列比对（local pairwise alignment）时的空位开启罚分。仅在选择了 `--localpair` 或 `--genafpair` 选项时有效。默认值：-2.00。
- **`--lep`** *数值* 局部双序列比对时的偏移值。仅在选择了 `--localpair` 或 `--genafpair` 选项时有效。默认值：0.1。
- **`--lexp`** *数值* 局部双序列比对时的空位延伸罚分。仅在选择了 `--localpair` 或 `--genafpair` 选项时有效。默认值：-0.1。
- **`--LOP`** *数值* 跳过比对（skip the alignment）时的空位开启罚分。仅在选择了 `--genafpair` 选项时有效。默认值：-6.00。
- **`--LEXP`** *数值* 跳过比对时的空位延伸罚分。仅在选择了 `--genafpair` 选项时有效。默认值：0.00。
- **`--bl`** *数值* 使用 BLOSUM 矩阵（Henikoff and Henikoff 1992）。可选数值为 30、45、62 或 80。默认值：62。
- **`--jtt`** *数值* 使用 JTT PAM 矩阵（Jones et al. 1992）。数值需大于 0。默认使用 BLOSUM62。
- **`--tm`** *数值* 使用跨膜 PAM 矩阵（Jones et al. 1994）。数值需大于 0。默认使用 BLOSUM62。
- **`--aamatrix`** *矩阵文件* 使用用户自定义的氨基酸打分矩阵。矩阵文件的格式与 BLAST 相同。当输入为核苷酸序列时，该选项将被忽略。默认使用 BLOSUM62。
- **`--fmodel`** 将氨基酸/核苷酸的组成信息（composition information）纳入打分矩阵中。默认关闭（off）。

### 输出设置（Output）

- **`--clustalout`** 输出格式：Clustal 格式。默认关闭（off，即默认输出 FASTA 格式）。
- **`--inputorder`** 输出顺序：与输入顺序相同。默认开启（on）。
- **`--reorder`** 输出顺序：按比对结果重新排序。默认关闭（off，即默认使用 inputorder 保持原顺序）。
- **`--treeout`** 将引导树（Guide tree）输出到 `input.tree` 文件中。默认关闭（off）。
- **`--quiet`** 不报告运行进度。默认关闭（off）。

### 输入设置（Input）

- **`--nuc`** 假定输入的序列为核苷酸序列。默认自动识别（auto）。
- **`--amino`** 假定输入的序列为氨基酸序列。默认自动识别（auto）。
- **`--seed`** *比对文件1* `[--seed 比对文件2 --seed 比对文件3 ...]` 将 *比对文件n*（FASTA 格式）中提供的种子比对（seed alignments）与输入文件中的序列进行比对。每个种子比对内部的序列比对关系将被保留。

## 参考

- https://mafft.cbrc.jp/alignment/software/
- https://mafft.cbrc.jp/alignment/software/manual/manual.html