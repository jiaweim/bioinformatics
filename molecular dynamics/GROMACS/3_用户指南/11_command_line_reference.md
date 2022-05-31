# 命令行参考

- [命令行参考](#命令行参考)
  - [简介](#简介)
  - [命令](#命令)
  - [gmx pdb2gmx](#gmx-pdb2gmx)
  - [参考](#参考)

2022-05-26, 08:42
***

## 简介

GROAMCS 包含许多用于准备、运行和分析分子动力学模拟的工具。它们都作为 `gmx` 包的一部分，并使用类似 `gmx grompp` 的命令运行。

如果你安装的 MPI 版本的 GROMACS，则默认情况下 gmx 的命令为 `gmx_mpi`，对应命令都要相应调整。

## 命令

|命令|功能|
|---|---|
|[gmx mdrun](../commands/gmx_mdrun.md)|进行模拟、简正分析或能量最小化|

- [gmx grompp](../commands/gmx_grompp.md)


## gmx pdb2gmx

```sh
gmx pdb2gmx [-f [<.gro/.g96/...>]] [-o [<.gro/.g96/...>]] [-p [<.top>]]
            [-i [<.itp>]] [-n [<.ndx>]] [-q [<.gro/.g96/...>]]
            [-chainsep <enum>] [-merge <enum>] [-ff <string>]
            [-water <enum>] [-[no]inter] [-[no]ss] [-[no]ter]
            [-[no]lys] [-[no]arg] [-[no]asp] [-[no]glu] [-[no]gln]
            [-[no]his] [-angle <real>] [-dist <real>] [-[no]una]
            [-[no]ignh] [-[no]missing] [-[no]v] [-posrefc <real>]
            [-vsite <enum>] [-[no]heavyh] [-[no]deuterate]
            [-[no]chargegrp] [-[no]cmap] [-[no]renum] [-[no]rtpres]
```

|选项|说明|
|---|---|
|-f [<.gro/.g96/. . . >] (protein.pdb)|输入结构文件|
|-o [<.gro/.g96/. . . >] (conf.gro)|输出结构文件|

其它选项：

|选项|说明|
|---|---|
|`-water <enum> (select)`|要使用的水模型，支持：select, none, spc, spce, tip3p, tip4p, tip5p, tips3p|
|`-[no]ignh`|忽略坐标文件中的氢原子|

## 参考

- https://manual.gromacs.org/current/user-guide/cmdline.html
