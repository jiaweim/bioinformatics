# CentOS 文件系统

- [CentOS 文件系统](#centos-文件系统)
  - [结构](#结构)
  - [usr](#usr)

2022-06-06, 14:02
***

## 结构

|Linux 目录|功能|与 Windows 对比|
|---|---|---|
|`/`|Linux 顶级目录|C:\|
|`/bin`|与系统相关的二进制文件，如 ls, rm 等|C:\Windows|
|`/boot`|与启动相关的文件|C:\Windows|
|`/dev`|与 Linux 连接的所有设备信息|C:\Windows|
|`/etc`|Linux 系统及应用的配置文件|C:\Windows|
|`/home`|用户目录|My Documents|
|`/lib`|库文件|C:\Windows\system|
|`/lost+found`|fsck (filesystem check)恢复的文件|Found.000|
|`/media`|可移动设备的挂载点，如 CD/DVD ROM 等，这些设备连接到计算机后，会自动挂在到这个目录下|D: or E: drives|
|`/mnt`|早期 Linux 系统中，可移动介质的挂载点|A mapped drive such as X: , Y:, Z:|
|`/opt`|安装“可选”软件，如不由包管理器处理的软件，如商业软件|None|
|`/proc`|提供系统信息的虚拟文件系统|C:\Windows\system 或 C:\Windows\System32|
|`/root`|root 用户目录|My Documents for Administrator|
|`/sbin`|系统二进制文件，一般是完成系统任务的程序，通常为超级用户保留|C:\Windows|
|`/selinux`|存储安全增强相关信息，部分 Linux 分布版没有该目录|None|
|`/srv`|存储系统使用额数据服务|None|
|`/sys`|存储 Linux 系统信息|C:\Windows\system or C:\Windows\System32|
|`/tmp`|存储由各种应用程序创建的临时文件，一些配置导致系统每次重启时清空该目录|C:\Windows\Temp|
|`/usr`|存储用户程序|C:\Program Files or C:\ProgramData|
|`/var`|存储可变数据文件|None|

- /

系统根目录（不要与 `/root` 目录混淆，该文件夹是 root 用户的主目录）。`/` 是 Linux 文件系统的顶级目录，在 CentOS 7 中，所有其它文件和文件夹都位于 `/` 目录中。

- /boot

启动系统所需的文件，包括 Linux 内核、初始 RAM 磁盘映射（用于启动时所需的驱动）和启动加载程序。

- /etc

在 CentOS 7 中,`/etc` 目录包含系统配置文件。也包含一系列 shell 脚本，在系统启动时，这些脚本会开启系统服务。这个目录的文件都是可读的文本文件。普通用户通常无法访问该文件夹。

- /proc

proc 文件系统，又称为虚拟文件系统，包含系统硬件和运行时进程信息

在 `/proc` 内，可以看到以正在运行的 Linux 进程的 PID 命名的文件夹。与其它目录不同，proc 文件系统不再硬盘上，而是在系统内存 RAM 中，所以称其为虚拟文件系统。

- /dev

包含系统用来访问硬件设备的文件。在 CentOS 7 中，所有设备都由一个文件表示。将硬件插入计算机时，可以在 `/dev` 目录中找到与该硬件相关的文件。如硬盘、USB、CD 等。

- /home

包含用户个人数据和配置文件。在 `/home` 目录下默认包含每个 Linux 用户的目录。

普通用户只能在自己的目录下写文件。

- /root

超级用户的主目录。

- /var

动态文件，包括数据库、缓存目录、日志文件等。系统运行时，`/var` 目录的内存会动态改变。

- /usr

包含安装的软件以及共享库。该目录里可能是最大的一个，包含普通用户所需要的所有程序和文件。

- /usr/bin

包含系统所有用户可用的程序和命令，例如，基本的 Linux 命令 `ls`, `cd` 等。管理员和普通用户都可以使用。

- /usr/sbin

包含系统管理员使用的程序和命令。没有管理员权限无法执行 /usr/sbin 目录中的命令。

- /run

自上次启动以来启动进程的运行时数据。

- /lost+found

每个使用 Linux 文件系统的格式化分区或设备，如 ext3 文件系统，都会有这个目录。当部分恢复一个损坏的文件系统时，会用到这个目录。如果没有文件系统损坏，这个目录是空的。

## usr

`/usr` 目录结构和根目录 `/` 很多都是一样的。其内容如下：

- `/usr/bin`，存储常用的命令，如 `clear`, `gcc` 等
- `/usr/etc`，存储应用程序配置文件
- `/usr/games`，游戏应用目录
- `/usr/include`，存储头文件
- `/usr/lib`，存储库文件
- `/usr/libexec`，存储以二进制形式存储的库文件
- `/usr/local`，存储其它用户程序的目录，通常由源码编译的程序会安装在 `/usr/local/bin` 目录
- `/usr/sbin`，存储需要超级用户权限的程序二进制文件
- `/usr/share`，存储 Linux 安装程序的文档文件，即 `/usr/bin` 中程序使用的共享数据，包括默认的配置文件、图标、桌面背景、音频文件等。
- `/usr/share/doc`，大多数安装在系统的软件包会包含一些文档，在该目录下，可以找到按照软件包分类的文档。
- `/usr/src`，用户应用的源文件
- `/usr/tmp`，用作程序的临时目录，可能指向 `/var/tmp` 目录

如果继续查看 `/usr/local` 目录，会发现其内容和 `/usr` 一样。
