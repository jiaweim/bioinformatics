# gmx editconf

## 简介

```sh
gmx editconf [-f [<.gro/.g96/...>]] [-n [<.ndx>]] [-bf [<.dat>]]
             [-o [<.gro/.g96/...>]] [-mead [<.pqr>]] [-[no]w]
             [-[no]ndef] [-bt <enum>] [-box <vector>]
             [-angles <vector>] [-d <real>] [-[no]c]
             [-center <vector>] [-aligncenter <vector>]
             [-align <vector>] [-translate <vector>]
             [-rotate <vector>] [-[no]princ] [-scale <vector>]
             [-density <real>] [-[no]pbc] [-resnr <int>] [-[no]grasp]
             [-rvdw <real>] [-[no]sig56] [-[no]vdwread] [-[no]atom]
             [-[no]legend] [-label <string>] [-[no]conect]
```

## 选项

**IO 选项**

|选项|说明|默认值|
|---|---|---|
|`-f` [<.gro/.g96/…>]|输入结构文件|conf.gro|
|`-o` [<.gro/.g96/…>]|输出结构文件：gro g96 pdb brk ent esp|out.gro|
|`-[no]c`|

**其它选项**

|选项|说明|默认值|
|---|---|---|
|`-bt` `<enum>`|选择盒子类型：triclinic, cubic, dodecahedron, octahedron|triclinic|
|`-box` `<vector>`|盒子向量长度|(0 0 0)|
|`-d` `<real>`|溶质与盒子的距离|0|

## 参考

- https://manual.gromacs.org/documentation/current/onlinehelp/gmx-editconf.html
