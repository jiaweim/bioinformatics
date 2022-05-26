# 命令行参考

- [命令行参考](#命令行参考)
  - [gmx grompp](#gmx-grompp)
  - [gmx pdb2gmx](#gmx-pdb2gmx)

2022-05-26, 08:42
***

## gmx grompp

```sh
gmx grompp  [-f [<.mdp>]] [-c [<.gro/.g96/...>]] [-r [<.gro/.g96/...>]]
            [-rb [<.gro/.g96/...>]] [-n [<.ndx>]] [-p [<.top>]]
            [-t [<.trr/.cpt/...>]] [-e [<.edr>]] [-qmi [<.inp>]]
            [-ref [<.trr/.cpt/...>]] [-po [<.mdp>]] [-pp [<.top>]]
            [-o [<.tpr>]] [-imd [<.gro>]] [-[no]v] [-time <real>]
            [-[no]rmvsbds] [-maxwarn <int>] [-[no]zero] [-[no]renum]
```

`gmx grompp` (gromacs preprocessor) 读取分子拓扑文件，检查文件的有效性，然后将拓扑从分子描述扩展为原子描述。拓扑文件包含分子类型和分子数量的信息，预处理器根据需要复制恶分子。分子类型的数量没有限制。键和键角可以分别转换为氢和重原子的约束。然后读取坐标文件，如果需要可以从 Maxwellian 分布生成速度。`gmx grompp` 还读取 `gmx mdrun` 的参数，如 MD 步数、时间步、截止点（cut-off）等。最终生成一个二进制文件，它可以作为 MD 程序的唯一输入文件。

`gmx grompp` 使用拓扑文件中的原子名称。坐标文件（`-c` 选项）中的原子名称只是用来验证拓扑文件中的原子名称，当不匹配时发出警告。注意，原子名称与模拟无关，只是用原子类型来生成相互作用参数。

`gmx grompp` 使用内置的预处理器解析 includes, macros 等。该预处理器支持如下关键字：

```c
#ifdef VARIABLE
#ifndef VARIABLE
#else
#endif
#define VARIABLE
#undef VARIABLE
#include "filename"
#include <filename>
```

这些语句在拓扑文件中的功能使用 [.mdp](../5_参考手册/7_file_formats.md#mdp) 文件中的两个 flag 来调整：

```c
define = -DVARIABLE1 -DVARIABLE2
include = -I/home/john/doe
```

要了解更多相关知识，可以学习一下 C 语言。使用 `-pp` flag 输出预处理的拓扑文件，以便验证其内容。

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
