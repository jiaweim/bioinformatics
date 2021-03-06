# cal

- [cal](#cal)
  - [简介](#简介)
  - [实例](#实例)

2022-06-06, 10:52
****

## 简介

`cal` 命令 (Calendar) 用来显示当前日历，或者指定日期的公历（公历是现在国际通用的历法，又称格列历，通称阳历）。如只有一个参数，则表示年份(1-9999)，如有两个参数，则表示月份和年份 。

语法：

```sh
cal [参数] [月份] [年份]
```

|参数|说明|
|---|---|
|-l|单月分输出日历|
|-3|显示最近三个月的日历|
|-s|将星期天作为月的第一天|
|-m|将星期一作为月的第一天|
|-j|显示在当年中的第几天（儒略日）|
|-y|显示当年的日历|

## 实例

- 显示当前月份的日历

```sh
[root@localhost ~]# cal
      June 2022     
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
```

- 显示最近三个月的日历（上个月、当前月、下个月）

```sh
[root@localhost ~]# cal -3
      May 2022              June 2022             July 2022     
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7            1  2  3  4                  1  2
 8  9 10 11 12 13 14   5  6  7  8  9 10 11   3  4  5  6  7  8  9
15 16 17 18 19 20 21  12 13 14 15 16 17 18  10 11 12 13 14 15 16
22 23 24 25 26 27 28  19 20 21 22 23 24 25  17 18 19 20 21 22 23
29 30 31              26 27 28 29 30        24 25 26 27 28 29 30
                                            31                  
```

- 显示指定年月的日历，例如，显示 2022 年 2 月的日历

```sh
[root@localhost ~]# cal 2 2020
    February 2020   
Su Mo Tu We Th Fr Sa
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
```
