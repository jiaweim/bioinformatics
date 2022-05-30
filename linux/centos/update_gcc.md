# CentOS 升级 gcc 版本

## 查看当前 gcc 版本

```sh
gcc --version
```

升级到gcc 7.3
yum -y install centos-release-scl 
yum -y install devtoolset-7-gcc devtoolset-7-gcc-c++ devtoolset-7-binutils 
scl enable devtoolset-7 bash

需要注意的是scl命令启用只是临时的，退出shell或重启就会恢复原系统gcc版本。
如果要长期使用gcc 7.3的话：

echo "source /opt/rh/devtoolset-7/enable" >>/etc/profile

升级到gcc 8.3
yum -y install centos-release-scl 
yum -y install devtoolset-8-gcc devtoolset-8-gcc-c++ devtoolset-8-binutils 
scl enable devtoolset-7 bash

需要注意的是scl命令启用只是临时的，退出shell或重启就会恢复原系统gcc版本。
如果要长期使用gcc 8.3的话：

echo "source /opt/rh/devtoolset-8/enable" >>/etc/profile

升级到gcc 9.3
yum -y install centos-release-scl 
yum -y install devtoolset-9-gcc devtoolset-9-gcc-c++ devtoolset-9-binutils 
scl enable devtoolset-9 bash

需要注意的是scl命令启用只是临时的，退出shell或重启就会恢复原系统gcc版本。
如果要长期使用gcc 9.3的话：

echo "source /opt/rh/devtoolset-9/enable" >>/etc/profile

## 参考

- https://blog.csdn.net/qq_39715000/article/details/120703444
