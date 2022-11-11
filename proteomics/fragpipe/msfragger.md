# MSFragger

- [MSFragger](#msfragger)
  - [简介](#简介)
  - [使用要求](#使用要求)
  - [安装](#安装)
  - [参数设置](#参数设置)
  - [运行 MSFragger](#运行-msfragger)
  - [参考](#参考)

***

## 简介

MSFragger 是一个超快数据库检索工具，用于基于质谱的蛋白质组学肽段鉴定。MSFragger 的速度使其特别适合分析大型数据集（包括 timsTOF 数据）、无酶约束检索、以及开放检索。

使用 MSFragger 的方式有三种：

1. 在 FragPipe 中使用
2. 在 ProteomeDiscoverer 中使用
3. 作为单独的 JAR 使用，或通过 philosopher

不管哪种情况，都需要 MSFragger JAR 文件。在[这里](https://github.com/Nesvilab/MSFragger/tree/master/parameter_files)可以看到示例参数文件。

MSFragger 用跨平台的 Java 实现，兼容标准开放的质谱数据格式（mzXML/mzML）。独立的 JAR 和 ProteomeDiscoverer 节点现在也支持 Thermo RAW 文件。MSFragger 输出 pepXML 或 tsv 格式，很容易与下游数据分析兼容。

## 使用要求

**输入文件**

MSFragger 支持 [.mzML](https://fragpipe.nesvilab.org/docs/tutorial_convert.html), Thermo .raw 和 Bruker timsTOF .d 谱图文件格式。

**硬件**

MSFragger 由于内存片段索引技术，需要大量内存。建议至少 8-16 GB 内存，对复杂的 closed 检索和 open 检索，需要更多内存。

MSFragger 对处理器的要求取决于搜索的复杂性。对 open 检索（500 Da 母离子质量窗口），使用人蛋白质组，采用 tryptic 酶切，单核一小时大约能搜 40,000 张 MS/MS 谱图。MSFragger 支持多线程检索，在 28 核工作站单个文件只要 2 分钟。

**操作系统**

MSFragger 已经在 Mac OS X, Windows 7 和许多 Linux 发行版上进行了测试。注意，需要 64 位操作系统，这样才能访问超过 4 GB 内存。

**Java**

MSFragger 使用 Java 1.8 编写，需要安装 Java。

## 安装

MSFragger 是 Java 程序，其实不用安装。

如果要直接读取 Thermo (.raw) 或 Bruker (.d) 谱图文件，下载 .zip 版本解压。JAR 文件和 ext 目录在同一个文件夹即可。

## 参数设置

**常规参数**

|参数|说明|默认值|
|---|---|---|
|num_threads|CPU 线程数，应该设置为逻辑处理器数量。0 表示设置为可用处理器数|0|
|database_name|FASTA 格式的蛋白质数据库文件路径，必须包含 decoy 序列||

**检索参数**

|参数|说明|默认值|
|---|---|---|
|precursor_mass_lower|Lower bound of the precursor mass window|-20|
|precursor_mass_upper|Upper bound of the precursor mass window|20|
|precursor_mass_units|Precursor mass tolerance units (0 for Da, 1 for ppm)|1|
|precursor_true_tolerance|True precursor mass tolerance (window is +/- this value). Used for tie breaker of results (in spectral ambiguous cases), zero bin boosting in open searches (0 disables these features), and mass calibration. This option is STRONGLY recommended for open searches.|20|
|precursor_true_units|True precursor mass tolerance units (0 for Da, 1 for ppm).|1|
|fragment_mass_tolerance|Fragment mass tolerance (window is +/- this value).|20|
|fragment_mass_units|Fragment mass tolerance units (0 for Da, 1 for ppm).|1|
|calibrate_mass|质量校正 (0 for OFF, 1 for ON, 2 for ON and find optimal parameters)|2|
|write_calibrated_mgf|Write calibrated spectra to MGF files (0 for no and 1 for yes).|0|
|decoy_prefix|Prefix of the decoy protein entries. Used for parameter optimization only.||
|isotope_error|Isotope correction for MS/MS events triggered on isotopic peaks. Should be set to 0 (disabled) for open search or 0/1/2 for correction of narrow window searches. Shifts the precursor mass window to multiples of this value multiplied by the mass of C13-C12.|0|
|mass_offsets|Creates multiple precursor tolerance windows with specified mass offsets. These values are multiplexed with the isotope error option. For example, mass_offsets = 0/79.966 can be used as a restricted 'open' search that looks for unmodified and phosphorylated peptides. Setting isotope_error to 0/1/2 in combination with this example will create search windows around (0, 1, 2, 79.966, 80.966, 81.966).|0|
|precursor_mass_mode|One of isolated/selected/recalculated. Isolated uses the isolation m/z, selected uses the selected m/z, while recalculated uses a recalculated m/z from .ma files within the same directory. If the desired m/z type is not present for a scan, it will default to whatever m/z is available.|selected|
|localize_delta_mass|Generate and use mass difference fragment index in addition to the regular fragment index for search. This allows shifted fragment ions - fragment ions with mass increased by the calculated mass difference, to be included in scoring.|0|
|delta_mass_exclude_ranges|Exclude mass range for searching with delta mass to remove double counting of fragments in chimeric spectra and instances of monoisotopic error.|(-1.5, 3.5)|
|fragment_ion_series|Ion series used in search. Can be the combinations of a, b, c, x, y, z, b-18, or y-18.|b,y|
|precursor_charge|<li>When override_charge is set to 0, use the original precursor charge if there is one in the spectral file, or try the charge states in the specified range if there is no precursor charge in the spectral file.<li>When override_charge is set to 1, always try the charge states in the specified range|1 4|
|override_charge|Ignores precursor charge and uses charge state specified in precursor_charge range (0 or 1).|0|
|max_fragment_charge|Maximum charge state for theoretical fragments to match (1-4).|2|

**理论酶切参数**

|参数|说明|默认值|
|---|---|---|
|search_enzyme_name|<li>Name of enzyme to be written to the pepXML file. A complete list of enzymes can be found at the bottom of this page. Note that the enzyme name (and cleavage rules) must exactly match for downstream processing to run properly.<li>For Nonspecific searches, please use `nonspecific` as the enzyme name.|trypsin|
|search_enzyme_cutafter|Residues after which the enzyme cuts (specified as a string of amino acids). Must correspond to the `search_enzyme_name` (see a list of supported enzymes at the bottom of [this page](https://github.com/Nesvilab/philosopher/wiki/PeptideProphet)).|KR|
|search_enzyme_butnotafter|Residues that the enzyme will not cut before (misnomer: should really be called butnotbefore). Must correspond to the search_enzyme_name|P|
|num_enzyme_termini|Number of enzyme termini (0 for non-enzymatic, 1 for semi-enzymatic, and 2 for fully-enzymatic).|2|
|allowed_missed_cleavage|Allowed number of missed cleavages.|1|
|digest_min_length|Minimum length of peptides to be generated during in silico digestion.|7|
|digest_max_length|Maximum length of peptides to be generated during in silico digestion.|50|
|digest_mass_range|Mass range of peptides to be generated during in silico digestion in Daltons (specified as a space separated range).|500.0 5000.0|

**可变修饰**

|参数|说明|默认值|
|---|---|---|
|clip_nTerm_M|Specifies the trimming of a protein N-terminal methionine as a variable modification (0 or 1).|1|
|variable_mod_01 .. 16|Sets variable modifications (variable_mod_01 to variable_mod_16). Space separated values with 1st value being the modification mass and the second being the residues (specified consecutively as a string) it modifies.|
|allow_multiple_variable_mods_on_residue|Allow each amino acid to be modified by multiple variable modifications (0 or 1).|0|
|max_variable_mods_per_peptide|Maximum total number of variable modifications per peptide. (maximum of 5).|3|
|max_variable_mods_combinations|Maximum allowed number of modified variably modified peptides from each peptide sequence, (maximum of 65534). If a greater number than the maximum is generated, only the unmodified peptide is considered.|5000|

```txt
* is used to represent any amino acid
^ is used to represent a terminus
[ is a modifier for protein N-terminal
] is a modifier for protein C-terminal
n is a modifier for peptide N-terminal
c is a modifier for peptide C-terminal
```

语法示例

```txt
15.9949 M 3 (for oxidation on methionine)
79.66331 STY 3 (for phosphorylation)
-17.0265 nQnC 3 (for pyro-Glu or loss of ammonia at peptide N-terminal)
n^ (put the modification on the peptide N-terminus itself)
n* (put it on any amino acid that is located at peptide N-terminus (vs. e.g. -17 nQ that puts it on N-terminal Q only). There may not be a difference in the results but there is a big difference in the number of peptide candidates generated for scoring.)
```

默认

```txt
variable_mod_01 = 15.9949 M 3
variable_mod_02 = 42.0106 [^ 1
```

**Spectral Processing**

minimum_peaks
Minimum number of peaks in experimental spectrum for matching.
Default: 15
use_topN_peaks
Pre-process experimental spectrum to only use top N peaks.
Default: 150
minimum_ratio
Filters out all peaks in experimental spectrum less intense than this multiple of the base peak intensity.
Default: 0.01
clear_mz_range
Removes peaks in this m/z range prior to matching. Useful for iTRAQ/TMT experiments (i.e., 0.0 150.0).
Default: 0.0 0.0
excluded_scan_list_file
Takes the path of a text file containing scan names. MSFragger would skip those scans if the path is not empty. Comment or delete this parameter's name and its value if you don't want to use it.
Default: This parameter is commented in fragger.params file.
remove_precursor_peak
Remove precursor peaks from tandem mass spectra. 0 = not remove; 1 = remove the peak with the precursor charge; 2 = remove the peaks with all charge states.
Default: 0
remove_precursor_range
m/z range in removing precursor peaks. Unit: Da.
Default: -1.5,1.5
intensity_transform
If need to transform peak intensities with sqrt root. 0 = not transform; 1 = transform using sqrt root.
Default: 0
deisotope
Deisotoping MS/MS spectra. 0 = not deisotope; 1 = Deisotope and assume singleton peaks singly charged; 2 = Deisotope, and assume singleton peaks singly or doubly charged.
Default: 1

**Open Search**

|参数|说明|默认值|
|---|---|---|
|track_zero_topN|额外记录 top N 个无修饰肽段结果，以增强特征。如果需要 zero bin boosting，，则应设置为大于 `output_report_topN` 的数|0|
|zero_bin_accept_expect|如果
Ranks a zero-bin hit above all non-zero-bin hit if it has expectation less than this value.
Default: 0.0
zero_bin_mult_expect
Multiplies expect value of PSMs in the zero-bin during results ordering (set to less than 1 for boosting).
Default: 1.00
add_topN_complementary
Inserts complementary ions corresponding to the top N most intense fragments in each experimental spectra. Useful for recovery of modified peptides near C-terminal in open search. Should be set to 0 (disabled) otherwise.
Default: 0

**Modeling And Output**

|参数|说明|默认值|
|---|---|---|
|min_fragments_modelling|用于统计建模的 PSM 要求的最小匹配峰数|2|
|min_matched_fragments|输出 PSM 要求的最小匹配峰数|4|
|output_file_extension|输出文件扩展名|pepXML|
|output_format|输出文件格式 (pepXML 或 tsv)|pepXML|
|output_report_topN|每个输入谱图输出 PSM 数|1|
|output_max_expect|如果最高 E 值大于该阈值，不输出 PSM|50.0|
|report_alternative_proteins|对在多个蛋白质中存在的肽段，报告其它蛋白（0 表示否，1表示是）|0|

**固定修饰**

|参数|说明|默认值|
|---|---|---|
|add_Cterm_peptide|肽段 C 端固定修饰 Da|0.0|
|add_Nterm_peptide|肽段 N 端固定修饰 Da|0.0|
|add_Cterm_protein|蛋白 C 端固定修饰 Da|0.0|
|add_Nterm_protein|蛋白 N 端固定修饰 Da|0.0|
|add_C_cysteine|添加到半胱氨酸 C 上的固定修饰|57.021460|
|add_X_usertext|添加到其它氨基酸上的固定修饰|0.0|

例如：

```txt
add_C_cysteine = 57.021464
add_K_lysine = 144.1021
```

## 运行 MSFragger

```powershell
java -Xmx32g -jar MSFragger.jar <parameter file> <list of mzML/mzXML files>
```

或者：

```powershell
java -Xmx32g -jar MSFragger.jar <options> <list of mzML/mzXML files>
```

## 参考

- https://github.com/Nesvilab/MSFragger/wiki
