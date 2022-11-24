# 在 GROMACS 如何扩展或继续模拟

- [在 GROMACS 如何扩展或继续模拟](#在-gromacs-如何扩展或继续模拟)
  - [简介](#简介)
  - [继续模拟](#继续模拟)
  - [扩展模拟](#扩展模拟)
  - [参考](#参考)

Last updated: 2022-11-24, 19:04
****

## 简介

在进行分子模拟时，往往出现如下情形：

- 模拟停止了，你又不想从头开始重新模拟，最好从模拟崩溃的地方继续模拟，避免浪费时间；
- 模拟结束了，但你想要延长模拟时间。

下面介绍在 GROMACS 中如何继续模拟和扩展模拟。

## 继续模拟

GROMACS 默认每 15 分钟输出一个 cpt 格式的检查点文件 `md.cpt`，并自动将上一个检查点文件备份为 `md_prev.cpt`。

检查点文件包含系统的完整描述，存储了系统的坐标和速度。因此可以从最后一个检查点继续模拟。

只需要在 `gmx mdrun` 中用 `-cpi` 传入检查点文件：

```bash
gmx mdrun -v -deffnm md -cpi md.cpt (-cpt 5)
```

语法：

- 可以更改检查点输出频率，如用 `-cpt 5` 每 5 分钟输出一个检查点文件。

模拟从选择的检查点开始继续。模拟总时间在用来创建 tpr 文件的 mdp 文件中。

如果从同一个检查点开始不同的模拟，你会发现两个模拟有所差异。这是因为计算机的精度有限。

## 扩展模拟

模拟完成后，你可以又想继续模拟一会儿，这时可以用 `gmx convert-tpr` 模块。

这个模块用于编辑 tpr 文件，可以为某个 tpr 文件延长模拟时间。通过两步实现：

1. 首先，要延长模拟时间，用 `gmx convert-tpr` 生成一个包含额外时间的 tpr 文件
2. 然后，从最后一个检查点开始运行新的 tpr 文件（和继续模拟一样）

例如，假设你从 tpr 文件 `md_10.tpr` 完成了一个 10 ns 的模拟，随后，你又想继续模拟 10 ns。

用 `gmx convert-tpr` 延长模拟时间：

```bash
gmx_mpi convert-tpr -s md_10.tpr -extend 10000 -o md_20.tpr
```

语法：

- `-s` 指定要扩展的原始 tpr 文件
- `-extend` 选项指定要添加到模拟中的 ps 数，在上例中微微 10 ns (10000 ps)

然后就可以从最近一个检查点开始运行新的 tpr 文件 `md_20.tpr`。

```bash
gmx mdrun -v -deffnm md_20 -cpi md_10.cpt -noappend
```

这样会得到一个新的轨迹和相应文件。可以使用 `gmx trjcat` 将新轨迹与前一个轨迹合并，如下：

```bash
gmx trjcat -f md_10.xtc md_20.part0002.xtc -o final.xtc
```

`final.xtc` 轨迹包含系统的整个模拟。

可以重复该过程，然后将所有轨迹合并。

## 参考

- https://www.compchems.com/extend-or-continue-a-gromacs-simulation/
