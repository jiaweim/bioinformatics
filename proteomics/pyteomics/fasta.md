# FASTA

- [FASTA](#fasta)
  - [简介](#简介)
  - [读](#读)
    - [描述信息解析](#描述信息解析)
  - [写](#写)
  - [参考](#参考)

***

## 简介

FASTA 是蛋白质序列数据库的常用格式。

## 读

使用 `pyteomics.fasta.read()` 函数从 FASTA 数据库提取数据：

```python
>>> from pyteomics import fasta
>>> with fasta.read('/path/to/file/my.fasta') as db:
>>>     for entry in db:
>>>         ...
```

`pyteomics.fasta.read()` 返回 generator 而不是 list，避免占用过多内存。generator 生成 (description, sequence) tuple，所以可以按如下方式使用：

```python
>>> with fasta.read('/path/to/file/my.fasta') as db:
>>>     for descr, seq in db:
>>>         ...
```

也可以使用属性来访问描述信息和序列：

```python
>>> with fasta.read('my.fasta') as reader:
>>>     descriptions = [item.description for item in reader]
```

### 描述信息解析



## 写

使用 `(description, sequence)` tuple 序列创建 FASTA 文件：

```python
>>> entries = [('Protein 1', 'PEPTIDE'*1000), ('Protein 2', 'PEPTIDE'*2000)]
>>> fasta.write(entries, 'target-file.fasta')
```


## 参考

- https://pyteomics.readthedocs.io/en/latest/
