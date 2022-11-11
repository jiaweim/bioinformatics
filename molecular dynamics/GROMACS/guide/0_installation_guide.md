# GROMACS 安装

- [GROMACS 安装](#gromacs-安装)
  - [构建 GROMACS 简介](#构建-gromacs-简介)
    - [快速安装](#快速安装)
  - [配置](#配置)
    - [平台](#平台)
  - [参考](#参考)

***

> 以下安装 GROMACS 2022.3

## 构建 GROMACS 简介

### 快速安装

1. 获得最新版本的 C 和 C++ 编译器
2. 检查 CMake 版本，确保不低于 3.16.3
3. 下载并解压最新版本的 GROMACS tarball
4. 创建一个单独的构建目录，并切换到该目录
5. 以 source 目录为参数运行 `cmake`
6. 运行 `make`, `make check` 和 `make install`
7. Source `GMXRC` 以访问 GROMACS

以下是一系列要运行的命令：

```powershell
tar xfz gromacs-2022.3.tar.gz
cd gromacs-2022.3
mkdir build
cd build
cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON
make
make check
sudo make install
source /usr/local/gromacs/bin/GMXRC
```

## 配置

### 平台



## 参考

- https://manual.gromacs.org/current/install-guide/index.html
