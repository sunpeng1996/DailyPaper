---
title: 'REWEAVE: Online Learning for Workload-Adaptive HNSW Indexes'
title_zh: REWEAVE：面向工作负载自适应HNSW索引的在线学习方法
authors:
- Minghao Li
- Nick Koudas
- Raghav Mittal
affiliations:
- University of Toronto
- The University of Texas At Arlington
arxiv_id: '2611.16060'
url: https://arxiv.org/abs/2611.16060
pdf_url: https://arxiv.org/pdf/2611.16060
published: '2026-11-11'
collected: '2026-11-13'
category: Other
direction: 向量检索 · HNSW索引自适应优化
tags:
- HNSW
- ANN Search
- Vector Database
- Online Learning
- Workload Adaptation
one_liner: 通过查询反馈在线重连HNSW底层边，固定度数预算下大幅提升检索召回与吞吐量
practical_value: '- 电商/推荐向量召回模块可直接复用边重连逻辑：固定HNSW度数预算下，基于真实查询反馈调整底层边，无需额外存储即可提升偏斜查询分布下的召回率

  - 反馈机制可迁移：混合精确+自监督反馈模式下，仅用10%的精确查询样本即可恢复55%的全量精确反馈增益，大幅降低标注成本，适配少标注业务场景

  - 工程trick复用：新增Missed-Neighbor Buffer补全搜索遗漏的真实近邻候选，搭配UCB导航+宽beam训练，推理阶段无额外开销即可提升召回

  - 适配query漂移场景：电商大促、换季等查询分布漂移场景下，开启时间折扣的动态重连，可在减少34%距离计算量的前提下将召回@100从0.745提升至0.979'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
HNSW索引仅基于语料构建，与实际业务中偏斜、动态漂移的查询工作负载不匹配，有限的度数预算被浪费在极少被访问的边上，导致召回率低、检索开销大；现有工作负载适配方案要么不修改边结构，要么无法在固定度数预算下提供效果保证。
### 方法关键点
- 五阶段在线循环：导航→奖励分配→值更新→候选收集→重连，仅修改HNSW底层0层，上层保留原始路由逻辑，训练结束后可直接用标准HNSW推理，无额外开销
- 奖励设计：支持端点奖励、召回奖励两种模式，搭配MC/TD折扣信用分配，将搜索成功的贡献回溯到上游路由边；支持混合精确+自监督反馈，降低标注成本
- 候选池设计：新增邻居缓冲和遗漏近邻缓冲两类候选池，每轮重连时每个节点保留得分最高的M条边，严格遵守原度数预算
- 理论保证：证明值估计和图稳定性，UCB导航的路由后悔界为O(logT)
### 关键实验
覆盖Amazon-ESCI电商商品嵌入、GIST-1M图像特征、T2I-10M/100M多模态嵌入4类数据集，对比原生HNSW、NGFix、NAP、CORAL等基线。核心结果：固定度数下比原生HNSW召回@100最高提升23.3pp；相同0.8召回@100下，吞吐量是NGFix的3.3倍；Amazon-ESCI漂移场景下，召回@100从0.745提升到0.979，距离计算量减少34%；仅用10%精确查询样本即可恢复55%的全量精确反馈增益。
### 核心结论
适配业务查询分布的索引优化收益远高于纯语料构建的通用索引，无需增加存储开销即可大幅提升检索性能
