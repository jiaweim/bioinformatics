# remove

2022-05-25, 12:42
***

## 简介

从模型中删除选择的原子。

用法：

```sh
remove (selection)
```

## 示例

- 使用选择功能，移除氢原子

```sh
remove (hydro)
```

- 使用氢原子名称移除氢原子

```sh
remove hydrogens
```

- 根据残基名称，移除 water

```sh
remove resn hoh
```

- 移除溶剂

```sh
remove solvent
```

## 参考

- https://pymolwiki.org/index.php/Remove
