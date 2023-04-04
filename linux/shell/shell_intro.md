# Shell 概述

- [Shell 概述](#shell-概述)
  - [简介](#简介)
  - [Shell 和终端窗口](#shell-和终端窗口)
    - [Shell prompt](#shell-prompt)
  - [运行命令](#运行命令)

***

## 简介

在 Unix 系统，用来解释和管理命令的程序称为 `shell`。

Ubuntu 中使用的为 Bash shell，是 Bourne Again Shell 的缩写。其它类型的 shell 还有：

- C shell (csh)，BSD UNIX
- Korn shell (ksh)，UNIX System V

## Shell 和终端窗口

在 linux 中访问 shell 接口有三种常见方式：

- shell 提示符
- 终端窗口（Terminal window）
- 虚拟控制台

### Shell prompt

对没有 GUI 的 linux 系统，登录后可以看到 shell 提示符（prompt）。

普通用户的默认提示符为美元符号：

```bash
$
```

根（root）用户的默认提示符为井号：

```bash
#
```

在大多数 linux 系统中，shell 提示符前面有用户名、系统名和当前目录名称。例如，假设计算机名为 `pine`，用户名为 `jake`，当前目录为 `/usr/share/`，此时提示样式：

```bash
jake@pine:share$
```

## 运行命令

