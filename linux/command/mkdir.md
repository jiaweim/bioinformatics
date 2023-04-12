# mkdir

- [mkdir](#mkdir)
  - [简介](#简介)
  - [示例](#示例)

2022-06-08, 14:21
****

## 简介

`mkdir` (make directories ) 用来创建目录。

- 若要创建的目录已存在，则会提示已存在而停止创建，不覆盖已有文件。
- 目录不存在，但具有嵌套的依赖关系，例如 a/b/c/d/e/f，要想一次性创建则需要加入 `-p` 参数，进行递归操作。

```sh
mkdir [参数] 目录...
```

|参数|说明|
|---|---|
|`-p`|递归创建多级目录|
|`-m`|建立目录的同时设置目录的权限|
|-z|设置安全上下文|
|-v|显示目录的创建过程|

## 示例

- 在当前工作目录，创建 `dir1` 目录

```bash
$ mkdir dir1
```

- 创建目录 `dir2`，并设置权限为 700

```sh
$ mkdir -m 700 dir2
$ ls -l
total 0
drwxr-xr-x. 2 root root 6 Jun  8 10:07 dir1
drwx------. 2 root root 6 Jun  8 10:10 dir2
```

- 一次创建多个目录

```sh
$ mkdir dir3 dir4 dir5
$ ls
dir1  dir2  dir3  dir4  dir5
```

- 创建嵌套目录

```sh
$ mkdir -p dir6/dir5/dir4
```
