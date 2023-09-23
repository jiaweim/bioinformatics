# 人口覆盖分析

2023-06-15
***

## 简介

T 细胞识别特定 MHC-epitope 复合体。表位只在能够表达结合该表位的 MHC 分子的个体中引起反应，该现象被称为 MHC 限制的 T 细胞反应。

MHC 分子具有极强的多态性，目前已知有 1000 多种人类 MHC（HLA）等位基因。选择具有不同 HLA 结合特异性的多肽有助于增加基于肽段的疫苗或诊断策略的人群覆盖率。由于不同的 HLA 类型在不同人种中的表达频率显著不同大，使得人群覆盖率与 MHC 多态性的关系很复杂。因此，如果没有仔细考虑，疫苗或诊断方法可能导致基于人群覆盖率的种族偏见。

为了解决该问题，IEDB 提供了 "Population Coverage" 计算工具。

该工具根据表位的 HLA 基因型频率和 MHC 结合结合数据预测对给定表位集合有反应的个体比例[^1]。HLA 等位基因频率来源于等位基因频率数据库（ http://www.allelefrequencies.net/ ）。目前，等位基因频率数据库提供了分布在 16 个不同地理位置的 115 个国家和 21 个不同种族的等位基因频率。另外，该工具还支持用户自定义包含等位基因频率的人群。

可以同时计算多个人口覆盖率，并生成平均人口覆盖率。由于 MHC-I 和 MHC-II T 细胞表位激活两种不同 T 细胞，即 CTL 和 HTL 的免疫应答，因此该程序提供了三种计算选项：

1. MHC-I 类型
2. MHC-II 类型
3. MHC-I + MHC-II

对每个人群覆盖率，该工具计算：

1) 预测的人群覆盖率
2) 人群识别的 epitope-HLA 平均数
3) 被 90% 人群识别的最小 epitope-HLA 数

## 使用

1. 输入 epitope 数
2. 输入 epitope-MHC 数据
3. 选择人群
4. 选择计算选项
5. 提交

如果要自定义人群，需在第一步之前完成。

## 参数

- **Number of epitope(s)**

输入表位集合中表位数目。例如：50

- **Epitope**

表位名称或序列（可选）。例如：GILGFVFTL

- **MHC restricted allele(s)**

以逗号分隔的等位基因，或点击 "Browser..." 在数据库选择等位基因。
例如：`HLA-A*02:01`, `HLA-A*02:02`, `HLA-A*02:04`

- **Epitope / MHC restriction data file**

epitope-MHC 限制数据可以通过文件提供。该文件包含两列数据，以 tab 分隔
第一列为 epitope 名称或序列，第二列为逗号分隔的 MHC 等位基因。没有标题行。示例：

```
FMKAVCVEV   HLA-A*02:01,HLA-A*02:02,HLA-A*02:03,HLA-A*02:06,HLA-A*68:02
FLIFFDLFLV  HLA-A*02:01,HLA-A*02:02,HLA-A*02:03,HLA-A*02:06,HLA-A*68:02
GLIMVLSFL   HLA-A*02:01,HLA-A*02:02,HLA-A*02:03,HLA-A*02:06,HLA-A*23:01
VLAGLLGNV   HLA-A*02:01,HLA-A*02:02,HLA-A*02:03,HLA-A*02:06,HLA-A*68:02
GLLGNVSTV   HLA-A*02:01,HLA-A*02:03,HLA-A*02:06
KILSVFFLA   HLA-A*02:01,HLA-A*02:02,HLA-A*02:06,HLA-A*03:01,HLA-A*11:01
ILSVSSFLFV  HLA-A*02:01,HLA-A*02:02,HLA-A*02:03,HLA-A*68:02,HLA-A*23:01
VLLGGVGLVL  HLA-A*02:01,HLA-A*23:01
QTNFKSLLR   HLA-A*03:01,HLA-A*11:01,HLA-A*31:01,HLA-A*68:01
LACAGLAYK   HLA-A*11:01,HLA-A*33:01,HLA-A*68:01
VTCGNGIQVR  HLA-A*11:01,HLA-A*31:01,HLA-A*33:01
ALFFIIFNK   HLA-A*03:01,HLA-A*11:01,HLA-A*68:01
GVSENIFLK   HLA-A*03:01,HLA-A*11:01,HLA-A*68:01
HVLSHNSYEK  HLA-A*03:01,HLA-A*11:01,HLA-A*68:01
LLACAGLAYK  HLA-A*03:01,HLA-A*11:01,HLA-A*68:01
FILVNLLIFH  HLA-A*33:01,HLA-A*68:01
TPYAGEPAPF  HLA B*07:02,HLA B*35:01,HLA B*35:08,HLA B*51:01,HLA B*53:01
LPYGRTNL    HLA B*07:02,HLA B*51:01,HLA B*54:01
LPSENERGY   HLA B*35:08
```

