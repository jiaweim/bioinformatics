# ls

- [ls](#ls)
  - [简介](#简介)
  - [实例](#实例)
  - [长格式信息说明](#长格式信息说明)
  - [参考](#参考)

2022-06-06, 12:31
@author Jiawei Mao
*****

## 简介

`ls` (list) 列举指定目录下的文件名称及其属性。

默认不加参数的情况下，`ls` 命令会列出当前工作目录中的文件信息，经常与`cd` 和 `pwd` 命令搭配使用，十分方便。而带上参数后，则可以做更多的事情。

```sh
ls [选项] [文件]
```

|选项|长选项|说明|
|---|---|---|
|`-a`|`--all`|显示以 `.` 开头的隐藏文件|
|`-l`||使用长格式列出文件及目录的详细信息|
|`-r`|`--reverse`|以相反顺序显示结果(默认依字母升序)|
|`-t`||按文件最后修改时间排序|
|-A||同 -a ，但不列出 “.” (当前目录) 及 “..” (父目录)|
|`-S`||根据文件大小排序|
|-R||递归列出所有子目录|
|`-d`|`--directory`|查看目录的信息，而不是里面子文件的信息，将其与 `-l` 选项结合，可以查看指定目录的详细信息，而不是目录中的内容|
|`-F`|`--classify`|在列出的名字后面加一个指示符，如果是目录，后面会加上 `/` 字符|
|`-h`|`--human-readable`|当以长格式列出时，以人可读的格式输出文件大小，而不是字节数|
|`-i`||输出文件的索引节点信息|
|-m||水平列出文件，以逗号间隔|
|-X||按文件扩展名排序|
|`--color`||输出信息中带有着色效果|

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

## 长格式信息说明

下面是一个长格式的输出：

```sh
drwxr-xr-x. 4 5078 5001     4096 Aug  3  2020 data/
-rw-r--r--. 1 root root 30310596 May 30 21:19 data.tar.gz
drwxr-xr-x. 3 5078 5001       41 Apr 24  2020 Linux_x86_64/
-rwxr-xr-x. 1 5078 5001     1528 May 30 21:32 netMHCpan*
```

1. **第一个字段**包含文件的访问权限。

|编号|说明|选项|
|---|---|---|
|1|文件类型| `-` 表示普通文件, `d` 表示目录|
|2-4|文件所有者访问权限|
|5-7|文件所属组成员的访问权限|
|9-10|其它所有人的访问权限|

2. 第二个字段是文件的**硬链接**数。
3. `root` or `5078`，文件所有者的用户名
4. `root` or `5001`，文件所属用户组的名字
5. 4096，文件大小（字节数）
6. 文件修改时间
7. 文件名

## 参考

- 