# 开源 PyMOL 安装

下载地址： https://www.lfd.uci.edu/~gohlke/pythonlibs/

下载包：

- numpy+mkl
- PMW
- pymol

使用 pip 依次安装上面三个包。

这样子 PyMOL 能使用，但是在界面上会缺少部分功能，因为 PyMOL 部分界面是用 PyQT5 构建的，所以最后还要安装 pyqt5:

```python
pip install pyqt5
```
