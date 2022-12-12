# screen

- [screen](#screen)
  - [简介](#简介)
  - [操作](#操作)
  - [调用 Screen](#调用-screen)
  - [创建 Windows](#创建-windows)
  - [Session 中的操作](#session-中的操作)
  - [参考](#参考)

2022-05-30, 09:06
***

## 简介

screen 创建的虚拟终端，有两个工作模式：

- `attached`, 表示当前 screen 正在作为主终端使用，为活跃状态；
- `detached`, 表示当前 screen 正在作为后台使用，为非活跃状态。

## 操作

```sh
$> screen [-AmRvx -ls -wipe][-d <作业名称>][-h <行数>][-r <作业名称>][-s ][-S <作业名称>]
 
-A 　将所有的视窗都调整为目前终端机的大小。
-d   <作业名称> 　将指定的screen作业离线。
-h   <行数> 　指定视窗的缓冲区行数。
-m 　即使目前已在作业中的screen作业，仍强制建立新的screen作业。
-r   <作业名称> 　恢复离线的screen作业。
-R 　先试图恢复离线的作业。若找不到离线的作业，即建立新的screen作业。
-s 　指定建立新视窗时，所要执行的shell。
-S   <作业名称> 　指定screen作业的名称。
-v 　显示版本信息。
-x 　恢复之前离线的screen作业。
-ls或--list 　显示目前所有的screen作业。
-wipe 　检查目前所有的screen作业，并删除已经无法使用的screen作业。
```

- 创建命名 session

```sh
screen -S yourname
```

- 列出当前 session

```sh
screen -ls
```

- 进入指定名称的 session

```sh
screen -r name
```

- 结束某个 session

```sh
screen -d name
```

- 结束当前 session 并回到名称为 name 的 session

```sh
screen -d -r name
```

- 如果只有一个 session，直接删除，否则提示选择 session 删除

```sh
screen -X quit
```

- 删除指定会话

```sh
screen -X -S session_name quit
```

## 调用 Screen



## 创建 Windows





## Session 中的操作

Ctrl+a (C-a)

|操作|功能|
|---|---|
|C-a ?|显示所有键绑定信息|
|C-a w|显示所有窗口列表|
|C-a C-a|切换到之前显示的窗口|
|C-a c|创建一个新的 shell 窗口，并切换到该窗口|
|C-a n|切换到下一个窗口|
|C-a 0..9|切换到窗口 0..9|
|C-a d|断开会话|
|C-a k|关闭会话|

## 参考

- https://www.gnu.org/software/screen/
- [Screen 用户手册](https://www.gnu.org/software/screen/manual/screen.html)
