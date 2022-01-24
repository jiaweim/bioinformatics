# 蛋白相似度比较

- [蛋白相似度比较](#蛋白相似度比较)
  - [简介](#简介)
  - [align](#align)
    - [alignment 对象](#alignment-对象)
    - [RMSD](#rmsd)
    - [align 示例](#align-示例)
    - [align API](#align-api)
  - [super](#super)
  - [参考](#参考)

## 简介

PyMOL 及第三方扩展为对齐大分子结构提供了许多操作。

## align

`align` 执行序列对齐，并进行结构叠加，在叠加过程中可能会执行多个循环，以排除在拟合过程中发现的离阈值。

`align` 对序列相似度较高的蛋白质（identity>30%）效果较好。对序列相似度较低蛋白，使用 `super` 或 `cealign` 命名效果更好。

命令：

```sh
align mobile, target [, cutoff [, cycles
    [, gap [, extend [, max_gap [, object
    [, matrix [, mobile_state [, target_state
    [, quiet [, max_skip [, transform [, reset ]]]]]]]]]]]]]
```

- `mobile`, string, 选择的移动对象的原子
- `target`, string, 选择的目标对象的原子
- `cutoff`, float, RMS 离阈值，默认 2.0
- `cycles`, int, 循环最大次数，默认 5

### alignment 对象

指定 `object=` 参数可以创建 alignment 对象。alignment 对象提供如下功能：

- 对齐序列视图
- 在 3D 视图中国以线条的形式展示对齐的原子
- 可以导出为 clustalw 序列比对文件

### RMSD

对齐原子的 RMSD 值（排除离阈值之后的）在文本中输出。

所有原子的 RMSD 可以通过设置 `cycles=0` 获得，这样就不会排除任何离阈值。

也可以通过 Python 脚本捕获 RMSD，具体可以查看下面的 API。

> 输出为 RMS，但其实就是 RMSD，单位为 Angstroms.

### align 示例

```sh
fetch 1oky 1t46, async=0

# 1) default with outlier rejection
align 1oky, 1t46

# 2) with alignment object, save to clustalw file
align 1oky, 1t46, object=alnobj
save alignment.aln, alnobj

# 3) all-atom RMSD (no outlier rejection) and without superposition
align 1oky, 1t46, cycles=0, transform=0
```

### align API

```python
cmd.align( string mobile, string target, float cutoff=2.0,
           int cycles=5, float gap=-10.0, float extend=-0.5,
           int max_gap=50, string object=None, string matrix='BLOSUM62',
           int mobile_state=0, int target_state=0, int quiet=1,
           int max_skip=0, int transform=1, int reset=0 )
```

## super

当两个蛋白的序列相似度较低时，用 super 叠合的效果比 align 的好。

## 参考

- https://pymolwiki.org/index.php/Category:Structure_Alignment
