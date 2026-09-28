---
title: 'MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation'
title_zh: MOPD-Router：多教师在线蒸馏的无领域标签Token级路由框架
authors:
- Tianze Xu
- Yanzhao Zheng
- Zhentao Zhang
- Yuanqiang Yu
- Chao Ma
- Jihuai Zhu
- Lelun Wu
- Lyumanshan Ye
- Pengfei Liu
- Baohua Dong
affiliations:
- Shanghai Jiao Tong University
- Alibaba Group
- Shanghai Innovation Institute
- GAIR
- University of Science and Technology of China
arxiv_id: '2609.30837'
url: https://arxiv.org/abs/2609.30837
pdf_url: https://arxiv.org/pdf/2609.30837
published: '2026-09-24'
collected: '2026-09-28'
category: Training
direction: 多教师在线蒸馏 · 无标签动态路由
tags:
- MOPD
- On-Policy Distillation
- Knowledge Distillation
- LLM Training
- Token-level Routing
one_liner: 无需领域标签或独立路由模型，Token级动态加权多教师OPD信号提升蒸馏效果
practical_value: '- 多专家LLM蒸馏时可复用该框架，无需人工标注领域标签或额外训练路由模型，大幅降低多能力融合的训练成本

  - 生成式推荐的多维度信号融合场景可借鉴ExpertAlign思路：对用户兴趣、商品属性、文案规范等多源专家信号，按当前生成位置与各信号专长的对齐度动态加权，替代硬规则分配权重

  - Agent多工具调用结果融合场景可复用Novelty metric设计，仅在模型共同高概率支持的候选集上计算差异，过滤无效跨域信号干扰

  - 业务中多专家路由无需局限于Query级硬分配，Token/候选级动态路由可充分挖掘跨域专家的互补价值，效果优于固定路由'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多教师在线蒸馏（MOPD）依赖prompt级领域标签硬路由，一是现实中大量混合训练数据无可靠领域标签，二是固定单教师全程监督浪费了其他教师在单个Token上的互补监督信号，无法适配混合技能生成场景的需求。

### 方法关键点
- 提出MOPD-Router框架，无需领域标签或独立路由模型，在每个Token位置对全教师池的OPD信号动态加权，支持插件式路由metric扩展
- 实现3种路由metric：Entropy基于教师预测置信度加权，Novelty基于师生在共享高概率候选集上的分布差异加权，ExpertAlign基于教师校正方向与自身专长方向的正余弦相似度加权，仅保留对齐度为正的教师信号
- 训练时先计算每个教师的Token级OPD优势，按路由权重聚合后用PPO风格的clip损失更新学生模型

### 关键实验
在无标签混合数据的同规模蒸馏场景下，ExpertAlign比Mean聚合总得分高5.88（+12.3%）；在有领域标签数据上，不使用标签的ExpertAlign比标准MOPD高3.95（+7.8%），训练端到端开销仅比标准MOPD高18%，覆盖强到弱、同规模两种蒸馏场景效果均最优。

### 最值得记住的结论
Token级动态路由能充分挖掘跨域教师的互补监督信号，效果优于依赖prompt级领域标签的硬路由，且不需要额外训练独立路由模块。
