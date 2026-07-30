---
title: 'PSG: Pair-Space Generation for Efficient Generative Reranking'
title_zh: 面向高效生成式重排的对空间生成框架PSG
authors:
- Chao Feng
- Li Ma
- Xiancheng Gao
- Chenghao Zhang
- Yuanhao Pu
- Xiang Li
affiliations:
- Kuaishou Tech
arxiv_id: '2607.26427'
url: https://arxiv.org/abs/2607.26427
pdf_url: https://arxiv.org/pdf/2607.26427
published: '2026-07-29'
collected: '2026-07-30'
category: GenRec
direction: 生成式推荐 · 生成式重排效率优化
tags:
- Generative Reranking
- Autoregressive Decoding
- Pair Token
- GRPO
- Efficiency Optimization
one_liner: 将生成式重排解码单元从单item替换为有序item对，无损效果下实现1.83倍解码提速、4倍误差上限优化
practical_value: '- 生成式重排/推荐的低延迟优化可直接复用pair粒度解码思路，k=2是工业场景的最优权衡，在不损失表达能力的前提下将解码步骤减半，适配30ms级的线上延迟约束

  - Pair Token动态表示方法可复用：基于单item embedding+位置角色嵌入实时生成pair embedding，无需维护静态n²大小的embedding表，彻底解决大词汇表稀疏和存储问题

  - 三阶训练范式可迁移到其他RL引导的生成式推荐场景：先做pair语义预训练打底，再用NTP做自回归监督，最后用GRPO做序列级reward对齐，平衡拟合性与探索性

  - 工程优化trick：pair编码模块与用户行为编码器数据独立，可并行调度执行，额外开销仅3%，几乎不增加端到端延迟'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级生成式重排普遍采用Auto-Regressive (AR) 架构实现序列生成，存在两个核心瓶颈：一是解码延迟随输出序列长度线性增长，受线上30ms级的严格延迟约束，只能生成少量候选序列，限制了探索空间；二是teacher-forcing训练范式导致训练-推理分布不匹配，累计预测误差随序列长度上升，严重劣化推荐效果。
### 方法关键点
- 重构生成粒度：将生成原子从单个item升级为有序item对，解码步骤从L降至L/2，且pair空间与原item空间是双射关系，完全不损失表达能力
- 动态Pair Token表示：基于预训练的pair编码器，用单item embedding加可学习的位置角色嵌入实时生成pair embedding，避免静态n²大小词汇表的稀疏与存储问题；pair编码可与用户行为编码器并行执行，额外开销仅3%
- 三阶训练策略：先基于海量曝光日志做pair语义预训练，再在pair空间做Next Token Prediction (NTP) 自回归监督，最后用Group Relative Policy Optimization (GRPO) 对齐序列级业务目标，兼顾拟合精度与探索性
### 关键结果
离线在ML-1M、Amazon-Books、快手工业数据集RecFlow上，NDCG@6相比SOTA基线GoalRank最高提升8.38%；线上在快手4亿DAU的短视频feed场景A/B测试，用户人均停留时长提升0.178%，解码速度达1.83倍，单容器QPS提升79.8%，理论上累计误差的最坏边界优化近4倍。

**最值得记住的一句话**：生成式推荐的效率优化无需局限于硬件升级、算子优化等底层手段，调整生成粒度的范式创新可同时获得延迟与效果的双重收益。
