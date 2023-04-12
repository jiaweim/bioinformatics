# type

- [type](#type)
  - [简介](#简介)
  - [示例](#示例)

Last updated: 2023-04-12, 16:53
****

## 简介

type 属于 Shell 内置命令，显示指定命令属于哪种类型。用法：

```bash
$ type command
```

其中，`command` 是要检查的文件名。

## 示例

```bash
$ type type # shell 内置命令
type is a shell builtin
$ type ls # ls 是 'ls --color=auto' 的别名
ls is aliased to 'ls --color=auto'
$ type cp # cp 是可执行程序
cp is hashed (/usr/bin/cp)
```
