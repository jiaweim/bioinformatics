# 力场

## 简介

分子力学（Molecular Mechanics, MM）是一种计算方法，通过势能方程来分析分子体系。下面的势能方程基于键拉伸（bond stretching）、角弯曲（angle bending）、二面角（dihedral angles）、范德华力（Van der Waals）和库仑相互作用的能量项总和。

$$E_{MM}(R)=E_{str}+E_{bend}+E_{tors}+E_{cross}+E_{el}+E_{vdW}$$

该方程中包含的作用力可以分为成键项和非键项。

## 函数形式和参数

上述方程 $E_{MM}(R)$ 的每一项都可以用不同的数学表达式或函数表示。例如，其中的键能项 $E_{str}$ 可以表示为：

$$E_{str}=\sum_i \frac{k_i}{2}(l_i-l_{i,0})^2$$

## 参考

- https://www.compchems.com/force-fields-in-molecular-dynamics/
