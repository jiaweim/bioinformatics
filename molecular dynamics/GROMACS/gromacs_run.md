# 运行 GROMACS

- [运行 GROMACS](#运行-gromacs)
  - [文件准备](#文件准备)
    - [初始结构文件](#初始结构文件)
    - [力场相关](#力场相关)
    - [后处理工具](#后处理工具)
  - [示例](#示例)

## 文件准备

需要的文件：

- 初始构型文件：.gro, .pdb。
- 力场文件：.top, .itp
- 参数控制文件：mdp
- 索引文件：ndx

### 初始结构文件

建模相关工具：

Gauss View（收费）, Material Studio（收费）, Packmol, VMD...

### 力场相关

力场：AMBER, CHARMM, OPLS-AA, GROMOS, MARTINI...

其中 [Martini](http://md.chem.rug.nl/) 力场特别适合于蛋白质、细胞膜等复杂生物体系。

GROMACS 力场文件相关工具：

pdb2gmx, AMBER Tool, tppmktop, x2top, martini.py, ATB/PRODRG...

### 后处理工具

GROMACS 自带工具：

- gmx msd (计算均方位移)
- gmx rdf (计算径向分布函数)
- gmx totcf (计算旋转自相关函数)
- gmx potential (计算静电势)
- gmx helix (计算 $\alpha$ 螺旋结构的基本性质)

其它分析工具：

- MD_Analysis
- VMD
- Python, C++, Fortran 等语言自编后处理程序

## 示例

用 packmol 获得模拟体系，