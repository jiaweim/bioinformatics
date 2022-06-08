# rm

2022-06-02, 09:34
@author Jiawei Mao
*****

## 简介

`rm`（remove）用来删除文件或目录。

> **WARNING**: Unix 操作系统没有复原命令，用 `rm` 删除后就找不回了。

```sh
rm [参数] 文件
```

`item` 代表一个或多个文件或目录。

|选项|长选项|意义|
|---|---|---|
|`-i`|`--interactive`|删除前提示用户确认删除，默认提示|
|`-r`|`--recursive`|递归删除文件。这意味着，如果要删除一个目录，而此目录又包含子目录，那么子目录也会被删除。要删除一个目录，必须指定该选项|
|`-f`|`--force`|不提示直接删除。该选项覆盖`--interactive` 选项|
|`-v`|`--verbose`|在执行 rm 命令时，显示翔实的操作信息|

## 示例

- 删除文件，默认提示，输出 y 确认

```sh
[root@localhost home]# rm a.fasta 
rm: remove regular file ‘a.fasta’? y
```

- 直接删除，不需要二次确认

```sh
[root@localhost home]# rm -f a.fasta
```

- 强制删除目录及其内的所有文件

```sh
[root@localhost home]# rm -rf Documents
```

- 除了在删除文件之前，提示用户确认删除

```sh
rm -i file1
```

- 删除文件 file1, 目录 dir1，及 dir1 中的内容

```sh
rm -r file1 dir1
```

- 同上，除了如果文件 file1，或目录 dir1 不存在的话，rm 仍会继续执行

```bash
rm -rf file1 dir1
```

- 强制删除当前工作目录内所有以 .txt 结尾的文件

```sh
rm -f *.txt
```

- 强制清空服务器系统内的所有文件（千万不要用）

```sh
rm -rf /*
```
