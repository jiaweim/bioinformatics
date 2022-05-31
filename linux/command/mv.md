# mv

2022-05-25, 14:12
***

## 简介

`mv` 表示 move，用于文件和文件件的剪切和重命名。

在同一个目录内对文件进行剪切，其实就是重命名。

语法：

```sh
mv [参数] 源文件 目标文件
```

|参数|说明|
|---|---|
|`-i`|存在同名文件时，是否向用户询问|
|`-f`|覆盖已有文件时，不提示|
|`-b`|文件存在时，覆盖前为其创建备份|
|`-u`|当源文件比目标文件新，或目标文件不存在时，才执行移动操作|

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