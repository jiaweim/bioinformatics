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
  - [输出](#输出)
  - [Neighbor searching](#neighbor-searching)
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



## Run control

- **integrator**

|选项|说明|
|---|---|
|steep|用于能量最小化的最陡下降法。最大步长为 `emstep`，tolerance 为 `emtol`|



## 输出

|选项|默认值|说明|
|---|---|---|
|nstenergy|1000|保存能量到文件的时间间隔。|

## Neighbor searching

- **cutoff-scheme**

|选项|说明|
|---|---|
|Verlet|生成缓冲的 pair list。缓冲区大小根据 verlet-buffer-tolerance 自动设置，如果设置为 -1，则使用 rlist|
|

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

- **continuation**

该选项之前称为 `unconstrained-start`。

|选项|说明|
|---|---|
|no|对启动配置和重置 shell 应用约束|
|yes|不应用约束，对继续运行和重新运行非常有用|


## 参考

- https://manual.gromacs.org/documentation/current/user-guide/mdp-options.html
- https://www.compchems.com/gromacs-mdp-file-parameters/