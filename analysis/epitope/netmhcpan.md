# NetMHCpan

- [NetMHCpan](#netmhcpan)
  - [简介](#简介)
  - [输出结果说明](#输出结果说明)
  - [参考](#参考)

2021-07-29, 14:00
***

## 简介

NetMHCpan-4.1 使用人工神经网络预测多肽与已知序列的 MHC分子的结合。该方法使用超过 850,000 定量结合亲和力（Binding Affinity, BA）和质谱洗脱配体（Eluted Ligans, EL）肽段进行训练：

- BA 数据覆盖 201 种 MHC 分子，包括人（HLA-A,B,C,E），老鼠（H-2），牛（BoLA），灵长类（Patr, Mamu, Gogo），猪（SLA）和马（Eqa）；
- EL 数据覆盖 289 种 MHC 分析，包括人（HLA-A, B, C, E），老鼠（H-2），牛（BoLA），灵长类（Patr, Mamu, Gogo），猪（SLA），马（Eqca）和狗（DLA）。

此外，用户可以通过上传完整长度的 MHC 蛋白序列来获得对自定义 MHC-I 类分子的预测。可以对任意长度的肽段进行预测。

## 输出结果说明

|标题|说明|
|---|---|
|Pos|肽段在蛋白中的起始位置，0 开始|
|MHC|MHC 名称|
|Peptide|配体氨基酸序列|
|ID|肽段对应蛋白的 ID|
|Core|直接和 MHC 结合的核心 9 个氨基酸|
|icore|相互作用核心，这是候选/表位核心|
|EL-score|洗脱配体打分|
|EL_Rank|与一组随机天然肽段比较时获得的预测打分排序。该值不受某些分子的平均亲和力固有偏差影响，强结合定义为 %rank<0.5，弱结合定义为 %rank<2。建议使用 %Rank 而不是 Score 作为筛选标准|


## 参考

- https://services.healthtech.dtu.dk/service.php?NetMHCpan-4.1
