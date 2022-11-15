# gmx grompp

- [gmx grompp](#gmx-grompp)
  - [说明](#说明)
  - [选项](#选项)
    - [输入文件选项](#输入文件选项)
    - [输入/输出文件](#输入输出文件)
    - [输出文件选项](#输出文件选项)
    - [其它选项](#其它选项)
  - [参考](#参考)

2022-05-27, 09:57
****

```sh
gmx grompp  [-f [<.mdp>]] [-c [<.gro/.g96/...>]] [-r [<.gro/.g96/...>]]
            [-rb [<.gro/.g96/...>]] [-n [<.ndx>]] [-p [<.top>]]
            [-t [<.trr/.cpt/...>]] [-e [<.edr>]] [-qmi [<.inp>]]
            [-ref [<.trr/.cpt/...>]] [-po [<.mdp>]] [-pp [<.top>]]
            [-o [<.tpr>]] [-imd [<.gro>]] [-[no]v] [-time <real>]
            [-[no]rmvsbds] [-maxwarn <int>] [-[no]zero] [-[no]renum]
```

## 说明

GROMAC 预处理器 `gmx grompp` (gromacs preprocessor) 读取分子拓扑文件，检查文件的有效性，然后将拓扑从分子描述扩展为原子描述。拓扑文件包含分子类型和分子数量的信息，预处理器根据需要复制每个分子。对分子类型的数量没有限制。键和键角可以分别转换为氢和重原子的约束。然后读取坐标文件，根据需要还可以从 Maxwellian 分布生成速度。`gmx grompp` 还读取 [gmx mdrun](gmx_mdrun.md) 的参数，如 MD 步数、时间步、截止点（cut-off）等。最终生成一个二进制文件，作为 MD 程序的唯一输入文件。

`gmx grompp` 使用拓扑文件中的原子名称。坐标文件（`-c` 选项）中的原子名称只是用来验证拓扑文件中的原子名称，当不匹配时发出警告。需要注意的是，原子名称与模拟无关，只是用原子类型来生成相互作用参数。

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

这些语句在拓扑文件中的功能可以使用 [.mdp](../5_参考手册/7_file_formats.md#mdp) 文件中的两个 flag 来调整：

```c
define = -DVARIABLE1 -DVARIABLE2
include = -I/home/john/doe
```

要了解更多相关知识，可以学习一下 C 语言。可以使用 `-pp` flag 输出预处理的拓扑文件，以便验证其内容。

在使用位置约束时，带有约束坐标的文件使用 `-r` 选项提供（可以与 `-c` 选项提供的文件相同）。对于自由能计算，B 拓扑的单独参考坐标可以用 `-rb` 选项提供，否则它们将与 A 拓扑的参考坐标一样。

初始坐标可以使用 `-t` 选项从轨迹中读取。如果不使用 `-time` 选项，就直接读取最后一帧的坐标和速度。只有在缺失该信息时，才使用 `-c` 文件中的坐标，即该选项优先级更高。当 mdp 文件中 `gen_vel = yes` 时，不使用速度值。可以用 `-e` 选项指定能量文件，以读取 Nose-Hoover 和 Parrinello-Rahman 耦合变量。

通过 `-t` 指定 checkpoint 文件，`gmx grompp` 可以重启模拟（保持连续性）。不过，对于简单地更改运行时间步来延长运行，使用 `gmx convert-tpr` 比 `gmx grompp` 更方便。可以使用 `-cpi` 选项提供旧的 checkpoing 文件给 [gmx mdrun](gmx_mdrun.md)。如果你想更改 ensemble 或频率之类的，则建议使用 `-t` 选项指定 checkpoint 文件，使用 `-f` 指定新的 [mdp](../5_参考手册/7_file_formats.md#mdp) 文件。事实上，保留 ensemble 依然需要用 `-cpi` 选项提供 checkpoint 文件给 [gmx mdrun](gmx_mdrun.md)。

默认删除所有虚拟点构造导致的恒定能量的键合相互作用。如果该恒定能量不为零，则会导致总能量的偏移。关闭 `-rmvsbds` 可以保留所有键合相互作用。另外，虚拟点构造导致的常量距离约束都会被删除。如果有任何涉及虚拟点约束，直接报错。

为了验证运行输入文件，要注意屏幕上的所有警告信息，根据需要进行修改。同时要查看 `mdout.mdp` 文件，该文件包含注释行以及 `gmx grompp` 读取的输入。如果有疑问，可以使用 `-debug` 选项运行 `gmx grompp`，该选项会在 `grompp.log` 文件中提供更多信息。可以使用 `gmx dump` 查看运行输入胡文件，使用 `gmx check` 比较两个运行输入文件。

可以用 `-maxwarn` 选项覆盖由 `gmx grompp` 输出的警告信息。建议用户在使用此选项屏蔽警告信息前，仔细阅读警告信息，确定不影响结果。

## 选项

### 输入文件选项

|选项|默认值|说明|
|---|---|---|
|`-f [<.mdp>] (grompp.mdp)`||MD 参数文件|
|`-c` [<.gro/.g96/…>]|conf.gro|结构文件：gro g96 pdb brk ent esp tpr|
|`-r [<.gro/.g96/…>] (restraint.gro)`|yes|结构文件：gro g96 pdb brk ent esp tpr|
|`-rb [<.gro/.g96/…>] (restraint.gro)`|yes|结构文件：gro g96 pdb brk ent esp tpr|
|`-n [<.ndx>] (index.ndx)`|yes|索引文件|
|`-p [<.top>] (topol.top)`||拓扑文件|
|`-t` [<.trr/.cpt/…>]|traj.trr)|全精度轨迹：trr cpt tng|
|`-e [<.edr>] (ener.edr)`|yes|能量文件|
|`-qmi [<.inp>] (topol-qmmm.inp)`|yes|QM 程序的输入文件|

### 输入/输出文件

|选项|可选|说明|
|---|---|---|
|`-ref [<.trr/.cpt/…>] (rotref.trr)`|yes|全精度轨迹：trr cpt tng|

### 输出文件选项

|选项|可选|说明|
|---|---|---|
|`-po [<.mdp>] (mdout.mdp)`||带 MD 参数的 grompp 输入文件|
|`-pp [<.top>] (processed.top)`|yes|拓扑文件|
|`-o [<.tpr>] (topol.tpr)`||可移植 xdr 运行输入文件|
|`-imd [<.gro>] (imdgroup.gro)`|yes|Gromos-87 格式的坐标文件|

### 其它选项

|选项|说明|
|---|---|
|`-[no]v (no)`|Be loud and noisy|
|`-time <real> (-1)`|Take frame at or first after this time.|
|`-[no]rmvsbds (yes)`|Remove constant bonded interactions with virtual sites|
|`-maxwarn <int> (0)`|Number of allowed warnings during input processing. Not for normal use and may generate unstable systems|
`-[no]zero (no)`|Set parameters for bonded interactions without defaults to zero instead of generating an error|
|`-[no]renum (yes)`|Renumber atomtypes and minimize number of atomtypes|

## 参考

- https://manual.gromacs.org/current/onlinehelp/gmx-grompp.html
