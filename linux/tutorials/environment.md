# 环境

- [环境](#环境)
  - [简介](#简介)
  - [检查环境变量](#检查环境变量)
  - [常见环境变量](#常见环境变量)
  - [把可执行文件添加到环境变量](#把可执行文件添加到环境变量)

***

## 简介

shell 在环境中存储了两种基本类型的数据局：

- 环境变量
- shell 变量

Shell 变量是 bash 存放的少量数据，剩下的都是环境变量。

## 检查环境变量

`set` 可以显示 shell 或环境变量。

`printenv` 只显示环境变量。

因为环境变量列表比较长，最好把命令的输出管道传递给 less 来阅读：

```sh
printenv | less
```

运行后，可以看到环境变量信息 ：

```sh
MANPATH=/opt/rh/devtoolset-7/root/usr/share/man:
XDG_SESSION_ID=1139
HOSTNAME=localhost.localdomain
SELINUX_ROLE_REQUESTED=
TERM=xterm
SHELL=/bin/bash
HISTSIZE=1000
SSH_CLIENT=10.20.84.251 3621 22
PERL5LIB=/opt/rh/devtoolset-7/root//usr/lib64/perl5/vendor_perl:/opt/rh/devtoolset-7/root/usr/lib/perl5:/opt/rh/devtoolset-7/root//usr/share/perl5/vendor_perl
SELINUX_USE_CURRENT_RANGE=
SSH_TTY=/dev/pts/0
PCP_DIR=/opt/rh/devtoolset-7/root
USER=root
LD_LIBRARY_PATH=/opt/rh/devtoolset-7/root/usr/lib64:/opt/rh/devtoolset-7/root/usr/lib:/opt/rh/devtoolset-7/root/usr/lib64/dyninst:/opt/rh/devtoolset-7/root/usr/lib/dyninst:/opt/rh/devtoolset-7/root/usr/lib64:/opt/rh/devtoolset-7/root/usr/lib
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=01;05;37;41:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=:...skipping...
MANPATH=/opt/rh/devtoolset-7/root/usr/share/man:
XDG_SESSION_ID=1139
HOSTNAME=localhost.localdomain
SELINUX_ROLE_REQUESTED=
TERM=xterm
SHELL=/bin/bash
HISTSIZE=1000
PERL5LIB=/opt/rh/devtoolset-7/root//usr/lib64/perl5/vendor_perl:/opt/rh/devtoolset-7/root/usr/lib/perl5:/opt/rh/devtoolset-7/root//usr/share/perl5/vendor_perl
SELINUX_USE_CURRENT_RANGE=
SSH_TTY=/dev/pts/0
PCP_DIR=/opt/rh/devtoolset-7/root
USER=root
LD_LIBRARY_PATH=/opt/rh/devtoolset-7/root/usr/lib64:/opt/rh/devtoolset-7/root/usr/lib:/opt/rh/devtoolset-7/root/usr/lib64/dyninst:/opt/rh/devtoolset-7/root/usr/lib/dyninst:/opt/rh/devtoolset-7/root/usr/lib64:/opt/rh/devtoolset-7/root/usr/lib
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=01;05;37;41:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=01;36:*.au=01;36:*.flac=01;36:*.mid=01;36:*.midi=01;36:*.mka=01;36:*.mp3=01;36:*.mpc=01;36:*.ogg=01;36:*.ra=01;36:*.wav=01;36:*.axa=01;36:*.oga=01;36:*.spx=01;36:*.xspf=01;36:
MAIL=/var/spool/mail/root
PATH=/opt/rh/devtoolset-7/root/usr/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
PWD=/root
LANG=en_US.UTF-8
SELINUX_LEVEL_REQUESTED=
HISTCONTROL=ignoredups
SHLVL=1
HOME=/root
PYTHONPATH=/opt/rh/devtoolset-7/root/usr/lib64/python2.7/site-packages:/opt/rh/devtoolset-7/root/usr/lib/python2.7/site-packages
LOGNAME=root
XDG_DATA_DIRS=/root/.local/share/flatpak/exports/share:/var/lib/flatpak/exports/share:/usr/local/share:/usr/share
SSH_CONNECTION=10.20.84.251 3621 10.20.19.147 22
INFOPATH=/opt/rh/devtoolset-7/root/usr/share/info
XDG_RUNTIME_DIR=/run/user/0
DISPLAY=localhost:10.0
```

上面列出的是环境变量及其数值列表。上面的 `USER` 变量，表示当前用户。

- `printenv` 也能够列出特定变量的数值

```sh
[root@localhost ~]# printenv USER
root
```

- 使用无选项和参数的 `set` 命令，显示 shell 变量、环境变量和定义的 shell 函数

与 `printenv` 不同，set 命令的输出按首字母顺序排列

```sh
set
```

- 也可以使用 `echo` 命令来查看变量内容

```sh
[root@localhost ~]# echo $HOME
/root
```

别名无法用 `set` 或 `printenv` 查看，可以用 `alias` 查看别名：

```sh
[root@localhost ~]# alias
alias cp='cp -i'
alias l.='ls -d .* --color=auto'
alias ll='ls -l --color=auto'
alias ls='ls --color=auto'
alias mv='mv -i'
alias rm='rm -i'
alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'
```

## 常见环境变量

|变量|内容|
|---|---|
|DISPLAY|如果正在运行图形界面环境，该变量为显示器名字。通常为 ":0"，意思是由 X 的第一个显示器|
|EDITOR|文本编辑器名称|
|SHELL|shell 程序名称|
|HOME|用户家目录|
|LANG|字符集以及语言编码方式。|
|OLD_PWD|先前的工作目录|
|PAGER|页输出程序的名字。这经常设置为/usr/bin/less|
|PATH|由冒号分开的目录列表，当你输入可执行程序名后，会搜索这个目录列表|
|PS1|Prompt String 1. 定义 shell 提示符的内容。随后我们可以看到，这个变量内容可以定制|
|PWD|当前工作目录|
|TERM|终端类型名。类 Unix 系统支持许多终端协议；该变量指定终端仿真器所用的协议|
|TZ|所在时区。大多数类 Unix 系统使用 UTC 时间，根据该变量指定的偏差来显示本地时间|
|USER|用户名|

## 把可执行文件添加到环境变量

1. 创建软连接放到 `/usr/bin` 或 `/usr/sbin` 目录

```sh
ln -s /home/a/program /usr/bin/program
```

2. 添加到环境变量

在 `/etc/profile` 后面添加：

```sh
PATH=/home/a/program
```