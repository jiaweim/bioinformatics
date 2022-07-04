# unzip

- [unzip](#unzip)
  - [简介](#简介)
  - [示例](#示例)
  - [参考](#参考)

## 简介

`unzip` 命令用于解压缩 zip 格式文件，虽然 Linux 系统中更多的使用 tar 命令进行对压缩包的管理工作，但有时也会收到 Windows 系统常用的.zip和 .rar 格式的压缩包文件，`unzip` 格式便派上了用场。直接使用unzip命令解压缩文件后，压缩包内原有的文件会被提取并输出保存到当前工作目录下。

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

## 参考

- https://www.linuxcool.com/unzip
