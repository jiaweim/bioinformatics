# df

- [df](#df)
  - [简介](#简介)
  - [实例](#实例)

2022-06-06, 10:57
****

## 简介

`df` 命令（Disk Free）用于显示系统上磁盘空间的使用情况。

`df`命令显示的磁盘使用量情况含可用、已有及使用率等信息，默认单位为 Kb，建议使用 `-h` 参数进行单位换算。

```sh
df [参数] [对象磁盘/分区]
```

|参数|说明|
|---|---|
|`-a`|显示所有系统文件|
|`-B <块大小>`|指定显示时的块大小|
|`-h`|以容易阅读的方式显示|
|`-H`|以1000字节为换算单位来显示|
|`-i`|显示索引字节信息|
|`-k`|指定块大小为1KB|
|`-l`|只显示本地文件系统|
|`-t <文件系统类型>`|只显示指定类型的文件系统|
|`-T`|输出时显示文件系统类型|
|`-- -sync`|在取得磁盘使用信息前，先执行sync命令|

## 实例

- 带单位显示系统全部磁盘的使用情况

```sh
[root@localhost ~]# df -h
Filesystem               Size  Used Avail Use% Mounted on
devtmpfs                 252G     0  252G   0% /dev
tmpfs                    252G     0  252G   0% /dev/shm
tmpfs                    252G   53M  252G   1% /run
tmpfs                    252G     0  252G   0% /sys/fs/cgroup
/dev/mapper/centos-root   50G   12G   38G  24% /
/dev/sda2               1014M  245M  770M  25% /boot
/dev/sda1                200M   12M  189M   6% /boot/efi
/dev/mapper/centos-home   75T  3.5T   72T   5% /home
tmpfs                     51G  4.0K   51G   1% /run/user/42
tmpfs                     51G   36K   51G   1% /run/user/1001
tmpfs                     51G     0   51G   0% /run/user/1000
tmpfs                     51G     0   51G   0% /run/user/0
tmpfs                     51G     0   51G   0% /run/user/1006
tmpfs                     51G     0   51G   0% /run/user/1005
```

- 显示指定分区的磁盘使用情况

```sh
[root@localhost ~]# df -h /boot
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda2      1014M  245M  770M  25% /boot
```

- 显示文件格式为 xfs 的磁盘分区使用情况

```sh
[root@localhost ~]# df -h -t xfs
Filesystem               Size  Used Avail Use% Mounted on
/dev/mapper/centos-root   50G   12G   38G  24% /
/dev/sda2               1014M  245M  770M  25% /boot
/dev/mapper/centos-home   75T  3.5T   72T   5% /home
```
