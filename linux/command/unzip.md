# unzip

- [unzip](#unzip)
  - [简介](#简介)
  - [安装](#安装)
  - [使用](#使用)
  - [示例](#示例)
  - [参考](#参考)

Last updated: 2023-03-27, 19:04
****

## 简介

`unzip` 命令用于解压缩 zip 格式文件，虽然 Linux 系统中更多的使用 tar 命令进行对压缩包的管理工作，但有时也会收到 Windows 系统常用的.zip和 .rar 格式的压缩包文件，`unzip` 格式便派上了用场。直接使用 `unzip` 命令解压缩文件后，压缩包内原有的文件会被提取并输出保存到当前工作目录下。

## 安装

大部分 Linux 默认没有安装 `unzip`，需要手动安装。

- Ubuntu 和 Debian 安装

```bash
$ sudo apt install unzip
```

- CentOS 和 Fedora

```bash
$ sudo yum install unzip
```

## 使用

```bash
unzip [选项] 压缩包
```

|选项|说明|
|---|---|
|-l|显示压缩文件内所包含的文件|
|-v|执行时显示详细的信息|
|-c|将解压缩的结果显示到屏幕上，并对字符做适当的转换|
|-n|解压缩时不要覆盖原有的文件|
|-j|不处理压缩文件中原有的目录路径|

## 示例

- 解压到当前目录

```bash
unzip latest.zip
```

- 解压到指定目录

```bash
unzip latest.zip -d /home
```

- 查看压缩包是否完整，文件有无损坏

```bash
unzip -t latest.zip
```

- `unzip` 默认输出正在提取的所有文件名称，使用 `-q` 禁止打印这些信息

```bash
$ unzip -q filename.zip
```

- `-P` 指定密码解压加密压缩文件

```bash
$ unzip -P password filename.zip
```

不过应该避免在命令行上明文输入密码，应该不输入密码直接解压：

```bash
$ unzip filename.zip
```

然后 `unzip` 会弹出提示输入密码。

- `-x` 选项排除指定的文件或目录，多个文件以空格分隔

```bash
$ unzip filename.zip -x file1-to-exclude file2-to-exclude
```

例如，排除 `.git` 目录：

```bash
$ unzip filename.zip -x "*.git/"
```



## 参考

- https://www.linuxcool.com/unzip
- https://linuxize.com/post/how-to-unzip-files-in-linux/