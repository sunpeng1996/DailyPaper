---
title: 'HyperPage: Learned Page Layouts for Disk-Resident Graph Vector Indexes'
title_zh: HyperPage：面向磁盘驻留图向量索引的学习式页布局方法
authors:
- Xinyu Zhang
- Jingze Li
- Baihua Zheng
- Weiwei Sun
affiliations:
- 复旦大学
- 新加坡管理大学
arxiv_id: '2611.16149'
url: https://arxiv.org/abs/2611.16149
pdf_url: https://arxiv.org/pdf/2611.16149
published: '2026-11-12'
collected: '2026-11-13'
category: Other
direction: 向量索引优化 · 访问日志驱动
tags:
- VectorDB
- PageLayout
- DiskANN
- WorkloadDriven
- ANN
one_liner: 基于搜索Agent历史遍历日志优化磁盘向量索引页布局，较现有方案最多降21.2%页读取量
practical_value: '- 向量检索是RAG、生成式推荐召回的核心依赖，小内存预算（如成本控制的在线服务、边缘端）场景下，可参考HyperPage思路，用历史检索访问日志重排SSD上的向量索引页布局，无需修改检索逻辑即可降低I/O耗时，提升召回速度

  - 可复用其缓存感知的优化逻辑：先基于历史日志统计记录访问热度，将预算内的热记录直接放入内存缓存，仅对冷记录做页布局优化，避免将优化资源浪费在已经命中缓存的请求上

  - 其日志回放验证的思路可直接迁移到业务索引优化流程：线下回放历史请求即可评估布局优化收益，无线上风险，可快速验证落地效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
磁盘驻留图向量索引（如DiskANN）是Agent检索、RAG、大向量规模生成式推荐召回的核心组件，现有主流页布局方案仅基于图结构和向量特征设计，完全不考虑业务实际访问模式，在内存预算占索引比例较低的场景下，随机I/O开销极高，成为检索性能瓶颈；而搜索Agent训练、线上请求的历史遍历日志包含大量可复用的访问路径关联信息，此前未被用于布局优化。

### 方法关键点
- 核心验证：DiskANN类检索的遍历路径仅依赖内存中的PQ编码和已访问节点邻接表，与页布局无关，因此历史遍历日志可直接用于精准评估任意候选布局的页读取量
- 缓存感知优化：先基于历史日志统计记录访问热度，将预算内的热记录直接放入内存，仅对剩余冷记录基于历史访问的scope union做布局优化
- 多候选+回放选优：生成采用SET、CLQ、P05等不同优化目标的候选布局，在验证集上回放实际访问序列，选择最优布局和内存拆分比例
- 提供拉格朗日下界计算方法，可量化当前布局与理论最优的差距

### 关键实验
基于Search-R1 Agent的检索日志训练，在1M、21M规模的文本向量数据集上测试，对比MARGO、Starling等主流布局方案：HyperPage在7种不同内存预算下，页读取量较MARGO低5.2%~21.2%；1%小内存预算场景下，MARGO需要1.5~3倍的内存才能达到相同的页读取量；21M规模下检索单步耗时最多降低10.4%，全程不损失召回精度。

面向检索负载的索引物理层优化，在不修改检索逻辑、不损失召回精度的前提下，可实现显著的性能提升或硬件成本下降。
