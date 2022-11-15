# gmx rms

## 简介

```bash
gmx rms [-s [<.tpr/.gro/...>]] [-f [<.xtc/.trr/...>]]
        [-f2 [<.xtc/.trr/...>]] [-n [<.ndx>]] [-o [<.xvg>]]
        [-mir [<.xvg>]] [-a [<.xvg>]] [-dist [<.xvg>]] [-m [<.xpm>]]
        [-bin [<.dat>]] [-bm [<.xpm>]] [-b <time>] [-e <time>]
        [-dt <time>] [-tu <enum>] [-[no]w] [-xvg <enum>]
        [-what <enum>] [-[no]pbc] [-fit <enum>] [-prev <int>]
        [-[no]split] [-skip <int>] [-skip2 <int>] [-max <real>]
        [-min <real>] [-bmax <real>] [-bmin <real>] [-[no]mw]
        [-nlevels <int>] [-ng <int>]
```

## 选项

|选项|默认值|说明|
|---|---|---|
|`-s` [<.tpr/.gro/…>]|topol.tpr|Structure+mass(db): tpr gro g96 pdb brk ent|
|`-f` [<.xtc/.trr/…>]|traj.xtc)|Trajectory: xtc trr cpt gro g96 pdb tng|

## 参考

- https://manual.gromacs.org/current/onlinehelp/gmx-rms.html
