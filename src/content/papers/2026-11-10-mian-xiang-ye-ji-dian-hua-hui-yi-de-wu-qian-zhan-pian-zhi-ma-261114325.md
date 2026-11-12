---
title: Point-in-Time Encoders for Earnings Calls
title_zh: 面向业绩电话会议的无前瞻偏置时点文本编码器
authors:
- Alessio Brini
affiliations:
- Pratt School of Engineering, Duke University
arxiv_id: '2611.14325'
url: https://arxiv.org/abs/2611.14325
pdf_url: https://arxiv.org/pdf/2611.14325
published: '2026-11-10'
collected: '2026-11-12'
category: RAG
direction: 时序无偏检索 · 金融领域RAG优化
tags:
- DenseRetrieval
- LookAheadBias
- PointInTimeModel
- ContrastiveLearning
- RAG
- FinancialNLP
one_liner: 训练按年切分的无前瞻偏置时点编码器，在财报电话会议检索、预测任务优于通用检索器
practical_value: '- 针对时序敏感的检索/推荐场景（如电商大促前后内容检索、用户历史行为回溯评估），可借鉴按时间窗口切分训练集的编码器训练方案，消除前瞻偏置，提升离线评估的线上对齐度

  - 33.8M参数的垂直领域专属编码器检索效果优于通用检索器，垂直场景（如电商商品检索、客服问答）可优先训练小参数量专属Encoder，兼顾效果与推理成本

  - 增量续训的新版本编码器对历史数据的检索效果优于同期版本，可直接复用新Encoder优化历史语料的检索效果，无需重新标注历史数据'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有文本编码器训练会引入目标时点后的文本数据，在时序敏感的回溯测试等场景存在严重前瞻偏置，导致评估结果失真，无法对齐线上真实效果。
### 方法关键点
基于2010-2024年共412248份业绩电话会议语料，按年度设置训练截止时间窗，训练4种预训练范式的时点编码器，每个版本仅使用截止日期前的文本，再基于电话会议问答对微调。
### 关键结果
33.8M参数的领域专属时点编码器，在所有测试季度的答案检索效果优于全部被测通用检索器；将其向量加入收益预测模型，次日收益的秩相关系数提升约50%；后续时点版本编码器对更早季度的检索效果优于同期可用版本，基于其检索结果的时点LLM可继承该增益；对收益预测的提升不显著，核心价值在检索环节。
