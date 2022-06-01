# save

2022-05-25, 12:55
****

## 简介

`save` 命令将选择的原子保存到文件：

- 保存格式根据文件扩展名自动选择，支持 .pdb, .pqr, .mol, .sdf, .pkl, .pkla, .mmd, .out, .dat, .mmod, .pmo, .pov, .png, .pse, .psw, .aln, .fasta, .obj, .mtl, .wrl, .idtf, .dae, or .mol2.
- 如果文件扩展名为 `.pse` （PyMOL Session），则将完整的 PyMOL 状态保存到文件；
- clustalw 格式的比对也可以由 PyMOL 输出。按如下命令进行比对

```sh
align proteinA, proteinB, object=A_on_B
```

然后保存比对：

```sh
save A_aligned_with_B.aln, A_on_B
```

## 语法

```sh
save file [,(selection) [,state [,format]] ]
```

说明：

- 如果保存为 session 文件，则 "state" 无效
- 默认 `state=-1`，表示保存当前状态
- `state=0` 表示输出所有状态，如果包含多个状态，则输出的 PDB 文件会包含多状态。

## 示例

- 选择 alpha 碳导出

```sh
save onlyCAs.pdb, n. CA
```

- 保存 MD trajectory file to disk

```sh
save myTraj.pdb, myMDTrajectory, state=0
```

- 保存 PyMOL session

```sh
save thisSession.pse
```

## 参考

- https://pymolwiki.org/index.php/Save
- https://pymol.org/pymol-command-ref.html#save
