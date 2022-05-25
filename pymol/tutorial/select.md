# 选择

- [选择](#选择)
  - [简介](#简介)
  - [选择表达式](#选择表达式)
  - [选择运算符](#选择运算符)
  - [select](#select)
  - [参考](#参考)

2022-01-24, 12:30
***

## 简介

选择是必须要掌握的 PyMOL 操作之一。PyMOL 允许根据标识符和属性选择原子。许多命令（如 `color`, `show` 等）都支持对选择的原子子集进行操作。例如：

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

选择运算符和修饰符如下表所示。变量 `s1` 和 `s2` 表示选择表达式，如 "chain a" 或 "hydro"。

|运算符|等价操作符|说明|
|---|---|---|
|**通用操作**|||
|all|*|PyMOL 载入的所有原子|
|none||空选择|
|enabled||enabled 对象的原子|
|**命名选择**|||
|sele||命名选择或对象 "sele"（前提是不与其它运算符名称重复）|
|%sele||命名选择或对象 "sele"，推荐使用|
|?sele||命名选择或对象 "sele"，如果 "sele" 不存在，返回空选择|
|**逻辑**|||
|not S1|!|选择反转|
|S1 and S2| & |同时包含 S1 和 S2 的原子|
|S1 or S2|`|`|包含 S1 或 S2 的原子|
|S1 S2|| or|
|S1 and (S2 or S3)||括号用于控制顺序|
|first S1||S1 的第一个原子（单原子选择）|
|last S1||S1 的最后一个原子（单原子选择）|
|**识别符**|||
|model 1ubq|m.|对象 "1ubq" 的原子|
|chain C|c.|链识别符 "C"|
|segi S|s.|片段识别符 "S"|
|resn ALA|r.|残基名称 "ALA"|
|resi 100-200|i.|100-200 之间的残基|
|name CA|n.|原值名称 "CA"|
|alt A||备选位置 "A"|
|index 123|idx.|内部对象原子索引|
|id 123||PDB 文件中的 ID 列|
|rank 123||加载时对象索引索引|
|**属性**|||
|partial_charge < 1.2|pc.||
|elem C|e.|元素 C （碳）的所有原子|


## select

`select` 以选择的原子创建一个命名选择。语法：

```sh
select name [, selection [, enable [, quiet [, merge [, state ]]]]]
```

## 参考

- https://pymolwiki.org/index.php/Category:Selecting
- https://pymolwiki.org/index.php/Selection_Algebra
