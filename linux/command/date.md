# date

- [date](#date)
  - [简介](#简介)
  - [示例](#示例)

2022-06-06, 10:37
****

## 简介

`date` 命令用于显示或设置系统日期与时间信息。运维人员可以根据想要的格式来输出系统时间信息，时间格式 `MMDDhhmm[CC][YY][.ss]`，其中 MM 为月份，DD 为日，hh 为小时，mm 为分钟，CC 为年份前两位数字，YY 为年份后两位数字，ss 为秒数。

语法：

```sh
date [选项] [+输出形式]
```

|参数|说明|
|---|---|
|-d datestr|显示 datestr 中所设定的时间 (非系统时间)|
|-s datestr|将系统时间设为 datestr 中所设定的时间|
|-u|显示目前的格林威治时间|
|--help|显示帮助信息|
|--version|显示版本编号|

## 示例

- 以默认格式输出系统当前日期和时间

```sh
[root@localhost ~]# date
Sun Jun  5 22:36:27 EDT 2022
```

- 按照 “年-月-日” 的格式输出系统日期

```sh
[root@localhost ~]# date "+%Y-%m-%d"
2022-06-05
```

- 按照 “小时:分钟:秒” 的格式输出系统时间

```sh
[root@localhost ~]# date "+%H:%M:%S"
22:40:06
```

- 设置当前系统的日期和时间

```sh
[root@localhost ~]# date -s "20220606 10:41:00"
Mon Jun  6 10:41:00 EDT 2022
[root@localhost ~]# date
Mon Jun  6 10:41:09 EDT 2022
```
