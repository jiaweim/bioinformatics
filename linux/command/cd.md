# cd

- [cd](#cd)
  - [简介](#简介)
  - [选项](#选项)
  - [示例](#示例)

Last updated: 2023-04-12, 11:10
****

## 简介

```bash
$ cd [-L|[-P [-e]] [-@]] [dir]
```

修改 shell 工作目录。

切换到 `DIR` 目录。`DIR` 默认为 `$HOME` 变量值。另外：

- `~` 表示 home 目录里
- `.` 表示当前目录
- `..` 表示上层目录

`CDPATH` 变量定义 `DIR` 的搜索路径。`CDPATH` 中的备用目录用冒号 `:` 分隔。null 目录等价于当前目录。如果 `DIR` 以 `/` 开头，则不使用 `CDPATH`。

如果找不到 `DIR` 目录，并且设置了 `cdable_vars` shell 选项，则认为 `DIR` 是一个变量名。如果该变量包含值，则将该值作为 `DIR`。

## 选项

| 选项 | 说明 |
|--|--|
| `-L` | 强制解析符号链接：在处理 `..` 后解析 `DIR` 中的符号链接 |
| `-P` | 使用物理目录结构而不使用符号链接：先解析 `DIR` 中的符号链接，再处理 `..` |
| `-e` | 使用 `-P` 选项时无法成功确定当前工作目录，则以非零状态退出 |
| `-@` | 对支持该选项的系统，将具有扩展属性的文档显示为包含该文档属性的目录 |

默认解析符号链接，即 `-L` 为默认行为。

退出状态：

切换到 `DIR` 返回 0。

## 示例

- 切换到 home 目录

```bash
$ cd ~
```

或者：

```bash
$ cd
```

- 切换到指定用户的 home 目录

```bash
$ cd ~user_name
```

- 绝对路径（从根目录开始）

```bash
$ cd /usr/bin/
$ pwd
/usr/bin
```

- 相对路径（从当前目录开始）

假设当前目录为 `/usr/bin`，到 `/usr` 有两种方式。

1. 绝对路径

```bash
mjw@happy:/usr/bin$ cd /usr
mjw@happy:/usr$ pwd
/usr
```

2. 相对路径

```bash
mjw@happy:/usr/bin$ cd ..
mjw@happy:/usr$ pwd
/usr
```

切换回 `/usr/bin` 目录：

1. 绝对路径

```bash
mjw@happy:/usr$ cd /usr/bin
mjw@happy:/usr/bin$ pwd
/usr/bin
```

2. 相对路径

```bash
mjw@happy:/usr$ cd ./bin
mjw@happy:/usr/bin$ pwd
/usr/bin
```

另外，`./` 大多时候可以忽略，所以相对路径方式可以写为：

```bash
mjw@happy:/usr$ cd bin
mjw@happy:/usr/bin$ pwd
/usr/bin
```
