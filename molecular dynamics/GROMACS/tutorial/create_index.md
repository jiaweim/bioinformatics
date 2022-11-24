# 创建索引文件

- [创建索引文件](#创建索引文件)
  - [gmx make\_ndx](#gmx-make_ndx)
  - [创建索引](#创建索引)
  - [修改现有索引](#修改现有索引)
  - [使用索引文件](#使用索引文件)
  - [参考](#参考)

***

## gmx make_ndx

`gmx make_ndx` 命令用于创建索引组（index group）。

GROMACS 为不同操作设计了不同文件格式，索引文件格式为 `ndx`，由原子集合组成。

GROMACS 会为系统创建一个默认索引文件，不指定索引文件时，使用该默认索引文件。当默认索引文件不能满足需求时，即需要自己创建了。

## 创建索引

假设你有一个很大的系统，但是你只对其中一小部分感兴趣，此时就可以创建一个恶索引文件 `index.ndx`，并创建一个只包含你感兴趣部分的 group。

创建索引：

```bash
gmx make_ndx -f system.gro -o index.ndx
```

语法：

- `-f` 指定初始结构 `system.gro`
- `-o` 指定输出索引 `index.ndx`

运行该命令，会弹出 group 列表：

```bash
  0 System              : 260572 atoms
  1 Protein             :  4382 atoms
  2 Protein-H           :  2144 atoms
  3 C-alpha             :   268 atoms
  4 Backbone            :   804 atoms
  5 MainChain           :  1073 atoms
  6 MainChain+Cb        :  1336 atoms
  7 MainChain+H         :  1334 atoms
  8 SideChain           :  3048 atoms
  9 SideChain-H         :  1071 atoms
 10 Prot-Masses         :  4382 atoms
 11 non-Protein         : 256190 atoms
 12 Other               : 255828 atoms
 13 CHL1                : 51507 atoms
 14 POPC                : 47682 atoms
 15 Na+                 :   221 atoms
 16 Cl-                 :   141 atoms
 17 TP3                 : 156639 atoms
```

这些 group 的名称不言自明。

要添加包含 Protein (group 1)、lipid CHL1 (group 13) 和 POPC (group 14)，可以输入如下命令：

```bash
1 | 13 | 14
```

```bash
  0 System              : 260572 atoms
  1 Protein             :  4382 atoms
  2 Protein-H           :  2144 atoms
  3 C-alpha             :   268 atoms
  4 Backbone            :   804 atoms
  5 MainChain           :  1073 atoms
  6 MainChain+Cb        :  1336 atoms
  7 MainChain+H         :  1334 atoms
  8 SideChain           :  3048 atoms
  9 SideChain-H         :  1071 atoms
 10 Prot-Masses         :  4382 atoms
 11 non-Protein         : 256190 atoms
 12 Other               : 255828 atoms
 13 CHL1                : 51507 atoms
 14 POPC                : 47682 atoms
 15 Na+                 :   221 atoms
 16 Cl-                 :   141 atoms
 17 TP3                 : 156639 atoms
 18 Protein_CHL1_POPC   : 103571 atoms 
```

这样就多了一个 group。

可以对其重命名：

```bash
name 18 Protein_Lipids
```

```bash
  0 System              : 260572 atoms
  1 Protein             :  4382 atoms
  2 Protein-H           :  2144 atoms
  3 C-alpha             :   268 atoms
  4 Backbone            :   804 atoms
  5 MainChain           :  1073 atoms
  6 MainChain+Cb        :  1336 atoms
  7 MainChain+H         :  1334 atoms
  8 SideChain           :  3048 atoms
  9 SideChain-H         :  1071 atoms
 10 Prot-Masses         :  4382 atoms
 11 non-Protein         : 256190 atoms
 12 Other               : 255828 atoms
 13 CHL1                : 51507 atoms
 14 POPC                : 47682 atoms
 15 Na+                 :   221 atoms
 16 Cl-                 :   141 atoms
 17 TP3                 : 156639 atoms
 18 Protein_Lipids      : 103571 atoms 
```

还有多种选择方式。

- 选择 1-100 的原子

```bash
a 1-100
```

- 选择残基

```bash
r 1-100
```

- 只选择蛋白的重原子

```bash
1 & ! a H* 
```

表示 group **1** and (**&**) not (**!**) atoms (**a**) hydrogens (**H**)。

完成后，输入 `q` 保存。

## 修改现有索引

```bash
gmx make_ndx -f system.gro -n index.ndx
```

## 使用索引文件

索引文件一般通过 `-n` 选项指定，和其它命令结合使用。

## 参考

- https://www.compchems.com/how-to-create-an-index-file-in-gromacs/
- https://manual.gromacs.org/current/onlinehelp/gmx-make_ndx.html
