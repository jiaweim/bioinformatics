# gmx pdb2gmx

***

## 简介

```python
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

`gmx pdb2gmx` 读取 .pdb (或 .gro)文件和数据库文件，向分子中添加氢，生成 GROMACS 格式坐标（或 .pdb 格式），以及 GROMACS 格式的拓扑。这些文件随后可以用来生成运行输入文件。

`gmx pdb2gmx` 会在当前工作目录的 `<forcefield>.ff` 子目录、GROMACS 的 `GMXLIB` 环境变量路径搜索 `forcefield.itp` 力场文件。力场的选择默认是交互式的，但也可以使用 `-ff` 选项使用力场 short name 直接指定力场，这样 `gmx pdb2gmx` 只需查找相应力场的 `<forcefield>.ff` 目录。



## 选项

**IO 选项**

|选项|默认|说明|
|---|---|---|
|`-f`|protein.pdb|输入结构文件|
|`-o`|conf.gro|输出结构文件|
|`-p`|topol.top|输出拓扑文件|
|`-i`|posre.itp|输出位置约束文件|
|`-n`|index.ndx|输出索引文件|

**其他选项**

|选项|默认|说明|
|---|---|---|
|`-[no]ignh`|忽略坐标文件中的氢原子|
|`-water`|指定水模型：select, none, spc, spce, tip3p, tip4p, tip5p, tips3p|
|`-[no]inter`|将接下来的 8 个选项设置为交互式的|
|`-[no]ter`|为 N 端和 C 端交互式分配电荷|
|`-ff`|设置力场|

## 参考

- https://manual.gromacs.org/documentation/current/onlinehelp/gmx-pdb2gmx.html
