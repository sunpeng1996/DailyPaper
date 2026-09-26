---
title: Intrinsic-Extrinsic Coupling in Learning Dynamics
title_zh: 学习动力学中的内-外耦合机制研究
authors:
- Qinyou Wang
arxiv_id: '2609.30185'
url: https://arxiv.org/abs/2609.30185
pdf_url: https://arxiv.org/pdf/2609.30185
published: '2026-09-24'
collected: '2026-09-26'
category: Training
direction: 大模型训练动力学 · 状态干预优化
tags:
- Training Dynamics
- Model Intervention
- Incremental Learning
- SGDW
- RoBERTa
one_liner: 提出学习动力学内外部耦合量化框架，通过可执行状态干预验证多训练场景下的耦合效应
practical_value: '- 推荐系统增量更新（新类目/新商品引入）场景可复用分类头写保护机制，避免现有logit漂移导致旧类目/旧商品的排序效果下跌

  - 训练策略选型（蒸馏、replay策略、优化器选型）时，可借鉴四细胞对照方法量化内部干预和外部训练流程的交互效应，避免盲目假设正协同

  - LLM/大模型推荐基座增量微调场景，可引入有限精度验收检查trick，平衡历史效果保留和新任务适配的性能'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有训练优化默认当前观测可完全决定后续训练响应，忽略模型内部状态与外部训练流程的耦合效应，导致增量微调、蒸馏等场景效果波动不可控。
### 方法关键点
1. 基于受限学习状态干预的延续条件价值定义内-外耦合，用observation-relative fibers描述当前表现一致性
2. 提出有限帧分类头写保护机制，在有限精度验收约束下修复历史margin同时保留当前logit
3. 设计四细胞对照实验量化内部干预与外部训练流程的非加性交互效应
### 关键结果数字
- CLINC类增量场景下，replay会让32步更新的写操作贡献从5个正确预测降为0
- SGDW优化器下128步更新时，所有3个激活根的正确数交互均为负，耦合不一定带来正协同
- 交叉熵读出上，引导分配在5组对比中平均损失均低于标准replay
