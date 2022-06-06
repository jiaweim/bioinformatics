# free

- [free](#free)
  - [简介](#简介)
  - [实例](#实例)
  - [信息解释](#信息解释)
    - [buff/cache](#buffcache)
    - [free vs. available](#free-vs-available)
    - [交换空间](#交换空间)
    - [/proc/meminfo](#procmeminfo)

2022-06-06, 11:06
*****

## 简介

`free` 命令显示系统内存使用量情况，包含物理和交换内存的总量、使用量和空闲量情况。

```sh
free [参数]
```

|参数|说明|
|---|---|
|-b|以Byte显示内存使用情况|
|-k|以kb为单位显示内存使用情况|
|-m|以mb为单位显示内存使用情况|
|-g|以gb为单位显示内存使用情况|
|-s|持续显示内存|
|-t|显示内存使用总合|
|-h|以易读的单位显示内存使用情况|

## 实例

- 以默认单位显示内存使用量

```sh
[root@localhost ~]# free
              total        used        free      shared  buff/cache   available
Mem:      527747332    23999468    17294004       34824   486453860   501909456
Swap:       4194300      554240     3640060
```

- 以 MB 为单位显示内存信息

```sh
[root@localhost ~]# free -m
              total        used        free      shared  buff/cache   available
Mem:         515378       23455       16856          34      475066      490127
Swap:          4095         541        3554
```

- 以易读的单位显示内存信息

```sh
[root@localhost ~]# free -h
              total        used        free      shared  buff/cache   available
Mem:           503G         22G         16G         34M        463G        478G
Swap:          4.0G        541M        3.5G
```

- 以易读的单位显示内存信息，每 10 秒刷新一次

```sh
[root@localhost ~]# free -hs 10
              total        used        free      shared  buff/cache   available
Mem:           503G         22G         16G         34M        463G        478G
Swap:          4.0G        541M        3.5G

              total        used        free      shared  buff/cache   available
Mem:           503G         22G         16G         34M        463G        478G
Swap:          4.0G        541M        3.5G
```

按 `Ctrl+C` 停止输出。

## 信息解释

说明：

- Mem，是内存的使用情况
- Swap，是交换空间使用情况
- total，系统总的物理内存和交换空间
- used，已使用的物理内存和交换空间
- free，还有多少物理内存和交换空间可用
- shared，被共享使用的物理内存
- buff/cache，被 buffer 和 cache 使用的物理内存
- available，还可以被应用程序使用的物理内存大小

### buff/cache

`buffer` 指缓冲区。要理解缓冲区，首先要理解 “扇区” 和 “块”：

- 扇区是设备的最小寻址单元，也叫 “硬扇区” 或 “设备块”。
- 块是操作系统中文件系统的最小寻址单元，也叫 “文件块” 或  “I/O 块”。

每个块包含一个或多个扇区，但大小不能超过一个页面，所以一个页可以容纳一个或多个内存中的块。当一个块被调入内存，它要存储在一个缓冲区中，每个缓冲区与一个块对应，它相当于磁盘块在内存中的表示。

> buffer cache 只有块的概念而没有文件的概念，它只是把磁盘上的块直接搬到内存中，而不关心块中存放的是什么格式的文件。

`cache` 在操作系统中指 page cache，即 “页高速缓存”。页高速缓存是内核实现的磁盘缓存。它主要用来减少对磁盘的 I/O 操作。具体来说，是通过把磁盘中的数据缓存到物理内存中，把对磁盘的访问变为对物理内存的访问。页告诉缓存的是内存页面。缓存中的页来自对普通文件、块设备文件（即 buffer cache）和内存映射文件的读写。

页高速缓存对普通文件的缓存我们可以这样理解：当内核要读一个文件(比如 `/etc/hosts`)，它会先检查这个文件的数据是不是已经在页高速缓存中了。如果在，就放弃访问磁盘，直接从内存中读取。这个行为称为缓存命中。如果数据不在缓存中，就是未命中缓存，此时内核就要调度块 I/O 操作从磁盘去读取数据。然后内核将读来的数据放入页高速缓存中。这种缓存的目标是文件系统可以识别的文件(比如 `/etc/hosts`)。

页高速缓存对块设备文件的缓存就是我们在前面介绍的 buffer cache。因为独立的磁盘块通过缓冲区也被存入了页高速缓存(缓冲区最终是由页高速缓存来承载的)。

到这里我们应该搞清楚了：无论是缓冲区还是页高速缓存，它们的实现方式都是一样的。缓冲区只不过是一种概念上比较特殊的页高速缓存罢了。

那么为什么 `free` 命令不直接称为 cache 而非要写成 buff/cache？ 这是因为缓冲区和页高速缓存的实现并非天生就是统一的。在 linux 内核 2.4 中才将它们统一。更早的内核中有两个独立的磁盘缓存：页高速缓存和缓冲区高速缓存。前者缓存页面，后者缓存缓冲区。当你知道了这些故事之后，输出中列的名称可能已经不再重要了。

### free vs. available

`free` 是真正尚未被使用的物理内存数量。`available` 则是从应用程序的角度看到的可用内存数量。

Linux 内核为了提升磁盘的操作情况，会消耗一部分内存去缓存磁盘数据，即 buffer 和 cache。所以对内核来说，buffer 和 cache 都属于已经被使用的内存，当应用程序需要内存时，如果没有足够的 `free` 内存可用，内核就会从 buffer 和 cache 中回收内存来满足应用程序的请求。所以从应用程序的角度看，`available=free+buffer+cache`，不过这只是一个很理想的计算方式，实际上的数据有较大的误差。

### 交换空间

swap space 是磁盘上的一块区域，可以是一个分区，也可以是一个文件。所以具体的实现可以是 swap 分区也可以是 swap 文件。当系统物理内存吃紧时，Linux 会将内存中不常访问的数据保存到 swap 上，这样系统就有更多的物理内存为各个进程服务，而当系统需要访问 swap 上存储的内容时，再将 swap 上的数据加载到内存中，这就是常说的换出和换入。交换空间可以在一定程度上缓解内存不足的情况，但是它需要读写磁盘数据，所以性能不是很高。

现在的机器一般都不太缺内存，如果系统默认还是使用了 swap 是不是会拖累系统的性能？理论上是的，但实际上可能性并不是很大。并且内核提供了一个叫做 swappiness 的参数，用于配置需要将内存中不常用的数据移到 swap 中去的紧迫程度。这个参数的取值范围是 0～100，0 告诉内核尽可能的不要将内存数据移到 swap 中，也即只有在迫不得已的情况下才这么做，而 100 告诉内核只要有可能，尽量的将内存中不常访问的数据移到 swap 中。在 ubuntu 系统中，swappiness 的默认值是 60。如果我们觉着内存充足，可以在 /etc/sysctl.conf 文件中设置 swappiness：

```sh
vm.swappiness=10
```

如果系统的内存不足，则需要根据物理内存的大小来设置交换空间的大小。

### /proc/meminfo

其实 free 命令中的信息都来自于 /proc/meminfo 文件。/proc/meminfo 文件包含了更多更原始的信息，只是看起来不太直观：

```sh
[root@localhost ~]# cat /proc/meminfo
MemTotal:       527747332 kB
MemFree:        42394308 kB
MemAvailable:   520738284 kB
Buffers:             104 kB
Cached:         471211804 kB
SwapCached:        41488 kB
Active:         268226676 kB
Inactive:       203722368 kB
Active(anon):     430988 kB
Inactive(anon):   341104 kB
Active(file):   267795688 kB
Inactive(file): 203381264 kB
Unevictable:           0 kB
Mlocked:               0 kB
SwapTotal:       4194300 kB
SwapFree:        3646972 kB
Dirty:                32 kB
Writeback:             0 kB
AnonPages:        702976 kB
Mapped:            96824 kB
Shmem:             34912 kB
Slab:            9667732 kB
SReclaimable:    8970468 kB
SUnreclaim:       697264 kB
KernelStack:       30848 kB
PageTables:        54640 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:    268067964 kB
Committed_AS:    6383984 kB
VmallocTotal:   34359738367 kB
VmallocUsed:     1346176 kB
VmallocChunk:   34219903836 kB
HardwareCorrupted:     0 kB
AnonHugePages:    339968 kB
CmaTotal:              0 kB
CmaFree:               0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:      756736 kB
DirectMap2M:    25067520 kB
DirectMap1G:    512753664 kB
```
