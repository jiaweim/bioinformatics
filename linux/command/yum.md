# yum

- [yum](#yum)
  - [语法](#语法)
  - [简介](#简介)
  - [command](#command)
    - [install](#install)
  - [参考](#参考)

2022-05-17, 13:01
***

## 语法

```unix
yum [options] [command] [package ...]
```

## 简介

yum (Yellowdog Updater Modified) 是一个基于 rpm 的交互式软件包管理器它可以：

- 自动执行系统更新
- 基于 "repository" 元数据进行依赖分析和过时（obsolete）处理
- 软件的安装、卸载和更新
- 软件搜索

yum 与其它高级包管理器类似，如 apt-get、smart 等，是 CentOS 的默认软件管理器。

## command

|命令|功能|
|---|---|
|install pkg1 [pkg2] [...]|安装软件|
|update [pkg1] [pkg2] [...]| 更新软件|
|yum remove softwarename|卸载软件|
|yum list softwarename|查看软件源中是否有此软件|
|yum list all|列出所有软件名称|
|yum list installed|列出已经安装的软件名称|
|yum list available|列出可以用yum安装的软件|
|yum clean all|清空 yum 缓存|
|yum search softwareinfo|根据软件信息搜索软件名字（如，使用search web搜索web浏览器）|
|yum whatprovides filename|在yum源中查找包含filename文件的软件包（如，whatprovides rm搜索汉含rm的软件，命令实质上是文件）|
|yum update|更新软件，会存在未知问题，一般不对服务器升降级|
|yum history|查看系统软件改变历史|
|yum reinstall softwarename|重新安装|
|yum info softwarename|查看软件信息|
|yum groups list|查看软件组信息|
|yum groups info softwarename|查看软件组内包含的软件|
|yum groups install softwarename|安装组件|
|yum groups remove softwarename|卸载组件|

### install

```sh
yum install pkg1 [pkg2] [...]
```

安装软件（默认安装最新版本）。并确保所有依赖关系满足。

- 如果没有对应名称的软件包，则假设该名称为 shell glob，并安装任何名称匹配的软件包；
- 如果名称以 @ 开头，则作为 `groupinstall` 名称处理；
- 如果名称为文件，则以 localinstall 处理；
- 如果



## 参考

- https://www.tutorialspoint.com/unix_commands/yum.htm
