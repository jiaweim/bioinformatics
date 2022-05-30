# gmx genion

- [gmx genion](#gmx-genion)
  - [说明](#说明)
  - [选项](#选项)
  - [参考](#参考)

2022-05-27, 10:16
***

```sh
gmx genion [-s [<.tpr>]] [-n [<.ndx>]] [-p [<.top>]]
           [-o [<.gro/.g96/...>]] [-np <int>] [-pname <string>]
           [-pq <int>] [-nn <int>] [-nname <string>] [-nq <int>]
           [-rmin <real>] [-seed <int>] [-conc <real>] [-[no]neutral]
```

## 说明

`gmx genion` 用单原子离子随机替换溶剂分子。

溶剂分子群应该是连续的，且所有分子应该有相同数目的原子。用户应该将离子添加到拓扑文件中，或者用 `-p` 选项自动修改拓扑文件。

所有力场中的离子分子类型、残基和原子名称都是无符号的大写元素名称。使用 `-pname` 或 `-nname` 选项指定分子名称，拓扑文件中的 `[molecules]` 部分也应该相应更新，可以手动更新，也可以用 `-p` 选项自动更新。不要使用原子名称。

对多电荷离子。。。

对较大的粒子，例如硫酸盐，建议使用 `gmx insert-molecules`。

## 选项

**输入文件选项**

|选项|可选|说明|
|---|---|---|
|`-s [<.tpr>] (topol.tpr)`|

**输出文件选项**

|选项|可选|说明|
|---|---|---|
|`-o [<.gro/.g96/…>] (out.gro)`||结构文件：gro g96 pdb brk ent esp|

## 参考

- https://manual.gromacs.org/current/onlinehelp/gmx-genion.html
