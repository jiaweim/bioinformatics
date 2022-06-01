# 用户目录

- [用户目录](#用户目录)
  - [pwd](#pwd)
  - [ls](#ls)
  - [cd](#cd)
  - [system](#system)
  - [参考](#参考)

2022-06-01, 09:09
@author Jiawei Mao
***

## pwd

2022-06-01, 09:16

```sh
pwd
```

打印当前工作目录。

## ls

2022-06-01, 09:15

```sh
ls [pattern]
dir [pattern]
```

`ls` 列出当前工作目录的内容。

- **例1**，列出当前目录文件

```sh
ls
```

- 例2，列出当前目录以 `pml` 结尾的文件

```sh
ls *.pml
```

## cd

2022-06-01, 09:10

```sh
cd DIR_NAME
```

更改 PyMOL 的当前工作目录。`DIR_NAME` 为目录。

- 例1，转到主目录

```sh
cd ~
```

- 例2，转到 `/tmp` 目录

```sh
cd /tmp
```

- 例 3，Windows 在带空格路径

```sh
cd \"program files"

cd "\program files"

cd \program?files
```

## system

2022-06-01, 09:21

```sh
system command
```

在 Unix 或 Windows 的子 Shell 中执行命令。

API：

```py
cmd.system(string command,int async=0)
```

async 只能在 Python 中指定：

- 如果 async 为 0（默认），则在 r 中返回 "system" 的结果代码
- 如果 async 为 1，则该命令在单独的线程运行

## 参考

- https://pymolwiki.org/index.php/Cd
- https://pymolwiki.org/index.php/Ls
