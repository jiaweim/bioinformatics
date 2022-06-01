# Molecular dynamics simulation

## 准备力场

下载 CHARMM36 力场文件：

http://mackerell.umaryland.edu/charmm_ff.shtml#gromacs

下载的 charmm36-jul2021.ff.tgz 文件，放到 gromacs top 目录：

`/usr/local/share/gromacs/top`

解压:

```sh
tar -xzvf charmm36-jul2021.ff.tgz
```

> 这个力场中没有 CL 离子

换成 charmm36-feb2021.ff 力场

## TLR-2

1. 准备拓扑

```sh
gmx pdb2gmx -f TLR2.pdb -o TLR2_processed.gro -ignh
```

`-ignh` 忽略氢原子，避免后续步骤出错。

弹窗选择：

- 选择 CHARMM36 力场
- 选择 TIP3P_CHARMM 水模型

Charmm36-jul2021 force field and the tip3p water model are used

显示总电荷 39.000 e。

2. 定义溶剂盒子

```sh
gmx editconf -f TLR2_processed.gro -o newbox.gro -bt dodecahedron -d 1.0 -c
```

3. 添加溶剂

```sh
gmx solvate -cp newbox.gro -cs spc216.gro -p topol.top -o solv.gro
```

4. 添加离子

使用推荐的 ions.mdp 参数，生成 tpr 文件：

```sh
gmx grompp -f ions.mdp -c solv.gro -p topol.top -o ions.tpr
```

将 ions.tpr 文件给 `genion` 命令填充离子：

```sh
gmx genion -s ions.tpr -o solv_ions.gro -p topol.top -pname NA -nname CL -neutral
```

5. 能量最小化

使用 minim.mdp 参数，生成 tpr 文件：

```sh
gmx grompp -f minim.mdp -c solv_ions.gro -p topol.top -o em.tpr
```

## TLR4

1. 准备拓扑

```sh
gmx pdb2gmx -f TLR4.pdb -o TLR4_processed.gro -ignh
```

`-ignh` 忽略氢原子，避免后续步骤出错。

弹窗选择：

- 选择 CHARMM36 力场
- 选择 TIP3P_CHARMM 水模型

Charmm36-jul2021 force field and the tip3p water model are used

显示总电荷 39.000 e。

2. 定义溶剂盒子

```sh
gmx editconf -f TLR4_processed.gro -o newbox.gro -bt dodecahedron -c -d 1.0
```

3. 添加溶剂

```sh
gmx solvate -cp newbox.gro -cs spc216.gro -p topol.top -o solv.gro
```

4. 添加离子

使用推荐的 ions.mdp 参数，生成 tpr 文件：

```sh
gmx grompp -f ions.mdp -c solv.gro -p topol.top -o ions.tpr
```

将 ions.tpr 文件给 `genion` 命令填充离子：

```sh
gmx genion -s ions.tpr -o solv_ions.gro -p topol.top -pname NA -nname CL -neutral
```

5. 能量最小化

使用 minim.mdp 参数，生成 tpr 文件：

```sh
gmx grompp -f minim.mdp -c solv_ions.gro -p topol.top -o em.tpr
```

## TLR3

1. 准备拓扑

```sh
gmx pdb2gmx -f tlr3.pdb -o tlr3_processed.gro -ignh
```

`-ignh` 忽略氢原子，避免后续步骤出错。

弹窗选择：

- 10: CHARMM36 all-atom force field (July 2020)
- 1: TIP3P       TIP 3-point, recommended, by default uses CHARMM TIP3 with LJ on H

总电荷：Total charge 36.000 e

2. 定义溶剂盒子

```sh
gmx editconf -f tlr3_processed.gro -o newbox.gro -bt dodecahedron -c -d 1.0
```

gmx editconf -f tlr3_processed.gro -o newbox.gro -bt octahedron -c -d 1.0

3. 添加溶剂

```sh
gmx solvate -cp newbox.gro -cs spc216.gro -p topol.top -o solv.gro
```

4. 添加离子

使用推荐的 ions.mdp 参数，生成 tpr 文件：

```sh
gmx grompp -f ions.mdp -c solv.gro -p topol.top -o ions.tpr
```

将 ions.tpr 文件给 `genion` 命令填充离子：

```sh
gmx genion -s ions.tpr -o solv_ions.gro -p topol.top -pname NA -nname CL -neutral
```

Replacing 36 solute molecules in topology file (topol.top)  by 0 NA and 36 CL ions.

添加了 36 个 CL 离子来中和电荷。

5. 能量最小化

使用 em.mdp 参数，生成 tpr 文件：

```sh
gmx grompp -f em.mdp -c solv_ions.gro -p topol.top -o em.tpr
```
