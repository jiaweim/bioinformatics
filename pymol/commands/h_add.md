# H Add

2022-05-31, 13:54
@author Jiawei Mao
****

## 简介

`h_add` 添加氢原子到分子上。

PyMOL 填充缺失的价态，但是没有优化羟基旋转。另外，许多晶体结构的 ASN/GLN/HIS 取向很随机。确定合适的酰胺旋转异构体（rotamer）和咪唑互变异构体（tautomers）以及指定的质子化状态是非常重要的计算化学内容，涉及静电势计算和组合搜索。在类似天冬氨酸酶和相邻羧酸盐的体系中海油溶剂和反离子的问题。

## GUI 操作

[A] -> hydrogens -> add

## 语法

```sh
# normal usage
h_add (selection)

# API usage
cmd.h_add( string selection="(all)" )
```

## 参考

- https://pymolwiki.org/index.php/H_Add
