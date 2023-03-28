# echo

- [echo](#echo)
  - [简介](#简介)
  - [命令](#命令)
  - [示例](#示例)
  - [参考](#参考)

***

## 简介

`echo` 是 Linux 最常用的命令之一。传递给 `echo` 的参数被打印到标准输出。

`echo` 一般在 shell 脚本中使用，用来显示消息或输出其它命令的结果。

## 命令

`echo` 是 Bash 等大多数流行 shell 的内置命令，在不过在不同 shell 中的行为稍有不同。

```bash
echo [-neE] [ARGUMENTS]
```

说明：

- `-n` 用于抑制末尾的换行符
- `-e` 表示解析以下反斜杠转移字符
  - `\\` - 显示反斜杠字符
  - `\a` - Alert (BEL)
  - `\b` - 显示退格字符
  - `\c` - 抑制后续输出
  - `\e` - 显示转义字符
  - `\f` - 显示制表符
  - `\n` - 换行
  - `\r` - 回车
  - `\t` - 水平 tab
  - `\v` - 垂直 tab
- `-E` 禁用转义字符解释，默认选项。

注释项：

- 在将参数传递给 `echo` 之前，shell 将替换所有变量、通配符和特殊字符；
- 虽然不是必需的，但是将传递给 `echo` 的参数放在双引号或者单引号中是很好的编程实践；
- 使用单引号时，引号内的每个字符被保留，不会展开变量和命令。

## 示例

- Hello World

```bash
$ echo Hello, World!
Hello, World!
```

- 显示包含双引号的文本

要打印双引号，要么括在单引号中，要么使用反斜杠转义。

```bash
$ echo 'Hello, "Linux"'
Hello, "Linux"
$ echo "Hello, \"Linux\""
Hello, "Linux"
```

- 显示包含特殊字符的信息

使用 `-e` 选项启用转义字符解析。

```bash
$ echo -e "You know nothing, Jon Snow.\n\t- Ygritte"
You know nothing, Jon Snow.
        - Ygritte
```

- 模式匹配字符

`echo` 可以与模式匹配字符一起使用，如通配符。如返回当前目录中所有 txt 文件：

```bash
$ echo The txt files are: *.txt
The txt files are: INSTALL.txt LICENSE.txt README.txt RELEASE_NOTES.txt
```

- 重定向到文件

可以使用 `>` 或 `>>` 运算符将输出重定向到文件。`>` 覆盖目标文件，`>>` 则追加内容。

```bash
echo -e 'The only true wisdom is in knowing you know nothing.\nSocrates' >> /tmp/file.txt
```

file.txt 不存在则新建。

- 显示变量

`echo` 可以显示变量。例如，打印当前用户名：

```bash
$ echo $USER
mjw
```

- 显示某个命令的输出

使用 `$(command)` 表达式将 `command` 的输出包括在 `echo` 参数中。

例如，显示当前日期：

```bash
$ echo "The date is: $(date +%D)"
The date is: 03/28/23
```

- 颜色

使用 ANSI 转义序列更改前景和背景颜色，也可以设置文本属性，如下划线、加粗等。

```bash
$ echo -e "\033[1;37mWHITE"
$ echo -e "\033[0;30mBLACK"
$ echo -e "\033[0;34mBLUE"
$ echo -e "\033[0;32mGREEN"
$ echo -e "\033[0;36mCYAN"
$ echo -e "\033[0;31mRED"
$ echo -e "\033[0;35mPURPLE"
$ echo -e "\033[0;33mYELLOW"
$ echo -e "\033[1;30mGRAY"
```

## 参考

- https://linuxize.com/post/echo-command-in-linux-with-examples/