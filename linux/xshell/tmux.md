# tmux

- [tmux](#tmux)
  - [简介](#简介)
  - [安装](#安装)
    - [从源码安装](#从源码安装)
  - [使用](#使用)
  - [参考](#参考)

2022-05-27, 22:23
***

## 简介

tmux 的业务逻辑：

```sh
# tmux的层次：
-session1
---window1
------subwindow1
------subwindow2
------subwindow3
------subwindow4
---window2
-session2
---window3
---window4
```

即：

- tmux 可以开启多个 session
- 一个 session 可以开多个 window
- 一个 window 可以分多个 subwindow

## 安装

ubuntu 安装：

```sh
sudo apt-get install tmux
```

### 从源码安装

tmux 需要两个包：

1. libevent
2. ncurses

另外，tmux 还需要 C 编译器，make, yacc (或 bison)以及 pkg-config.

**安装 libevent:**

```sh
wget 
```

configure: error: “curses not found” 类似not found这种错误都是缺少相关的依赖包~ 直接安装就好

```sh
yum install ncurses-devel 
```

## 使用

- 创建 session

```sh
tmux
```

- 创建命名 session

```sh
tmux new -s my_session
```

- 显示所有 session

```sh
tmux ls
```

- 使用 session 编号接入

```sh
tmux attach -t 0
```

- 使用 session 名称接入

```sh
tmux attach -t <session-name>
tmux a -t name # 简写
```

tmux 默认的前缀操作是 Ctrl+b，按完松开，再按下一个键。



## 参考

- https://github.com/tmux/tmux/wiki/Installing
- https://github.com/tmux/tmux/wiki/Getting-Started
