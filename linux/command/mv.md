# mv

- [mv](#mv)
  - [简介](#简介)
  - [选项](#选项)
  - [示例](#示例)
  - [参考](#参考)

Last updated: 2023-04-07, 17:20
*****

## 简介

`mv` (move) 用于文件的剪切或重命名。语法：

```sh
mv [option]… [-T] source dest
mv [option]… source… directory
mv [option]… -t directory source…
```

- 如果提供两个文件名，`mv` 将第一个文件移到第二个位置
- 如果指定 `--target-directory` (-t) 选项，或最后一个文件是目录且没有指定 `--no-target-directory` (-T) 选项，`mv` 将每个 `source` 文件移动到指定目录。

`mv` 移动文档通常只需要重命名。但是，如果目标的文档系统不同，此时重命名不起作用，`mv` 会像 `cp -a` 一样复制文件，然后（假设复制成功）删除原始文件。如果复制失败，`mv` 会删除目标位置已创建的部分副本。如果要将三个目录从一个文件系统复制到另一个文件系统，第一个目录副本创建成功，第二个目录失败，则第一个目录保留在目标文件系统，第二个和第三个目录保留在原始文件系统。

## 选项

`mv` 与 `cp` 许多参数相同。

- `-i`, `--interactive`

存在同名文件时，是否向用户询问，默认覆盖。

- `-u`, `--update`

当源文件比目标文件新，或目标文件不存在时，才执行移动操作。

- `-v`, `--verbose`

显示详细的操作信息。

|参数|长选项|说明|
|---|---|---|
|`-f`||覆盖已有文件时，不提示|
|`-b`||文件存在时，覆盖前为其创建备份|

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

- 一个或多个条目从一个目录移动到另一个目录

```bash
mv item... directory
```

- 移动 file1 到 file2

```bash
mv file1 file2
```

如果 file2 存在，其内容被 file1 的内容覆盖。如果 file2 不存在，则创建 file2。这两种情况下，file1 都不再存在。

- 覆盖前提示

```sh
mv -i file1 file2
```

除了如果 file2 存在，在覆盖 file2 前提示用户，和上面的示例一样。

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

## 参考

- https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html