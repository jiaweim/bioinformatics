# 安装 conda

## Linux

- 下载 Miniconda

使用镜像地址：https://mirrors.bfsu.edu.cn/anaconda/miniconda/

```bash
$ wget https://mirrors.bfsu.edu.cn/anaconda/miniconda/Miniconda3-py39_23.1.0-1-Linux-x86_64.sh
```

- 安装

```bash
$ bash Miniconda3-py39_23.1.0-1-Linux-x86_64.sh
```

按 q 跳出许可证 -> 输入 yes -> 回车

- 启动环境变量

```bash
source ~/.bashrc
```

- 升级 conda

```bash
$ conda update -n base -c defaults conda
```

## 参考

- https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html
- https://zhuanlan.zhihu.com/p/459607806