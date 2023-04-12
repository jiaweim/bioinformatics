# alias

- [alias](#alias)
  - [简介](#简介)
  - [创建别名](#创建别名)
  - [删除别名](#删除别名)
  - [惯用选项](#惯用选项)

***

## 简介

使用分号为分隔符，可以一行输入多个命令：

```bash
command1; command2; command3
```

例如：

```bash
mjw@happy:~$ cd /usr; ls; cd -
bin  games  include  lib  lib32  lib64  libexec  libx32  local  sbin  share  src
/home/mjw
mjw@happy:~$
```

这里有三个命令：

- `cd /usr` 将 `/usr` 设为当前工作目录
- `ls` 列出目录内容
- `cd -` 返回之前目录

## 创建别名

下面使用 `alias` 将这三个命令合并为一个新命令。比如命名为 `test`，先查看 `test` 是否被占用：

```bash
mjw@happy:~$ type test
test is a shell builtin
```

`test` 已经被占用了，换 foo 试试：

```bash
mjw@happy:~$ type foo
-bash: type: foo: not found
```

foo 可以用。然后开始创建别名：

```bash
$ alias foo='cd /usr; ls; cd -'
```

注意，别名语法：

```bash
$ alias name='string'
```

然后就能直接使用 foo 命令：

```bash
mjw@happy:~$ foo
bin  games  include  lib  lib32  lib64  libexec  libx32  local  sbin  share  src
/home/mjw
```

用 `type` 查看 foo：

```bash
mjw@happy:~$ type foo
foo is aliased to `cd /usr; ls; cd -'
```

## 删除别名

用 unalias 删除别名：

```bash
$ unalias foo
$ type foo
-bash: type: foo: not found
```

## 惯用选项

别名常用于为命令添加惯用选项。例如，`ls` 通过别名添加颜色支持：

```bash
$ type ls
ls is aliased to `ls --color=auto'
```

要知道系统中定义的其它别名，用不加参数的 `alias` 即可。下面是 Ubuntu 中默认定义的别名：

```bash
mjw@happy:~$ alias
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias l='ls -CF'
alias la='ls -A'
alias ll='ls -alF'
alias ls='ls --color=auto'
```

> **NOTE**
> 在命令行定义别名还有一个问题，在 Shell 会话结束后，这些别名会随之消失。所以需要将别名添加到系统环境初始化文件中。
