# 命令行使用

## 简介

对大多数桌面用户，建议再 GUI 模式下使用 FragPipe（https://fragpipe.nesvilab.org/docs/tutorial_fragpipe.html）。用户也可以使用 X forward 在远程服务器上使用（https://fragpipe.nesvilab.org/docs/tutorial_setup_x_forwarding.html）。

使用 `fragpipe` (Linux) 

## Linux server

服务上需要有和 X window 相关的包，不同的 Linux 发行版安装方法不同。下面是 Ubuntu 上的安装方式：

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install xorg openbox
```



## 参考

- https://fragpipe.nesvilab.org/docs/tutorial_setup_x_forwarding.html
