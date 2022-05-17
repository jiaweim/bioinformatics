# FragPipe

## 简介

FragPipe 是一个 Java 图形用户界面，提供了一套基于质谱的蛋白质组数据分析工具，包括：

- 核心搜索引擎 MSFragger，可用于常规和开放检索；
- MSFragger 搜库结果下游分析工具 Philosoher
  - PeptideProphet
  - iProphet
  - ProteinProphet
  - FDR filtering
  - label-based quantification
  - multi-experiment summary report
- 辅助解析 open search 结果的 Crystal-C 和 PTM-Shepherd
- 用于 TMT/iTRAQ 等重标记定量的 TMT-Integrator
- 用于无标定量和 Match-between-run (MBR) 的 IonQuant
- 构建谱图工具 EasyPQP
- DIA 数据分析工具 MSFragger-DIA 和 DIA-Umpire SE 模块

## 参考

- https://fragpipe.nesvilab.org/
