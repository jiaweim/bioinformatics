# Shell 变量

- [Shell 变量](#shell-变量)
  - [简介](#简介)
  - [常见 Shell 环境变量](#常见-shell-环境变量)

***

## 简介

shell 本身将用户在 shell 会话中可能有用的信息存储在变量中。例如：

- `$SHELL` 定义当前 SHELL 的识别符；
- `$PS1` 定义 SHELL 提示符；
- `$MAIL` 定义用户邮箱

使用 `set` 命令查看当前 shell 的所有变量。其中局部变量部分称为环境变量。使用 `env` 查看环境变量。

输入 `echo $VALUE` 查看特定环境变量，其中 `VALUE` 为环境变量名称。也可以使用 `declare` 查看当前环境变量名称和值，以及 shell 函数列表。

除了自己设置的变量，系统文件也设置变量，如配置文件位置、邮箱、路径等变量。系统文件还可以存储 shell 提示符的值、历史记录列表的大小、操作系统类型等变量。在变量名前加上 `$` 即可在命令行中访问变量值。例如：

```bash
$ echo $USER
mjw
```

启用 shell 时，会自动设置许多环境变量。

## 常见 Shell 环境变量

|变量|说明|
|---|---|
BASH|`bash` 命令的完整路径，通常为 `/bin/bash`
BASH_VERSION|`bash` 的版本
EUID|当前用户的有效用户 ID 编号。在 shell 启动时根据用户在 `/etc/passwd` 文件中的信息分配
FCEDIT|指定 `fc` 命令用来编辑历史的文本编辑器
HISTFILE|历史文件位置，一般位于 `$HOME/.bash_history`
HISTFILESIZE|保存的历史数目，达到该值后，最老的记录被删除，默认 1000
HISTCMD This returns the number of the current command in the history list.
HOME This is your home directory. It is your current working directory each time
you log in or type the cd command with any options.
HOSTTYPE This is a value that describes the computer architecture on which the Linux
system is running. For most modern PCs, the value is x86 _ 64.
MAIL This is the location of your mailbox file. The file is typically your username in
the /var/spool/mail directory.
OLDPWD This is the directory that was the working directory before you changed to
the current working directory.
OSTYPE This name identifies the current operating system. For Ubuntu, the OSTYPE
value is either linux or linux-gnu, depending on the type of shell you are
using. (Bash can run on other operating systems as well.)
PATH This is the colon-separated list of directories used to find commands that you
type. The default value for regular users varies for different distributions but
typically includes the following: /bin:/usr/bin:/usr/local/bin:/usr/
bin/X11:/usr/X11R6/bin:~/bin. You need to type the full path or a relative
path to a command that you want to run which is not in your PATH. For the
root user, the value also includes /sbin, /usr/sbin, and /usr/local/sbin.
PPID This is the process ID of the command that started the current shell (for
example, the Terminal window containing the shell).
PROMPT _
COMMAND
This can be set to a command name that is run each time before your shell
prompt is displayed. Setting PROMPT_COMMAND=date lists the current
date/time before the prompt appears.
PS1 This sets the value of your shell prompt. There are many items that you can
read into your prompt (date, time, username, hostname, and so on). Sometimes
a command requires additional prompts, which you can set with the
variables PS2, PS3, and so on.
PWD This is the directory that is assigned as your current directory. This value
changes each time you change directories using the cd command.
RANDOM Accessing this variable causes a random number to be generated. The
number is between 0 and 99999.
SECONDS This is the number of seconds since the time the shell was started.
SHLVL This is the number of shell levels associated with the current shell session.
When you log in to the shell, the SHLVL is 1. Each time you start a new Bash
command (by, for example, using su to become a new user, or by simply
typing bash), this number is incremented.
TMOUT This can be set to a number representing the number of seconds the shell
can be idle without receiving input. After the number of seconds is reached,
the shell exits. This security feature makes it less likely for unattended shells
to be accessed by unauthorized people. (This must be set in the login shell
for it actually to cause the shell to log out the user.)