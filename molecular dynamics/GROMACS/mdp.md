# 分子动力学参数

- [分子动力学参数](#分子动力学参数)
  - [简介](#简介)
  - [参数](#参数)
    - [能量最小化](#能量最小化)
  - [示例参数](#示例参数)
    - [能量最小化参数](#能量最小化参数)
    - [NVT 平衡参数](#nvt-平衡参数)
  - [Preprocessing](#preprocessing)
  - [Run control](#run-control)
  - [Energy minimization](#energy-minimization)
  - [Output control](#output-control)
  - [Neighbor searching](#neighbor-searching)
  - [Electrostatics](#electrostatics)
  - [Van der Waals](#van-der-waals)
  - [Velocity generation](#velocity-generation)
  - [Bonds](#bonds)
  - [参考](#参考)

## 简介

分子动力学参数（.mdp 选项）

## 参数

### 能量最小化

|选项|默认值|说明|
|---|---|---|
|emtol|10 kJ/mol/nm|当最大力小于此值时，最小化收敛|
|emstep|0.01 nm|步长|

## 示例参数

### 能量最小化参数

```mdp
; MINIMIZATION RUN (minim.mdp)
;(used as input into grompp to generate em.tpr)
;
; Parameters describing what to do, when to stop, and what to save
integrator  = steep         ; A steepest descent algorithm for energy minimization
emtol       = 1000.0        ; Stop minimization when the maximum force < 1000.0 kJ/mol/nm
emstep      = 0.01          ; Minimization step size
nsteps      = 50000         ; Maximum number of (minimization) steps to perform

;ELECTROSTATIC AND VDWAALS
; Parameters describing how to find the neighbors of each atom and how to calculate the interactions
nstlist         = 1         ; Frequency to update the neighbor list and long range forces
cutoff-scheme   = Verlet    ; Buffered neighbor searching
ns_type         = grid      ; Method to determine neighbor list (simple, grid)
coulombtype     = PME       ; Treatment of long range electrostatic interactions
rcoulomb        = 1.0       ; Short-range electrostatic cut-off (nm)
rvdw            = 1.0       ; Short-range Van der Waals cut-off (nm)
pbc             = xyz       ; Periodic Boundary Conditions in all 3 dimensions
```

该参数包含两部分。

第一部分设置运行的基本信息：

- 最小化算法 `integrator=steep`，使用最陡下降法。也可以使用更复杂的算法，如共轭梯度（cg），对于大多数系统不需要。
- 最小化的最大步骤数 `nsteps=50000`。如果在这个步数内没有收敛，运行也会结束。
- 收敛标准由 `emtol=1000` 指定。即最大力 $F_{max}$ 小于 $1000 kJ/mol/nm$ 时，认为运行收敛。

第二部分专门设置如下信息：

- 静电和范德华相互作用
- 周期性边界条件设置

对这一部分，通常使用一些标准值，在其它的 mdp 文件中，一般也是这些值。例如，对静电（`rcoulomb = 1.0`）和范德华（`rvdw=1.0`）相互作用，截止值通常建议使用 1.0-1.2 nm，并且使用粒子网格方法（Particle Mesh Ewald, **PME**）处理长程非键相互作用。

### NVT 平衡参数

NVT 系综平衡参数模板，要求系统达到所需温度。

```mdp
define                  = -DPOSRES  ; position restrain the protein
; Run parameters
integrator              = md        ; leap-frog integrator
nsteps                  = 50000     ; 2 * 50000 = 100 ps
dt                      = 0.002     ; 2 fs
; Output control
nstxout                 = 500       ; save coordinates every 1.0 ps
nstvout                 = 500       ; save velocities every 1.0 ps
nstenergy               = 500       ; save energies every 1.0 ps
nstlog                  = 500       ; update log file every 1.0 ps
; Bond parameters
continuation            = no        ; first dynamics run
constraint_algorithm    = lincs     ; holonomic constraints 
constraints             = h-bonds   ; bonds involving H are constrained
lincs_iter              = 1         ; accuracy of LINCS
lincs_order             = 4         ; also related to accuracy
; Nonbonded settings 
cutoff-scheme           = Verlet    ; Buffered neighbor searching
ns_type                 = grid      ; search neighboring grid cells
nstlist                 = 10        ; 20 fs, largely irrelevant with Verlet
rcoulomb                = 1.0       ; short-range electrostatic cutoff (in nm)
rvdw                    = 1.0       ; short-range van der Waals cutoff (in nm)
DispCorr                = EnerPres  ; account for cut-off vdW scheme
; Electrostatics
coulombtype             = PME       ; Particle Mesh Ewald for long-range electrostatics
pme_order               = 4         ; cubic interpolation
fourierspacing          = 0.16      ; grid spacing for FFT
; Temperature coupling is on
tcoupl                  = V-rescale             ; modified Berendsen thermostat
tc-grps                 = Protein Non-Protein   ; two coupling groups - more accurate
tau_t                   = 0.1     0.1           ; time constant, in ps
ref_t                   = 300     300           ; reference temperature, one for each group, in K
; Pressure coupling is off
pcoupl                  = no        ; no pressure coupling in NVT
; Periodic boundary conditions
pbc                     = xyz       ; 3-D PBC
; Velocity generation
gen_vel                 = yes       ; assign velocities from Maxwell distribution
gen_temp                = 300       ; temperature for Maxwell distribution
gen_seed                = -1        ; generate a random seed
```

过一下上面的一些重要参数。

第一行使用 `define=-DPOSRES` 对蛋白应用位置约束。位置约束在 `gmx pdb2gmx` 创建的 `posre.itp` 文件中，用于平衡蛋白质周围的溶剂时，不引起蛋白质结构的显著变化。

然后是运行参数：

```mdp
; Run parameters
integrator              = md        ; leap-frog integrator
nsteps                  = 50000     ; 2 * 50000 = 100 ps
dt                      = 0.002     ; 2 fs
```

## Preprocessing

- **include**

要包含在拓扑中的目录。格式：`-I/home/john/mylib -I../otherlib`

- **define**

传递给预处理器的预定义。默认无预定义。可以在自定义拓扑文件中使用任意定义来控制选项。作用于现有 `top` 文件机制的选项包括：

`-DFLEXIBLE`：告诉 `grompp` 在拓扑信息中使用柔性的水模型而不是刚性的水模型, 对简正模式分析有用。

`‐DPOSRES`：告诉 `grompp` 在拓扑信息中包括 posre.itp , 用于位置约束。

## Run control

- **integrator**

`md`

蛙跳式算法积分牛顿运动方程。

`md-vv`



|选项|说明|
|---|---|
|steep|用于能量最小化的最陡下降法。最大步长为 `emstep`，tolerance 为 `emtol`|

- **dt** (0.001) [ps]

积分时间步长(只对md , sd 和 bd 积分器有意义)

- **nsteps** (0)

积分或最小化的最大步数，-1 表示不限制步数。

## Energy minimization

- **emtol** (10.0) [kJ mol-1 nm-1]

当最大的力比这个值小时就认为最小化收敛。

- **emstep** (0.01) [nm]

初始步长大小。

- **nstcgsteep** (1000) [steps]

用共轭梯度进行能量最小化时执行一步最速下降的频率。

- **nbfgscorr** (10)

L-BFGS 最小化的校正步数。数值越高(至少理论上)越准确, 但速度更慢。

## Output control

- **nstxout** (0) [steps]

将坐标写入输出 trr 轨迹文件的间隔步数, 最后一步的坐标始终会写入。

- **nstvout** (0) [steps]

将速度写入输出 trr 轨迹文件的间隔步数, 最后一步的速度始终会写入。

- **nstfout** (0) [steps]

将力写入输出 trr 轨迹文件的间隔步数，最后一步的力始终会写入。

- **nstlog** (1000) [steps]

将能量写入log 文件的间隔步数, 最后一步的能量始终会写入。

- **nstcalcenergy** (100)

两次能量计算之间的间隔步数，0 表示不计算。此选项仅与动力学有关。此选项会影响并行模拟的性能，因为计算能量需要所有进程之间的全局通讯，在高度并行的情况下， 会成为计算瓶颈。

- **nstenergy** (1000) [steps]

将能量写入能量文件的间隔步数，最后一步的能量始终会写入。该数值应是 `nstcalcenergy` 的倍数。注意, 对所有 MD 步数与 `nstcalcenergy` 的模, 能量总和及其涨落都存储在能量文件中，所以当 `nstenergy>1` 时, `gmx energy` 仍可以给出精确的能量平均值及其涨落。


## Neighbor searching

- **cutoff-scheme**

`Verlet`

利用缓存生成粒子的配对列表。缓冲区大小根据 `verlet-buffer-tolerance` 自动设置。如果 `verlet-buffer-tolerance=-1`，则使用 `rlist`。

`group`

为原子组生成配对列表，这些 group 对应拓扑信息中的电荷 group。已不支持该选项。

- **nstlist** (10 steps)

`>0`

更新邻区列表的频率。当设置 dynamics 和 `verlet-buffer-tolerance`，nstlist 实际上是一个最小值，`gmx mdrun` 会根据需要增加它，除非直接设置为 1。在 GPU 上的并行模拟和非键合力的计算，设置为 20 或 40 通常能获得最佳性能。在能量最小化时，每次计算能量都会更新领区列表，并不会使用该参数。

`0`

只构建一次邻区列表，且不再更新。这主要用于真空中的模拟，所有离子彼此都能看到对方。但是 GROMACS 目前不支持真空模拟。

`<0`

不再使用。

- **pbc**

`xyz`

在所有方向上使用周期性边界条件。

`no`

不使用周期性边界条件, 忽略盒子。若不使用截断的模拟, 可将所有的 cut-offs 和 `nstlist` 设置为 0。要获得单个 MPI rank 上无 cut-offs 的最佳性能，可设置 `nstlist=0`， `ns‐type=simple`。

`xy`

只在 x 和 y 方向上使用周期性边界条件。仅适用于 `ns‐type=grid`，可与 walls 联用。没有墙或只有一个墙时，体系在 z 方向上大小是无限的，因此不能使用压力耦合或 Ewald 加和方法。当使用两面墙时没有这些缺点.

- **verlet-buffer-tolerance** (0.005) [kJ mol-1 ps-1]

执行动态模拟时使用。

只对cutoff‐scheme=Verlet 有用. 此选项设置由Verlet 缓冲引起的每个粒子配对相互作用的最大允许误差, 间接设
置了rlist . 若nstlist 和Verlet 缓冲大小都固定(出于性能原因), 不在配对列表中的粒子对在nstlist –1步内能够
不时地进入截断距离内. 这将导致非常小的能量跳跃. 对等温系综, 对于给定的截断和rlist 可估算出这些非常小的
能量跳跃. 估算时假定均相的粒子分布, 因此对多相体系可能会略微低估误差. 对于较长的配对列表寿命( nstlist –
1)*dt, 缓冲会被高估, 因为忽略了粒子之间的相互作用.
由于误差抵消, 总能量的实际漂移幅度通常小一到两个数量级. 注意, 与基于简单粒子配对的列表相比, GROMACS
的配对列表设置导致漂移降低为原来的1/10, 生成的缓冲大小考虑了这一点影响. 不使用动力学(能量最小化等)时, 缓
冲为截断的5%. 对NVE模拟, 会使用初始温度, 除非初始温度为零, 此时使用10%的缓冲. 对NVE模拟通常需要降低容
差以便在纳秒的时间尺度达到适当能量守恒. 要覆盖自动缓冲设置, 可使用verlet‐buffer‐tolerance=‐1 , 并手动
设置rlist .

## Electrostatics

- **coulombtype**

`Cut-off`

双程截断，其中邻区截断半径为 `rlist`，库仑截断距离为 `rcoulomb`，`rcoulomb≥rlist`。

Ewald
经典Ewald 加和方法. 实空间的截断距离rcoulomb 应等于rlist . 例如, 使用rlist=0.9,
rcoulomb=0.9 . 倒易空间使用的波矢的最大振幅由fourierspacing 控制. 直接/倒易空间的相对精度
由ewald‐rtol 控制.
注: Ewald 算法的复杂度为O(N ), 因此对于大的体系非常慢. 包含这个方法主要是为了作为参考–在大多数
情况下PME方法的性能都好得多.

快速平滑粒子网格Ewald(SPME) 静电方法. 直接空间类似于Ewald 加和方法, 而倒易空间部分使用FFT进行
计算. 格点尺寸由fourierspacing 控制, 内插的阶数由pme‐order 控制. 使用0.1 nm格点间距的三次内插
方法时, 静电力的计算精度为2–3*10 . 由于VDW截断导致的误差大于此, 你可以尝试使用0.15 nm的格点
间距. 当并行运行时, 内插的并行性能优于FFT, 因此可以试着减小格点尺寸, 同时增加内插.

P3M‐AD
粒子粒子粒子网格算法, 具有长程静电相互作用的解析梯度. 除影响函数对格点进行了优化外, 方法和代码
与SPME完全相同, 优化使在计算精度略有提高.
Reaction‐Field electrostatics
库仑截断距离为rcoulomb 的反应场, 其中rcoulomb≥rlist . 超过截断距离的介电常数为epsilon‐rf .
当epsilon‐rf=0 时, 介电常数无穷大.
Generalized‐Reaction‐Field
库仑截断距离为rcoulomb 的广义反应场, 其中rcoulomb≥rlist . 超过截断距离的介电常数为epsilonrf
. 离子强度由带电的(即非零电荷)电荷组计算. GRF势的温度通过ref‐t [K] 设定.
Reaction‐Field‐zero
在GROMACS中, 使用cutoff‐scheme=group 时, 正常的反应场静电方法会导致能量守恒性很差.
Reaction‐Field‐zero 通过将超出截断距离的势能设为零解决了这个问题. 这种方法只适用于介电常数无
穷大( epsilon‐rf=0 )的情况, 因为只有这样力在截断距离处才能消失. rlist 应比rcoulomb 大0.1至0.3
nm, 以考虑电荷组的大小已及更新邻区对时扩散的影响. 这一点以及使用查表代替解析函数使得
Reaction‐Field‐zero 的计算比正常反应场更耗时.
Reaction‐Field‐nec
与Reaction‐Field 相同, 但是GROMACS 3.3以前版本中的实现. 没有使用反应场校正排除原子对和自身
对的影响. 使用反应场计算1–4相互作用. 因排除不具有1–4相互作用的粒子对而缺少的校正达到总静电能
的百分之几, 并导致力和压力有微小的差别.
Shift
类似于vdwtype 的Shift . 你可能想使用Reaction‐Field‐zero 代替, 它具有类似的势能形状, 但具有物
理意义, 并且含有排除校正项, 计算的能量更好.
Encad‐Shift
库仑势在整个范围内降低, 使用Encad 模拟包中的定义
Switch
类似于vdwtype 的Switch . 切换库仑势可导致严重的假象, 建议: 使用Reaction‐Field‐zero 代替.

PME‐Switch
PME和对直接空间部分切换函数的组合(参见上文). rcoulomb 可以小于rlist .
主要用于等能量模拟(注意, PME 与cutoff‐scheme=Verlet 联用会更有效).
PME‐User
PME和用户表格的组合(参见上文). rcoulomb 可以小于rlist . mdrun 会从用户表格中减去PME网格的贡
献. 因为这个扣除, 用户表格应包含大约10个十进制的位置.
PME‐User‐Switch
PME-User和切换函数的组合(参见上文). 对最终粒子之间的相互作用使用切换函数, 即, 同时对用户提供的
函数和PME网格校正部分使用切换函数.

- **rcoulomb** (1) [nm]

库伦截断距离。对 PME，在 `gmx mdrun` 中

## Van der Waals

- **vdwtype**

`Cut-off`

双程截断, 邻区列表的截断距离为rlist , VdW截断距离为rvdw , 其中 rvdw≥rlist

- **DispCorr**

`no`

不使用任何修正。

`EnerPres`

对能量和压力进行长程色散校正。

`Ener`

只对能量进行长程色散校正。

## Velocity generation

- **gen-vel**



## Bonds

- **constraints**

拓扑中将哪些键转换为刚性完整约束。注意，典型的刚性水模型没有 bonds，而是一个专门的 `[settles]` 指令，因此不受该选项影响。

|选项|说明|
|---|---|
|none|不将任何 bonds 转换为约束|
|h-bonds|将和氢原子连接的键转换为约束|
|all-bonds|所有键转换为约束|
|h-angles|将所有键转换为约束，将涉及氢原子的角度转换为键约束|
|all-angles|将所有键转换为约束，所有角度转换为键约束|

- **constraint-algorithm**

`LINCS`

线性约束求解器(LINear Constraint Solver)。在区域分解中采用并行版本 P-LINCS。使用 `lincs-order` 设置精度，它同时设置了矩阵求逆展开中矩阵的个数。经过矩阵求逆校正后，算法会执行一次迭代校正以补偿因旋转导致的增长。迭代次数可以用 `lincs-iter` 设置。每 `nstlog` 步，相对约束的均方根偏差会输出到日志文件。如果在一个步骤键的旋转超过 `lincs‐warnangle` (度)，将打印警告到日志文件和 stderr。LINCS 不能用于耦合键角约束。

`SHAKE`

与 LINCS 相比，SHAKE方法稍慢且不太稳定，但能用于键角约束。使用 `shake-tol` 设置相对 tolerance，对正常 MD 0.0001 很合适。SHAKE 不支持处于不同节点上的原子之间的约束，因此当存在电荷组之间的约束时, 它不能与区域分解一起使用. SHAKE不能用于能量最小化。

- **continuation**

该选项之前称为 `unconstrained-start`。

|选项|说明|
|---|---|
|no|对启动配置和重置 shell 应用约束|
|yes|不应用约束，对继续运行和重新运行非常有用|


## 参考

- https://manual.gromacs.org/documentation/current/user-guide/mdp-options.html
- https://www.compchems.com/gromacs-mdp-file-parameters/
