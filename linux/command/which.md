# which

## 简介

有时候，系统中安装的程序不止一个版本。这种情况在大型服务器上很常见。使用 `which` 确定程序位置：

```bash
mjw@happy:~$ which ls
/usr/bin/ls
```

`which` 只适用于可执行文件，不适用于内建命令或代替实际可执行文件的别名。

对 shell 内建命令使用 `which`，要么没结果，要么报错：

```bash
mjw@happy:~$ which cd # Ubuntu 没有结果
mjw@happy:~$
```

