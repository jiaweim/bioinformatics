# 软件包管理

- [软件包管理](#软件包管理)
  - [打包系统](#打包系统)
  - [包文件](#包文件)
  - [安装](#安装)
    - [deb](#deb)
  - [安装软件](#安装软件)
    - [软件包文件](#软件包文件)
  - [卸载软件](#卸载软件)
  - [显示所安装软件的信息](#显示所安装软件的信息)

2022-05-23, 14:53
***

## 打包系统

不同的 Linux 发行版使用不同的打包系统，大多数发行版分属于两大包管理技术阵营：Debian 的 ".deb" 和红帽的 ".rpm"。

|包管理系统|发行版|
|----|---|
|Debian 风格（.deb）|Debian, Ubuntu, Xandros, Linspire|
|Red Hat 风格（.rpm）|Fedora, CentOS, Red Hat Enterprise Linux, OpenSUSE, Mandriva, PCLinuxOS|

Linux 系统中几乎所有的软件都可以在互联网上找到。其中大多数软件由
发行商以包文件的形式提供，剩下的则以源码形式存在，可以手动安装。

## 包文件

包文件是包管理系统中软件的基本单元。包文件是是构成软件包的压缩文件集合。

## 安装

### deb


## 安装软件

### 软件包文件

如果已经下载了一个软件包，可以使用底层工具直接安装：

|风格|命令|
|---|---|
|Debian|`dpkg --install package_file`|
|Red Hat|`rpm -i package_file`|

例如：如果已经从一个并非资源库的网站下载了软件包文件 emacs-22.1-7.fc7-i386.rpm，则可以通过这种方法来安装它：

```sh
rpm -i emacs-22.1-7.fc7-i386.rpm
```

> 因为这项技术使用底层的rpm 程序来执行安装任务，所以没有运行依赖解析。如果 rpm 程序发现缺少了一个依赖，则会报错并退出。

## 卸载软件

可以使用上层或者底层工具来卸载软件。下面是可用的上层工具：

|风格|命令|
|---|---|
|Debian|`apt-get remove package_name`|
|Red Hat|`yum erase package_name`|

- 例如：从Debian 风格的系统中卸载emacs 软件包：

```sh
apt-get remove emacs
```

## 显示所安装软件的信息

已知软件名称，可以使用如下命令查看软件的说明信息：

|风格|命令|
|---|---|
|Debian|`apt-cache show package_name`|
|Red Hat|`yum info package_name`|
