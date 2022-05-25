# save

2022-05-25, 12:55
***

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

## 示例

- 只保存 alpha 碳

```sh
save onlyCAs.pdb, n. CA
```


## 参考

- https://pymolwiki.org/index.php/Save
- https://pymol.org/pymol-command-ref.html#save
