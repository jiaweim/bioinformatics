# LinearDesign

- [LinearDesign](#lineardesign)
  - [简介](#简介)
  - [参考](#参考)

2021-06-02, 12:30
***

## 简介

http://rna.baidu.com/

全球首个 mRNA 疫苗基因序列设计算法 LinearDesign，专门用于优化 mRNA 序列设计的高效算法。

设计稳定且蛋白质产量高的 mRNA 是一项具有挑战性的问题。有研究表明，更稳定的二级结构和最佳密码子协同作用可以增加蛋白质的表达。因此，可以将mRNA 序列设计问题描述为：找到编码同一个蛋白质的同义序列中，找到二级结构稳定性和密码子最优的 mRNA 序列。

每个氨基酸由一个密码子翻译，每个密码子由3个相邻的核苷酸组成。例如，起始密码子 AUG 翻译称为甲硫氨酸。但是由于密码子的冗余性（21 个氨基酸有 43 = 64 个密码子），使得大多数氨基酸有多个密码子，使得 mRNA 设计的搜索空间和蛋白质长度呈指数关系，例如 SARS-CoV-2 的突触蛋白包含 1273 个氨基酸，包括大概 10632 个 mRNA 可能序列。因此，mRNA 序列设计问题，就是利用遗传密码子的冗余性来寻找比野生型更稳定、蛋白表达量更高的 mRNA 序列。

LinearDesign 的核心思想是：将 mRNA 序列设计问题简化为形式语言理论和计算语言中的经典概念，即随机上下文无关语法（Stochastic Context Free Grammar, SCFG）和确定性有限自动机（）

## 参考

- Mauger, David M., B. Joseph Cabral, Vladimir Presnyak, Stephen V. Su, David W. Reid, Brooke Goodman, Kristian Link, et al. “MRNA Structure Regulates Protein Expression through Changes in Functional Half-Life.” Proceedings of the National Academy of Sciences 116, no. 48 (November 26, 2019): 24075–83. https://doi.org/10.1073/pnas.1908052116.
- Zhang, He, Liang Zhang, Ziyu Li, Kaibo Liu, Boxiang Liu, David H. Mathews, and Liang Huang. “LinearDesign: Efficient Algorithms for Optimized MRNA Sequence Design.” ArXiv:2004.10177 [q-Bio], May 13, 2020. http://arxiv.org/abs/2004.10177.
