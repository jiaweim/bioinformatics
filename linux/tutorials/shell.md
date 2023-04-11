# Shell

- [Shell](#shell)
  - [简介](#简介)
  - [终端仿真器](#终端仿真器)
  - [shell 提示符](#shell-提示符)
  - [命令历史](#命令历史)
  - [命令示例](#命令示例)
  - [结束终端会话](#结束终端会话)
  - [参考](#参考)

Last updated: 2023-04-11, 19:48
****

## 简介

shell 是一个程序，它从键盘接受输入的命令，然后把命令传递给操作系统去执行。几乎所有的Linux 发行版都提供一个名为 `bash` 的来自GNU项目的shell 程序。“bash” 是 “Bourne Again SHell” 的首字母缩写，表明 `bash` 是最初Unix 上由 Steve Bourne 写的 `sh` 的增强版。

## 终端仿真器

当使用图形用户界面时，我们需要另一个和 shell 交互的叫做**终端仿真器**的程序。

如果我们浏览一下桌面菜单，可能会找到。在菜单里它可能都被称为“terminal”，但是 KDE
用的是 `konsole`, 而 GNOME 则使用 `gnome-terminal`。还有其他一些终端仿真器可供Linux 使用，但基本上都是为了让我们能访问 shell。虽然你可能会因为附加的一系列花俏功能而喜欢上某个终端。

## shell 提示符

启动 shell,可以看到一行这样的文字：

```sh
[me@linuxbox ~]$
```

这叫做 shell 提示符，一般以 `用户名@主机名` 的格式，后面紧跟当前用户目录和一个美元符号。

如果提示符最后一个字符是 `#` 而不是 `$`，那么这个终端会话拥有 root 权限。

## 命令历史

按下上箭头按键，可以看到刚才前面输入的命令重新出现在提示符之后。这叫做命令历史。许多Linux 发行版默认保存最后输入的 500 个命令。按下下箭头按键，先前输入的命令就消失了。

## 命令示例

- 显示系统同当前时间和日期 [date](../command/date.md)

```sh
$ date
Sun Jun  5 22:17:34 EDT 2022
```

- 显示当前月份的日历 [cal](../command/cal.md)

```sh
$ cal
      June 2022     
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
```

- 查看磁盘剩余空间 [df](../command/df.md)

```sh
$ df
Filesystem                1K-blocks       Used   Available Use% Mounted on
devtmpfs                  263856572          0   263856572   0% /dev
tmpfs                     263873664          0   263873664   0% /dev/shm
tmpfs                     263873664      53236   263820428   1% /run
tmpfs                     263873664          0   263873664   0% /sys/fs/cgroup
/dev/mapper/centos-root    52403200   12566408    39836792  24% /
/dev/sda2                   1038336     250688      787648  25% /boot
/dev/sda1                    204580      11640      192940   6% /boot/efi
/dev/mapper/centos-home 80302372864 3712241008 76590131856   5% /home
tmpfs                      52774736          4    52774732   1% /run/user/42
tmpfs                      52774736         36    52774700   1% /run/user/1001
tmpfs                      52774736          0    52774736   0% /run/user/1000
tmpfs                      52774736          0    52774736   0% /run/user/0
tmpfs                      52774736          0    52774736   0% /run/user/1006
tmpfs                      52774736          0    52774736   0% /run/user/1005
```

- 显示空闲内存 [free](../command/free.md)

```sh
$ free
              total        used        free      shared  buff/cache   available
Mem:      527747332    25218024     4674428       34420   497854880   500691276
Swap:       4194300      551936     3642364
```

## 结束终端会话

```sh
$ exit
```

## 参考

- https://en.wikipedia.org/wiki/Shell_(computing)
