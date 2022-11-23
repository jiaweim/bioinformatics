# gmx trjconv

***

## 简介

```python
gmx trjconv [-f [<.xtc/.trr/...>]]
            [-s [<.tpr/.gro/...>]] 
            [-n [<.ndx>]]
            [-fr [<.ndx>]] [-sub [<.ndx>]] [-drop [<.xvg>]]
            [-o [<.xtc/.trr/...>]] 
            [-b <time>] [-e <time>]
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

`trjconv` 用于转换和操控轨迹文件。

`gmx trjconv` 可以通过多种方式转换轨迹文件：

- 从一种格式转换为另一种格式
- 选择原子子集
- 更改周期性表示方式
- 将多聚体分子保持在一起
- 将原子在盒子内居中
- 将原子叠合到参考结构
- 减少帧数
- 改变每帧的时间戳(`‐t0` 和 `‐timestep`)
- 根据索引文件中的信息把轨迹分割为小的子轨迹, 这样对子轨迹的后续分析就变为对团簇的分析. 需要使用选项 `‐sub`。处理时假定索引文件中的条目为帧数, 并将把索引文件中的每个组输出为单独的轨迹.
- 选取某个量处于一定范围内的帧, 这个量由 `.xvg` 文件给出

`gmx trjconv` 还能将多个轨迹文件拼合起来.

选项 `-pbc` 设置周期性边界条件处理类型：

- `mol` 将分子的质心放在 box 里，需要同时使用 `-s` 选项指定 tpr 文件
- `res` 将残基的质心放在 box 里
- `atom` 将所有原子放在 box 里
- 

`-center` 将系统放在 box 中心。用户可以选择用于确定几何中心的 group。

## 选项

**IO 选项**

|选项|默认|说明|
|---|---|---|
|`-f` [<.xtc/.trr/…>]|traj.xtc|轨迹文件: xtc trr cpt gro g96 pdb tng|
|`-s` [<.tpr/.gro/…>]|topol.tpr|Structure+mass(db): tpr gro g96 pdb brk ent|
|`-n` [<.ndx>]|index.ndx|Index 文件|
|`-fr` [<.ndx>]|frames.ndx|Index 文件|
|`-o` [<.xtc/.trr/…>]|trajout.xtc|轨迹文件: xtc trr gro g96 pdb tng|

**控制选项**

|选项|默认值|说明|
|---|---|---|
|‐b|0|从轨迹文件中读取的第一帧（ps）|
|‐e|0|从轨迹文件中读取的最后一帧（ps）|
|‐tu|ps|时间值的单位: fs, ps, ns, us, ms, s|
|`‐[no]w`|no|程序结束后查看输出的 .xvg, .xpm, .eps和.pdb文件|
|`‐xvg <enum>`|xmgrace|xvg 绘图格式: xmgrace, xmgr, none|
|`‐skip <int>`|1|每 nr 帧输出一次|
|‐dt|0|只使用t除以dt的余数等于第一帧时间(ps)的帧, 即两帧之间的时间间隔|
|‐[no]round|no|将测量四舍五入至最接近的皮秒|
|`‐dump <time>`|‐1|重复最接近指定时间(ps)的帧|
|‐t0 <time> 0 起始时间(ps) (默认: 不改变)|
|‐timestep
<time> 0 更改输入帧之间的时间步长(ps)
‐pbc <enum> none PBC处理方式(完整说明见帮助文件): none, mol, res, atom, nojump,
cluster, whole
‐ur <enum> rect 单元晶胞的表示方式: rect, tric, compact
‐[no]center no 将盒子内的原子居中
‐boxcenter
<enum> tric ‐pbc 和‐center 的中心: tric, rect, zero
‐box <vector> 0 0 0 新立方盒子的尺寸(默认读取自输入文件)
‐trans <vector> 0 0 0 所有坐标将被平移 trans. 适用于与‐pbc mol ‐ur compact 组合使用.
‐shift <vector> 0 0 0 所有坐标将被偏移 framenr*shift
‐fit <enum> none
将分子叠合到结构文件中的参考结构.
可用选项: none, rot+trans, rotxy+transxy, translation, transxy,
progressive
‐ndec <int> 3 输出.xtc 和.gro 时, 小数位的精度
‐[no]vel yes 如果可能, 读取并输出速度
‐[no]force no 如果可能, 读取并输出力
‐trunc <time> ‐1 在此时间(ps)后截断输入轨迹文件
‐exec <string> 对每个输出帧执行命令, 帧号作为命令的参数
‐split <time> 0 当t除以split的余数等于第一帧时间(ps)时开始输出新文件
‐[no]sep no 将每一帧输出为独立的.gro , .g96 或.pdb 文件
‐nzero <int> 0 如果设置‐sep , 文件编号的数字位数, 如果需要, 数字签名会添加0
‐dropunder
<real> 0 舍弃低于此值的所有帧
|‐dropover <real>|0|舍弃高于此值的所有帧|
|`‐[no]conect`|no|当输出 `.pdb` 文件时增加连接记录。对于非标准分子，例如粗粒化分子的可视化会有用|

## 参考

- https://manual.gromacs.org/current/onlinehelp/gmx-trjconv.html
