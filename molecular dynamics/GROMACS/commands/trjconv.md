# gmx trjconv

***

## 简介

```python
gmx trjconv [-f [<.xtc/.trr/...>]] [-s [<.tpr/.gro/...>]] [-n [<.ndx>]]
            [-fr [<.ndx>]] [-sub [<.ndx>]] [-drop [<.xvg>]]
            [-o [<.xtc/.trr/...>]] [-b <time>] [-e <time>]
            [-tu <enum>] [-[no]w] [-xvg <enum>] [-skip <int>]
            [-dt <time>] [-[no]round] [-dump <time>] [-t0 <time>]
            [-timestep <time>] [-pbc <enum>] [-ur <enum>]
            [-[no]center] [-boxcenter <enum>] [-box <vector>]
            [-trans <vector>] [-shift <vector>] [-fit <enum>]
            [-ndec <int>] [-[no]vel] [-[no]force] [-trunc <time>]
            [-exec <string>] [-split <time>] [-[no]sep]
            [-nzero <int>] [-dropunder <real>] [-dropover <real>]
            [-[no]conect]
```

`gmx trjconv` 可以通过多种方式转换轨迹文件：

- 从一种格式转换为另一种格式
- 选择原子子集
- 更改周期性表示
- 将多聚体分子保持在一起

选项 `-pbc` 设置周期性条件处理的类型：

- `mol` 将分子的质心放在 box 里，需要同时使用 `-s` 选项指定 tpr 文件
- `res` 将残基的质心放在 box 里
- `atom` 将所有原子放在 box 里
- 

`-center` 选项将系统放在 box 中心。用户可以选择用于确定几何中心的 group。

## 选项

**IO 选项**

|选项|默认|说明|
|---|---|---|
|`-f` [<.xtc/.trr/…>]|traj.xtc|轨迹文件: xtc trr cpt gro g96 pdb tng|
|`-s` [<.tpr/.gro/…>]|topol.tpr|Structure+mass(db): tpr gro g96 pdb brk ent|
|`-n` [<.ndx>]|index.ndx|Index 文件|
|`-fr` [<.ndx>]|frames.ndx|Index 文件|
|`-o` [<.xtc/.trr/…>]|trajout.xtc|轨迹文件: xtc trr gro g96 pdb tng|

## 参考

- https://manual.gromacs.org/current/onlinehelp/gmx-trjconv.html
