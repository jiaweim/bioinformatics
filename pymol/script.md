# PyMOL 高级教程

- [PyMOL 高级教程](#pymol-高级教程)
  - [简介](#简介)
  - [安装 PyMOLwiki 中的命令](#安装-pymolwiki-中的命令)
  - [zero_residues](#zero_residues)

## 简介

PyMOL支持Python 编程语言，故可以借助python让pymol无所不能，pymol除了显示软件，也能成为计算软件。

脚本：把 pymol 作为一个模块，实现一些计算功能。 

命令：pymol中内置了一些命令，如color、dist等，我们也可以自定义新的命令。 

插件：pymol 中内置了一些插件，如 apbs-pdb2pqr 等，我们也可以自定义插件。

## 安装 PyMOLwiki 中的命令

以 [FocalBlur](https://pymolwiki.org/index.php/FocalBlur) 为例，演示如何安装命令。FocalBlur 脚本通过在图像中引入焦点模糊来常见有意思的图形。

1. 下载脚本

focal.blur.py 脚本位置：https://raw.githubusercontent.com/Pymol-Scripts/Pymol-script-repo/master/focal_blur.py

将脚本保存到本地，比如 D:\pdb\scripts\focal_blur.py

2. 打开 PyMOL，在命令窗口输入 `run D:\pdb\scripts\focal_blur.py` 完成安装。

3. 

## zero_residues

https://pymolwiki.org/index.php/Zero_residues

该脚本对所有残基重新编号，使第一个残基编号为 0。在处理对齐时非常有用。

