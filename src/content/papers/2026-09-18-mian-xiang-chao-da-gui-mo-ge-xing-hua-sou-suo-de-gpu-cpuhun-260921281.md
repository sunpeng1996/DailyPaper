---
title: Hybrid GPU-CPU Retrieval for Personalized Search at Ultra-Large Scale
title_zh: 面向超大规模个性化搜索的GPU-CPU混合检索系统
authors:
- Hao Fu
- Jichao Sun
- Baiting Zhu
- Qiaoling Liu
- Yan Shi
- Cheng Lu
- Liu Liu
- Yubo Wang
- Xin Yao
- Xiangyu Niu
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2609.21281'
url: https://arxiv.org/abs/2609.21281
pdf_url: https://arxiv.org/pdf/2609.21281
published: '2026-09-18'
collected: '2026-09-22'
category: RecSys
direction: 大规模召回 · GPU-CPU异构协同
tags:
- Embedding Retrieval
- Heterogeneous System
- GPU Serving
- Personalized Search
- Vector Search
one_liner: Meta提出异构协同检索架构，通过GPU高深度+CPU广覆盖通路解决万亿级语料个性化与规模的矛盾
practical_value: '- 召回层可直接复用分层架构：将高搜索价值的头部/小众高效用内容划入GPU通路做复杂交互预排序，海量长尾内容划入CPU通路做轻量语义匹配，平衡个性化精度、覆盖度与成本

  - GPU通路工程优化可直接落地：ANN检索、交互预排序全流程留驻GPU执行，稀疏嵌入表存CPU通过PCIe Gen5按需拉取，配合8bit量化融合内核，大幅降低CPU-GPU传输开销

  - CPU向量检索性能优化技巧可复用：用term-at-a-time顺序扫描替代document-at-a-time随机读提升缓存命中率，搭配AVX-512批量计算向量距离，实测可降低检索阶段算力89.45%

  - 容量规划可参考成本比例：相同广域向量检索负载下，GPU部署方案年成本约为CPU方案的4倍，可结合业务ROI灵活调整双通路的流量分配比例'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
万亿级用户生成内容的个性化搜索面临「个性化-规模悖论」：GPU高带宽内存无法经济地承载全量语料运行高交互性的个性化检索模型，CPU又无法在延迟约束内执行相同复杂度的交互计算，纯同构架构必须在个性化精度和内容覆盖度之间做出妥协。
### 方法关键点
- 异构双通路架构：从万亿级源语料分别筛选十亿级高搜索价值GPU语料库、规模大20倍的CPU广覆盖语料库，双通路并行检索后去重聚合送下游排序，支持独立版本发布、故障隔离、按需启停。
- GPU高深度通路：联合训练双塔检索+DeepFM交互预排序模型，融合InfoNCE检索、相关性、用户engagement多目标，ANN检索+预排序全流程留驻GPU，稀疏参数存CPU通过PCIe Gen5按需读取，单AMD MI300X卡可承载150-200QPS，P99模型侧延迟30-40ms。
- CPU广覆盖通路：独立构建百亿级嵌入索引，用分布式训练生成512k聚类中心降低扫描量，替换为TAAT顺序扫描+AVX-512批量向量计算优化性能，轻量双塔模型仅用点积做个性化匹配，控制算力开销。
### 关键结果
全系统A/B对比纯CPU基线，DCG@20提升4.51%，GSRR（有效搜索会话率）提升2.01%；双通路候选Jaccard相似度不足1%，候选差异化显著；CPU通路优化后检索算力降低89.45%；相同负载下GPU广域检索方案年成本约为CPU方案的4倍。
> 最值得记住的一句话：超大规模检索无需让单一硬件层优化互斥目标，异构通路可各自专业化、独立迭代，通过标准化候选契约协同，兼顾精度、覆盖、延迟与成本。
