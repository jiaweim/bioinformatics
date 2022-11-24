# mdp 参数文件

- [mdp 参数文件](#mdp-参数文件)
  - [简介](#简介)
  - [mdp 文件](#mdp-文件)
  - [EM mdp](#em-mdp)
  - [NVT mdp](#nvt-mdp)
  - [NPT mdp](#npt-mdp)
  - [MD mdp](#md-mdp)
  - [参考](#参考)

Last updated: 2022-11-24, 16:01
****

## 简介

分子动力学模拟可以在不同条件、不同时间，使用不同的算法来解动力学方程等等。

这些参数保存在 Molecular Dynamics parameters (mdp) 文件中，一个以 mdp 结尾的文本文件。

该文件用在 `gmx grompp` 模块中生成 tpr 文件。

## mdp 文件

mdp 大多时候可以使用标准值，不用更改。不过也要注意，部分参数需要根据系统进行调整。下面给出的模板可以作为起点，根据提供的差别进行调整。

## EM mdp

能量最小化的参数：

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

文件中已经包含参数信息的注释（`;` 后面为注释）。

该参数分为两部分，第一部分设置运行的基本信息：

- 最小化算法 `integrator=steep`，使用最陡下降法。也可以使用更复杂的算法，如共轭梯度（cg）或 `l-bfgs`，对于大多数系统不需要。
- 最小化的最大步骤数 `nsteps=50000`。如果在这个步数内没有收敛，运行也会结束。
- 收敛标准由 `emtol=1000` 指定。即最大力 $F_{max}$ 小于 $1000 kJ/mol/nm$ 时，认为运行收敛。

第二部分设置如下信息：

- 静电和范德华相互作用
- 周期性边界条件设置

对这一部分，通常使用一些标准值，在其它的 mdp 文件中，一般也是这些值。例如，对静电（`rcoulomb = 1.0`）和范德华（`rvdw=1.0`）相互作用，截止值通常建议使用 1.0-1.2 nm，并且使用粒子网格方法（Particle Mesh Ewald, **PME**）处理长程非键相互作用。

## NVT mdp

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

第一行使用 `define=-DPOSRES` 对蛋白应用位置约束。位置约束在 `gmx pdb2gmx` 创建的 `posre.itp` 文件中，用于平衡蛋白质周围的溶剂时，不引起蛋白质结构的显著变化。

然后是运行参数：

```mdp
; Run parameters
integrator              = md        ; leap-frog integrator
nsteps                  = 50000     ; 2 * 50000 = 100 ps
dt                      = 0.002     ; 2 fs
```

这里指定了：

- 解运行方程的算法，本例使用了 leap-frog 积分器 `integrator=md`
- 模拟时间由设置的时间步长 `dt` 和步数 `nsteps` 指定。

本例选择步长 2fs（`dt=0.002`）、步数 50,000 步（`nsteps=50000`），因此总时长为：

$$t = dt \cdot nsteps = 0.002 \cdot 50000=100000fs = 100ps = 0.1ns$$

根据系统的复杂性，平衡所需的时间可能差别很大，可以通过查看 RMSD 来评估系统是否平衡。

下面的参数则设置将信息保存到输出文件的频率：

```mdp
; Output control
nstxout                 = 500       ; save coordinates every 1.0 ps
nstvout                 = 500       ; save velocities every 1.0 ps
nstenergy               = 500       ; save energies every 1.0 ps
nstlog                  = 500       ; update log file every 1.0 ps
```

- `nstxout=500` 和 `nstvout=500` 表示每 500 个时间步保存一次坐标和速度到轨迹文件 trr 中；

$$t = dt \cdot nsteps = 0.002 \cdot  500 = 1000 fs = 1 ps$$

如果想使用消耗较小的 xtc 轨迹格式，则可以使用 `nstxout-compressed`。

- `nstenergy=500` 设置保存能量到 edr 文件的频率
- `nstlog=500` 设置写入日志文件的频率

下一部分：

```mdp
; Bond parameters
continuation            = no        ; first dynamics run
constraint_algorithm    = lincs     ; holonomic constraints 
constraints             = h-bonds   ; bonds involving H are constrained
lincs_iter              = 1         ; accuracy of LINCS
lincs_order             = 4         ; also related to accuracy
```

这里主要设置的两类参数：

- `continuation=no` 表示不是从另一个运行继续模拟，NVT 平衡一般是这种情况；
- 使用 LINCS 算法约束蛋白质的键

跳过前面已经提过的静电相互作用和范德华力设置。下一步实验条件：

```mdp
; Temperature coupling is on
tcoupl                  = V-rescale             ; modified Berendsen thermostat
tc-grps                 = Protein Non-Protein   ; two coupling groups - more accurate
tau_t                   = 0.1     0.1           ; time constant, in ps
ref_t                   = 300     300           ; reference temperature, one for each group, in K
; Pressure coupling is off
pcoupl                  = no        ; no pressure coupling in NVT
```

为了使系统达到所需温度，需要设置恒温器算法，通过 `tcoupl` 参数设置。`V-rescale` 适用于一般平衡。对于更复杂的系统，则建议使用太简单的算法，如 `berendsen`。

可以使用 `tc-grps` 参数为恒温器创建单独的 group。通常建议至少创建两个 group，即蛋白部分(`Protein`) 和系统的余下部分 `Non-protein`。可以传入任何可用的 GROMACS index。

然后用 `ref-t` 设置期望温度，`tau-t` 设置耦合常数。

> **NOTE**: 在 NVT 平衡中，不需要调节系统压力，所以系统盒子尺寸保持不变 `pcoupl=no` .

nvt.mdp 的最后一部分，决定是否为系统分配初始速度：

```mdp
; Velocity generation
gen_vel                 = yes       ; assign velocities from Maxwell distribution
gen_temp                = 300       ; temperature for Maxwell distribution
gen_seed                = -1        ; generate a random seed
```

由于 NVT 平衡是模拟的第一步，所以需要分配初始速度 `gen_vel=yes`，速度将从麦克斯韦-玻尔兹曼分布中选择，温度由 `gen_temp` 设置

## NPT mdp

NPT 平衡使系统达到所需压力：

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
continuation            = yes       ; Restarting after NVT 
constraint_algorithm    = lincs     ; holonomic constraints 
constraints             = h-bonds   ; bonds involving H are constrained
lincs_iter              = 1         ; accuracy of LINCS
lincs_order             = 4         ; also related to accuracy
; Nonbonded settings 
cutoff-scheme           = Verlet    ; Buffered neighbor searching
ns_type                 = grid      ; search neighboring grid cells
nstlist                 = 10        ; 20 fs, largely irrelevant with Verlet scheme
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
; Pressure coupling is on
pcoupl                  = Parrinello-Rahman     ; Pressure coupling on in NPT
pcoupltype              = isotropic             ; uniform scaling of box vectors
tau_p                   = 2.0                   ; time constant, in ps
ref_p                   = 1.0                   ; reference pressure, in bar
compressibility         = 4.5e-5                ; isothermal compressibility of water, bar^-1
refcoord_scaling        = com
; Periodic boundary conditions
pbc                     = xyz       ; 3-D PBC
; Velocity generation
gen_vel                 = no        ; Velocity generation is off 
```

大部分参数前面已经讨论过了，下面主要说明与前面 NVT 平衡不同的部分：

```mdp
; Pressure coupling is on
pcoupl                  = Parrinello-Rahman     ; Pressure coupling on in NPT
pcoupltype              = isotropic             ; uniform scaling of box vectors
tau_p                   = 2.0                   ; time constant, in ps
ref_p                   = 1.0                   ; reference pressure, in bar
compressibility         = 4.5e-5                ; isothermal compressibility of water, bar^-1
refcoord_scaling        = com
```

可以看到，这里启用了压力耦合，所以会调整盒子的大小以达到所需压力。

GROMACS 提供了许多稳压算法，这里用 `pcoupl` 选择了常用的 `Parrinello-Rahman` 算法。在平衡阶段，不需要使用太复杂的稳压算法，如 `Berendsen`。

用 `ref_p=1.0` 设置期望压力值，用 `tau_p=2.0` 设置耦合时间常数。另外，盒子将在所有维度均匀缩放 `pcoupltype=isotropic`。如果模拟膜环境，则推荐使用半各向同性缩放 `semiisotropic`，在 x,y 轴各向同性，在 z 则不同。

> **NOTE**: NPT 平衡通常是第二个平衡步骤，所以选择 `continuation=yes`，从 NVT 系综平衡结果继续模拟。
> 此外，不需要重新生成速度，因为在前面的步骤已经生成了，只需要从之前的文件读取速度信息。

## MD mdp

最后是生成运行的 mdp 文件。通常是在 NPT 系综内模拟，不限制蛋白质位置：

```mdp
; Run parameters
integrator              = md        ; leap-frog integrator
nsteps                  = 500000    ; 2 * 500000 = 1000 ps (1 ns)
dt                      = 0.002     ; 2 fs
; Output control
nstxout                 = 0         ; suppress bulky .trr file by specifying 
nstvout                 = 0         ; 0 for output frequency of nstxout,
nstfout                 = 0         ; nstvout, and nstfout
nstenergy               = 5000      ; save energies every 10.0 ps
nstlog                  = 5000      ; update log file every 10.0 ps
nstxout-compressed      = 5000      ; save compressed coordinates every 10.0 ps
compressed-x-grps       = System    ; save the whole system
; Bond parameters
continuation            = yes       ; Restarting after NPT 
constraint_algorithm    = lincs     ; holonomic constraints 
constraints             = h-bonds   ; bonds involving H are constrained
lincs_iter              = 1         ; accuracy of LINCS
lincs_order             = 4         ; also related to accuracy
; Neighborsearching
cutoff-scheme           = Verlet    ; Buffered neighbor searching
ns_type                 = grid      ; search neighboring grid cells
nstlist                 = 10        ; 20 fs, largely irrelevant with Verlet scheme
rcoulomb                = 1.0       ; short-range electrostatic cutoff (in nm)
rvdw                    = 1.0       ; short-range van der Waals cutoff (in nm)
; Electrostatics
coulombtype             = PME       ; Particle Mesh Ewald for long-range electrostatics
pme_order               = 4         ; cubic interpolation
fourierspacing          = 0.16      ; grid spacing for FFT
; Temperature coupling is on
tcoupl                  = V-rescale             ; modified Berendsen thermostat
tc-grps                 = Protein Non-Protein   ; two coupling groups - more accurate
tau_t                   = 0.1     0.1           ; time constant, in ps
ref_t                   = 300     300           ; reference temperature, one for each group, in K
; Pressure coupling is on
pcoupl                  = Parrinello-Rahman     ; Pressure coupling on in NPT
pcoupltype              = isotropic             ; uniform scaling of box vectors
tau_p                   = 2.0                   ; time constant, in ps
ref_p                   = 1.0                   ; reference pressure, in bar
compressibility         = 4.5e-5                ; isothermal compressibility of water, bar^-1
; Periodic boundary conditions
pbc                     = xyz       ; 3-D PBC
; Dispersion correction
DispCorr                = EnerPres  ; account for cut-off vdW scheme
; Velocity generation
gen_vel                 = no        ; Velocity generation is off 
```

生产运行通常比前面的模拟要耗时，因此，最好将轨迹保存为内存消耗较小的格式 xtc。在 Output control 部分指定：

```mdp
; Output control
nstxout                 = 0         ; suppress bulky .trr file by specifying 
nstvout                 = 0         ; 0 for output frequency of nstxout,
nstfout                 = 0         ; nstvout, and nstfout
nstenergy               = 5000      ; save energies every 10.0 ps
nstlog                  = 5000      ; update log file every 10.0 ps
nstxout-compressed      = 5000      ; save compressed coordinates every 10.0 ps
compressed-x-grps       = System    ; save the whole system
```

之前设置的参数 `nstxout`、`nstvout` 都设置为 0.

每 5000 步将坐标写入 xtc 文件 `nstxout-compressed=5000`。另外使用 `compressed-x-grps=System` 指定要保存整个系统，也可以只保存蛋白质 `compressed-x-grps=Protein`。

> **NOTE**: 这里没有定义 `define=-DPOSRES`，生产运行不需要约束蛋白位置。

## 参考

- https://www.compchems.com/gromacs-mdp-file-parameters/
- https://manual.gromacs.org/current/user-guide/mdp-options.html
