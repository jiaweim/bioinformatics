# CHARMM36

下载 CHARMM36 力场文件：

http://mackerell.umaryland.edu/charmm_ff.shtml#gromacs

下载的 charmm36-jul2021.ff.tgz 文件，放到 gromacs 安装目录下的 top 目录：

`/usr/local/share/gromacs/top`

解压:

```sh
tar -xzvf charmm36-jul2021.ff.tgz
```

> 这个力场中没有 CL 离子

换成 charmm36-feb2021.ff 力场

在 GROMACS 5.0+ 中使用 CHARMM36，在 mdp 文件中使用如下设置：

```powershell
constraints = h-bonds
cutoff-scheme = Verlet
vdwtype = cutoff
vdw-modifier = force-switch
rlist = 1.2
rvdw = 1.2
rvdw-switch = 1.0
coulombtype = PME
rcoulomb = 1.2
DispCorr = no
```
