# ls

- [ls](#ls)
  - [简介](#简介)
  - [颜色](#颜色)
  - [选项](#选项)
    - [文件筛选选项](#文件筛选选项)
    - [输出信息选项](#输出信息选项)
    - [格式化选项](#格式化选项)
    - [输出排序](#输出排序)
  - [信息说明](#信息说明)
  - [实例](#实例)
  - [参考](#参考)

2022-06-06, 12:31
*****

## 简介

`ls` (list) 列举指定目录下的文件名称及属性。

`ls` 默认列出当前工作目录中非隐藏文件的信息，经常与 `cd` 和 `pwd` 搭配使用。而带上参数后，则可以做更多的事情。

```sh
ls [选项] [文件]
```

## 颜色

```bash
$ alias ls
alias ls='ls --color=auto'
```

`--color=auto` 对不同文件和目录类型，使用不同颜色显示。

- 黑色（black）：常规文件
- 蓝色（blue）：目录
- 浅绿色（aqua）：符号链接
- 绿色（green）：可执行文件

## 选项

### 文件筛选选项

- `-a`, `--all`

不忽略以 `.` 开头的文件（即隐藏文件）。

- `-A`, `--almost-all`

不忽略以 `.` 开头的文件，即忽略 `.` 和 `..`。

`--all (-a)` 选项会覆盖该选项。

- `-B`, `--ignore-backups`

在目录中忽略以 `~` 结尾的文件。该选项等价于 `--ignore='.*~'`。

- `-d`, `--directory`

仅列出目录的名称，而不列出其内容。除了指定 `--dereference-command-line (-H)`, `--dereference (-L)` 或 `--dereference-command-line-symlink-to-dir`，否则不跟踪符号链接。

- `--hide=PATTERN`

忽略名称匹配 `pattern` 的文件，除非使用了 `--all` 或 `--almost-all` 选项。该选项与 `--ignore=pattern` 功能类似，只是会被 `--all` 和 `--almost` 覆盖。

此选项在 shell 别名中可有用。例如，如果 `lx` 是 `ls --hide='*~''` 的别名，`ly` 是 `ls --ignore-'*~'` 的别名，则 `lx -A` 可以列而出 `README~` 文件，而 `ly -A` 不能。

例如，隐藏以 `a` 开头的文件：

```bash
$ ls --hide=a*
```

- `-R`, `--recursive`

递归列出所有目录的内容。

### 输出信息选项

- `-l`, `--format=long`, `--format=verbose`

长格式。除了文件名，还输出文件类型、文件模式 bits、硬链接数，owner 名称、group 名称、大小和时间戳（通常为修改时间戳）。如果无法确定 owner 或 group 名称，则打印 owner 或 group 的 ID（右对齐与文本区分）。其它取法确定的信息用 `?` 表示。

文件大小通常为字节数，但可以修改。例如 `--human-readable (-h)` 打印缩写的易读的计数，而 `--block-size="1"` 输出包含千位分隔符的字节计数。

对列出的每个目录，在前面多一行 `total blocks`，其中 `blocks` 是系文件系统分配给目录中所有文件的空间。block 默认 1024 byte，也可以覆盖。

文件类型是如下字符之一：

| 字符 | 类型 |
|--|--|
| `-` | 常规文件 |
| `b` | block 特殊文件 |
| `c` | 字符特殊文件 |
| `C` | 高性能（连续数据）文件 |
| `d` | 目录 |
| `D` | door (Solaris) |
| `l` | 符号链接 |
| `M` | off-line (“migrated”) file (Cray DMF) |
| `n` | network special file (HP-UX) |
| `p` | FIFO (named pipe) |
| `P` | port (Solaris) |
| `s` | socket |
| `?` | 其它文件类型 |



### 格式化选项

- `-F`, `--classify [=when]`, `--indicator-style=classify`

在每个文件后面添加一个字符，指示文档类型。

| 文件 | 字符 |
|--|--|
| 常规可执行文件 | `*` |
| 目录 | `/` |
| 符号链接 | `@` |
| FIFOs | ` | ` |
| sockets | `=` |
| doors | `>` |
| 常规文件 | 无 |

`when` 可以省略，或者为：

- `none`，不分类，默认
- `auto`，当标准输出为终端时分类
- `always`，总是分类

指定 `--classify` 不指定 `when` 等价于 `--classify=always`。


### 输出排序

- `-S`, `--sort=size`

按文件大小排序，大的优先。

- `-t`, `--sort=time`

根据修改时间戳（timestamp）排序，最新在前。可以用 `--time` 选项修改顺序。

|选项|长选项|说明|
|---|---|---|
|`-r`|`--reverse`|以相反顺序显示结果(默认依字母升序)|
|-A||同 -a ，但不列出 “.” (当前目录) 及 “..” (父目录)|
|`-h`|`--human-readable`|当以长格式列出时，以人可读的格式输出文件大小，而不是字节数|
|`-i`||输出文件的索引节点信息|
|-m||水平列出文件，以逗号间隔|
|-X||按文件扩展名排序|
|`--color`||输出信息中带有着色效果|

- **隐藏文件**

隐藏的文件或目录以 `.` 开头，`ls` 默认不显示。这些文件通常为配置文件或目录里。使用 `-a` 选项可查看。


## 信息说明

下面是一个长格式的输出：

```sh
total 24
drwxr-xr-x. 4 5078 5001     4096 Aug  3  2020 data/
-rw-r--r--. 1 root root 30310596 May 30 21:19 data.tar.gz
drwxr-xr-x. 3 5078 5001       41 Apr 24  2020 Linux_x86_64/
-rwxr-xr-x. 1 5078 5001     1528 May 30 21:32 netMHCpan*
```

`total`

1. **第一个字段**包含文件的访问权限，10 个字符

|编号|说明|选项|
|---|---|---|
|1|文件类型| `-` 普通文件, `d` 目录，`l` 符号链接|
|2-4|文件所有者访问权限|
|5-7|文件所属组成员的访问权限|
|9-10|其它所有人的访问权限|

2. 第二个字段是文件的**硬链接**数。
3. `root` or `5078`，文件所有者（owner）名称
4. `root` or `5001`，文件所属用户组（group）名称
5. 4096，文件大小（字节数）
6. 文件修改时间
7. 文件名

> **NOTE**
> 1. 对目录，显示的大小 (如 4096)是包含目录信息的文件大小，而不是目录所包含所有文件的大小。
> 


## 实例

- 输出当前目录中的文件（默认不含隐藏文件）

```sh
$ ls
anaconda-ks.cfg  initial-setup-ks.cfg  local
```

- 输出当前目录中的文件（含隐藏文件）

```sh
$ ls -a
.   anaconda-ks.cfg  .bash_logout   .bashrc  .config  .dbus                 local  .subversion  .viminfo
..  .bash_history    .bash_profile  .cache   .cshrc   initial-setup-ks.cfg  .pki   .tcshrc      .Xauthority
```

- 输出文件的长格式，包含详情信息

```sh
$ ls -l
total 8
-rw-------. 1 root root 2089 Feb 17 08:04 anaconda-ks.cfg
-rw-r--r--. 1 root root 2120 Feb 17 08:23 initial-setup-ks.cfg
drwxr-xr-x. 6 root root   56 May 27 11:05 local
```

- 输出**指定目录**中的文件列表

```sh
$ ls /root/local
bin  include  lib  share
```

- 列出**多个目录**中的文件列表

```sh
$ ls ~ /usr
/root:
anaconda-ks.cfg  initial-setup-ks.cfg  local

/usr:
bin  etc  games  include  java  lib  lib64  libexec  local  sbin  share  src  tmp
```

- 输出文件名称及索引节点信息

```sh
$ ls -li
total 8
62277116535 drwxr-xr-x. 2 root root   30 Jun  8 11:35 dir1
64425670017 drwxr-xr-x. 2 root root   30 Jun  8 11:36 dir2
53692827390 -rw-r--r--. 4 root root 2689 Jun  8 11:29 fun
53692827390 -rw-r--r--. 4 root root 2689 Jun  8 11:29 fun-hard
```

`fun-hard` 是 `fun` 的硬链接，所以两者指向相同的数据块，因此索引节点相同。

- 搭配通配符一起使用，输出指定目录中所有以sd开头的文件名称

```sh
[root@linuxcool ~]# ls /dev/sd*
/dev/sda  /dev/sda1  /dev/sda2
```

- 按时间顺序输出

```sh
[root@localhost usr]# ls -lt
total 320
drwxr-xr-x.  16 root root   194 Jun  6 15:43 local
dr-xr-xr-x.   2 root root 61440 Jun  5 22:29 bin
drwxr-xr-x. 274 root root  8192 Jun  5 09:34 share
drwxr-xr-x.  81 root root  8192 Jun  5 09:34 include
dr-xr-xr-x.   2 root root 20480 Jun  4 03:08 sbin
dr-xr-xr-x.  46 root root  4096 Jun  4 03:08 lib
dr-xr-xr-x. 176 root root 98304 Jun  2 08:13 lib64
drwxr-xr-x.  55 root root 12288 Jun  2 08:13 libexec
drwxr-xr-x.   3 root root    55 May 17 02:02 java
drwxr-xr-x.   4 root root    34 Feb 17 07:54 src
lrwxrwxrwx.   1 root root    10 Feb 17 07:54 tmp -> ../var/tmp
drwxr-xr-x.   2 root root     6 Apr 11  2018 etc
drwxr-xr-x.   2 root root     6 Apr 11  2018 games
```

## 参考

- https://www.gnu.org/software/coreutils/ls
- https://www.gnu.org/software/coreutils/manual/html_node/Which-files-are-listed.html
- https://www.gnu.org/software/coreutils/manual/html_node/What-information-is-listed.html