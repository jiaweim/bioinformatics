# Seq

- [Seq](#seq)
  - [1. 简介](#1-简介)
  - [2. 类似字符串](#2-类似字符串)
  - [3. 切片](#3-切片)
  - [4. 转换为字符串](#4-转换为字符串)
  - [5. 串联序列](#5-串联序列)
  - [6. 大小写](#6-大小写)
  - [7. 核酸序列反向互补](#7-核酸序列反向互补)
  - [8. 转录](#8-转录)
  - [9. 翻译](#9-翻译)
  - [10. 翻译表](#10-翻译表)
  - [11. Seq 对象对比](#11-seq-对象对比)
  - [12. 内容未知的序列](#12-内容未知的序列)
  - [13. MutableSeq](#13-mutableseq)
  - [14. 直接操作字符串](#14-直接操作字符串)
  - [15. 方法](#15-方法)
    - [find](#find)
    - [index](#index)

Last updated: 2022-06-17, 13:55
@author Jiawei Mao
****

## 1. 简介

Biopython 使用 `Seq` 对象包装序列。`SeqRecord` 在 `Seq` 的基础上添加了注释信息。

序列本质上是类似 `AGTACACTGGT` 的字符串，`Seq` 对象和 Python 字符串最重要的区别是它们具有不同的方法。虽然 `Seq` 对象的许多方法与 Python 字符串的方法相同，但它还有一些特有方法，如 `translate()` 进行翻译，`reverse_complement()` 反向互补等。

## 2. 类似字符串

大多时候可以像处理 Python 字符串一样处理 `Seq` 对象。例如，查看长度、迭代元素：

```py
>>> from Bio.Seq import Seq
>>> my_seq = Seq("GATCG")
>>> for index, letter in enumerate(my_seq):
...     print("%i %s" % (index, letter))
0 G
1 A
2 T
3 C
4 G
>>> print(len(my_seq))
5
```

也可以像访问字符串一样访问序列的元素：

```python
>>> print(my_seq[0]) #first letter
G
>>> print(my_seq[2]) #third letter
T
>>> print(my_seq[-1]) #last letter
G
```

`Seq` 对象包含类似字符串的 `.count()` 方法，用于非重叠计数。例如：

```python
>>> from Bio.Seq import Seq
>>> "AAAA".count("AA")
2
>>> Seq("AAAA").count("AA")
2
```

单字符计数：

```python
>>> from Bio.Seq import Seq
>>> my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
>>> len(my_seq)
32
>>> my_seq.count("G")
9
>>> 100 * float(my_seq.count("G") + my_seq.count("C")) / len(my_seq)
46.875
```

可以使用上面的代码计算 GC%，不过 `Bio.SeqUtils` 提供了更便捷的函数：

```python
>>> from Bio.Seq import Seq
>>> from Bio.SeqUtils import GC
>>> my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
>>> GC(my_seq)
46.875
```

`Bio.SeqUtils.GC()` 会自动处理大小写问题和模糊碱基问题，例如 `S` 表示 G 或 C。

> [!IMPORTANT]
> `Seq` 和 Python 字符串一样，是只读的。如果要编辑序列，要么创建新的 `Seq`，要么使用 `MutableSeq` 对象。

## 3. 切片

序列切片：

```python
>>> from Bio.Seq import Seq
>>> my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
>>> my_seq[4:12]
Seq(GATGGGCC)
```

`Seq` 与 Python 字符串的索引规则一样，对切片索引采用前闭后开的原则，即包含开始索引的元素，不包含结尾索引的元素。

`Seq` 也可以采用 `start`, `stop`, `stride` 参数进行切片。例如，获得 DNA 序列的第 1、2、3 个密码子的位置：

```python
>>> my_seq[0::3]
Seq(GCTGTAGTAAG)
>>> my_seq[1::3]
Seq(AGGCATGCATC)
>>> my_seq[2::3]
Seq(TAGCTAAGAC)
```

也可以反向切片：

```python
>>> my_seq[::-1]
Seq(CGCTAAAAGCTAGGATATATCCGGGTAGCTAG)
```

## 4. 转换为字符串

在许多场景需要将 `Seq` 对象转换为字符串。使用 `str()` 方法即可：

```python
>>> str(my_seq)
'GATCGATGGGCCTATATAGGATCGAAAATCGC'
```

使用 `print` 函数也可以打印完整序列：

```python
>>> print(my_seq)
GATCGATGGGCCTATATAGGATCGAAAATCGC
```

也可以在 Python 格式化字符串中使用 `%s` 占位符：

```python
>>> fasta_format_string = ">Name\n%s\n" % my_seq
>>> print(fasta_format_string)
>Name
GATCGATGGGCCTATATAGGATCGAAAATCGC
<BLANKLINE>
```

## 5. 串联序列

从 Biopython 1.78 开始，可以直接将两个 `Seq` 对象串在一起：

```python
>>> from Bio.Seq import Seq
>>> protein_seq = Seq("EVRNAK")
>>> dna_seq = Seq("ACGT")
>>> protein_seq + dna_seq
Seq('EVRNAKACGT')
```

如果要将很多序列串在一起，可以用 for 循环：

```python
>>> from Bio.Seq import Seq
>>> list_of_seqs = [Seq("ACGT"), Seq("AACC"), Seq("GGTT")]
>>> concatenated = Seq("")
>>> for s in list_of_seqs:
...      concatenated += s
...
>>> concatenated
Seq('ACGTAACCGGTT')
```

也可以用 `.join` 方法：

```python
>>> from Bio.Seq import Seq
>>> contigs = [Seq("ATG"), Seq("ATCCCG"), Seq("TTGCA")]
>>> spacer = Seq("N"*10)
>>> spacer.join(contigs)
Seq('ATGNNNNNNNNNNATCCCGNNNNNNNNNNTTGCA')
```

## 6. 大小写

用 `upper` 和 `lower` 方法转换大小写：

```python
>>> from Bio.Seq import Seq
>>> dna_seq = Seq("acgtACGT")
>>> dna_seq
Seq('acgtACGT')
>>> dna_seq.upper()
Seq('ACGTACGT')
>>> dna_seq.lower()
Seq('acgtacgt')
```

转换大小写，有利于不区分大小写进行匹配：

```python
>>> "GTAC" in dna_seq
False
>>> "GTAC" in dna_seq.upper()
True
```

## 7. 核酸序列反向互补

对核酸序列，可以使用内置方法获得 `Seq` 对象的互补或反向互补序列：

```python
>>> from Bio.Seq import Seq
>>> my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
>>> my_seq
Seq('GATCGATGGGCCTATATAGGATCGAAAATCGC')
>>> my_seq.complement()
Seq('CTAGCTACCCGGATATATCCTAGCTTTTAGCG')
>>> my_seq.reverse_complement()
Seq('GCGATTTTCGATCCTATATAGGCCCATCGATC')
```

如前所述，可以用反向切片获得反向序列：

```python
>>> my_seq[::-1]
Seq('CGCTAAAAGCTAGGATATATCCGGGTAGCTAG')
```

如果不小心对蛋白质序列做反向互补，虽然可能有结果，但没有任何生物学意义：

```python
>>> from Bio.Seq import Seq
>>> protein_seq = Seq("EVRNAK")
>>> protein_seq.complement()
Seq('EBYNTM')
```

其中 `E` 不是 IUPAC 有效的核苷酸代码，因此没有互补。但是 `V` 表示 "A", "C" 或 "G"，其互补为 "B"，其它类似。

## 8. 转录

genbank 数据库保存的为正义链（sense strand），也称为 coding strand。如下所示：

```txt
   DNA coding strand (aka Crick strand, strand +1)
5’  ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG  3’
    |||||||||||||||||||||||||||||||||||||||
3’  TACCGGTAACATTACCCGGCGACTTTCCCACGGGCTATC  5’
   DNA template strand (aka Watson strand, strand −1)
 
                        |
                  Transcription
                        ↓
 
5’  AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG  3’
       Single stranded messenger RNA
```

这是一段双链 DNA 片段，编码一条肽段。转录从模板链（template strand）开始，通过反向互补生成 mRNA。但是，在 Biopython 和其它生信工具中，通常直接使用编码链，替换 `T -> U` 就获得了 mRNA 序列。

下面演示用 Biopython 进行转录，首先创建编码链和模板链，序列和上图一致：

```python
>>> from Bio.Seq import Seq
>>> coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
>>> coding_dna
Seq('ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG')
>>> template_dna = coding_dna.reverse_complement()
>>> template_dna
Seq('CTATCGGGCACCCTTTCAGCGGCCCATTACAATGGCCAT')
```

> [!NOTE]
> 核苷酸一般从 5'->3' 方向读取，上图中模板链是 3'->5' 显示的

然后，用 `Seq` 的 `transcribe` 方法转录生成 mRNA：

```python
>>> coding_dna
Seq('ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG')
>>> messenger_rna = coding_dna.transcribe()
>>> messenger_rna
Seq('AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG')
```

可以发现，只是将 T 替换成了 U，即 `transcribe()` 的功能，就是将 `T` 替换为 `U`。

如果想和生物转录过程一样，从模板链开始，则可以分两步进行：

```python
>>> template_dna.reverse_complement().transcribe()
Seq('AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG')
```

`Seq` 还包含从 mRNA 到 DNA 编码链的反转录方法。即将 U 替换为 T：

```python
>>> from Bio.Seq import Seq
>>> messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
>>> messenger_rna
Seq('AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG')
>>> messenger_rna.back_transcribe()
Seq('ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG')
```

## 9. 翻译

还是用上面的示例，现在将 mRNA 翻译为蛋白质序列：

```python
>>> from Bio.Seq import Seq
>>> messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
>>> messenger_rna
Seq('AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG')
>>> messenger_rna.translate()
Seq('MAIVMGR*KGAR*')
```

也可以直接从 DNA 编码链进行翻译：

```python
>>> from Bio.Seq import Seq
>>> coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
>>> coding_dna
Seq('ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG')
>>> coding_dna.translate()
Seq('MAIVMGR*KGAR*')
```

上面的蛋白质序列，除了最后的终止符 `*`（对应终止密码子），中间也有一个终止符。这里是故意这么设计的，用来引出 `translate` 的翻译表参数。

Biopython 的翻译表来自 [NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi)，默认使用 `standard` 遗传密码。如果你正在处理线粒体序列，就需要告诉 `translate` 所需的翻译表：

```python
>>> coding_dna.translate(table="Vertebrate Mitochondrial")
Seq('MAIVMGRWKGAR*')
```

也可以使用密码子表在 NCBI 中的编号，通常包含在 GenBank 文件的 feature 注释中：

```python
>>> coding_dna.translate(table=2)
Seq('MAIVMGRWKGAR*')
```

设置 `to_stop=True` 表示遇到终止密码子就停止翻译，例如：

```python
>>> coding_dna.translate()
Seq('MAIVMGR*KGAR*')
>>> coding_dna.translate(to_stop=True)
Seq('MAIVMGR')
>>> coding_dna.translate(table=2)
Seq('MAIVMGRWKGAR*')
>>> coding_dna.translate(table=2, to_stop=True)
Seq('MAIVMGRWKGAR')
```

> [!NOTE]
> 使用 `to_stop` 参数时，终止密码子不会翻译，即终止符不会包含在蛋白序列中

如果不喜欢默认 `*`，可以用 `stop_symbol` 自定义终止符：

```python
>>> coding_dna.translate(table=2, stop_symbol="@")
Seq('MAIVMGRWKGAR@')
```

对完整编码序列 CDS，以起始密码子开始，以终止密码子结尾，长度为 3 的倍数，并且内部没有 in-frame 终止密码子。一般来说使用默认的翻译方法即可（也可以加上 `to_stop` 选项）。然而，如果你的序列不是标准的起始密码子呢？这种情况在细菌中很常见，如大肠杆菌 K12 的 yaaX 基因。

```python
>>> from Bio.Seq import Seq
>>> gene = Seq("GTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCA"
...            "GCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGAT"
...            "AATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACAT"
...            "TATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCAT"
...            "AAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAA")
>>> gene.translate(table="Bacterial")
Seq('VKKMQSIVLALSLVLVAPMAAQAAEITLVPSVKLQIGDRDNRGYYWDGGHWRDH...HR*',
ProteinAlpabet())
>>> gene.translate(table="Bacterial", to_stop=True)
Seq('VKKMQSIVLALSLVLVAPMAAQAAEITLVPSVKLQIGDRDNRGYYWDGGHWRDH...HHR')
```

在细菌遗传密码中，`GTG` 是一个有效的起始密码子，虽然它通常编码缬氨酸（Valine），但是作为起始密码子则应翻译为甲硫氨酸。因此需要使用 `cds` 参数告诉 Biopython 这是一段完整的 CDS：

```python
>>> gene.translate(table="Bacterial", cds=True)
Seq('MKKMQSIVLALSLVLVAPMAAQAAEITLVPSVKLQIGDRDNRGYYWDGGHWRDH...HHR')
```

使用此选项，Biopython 会检查序列是否是完整的 CDS，不是就抛出异常。

## 10. 翻译表

Biopython 内部使用的翻译表派生自 [NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi)。

在 Genbank 文件中，在 CDS 中使用 `/transl_table` 指定翻译表。

和前面一样，这里用标准翻译表和脊椎动物线粒体的翻译表演示。

```python
>>> from Bio.Data import CodonTable
>>> standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
>>> mito_table = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]
```

也可以使用翻译表的 NCBI 编号：

```python
>>> from Bio.Data import CodonTable
>>> standard_table = CodonTable.unambiguous_dna_by_id[1]
>>> mito_table = CodonTable.unambiguous_dna_by_id[2]
```

输出两个翻译表进行对比：

```python
>>> print(standard_table)
Table 1 Standard, SGC0

  |  T      |  C      |  A      |  G      |
--+---------+---------+---------+---------+--
T | TTT F   | TCT S   | TAT Y   | TGT C   | T
T | TTC F   | TCC S   | TAC Y   | TGC C   | C
T | TTA L   | TCA S   | TAA Stop| TGA Stop| A
T | TTG L(s)| TCG S   | TAG Stop| TGG W   | G
--+---------+---------+---------+---------+--
C | CTT L   | CCT P   | CAT H   | CGT R   | T
C | CTC L   | CCC P   | CAC H   | CGC R   | C
C | CTA L   | CCA P   | CAA Q   | CGA R   | A
C | CTG L(s)| CCG P   | CAG Q   | CGG R   | G
--+---------+---------+---------+---------+--
A | ATT I   | ACT T   | AAT N   | AGT S   | T
A | ATC I   | ACC T   | AAC N   | AGC S   | C
A | ATA I   | ACA T   | AAA K   | AGA R   | A
A | ATG M(s)| ACG T   | AAG K   | AGG R   | G
--+---------+---------+---------+---------+--
G | GTT V   | GCT A   | GAT D   | GGT G   | T
G | GTC V   | GCC A   | GAC D   | GGC G   | C
G | GTA V   | GCA A   | GAA E   | GGA G   | A
G | GTG V   | GCG A   | GAG E   | GGG G   | G
--+---------+---------+---------+---------+--
```

以及：

```python
>>> print(mito_table)
Table 2 Vertebrate Mitochondrial, SGC1

  |  T      |  C      |  A      |  G      |
--+---------+---------+---------+---------+--
T | TTT F   | TCT S   | TAT Y   | TGT C   | T
T | TTC F   | TCC S   | TAC Y   | TGC C   | C
T | TTA L   | TCA S   | TAA Stop| TGA W   | A
T | TTG L   | TCG S   | TAG Stop| TGG W   | G
--+---------+---------+---------+---------+--
C | CTT L   | CCT P   | CAT H   | CGT R   | T
C | CTC L   | CCC P   | CAC H   | CGC R   | C
C | CTA L   | CCA P   | CAA Q   | CGA R   | A
C | CTG L   | CCG P   | CAG Q   | CGG R   | G
--+---------+---------+---------+---------+--
A | ATT I(s)| ACT T   | AAT N   | AGT S   | T
A | ATC I(s)| ACC T   | AAC N   | AGC S   | C
A | ATA M(s)| ACA T   | AAA K   | AGA Stop| A
A | ATG M(s)| ACG T   | AAG K   | AGG Stop| G
--+---------+---------+---------+---------+--
G | GTT V   | GCT A   | GAT D   | GGT G   | T
G | GTC V   | GCC A   | GAC D   | GGC G   | C
G | GTA V   | GCA A   | GAA E   | GGA G   | A
G | GTG V(s)| GCG A   | GAG E   | GGG G   | G
--+---------+---------+---------+---------+--
```

还可以查询终止密码子和起始密码子：

```python
>>> mito_table.stop_codons
['TAA', 'TAG', 'AGA', 'AGG']
>>> mito_table.start_codons
['ATT', 'ATC', 'ATA', 'ATG', 'GTG']
>>> mito_table.forward_table["ACG"]
'T'
```

可以在 [Codon Usage Database](http://www.kazusa.or.jp/codon/) 查询物种使用的各个密码子的比例。

## 11. Seq 对象对比

序列比较是一个比较复杂的问题，并没有简单的方法来判断两个序列是否相等。因为一条序列中字母的意义依赖于上下文，例如字母 "A" 可能属于 DNA、RNA 或蛋白质序列。

那么，DNA 片段 "ACG" 和 RNA 片段 "ACG" 是否相等？还有肽段 "ACG"，字符串 "ACG"？在日常使用中，处理的一般是相同类型序列，即全部都是 DNA、RNA 或蛋白质。自 Biopython 1.65，只比价序列字符，和 Python 字符串一样：

```python
>>> from Bio.Seq import Seq
>>> seq1 = Seq("ACGT")
>>> "ACGT" == seq1
True
>>> seq1 == "ACGT"
True
```

作为扩展，在 Python dict 可以用 `Seq` 作为 key，与字符串作为 key 效果一样。

## 12. 内容未知的序列

在某些情况下，可能知道序列长度，但是不知道实际序列。例如，在 GenBank 和 EMBL 文件中，可能只有基因组 DNA 序列的配置信息，而没有具体序列。对这类序列，可以将 `None` 作为参数创建 `Seq` 对象；

```python
>>> from Bio.Seq import Seq
>>> unknown_seq = Seq(None, 10)
```

对这类序列，如果访问 `Seq` 的内容，抛出 `UndefinedSequenceError`:

```python
>>> unknown_seq
Seq(None, length=10)
>>> len(unknown_seq)
10
>>> print(unknown_seq)
Traceback (most recent call last):
...
Bio.Seq.UndefinedSequenceError: Sequence content is undefined
>>>
```

## 13. MutableSeq

与 Python 字符串一样，`Seq` 对象是只读的，即不可变（immutable）：

```python
>>> from Bio.Seq import Seq
>>> my_seq = Seq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA")
```

如果修改序列，会抛出错误：

```python
>>> my_seq[5] = "G"
Traceback (most recent call last):
...
TypeError: 'Seq' object does not support item assignment
```

将其转换为可变序列 `MutableSeq` 对象，就可以随意修改：

```python
>>> from Bio.Seq import MutableSeq
>>> mutable_seq = MutableSeq(my_seq)
>>> mutable_seq
MutableSeq('GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA')
```

或直接从字符串创建 `MutableSeq`：

```python
>>> mutable_seq
MutableSeq('GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA')
>>> mutable_seq[5] = "C"
>>> mutable_seq
MutableSeq('GCCATCGTAATGGGCCGCTGAAAGGGTGCCCGA')
>>> mutable_seq.remove("T")
>>> mutable_seq
MutableSeq('GCCACGTAATGGGCCGCTGAAAGGGTGCCCGA')
>>> mutable_seq.reverse()
>>> mutable_seq
MutableSeq('AGCCCGTGGGAAAGTCGCCGGGTAATGCACCG')
```

> [!CAUTION]
> `MutableSeq` 的 `reverse_complement()` 和 `reverse()` 等方法都是原位操作。

由于是可变对象，所以 `MutableSeq` 不能作为 dict 的 key。

修改完序列，可以将 `MutableSeq` 转换成只读的 `Seq`：

```python
>>> from Bio.Seq import Seq
>>> new_seq = Seq(mutable_seq)
>>> new_seq
Seq('AGCCCGTGGGAAAGTCGCCGGGTAATGCACCG')
```

## 14. 直接操作字符串

如果确实不想用 `Seq` 对象，或者说更喜欢函数式编程，在 `Bio.Seq` 中包含各种函数，除了可用于 `Seq`、`MutableSeq` 对象，也可以直接对字符串进行操作：

```python
>>> from Bio.Seq import reverse_complement, transcribe, back_transcribe, translate
>>> my_string = "GCTGTTATGGGTCGTTGGAAGGGTGGTCGTGCTGCTGGTTAG"
>>> reverse_complement(my_string)
'CTAACCAGCAGCACGACCACCCTTCCAACGACCCATAACAGC'
>>> transcribe(my_string)
'GCUGUUAUGGGUCGUUGGAAGGGUGGUCGUGCUGCUGGUUAG'
>>> back_transcribe(my_string)
'GCTGTTATGGGTCGTTGGAAGGGTGGTCGTGCTGCTGGTTAG'
>>> translate(my_string)
'AVMGRWKGGRAAG*'
```

## 15. 方法

### find

```py
def find(self, sub, start=None, end=None)
```

同 [index 方法](#index)。

### index

```py
def index(self, sub, start=None, end=None)
```

返回子序列 `sub` 第一次出现的位置。可选参数 `start` 和 `end` 用于指定查找的范围。

这个方法和 'find' 功能一样，只是在没有找到子序列 `sub` 时，`find` 方法返回 -1，而 `index` 抛出 `ValueError`。

**例1**，查找 'AUG' 第一次出现的位置：

```py
>>> from Bio.Seq import Seq
>>> my_rna = Seq("GUCAUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAGUUG")
>>> my_rna.index("AUG")
3
```

**例2**，指定 `start`，可以避开第一个，查找后面的 'AUG'：

```py
>>> my_rna.index("AUG", 4)
15
```

**例3**，抛出 `ValueError`：

```py
>>> my_rna.index("T")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "D:\Python\Python39\lib\site-packages\Bio\Seq.py", line 797, in index
    return self._data.index(sub, start, end)
ValueError: subsection not found
>>> my_rna.find("T")
-1
```
