# 重定向

- [重定向](#重定向)
  - [简介](#简介)
  - [标准输出、标准输入和标准错误](#标准输出标准输入和标准错误)
  - [标准输出重定向](#标准输出重定向)
  - [标准错误重定向](#标准错误重定向)
    - [标准输出和标准错误重定向到同一个文件](#标准输出和标准错误重定向到同一个文件)
    - [丢弃输出结果](#丢弃输出结果)
  - [标准输入重定向](#标准输入重定向)
  - [管道](#管道)
    - [排序列表](#排序列表)
    - [uniq 报告或忽略重复行](#uniq-报告或忽略重复行)
    - [wc 统计换行符、单词的数量](#wc-统计换行符单词的数量)
    - [grep 输出与模式匹配的行](#grep-输出与模式匹配的行)
    - [head/tail](#headtail)
    - [tee](#tee)

Last updated: 2023-04-17, 13:59
****

## 简介

I/O 重定向涉及如下命令：

- cat，拼接文件
- sort，排序文本行
- uniq，报告或忽略重复的行
- wc，统计文件中换行符、单词以及字节的数量
- grep，输出与模式匹配的行
- head，输出文件的开头部分
- tail，输出文件的结尾部分
- tee，读取标准输入并将输出结果写入标准输出和文件

|操作符|操作|
---|---
`>`|标准输出重定向（覆盖）
`>>`|标准输出重定向（追加）
`2>`|标准错误重定向（覆盖）
`&>`|标准输出和标准错误重定向（覆盖）
`&>>`|标准输出和标准错误重定向（追加）
`2> /dev/null`|丢弃错误信息
`cat filename`|将文本复制到标准输出
`cat`|复制标准输入到标准输出

## 标准输出、标准输入和标准错误

程序（如 ls）将运行结果和状态消息分别发送到标准输出（stdout）和标准错误（stderr）的特殊文件。在默认情况下，标准输出和标准错误与显示器屏幕关联，并不会保存到文件。

另外，许多程序从标准输入（stdin）中获取输入，默认，标准输入与键盘相关联。

## 标准输出重定向

使用重定向操作符 `>` 将标准输出重定向到其它文件，后面跟上文件名即可。

例如，将 `ls` 命令的输出结果保存在 ls-output.txt 中：

```bash
$ ls -l /usr/bin > ls-output.txt
$ ls -l ls-output.txt
-rw-r--r-- 1 mjw mjw 52401 Apr 17 09:21 ls-output.txt
```

对一个不存在的目录使用 `ls`：

```bash
$ ls -l /bin/usr > ls-output.txt
ls: cannot access '/bin/usr': No such file or directory
```

接收到一条错误信息，直接显示在屏幕上。

这是因为 `ls` 没有将错误消息发送到标准输出。和大多数编写良好的 UNIX 程序一样，ls 将错误信息发送到标准错误。由于只重定向了标准输出，并未重定向标准错误，所以错误信息依旧在屏幕上显示。

查看此时的输出文件：

```bash
mjw@happy:~$ ls -l ls-output.txt
-rw-r--r-- 1 mjw mjw 0 Apr 17 09:25 ls-output.txt
```

文件大小为 0。这是因为重定向 `>` 会覆盖目标文件。也可以使用该方法直接清空某个文件（或创建一个新的文件）：

```bash
mjw@happy:~$ > ls-output.txt
```

- 重定向操作符 `>>` 将输出追加到文件末尾，如果指定文件不存在，新建该文件

```bash
mjw@happy:~$ ls -l /usr/bin >> ls-output.txt
mjw@happy:~$ ls -l /usr/bin >> ls-output.txt
mjw@happy:~$ ls -l /usr/bin >> ls-output.txt
mjw@happy:~$ ls -l ls-output.txt
-rw-r--r-- 1 mjw mjw 157203 Apr 17 09:37 ls-output.txt
```

重复执行三次，输出文件 ls-output.txt 也扩大了三倍。

## 标准错误重定向

标准错误没有专门的重定向操作符，只能引用其文件描述符。

Shell 内部分别用文件描述符 0、1和2引用标准输入、标准输出和标准错误。因此可用下列语法来重定向到标准错误：

```bash
mjw@happy:~$ ls -l /bin/usr 2> ls-error.txt
```

文件描述符 2 紧靠在重定向操作符之前，将标准错误重定向到 ls-error.txt。

### 标准输出和标准错误重定向到同一个文件

有两种实现方法。

- 传统方法适合于旧版 Shell：

```bash
mjw@happy:~$ ls -l /bin/usr > ls-output.txt 2>&1
```

这里执行了两次重定向：

- 先将标准输出重定向到 ls-output.txt
- 然后用 `2>&1` 将文件描述符 2 （标准错误）重定向到文件描述符 1（标准输出）

> **NOTE**
> 标准错误的重定向必须在标准输出重定向之后执行，否则无效。

- 新版 Bash 可以采用联合重定向

```bash
mjw@happy:~$ ls -l /bin/usr &> ls-output.txt
```

这里 `&>` 将标准输出和标准错误重定向到 ls-output.txt。

- 将标准输出和标准错误追加到单个文件

```bash
mjw@happy:~$ ls -l /bin/usr &>> ls-output.txt
```

### 丢弃输出结果

将输出结果重定向到 `/dev/null` 特殊文件，表示丢弃该信息。该文件是一个系统设备，能够接收输入结果但不做任何处理。

- 丢弃命令的错误信息

```bash
$ ls -l /bin/usr 2> /dev/null
```

## 标准输入重定向

`cat` 读取一个或多个文件并将其复制到**标准输出**:

```bash
$ cat filename
```

例如，显示 ls-output.txt 的内容：

```bash
mjw@happy:~$ cat ls-output.txt
```

`cat` 常用于显示比较短的文本文件。因为 cat 能够接收多个文件，所以还可用于将文件拼接在一起。假设我们下载了一个被分割成多个部分的文件，希望将其还原，如果这些文件命名为：

```bash
movie.mpeg.001 movie.mpeg.002 ... movie.mpeg.099
```

使用下列命令进行拼接：

```bash
$ cat movie.mpeg.0* > movie.mpeg
```

因为通配符会按顺序扩展，所以 `cat` 命令的参数排列不会出错。

那么 `cat` 与标准输入有什么关系呢？

不带参数的 `cat` 从标准输入读取。因为标准输入默认和键盘绑定，所以 `cat` 会等待从键盘输入，Ctrl+D 表示输入结束。

```bash
mjw@happy:~$ cat
Twinkle Twinkle Little Star
Twinkle Twinkle Little Star
```

因为 `cat` 将标准输入复制到标准输出，所以看到了重复显示的两行文本。

假设我们要创建一个 little_star.txt 文件，包含上面的文本内容：

```bash
mjw@happy:~$ cat > little_star.txt
Twinkle Twinkle Little Star
```

## 管道

管道操作符 `|` 将一个命令的标准输出传给另一个命令的标准输入。

```bash
$ command1 | command2
```

例如，对将结果发往标准输出的命令，都可以使用 less 将其输出结果逐页显示出来：

```bash
mjw@happy:~$ ls -l /usr/bin | less
```

管道一般用来执行复杂的数据操作。也可以把多个命令组合起来形成管道，这种方式用到的命令通常被称为过滤器。过滤器获取输入，对其进行改动，然后输出。

### 排序列表

把 `/bin` 和 `/usr/bin` 目录下的所有可执行文件合并成一个列表，然后排序：

```bash
mjw@happy:~$ ls /bin /usr/bin | sort | less
```

> **NOTE**
> `>` 与 `|` 的差异
> `>` 连接命令与文件，`|` 将一个命令的输出结果与另一个命令的输入连接在一起

### uniq 报告或忽略重复行

`uniq` 通常与 `sort` 配合使用。`uniq` 可以从标准输入或单个文件名参数或获取有序的数据列表，默认删除所有重复行。

```bash
mjw@happy:~$ ls /bin /usr/bin | sort | uniq | less
```

如果想看看有哪些重复行，可以使用 `uniq -d` 选项。

### wc 统计换行符、单词的数量

wc (word count)统计文件中换行符、单词以及 byte 数。例如：

```bash
mjw@happy:~$ wc ls-output.txt
  2  18 112 ls-output.txt
```

上面三个数字分别为：行数、单词数、字节数。

如果没有命令行参数，`wc` 从标准输入中读取。

### grep 输出与模式匹配的行

```bash
$ grep pattern filename
```

`grep` 用于在文件中查找文本模式。

假设要从程序列表中找出名称中包含 `zip` 的所有文件，从而知道系统中有多少与压缩相关的程序：

```bash
mjw@happy:~$ ls /bin /usr/bin | sort | uniq | grep zip
funzip
gpg-zip
gunzip
gzip
streamzip
unzip
unzipsfx
zipdetails
zipgrep
zipinfo
```

grep 命令有两个很方便的选项：

- `-i` 忽略大小写（默认区分）
- `-v` 只输出不匹配指定模式的行

### head/tail

head 和 tail 分别输出文件的前 10 行和后 10 行。通过 `-n` 选项可以调整行数：

```bash
mjw@happy:~$ head -n 5 ls-output.txt
total 98744
-rwxr-xr-x 1 root root     141816 Oct  1  2021 DistanceEst
lrwxrwxrwx 1 root root          4 Feb 17  2020 NF -> col1
lrwxrwxrwx 1 root root          1 Mar 25  2022 X11 -> .
-rwxr-xr-x 1 root root      51632 Feb  8  2022 [
mjw@happy:~$ tail -n 5 ls-output.txt
-rwxr-xr-x 1 root root       2959 Oct  8  2022 zipgrep
-rwxr-xr-x 2 root root     174512 Oct  8  2022 zipinfo
-rwxr-xr-x 1 root root       2206 Sep  5  2022 zless
-rwxr-xr-x 1 root root       1842 Sep  5  2022 zmore
-rwxr-xr-x 1 root root       4577 Sep  5  2022 znew
```

这两个命令都可以用在管道中：

```bash
mjw@happy:~$ ls /usr/bin | tail -n 5
zipgrep
zipinfo
zless
zmore
znew
```

### tee

为了和管道的比较保持一致，Linux 还提供了 `tee` 命令，`tee` 表示 T 形头，用于从标准输入读取内容，然后将其复制到标准输出和其它文件中。

例如，将 grep 过滤前加入 tee 命令，将整个目录列表保存到 ls.txt：

```bash
mjw@happy:~$ ls /usr/bin | tee ls.txt | grep zip
funzip
gpg-zip
gunzip
gzip
streamzip
unzip
unzipsfx
zipdetails
zipgrep
zipinfo
```

