# 测量

- [测量](#测量)
  - [简介](#简介)
  - [distance](#distance)
  - [参考](#参考)

## 简介

选择 `Wizard -> measurement`，

## distance

`distance` 在选择的两个对象之间创建 distance 对象，用于显示指定 cutoff 之间的距离。

```sh
distance [ name [, selection1 [, selection2 [, cutoff [, mode ]]]]]
```

`distance` 还可以用来创建

- 例 1，显示1ESR 的第 10 个残基的 alpha 碳和第 40 个残基的 alpha 碳的距离

```sh
# make the first residue 0.
zero_residues 1esr, 0
distance i. 10 and n . CA, i. 40 and n. CA
```

## 参考

- https://pymolwiki.org/index.php/Distance
