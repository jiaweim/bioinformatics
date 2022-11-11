# SwissDock

## 简介

功能：

- SwissDock 是一个用于预测靶蛋白和小分子之间可能的相互作用服务器。
- S3DB，手动维护的 target, ligand 结构数据库

SwissDock 基于对接软件 EADock DSS，其算法如下：

1. 在盒子（local docking）或目标腔（blind docking）附近生成许多结合模式；
2. 同时，在一个网格上评估它们的 CHARMM 能量；
3. 用 FACTS 方法评估能量最有利的结合模式，并进行聚类冯恩熙；
4. 最佳的 cluster 可以在线可视化，也可以下载到本地。

## 示例

Peroxisome proliferator activated receptor delta 

## 参考

- http://www.swissdock.ch/
- Grosdidier A, Zoete V, Michielin O. SwissDock, a protein-small molecule docking web service based on EADock DSS. Nucleic Acids Res. 2011 Jul;39(Web Server issue):W270-7. doi: 10.1093/nar/gkr366. Epub 2011 May 29. PMID: 21624888; PMCID: PMC3125772.
- Grosdidier A, Zoete V, Michielin O. Fast docking using the CHARMM force field with EADock DSS. J Comput Chem. 2011 Jul 30;32(10):2149-59. doi: 10.1002/jcc.21797. Epub 2011 May 3. PMID: 21541955.
