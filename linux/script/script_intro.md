# Shell 脚本

## 简介

Shell 脚本就是包含一系列命令的文件。Shell 读取该文件并执行其中的命令。

Shell 的独特之处在于它既是系统的命令行接口，又是脚本语言解释器。

## 创建 Shell 脚本

创建并执行脚本需要三步：

1. 编写脚本。Shell 脚本是普通的文本文件，所以，需要文本编辑器来编写脚本。Vim, gedit, Kate 等都是不错的文本编辑器。
2. 将脚本设置为可执行。系统不会将任何文本文件视为可执行文件，所以需要手动设置脚本的可执行权限。
3. 把脚本放在 Shell 能够找到的地方。如果没有明确额指定路径，Shell 会自动搜索某些目录，在其中查找可额执行文件。

### 脚本文件格式

创建一个简单的 Hello World 脚本。输入：

```bash
#!/bin/bash

# 这是第一个脚本

echo 'Hello World!'
```

`#!` 用于告知内核用来个解释器执行接下来的脚本。

### 可执行权限

```bash
mjw@happy:~/scripts$ ls -l
total 4
-rw-r--r-- 1 mjw mjw 59 Apr 17 14:37 hello_world.sh
mjw@happy:~/scripts$ chmod 755 hello_world.sh
mjw@happy:~/scripts$ ls -l
total 4
-rwxr-xr-x 1 mjw mjw 59 Apr 17 14:37 hello_world.sh
```
 
 脚本有两个常见的权限设置：755 和 700。755 赋予所有用户可执行权限，700 仅赋予 owner 可执行权限。

 ### 执行脚本

 要执行脚本，必须在前面指定路径：

 ```bash
 mjw@happy:~/scripts$ ./hello_world.sh
Hello World!
 ```

直接使用 `hello_world.sh` 不行：

```bash
mjw@happy:~/scripts$ hello_world.sh
hello_world.sh: command not found
```

这与环境变量 `PATH` 有关，`$PATH` 并不包含当前 pwd，所以报错。

