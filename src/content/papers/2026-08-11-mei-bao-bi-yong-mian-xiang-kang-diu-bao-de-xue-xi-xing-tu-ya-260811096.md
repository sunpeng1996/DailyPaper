---
title: 'Every Packet Counts: Dispersing Information for Loss-Resilient Learned Image
  Compression'
title_zh: 每包必用：面向抗丢包的学习型图像压缩信息分散方法
authors:
- Yuhang Wei
- Chuqin Zhou
- Yibo Shi
- Jing Wang
- Guo Lu
affiliations:
- Shanghai Jiao Tong University
- Central Media Technology Institute, Huawei Technologies Ltd.
arxiv_id: '2608.11096'
url: https://arxiv.org/abs/2608.11096
pdf_url: https://arxiv.org/pdf/2608.11096
published: '2026-08-11'
collected: '2026-08-12'
category: Other
direction: 学习型图像压缩 · 抗丢包性能优化
tags:
- Learned Image Compression
- Loss Resilience
- Channel Redistribution
- Autoregressive Structure
- Image Coding
one_liner: 提出通道重分配+交错分组+短依赖结构的端到端抗丢包学习图像压缩方案，性能显著优于SOTA
practical_value: '- 弱网商品图传输场景可直接复用：跨境/下沉市场电商的商品图传输可落地整套方案，提升丢包场景下图片加载质量

  - 信息分散抗单点思路可复用：推荐/广告特征体系可参考通道重分配逻辑，避免核心信息过度集中在少数特征/模块，降低单节点故障影响

  - 交错分组策略可迁移至多队列流量调度：将高优请求按步长打散到不同队列，单队列故障时不会损失过多高优流量

  - 短依赖链思路可优化推荐链路架构：减少模块间串行强依赖，避免单个模块故障引发全链路效果雪崩'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有学习型图像压缩（LIC）在卫星、应急通信等常见丢包场景下表现极差，根源来自两个核心问题：组包阶段信息分布不均，关键信息集中在少数通道；熵编码阶段存在串行解码依赖，单个包丢失易引发级联错误。
### 方法关键点
1. 组包前引入Inter-Channel Redistribution（ICR）机制重平衡通道能量，避免关键信息集中在少量通道；
2. 提出Interleaved Channel Grouping（ICG）策略，按步长划分隐层通道，将信息均匀分散到每个大小受限的数据包中；
3. 采用双层双分支自回归结构缩短依赖链，限制丢包引发的级联错误扩散。
### 关键结果
20%丢包率下，对比SOTA LossResilientLIC平均PSNR提升1.84dB，PSNR方差降低一个数量级；仅在均匀随机丢包场景训练即可泛化到Gilbert-Elliott信道的突发丢包场景，性能优于专门针对该场景训练的方法。