- **Population(s) / Area(s)**

选择一个或多个人口/地区进行计算。

- **User population**

可以通过 "Add user population(s)" 添加自定义人群。文件以 tab 分隔：

- 第一行为标题行，前三列是必须的，分别为 "MHC class", "MHC locus" 和 "MHC allele"，后面为 population 名称。
	- 第一列 MHC class 的值为 I 或 II
	- 第二列 MHC locus 的值为 HLA-A, HLA-B 等
	- 第三列 MHC allele 为 `HLA-A*01:01`, `HLA-A*02:01`, ... 
- 余下列指定不同人群中等位基因基因型频率，值从 0 到 1

示例文件：

```
MHC Class	MHC Locus	MHC Allele	Asian	Black	European-Caucasian	North-America-Caucasian
I	HLA-A	HLA-A*01:01	0.007594	0.035415	0.167566	0.159952
I	HLA-A	HLA-A*02:01	0.082624	0.103242	0.258922	0.175362
I	HLA-A	HLA-A*02:02	0.000944	0.044661	0.007503	0.018633
I	HLA-A	HLA-A*02:03	0.044386	0.001166	0.001180	0.020772
I	HLA-A	HLA-A*02:05	0.001455	0.018778	0.013118	0.016581
I	HLA-A	HLA-A*02:06	0.055333	0.003050	0.001180	0.040005
I	HLA-A	HLA-A*02:07	0.055651	0.003824	0.001239	0.017781
I	HLA-A	HLA-A*03:01	0.006457	0.075907	0.144457	0.139229
I	HLA-A	HLA-A*11:01	0.195719	0.005565	0.059346	0.064107
I	HLA-A	HLA-A*23:01	0.001031	0.094016	0.015911	0.022698
I	HLA-A	HLA-A*24:02	0.289243	0.021283	0.086281	0.081162
I	HLA-A	HLA-A*29:02	0.002698	0.025873	0.031881	0.029116
I	HLA-A	HLA-A*30:02	0.010957	0.167618	0.023630	0.024692
I	HLA-A	HLA-A*31:01	0.041698	0.006330	0.025705	0.022621
I	HLA-A	HLA-A*32:01	0.003190	0.053094	0.035382	0.029048
I	HLA-A	HLA-A*33:01	0.085544	0.054853	0.011240	0.018536
I	HLA-A	HLA-A*68:01	0.002602	0.035635	0.030524	0.025515
I	HLA-A	HLA-A*68:02	0.001176	0.049107	0.006589	0.010822
I	HLA-B	HLA-B*07:02	0.028378	0.071702	0.133564	0.137727
I	HLA-B	HLA-B*08:01	0.001975	0.025022	0.115568	0.098939
I	HLA-B	HLA-B*18:01	0.004567	0.025998	0.048107	0.040104
I	HLA-B	HLA-B*27:05	0.022683	0.019458	0.043063	0.035351
I	HLA-B	HLA-B*35:01	0.047747	0.046201	0.083716	0.091069
I	HLA-B	HLA-B*40:01	0.131705	0.005201	0.043731	0.035797
I	HLA-B	HLA-B*40:02	0.072184	0.005966	0.021939	0.025439
I	HLA-B	HLA-B*44:02	0.008721	0.009772	0.084896	0.087797
I	HLA-B	HLA-B*44:03	0.032425	0.096600	0.051205	0.039117
I	HLA-B	HLA-B*45:01	0.000540	0.057025	0.006756	0.008518
I	HLA-B	HLA-B*51:01	0.062760	0.023168	0.054903	0.047645
I	HLA-B	HLA-B*53:01	0.000877	0.102308	0.003216	0.006234
I	HLA-B	HLA-B*54:01	0.043998	0.000535	0.000551	0.000542
```

- **Calculation option(s)**

选择针对哪种 MHC 计算人群覆盖率。

## 示例

- 输入

![[Pasted image 20230615144319.png]]

- 输出

![[Pasted image 20230615144345.png]]

不同人群的 HLA 等位基因频率来源：来自世界各地研究的不同人群的 HLA 等位基因频率和相关数据由 allelefrequencies.net 数据库提供。根据地理位置、国家和种族将人群划分为一个分层结构，上层的等位基因频率信息由下层的合并而来。

统计分辨率达到 2 组数字的等位基因，如 `HLA-A*01:01`。忽略分辨率小于 2 组的等位基因，如 `HLA-A*07`, `HLA-A*09` 等。将分辨率大于 2 组的等位基因合并到 2 组。

等位基因频率通过估计每组群体中等位基因的总拷贝数 (a) 和主体数 (n)，频率 $AF=a/2n$。最终数据集包含 3245 个等位基因（包括 I 和 II），涵盖全球 16 个地区、21 个民族、115 个国家。

## 参考

- http://tools.iedb.org/population/help/

[^1]: https://pubmed.ncbi.nlm.nih.gov/16545123/