# help

- [help](#help)
  - [简介](#简介)
  - [`--help`](#--help)
  - [man](#man)
  - [apropos](#apropos)
  - [whatis](#whatis)
  - [info](#info)

Last updated: 2023-04-12, 19:20
****

## 简介

Bash 自带的帮助功能可用于所有 Shell 内置命令。

```bash
$ help command
```

例如：

```bash
$ help cd
cd: cd [-L|[-P [-e]] [-@]] [dir]
    Change the shell working directory.

    Change the current directory to DIR.  The default DIR is the value of the
    HOME shell variable.

    The variable CDPATH defines the search path for the directory containing
    DIR.  Alternative directory names in CDPATH are separated by a colon (:).
    A null directory name is the same as the current directory.  If DIR begins
    with a slash (/), then CDPATH is not used.

    If the directory is not found, and the shell option `cdable_vars' is set,
    the word is assumed to be  a variable name.  If that variable has a value,
    its value is used for DIR.

    Options:
      -L        force symbolic links to be followed: resolve symbolic
                links in DIR after processing instances of `..'
      -P        use the physical directory structure without following
                symbolic links: resolve symbolic links in DIR before
                processing instances of `..'
      -e        if the -P option is supplied, and the current working
                directory cannot be determined successfully, exit with
                a non-zero status
      -@        on systems that support it, present a file with extended
                attributes as a directory containing the file attributes

    The default is to follow symbolic links, as if `-L' were specified.
    `..' is processed by removing the immediately previous pathname component
    back to a slash or the beginning of DIR.

    Exit Status:
    Returns 0 if the directory is changed, and if $PWD is set successfully when
    -P is used; non-zero otherwise.
```

> **NOTE**
> `[]` 内的参数为可选参数。


## `--help`

尽管 `help` 文档信息简洁明了，但算不上教程。很多程序都支持 `--help` 选项，可以显示命令所支持的语法和选项相关描述。例如：

```bash
mjw@happy:~$ mkdir --help
Usage: mkdir [OPTION]... DIRECTORY...
Create the DIRECTORY(ies), if they do not already exist.

Mandatory arguments to long options are mandatory for short options too.
  -m, --mode=MODE   set file mode (as in chmod), not a=rwx - umask
  -p, --parents     no error if existing, make parent directories as needed
  -v, --verbose     print a message for each created directory
  -Z                   set SELinux security context of each created directory
                         to the default type
      --context[=CTX]  like -Z, or if CTX is specified then set the SELinux
                         or SMACK security context to CTX
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/mkdir>
or available locally via: info '(coreutils) mkdir invocation'
```

部分程序可能不支持 `--help` 选项，不过可以试试。

## man

大多数命令行程序会提供一份手册（manual）。`man` 可以浏览这种文档。

```bash
$ man program
```

手册的格式各不相同。不过一般都会包含下列部分：

- 标题
- 命令语法提要
- 命令作用描述
- 命令选项清单及其描述

不过，手册页通常不包含示例，其目的是作为参考，而非教程。

查看 `ls` 的手册：

```bash
$ man ls
```

在大多数 Linux 系统，`man` 使用 `less` 命令显示手册页。

`man` 显示的手册被分为若干部分（section）：

| section | 内容 |
|--|--|
| 1 | 用户命令 |
| 2 | 系统调用的编程接口 |
| 3 | C 库函数的编程接口 |
| 4 | 特殊文件，例如设备节点和驱动程序 |
| 5 | 文件格式 |
| 6 | 游戏和娱乐，例如屏保程序 |
| 7 | 杂项 |
| 8 | 系统管理命令 |

有时需要手册的某一节，从中查找所需内容：

```bash
$ man section search_term
```

例如：

```bash
$ man 5 passwd
```

显示描述 `/etc/passwd` 文件格式的手册页面。

## apropos

`apropos` 可以根据关键字在手册页中搜索可能的匹配项。这种方法比较粗糙，但有时也管用。

例如，用 partition 关键字搜索手册页：

```bash
mjw@happy:~$ apropos partition
addpart (8)          - tell the kernel about the existence of a partition
delpart (8)          - tell the kernel to forget about a partition
parted (8)           - a partition manipulation program
partprobe (8)        - inform the OS of partition table changes
partx (8)            - tell the kernel about the presence and numbering of on-disk partitions
resizepart (8)       - tell the kernel about the new size of a partition
systemd-gpt-auto-generator (8) - Generator for automatically discovering and mounting root, /home/, /srv/, /var/ and ...
```

输出结果每行的第一个字段是手册名称，第二个字段是相应的 section。

man 命令的 `-k` 选项与 `apropos` 的功能相同。

## whatis

`whatis` 显示匹配指定关键字的手册页名称和单行描述。

```bash
mjw@happy:~$ whatis ls
ls (1)               - list directory contents
```

## info

GNU 为自家的程序提供了手册页的替代品 `info`。`Info` 信息使用 `info` 阅读器查看。

`info` 页中包含超链接，与网页很像。

info 程序读取 info 文件，该文件按照树形结构组织各个节点，每个节点包含一个主题。info 文件包含的超链接允许在节点之间跳转。超链接可以通过前置的星号来识别，将光标放在超链接上并按 Enter 键激活。

输入 info 和程序名称启动 info 程序。info 常用控制命令：

| 命令 | 操作 |
|--|--|
| ? | 显示命令帮助 |
| Page Up 或 BackSpace | 显示上一页 |
| Page Down 或空格 | 显示下一页 |
| n | 显示下一个节点 |
| p | 显示上一个节点 |
| u | 显示当前节点的父节点（up），通常是一个菜单 |
| Enter | 进入光标所在超链接 |
| q | 退出（quit） |

平常使用的很多命令都属于 GNU 项目的 Coreutils 软件，查看其 info:

```bash
$ info coreutils
```

会显示一个菜单页面，其中包含指向 Coreutils 软件包内各个程序的超链接。

