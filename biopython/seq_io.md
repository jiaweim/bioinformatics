# 序列 IO

- [序列 IO](#序列-io)
  - [解析或读取序列](#解析或读取序列)
    - [读取序列文件](#读取序列文件)
    - [迭代文件中的 record](#迭代文件中的-record)
    - [从文件到记录列表](#从文件到记录列表)
    - [提取数据](#提取数据)
    - [修改数据](#修改数据)
  - [2. 从压缩文件解析序列](#2-从压缩文件解析序列)
  - [从网络解析序列](#从网络解析序列)
    - [解析网络 GenBank 序列](#解析网络-genbank-序列)
    - [解析网络 SwissPro 序列](#解析网络-swisspro-序列)
  - [序列字典](#序列字典)
  - [输出序列文件](#输出序列文件)
    - [Round trips](#round-trips)
    - [序列格式转换](#序列格式转换)
    - [生成反向互补序列文件](#生成反向互补序列文件)
    - [格式化字符串](#格式化字符串)
  - [支持的文件格式](#支持的文件格式)

Last updated: 2022-06-21, 13:50
@author Jiawei Mao
***

## 解析或读取序列

函数 `Bio.SeqIO.parse()` 读取序列数据，返回 `SeqRecord` 对象。该函数包含两个参数：

1. 第一个参数是文件句柄或路径。
2. 第二个字符串参数指定序列格式

`Bio.SeqIO.parse()` 返回 `SeqRecord` 对象的迭代器。

对只包含一条序列的文件，可以使用 `Bio.SeqIO.read()`，参数和 `parse()` 相同，但是直接返回一个 `SeqRecord` 对象，如果文件包含多条序列，抛出异常。

### 读取序列文件

一般用 `Bio.SeqIO.parse()` 读取序列文件，返回 `SeqRecord` 对象，用 for 循环迭代。

- 例如，载入兰花的 DNA 序列的 FASTA 文件：

```py
from Bio import SeqIO

for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
```

- 解析 GenBank 格式

```py
from Bio import SeqIO

for seq_record in SeqIO.parse("ls_orchid.gbk", "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
```

- 也可以在 List 推导中使用 Python 迭代器

将文件中的 `SeqRecord` 放到 list 中

```py
>>> from Bio import SeqIO
>>> identifiers = [seq_record.id for seq_record in SeqIO.parse("ls_orchid.gbk", "genbank")]
>>> identifiers
[Z78533.1, Z78532.1, Z78531.1, Z78530.1, Z78529.1, Z78527.1, ..., Z78439.1]
```

### 迭代文件中的 record

因为 `SeqIO.parse` 返回的是迭代器，所以可以使用 `next()` 函数逐个查看序列。

```py
from Bio import SeqIO

record_iterator = SeqIO.parse("ls_orchid.fasta", "fasta")

first_record = next(record_iterator)
print(first_record.id)
print(first_record.description)

second_record = next(record_iterator)
print(second_record.id)
print(second_record.description)
```

如果没有元素了，继续调用 `next()` 抛出 `StopIteration` 异常。

如果文件里有多条记录，但是你只需要第一条，此时使用 `next` 非常简洁：

```py
from Bio import SeqIO

first_record = next(SeqIO.parse("ls_orchid.gbk", "genbank"))
```

### 从文件到记录列表

使用 `list()` 函数将记录迭代器转换为记录列表：

```py
from Bio import SeqIO

records = list(SeqIO.parse("ls_orchid.gbk", "genbank"))

print("Found %i records" % len(records))

print("The last record")
last_record = records[-1] # using Python
s list tricks
print(last_record.id)
print(repr(last_record.seq))
print(len(last_record))

print("The first record")
first_record = records[0] # remember, Python counts from zero
print(first_record.id)
print(repr(first_record.seq))
print(len(first_record))
```

```sh
Found 94 records
The last record
Z78439.1
Seq(CATTGTTGAGATCACATAATAATTGATCGAGTTAATCTGGAGGATCTGTTTACT...GCC)
592
The first record
Z78533.1
Seq(CGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTGATGAGACCGTGG...CGC)
740
```

### 提取数据

为了查看注释信息的保存方式，下面输出 `ls_orchid.gbk` 文件的第一条记录：

```py
from Bio import SeqIO

record_iterator = SeqIO.parse("ls_orchid.gbk", "genbank")
first_record = next(record_iterator)
print(first_record)
```

输出内容：

```sh
ID: Z78533.1
Name: Z78533
Description: C.irapeanum 5.8S rRNA gene and ITS1 and ITS2 DNA.
Number of features: 5
/sequence_version=1
/source=Cypripedium irapeanum
/taxonomy=['Eukaryota', 'Viridiplantae', 'Streptophyta', ..., 'Cypripedium']
/keywords=['5.8S ribosomal RNA', '5.8S rRNA gene', ..., 'ITS1', 'ITS2']
/references=[...]
/accessions=['Z78533']
/data_file_division=PLN
/date=30-NOV-2006
/organism=Cypripedium irapeanum
/gi=2765658
Seq('CGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTGATGAGACCGTGG...CGC')
```

上面给出了 `SeqRecord` 的大多数注释信息的摘要。`.annotations` 属性是一个 Python dict。在输出 record 时，该注释 dict 也随之输出。我们也可以直接输出：

```py
print(first_record.annotations)
```

也可以输出所有的 key:

```py
print(first_record.annotations.keys())
```

或者所有的值：

```py
print(first_record.annotations.values())
```

注释值通常为字符串或字符串列表。引用是特例，为保存为引用对象。

假设你想从 [ls_orchid.gbk](https://raw.githubusercontent.com/biopython/biopython/master/Doc/examples/ls_orchid.gbk) 文件中提取 species 信息。物种信息 `Cypripedium irapeanum` 保存在注释 dict 的 'source' 和 'organism' 中，可以按如下方式访问：

```py
>>> print(first_record.annotations["source"])
Cypripedium irapeanum
```

或者：

```py
>>> print(first_record.annotations["organism"])
Cypripedium irapeanum
```

`organism` 一般用来保存科学名称，如 *Arabidopsis thaliana*，而 `source` 用于保存通用名。在本例中，两个字段相同。

下面我们迭代所有记录，将物种信息保存到列表：

```py
from Bio import SeqIO

all_species = []
for seq_record in SeqIO.parse("ls_orchid.gbk", "genbank"):
    all_species.append(seq_record.annotations["organism"])
print(all_species)
```

也可以使用列表推导的方式来写：

```py
from Bio import SeqIO

all_species = [
    seq_record.annotations["organism"]
    for seq_record in SeqIO.parse("ls_orchid.gbk", "genbank")
]
print(all_species)
```

两种方式，输出结果相同：

```sh
['Cypripedium irapeanum', 'Cypripedium californicum', ..., 'Paphiopedilum barbatum']
```

如果想从 FASTA 文件中提取物种信息，由于 FASTA 没有专门的字段存储该信息，只能手动从第一行的描述信息中提取。[ls_orchid.fasta](https://raw.githubusercontent.com/biopython/biopython/master/Doc/examples/ls_orchid.fasta) 文件的第一条记录如下：

```fasta
>gi|2765658|emb|Z78533.1|CIZ78533 C.irapeanum 5.8S rRNA gene and ITS1 and ITS2 DNA
CGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTGATGAGACCGTGGAATAAACGATCGAGTG
AATCCGGAGGACCGGTGTACTCAGCTCACCGGGGGCATTGCTCCCGTGGTGACCCTGATTTGTTGTTGGG
...
```

物种名称为第二个单词。因此，从空格拆分记录的 `.description`，字段 0 是记录的识别符，字段 1 就是所需的物种信息：

```py
from Bio import SeqIO

all_species = []
for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    all_species.append(seq_record.description.split()[1])
print(all_species)
```

输出：

```sh
['C.irapeanum', 'C.californicum', 'C.fasciculatum', 'C.margaritaceum', ..., 'P.barbatum']
```

List 推导版本：

```py
from Bio import SeqIO

all_species == [
    seq_record.description.split()[1]
    for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta")
]
print(all_species)
```

总的来说，从 FASTA 描述行提取信息不是很好。如果能获得注释良好的文件格式，如 GenBank 或 EMBL，这种注释信息更好提取。

### 修改数据

`SeqRecord` 的属性可以直接修改，例如：

```py
>>> from Bio import SeqIO
>>> record_iterator = SeqIO.parse("ls_orchid.fasta", "fasta")
>>> first_record = next(record_iterator)
>>> first_record.id
'gi|2765658|emb|Z78533.1|CIZ78533'
>>> first_record.id = "new_id"
>>> first_record.id
'new_id'
```

注意，如果要更改 FASTA 的输出信息，则需要同时修改 `id` 和 `description` 属性。为了确保正确，可以在期望的 `description` 前面加上 `id`，中间以空格分开：

```py
>>> from Bio import SeqIO
>>> record_iterator = SeqIO.parse("ls_orchid.fasta", "fasta")
>>> first_record = next(record_iterator)
>>> first_record.id = "new_id"
>>> first_record.description = first_record.id + " " + "desired new description"
>>> print(first_record.format("fasta")[:200])
>new_id desired new description
CGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTGATGAGACCGTGGAATAAA
CGATCGAGTGAATCCGGAGGACCGGTGTACTCAGCTCACCGGGGGCATTGCTCCCGTGGT
GACCCTGATTTGTTGTTGGGCCGCCTCGGGAGCGTCCATGGCGGGT
```

## 2. 从压缩文件解析序列

用 Python 的 `gzip` 模块打开压缩文件进行处理：

```python
>>> import gzip
>>> from Bio import SeqIO
>>> with gzip.open("ls_orchid.gbk.gz", "rt") as handle:
...     print(sum(len(r) for r in SeqIO.parse(handle, "gb")))
...
67518
```

对 bzip2 格式可以用 `bz2` 模块：

```python
>>> import bz2
>>> from Bio import SeqIO
>>> with bz2.open("ls_orchid.gbk.bz2", "rt") as handle:
...     print(sum(len(r) for r in SeqIO.parse(handle, "gb")))
...
67518
```

gzip 格式的变体 BGZF（Blocked GNU Zip Format）可以像谱图 gzip 文件一样读取，但是具有随机访问的优势。

## 从网络解析序列

> [!NOTE]
> 虽然可以直接用 BioPython 解析网络数据，但还是建议下载保存为文件再处理。

### 解析网络 GenBank 序列

基本步骤：连接到 NCBI，使用 GI 编号从 GenBank 获取序列。

首先，尝试下载一条记录。如果不需要注释信息，下载 FASTA 更好。因为只有一条序列，使用 `SeqIO.read()` 函数：

```python
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "A.N.Other@example.com"
with Entrez.efetch(
    db="nucleotide", rettype="fasta", retmode="text", id="6273291"
) as handle:
    seq_record = SeqIO.read(handle, "fasta")
print("%s with %i features" % (seq_record.id, len(seq_record.features)))
```

```txt
gi|6273291|gb|AF191665.1|AF191665 with 0 features
```

在 NCBI 还可以选择其它格式：

```python
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "A.N.Other@example.com"
with Entrez.efetch(
    db="nucleotide", rettype="gb", retmode="text", id="6273291"
) as handle:
    seq_record = SeqIO.read(handle, "gb")  # using "gb" as an alias for "genbank"
print("%s with %i features" % (seq_record.id, len(seq_record.features)))
```

```txt
AF191665.1 with 3 features
```

一次下载多条序列。用 `SeqIO.parse()` 解析：

```python
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "A.N.Other@example.com"
with Entrez.efetch(
    db="nucleotide", rettype="gb", retmode="text", id="6273291,6273290,6273289"
) as handle:
    for seq_record in SeqIO.parse(handle, "gb"):
        print("%s %s..." % (seq_record.id, seq_record.description[:50]))
        print(
            "Sequence length %i, %i features, from: %s"
            % (
                len(seq_record),
                len(seq_record.features),
                seq_record.annotations["source"],
            )
        )
```

```txt
AF191665.1 Opuntia marenae rpl16 gene; chloroplast gene for c...
Sequence length 902, 3 features, from: chloroplast Opuntia marenae
AF191664.1 Opuntia clavata rpl16 gene; chloroplast gene for c...
Sequence length 899, 3 features, from: chloroplast Grusonia clavata
AF191663.1 Opuntia bradtiana rpl16 gene; chloroplast gene for...
Sequence length 899, 3 features, from: chloroplast Opuntia bradtianaa
```

### 解析网络 SwissPro 序列

从 ExPASy 解析单条序列：

```python
from Bio import ExPASy
from Bio import SeqIO

with ExPASy.get_sprot_raw("O23729") as handle:
    seq_record = SeqIO.read(handle, "swiss")
print(seq_record.id)
print(seq_record.name)
print(seq_record.description)
print(repr(seq_record.seq))
print("Length %i" % len(seq_record))
print(seq_record.annotations["keywords"])
```

```txt
O23729
CHS3_BROFI
RecName: Full=Chalcone synthase 3; EC=2.3.1.74; AltName: Full=Naringenin-chalcone synthase 3;
Seq('MAPAMEEIRQAQRAEGPAAVLAIGTSTPPNALYQADYPDYYFRITKSEHLTELK...GAE')
Length 394
['Acyltransferase', 'Flavonoid biosynthesis', 'Transferase']
```

## 序列字典

对自索引文件格式，如 twoBit，`SeqIO.parse` 返回值可以作为 dict 使用，即可以随机访问序列文件。例如：

```python
>>> from Bio import SeqIO
>>> handle = open("sequence.bigendian.2bit", "rb")
>>> records = SeqIO.parse(handle, "twobit")
>>> records.keys()
dict_keys(['seq11111', 'seq222', 'seq3333', 'seq4', 'seq555', 'seq6'])
>>> records['seq222']
SeqRecord(seq=Seq('TTGATCGGTGACAAATTTTTTACAAAGAACTGTAGGACTTGCTACTTCTCCCTC...ACA'), id='seq222', name='<unknown name>', description='<unknown description>', dbxrefs=[])
>>> records['seq222'].seq
Seq('TTGATCGGTGACAAATTTTTTACAAAGAACTGTAGGACTTGCTACTTCTCCCTC...ACA')
>>> handle.close() # 文件关闭后，无法继续访问
>>> records['seq222'].seq
Traceback (most recent call last):
...
ValueError: cannot retrieve sequence: file is closed
```

对其它文件格式，`Bio.SeqIO` 提供了三个相关函数，实现随机访问功能：

- `Bio.SeqIO.to_dict()` 最灵活，内存占用最高。将所有记录转换为 dict。
- `Bio.SeqIO.index()` 类似只读 dict，根据需要将序列解析为 `SeqRecord`。
- `Bio.SeqIO.index_db()` 类似只读 dict，但是将识别符和 file offsets 保存为 SQLite3 数据库文件，内存占用低，但要慢一点。



## 输出序列文件

2022-06-14, 15:19

前面已经讨论了使用 `SeqIO.parse()` 读取文件，下面介绍使用 `SeqIO.write()` 输出文件。该函数包含三个参数：

1. `SeqRecord` 对象
2. 写入文件的句柄或文件名
3. 输出格式

示例：首先创建 `SeqRecord` 对象列表：

```py
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

rec1 = SeqRecord(
    Seq(
        "MMYQQGCFAGGTVLRLAKDLAENNRGARVLVVCSEITAVTFRGPSETHLDSMVGQALFGD"
        "GAGAVIVGSDPDLSVERPLYELVWTGATLLPDSEGAIDGHLREVGLTFHLLKDVPGLISK"
        "NIEKSLKEAFTPLGISDWNSTFWIAHPGGPAILDQVEAKLGLKEEKMRATREVLSEYGNM"
        "SSAC",
    ),
    id="gi|14150838|gb|AAK54648.1|AF376133_1",
    description="chalcone synthase [Cucumis sativus]",
)

rec2 = SeqRecord(
    Seq(
        "YPDYYFRITNREHKAELKEKFQRMCDKSMIKKRYMYLTEEILKENPSMCEYMAPSLDARQ"
        "DMVVVEIPKLGKEAAVKAIKEWGQ",
    ),
    id="gi|13919613|gb|AAK33142.1|",
    description="chalcone synthase [Fragaria vesca subsp. bracteata]",
)

rec3 = SeqRecord(
    Seq(
        "MVTVEEFRRAQCAEGPATVMAIGTATPSNCVDQSTYPDYYFRITNSEHKVELKEKFKRMC"
        "EKSMIKKRYMHLTEEILKENPNICAYMAPSLDARQDIVVVEVPKLGKEAAQKAIKEWGQP"
        "KSKITHLVFCTTSGVDMPGCDYQLTKLLGLRPSVKRFMMYQQGCFAGGTVLRMAKDLAEN"
        "NKGARVLVVCSEITAVTFRGPNDTHLDSLVGQALFGDGAAAVIIGSDPIPEVERPLFELV"
        "SAAQTLLPDSEGAIDGHLREVGLTFHLLKDVPGLISKNIEKSLVEAFQPLGISDWNSLFW"
        "IAHPGGPAILDQVELKLGLKQEKLKATRKVLSNYGNMSSACVLFILDEMRKASAKEGLGT"
        "TGEGLEWGVLFGFGPGLTVETVVLHSVAT",
    ),
    id="gi|13925890|gb|AAK49457.1|",
    description="chalcone synthase [Nicotiana tabacum]",
)

my_records = [rec1, rec2, rec3]
```

然后，将 `SeqRecord` 列表写入 FASTA 文件：

```py
from Bio import SeqIO

SeqIO.write(my_records, "my_example.faa", "fasta")
```

生成的 fasta 文件如下：

```fasta
>gi|14150838|gb|AAK54648.1|AF376133_1 chalcone synthase [Cucumis sativus]
MMYQQGCFAGGTVLRLAKDLAENNRGARVLVVCSEITAVTFRGPSETHLDSMVGQALFGD
GAGAVIVGSDPDLSVERPLYELVWTGATLLPDSEGAIDGHLREVGLTFHLLKDVPGLISK
NIEKSLKEAFTPLGISDWNSTFWIAHPGGPAILDQVEAKLGLKEEKMRATREVLSEYGNM
SSAC
>gi|13919613|gb|AAK33142.1| chalcone synthase [Fragaria vesca subsp. bracteata]
YPDYYFRITNREHKAELKEKFQRMCDKSMIKKRYMYLTEEILKENPSMCEYMAPSLDARQ
DMVVVEIPKLGKEAAVKAIKEWGQ
>gi|13925890|gb|AAK49457.1| chalcone synthase [Nicotiana tabacum]
MVTVEEFRRAQCAEGPATVMAIGTATPSNCVDQSTYPDYYFRITNSEHKVELKEKFKRMC
EKSMIKKRYMHLTEEILKENPNICAYMAPSLDARQDIVVVEVPKLGKEAAQKAIKEWGQP
KSKITHLVFCTTSGVDMPGCDYQLTKLLGLRPSVKRFMMYQQGCFAGGTVLRMAKDLAEN
NKGARVLVVCSEITAVTFRGPNDTHLDSLVGQALFGDGAAAVIIGSDPIPEVERPLFELV
SAAQTLLPDSEGAIDGHLREVGLTFHLLKDVPGLISKNIEKSLVEAFQPLGISDWNSLFW
IAHPGGPAILDQVELKLGLKQEKLKATRKVLSNYGNMSSACVLFILDEMRKASAKEGLGT
TGEGLEWGVLFGFGPGLTVETVVLHSVAT
```

`SeqIO.write()` 返回写入的 `SeqRecord` 数目。

### Round trips

读取文件后，再将解析的信息写入文件，如果生成的文件与源文件一样，称为 round trip。要实现该功能，需要从原始文件提取完整的信息，`Bio.SeqIO` 并不支持。

例如，FASTA 文件对序列数据支持任意换行，下面两个示例文件的内容除了换行，其它内容完全一样，使用 `SeqIO` 解析会生成完全一样的 `SeqRecord`：

```fasta
>YAL068C-7235.2170 Putative promoter sequence
TACGAGAATAATTTCTCATCATCCAGCTTTAACACAAAATTCGCACAGTTTTCGTTAAGA
GAACTTAACATTTTCTTATGACGTAAATGAAGTTTATATATAAATTTCCTTTTTATTGGA

>YAL068C-7235.2170 Putative promoter sequence
TACGAGAATAATTTCTCATCATCCAGCTTTAACACAAAATTCGCA
CAGTTTTCGTTAAGAGAACTTAACATTTTCTTATGACGTAAATGA
AGTTTATATATAAATTTCCTTTTTATTGGA
```

要实现 round-tripable FASTA 解析器，就需要记录换行位置，而这些额外信息通常没有意义。Biopython 在输出时单行默认使用 60 个字符。在其它文件格式中，对空白间隔也有相同文件。另外，Biopython 目前还无法还无法保存所有的注释信息，如 GenBank 和 EMBL。

### 序列格式转换

结合 `SeqIO.parse()` 和 `SeqIO.write()` 函数，可以实现文件格式转换。

例如，读取 GenBank 格式的 ls_orchid.gbk 文件，输出 FASTA 格式：

```py
from Bio import SeqIO

records = SeqIO.parse("ls_orchid.gbk", "genbank")
count = SeqIO.write(records, "my_example.fasta", "fasta")
print("Converted %i records" % count)
```

由于文件转换是非常常见的操作，因为有辅助函数实现该功能：

```py
from Bio import SeqIO

count = SeqIO.convert("ls_orchid.gbk", "genbank", "my_example.fasta", "fasta")
print("Converted %i records" % count)
```

原则上，只需要更改文件名和格式名，上面的代码就可以用来转换 Biopython 支持的所有文件格式。但是，有些格式需要其它格式所没有的信息，因此，虽然可以将 FASTQ 文件转换为 FASTA 文件，但反之不行。

使用 `SeqIO.convert()` 函数不仅代码更短，而且可能更快。因为 `convert()` 可以利用几个特定文件格式的优化功能。

### 生成反向互补序列文件

假设你有一个核苷酸序列文件，希望将其转换为包含反向互补序列的文件。

首先，使用 `SeqIO.parse()` 载入核苷酸序列文件，可以用 `Seq` 对象的 `.reverse_complement()` 方法输出反向互补序列：

```py
>>> from Bio import SeqIO
>>> for record in SeqIO.parse("ls_orchid.gbk", "genbank"):
...     print(record.id)
...     print(record.seq.reverse_complement())
```

如果我们向将这条反向互补序列保存到文件，首先需要创建 `SeqRecord` 对象。我们可以使用 `SeqRecord` 自带的 `.reverse_complement()` 方法，但是需要对新的 record 重命名。

这里用 list 推导很方便：

```py
>>> from Bio import SeqIO
>>> records = [rec.reverse_complement(id="rc_"+rec.id, description = "reverse complement") \
...            for rec in SeqIO.parse("ls_orchid.fasta", "fasta")]
>>> len(records)
94
```

还可以在 List 推导中添加条件语句：

```py
>>> records = [rec.reverse_complement(id="rc_"+rec.id, description = "reverse complement") \
...            for rec in SeqIO.parse("ls_orchid.fasta", "fasta") if len(rec)<700]
>>> len(records)
18
```

也可以使用生成器表示式，其优点是不会一次在内存中生成所有序列：

```py
>>> records = (rec.reverse_complement(id="rc_"+rec.id, description = "reverse complement") \
...           for rec in SeqIO.parse("ls_orchid.fasta", "fasta") if len(rec)<700)
```

完整示例：

```py
>>> from Bio import SeqIO
>>> records = (rec.reverse_complement(id="rc_"+rec.id, description = "reverse complement") \
...            for rec in SeqIO.parse("ls_orchid.fasta", "fasta") if len(rec)<700)
>>> SeqIO.write(records, "rev_comp.fasta", "fasta")
18
```

### 格式化字符串

例如，读取 GenBank 文件，创建 FASTA 格式的字符串：

```py
from Bio import SeqIO
from io import StringIO

records = SeqIO.parse("ls_orchid.gbk", "genbank")
out_handle = StringIO()
SeqIO.write(records, out_handle, "fasta")
fasta_data = out_handle.getvalue()
print(fasta_data)
```

对单条记录的格式化字符串，可以使用 `SeqRecord` 的 `format()` 方法。

尽管不推荐，但是我们可以用 `format()` 方法辅助写入文件：

```py
from Bio import SeqIO

with open("ls_orchid_long.tab", "w") as out_handle:
    for record in SeqIO.parse("ls_orchid.gbk", "genbank"):
        if len(record) > 100:
            out_handle.write(record.format("tab"))
```

这种风格的代码适合简单的顺序文件格式，如 FASTA，但是不适合更复杂的文件格式。所以我们推荐使用 `SeqIO.write()` 函数：

```py
from Bio import SeqIO

records = (rec for rec in SeqIO.parse("ls_orchid.gbk", "genbank") if len(rec) > 100)
SeqIO.write(records, "ls_orchid.tab", "tab")
```

另外，使用 `SeqIO.write()` 也比 `SeqRecord.format()` 更快。

## 支持的文件格式

|格式|Read|Write|Index|说明|
|---|---|---|---|---|
|abi|1.58|No|N/A|Reads the ABI “Sanger” capillary sequence traces files, including the PHRED quality scores for the base calls. This allows ABI to FASTQ conversion. Note each ABI file contains one and only one sequence (so there is no point in indexing the file)|
|abi-trim|1.71|No|N/A|Same as “abi” but with quality trimming with Mott’s algorithm|
|ace|1.47|No|1.52|Reads the contig sequences from an ACE assembly file. Uses Bio.Sequencing.Ace internally|
|cif-atom|1.73|No|No|Uses Bio.PDB.MMCIFParser to determine the (partial) protein sequence as it appears in the structure based on the atomic coordinates.|
|cif-seqres|1.73|No|No|Reads a macromolecular Crystallographic Information File (mmCIF) file to determine the complete protein sequence as defined by the _pdbx_poly_seq_scheme records.|
|clustal|1.43|1.43|No|The alignment format of Clustal X and Clustal W.|
|embl|1.43|1.54|1.52|The EMBL flat file format. Uses Bio.GenBank internally.|
|fasta|1.43|1.43|1.52|This refers to the input FASTA file format introduced for Bill Pearson’s FASTA tool, where each record starts with a “>” line.|
|fasta-2line|1.71|1.71|No|FASTA format variant with no line wrapping and exactly two lines per record.|
|fastq-sanger or fastq|1.50|1.50|1.52|FASTQ files are a bit like FASTA files but also include sequencing qualities. In Biopython, “fastq” (or the alias “fastq-sanger”) refers to Sanger style FASTQ files which encode PHRED qualities using an ASCII offset of 33. See also the incompatible “fastq-solexa” and “fastq-illumina” variants used in early Solexa/Illumina pipelines, Illumina pipeline 1.8 produces Sanger FASTQ.|
|fastq-solexa|1.50|1.50|1.52|In Biopython, “fastq-solexa” refers to the original Solexa/Illumina style FASTQ files which encode Solexa qualities using an ASCII offset of 64. See also what we call the “fastq-illumina” format.
|fastq-illumina|1.51|1.51|1.52|In Biopython, “fastq-illumina” refers to early Solexa/Illumina style FASTQ files (from pipeline version 1.3 to 1.7) which encode PHRED qualities using an ASCII offset of 64. For good quality reads, PHRED and Solexa scores are approximately equal, so the “fastq-solexa” and “fastq-illumina” variants are almost equivalent.|
|gck|1.75|No|No|The native format used by Gene Construction Kit.|
|genbank or gb|1.43|1.48 / 1.51|1.52|[GenBank 序列格式](https://bioperl.org/formats/sequence_formats/GenBank_sequence_format) 内部使用 `Bio.GenBank` 解析。Biopython 1.48-1.51 输出的 GenBank 文件只有少量注释，而 1.51 后也输出 features table|
|ig|1.47|No|1.52|This refers to the IntelliGenetics file format, apparently the same as the MASE alignment format.
|imgt|1.56|1.56|1.56|This refers to the IMGT variant of the EMBL plain text file format.
|nexus|1.43|1.48|No|The NEXUS multiple alignment format, also known as PAUP format. Uses Bio.Nexus internally.
|pdb-seqres|1.61|No|No|Reads a Protein Data Bank (PDB) file to determine the complete protein sequence as it appears in the header (no dependency on Bio.PDB and NumPy).
|pdb-atom|1.61|No|No|Uses Bio.PDB to determine the (partial) protein sequence as it appears in the structure based on the atom coordinate section of the file (requires NumPy).
|phd|1.46|1.52|1.52|PHD files are output from PHRED, used by PHRAP and CONSED for input. Uses Bio.Sequencing.Phd internally.
|phylip|1.43|1.43|No|PHYLIP files. Truncates names at 10 characters.
|pir|1.48|1.71|1.52|A “FASTA like” format introduced by the National Biomedical Research Foundation (NBRF) for the Protein Information Resource (PIR) database, now part of UniProt.
|seqxml|1.58|1.58|No|Simple sequence XML file format.|
|sff|1.54|1.54|1.54|Standard Flowgram Format (SFF) binary files produced by Roche 454 and IonTorrent/IonProton sequencing machines.|
|sff-trim|1.54|No|1.54|Standard Flowgram Format applying the trimming listed in the file.|
|snapgene|1.75|No|No|The native format used by SnapGene.|
|stockholm|1.43|1.43|No|The Stockholm alignment format is also known as PFAM format.|
|swiss|1.43|No|1.52|Swiss-Prot aka UniProt format. Uses Bio.SwissProt internally. See also the UniProt XML format.|
|tab|1.48|1.48|1.52|Simple two column tab separated sequence files, where each line holds a record’s identifier and sequence. For example, this is used by Aligent’s eArray software when saving microarray probes in a minimal tab delimited text file.|
|qual|1.50|1.50|1.52|Qual files are a bit like FASTA files but instead of the sequence, record space separated integer sequencing values as PHRED quality scores. A matched pair of FASTA and QUAL files are often used as an alternative to a single FASTQ file.
|uniprot-xml|1.56|No|1.56|UniProt XML format, successor to the plain text Swiss-Prot format.|
|xdna|1.75|1.75|No|The native format used by Christian Marck’s DNA Strider and Serial Cloner.|
