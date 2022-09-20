# Heterogen Section

- [Heterogen Section](#heterogen-section)
  - [简介](#简介)
  - [HET](#het)
  - [参考](#参考)

## 简介

PDB 文件中的杂原子部分（heterogen）包含非标准残基的描述。

## HET

HET record 用于描述非标准残基，如抑制剂、溶剂分子以及离子等。不是 SEQRES 所述生物大分子的一部分、但会与生物大分子结合的基团，或者它们是构成生物大分子的一部分，但是不属于下列物种之一，就被视为 HET：

- 标准氨基酸
- 标准核酸（C, G, A, U, I, DC, DG, DA, DU, DT, DI）
- 未知氨基酸（UNK）或核酸（N）



## 参考

- http://www.wwpdb.org/documentation/file-format-content/format33/sect4.html
