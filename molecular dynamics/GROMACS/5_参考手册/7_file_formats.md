# 文件格式

- [文件格式](#文件格式)
  - [文件格式摘要](#文件格式摘要)
    - [参数文件](#参数文件)
    - [拓扑文件](#拓扑文件)
  - [文件格式细节](#文件格式细节)
    - [atp](#atp)
    - [gro](#gro)
    - [itp](#itp)
    - [mdp](#mdp)
    - [top](#top)
    - [tpr](#tpr)
    - [trr](#trr)
  - [参考](#参考)

2022-05-25, 21:57
***

## 文件格式摘要

### 参数文件

|文件|说明|
|---|---|
|[mdp](#mdp)|运行参数文件，[gmx grompp](../3_用户指南/11_command_line_reference.md#gmx-grompp) 和 [gmx conveert-tpr]
- `mdp`，运行参数文件，`gmx grompp` 和 `gmx convert-tpr` 的输入；
- `m2p`，`gmx xpm2ps` 的输入参数。

**结构文件**

- `gro`，GROMACS 格式
- `g96`，GROMOS-96 格式
- `pdb`，Protein DataBank 格式

结构和质量（db）：`tpr`, `gro`, `g96` 或 `pdb`。当使用 gro 或 pdb，则质量数据库中读取合适的质量。

### 拓扑文件

|文件格式|说明|
|---|---|
|[top](#top)|系统拓扑（ascii）|



## 文件格式细节

### atp

### gro

gro 文件包含 Gromos87 格式的分子结构。通过连接文件 gro 可以作为轨迹使用。每一帧的标题字符串中包含时间值，以 `t=` 开头。下面是部分样本：

```gro
MD of 2 waters, t= 0.0
6
1WATER OW1 1 0.126 1.624 1.679 0.1227 -0.0580 0.0434
1WATER HW2 2 0.190 1.661 1.747 0.8085 0.3191 -0.7791
1WATER HW3 3 0.177 1.568 1.613 -0.9045 -2.6469 1.3180
2WATER OW1 4 1.275 0.053 0.622 0.2519 0.3140 -0.1734
2WATER HW2 5 1.337 0.002 0.680 -1.0641 -1.1349 0.0257
2WATER HW3 6 1.326 0.120 0.568 1.9427 -0.8216 -0.0244
1.82060 1.82060 1.82060
```

从上到下每行信息：

- 标题行，格式自由，可以以 't=' 插入时间，单位为 ps
- 原子个数
- 每行一个原子
- 盒子向量（空格分离的实数）：v1(x) v2(y) v3(z) v1(y) v1(z) v2(x)
v2(z) v3(x) v3(y)，最后 6 个值可以忽略，默认为 0.GROMACS 只支持 v1(y)=v1(z)=v2(z)=0 的盒子。

### itp

itp 文件表示 include topology。这些文件包含在拓扑文件 top 中。

### mdp

下面是一个 mdp 文件样本。这些值的顺序不重要。对重复设置，后面的覆盖前面的。左侧的破折号和下划线被忽略。

样本文件是模拟一个蛋白质在水盒子中 1 纳秒的设置。

```mdp
integrator               = md
dt                       = 0.002
nsteps                   = 500000

nstlog                   = 5000
nstenergy                = 5000
nstxout-compressed       = 5000

continuation             = yes
constraints              = all-bonds
constraint-algorithm     = lincs

cutoff-scheme            = Verlet

coulombtype              = PME
rcoulomb                 = 1.0

vdwtype                  = Cut-off
rvdw                     = 1.0
DispCorr                 = EnerPres

tcoupl                   = V-rescale
tc-grps                  = Protein  SOL
tau-t                    = 0.1      0.1
ref-t                    = 300      300

pcoupl                   = Parrinello-Rahman
tau-p                    = 2.0
compressibility          = 4.5e-5
ref-p                    = 1.0
```

### top

2022-05-26, 09:18

top 文件表示拓扑，是一个 ASCII 文件，由 [gmx grompp](../3_用户指南/11_command_line_reference.md#gmx-grompp) 读取并转换为二进制的拓扑文件 [tpr](#tpr)。

top 文件示例：

```top
;
; Example topology file
;
[ defaults ]
; nbfunc        comb-rule       gen-pairs       fudgeLJ fudgeQQ
  1             1               no              1.0     1.0

; The force field files to be included
#include "rt41c5.itp"

[ moleculetype ]
; name  nrexcl
Urea         3

[ atoms ]
;   nr    type   resnr  residu    atom    cgnr  charge
     1       C       1    UREA      C1       1   0.683
     2       O       1    UREA      O2       1  -0.683
     3      NT       1    UREA      N3       2  -0.622
     4       H       1    UREA      H4       2   0.346
     5       H       1    UREA      H5       2   0.276
     6      NT       1    UREA      N6       3  -0.622
     7       H       1    UREA      H7       3   0.346
     8       H       1    UREA      H8       3   0.276

[ bonds ]
;  ai    aj funct           c0           c1
    3     4     1 1.000000e-01 3.744680e+05
    3     5     1 1.000000e-01 3.744680e+05
    6     7     1 1.000000e-01 3.744680e+05
    6     8     1 1.000000e-01 3.744680e+05
    1     2     1 1.230000e-01 5.020800e+05
    1     3     1 1.330000e-01 3.765600e+05
    1     6     1 1.330000e-01 3.765600e+05

[ pairs ]
;  ai    aj funct           c0           c1
    2     4     1 0.000000e+00 0.000000e+00
    2     5     1 0.000000e+00 0.000000e+00
    2     7     1 0.000000e+00 0.000000e+00
    2     8     1 0.000000e+00 0.000000e+00
    3     7     1 0.000000e+00 0.000000e+00
    3     8     1 0.000000e+00 0.000000e+00
    4     6     1 0.000000e+00 0.000000e+00
    5     6     1 0.000000e+00 0.000000e+00

[ angles ]
;  ai    aj    ak funct           c0           c1
    1     3     4     1 1.200000e+02 2.928800e+02
    1     3     5     1 1.200000e+02 2.928800e+02
    4     3     5     1 1.200000e+02 3.347200e+02
    1     6     7     1 1.200000e+02 2.928800e+02
    1     6     8     1 1.200000e+02 2.928800e+02
    7     6     8     1 1.200000e+02 3.347200e+02
    2     1     3     1 1.215000e+02 5.020800e+02
    2     1     6     1 1.215000e+02 5.020800e+02
    3     1     6     1 1.170000e+02 5.020800e+02

[ dihedrals ]
;  ai    aj    ak    al funct           c0           c1           c2
    2     1     3     4     1 1.800000e+02 3.347200e+01 2.000000e+00
    6     1     3     4     1 1.800000e+02 3.347200e+01 2.000000e+00
    2     1     3     5     1 1.800000e+02 3.347200e+01 2.000000e+00
    6     1     3     5     1 1.800000e+02 3.347200e+01 2.000000e+00
    2     1     6     7     1 1.800000e+02 3.347200e+01 2.000000e+00
    3     1     6     7     1 1.800000e+02 3.347200e+01 2.000000e+00
    2     1     6     8     1 1.800000e+02 3.347200e+01 2.000000e+00
    3     1     6     8     1 1.800000e+02 3.347200e+01 2.000000e+00

[ dihedrals ]
;  ai    aj    ak    al funct           c0           c1
    3     4     5     1     2 0.000000e+00 1.673600e+02
    6     7     8     1     2 0.000000e+00 1.673600e+02
    1     3     6     2     2 0.000000e+00 1.673600e+02

; Include SPC water topology
#include "spc.itp"

[ system ]
Urea in Water

[ molecules ]
Urea    1
SOL     1000
```

### tpr

2022-05-26, 09:18

tpr 文件表示便携式二进制（portable binary）运行输入文件。该文件包含模拟的起始结构、分子拓扑以及所有的模拟参数。由于是二进制格式，因此无法使用普通的编辑器读取。读取 tpr 文件方法：

```sh
gmx dump -s topol.tpr
```

或者：

```sh
gmx dump -s topol.tpr | less
```

还可以使用如下命令比价两个 tpr 文件：

```sh
gmx check -s1 top1 -s2 top2 | less
```

### trr

## 参考

- https://manual.gromacs.org/current/reference-manual/file-formats.html
