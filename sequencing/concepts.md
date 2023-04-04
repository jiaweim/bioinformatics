# 测序概念

## read

高通量测序时，芯片上的每个反应都会读出一条较短的序列，称为 **read**，即读段或读序。

一代和三代的 reads 读长在几千到几万 bp 之间，二代的相对较短，平均几十到几百 bp。

PE reads 就是 paired-end reads。在测序过程中，一条 DNA 分子的两端都可以测序。先测其中的一端，获得一条 read，然后再转到另一端测序，获得另一条 read。得到的这两个 reads 就是PE reads。PE reads 的获得有助于后期序列组装。

## contig

有很多 reads 通过片段重叠，能够组装成一个更大的片段，称为 contig，它们是（片段）重叠群；就是不同reads之间的overlap（交叠区），拼接成的序列就是contig。

Contig N50：Reads拼接后会获得一些不同长度的Contigs.将所有的Contig长度相加,能获得一个Contig总长度.然后将所有的Contigs按照从长到短进行排序,如获得Contig 1,Contig 2,contig 3...………Contig 25.将Contig按照这个顺序依次相加,当相加的长度达到Contig总长度的一半时,最后一个加上的Contig长度即为Contig N50.举例：Contig 1+Contig 2+ Contig 3 +Contig 4=Contig总长度*1/2时,Contig 4的长度即为Contig N50.ContigN50可以作为基因组拼接的结果好坏的一个判断标准。