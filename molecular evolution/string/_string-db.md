# STRING

如果你想先看看已知的、高置信度的共进化伙伴
→ 直接用 STRING，输入蛋白 A，寻找紫色（同现）边的连接蛋白。

如果你已有候选蛋白 B，想用实验前先行验证
→ 用 MirrorTree 在线服务器，上传两个蛋白的比对，看相关系数。
→ 或尝试 EVcomplex 做更精细的耦合分析。

如果你需要一套可本地批量运行的方案
→ 用 Python 的 EVcouplings 包（含 EVcomplex）分析多对蛋白。
→ 用 R 包 phangorn + ape 自行实现镜像树流程。

## 入门




## 参考

- https://string-db.org/