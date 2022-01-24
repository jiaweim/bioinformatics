# 对象管理

- [对象管理](#对象管理)
  - [简介](#简介)
  - [移除对象](#移除对象)
  - [载入对象](#载入对象)
  - [参考](#参考)

2022-01-24, 09:57
***

## 简介

下面是 PyMOL 输出输出相关的命令。

## 移除对象

`delete` 命令用于移除对象或指定的选择项。

```sh
delete name  
delete all   # 删除所有对象
```

- `name`

对象或选择项名称。

## 载入对象

```sh
load filename [,object [,state [,format [,finish [,discrete [,multiplex ]]]]]]
```

`load` 命令用于载入文件，根据文件扩展名确定文件类型。

支持的文件类型：

- PDB 格式，支持各种扩展，用于指定连接性、化学价、多个模型、轨迹等；
- MOL 格式，加载单个小分子结构；
- SDF 格式，加载多个小分子结构；
- MOL2 格式，加载同时包含小分子和蛋白的系统；
- XYZ 变体，包括多模型 XYZ；

```sh
'pdb' : PDB,  'mmod' : Macromodel, 'xyz' : Tinker, 'cc1' : ChemDraw3D  
'mol' : MDL MOL-file, 'sdf' : MDL SD-file
'xplor' : X-PLOR/CNS map, 'ccp4' : CCP4 map,
'callback' : PyMOL Callback object (PyOpenGL)
'cgo' : compressed graphics object (list of floats)
'trj' : AMBER trajectory (use load_traj command for more control)
'top' : AMBER topology file 'rst' : AMBER restart file
'cex' : Metaphorics CEX format
'pse' : PyMOL Session file
'pqr' : PQR (a modified PDB file with charges and radii)
'mol2' : MOL2
```

- `filename`, 文件路径或 URL；
- `object`，string ，载入 PyMOL 对象名称，默认为文件前缀；
- `state`，integer，保存对象的 state 号，默认 0；
- `format`，string，文件格式。默认为文件扩展名；
- `finish`，integer



## 参考

- https://pymolwiki.org/index.php/Delete
- https://pymolwiki.org/index.php/Load
