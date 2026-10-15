---
title: 'Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher
  On-Policy Distillation'
title_zh: 面向多教师On-Policy蒸馏的跨教师防护机制：突破域路由监督局限
authors:
- Shi-Yu Tian
- Yong Liu
- Ximan Liu
- Tianrui Zhu
- Sule Bai
- Xinwei Yang
- Ruiqi Liu
- Kun-Yang Yu
- Ming Yang
- Zhi Zhou
affiliations:
- Nanjing University
- JD.com
arxiv_id: '2610.13521'
url: https://arxiv.org/abs/2610.13521
pdf_url: https://arxiv.org/pdf/2610.13521
published: '2026-10-08'
collected: '2026-10-15'
category: Training
direction: 多教师On-Policy蒸馏 梯度冲突优化
tags:
- Knowledge Distillation
- On-Policy Distillation
- Multi-Teacher Learning
- Gradient Conflict
- LLM Training
one_liner: 提出ROADMOPD跨教师防护机制，解决多教师On-Policy蒸馏的梯度冲突，高冲突场景弱势域提分超5pp
practical_value: '- 多垂直域大模型蒸馏场景（如电商场景将搜索、推荐、广告垂域大模型合并为单个推理模型）可直接复用ROADMOPD的框架，避免弱势垂域能力退化，相比传统MOPD方案高冲突场景提分超5pp

  - Token级跨教师一致性加权技巧可迁移至多模型对齐的生成任务（如推荐文案生成、RAG回答生成），通过多模型偏好匹配动态调整token损失权重，减少冲突信号的负向干扰

  - 带梯度norm保留的预防性投影方法可替换多任务排序模型中的PCGrad等事后梯度修正方案，兼顾多任务梯度冲突消解与目标任务性能保留，实测性能优于传统梯度手术方案'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多教师On-Policy蒸馏（MOPD）通过域路由将不同域数据分配给对应垂域教师监督，是合并多垂直大模型能力到单学生模型的主流方案，但传统仅做域路由的方案存在显著缺陷：不同域更新作用于共享参数时会产生严重梯度冲突，高差异域组合（如医疗+数学/代码）下弱势域性能最多暴跌14pp以上，现有梯度修正方法均未利用非路由教师的同轨迹反馈提前规避冲突。

### 方法关键点
- 跨教师引导的Token级信用分配：对比路由教师与非路由辅助教师相对于冻结参考模型的偏好一致性，动态调整每个Token的监督权重，偏好一致时放大权重，冲突时衰减权重，消解token级的冲突信号
- 预防性多教师梯度投影：参数更新前用同轨迹下辅助教师的梯度作为约束，投影掉目标域梯度中与辅助梯度冲突的分量，同时设置梯度Norm下限保留目标域有效学习信号，避免有效信号被过度消除
- 多域兼容：支持3个及以上教师场景，平均多辅助教师的一致性信号，按冲突程度顺序执行梯度投影

### 关键结果
在数学、代码、医疗3个域共11个基准测试，对比Vanilla MOPD、ExOPD等4种主流基线：高冲突场景（数学/代码+医疗）下，弱势医疗域性能比Vanilla MOPD提升5.6-8.8pp，整体性能提升0.72-2.89pp；三域联合训练场景下整体性能比最优基线高1.18pp；低冲突场景（数学+代码）也获得0.35pp的性能增益。

**最值得记住的结论**：多教师蒸馏的核心矛盾不是路由分配，而是跨教师更新的兼容性协调，利用非路由教师的同轨迹反馈做前置冲突防护，比事后梯度修正效果更优
