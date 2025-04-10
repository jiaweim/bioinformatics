# 字符串匹配

## String

字符串为有限字符序列。字符从字母表（alphabet）$\sum$ 抽取，对 DNA 序列：
$$
\sum=\{A,C,G,T\}
$$

- 子字符串

`S` 的子字符串（substring）指 `S` 内部的字符串：

```python
>>> s = 'AACCGGTT' 
>>> s[2:6] 
'CCGG' # substring of seq
```

如果存在字符串 `u` 和 `v`，满足 $T=uSv$，那么 $S$ 就是 $T$ 的子字符串（`u` 或 `v` 可以为空）。

- 前缀

`S` 的前缀（prefix）是从 $S$ 开头开始的子字符串。

```python
>>> s = 'AACCGGTT' 
>>> s[0:6] 
'AACCGG' # prefix 
>>> s[:6] # same as above 
'AACCGG'
```

- 后缀

`S` 的后缀（suffix）是到 `S` 末尾的子字符串。

```python
>>> s = 'AACCGGTT' 
>>> s[4:8] 
'GGTT' # suffix 
>>> s[4:] # like s[4:len(s)] 
'GGTT'  
>>> s[-4:] # like s[len(s)-4:len(s)] 
'GGTT'
```

## naïve 算法

查找 pattern $P$ 在文本 $T$ 中出现的位置。每个出现的位置称为一个匹配（match）。

令，$n=|P|$, $m=|T|$, $n\le m$。

尝试所有位置，检查是否匹配，称为 **naïve 算法**。

naïve 算法很简单，Python 实现如下：

- p, Pattern
- t, text

```python
def naive(p, t): 
    occurrences = [] 
    for i in range(len(t) - len(p) + 1):  # loop over alignments 
        match = True 
        for j in range(len(p)):           # loop over characters 
            if t[i+j] != p[j]:            # compare characters 
                match = False             # mismatch; reject alignment 
                break 
        if match: 
          occurrences.append(i)           # all chars matched; record 
    return occurrences
```

`naive` 可以直接采用 java 自带的 `String.indexOf` 实现。

- 可能的匹配个数

$$
m-n+1
$$

<img src="./images/image-20250410110204383.png" alt="image-20250410110204383" style="zoom:50%;" />

- 字符匹配最大可能次数：若次都正确匹配，对应长度 $n$，则匹配次数最多

$$
n(m-n+1)
$$

- 字符匹配最小可能次数：第一次就失败

$$
(m-n+1)
$$

## Boyer-Moore

Boyer-Moore 与 Naive-exact-matching 类似，但是会跳过不必要的匹配，从而提高速度。

Boyer-Moore 算法被认为是最有效的自然语言字符串匹配算法。其性能至少是其它算法的两倍。

例如：

<img src="./images/image-20250410141450720.png" alt="image-20250410141450720" style="zoom:50%;" />

由于 $P$ 中没有 $u$，因此可以跳过接下来的两个匹配。

Boyer-Moore 匹配规则：

1. Bad character rule：当字符不匹配，可以跳过多少字符
2. Good suffix rule：使用匹配的字符来确定可以跳过多少字符，当 bad character rule 跳过字符太少时应用
3. 从左向右匹配，但是从右向左进行字符比较

*good suffix rule* 比较难理解，有些简化算法直接将其简化为向后移动一位字符。

**Bad character rule**

对 mismatch，向后移动 $P$ 直到：

a. mismatch 变为 match，对 Step1，T 与 C 不匹配，需要将 $P$ 向后移动 3 位，才能匹配到 `C`

b. G 与 A 不匹配，但是 $P$ 没有 A，所以移动 $P$，直到跳过 A

c. 如果完整匹配，则不跳过字符

<img src="./images/image-20250410144956567.png" alt="image-20250410144956567" style="zoom:50%;" />

**Good suffix rule**

令 $t$ 为内部循环匹配的子串，跳过直到：

a. $P$ 和 $t$ 之间没有匹配

b. 或者 $P$ 超过了 $t$

