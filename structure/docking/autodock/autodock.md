# AutoDock

- [AutoDock](#autodock)
  - [简介](#简介)
  - [入门指南](#入门指南)
  - [参考](#参考)

Last updated: 2023-01-09, 18:50
****

## 简介

计算对接被广泛用于蛋白质-配体相互作用的研究以及药物的发现和开发。分子对接通常从一个已知结构的靶结构开始，如药物作用酶的晶体结构，然后使用对接预测小分子与靶蛋白的结合构象和结合自由能。单次对接实验有助于探索靶蛋白的功能，而虚拟筛选（大量小分子和靶蛋白进行对接和排序）可用于发现新的抑制剂，用于开发新的药物。

AutoDock 是一套免费开源软件，用于小分子和大分子受体的对接和虚拟筛选。该套件目前包含如下几个互补工具：

**计算对接软件**

- AutoDock4 是一个基于经验自由能场和快速 Lamarckian 遗传搜索算法的对接软件。可以有效地将配体与生物大分子进行对接和虚拟筛选，也可以用于预测共价配体复合物、具有柔性环的配体、显式水合作用以及金属蛋白靶点。
- AutoDock Vina 是一个基于简单打分函数和快速梯度优化构象搜索的计算对接软件。可用于类药物配体和蛋白质靶标之间的快速有效对接。
- AutoDockFR 也是一个柔性对接程序，允许靶蛋白侧链运动和诱导 fit。
- AutoDockCrankPep 用于肽段和靶蛋白的对接程序。

**交互 GUI**

- AutoDockTools 是一个 GUI 工具，用于 AutoDock 套件的准备坐标、对接和分析。AutoDockTools 是 [MGLTools](https://ccsb.scripps.edu/mgltools/) 的一部分。
- Raccoon 和 Raccoon2 是用于虚拟筛选和分析的交互式 GUI 工具。

**结合位点预测**

- AutoSite 是一个预测受体上配体结合的最佳位点程序。
- AutoLigand 是一个预测配体与受体结合的最佳位点程序。

## 入门指南

学习 AutoDock 的最佳资料：[Computational protein–ligand docking and virtual drug screening with the AutoDock suite](https://www.nature.com/articles/nprot.2016.051)。记得下载附件，包括几个示例文件。该教程介绍了 AutoDock 的三个核心工具：

- AutoDockTools，GUI 程序，用于准备配体和蛋白质坐标文件，以及结果分析；
- AutoDock Vina，一个简单的一步对接软件，适用于大多配体-蛋白质系统柜；
- AutoDock with AutoGrid，分两步进行对接，为特殊系统提供更多用户可调的选项。

当十分对接程序和常见系统后，就可以尝试一些需要特殊处理的对接程序，包括：

- AutoDockFR：支持柔性对接，支持靶蛋白侧链移动和诱导 fit；
- AutoDockCrankPep：肽段和靶蛋白的对接程序。

如果对虚拟筛选感兴趣，Raccoon2 提供了一个专门的 GUI 来管理坐标和对接，以及结果分析。

## 参考

- https://ccsb.scripps.edu/projects/docking/
