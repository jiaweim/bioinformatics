# NetMHCpan

## 安装

1. 解压文件

```sh
tar -xzvf netMHCpan-4.1b.Linux.tar.gz
```

2. 下载文件

[data.tar.gz](https://services.healthtech.dtu.dk/services/NetMHCpan-4.1/data.tar.gz)

放到 netMHCpan-4.1 文件夹，并解压

```sh
tar -xvf data.tar.gz
```

这样就生成一个 data 目录，解压后可以删除 data.tar.gz 文件。

3. 编辑 'netMHCpan' 脚本

a. 在文件顶部找到 "GENERAL SETTINGS: CUSTOMIZE TO YOUR SITE"，将 'NMHOME' 变量设置为 'netMHCpan-4.1' 目录在系统中的完整路径。

b. 将 TMPDIR 设置为临时目录的完整路径，必须有写入权限。

可以在 netMHCpan-4.1 目录创建 tmp 目录，然后将临时目录设置为 $NMHOME/tmp

4. 在 'netMHCpan-4.1/test' 目录测试软件

```sh
> ../netMHCpan -p test.pep > test.pep.myout
> ../netMHCpan test.fsa > test.fsa.myout
> ../netMHCpan -hlaseq B0702.fsa -p test.pep > test.pep_userMHC.myout
> ../netMHCpan -p test.pep -BA > test.pep_BA.out
> ../netMHCpan -p test.pep -BA -xls -a HLA-A01:01,HLA-A02:01 -xlsfile my_NetMHCpan_out.xls
```

## 使用

命令：

```sh
netMHCpan 
```

|参数|默认值|说明|
|---|---|---|
|`-p`|1|使用肽段输入|
|`-v`|0|verbose|
|`-BA`|同时预测 binding affinity|
|`-xls`|1|将结果保存到为 xls 格式|
|`-xlsfile filename`|输出的 xls 文件名|
|`-a line`|HLA-A02:01|MHC表位|
|`-l string`|8,9,10,11|肽段长度|
|`-rth float`|0.500000|Rank Threshold for high binding peptides|
|`-rlt float`|2.000000|Rank Threshold for low binding peptides|
|`-t float`|-99.9|Threshold for output (%rank) [<0 print all]|
|`-hlaseq filename`||File with full length MHC sequences|
|`-f filename`|0| File name with input|
|`-inptype int`|0|Input type [0] FASTA [1] Peptide|
|`-s`|0|Sort output on descending affinity|

- 例 1，使用肽段列表 test.pep，结果输出到 test.pep.myout

```sh
netMHCpan -p test.pep > test.pep.myout
```

- 例 2，

```sh
netMHCpan test.fsa > test.fsa.myout
```

```sh
netMHCpan -hlaseq B0702.fsa -p test.pep > test.pep_userMHC.myout
```

```sh
netMHCpan -p test.pep -BA > test.pep_BA.out
```

- 例 3

```sh
netMHCpan -p test.pep -BA -xls -a HLA-A01:01,HLA-A02:01 -xlsfile my_NetMHCpan_out.xls
```

- 例 4

预测 FASTA 文件所有蛋白，肽段长度为 8-14，所有猪表位，输出 xls 格式。

```sh
netMHCpan a.fasta -a SLA-1-CHANGDA,SLA-1-HB01,SLA-1-HB02,SLA-1-HB03,SLA-1-HB04,SLA-1-LWH,SLA-1-TPK,SLA-1-YC,SLA-1-YDL01,SLA-1-YTH,SLA-1:0101,SLA-1:0201,SLA-1:0202,SLA-1:0401,SLA-1:0501,SLA-1:0601,SLA-1:0701,SLA-1:0702,SLA-1:0801,SLA-1:1101,SLA-1:1201,SLA-1:1301,SLA-1:es11,SLA-2-YDL02,SLA-2:0101,SLA-2:0102,SLA-2:0201,SLA-2:0202,SLA-2:0301,SLA-2:0302,SLA-2:0401,SLA-2:0402,SLA-2:0501,SLA-2:0502,SLA-2:0601,SLA-2:0701,SLA-2:1001,SLA-2:1002,SLA-2:1101,SLA-2:1201,SLA-2:CDY.AA,SLA-2:HB01,SLA-2:LWH.AA,SLA-2:TPK.AA,SLA-2:YC.AA,SLA-2:YDL.AA,SLA-2:YDY.AA,SLA-2:YTH.AA,SLA-2:es22,SLA-3-CDY,SLA-3-HB01,SLA-3-LWH,SLA-3-TPK,SLA-3-YC,SLA-3-YDL,SLA-3-YDY01,SLA-3-YDY02,SLA-3-YTH,SLA-3:0101,SLA-3:0301,SLA-3:0302,SLA-3:0303,SLA-3:0304,SLA-3:0401,SLA-3:0402,SLA-3:0501,SLA-3:0502,SLA-3:0503,SLA-3:0601,SLA-3:0602,SLA-3:0701,SLA-6:0101,SLA-6:0102,SLA-6:0103,SLA-6:0104,SLA-6:0105 -l 8,9,10,11,12,13,14 -xls -xlsfile a.xls
```