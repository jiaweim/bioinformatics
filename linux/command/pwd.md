# pwd

2022-06-06, 10:44
****

## 简介

```bash
pwd [option]…
```

`pwd` (Print Working Directory)用于显示当前工作目录的路径，即显示所在位置的绝对路径。



| 短参数 | 长参数 | 说明 |
|--|--|--|
| `-L` | `--logical` | 如果环境变量 `PWD` 提供了当前目录的绝对名称，没有 `.` 和 `..` 部分，但可能带有符号链接，则输出这些内容。否则回退到默认的 `-P` |
| `-P` | `--physical` | 打印当前目录的完全解析名称。即输出名称的所有部分都是实际目录名称，没有符号链接 |

同时提供 `-L` 和 `-P` 时，最后一个优先。默认为 `-P`。

由于 shell 别名和内置的 `pwd` 函数，以交互方式或脚本中使用的 `pwd` 可能与此描述的行为不同。通过 `env pwd` 可以避免 shell 干扰。

返回 0 表示成功，非 0 表示失败。

## 实例

```sh
$ pwd
/usr
```

## 参考

- https://www.gnu.org/software/coreutils/manual/html_node/pwd-invocation.html