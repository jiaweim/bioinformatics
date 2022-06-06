# ls

- [ls](#ls)
  - [简介](#简介)
  - [实例](#实例)

2022-06-06, 12:31
****

## 简介

`ls` (list)列举指定目录下的文件名称及其属性。

默认不加参数的情况下，`ls` 命令会列出当前工作目录中的文件信息，经常与`cd` 和 `pwd` 命令搭配使用，十分方便。而带上参数后，则可以做更多的事情。

```sh
ls [参数] [文件]
```

|参数|说明|
|---|---|
|`-a`|显示所有文件及目录 (包括以“.”开头的隐藏文件)|
|`-l`|使用长格式列出文件及目录的详细信息|
|-r|将文件以相反次序显示(默认依英文字母次序)|
|-t|根据最后的修改时间排序|
|-A|同 -a ，但不列出 “.” (当前目录) 及 “..” (父目录)|
|-S|根据文件大小排序|
|-R|递归列出所有子目录|
|-d|查看目录的信息，而不是里面子文件的信息|
|`-i`|输出文件的inode节点信息|
|-m|水平列出文件，以逗号间隔|
|-X|按文件扩展名排序|
|`--color`|输出信息中带有着色效果|

## 实例

- 输出当前目录中的文件（默认不含隐藏文件）

```sh
[root@localhost ~]# ls
anaconda-ks.cfg  initial-setup-ks.cfg  local
```

- 输出当前目录中的文件（含隐藏文件）

```sh
[root@localhost ~]# ls -a
.   anaconda-ks.cfg  .bash_logout   .bashrc  .config  .dbus                 local  .subversion  .viminfo
..  .bash_history    .bash_profile  .cache   .cshrc   initial-setup-ks.cfg  .pki   .tcshrc      .Xauthority
```

- 输出文件的长格式，包含详情信息

```sh
[root@localhost ~]# ls -l
total 8
-rw-------. 1 root root 2089 Feb 17 08:04 anaconda-ks.cfg
-rw-r--r--. 1 root root 2120 Feb 17 08:23 initial-setup-ks.cfg
drwxr-xr-x. 6 root root   56 May 27 11:05 local
```

- 输出指定目录中的文件列表

```sh
[root@localhost ~]# ls /root/local
bin  include  lib  share
```

- 输出文件名称及inode属性块号码

```sh
[root@localhost ~]# ls -i
100663406 anaconda-ks.cfg  100663436 initial-setup-ks.cfg   67735619 local
```

- 搭配通配符一起使用，输出指定目录中所有以sd开头的文件名称

```sh
[root@linuxcool ~]# ls /dev/sd*
/dev/sda  /dev/sda1  /dev/sda2
```
