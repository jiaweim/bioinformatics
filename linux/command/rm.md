# rm

- [rm](#rm)
  - [简介](#简介)
  - [选项](#选项)
  - [示例](#示例)

Last updated: 2023-04-12, 14:30
****

## 简介

`rm`（remove）用来删除文件或目录。

```sh
rm [参数] 文件
```

`item` 代表一个或多个文件或目录。

> **WARNING**
> Unix 操作系统没有复原命令，用 `rm` 删除后就找不回了。
> 特别是使用通配符时，除仔细检查输入内容外，先用 `ls` 测试一下通配符。然后按上方向键调出先前命令，将 ls 替换为 rm 命令。


## 选项

- `-i`, `--interactive`

删除前提示用户确认删除，默认提示。

- `-r`, `--recursive`

递归删除文件。这意味着，如果要删除一个目录，而此目录又包含子目录，那么子目录也会被删除。要删除一个目录，必须指定该选项。

- `-f`, `--force`

不提示直接删除。该选项覆盖`--interactive` 选项。

- `-v`, `--verbose`

在执行 rm 命令时，显示翔实的操作信息。

## 示例

- 删除文件，默认提示，输出 y 确认

```sh
$ rm a.fasta 
rm: remove regular file ‘a.fasta’? y
```

- 直接删除，不需要二次确认

```sh
$ rm -f a.fasta
```

- 强制删除目录及其内的所有文件

```sh
$ rm -rf Documents
```

- 除了在删除文件之前，提示用户确认删除

```sh
$ rm -i file1
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
$ rm -rf /*
```

```bash
$ rmdir /home/joe/nothing/ # 只能删空目录
$ rm -r /home/joe/bigdir/  # 删除目录
$ rm -rf /home/joe/hugedir/
```