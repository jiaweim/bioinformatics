# fetch_path

- [fetch_path](#fetch_path)
  - [简介](#简介)
  - [设置方法](#设置方法)
  - [参考](#参考)

2022-06-01, 09:42
****

## 简介

PyMOL 使用 `fetch` 命令从网上下载结构前，会先查询 `fetch_path` 目录，如果该目录有该结构，就不继续下载；同理，`fetch` 下载的结构也会保存在该目录。`fetch_path` 用于设置默认路径。

> PyMOL 只搜索以小写的 pdb code 开始的文件。

## 设置方法

在 Linux 或 MacOS :

```sh
set fetch_path, /spc/pdb
```

在 Windows:

```sh
set fetch_path, D:\mypdbs
```

使用 API：

```py
cmd.set('fetch_path', cmd.exp_path('~/fetch_path'), quiet=0)
```

将设置保存在 `pymolrc` 配置文件中，可以持久化设置。

## 参考

- https://pymolwiki.org/index.php/Fetch_Path
