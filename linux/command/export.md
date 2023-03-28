# export

- [export](#export)
  - [简介](#简介)
  - [$PATH](#path)
  - [添加目录到 $PATH](#添加目录到-path)
  - [参考](#参考)

***

## 简介

在命令行键入命令，shell 会运行一个指定名称的可执行文件。在 Linux 中，这些可执行程序，如 `ls`, `find`, `file` 等，位于系统上的几个不同目录。存储在这些目录中的任何具有执行权限的文件都可以在任何位置运行。保存可执行程序的常见目录有：

- `/bin`
- `/sbin`
- `/usr/sbin`
- `/usr/local/bin`
- `/usr/local/sbin.`

但是 shell 如何知道在哪个目录查找可执行程序？答案很简单，键入命令时，shell 会在用户 `$PATH` 变量中指定的所有目录搜索该名称的可执行文件。

## $PATH

`$PATH` 环境变量是以冒号分隔的目录列表，它告诉 shell要搜索哪些目录以查找可执行文件。

可以用 `printenv` 或 `echo` 来查看 $PATH 包含的目录：

```bash
$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/snap/bin
```

如果在两个不同的目录有相同名称的可执行文件，shell 运行 `$PATH` 中第一个目录中的文件。

## 添加目录到 $PATH

当可执行文件放在不同位置，或者希望有一个专用目录来放置个人脚本，但可以在不指定可执行文件的绝对路径的情况下运行它们，只需将该目录添加到 `$PATH`。

例如，假设你在 home 目录下有一个 `bin` 目录用来放置可执行脚本，将其添加到 `$PATH`：

```bash
$ export PATH="$HOME/bin:$PATH"
```

`export` 命令将修改后的变量导出到 shell 子进程环境中。

现在可以直接键入可执行脚本名称来运行，无需指定文件的完整路径。

但是，该设置是临时的，仅在当前 shell 有效。

要永久设置，需要在 shell 配置文件中定义 `$PATH` 变量。在大多数 Linux 中，在启动新会话时，会从以下文件读取环境变量：

- 全局 shell 配置文件，如 `/etc/environment` 和 `/etc/profile`。如果希望添加到系统用户 `$PATH`，使用该文件。
- 特定用户的 shell 配置文件。例如，在 Bash 中配置文件中 `~/.bashrc`，在其中设置 `$PATH` 变量，在 Zsh 中配置文件位 `~/.zshrc`。

下面在 `~/.bashrc` 文件中设置变量。使用文本编辑器打开该文件：

```bash
$ nano ~/.bashrc
```

然后在其中添加环境变量：

```bash
export PATH="$HOEM/bin:$PATH"
```

保存文件，使用 `source` 命令将新的 `$PATH` 载入当前 shell:

```bash
$ source ~/.bashrc
```

查看是否添加成功：

```bash
$ echo $PATH
```

## 参考

- https://linuxize.com/post/how-to-add-directory-to-path-in-linux/