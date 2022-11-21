# 恒压方法

- [恒压方法](#恒压方法)
  - [简介](#简介)
  - [Berenedsen barostat](#berenedsen-barostat)
  - [参考](#参考)

***

## 简介

分子动力学（MD）是一种模拟分子运行的计算技术。为了评估模拟结果的质量，可恶意将模拟结果与真实实验结果进行比较。如果模拟结果与实验数据接近，则认为模拟结果正确。

在实验室中，化学反应一般在恒压下进行，为了模拟这类数据，需要模拟系统在恒压下随时间的变化。可以认为这类算法在实验中实现了一个气压调节器（barostat），该方法允许瞬间的压力波动，但是压力均值保持恒定。

分子动力学中使用最广泛的系综是 NPT 系综，其原子数（N）、压力（P）和温度（T）是守恒的。因此，恒压算法（barostat）往往与恒温算法（thermostat）一起实现，以便模拟恒温、恒压过程。

## Berenedsen barostat





## 参考

- https://www.compchems.com/barostats-in-molecular-dynamics/
