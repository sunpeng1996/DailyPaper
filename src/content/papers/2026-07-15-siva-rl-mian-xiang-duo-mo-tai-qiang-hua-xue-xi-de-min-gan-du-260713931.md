---
title: 'SIVA-RL: Sensitivity-Invariance Visual Alignment for Multimodal Reinforcement
  Learning'
title_zh: SIVA-RL：面向多模态强化学习的敏感度-不变性视觉对齐
authors:
- Cheng Tang
- Junzhi Ning
- Min Cen
- Wei Li
- Xinyi Zeng
- Pinxian Zeng
- Rongbin Li
- Qiming Zhu
- Yuqiang Li
- Junjun He
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Shanghai Jiao Tong University
- Sichuan University
- The Chinese University of Hong Kong, Shenzhen
- University of Macau
arxiv_id: '2607.13931'
url: https://arxiv.org/abs/2607.13931
pdf_url: https://arxiv.org/pdf/2607.13931
published: '2026-07-15'
collected: '2026-07-16'
category: Multimodal
direction: 多模态强化学习 · 视觉语言对齐
tags:
- Multimodal RL
- Vision-Language Alignment
- GRPO
- DAPO
- Intervention Learning
one_liner: 提出基于样本结果感知的多模态RL视觉对齐框架，显著提升视觉依赖推理任务性能
practical_value: '- 多模态商品理解/AI导购场景下，可复用PatchSwap局部干预方法构造负样本，提升VLM对商品视觉特征的grounding能力，避免依赖文本先验出错

  - 训练多模态推荐Agent时，可引入结果感知的软权重路由策略，对干预后reward波动大/小的样本分别做敏感度/不变性对齐，提升鲁棒性

  - 框架兼容GRPO/DAPO等主流RL训练backbone，可直接嵌入现有多模态大模型训练pipeline无过重改造'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多模态RL基于答案正确性的奖励无法保证模型预测依赖真实视觉证据，现有视觉干预方法按干预类型而非实际效果分配监督，相同干预在不同样本上效果差异大，导致监督失效。

### 方法关键点
1. 提出SIVA-RL框架，用逐样本结果感知的监督替代干预类型条件正则；2. 基于token对齐、距离约束的PatchSwap构造图像局部干预样本；3. 用冻结审计策略打分原始-干预样本对，将奖励下降幅度作为软路由权重：奖励下降大的样本做敏感度对齐（要求模型感知视觉变化），下降小的做不变性对齐（要求模型对无关视觉变化鲁棒），模糊样本降权；4. 兼容GRPO、DAPO两种RL训练backbone。

### 关键结果
在9个多模态推理基准上，3B/7B模型全场景优于匹配RL基线，视觉依赖推理任务提升8.79个百分点，GRPO/DAPO四种配置下整体相对提升最高达14.9%。
