# 概述

- [概述](#概述)
  - [简介](#简介)
  - [PyMOL 功能](#pymol-功能)

2022-01-17, 13:48
***

## 简介

从 [RCSB PDB](https://www.rcsb.org/) 下载一个蛋白结构，例如：

https://www.rcsb.org/structure/7JZK

打开 PDB 文件，其中结构部分如下：

```pdb
ATOM      1  N   THR C 108     -48.621  -8.612  44.917  1.00 82.24           N  
ATOM      2  CA  THR C 108     -49.795  -8.172  45.666  1.00 93.09           C  
ATOM      3  C   THR C 108     -49.382  -7.591  47.014  1.00 90.10           C  
ATOM      4  O   THR C 108     -49.830  -6.515  47.415  1.00 84.37           O  
ATOM      5  CB  THR C 108     -50.824  -9.326  45.877  1.00 98.08           C  
ATOM      6  OG1 THR C 108     -50.307 -10.295  46.803  1.00 98.78           O  
ATOM      7  CG2 THR C 108     -51.179 -10.003  44.544  1.00 95.02           C  
ATOM      8  N   ASP C 109     -48.476  -8.290  47.693  1.00 89.63           N  
ATOM      9  CA  ASP C 109     -48.037  -7.842  49.001  1.00 75.67           C  
ATOM     10  C   ASP C 109     -47.027  -6.712  48.900  1.00 71.48           C  
...
ATOM   3365  C   ALA B 316     -21.124  25.852  44.442  1.00 88.72           C  
ATOM   3366  O   ALA B 316     -21.251  25.130  45.435  1.00 89.59           O  
ATOM   3367  CB  ALA B 316     -23.341  25.415  43.363  1.00 79.51           C  
ATOM   3368  N   THR B 317     -19.946  26.075  43.876  1.00 90.56           N  
ATOM   3369  CA  THR B 317     -18.705  25.531  44.432  1.00 94.94           C  
ATOM   3370  C   THR B 317     -17.978  26.570  45.291  1.00 92.87           C  
ATOM   3371  O   THR B 317     -16.816  26.384  45.652  1.00 98.00           O  
ATOM   3372  CB  THR B 317     -17.737  25.010  43.323  1.00 96.51           C  
ATOM   3373  OG1 THR B 317     -17.650  25.953  42.251  1.00 94.80           O  
ATOM   3374  CG2 THR B 317     -18.196  23.652  42.787  1.00 91.89           C  
TER    3375      THR B 317     
```

例如第 1 行：

```pdb
ATOM      1  N   THR C 108     -48.621  -8.612  44.917  1.00 82.24           N  
```

表示，第 1 个原子 `N`：

- 属于氨基酸 `THR`
- 在 `C` 链上
- 是第 108 个氨基酸
- x, y, z 坐标位置（-48.621  -8.612  44.917）
- 占有率（1.00）
- 温度因子（82.24）
- 原子名称（N）

## PyMOL 功能

PyMOL 有如下应用场景：

- 蛋白质结构展示
  - 图
  - 动画
- 蛋白质-小分子相互作用展示
- 小分子-蛋白质对接动画
- 氨基酸修饰：糖基化、磷酸化...
- 计算小分子附近 5 $\mathring{A}$ 内的氨基酸
