# Shell 扩展

## 花括号

例如：

```bash
mjw@happy:~/scripts$ echo Front-{A,B,C}-Back
Front-A-Back Front-B-Back Front-C-Back
```

花括号表达式可以是逗号分隔的字符串列表，也可以是整数区间或单个字符，但不能 包含未经引用的空白字符。

- 整数区间

```bash
mjw@happy:~/scripts$ echo Number_{1..5}
Number_1 Number_2 Number_3 Number_4 Number_5
```

