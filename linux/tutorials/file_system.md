# 文件系统

- [文件系统](#文件系统)
  - [文件系统树](#文件系统树)
  - [当前工作目录](#当前工作目录)
  - [列出目录内容](#列出目录内容)
  - [更改当前工作目录](#更改当前工作目录)
  - [绝对路径](#绝对路径)
  - [相对路径](#相对路径)
  - [注意事项](#注意事项)

2022-06-06, 12:13
****

## 文件系统树

Linux 以分层目录结构组织所有文件。

## 当前工作目录

当前所在目录称为当前工作目录，使用 [pwd](../command/pwd.md) (print working directory) 显示当前工作目录：

```sh
[root@localhost ~]# pwd
/root
```

## 列出目录内容

使用 [ls](../command/ls.md) 命令列出目录包含的文件及子目录：

```sh
[root@localhost ~]# ls
anaconda-ks.cfg  initial-setup-ks.cfg  local
```

## 更改当前工作目录

使用 [cd](../command/cd.md) 命令更改工作目录。

## 绝对路径

绝对路径从根目录开始。例如，大多数系统程序都安装在 `/usr/bin` 目录，以 `/` 开始，表明为根目录。

## 相对路径

相对路径从工作目录开始：

- `.` 指工作目录
- `..` 指工作目录的父目录

例如，我们先把工作目录切换到 `/usr/bin`：

```sh
[root@localhost ~]# cd /usr/bin
[root@localhost bin]# pwd
/usr/bin
```

然后，把工作目录转到 `/usr/bin` 的父目录 `/usr`。有两种实现方法，使用绝对路径：

```sh
[root@localhost bin]# cd /usr
[root@localhost usr]# pwd
/usr
```

或使用相对路径：

```sh
[root@localhost bin]# pwd
/usr/bin
[root@localhost bin]# cd ..
[root@localhost usr]# pwd
/usr
```

## 注意事项

1. 以 `.` 字符开头的文件名是隐藏文件。用 `ls` 命令不能列出它们，不过用 `ls -a` 就可以。
2. 文件名和命令名大小写铭感。
3. Linux 没有文件扩展名的概念。
4. 虽然 Linux 支持长文件名，可以包含空格和标点符号，不过标点符号仅限于 `.`, `-` 和下划线。且，不过在文件名中使用空格。
