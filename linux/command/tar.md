# tar

- [tar](#tar)
  - [简介](#简介)
  - [示例](#示例)
  - [参考](#参考)

@author Jiawei Mao
***

## 简介

`tar` 命令用于压缩和解压缩文件，能够生成 Linux系统中常见的.tar、.tar.gz、.tar.bz2等格式的压缩包文件。对于 RHEL7、CentOS7 版本以后的系统，解压时可以不加压缩格式参数（如 `z` 或 `j`），系统能自动进行分析并解压。

把要传输的文件先进行压缩再进行传输，能够很好的提高工作效率，方便分享。

```bash
tar 选项 文件或目录
```



## 示例

- 解压 `foo.tar.gz` 文件

```sh
tar -xzf foo.tar.gz
```

## 参考

- https://www.tutorialspoint.com/unix_commands/tar.htm
