# mv

2022-05-25, 14:12
*****

## 简介

`mv` (move) 用于文件的剪切和重命名。

在同一个目录内对文件进行剪切，其实就是重命名。

语法：

```sh
mv [参数] 源文件 目标文件
```

`mv` 与 `cp` 许多参数相同。

|参数|长选项|说明|
|---|---|---|
|`-i`|`--interactive`|存在同名文件时，是否向用户询问，默认覆盖|
|`-f`||覆盖已有文件时，不提示|
|`-b`||文件存在时，覆盖前为其创建备份|
|`-u`|`--update`|当源文件比目标文件新，或目标文件不存在时，才执行移动操作|
|`-v`|`--verbose`|显示详细的操作信息|

## 示例

- 将文件 `a.txt` 重命名为 `b.txt`

```sh
$ mv a.txt b.txt
```

- 将文件 `a.txt` 移动到 `/etc` 目录，文件名称不变

```sh
$ mv a.txt /etc
```

- 将目录 `Documents` 移动到 `/etc`，并重命名为 `docs`

```sh
mv Documents /etc/docs
```

- 将 `/home` 目录中所有文件都移到当前目录，遇到已有文件直接覆盖

```sh
mv -f /home/* .
```

- 把 `item1` 移动或重命名为 `item2`

```bash
mv item1 item2
```

- 一个或多个条目从一个目录移动到另一个目录

```bash
mv item... directory
```

- 移动 file1 到 file2

```bash
mv file1 file2
```

如果 file2 存在，其内容被 file1 的内容重写。如果 file2 不存在，则创建 file2。这两种情况下，file1 都不再存在。

- 覆盖前提示

```sh
mv -i file1 file2
```

除了如果 file2 存在的话，在 file2 被重写之前，用户会得到提示信息外，这个和上面的选项一样。

- 移动多个文件

```bash
mv file1 file2 dir1
```

移动 file1 和 file2 到目录 dir1 中。dir1 必须已经存在。

- 移动目录

```bash
mv dir1 dir2
```

- 如果目录 dir2 不存在，创建目录 dir2，并且移动目录 dir1的内容到目录 dir2 中，同时删除目录 dir1。
- 如果目录 dir2存在，移动目录 dir1（及它的内容）到目录 dir2。
