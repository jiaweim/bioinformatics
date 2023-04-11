# 权限

- [权限](#权限)
  - [简介](#简介)
  - [User, Group, Others](#user-group-others)

***

## 简介

UNIX 系统不仅是多任务处理系统，还是多用户系统。

## User, Group, Others

Linux 对权限设置了用户（User）、组（group）和其它三类。

用 `id` 查看用户身份：

```bash
$ id
uid=1000(mjw) gid=1000(mjw) groups=1000(mjw),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),116(netdev)
```

在创建用户时，会为用户：

- 分配一个用户 ID (uid) 数字，为了便于使用，uid 由被映射为用户名。
- 分配一个组 ID（gid）数字

在 Ubuntu 系统中，编号从 1000 开始。Ubuntu 用户归属多个 group，这与 Ubuntu 的系统设备和服务的权限管理方式有关。

信息存储位置：

- 文件的 owner 信息保存在 `/etc/passwd` 中
- group 信息保存在 `/etc/group` 文件中

在创建用户和 group 时，这两个文件与 `/etc/shadow` 文件一并改动，后者保存了用户的密码信息。

对每个用户，`/etc/passwd` 文件定义了用户名、uid、gid、用户的真实姓名、home 目录以及登录 Shell。

