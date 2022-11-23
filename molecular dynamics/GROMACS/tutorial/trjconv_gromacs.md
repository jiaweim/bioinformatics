# 轨迹文件管理

- [轨迹文件管理](#轨迹文件管理)
  - [简介](#简介)
  - [gmx trjconv](#gmx-trjconv)
    - [减少 xtc 估计文件维度](#减少-xtc-估计文件维度)
    - [将 trr 转换为 xtc](#将-trr-转换为-xtc)
    - [选择 xtc 轨迹文件的一部分](#选择-xtc-轨迹文件的一部分)
    - [提取某一帧](#提取某一帧)
    - [使分子在模拟盒子中居中](#使分子在模拟盒子中居中)
    - [gro 转换为 pdb](#gro-转换为-pdb)
  - [trjcat](#trjcat)
  - [参考](#参考)

Last updated: 2022-11-23, 15:06
****

## 简介

GROMACS 处理分子动力学模拟轨迹的两个基本命令：

- `gmx trjconv`
- `gmx trjcat`

## gmx trjconv

`gmx trjconv` 是 GROMACS 分析模拟结果使用最广泛的命令之一。下面介绍一些常见的使用方法。

### 减少 xtc 估计文件维度

有时候模拟生成的轨迹文件过于大（上百 GB），处理起来很麻烦。为了减少数据传输的压力和降低内存占用，可以通过减少帧数降低 xtc 大小。

```bash
gmx trjconv -f system.xtc -s system.tpr -dt 10 -o system_reduced.xtc (-n ../index.ndx)
```

- `-f` 指定初始轨迹
- `-s` 指定 tpr 文件
- `-dt` 指定减少输出的帧数，这里表示每 10ps 写入一帧
- `-o` 指定输出轨迹文件
- 还可以通过 `-n` 指定先前创建的索引文件 `index.ndx`，这样可以对轨迹进行裁剪，只选择系统中感兴趣的特定部分。

### 将 trr 转换为 xtc

GROMACS 的轨迹文件有两种不同的格式：

- 轻量级的 xtc 格式，以较低精度存储系统坐标的轨迹
- 更耗内存的 trr 格式，包含模拟过程中的位置、速度和力的高精度轨迹信息

在 mdp 参数文件中可以指定你需要的格式。

也可以使用 `gmx trjconv` 将轨迹文件从一种格式转换为另一种格式。

例如，将 trr 转换为 xtc:

```bash
gmx trjconv -f system.trr -s system.tpr -o system.xtc (-dt 100 -n index.ndx)
```

- `-f` 提供 trr 格式的初始轨迹文件 `system.trr`
- `-s` 指定 tpr 文件
- `-o` 指定输出的 xtc 轨迹文件

可选：

- `-dt` 用来减少输出中的帧数
- `-n` 指定之前生成的索引文件

### 选择 xtc 轨迹文件的一部分

可以用 `gmx trjconv` 切割轨迹，选择指定两帧之间的部分。

```bash
gmx trjconv -f system.xtc -s system.tpr -b 0 -e 100 -o system_cut.xtc (-n ../index.ndx)
```

- `-f` 指定初始轨迹
- `-s` 指定 tpr 文件
- `-b` 指定切割轨迹的起始帧（0 ps）
- `-e` 指定切割轨迹的结束帧（100 ps）
- `-o` 指定输出轨迹文件位置

可选：

- `-n` 用于包含索引文件

### 提取某一帧

可以用 `gmx trjconv` 提取轨迹的某一帧，并将其导出为 gro 文件，就获得了系统在指定时间步的结构。

使用 `-dump` 指定时间，就能够获得和该时间最近的一帧，例如，提取 $t=10ps$ 最近的一帧：

```bash
gmx trjconv -f system.xtc -s system.tpr -dump 10 -o system.gro (-n ../index.ndx)
```

- `-dump` 指定时间（10 ps）

可选：

- `-n` 指定索引文件 `index.ndx`，这样可以提取系统的一部分结构。

### 使分子在模拟盒子中居中

MD 模拟过程中，可能遇到如下问题：

- 分子/蛋白质 不在模拟盒子的中心
- 模拟的分子分解成不同部分
- 在可视化生成的模拟结构时，看到了奇怪的拉长键

不必担心，这是完全正常的，都是实现周期性边界调节的结果。

使用 `gmx trjconv` 可以获得系统的正确可视化状态。并且可以将系统的特定部分（如分子或蛋白质）置于模拟盒子的中心。

```bash
gmx trjconv -f system.gro -s system.tpr -pbc mol -center -ur compact -o centered.gro (-n index.ndx)
```

- `-f` 以 gro 格式提供初始轨迹
- `-s` 提供 tpr 文件
- `-pbc mol -center` 将分子质心放入盒子，并将系统居中
- `-ur compact` 使所有原子离盒子中心尽可能近
- `-o` 输出结构

运行命令，会要求选择：

1. Select the group that you want to center in the box.
2. Select the group that you want in the output file

将蛋白放在模拟盒子中心，输出包含整个系统的 gro 文件，则选择：

1. **“Protein”** as group 1
2. **“System”** as group 2

### gro 转换为 pdb

```bash
gmx trjconv -s system.tpr -f system.gro -o system.pdb -pbc whole -conect (-n index.ndx)
```

语法：

- `-s` 指定 tpr 文件
- `-f` 指定需要转换为 gro 文件 `system.gro`
- `-o` 指定输出 pdb 文件 `system.pdb`
- `-pbc` 指定 PBC 处理方式
- `-conect` 将

GROMACS 会询问将哪部分保存到 pdb 文件。可以选择整个系统，或者系统的任何部分。比如，如果模拟水中的大那笔之，但是只想要没有溶剂的蛋白质 pdb 文件，则可以选择 `Group 1 "Protein"`。

## trjcat

`trjcat` 用于合并不同的轨迹文件。

这个命令使用相对较少，但偶尔可能很有用：

```bash
gmx trjcat -f traj_1.xtc traj_2.xtc -o final_traj.xtc (-settime)
```

如果一个目录中有多个 xtc 文件，则可以直接使用 *xtc，GROMACS 会自动根据时间值排序文件。

## 参考

- https://www.compchems.com/how-to-manage-a-trajectory-file-in-gromacs/
- https://jerkwin.github.io/2016/05/31/GROMACS%E8%BD%A8%E8%BF%B9%E5%91%A8%E6%9C%9F%E6%80%A7%E8%BE%B9%E7%95%8C%E6%9D%A1%E4%BB%B6%E7%9A%84%E5%A4%84%E7%90%86/
