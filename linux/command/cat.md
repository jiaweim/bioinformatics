# cat

- [cat](#cat)
  - [简介](#简介)
  - [选项](#选项)
  - [示例](#示例)
  - [参考](#参考)

Last updated: 2023-04-04, 19:04
****

## 简介

```bash
cat [option] [file]…
```

`cat` 将每个文件和标准输入（`-` 表示标准输入）复制到标准输出。

## 选项

| 短选项 | 长选项 | 说明 |
|--|--|--|
| `-A` | `--show-all` | 等价于 `-vET |
| `-b` | `--number-nonblank` | 对非空行从 1 开始编号 |
| `-e` |  | 等价于 `-vE` |
| `-E` | `--show-ends` | 每行末尾显示 `$`。`\r\n` 组合显示为 `^M$` |
| `-n` | `--number` | 对所有输出行编号，从 1 开始。设置 `-b` 时忽略该选项 |
| `-s` | `--squeeze-blank` | 对连续空行，只显示一个空行 |
| `-t` |  | 等价于 `-vT` |
| `-T` | `--show-tabs` | 将 TAB 字符显示为 `^I` |
| `-u` |  | 忽略，用于 POSIX 兼容 |
| `-v` | `--show-nonprinting` | 使用 `^` 显示除 LFD 和 TAB 之外的控制字符，以及高位设置为 `M-` 的字符前面 |

说明：

- 在 MS-DOS 这类区分文本和二进制文档的系统上，`cat` 通常以二进制模式读写；
- 使用 `-bensAE` 选项之一时，`cat` 以文本模式读写；
- 标准输入/输出为 terminal 时，`cat` 以文本模式读写。

退出状态为 `0` 表示成功，否则为失败。

## 示例

- 将标准输入复制到标准输出

```bash
$ cat
```



## 参考

- https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html