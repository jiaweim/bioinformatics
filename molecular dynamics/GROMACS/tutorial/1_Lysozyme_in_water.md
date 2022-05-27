# 溶菌酶在水里的模拟

- [溶菌酶在水里的模拟](#溶菌酶在水里的模拟)
  - [简介](#简介)
  - [准备拓扑结构](#准备拓扑结构)
    - [GROMACS 常识](#gromacs-常识)
    - [生成溶菌酶的拓扑文件](#生成溶菌酶的拓扑文件)
    - [检查拓扑文件](#检查拓扑文件)
  - [定义溶剂盒子](#定义溶剂盒子)
  - [添加离子](#添加离子)
  - [参考](#参考)

2022-05-24, 17:16
***

## 简介

![](images/2022-05-24-17-16-13.png)

该教程模拟一个蛋白质（溶菌酶）在包含离子的水中行为。每个步骤详细解释了输入和输出，使用典型的设置。

## 准备拓扑结构

![](images/2022-05-24-17-21-20.png)

### GROMACS 常识

GROMACS 5.0 之后，所有 GROMACS 工具都成为 "gmx" 程序的模块。这与之前的版本有所不同，那时所有工具都作为单独的命令调用。在 5.0 中，这些工具仍然可以通过符号链接实现，但不推荐。可以调用如下命令查看 GROMACS 模块：

```sh
gmx help (module)
```

或者

```sh
gmx (module) -h
```

将 `(module)` 替换为具体的命令名称。然后相关信息就被输出，包括可用算法、选项、所需文件格式、已知的 bugs 和限制等。对 GROMACS 新用户来说，调用常用命令的 help 信息是一种很好的学习方式。

### 生成溶菌酶的拓扑文件

首先我们要下载溶菌酶（Lysozyme）的蛋白质结构文件。本教程我们使用鸡蛋清溶菌酶（PDB 1AKI）。到 [RCSB](https://www.rcsb.org/) 下载晶体结构的 PDB 文件。

下载结构后，可以使用 VMD, Chimera, PyMOL 等可视化结构。另外，还需要去掉上面的结晶水。可以用纯文本软件打开结构文件，删除 PDB 文件中的水分子（HOH 残基）。也可以使用 grep 

```sh
grep -v HOH 1aki.pdb > 1AKI_clean.pdb
```

也可以使用 PyMOL 载入 pdb 文件，然后用 `remove solvent` 命令移除水分子。

一定注意检查 pdb 文件中 MISSING 注释下的内容，因为这些是晶体结构中缺失的原子或残基。末端残基的缺失对动力学模拟可能没影响，但是内部缺失的原子或残基会导出 `pdb2gmx` 出错。可以使用其它软件包对这些缺失的原子/残基进行建模。

需要注意的是，`pdb2gmx` 不是魔法，它不能生成所有分子的拓扑结构，仅限于力场定义的残基（*.rtp 文件，通常包括蛋白质、核酸以及有限的辅助因子，如 NAD 和 ATP）。

现在已经移除了结晶水，并且已经确定所有必要的原子都存在，且 pdb 文件只包含蛋白质原子，将其作为 GROMACS 的第一个模块 `pdb2gmx` 的输入。`pdb2gmx` 用来生成三个文件：

1. 分子的拓扑结构
2. 位置约束文件
3. 后处理结构文件

拓扑结构文件（topol.top）包含模拟中定义分子所需的所有信息。该信息包括非键参数（原子类型和价态）和键参数（键、角度和二面角）。使用如下命令执行 `pdb2gmx`：

```sh
gmx pdb2gmx -f 1AKI_clean.pdb -o 1AKI_processed.gro -water spce
```

然后 gmx 会提示选择一个力场：

```sh
Select the Force Field:

From '/usr/local/share/gromacs/top':

 1: AMBER03 protein, nucleic AMBER94 (Duan et al., J. Comp. Chem. 24, 1999-2012, 2003)
 2: AMBER94 force field (Cornell et al., JACS 117, 5179-5197, 1995)
 3: AMBER96 protein, nucleic AMBER94 (Kollman et al., Acc. Chem. Res. 29, 461-469, 1996)
 4: AMBER99 protein, nucleic AMBER94 (Wang et al., J. Comp. Chem. 21, 1049-1074, 2000)
 5: AMBER99SB protein, nucleic AMBER94 (Hornak et al., Proteins 65, 712-725, 2006)
 6: AMBER99SB-ILDN protein, nucleic AMBER94 (Lindorff-Larsen et al., Proteins 78, 1950-58, 2010)
 7: AMBERGS force field (Garcia & Sanbonmatsu, PNAS 99, 2782-2787, 2002)
 8: CHARMM27 all-atom force field (CHARM22 plus CMAP for proteins)
 9: GROMOS96 43a1 force field
10: GROMOS96 43a2 force field (improved alkane dihedrals)
11: GROMOS96 45a3 force field (Schuler JCC 2001 22 1205)
12: GROMOS96 53a5 force field (JCC 2004 vol 25 pag 1656)
13: GROMOS96 53a6 force field (JCC 2004 vol 25 pag 1656)
14: GROMOS96 54a7 force field (Eur. Biophys. J. (2011), 40,, 843-856, DOI: 10.1007/s00249-011-0700-9)
15: OPLS-AA/L all-atom force field (2001 aminoacid dihedrals)
```

力场的选择非常重要。这里我们选择 all-atom OPLS 力场，因此输入 15，然后回车。`pdb2gmx` 有很多选项，常用的包括：

- `-ignh`：忽略 PDB 文件中的氢原子，对 NMR 结构特别有用。否则，如果有氢原子，则氢原子格式必须满足 GROMACS 力场。由于存在不同的惯例，因此处理 H 原子可能很令人头疼。如果需要保留初始 H 原子坐标，但需要重命名，则可以使用 Linux 的 `sed` 命令。
- `-ter`：以交互的方式为 N 端和 C 端分配电荷状态。
- `-inter`：以交互的方式为 Glu, Asp, Lys, Arg 和 His 分配电荷状态；选择与二硫键相关的 Cys。

运行后，会生成三个文件：1AKI_processed.gro，posre.itp 和 topol.top：

- 1AKI_processed.gro 是 GROMACS 格式的结构文件，包含力场中定义的所有原子；
- topol.top 是系统拓扑文件；
- posre.itp 包含用于限制重原子位置的信息。

最后说明一点，许多用户以为 .gro 文件是必须的，这不对。GROMACS 可以处理许多不同的文件格式，.gro 只是写入坐标文件命令的默认选项。.gro 格式非常紧凑，但精度有限。如果你喜欢用 PDB 格式，只需要将 .pdb 作为输出文件的扩展名。`pdb2gmx` 的目的是生成符合力场的拓扑文件，输出的结构文件只是其副产物。

### 检查拓扑文件

让我们看看输出的拓扑文件 `topl.top` 里面有什么。使用纯文本编辑器打开。跳过注释行（以 ; 开头），第一行为：

```txt
#include "oplsaa.ff/forcefield.itp"
```

这一行调用了 OPLS-AA 力场的参数。它在文件开头，表明后续所有参数都源自此力场。下一个重要的内容是 `[ moleculetype ]`，如下：

```txt
[ moleculetype ]
; Name            nrexcl
Protein_chain_A     3
```

其中：

- "Protein_chain_A" 为分子名称，说明这个蛋白在 PDB 文件中被标记为 chain A。
- 3 表示成键邻居。

接下来定义蛋白的原子信息。如下：

```top
[ atoms ]
;   nr       type  resnr residue  atom   cgnr     charge       mass  typeB    chargeB      massB
; residue   1 LYS rtp LYSH q +2.0
     1   opls_287      1    LYS      N      1       -0.3    14.0027
     2   opls_290      1    LYS     H1      1       0.33      1.008
     3   opls_290      1    LYS     H2      1       0.33      1.008
     4   opls_290      1    LYS     H3      1       0.33      1.008
     5  opls_293B      1    LYS     CA      1       0.25     12.011
     6   opls_140      1    LYS     HA      1       0.06      1.008
```

这些信息的含义：

- nr: 原子编号
- type: 原子类型
- resnr: 氨基酸残基编号
- residue: 氨基酸残基名称

> 在 PDB 文件中该残基为 "LYS"，在 .rtp 中 "LYSH" 表示质子化的 LYS，在中性 pH 下 LYS 的主要存在形式。

- atom: 原子名称
- cgnr: 电荷组编号

> 电荷组（charge group） 定义整数的电荷，用于辅助加速计算。

- charge: 电荷
- mass: 质量
- typeB, chargeB, massB: 用于自由能扰动。

后面还有 `[ bonds ]`, `[ pairs ]`, `[ angles ]` 以及 `[ dihedrals ]`。分别是键、键角和二面角等。

该文件的其余部分涉及其它的一些拓扑，从位置约束开始。pdb2gmx 生成的 "posre.itp" 文件定义了一些力常量，用于平衡过程中保持原子的位置。

```c
; Include Position restraint file
#ifdef POSRES
#include "posre.itp"
#endif
```

这部分意味着 "Protein_chain_A" 定义的结束。文件余下部分定义其它分子，以及系统级描述。下一个分子（默认为溶剂），

## 定义溶剂盒子

![](images/2022-05-26-16-14-45.png)

下面我们将模拟一个简单的水系统。在不同溶剂中模拟蛋白质和其它分子也是可能额，前提是所涉及的分子都有定义良好的参数。

定义溶剂盒子分两步：

1. 使用 `editconf` 定义盒子尺寸
2. 使用溶剂模块将盒子装满水

在本教程中，为了简化，我们使用一个简单的立方体作为盒子。等你对盒子类型更加熟悉，我强烈推荐灵性的十二面体的盒子，因为它的体积大约是相同周期距离的立方体盒子的 71%，因此可以减少用来溶解蛋白质的水分子数量。

首先，用 editconf 定义盒子：

```sh
gmx editconf -f 1AKI_processed.gro -o 1AKI_newbox.gro -c -d 1.0 -bt cubic
```

上面的命令将蛋白质放在盒子中心 `-c`，使其距离盒子边缘至少 1.0 nm 远 `-d 1.0`。盒子类型定义为立方体 `-bt cubic`。到盒子边缘的距离是一个很重要的参数。由于我们将使用周期性边界条件，因此必须满足最低图像约定（minimum image convention）。即蛋白质应该永远看不到它的周期图像，否则计算的力有问题。将溶质-盒子距离指定为 1.0 nm 意味着蛋白质的任意两个周期图像之间至少有 2 nm。该距离足以满足模拟常用的任何截断方案。

定义好盒子，我们用溶剂（水）填充它。使用 `solvate` 完成溶剂化：

```sh
gmx solvate -cp 1AKI_newbox.gro -cs spc216.gro -o 1AKI_solv.gro -p topol.top
```

蛋白质配置 `-cp` 包含在上一步 `editconf` 的输出文件 1AKI_newbox.gro 中，而溶剂配置 `-cs` 包含在 GROMACS 安装文件中。这里我们使用 spc216.gro，这是一个同通用的平衡三点溶剂模型。spc216.gro 可作为 SPC, SPC/E 或 TIP3P 水的溶剂配置，因为它们都是三点水模型。输出为 1AKI_solv.gro，并告诉 `solvate` 拓扑文件位 topol.top，这样它就可以修改拓扑文件。运行后可以看到 topol.top 文件中 `[ molecules ]` 的改变：

```top
[ molecules ]
; Compound  #mols
Protein_A       1 
SOL         10832
```

`solvate` 将添加的溶剂分子个数写入了拓扑文件。需要注意的是，如果使用非水溶剂，则不写入拓扑文件，这个功能是与水硬编码绑定的。

## 添加离子

![](images/2022-05-26-17-01-03.png)

现在已经有了一个带电蛋白质的溶剂化系统，pdb2gmx 的结果告诉我们，该蛋白质的净电荷为 +8e （根据氨基酸组成）。如果你错过了命令行信息，也可以在 topol.top 文件的 `[ atoms ]` 的最后一行看到，显示为 "qtot 8"。由于生命系统不可能是带电的，因此我们必须向系统中添加离子。

添加离子的工具为 `genion`。`genion` 读取拓扑文件，并以用户指定的离子替换水分子。输入为运行输入文件 .tpr，该文件由 GROMACS grompp 模块生成，后续我们运行第一次模拟时也会用到。grompp 的功能是处理坐标文件和拓扑文件，生成原子级的输入文件 .tpr。tpr 为文件包含系统中所有原子的所有参数。

要使用 grompp 生成 tpr 文件，还需要一个输入文件，mdp 文件；grompp 将使用 mdp 文件中的参数与坐标信息、拓扑信息一起生成 tpr 文件。

.mdp 文件通常用于运行能量最小化和 MS 模拟，但在这里，仅用 mdp 文件生成系统的原子描述。下面是一个 mdp 文件 ions.mdp 示例：

```mdp
; ions.mdp - used as input into grompp to generate ions.tpr
; Parameters describing what to do, when to stop and what to save
integrator  = steep         ; Algorithm (steep = steepest descent minimization)
emtol       = 1000.0        ; Stop minimization when the maximum force < 1000.0 kJ/mol/nm
emstep      = 0.01          ; Minimization step size
nsteps      = 50000         ; Maximum number of (minimization) steps to perform

; Parameters describing how to find the neighbors of each atom and how to calculate the interactions
nstlist         = 1         ; Frequency to update the neighbor list and long range forces
cutoff-scheme	= Verlet    ; Buffered neighbor searching 
ns_type         = grid      ; Method to determine neighbor list (simple, grid)
coulombtype     = cutoff    ; Treatment of long range electrostatic interactions
rcoulomb        = 1.0       ; Short-range electrostatic cut-off
rvdw            = 1.0       ; Short-range Van der Waals cut-off
pbc             = xyz       ; Periodic Boundary Conditions in all 3 dimensions
```

mdp 文件可以包含任何允许的参数组合。我通常使用能量最小化脚本，因为它比较基础，不涉及复杂的参数组合。要注意的是，本教程提供的文件仅用于 OPLS-AA 力场。对于其它力场，尤其是非键相互作用，参数会不同。

用如下命令生成 tpr 文件：

```sh
gmx grompp -f ions.mdp -c 1AKI_solv.gro -p topol.top -o ions.tpr
```

已经有二进制的原子级的系统描述文件 ions.tpr。将其传递给 `genion`：

```sh
gmx genion -s ions.tpr -o 1AKI_solv_ions.gro -p topol.top -pname NA -nname CL -neutral
```

## 参考

- http://www.mdtutorials.com/gmx/lysozyme/index.html
