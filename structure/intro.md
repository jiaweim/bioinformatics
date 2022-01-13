#

## GDT TS

全局距离测试总分（Global Distance Test - Total Score, GDT_TS）用来表示两个蛋白结构的相似程度，是蛋白质结构 refinement 领域常用的一个评价标准。两个结构的序列不需要相同，GDT_TS 考虑两个模型的不同叠加方式，给出了预测模型中每个氨基酸与经验模型中每个氨基酸的接近程度的总体平均度量。

当两个结构在细节上存在差异时，GDT_TS 的效果由于均方根偏差（Root Mean Square Deviation, RMSD）。两种方法使用的都是 alpha 碳原子，差别是RMSD 使用的是 alpha 碳之间的实际距离，而 GDT 使用的是在指定距离内发现的 alpha 碳的百分比。 

GDT_TS 值的范围从 0 （毫无意义的预测）到 100（完美预测）。



## 参考

