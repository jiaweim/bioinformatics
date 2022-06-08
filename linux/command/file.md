# file

- [file](#file)
  - [简介](#简介)
  - [实例](#实例)

2022-06-07, 12:48
****

## 简介

`file` 命令用于识别文件类型，也可以辨别一些内容的编码格式。由于Linux系统并不是像Windows 系统那样通过扩展名来定义文件类型，因此用户无法直接通过文件名来进行分辨。`file` 命令通过分析文件头部信息中的标识来显示文件类型，使用很方便。

```sh
file [选项] 文件
```

|选项|说明|
|---|---|
|`-b`|列出识别结果，不显示文件名称 (简要模式)|
|-c|详细显示指令执行过程|
|-f|指定名称文件，显示多个文件类型信息|
|-L|直接显示符号连接所指向的文件类别|
|-m|指定魔法数字文件|
|-v|显示版本信息|
|-z|尝试去解读压缩文件的内容|
|`-i`|显示MIME类别|

## 实例

- 查看文件类型

```sh
[root@localhost data]# file README 
README: ASCII text
```

- 查看目录

```sh
[root@localhost data]# file threshold/
threshold/: directory
```

- 查看命令

```sh
[root@localhost data]# file /bin/ls
/bin/ls: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.32, BuildID[sha1]=c8ada1f7095f6b2bb7ddc848e088c2d615c3743e, stripped
```

- 查看类型，但不显示文件名

```sh
[root@localhost data]# file -b README 
ASCII text
```

- 以 MIME 类别显示文件类型

```sh
[root@localhost data]# file -i README 
README: text/plain; charset=us-ascii
```

- 查看符号连接文件的类型，会提示目标文件名称

```sh

```
