---
title: 'SoftRerank: Hierarchical Soft Fusion with Candidate-Label Reranking for Long-Tailed
  Micro-Action Recognition'
title_zh: SoftRerank：面向长尾微动作识别的层级软融合与候选标签重排序方法
authors:
- Yichi Zhang
- Zhichao Xia
- Yanjun Chi
- Lingsi Zhu
- Yuefeng Zou
- Jun Yu
- Qingsong Liu
- Jianqing Sun
- Shengping Liu
affiliations:
- University of Science and Technology of China
- Unisound AI Technology Co., Ltd.
arxiv_id: '2609.08221'
url: https://arxiv.org/abs/2609.08221
pdf_url: https://arxiv.org/pdf/2609.08221
published: '2026-09-08'
collected: '2026-09-11'
category: Other
direction: 长尾分类 · 多粒度候选重排序
tags:
- Long-Tailed Learning
- Reranking
- Hierarchical Classification
- Video Recognition
- Imbalanced Data
one_liner: 提出结合层级软融合与候选标签重排序的长尾微动作识别方案，获ACMMM2026挑战赛第一
practical_value: '- 长尾分布优化的类平衡采样+逆频率重加权trick，可直接迁移到电商长尾商品/内容推荐的排序模型训练，缓解头部样本主导的bias

  - 先粗分类再条件细分类的层级分类范式，可复用在搜索推荐多阶段排序链路，降低易混淆item的识别错误率

  - 针对歧义样本的候选标签重排思路，可借鉴到广告/推荐场景的歧义Query语义匹配、相似item排序优化'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
微动作识别受样本时长极短、视觉变化弱、类别间模式相似、标签分布长尾等问题限制，现有方案对易混淆细粒度类别区分度不足。
### 方法关键点
1. 端到端全量微调InternVideo2.5，在共享视频表征上并行接入粗分类头与分组条件细粒度分类头，提升粗细粒度预测的一致性；
2. 采用类平衡采样+逆频率重加权策略，缓解长尾标签分布带来的头部类别偏差；
3. 新增轻量候选标签重排模块，基于难样本与视频-标签匹配逻辑优化易混淆细粒度动作识别，最终通过层级软融合输出结果。
### 关键结果
在MA-52数据集上F1-mean达79.99%，斩获ACM MM 2026第三届微动作分析挑战赛第一名。
