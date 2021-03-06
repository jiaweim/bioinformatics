# chmod

## 简介

`chmod` (change mode) 用于改变文件或目录权限。默认只有文件的所有者和管理员可以设置文件权限，普通用户只能管理自己文件的权限属性。

设置权限时可以使用数字法，亦可使用字母表达式，对于目录文件建议加入 `-R` 参数进行递归操作，意味着不仅对于目录本身，也对目录内的子文件/目录都进行新权限的设定。

```sh
chmod 参数 文件
```

|选项|说明|
|---|---|
|-c|若该文件权限确实已经更改，才显示其更改动作|
|-f|若该文件权限无法被更改也不显示错误讯息|
|-v|显示权限变更的详细资料|
|-R|对目前目录下的所有文件与子目录进行相同的权限变更(即以递回的方式逐个变更)|

## 示例

