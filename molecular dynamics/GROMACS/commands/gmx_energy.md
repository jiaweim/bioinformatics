# gmx energy

- [gmx energy](#gmx-energy)
  - [简介](#简介)
  - [参考](#参考)

2022-05-30, 13:18
***

```sh
gmx energy [-f [<.edr>]] [-f2 [<.edr>]] [-s [<.tpr>]] [-o [<.xvg>]]
           [-viol [<.xvg>]] [-pairs [<.xvg>]] [-corr [<.xvg>]]
           [-vis [<.xvg>]] [-evisco [<.xvg>]] [-eviscoi [<.xvg>]]
           [-ravg [<.xvg>]] [-odh [<.xvg>]] [-b <time>] [-e <time>]
           [-[no]w] [-xvg <enum>] [-[no]fee] [-fetemp <real>]
           [-zero <real>] [-[no]sum] [-[no]dp] [-nbmin <int>]
           [-nbmax <int>] [-[no]mutot] [-[no]aver] [-nmol <int>]
           [-[no]fluct_props] [-[no]driftcorr] [-[no]fluc]
           [-[no]orinst] [-[no]ovec] [-acflen <int>] [-[no]normalize]
           [-P <enum>] [-fitfn <enum>] [-beginfit <real>]
           [-endfit <real>]
```

## 简介

`gmx energy` 从能量文件中提取能量组分。程序会以交互方式提示用户选择所需的能量项。

程序会使用全精度计算模拟中能量的平均值、RMSD和漂移(参见手册)。漂移（drift）是通过使用最小二乘法将数据拟合为直线来计算的。报告的总漂移是拟合直线第一个点和最后一个点的差值. 平均值的误差估计是基于5个块的块平均得到的,
计算时使用了全精度的平均值. 利用‐nbmin 和‐nbmax 选项, 可以使用多个块长度进行误差估计. 注意, 在大多数情
况下, 能量文件包含了对所有MD步骤的平均, 或进行平均的点比能量文件中的帧数多很多. 这使得gmx energy 的统
计输出比.xvg 文件中的数据更准确. 当能量文件中不存在精确的平均值时, 上述统计数据只是简单地对每帧能量数
据的平均.
涨落项给出了围绕最小二乘拟合线的RMSD.

如果选择了正确的能量项, 并且使用了该命令行选项‐fluct_props , 程序可以计算一些涨落相关的性质. 会计算以
下性质:

性质需要的能量项
等压热容C_p(NPT模拟) Enthalpy, Temp
等容热容C_v(NVT模拟) Etot, Temp
热膨胀系数(NPT模拟) Enthalpy, Vol, Temp
等温压缩率Vol, Temp
绝热体弹性模量Vol, Temp

你也需要通过‐nmol 来设定分子的数目. C_p/C_v的计算 不 包含任何量子效应校正. 如果需要考虑量子效应可以使
用gmx dos 程序.

当设置‐viol 选项时, 会绘制时间平均的背离数据, 并重新计算背离的实时时间平均值和瞬时累计值. 此外, 可以利
用‐pairs 选项来绘制选定原子对之间的实时时间平均距离和瞬时距离.
选项‐ora , ‐ort , ‐oda , ‐odr 和‐odt 用于分析取向限制数据. 前两个选项绘制取向, 后三个选项绘制来自实验值
的取向偏差. 以上选项中以a 结尾的选项绘制时间平均随限制的变化. 以t 结尾选项会提示用户限制标签号并绘制数
据随时间的变化. 选项‐odr 绘制RMS偏差随限制的变化. 当使用时间或系综平均的取向限制运行时, 选项‐orinst
可以用来分析瞬时, 非系综平均的取向和偏差, 而不是时间和系综平均的值.
选项‐oten 用于绘制每个取向限制实验中分子序张量的特征值. 与选项‐ovec 同用时还可以绘制特征向量.
选项‐odh 用于从ener.edr 文件中提取并绘制自由能数据(哈密顿差值和/或哈密顿导数dhdl).
使用‐fee 选项会计算体系与理想气体状态时的自由能差值:



## 参考

- https://manual.gromacs.org/current/onlinehelp/gmx-energy.html
