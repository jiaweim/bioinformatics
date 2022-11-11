# GROMACS 安装

- [GROMACS 安装](#gromacs-安装)
  - [简介](#简介)
  - [安装 cmake](#安装-cmake)
    - [更新 CMAKE](#更新-cmake)
  - [安装 FFTW](#安装-fftw)
  - [安装 GROMACS](#安装-gromacs)
  - [安装 Python](#安装-python)
  - [单核版本](#单核版本)
  - [CMAKE 选项](#cmake-选项)
    - [MPI](#mpi)
  - [Linux 上安装步骤](#linux-上安装步骤)
  - [问题集锦](#问题集锦)
    - [CXX not found](#cxx-not-found)
    - [更新 gcc](#更新-gcc)
  - [参考](#参考)

2022-05-23, 15:01
***

## 简介

下面是在 CentOS 系统安装 GROMACS 的过程。

下面安装的是纯 CPU 运算、单精度、能单机并行但不能跨节点并行的版本。

## 安装 cmake

构建 GROMACS 需要 CMake 版本不低于 3.16.3。可以使用 `cmake3 --version` 查看 CMake 版本。

1. 首先，安装 EPEL 源：

```sh
yum install epel-release
```

2. 然后，安装 cmake:

```sh
yum install cmake3
```

遇到提示输入 y.

3. 确认安装成功

使用 `cmake3 --version` 或 `cmake3 /V` 查看 cmake 版本。

```sh
$ cmake3 --version
cmake3 version 3.17.5

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

如果输出 cmake 版本，说明安装成功

### 更新 CMAKE

卸载：

```sh
yum remove cmake3 -y
```

下载最新版：

```sh
wget https://github.com/Kitware/CMake/releases/download/v3.22.4/cmake-3.22.4.tar.gz
```

解压：

```sh
tar xvf cmake-3.22.4.tar.gz
```

转到目录：

```sh
cd cmake-3.22.4/
```

安装：

```sh
./configure
gmake
gmake install
```

查看版本：

```sh
$ cmake --version
cmake version 3.22.4
```

## 安装 FFTW

GROMACS 依赖于快速傅里叶变换库 FFTW（http://www.fftw.org/ ），FFTW 3.3.10 下载地址 http://www.fftw.org/fftw-3.3.10.tar.gz

1. 下载 FFTW

```sh
wget http://www.fftw.org/fftw-3.3.10.tar.gz
```

2. 解压文件

```sh
tar -xzvf fftw-3.3.10.tar.gz
```

3. 转到解压目录

```sh
cd fftw-3.3.10/
```

4. 配置

```sh
./configure --prefix=/sob/fftw3310 --enable-sse2 --enable-avx --enable-float --enable-shared
```

 --enable-avx2

5. 编译

```sh
make -j install
```

编译完毕后，出现 `/sob/fftw3310` 目录。然后就可以把 FFTW 的解压目录和压缩包删除。

## 安装 GROMACS

1. 下载 GROMACS 2022.1

下载地址：
ftp://ftp.gromacs.org/gromacs/gromacs-2022.1.tar.gz

```sh
wget ftp://ftp.gromacs.org/gromacs/gromacs-2022.1.tar.gz
```

2. 解压文件

```sh
tar -xzvf gromacs-2022.1.tar.gz
```

3. 安装

依次运行：

```sh
cd gromacs-2022.1
mkdir build
cd build
export CMAKE_PREFIX_PATH=/sob/fftw3310
cmake3 .. -DCMAKE_INSTALL_PREFIX=/sob/gmx2022.1
make install -j
```

由于 CentOS 默认的 Python3 版本为 3.6.8，而构建 GROMACS 至少需要 3.7.

## 安装 Python

1. 安装依赖项

```sh
sudo yum install gcc openssl-devel bzip2-devel libffi-devel zlib-devel
```

2. 下载 Python

https://www.python.org/ftp/python/3.9.13/Python-3.9.13.tgz

```sh
wget https://www.python.org/ftp/python/3.9.13/Python-3.9.13.tgz
```

3. 解压

```sh
tar -xvf Python-3.9.13.tgz
```

4. 转到 Python-3.9.13 目录，运行

```sh
cd Python-3.9.13/
./configure --enable-optimizations
```

5. 构建 Python

```sh
sudo make altinstall
```

6. 查看 Python 版本

```sh
$ python3.9 --version
Python 3.9.13
```

查看 pip 版本

```sh
$ pip3.9 -V
pip 22.0.4 from /usr/local/lib/python3.9/site-packages/pip (python 3.9)
```

## 单核版本

此处安装 GROMACS 2022.1：

1. 获取最新版本的 C 和 C++ 编译器

```sh
yum install make automake gcc gcc-c++ kernel-devel
```

确认版本：

```sh
$ gcc --version
gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44)
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

$ g++ --version
g++ (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44)
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

2. 检查 CMake 版本，确定大于 3.16.3

```sh
$ cmake3 --version
cmake3 version 3.17.5

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

3. 下载并解压 GROMACS

```sh
wget ftp://ftp.gromacs.org/gromacs/gromacs-2022.1.tar.gz
```

## CMAKE 选项

|选项|说明|
|---|---|
|`-DCMAKE_C_COMPILER=xxx`|使用的 C99 编译器名称，默认为环境变量 `CC`|
|`-DCMAKE_CXX_COMPILER=xxx`|使用的 C++17 编译器名称，默认为 `CXX` 环境变量|
|`-DGMX_MPI=on`|是否支持 MPI|
|`-DGMX_GPU=CUDA`|支持 NVIDIA GPU|
|`-DGMX_GPU=OpenCL`|支持 OpenCL GPU|
|`-DGMX_GPU=SYCL`|支持 SYCL|

### MPI

GROMACS 可以使用其内置的线程 MPI 在单个工作站的多个核上并行运行。不需要任何用户操作就可以启用该功能。

如果需要在多台机器上并行运行，则需要安装 MPI 库。理论上自 2009 年以来发布的 MPI 版本都可以，不过 GROMACS 团队推荐使用最新版的 OpenMPI 或 MPICH。

## Linux 上安装步骤

安装 CMake

```sh
sudo apt install cmake
```

创建 GROMACS 工作路径：

```sh
mkir gmx
cd gmx
```

下载 GROMACS 源码：

```sh
wget ftp://ftp.gromacs.org/gromacs/gromacs-2022.1.tar.gz
```

```sh
tar xfz gromacs-2022.1.tar.gz # 解压
cd gromacs-2022.1/
mkdir build
cd build
cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON # 生成编译文件
make # 编译生成可执行文件
make check # 检查编译文件是否正确
sudo make install # 安装
source /usr/local/gromacs/bin/GMXRC # 让刚刚的安装生效
```

```sh
gmx # 查看是否安装成功
```

## 问题集锦

### CXX not found

没有安装 gcc 或 g++ 编译环境，采用如下命令安装：

```sh
sudo apt-get install build-essential
```

然后使用以下命令验证是否安装成功：

```sh
gcc --version
g++ --verrsion
```

对 RH 体系：

```sh
yum install make automake gcc gcc-c++ kernel-devel
```

### 更新 gcc



## 参考

- http://sobereva.com/457
- https://manual.gromacs.org/documentation/current/install-guide/index.html