<img src="./images/image-20250410152004015.png" alt="image-20250410152004015" style="zoom:50%;" />

同时应用 bad character 和 good suffix 规则：

1. 没有匹配，应用 bad character 规则
2. 匹配 3 个字符，采用 bad character 规则可以后移动 1 位，即跳过 0 位；采用 good suffix 规则可以后移 3 位，即跳过 2 位
3. 匹配 6 个字符，采用 bad character 规则可以后移 3 位，即跳过 2 位；采用 good suffix 规则可以后移 8 位，即跳过 7 位

<img src="./images/image-20250410152355107.png" alt="image-20250410152355107" style="zoom:50%;" />

### 预处理

为了更好地应用 Boyer-Moore 规则，需要对 $P$ 进行预处理，构建一个**查询表**。

假设 $P=TCGC$，对 **bad character** 规则：

- 横向为 pattern $P$
- 纵向为字母表 $\sum$

|      | T    | C    | G    | C    |
| ---- | ---- | ---- | ---- | ---- |
| A    | 0    | 1    | 2    | 3    |
| C    | 0    | -    | 0    | -    |
| G    | 0    | 1    | -    | 0    |
| T    | -    | 0    | 1    | 2    |

例如，$P$ 的 G 与 文本 T 不匹配，查表值为 1，所以可以跳过 1 位，即后移 2 位：

<img src="./images/image-20250410155028469.png" alt="image-20250410155028469" style="zoom:50%;" />

### Z Algorithm

在线性时间内计算 $Z_i$, $r_i$ 和 $l_i$，从 $i=2$ 开始（1-based）。

- z-box，与前缀匹配的子字符串（1 除外）
- $Z_i$ 表示 z-box 的长度
- $l_i$ 表示 z-box 起始位置
- $r_i$ 表示 z-box 终止位置：对 $1<j\le i$，$r_i$ 是使得 $Z_j>0$ 的 $j+Z_j-1$ 的最大值

$S=aabaabcaxaabaabcy$，那么

例如，对字符串 $S=aabcaabxaaz$：

- $Z_5$=3 (aabx...aabc)
- $Z_6=1$ (ab...aa)
- $Z_7=0$ (bx..aa)
- $Z_8=0$ (xa..aa)
- $Z_9=2$ (aaz..aab)

如果直接根据该定义计算所有 $Z_i$，则时间复杂度为 $O(|S|^2)$，而 Z 算法能在 $O(|S|)$ 时间内完成。

计算 $Z_2$：从左向右对比 $S[2..|S|]$ 与 $S[1..|S|]$，直到发现 mismatch：

- 如果 $Z_2>0$，则 $r_2=Z_2+1$, $l_2=2$
- 否则 $r_2=0$, $l_2=0$

假设已经计算 $Z_{k-1}$ 对 $k-1>1$，即已知 $r_{k-1}$ 和 $l_{k-1}$，核心思想利用已经计算的 $Z_{k-1}$ 来加速 $Z_k$ 的计算。

在某些情况，不需要任何比对，就可以从 $Z_{k-1}$ 推导出 $Z_k$。例如，假设 $k=121$，已经计算 $Z_2$ 到 $Z_{120}$，并且 $r_{120}=130$, $l_{120}=100$。这表示从 100 开始长度为 31 的子串与 $S$ 前缀匹配。由此可见，从位置 121 开始到 130 长度为 10 的子串必然与 $S$ $i=22$ 的子串匹配，因此，$Z_{22}$ 对计算 $Z_{121}$ 有帮助：

- 假设 $Z_{22}=3$，

##  参考

- https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm
- Boyer, RS and Moore, JS. "A fast string searching algorithm." Communications of the ACM 20.10 (1977): 762-772.
- https://www.cs.emory.edu/~cheung/Courses/253/Syllabus/Text/Matching-Boyer-Moore1.html#:~:text=The%20Boyer%2DMoore%20algorithm%20is,as%20the%20other%20algorithms%20tested.
- 《Algorithms on Strings, Trees and Sequences: Computer Science and Computational Biology》,Dan Gusfield

