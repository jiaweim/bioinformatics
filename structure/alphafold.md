# AlphaFold 蛋白结构数据库

- [AlphaFold 蛋白结构数据库](#alphafold-蛋白结构数据库)
  - [简介](#简介)
  - [CASP](#casp)
  - [AlphaFold](#alphafold)
  - [参考](#参考)

## 简介

AlphaFold DB 目前提供下表所示的预测的蛋白结构数据库。

可以在蛋白对应页面下载单个蛋白的结构，例如 https://alphafold.ebi.ac.uk/entry/F4HVG8

也可以使用下表提供的链接下载整个物种的蛋白结构数据库。对所有物种的预测结构，可以在 FTP 站点下载：http://ftp.ebi.ac.uk/pub/databases/alphafold/

|Species|Common Name|Reference Proteome|Predicted Structures|Download|
|---|---|---|---|---|
|Arabidopsis thaliana|Arabidopsis|UP000006548|27,434|Download (3642 MB)|
|Caenorhabditis elegans|Nematode worm|UP000001940 |19,694|Download (2601 MB)|
|Candida albicans|C. albicans|UP000000559 |5,974|Download (965 MB)|
|Danio rerio|Zebrafish|UP000000437 |24,664|Download (4141 MB)|
|Dictyostelium discoideum|Dictyostelium|UP000002195 |12,622|Download (2150 MB)|
|Drosophila melanogaster|Fruit fly|UP000000803 |13,458|Download (2174 MB)|
|Escherichia coli|E. coli|UP000000625 |4,363|Download (448 MB)|
|Glycine max|Soybean|UP000008827 |55,799|Download (7142 MB)|
|Homo sapiens|Human|UP000005640 |23,391|Download (4784 MB)|
|Leishmania infantum|L. infantum|UP000008153 |7,924|Download (1481 MB)|
|Methanocaldococcus jannaschii|M. jannaschii|UP000000805 |1,773|Download (171 MB)|
|Mus musculus|Mouse|UP000000589 |21,615|Download (3547 MB)|
|Mycobacterium tuberculosis|M. tuberculosis|UP000001584 |3,988|Download (421 MB)|
|Oryza sativa|Asian rice|UP000059680 |43,649|Download (4416 MB)|
|Plasmodium falciparum|P. falciparum|UP000001450 |5,187|Download (1132 MB)|
|Rattus norvegicus|Rat|UP000002494 |21,272|Download (3404 MB)|
|Saccharomyces cerevisiae|Budding yeast|UP000002311 |6,040|Download (960 MB)|
|Schizosaccharomyces pombe|Fission yeast|UP000002485 |5,128|Download (776 MB)|
|Staphylococcus aureus|S. aureus|UP000008816 |2,888|Download (268 MB)|
|Trypanosoma cruzi|T. cruzi|UP000002296 |19,036|Download (2905 MB)|
|Zea mays|Maize|UP000007305 |39,299|Download (5014 MB|

## CASP

蛋白质结构预测的关键评估（Critical Assessment of protein Structure Prediction, CASP）旨在推进从蛋白序列预测蛋白质结构的方法。CASP 通过盲预测提供预测方法的客观测试。

CASP 比赛已进行 14 届，从1994年开始，每 2 年一次。第 15 届预计在 2022 年春开始。这些实验的完整数据可以在官网找到：https://www.predictioncenter.org/ 。

## AlphaFold

AlphaFold 骨架准确性中位数为 0.96 Å RMSD$_{95}$（95% 残基覆盖率下 $C_{\alpha}$ 的均方根偏差）（95% CI=0.85 Å - 1.16 Å）,而次优的方法骨架精度中位数为 2.8 Å RMSD$_{95}$（95% CI=2.7Å - 4.0Å）。

AlphaFold 对超级复合物准确，但对膜蛋白的误差较大。



## 参考

- https://alphafold.ebi.ac.uk/download
- https://www.predictioncenter.org/
