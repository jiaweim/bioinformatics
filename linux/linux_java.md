# 安装 Java 17

- [安装 Java 17](#安装-java-17)
  - [1. 安装 wget 和 curl](#1-安装-wget-和-curl)
  - [2. 下载 java](#2-下载-java)
  - [3. 安装 Java](#3-安装-java)
  - [4. 设置默认 Java](#4-设置默认-java)
  - [参考](#参考)

## 1. 安装 wget 和 curl

```sh
sudo yum -y install wget curl
```

## 2. 下载 java

```sh
wget https://download.oracle.com/java/17/archive/jdk-17.0.3.1_linux-x64_bin.rpm
```

## 3. 安装 Java

```sh
sudo rpm -ivh jdk-17.0.3.1_linux-x64_bin.rpm
```

Java 默认安装在 `/usr/java/` 目录。可以自定义路径：

```sh
sudo rpm -ivh -prefix=// .rpmfile
```

验证 java 安装：

```sh
$ java -version
java version "17.0.3.1" 2022-04-22 LTS
Java(TM) SE Runtime Environment (build 17.0.3.1+2-LTS-6)
Java HotSpot(TM) 64-Bit Server VM (build 17.0.3.1+2-LTS-6, mixed mode, sharing)
```

## 4. 设置默认 Java

首先，查看已安装的 Java：

```sh
sudo alternatives --config java
```

在输出可以看到所有安装的 Java 版本：

```sh
There are 3 programs which provide 'java'.

  Selection    Command
-----------------------------------------------
   1           java-1.7.0-openjdk.x86_64 (/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.261-2.6.22.2.el7_8.x86_64/jre/bin/java)
   2           java-1.8.0-openjdk.x86_64 (/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.332.b09-1.el7_9.x86_64/jre/bin/java)
*+ 3           /usr/java/jdk-17.0.3.1/bin/java

Enter to keep the current selection[+], or type selection number: 
```

输入对应编码，就可以设置默认 java 版本。

## 参考

- https://techviewleo.com/install-java-openjdk-on-rocky-linux-centos/
