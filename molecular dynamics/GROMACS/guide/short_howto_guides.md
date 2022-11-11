# 简短指南

## 水溶剂

当使用 `solvate` 生成一盒溶剂，需要提供一个预平衡的溶剂盒，使溶剂堆积到溶质周围，然后截断以获得想要的模拟体积。

当使用任何 3 点模型（如 `SPC`, `SPC/E` 或 `TIP3P`），应该指定 `-cs spc216.gro`，GROMACS 安装目录下 `gromacs/share/top` 包含该文件。其它水分子模型，如 TIP4P、TIP5P 也可以用，都在该目录。溶剂化后，应该确保在所需的温度下平衡至少 5-10 ps。

需要在 top 文件中选择正确的水分子模型，可以使用 pdb2gmx 的 `-water` 选项指定，也可以直接编辑 top 文件。

## 参考

- https://manual.gromacs.org/2022/how-to/index.html
