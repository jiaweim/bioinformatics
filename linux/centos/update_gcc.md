# CentOS 升级 gcc 版本

- [CentOS 升级 gcc 版本](#centos-升级-gcc-版本)
  - [简介](#简介)
  - [查看当前 gcc 版本](#查看当前-gcc-版本)
  - [升级到 gcc 6.3](#升级到-gcc-63)
  - [升级到 gcc 7.3](#升级到-gcc-73)
  - [升级到 gcc 8.3](#升级到-gcc-83)
  - [升级到gcc 9.3](#升级到gcc-93)
  - [重装](#重装)
  - [参考](#参考)

Last updated: 2022-06-15, 10:56
@author Jiawei Mao
***

## 简介

CentOS 自带的编译器版本较老，许多较新的软件不支持，因此有更新编译器的需求。

## 查看当前 gcc 版本

```sh
gcc --version
```

## 升级到 gcc 6.3

确定是否安装 centos-release-scl:

```sh
[root@localhost tools]# rpm -q centos-release-scl
centos-release-scl-2-3.el7.centos.noarch
```

如果没有安装，则安装：

```sh
yum -y install centos-release-scl
```

然后安装 gcc:

```sh
yum -y install devtoolset-6-gcc devtoolset-6-gcc-c++ devtoolset-6-binutils 
```

启用：

```sh
scl enable devtoolset-6 bash
```

需要注意的是scl命令启用只是临时的，退出shell或重启就会恢复原系统gcc版本。

如果要长期使用gcc 6.3的话：

```sh
echo "source /opt/rh/devtoolset-6/enable" >>/etc/profile
```

这样退出 shell 重新打开就是新版 gcc 了。

## 升级到 gcc 7.3

```sh
yum -y install centos-release-scl 
yum -y install devtoolset-7-gcc devtoolset-7-gcc-c++ devtoolset-7-binutils 
scl enable devtoolset-7 bash
```

需要注意的是scl命令启用只是临时的，退出shell或重启就会恢复原系统gcc版本。

如果要长期使用gcc 7.3的话：

```sh
echo "source /opt/rh/devtoolset-7/enable" >>/etc/profile
```

## 升级到 gcc 8.3

```sh
yum -y install centos-release-scl 
yum -y install devtoolset-8-gcc devtoolset-8-gcc-c++ devtoolset-8-binutils 
scl enable devtoolset-7 bash
```

需要注意的是scl命令启用只是临时的，退出shell或重启就会恢复原系统gcc版本。

如果要长期使用gcc 8.3的话：

```sh
echo "source /opt/rh/devtoolset-8/enable" >>/etc/profile
```

## 升级到gcc 9.3

yum -y install centos-release-scl 
yum -y install devtoolset-9-gcc devtoolset-9-gcc-c++ devtoolset-9-binutils 
scl enable devtoolset-9 bash

需要注意的是scl命令启用只是临时的，退出shell或重启就会恢复原系统gcc版本。
如果要长期使用gcc 9.3的话：

echo "source /opt/rh/devtoolset-9/enable" >>/etc/profile

## 重装

先卸载：

```sh
yum -y erase devtoolset-6-gcc devtoolset-6-gcc-c++ devtoolset-6-binutils 
```

然后安装上面的操作重新安装。

## 参考

- https://blog.csdn.net/qq_39715000/article/details/120703444
