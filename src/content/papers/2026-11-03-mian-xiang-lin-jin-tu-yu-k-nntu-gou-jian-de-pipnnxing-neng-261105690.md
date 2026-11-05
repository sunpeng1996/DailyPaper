---
title: Turbocharging PiPNN for Proximity and $k$-NN Graph Building
title_zh: 面向邻近图与k-NN图构建的PiPNN性能优化方案
authors:
- Tobias Rubel
- Richard Wen
- Guy Blelloch
- Laxman Dhulipala
- Lars Gottesbüren
- Jakub Łącki
- Vahab Mirrokni
affiliations:
- University of Maryland
- Carnegie Mellon University
- Google Research
arxiv_id: '2611.05690'
url: https://arxiv.org/abs/2611.05690
pdf_url: https://arxiv.org/pdf/2611.05690
published: '2026-11-03'
collected: '2026-11-05'
category: Other
direction: 向量检索 · ANNS索引构建加速
tags:
- ANNS
- k-NN Graph
- PiPNN
- GPU Acceleration
- Quantization
one_liner: 提出CPU版PiPNN II与GPU版GPiPNN，实现ANNS索引与k-NN图构建数倍到数十倍提速
practical_value: '- 电商/推荐系统的向量召回模块迭代时，可直接复用PiPNN II/GPiPNN的量化+GEMM融合top-K kernel设计，大幅降低百亿级商品/内容向量索引的构建耗时，适配向量库日更甚至小时级更新的需求

  - GPU端向量索引构建可参考将递归分区扁平化、用固定大小score tile适配GPU张量核心的方案，相比现有主流CAGRA/Jasper实现最高可获50倍提速，大幅降低大尺度索引构建的机器成本

  - 相似品推荐、用户聚类、异常检测等场景需要快速构建k-NN图时，可复用PiPNN分块直接生成候选边的思路，跳过传统「先建索引再逐点查询」的冗余步骤，CPU端最高可获13倍提速'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有图结构近似最近邻搜索（ANNS）索引（如HNSW、Vamana）查询性能优异，但构建速度极慢，无法适配电商/推荐系统中商品/内容向量库高频更新、大尺度k-NN图快速构建的需求；初代PiPNN虽已比主流Vamana实现提速11.6倍，但未充分利用量化、硬件指令集等优化空间，仍有性能潜力可挖。
### 方法关键点
- 量化优化：采用RSQ8（8位旋转标量量化）、TQ4（4位TurboQuant变种）两种量化方案压缩向量，同时适配CPU VNNI、GPU张量核心的低精度矩阵运算指令，大幅降低内存访存开销。
- 核函数融合：将GEMM运算与top-K聚合核函数深度融合，避免完整距离矩阵落盘，降低IO开销；CPU端针对top-K的不同K值定制专用实现，GPU端将递归分区逻辑扁平化、用固定大小score tile适配GPU硬件调度规则，提升张量核心利用率。
- 工程优化：GPU端替换依赖锁的HashPrune为排序合并方案，避免并发写冲突；将需要重新计算距离的RobustPrune替换为DirectEdgePrune，复用已计算的边距离避免重复运算。
### 关键结果
实验覆盖文本、图像、多模态共12个数据集，最大规模达10亿点：CPU版PiPNN II比初代PiPNN最高提速8倍，比量化Vamana平均提速5.9倍，10亿级10-NN图构建仅需16分钟；GPU版GPiPNN比CAGRA最高提速50倍，比Jasper最高提速43.7倍，k-NN图构建比cuVS NN-Descent最高提速6.6倍，所有方案均保留了与原方法相当的查询召回率。
### 核心结论
针对特定硬件定制的量化+核融合设计，可将ANNS索引构建速度提升一个数量级，完全适配大模型时代向量库高频更新的需求
