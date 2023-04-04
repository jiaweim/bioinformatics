# uname

## 简介

```bash
$ uname [option]…
```

`uname` 打印系统信息。默认为 `-s` 选项。

指定多个选项或 `-a`，则按以下顺序打印信息：

- kernel-name
- nodename
- kernel-release
- kernel-version
- machine
- processor
- hardware-platform
- operating-system

选项|长选项|说明
`-a`|`--all`|打印以下所有信息
`-i`|`--hardware-platform`|

‘-i’
‘--hardware-platform’
Print the hardware platform name (sometimes called the hardware implementation). Print ‘unknown’ if this information is not available. Note this is non-portable (even across GNU/Linux distributions).

‘-m’
‘--machine’
Print the machine hardware name (sometimes called the hardware class or hardware type).

‘-n’
‘--nodename’
Print the network node hostname.

‘-p’
‘--processor’
Print the processor type (sometimes called the instruction set architecture or ISA). Print ‘unknown’ if this information is not available. Note this is non-portable (even across GNU/Linux distributions).

‘-o’
‘--operating-system’
Print the name of the operating system.

‘-r’
‘--kernel-release’
Print the kernel release.
`-s`|`--kernel-name`|打印内核名称。POSIX 1003.1-2001 称为操作系统实现。有些 OS（如 FreeBSD, HP-UX）kernel 名称与操作系统相同（`o`）
`-v`|`--kernel-version`|内核版本

## 参考

- https://www.gnu.org/software/coreutils/manual/html_node/uname-invocation.html