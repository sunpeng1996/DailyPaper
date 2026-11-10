---
title: An Adaptive, Context-Aware, and Stacked Attention Network-Based Recommendation
  System to Capture Users' Temporal Preference
title_zh: 基于自适应上下文感知堆叠注意力网络的用户时序偏好推荐系统
authors:
- Jung-Hsien Chiang
- Chung-Yao Ma
- Chi-Shiang Wang
- Pei-Yi Hao
arxiv_id: '2611.11278'
url: https://arxiv.org/abs/2611.11278
pdf_url: https://arxiv.org/pdf/2611.11278
published: '2026-11-08'
collected: '2026-11-10'
category: RecSys
direction: 时序推荐 · 注意力机制用户偏好建模
tags:
- Temporal Recommendation
- Attention Network
- Context-Aware Recommendation
- Sequential Preference
- Implicit Feedback
one_liner: 提出堆叠双注意力的上下文感知推荐模型，精准捕捉用户动态时序偏好
practical_value: '- 时序窗口内的物品注意力加权方案可直接替换现有序列推荐中的平均/GRU编码，适配美妆、服饰等用户兴趣快速漂移的电商场景

  - 可按场景灵活调整模型结构：兴趣复杂的长视频/综合电商增加注意力头数与层数，稀疏短序列的内容社交/小品类电商减少层数并关闭位置编码降低过拟合

  - 采用BPR预训练初始化用户/物品embedding再微调的方案，可降低模型收敛成本，线上推理复杂度仅O(k)适配高并发场景

  - 时间窗口长度可按品类调整：决策链短的美妆/家居选2-5的小窗口，长决策链的3C/文旅选6以上的大窗口提升匹配精度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有序列推荐存在明显缺陷：RNN类方案过度关注近期行为、忽略用户长期静态兴趣，传统CF方法无法捕捉用户偏好随时间的动态漂移，且在交互稀疏的场景下表现极差，而用户兴趣变化是电商、内容平台推荐效果持续下滑的核心原因，亟需兼顾长短期兴趣、适配稀疏数据的时序推荐方案。
### 方法关键点
1. 双注意力模块设计：上下文物品注意力模块对指定时间窗口内的用户交互物品加权，输出时序上下文表征，可接入Transformer位置编码引入交互顺序信息
2. 堆叠多头部用户注意力模块：将用户embedding与上下文表征映射到多个独立子空间，捕捉用户多维度兴趣，可堆叠多层提取深层稳定偏好
3. 训练推理优化：采用BPR预训练的用户/物品embedding做初始化，成对损失训练，线上推理复杂度与矩阵分解一致，仅O(k)
### 关键实验结果
在MovieLens-100k、Pinterest、Amazon Beauty三个公开数据集上，对比BPR、NCF、NAIS、GRU4Rec、SASRec 5个SOTA基线，HR@10最高提升4.78%，NDCG@10最高提升8.21%，MRR@10最高提升10.35%；稀疏场景下表现远超GRU类序列模型，GPU推理速度比RNN类方案快5倍以上。
### 核心结论
时序推荐的性能优化核心是根据业务场景的用户交互密度、兴趣变化速度调整注意力结构和时间窗口参数，而非盲目叠加深度。
