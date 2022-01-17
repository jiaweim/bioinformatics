# 用户目录

- [用户目录](#用户目录)
  - [pwd](#pwd)
  - [ls](#ls)
  - [cd](#cd)

## pwd

```sh
pwd
```

打印当前工作目录。

## ls

```sh
ls [pattern]
dir [pattern]
```

`ls` 列出当前工作目录的内容。

- **例1**，列出当前目录文件

```sh
ls
```

- 例2，列出当前目录以 `pml` 结尾的目录

```sh
ls *.pml
```

## cd

```sh
cd DIR_NAME
```

更改 PyMOL 的当前工作目录。`DIR_NAME` 为目录。

**例1**，转到主目录

```sh
cd ~
```

- **例2**，转到 `/tmp` 目录

```sh
cd /tmp
```
