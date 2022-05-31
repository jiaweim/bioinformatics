# 选择

- [选择](#选择)
  - [简介](#简介)
  - [选择表达式](#选择表达式)
  - [选择运算符](#选择运算符)
  - [select](#select)
  - [示例](#示例)
  - [参考](#参考)

2022-01-24, 12:30
***

## 简介

**选择** 是必须要掌握的 PyMOL 操作之一。PyMOL 可以根据标识符和属性选择原子。许多命令（如 `color`, `show` 等）支持对选择的原子子集进行操作。例如：

```sh
PyMOL>show spheres, solvent and chain A
```

和逻辑运算符 `and`, `or` 和 `not` 结合，选择语法更加强大。`and` 表示只选择满足所有属性的原子，而 `or` 则选择满足任一条件的原子。

## 选择表达式

选择表达式用于选择原子对象。命名支持大小写字母、数字和下划线，以下字符不可用：

```sh
! @ # $ % ^ &* ( ) ' " [ ] { } \ | ~ ` <> . ? /
```

## 选择运算符

下表为选择运算符和修饰符。变量 `s1` 和 `s2` 表示选择表达式，如 "chain a" 或 "hydro."。

|运算符|等价操作符|说明|
|---|---|---|
|**通用操作**|||
|all|*|PyMOL 载入的所有原子|
|none||空选择|
|enabled||enabled 对象的原子|
|**命名选择**|||
|sele||命名选择或对象 "sele"（前提是不与其它运算符名称重复）|
|%sele||命名选择或对象 "sele"，**避免歧义，推荐使用**|
|?sele||命名选择或对象 "sele"，如果 "sele" 不存在，返回空选择|
|**逻辑**|||
|not S1|!|选择反转|
|S1 and S2| & |S1 和 S2 同时包含的原子|
|S1 or S2|`|`|S1 或 S2 包含的原子|
|S1 S2|| 隐式 or|
|S1 and (S2 or S3)||括号用于控制顺序|
|first S1||S1 的第一个原子（单原子选择）|
|last S1||S1 的最后一个原子（单原子选择）|
|**识别符**|||
|model 1ubq|m.|对象 "1ubq" 的原子|
|chain C|c.|链识别符 "C"|
|segi S|s.|片段识别符 "S"|
|resn ALA|r.|残基名称 "ALA"|
|resi 100-200|i.|残基识别符在 100-200 之间的残基|
|name CA|n.|原子名称 "CA"|
|alt A||备选位置 "A"|
|index 123|idx.|内部对象原子索引|
|id 123||PDB 文件中的 ID 列|
|rank 123||加载时对象原子索引|
|pepseq ACDEF|ps.|单字母编码的蛋白质残基序列 "ACDEF" (see also FindSeq)|
|label "Hello World"||标签为 "Hello World" 的原子 (new in PyMOL 1.9)|
|**标识符匹配**|||
|S1 in S2||S1 中 name, resi, resn, chain 和 segi 都和 S2 中匹配的原子|
|S1 like S2||S1 中 name, resi 和 S2 中匹配的原子|
|**实体扩展**|||
|||所有的 `by` 运算符优先级都较低，因此 `(byres S1 or S2)` 等价于 `(byres (S1 or S2))`|
|byobject S1||将 S1 扩展为完整对象|
|bysegi S1|bs.|将 S1 扩展为整个片段|
|bychain S1|bc.|将 S1 扩展为整条链|
|byres S1|br.|将 S1 扩展为整个残基|
|bycalpha S1|bca.|至少有一个原子在 S1 中的残基的 CA 原子|
|bymolecule S1|bm.|将 S1 扩展为完整分子（通过化学键连接）|
|byfragment S1|bf.||
|byring S1||至少有一个原子在 S1 中的所有 ≤7 的 环|
|bycell S1||将所选内容扩展到单元格|
|**键扩展**|||
|bound_to S1|bto.|直接 S1 连接的原子，包括 S1|
|neighbor S1|nbr.|直接和 S1 连接的原子，不包括 S1|
|S1 extend 3|xt.|扩展 3 个连接化学键|
|**距离**|||
|S1 within 12.3 of S2|w.|S1 中原子，要求与 S2 中任何原子距离在 12.3 A 内|
|S1 around 12.3|a.|原子的中心与 S1 中任意原子的中心在 12.3 内|
|S1 expand 12.3|x.|原子的中心与 S1 中任意原子的中心在 12.3 内的原子，包括 S1|
|S1 gap 1.2||与 S1 的 VDW 半径至少为 1.2A 的原子|
|S1 near_to 12.3 of S2|nto.|同 `within`，
|**属性**|||
|partial_charge < 1.2|pc.||
|elem C|e.|元素 C （碳）的所有原子|


## select

`select` 以选择的原子创建一个命名选择。语法：

```sh
select name [, selection [, enable [, quiet [, merge [, state ]]]]]
```

## 示例

- 选择 chain A 的原子，但不包含编号为 125 的残基

```sh
select chain A and (not resi 125)
```

## 参考

- https://pymolwiki.org/index.php/Category:Selecting
- https://pymolwiki.org/index.php/Selection_Algebra
