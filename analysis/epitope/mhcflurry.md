# MHCflurry

- [MHCflurry](#mhcflurry)
  - [简介](#简介)
  - [数据集](#数据集)
  - [Python 接口](#python-接口)
    - [载入 predictor](#载入-predictor)
    - [预测单个肽段](#预测单个肽段)
    - [扫描蛋白序列](#扫描蛋白序列)
    - [底层接口](#底层接口)
  - [参考](#参考)

2021-06-16, 10:48
***

## 简介

MHCflurry 单独构建了 MHC 等位基因依赖的 BA 预测器和非等位基因依赖的 AP 预测器。首先使用 MHC-I 配体数据训练一个 MHC-I BA 预测器，包括亲和力测定数据集和质谱数据集。

训练数据中使用的体外（*in vitro*）测量的亲和力在很大程度上独立于AP，这是限制 BA 预测模型学习 AP 信号的选择之一。MHCflurry 使用 BA 预测模型结合质谱鉴定到的肽段和诱饵肽段（decoy），生成 AP 模型的训练集。

## 数据集

为了对 BA 预测模型进行测试，收集了 11 个研究 MHC-I 结合肽段的质谱数据集。这里只保留已知 MHC-I 基因型的样本。

其中两项研究使用转基因细胞系表达单个 MHC-I 等位基因，我们将其称为单等位基因样本（MONOALLELIC），包括 Sarkizova 发表的 92 个样本以及 Abelin 等发表的 8 个样本。



## Python 接口

### 载入 predictor

`Class1PresentationPredictor` 类是主要的预测类，也是该类提供 `mhcflurry-predict` 和 `mhcflurry-predict-scan` 命令。

`Class1PresentationPredictor` 类包含两个主要功能类：

- `Class1AffinityPredictor` 实现结合力预测；
- `Class1ProcessingPredictor` 实现抗原处理预测。

然后使用逻辑回归计算结合力与抗原处理的综合打分。

使用静态方法 `load` 载入训练好的模型。使用方法：

```py
>>> from mhcflurry import Class1PresentationPredictor
>>> predictor = Class1PresentationPredictor.load()
>>> predictor.supported_alleles[:5]
['Atbe-B*01:01', 'Atbe-E*03:01', 'Atbe-G*03:01', 'Atbe-G*03:02', 'Atbe-G*06:01']
```

### 预测单个肽段

对单个肽段，使用 `Class1PresentationPredictor` 的 `predict` 方法，该方法返回 `pandas.DataFrame`，包含对应的结合力、处理以及最终打分：

```py
>>> predictor.predict(
...    peptides=["SIINFEKL", "NLVPMVATV"],
...    alleles=["HLA-A0201", "HLA-A0301"],
...    verbose=0)
     peptide  peptide_num sample_name      affinity best_allele  processing_score  presentation_score
0   SIINFEKL            0     sample1  12906.786173   HLA-A0201          0.101473            0.012503
1  NLVPMVATV            1     sample1     15.038358   HLA-A0201          0.676289            0.975463
```

这里等位基因为 MHC-I 基因，对每个肽段，输出最强的等位基因结果。

如果有多个样本基因型，则可以传入 dict：

```py
>>> predictor.predict(
...    peptides=["KSEYMTSWFY", "NLVPMVATV"],
...    alleles={
...       "sample1": ["A0201", "A0301", "B0702", "B4402", "C0201", "C0702"],
...       "sample2": ["A0101", "A0206", "B5701", "C0202"],
...    },
...    verbose=0)
      peptide  peptide_num sample_name      affinity best_allele  processing_score  presentation_score
0  KSEYMTSWFY            0     sample1  16737.745268       A0301          0.381632            0.026550
1   NLVPMVATV            1     sample1     15.038358       A0201          0.676289            0.975463
2  KSEYMTSWFY            0     sample2     62.540779       A0101          0.381632            0.796731
3   NLVPMVATV            1     sample2     15.765500       A0206          0.676289            0.974439
```

输出每个 sample/peptide 组合最强的 binder。

用户可能更多关注亲和力预测，因为处理和呈递预测是实验性功能。如果要使用呈递打分，则应当给出肽段或的 N-端和 C-端序列，以提供准确度。例如：

```py
>>> predictor.predict(
...    peptides=["KSEYMTSWFY", "NLVPMVATV"],
...    n_flanks=["NNNNNNN", "SSSSSSSS"],
...    c_flanks=["CCCCCCCC", "YYYAAAA"],
...    alleles={
...       "sample1": ["A0201", "A0301", "B0702", "B4402", "C0201", "C0702"],
...       "sample2": ["A0101", "A0206", "B5701", "C0202"],
...    },
...    verbose=0)
      peptide   n_flank   c_flank  peptide_num sample_name      affinity best_allele  processing_score  presentation_score
0  KSEYMTSWFY   NNNNNNN  CCCCCCCC            0     sample1  16737.745268       A0301          0.605816            0.056190
1   NLVPMVATV  SSSSSSSS   YYYAAAA            1     sample1     15.038358       A0201          0.824994            0.986719
2  KSEYMTSWFY   NNNNNNN  CCCCCCCC            0     sample2     62.540779       A0101          0.605816            0.897493
3   NLVPMVATV  SSSSSSSS   YYYAAAA            1     sample2     15.765500       A0206          0.824994            0.986155
```

### 扫描蛋白序列

`predict_sequences` 方法支持扫描蛋白序列。例如：

```py
>>> predictor.predict_sequences(
...   sequences={
...       'protein1': "MDSKGSSQKGSRLLLLLVVSNLL",
...       'protein2': "SSLPTPEDKEQAQQTHH",
...   },
...   alleles={
...       "sample1": ["A0201", "A0301", "B0702"],
...       "sample2": ["A0101", "C0202"],
...   },
...   result="filtered",
...   comparison_quantity="affinity",
...   filter_value=500,
...   verbose=0)
  sequence_name  pos     peptide         n_flank     c_flank sample_name    affinity best_allele  affinity_percentile  processing_score  presentation_score
0      protein1   13   LLLLVVSNL   MDSKGSSQKGSRL           L     sample1   38.206225       A0201             0.380125          0.017644            0.571060
1      protein1   14   LLLVVSNLL  MDSKGSSQKGSRLL                 sample1   42.243472       A0201             0.420250          0.090984            0.619213
2      protein1    5   SSQKGSRLL           MDSKG   LLLVVSNLL     sample2   66.749223       C0202             0.803375          0.383608            0.774468
3      protein1    6   SQKGSRLLL          MDSKGS    LLVVSNLL     sample2  178.033467       C0202             1.820000          0.275019            0.482206
4      protein1   13  LLLLVVSNLL   MDSKGSSQKGSRL                 sample1  202.208167       A0201             1.112500          0.058782            0.261320
5      protein1   12  LLLLLVVSNL    MDSKGSSQKGSR           L     sample1  202.506582       A0201             1.112500          0.010025            0.225648
6      protein2    0   SSLPTPEDK                    EQAQQTHH     sample1  335.529377       A0301             1.011750          0.010443            0.156798
7      protein2    0   SSLPTPEDK                    EQAQQTHH     sample2  353.451759       C0202             2.674250          0.010443            0.150753
8      protein1    8   KGSRLLLLL        MDSKGSSQ      VVSNLL     sample2  410.327286       C0202             2.887000          0.121374            0.194081
9      protein1    5    SSQKGSRL           MDSKG  LLLLVVSNLL     sample2  477.285937       C0202             3.107375          0.111982            0.168572
```

使用 `predict_sequences`时，会自动使用 flanking sequences。

### 底层接口

`Class1AffinityPredictor` 负责预测结合力，如果只需要结合力，则可以直接使用该类：

```py
>>> from mhcflurry import Class1AffinityPredictor
>>> predictor = Class1AffinityPredictor.load()
>>> predictor.predict_to_dataframe(allele="HLA-A0201", peptides=["SIINFEKL", "SIINFEQL"])
    peptide     allele    prediction  prediction_low  prediction_high  prediction_percentile
0  SIINFEKL  HLA-A0201  12906.786173     8829.460289     18029.923061               6.566375
1  SIINFEQL  HLA-A0201  13025.300796     9050.056312     18338.004869               6.623625
```

`prediction_low` 和 `prediction_high` 字段给出在整个模型中的 5-95 百分位值。

同样可以用 `Class1ProcessingPredictor` 直接预测抗原处理值。

## 参考

- https://openvax.github.io/mhcflurry/
