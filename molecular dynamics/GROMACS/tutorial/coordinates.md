# restraint, constraint 和 freeze

## 简介

gromacs 里面人为固定坐标有三大类方式：restraint、constraint 和 freeze，有各自的特点。

## 限制（restraint）

包括位置限制(即正式 MD 前首先要进行的限制性动力学)、角度限制、二面角限制、方向限制和距离限制。限制的特点是可以让被限制的东西在一定范围内运动，而非彻底固定住，实际上就是施加一个谐振势来限制其移动。

**位置限制**就不必说了，`posre.itp` 里面 `[ position_restraints ]` 定义的就是，默认相对于最初位置进行限制。

**角度限制**包括两类:

- 一类是两对原子间角度的限制，用 `[ angle_restraints ]` 来指定，例如：

```bash
[ angle_restraints ]
; i   j    k    l    type   theta0     fc     multiplicity
651 1211 1683 1211    1      67.0     1500         1
```

说明限制 651-1211 与 1683-1211 原子对之间的夹角在 67 度附近，力常数为1500。type无用。

- 另一类角度限制包括一对原子与 z 轴夹角角度的限制，用 `[ angle_restraints_z ]` 指定，例如：

```bash
[ angle_restraints_z ]
; #1 #2  type  theta0    fc     multiplicity
22  45     1     90      500         2
```

说明限制 22 与 45 号原子的连线与z轴垂直，力常数是 500，多重性是2，使得 90度夹角时候限制势能最低，0 和 180 度时最高。type无用。

**二面角限制**使用 `[ dihedral_restraints ]` 段落来定义，实际上improper项就是用二面角限制方式限制的。例如

```bash
[ dihedral_restraints ]
;   i    j     k    l    type  label  phi  dphi  kfac  power
    5    7     9    15     1      1  180     0     1      2
```

被限制的是 5,7,9,15 原子组成的二面角，type总是1，label 没用，phi 是参考角，dphi 是超过参考角多少度开始使用限制势，power没用。kfac 乘上 mdp中的dihre_fc 将作为限制势力常数。

最后在mdp中加入例如：

```bash
dihre               =  simple
dihre_fc            =  100
dihre_tau           =  0.0
nstdihreout         =  50
```

**距离限制**在 `[ distance_restraints ]` 里面定义，比如

```bash
[ distance_restraints ]
; i j type index type low up1 up2 fac
10 16 1 0 1 0.0 0.3 0.4 1.0
```

type总是1，index是计算的顺序，如果几个项index都一样，比如10-28和10-46，就同时计算。势能图见gmx3.3手册p60，low,up1,up2分别指图上的r0,r1,r2，可见原子间距离在low至up1区间内是不受限制的，这种方式可以达成NMR限制。fac是指这个因子乘上mdp中disre_fc作为限制势力常数。
也可以定义两个原子在[ bonds ]里用bond type 6，就是个和普通键一样的谐振子势，但是这两个原子间被认为没有键连。

应当注意以上限制方式中[]段落应当紧接着写在被限制分子的.itp后面（或者说对应的[ moleculetype ]后面），这样程序才知道其中的原子编号指的是哪种分子中的原子。

## 参考

- http://sobereva.com/10
