---
title: 'InstructMixup: Instruction-Guided Salient Patch Editing for Robust Data Augmentation'
title_zh: InstructMixup：指令引导显著块编辑的鲁棒数据增强方法
authors:
- Khawar Islam
- Arif Mahmood
- Xin Jin
- Naveed Akhtar
arxiv_id: '2607.19324'
url: https://arxiv.org/abs/2607.19324
pdf_url: https://arxiv.org/pdf/2607.19324
published: '2026-07-21'
collected: '2026-07-23'
category: Training
direction: 视觉模型训练 · 数据增强方法优化
tags:
- Data Augmentation
- Mixup
- Visual Model
- Robust Training
- Generative Editing
one_liner: 提出单样本内指令引导显著块编辑数据增强策略，在7个视觉基准上全面优于9种现有增强方法
practical_value: '- 电商多模态内容理解（商品图分类、违规检测等）训练可复用单样本内编辑增强思路，避免跨样本mixup破坏语义标签的问题，提升模型鲁棒性

  - 大规模商品图增强场景可采用「离线生成编辑patch缓存+训练时直接混合」的工程策略，几乎不增加训练侧开销

  - 细粒度商品分类/检索任务可借鉴自适应注入分形结构的思路，提升模型对遮挡、污损低质量商品图的泛化能力'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有mixup类数据增强需计算跨样本混合区域，开销大，且跨样本混合易破坏生成样本语义完整性，导致标签不一致，降低模型泛化能力。
### 方法关键点
1. 全流程在单样本内做增强：先用轻量显著检测器提取单样本多尺度显著块，经指令引导生成模型编辑后blend回原样本非显著区，编辑操作离线预计算缓存，训练时开销可忽略；
2. 自适应向显著区注入自相似分形结构，让样本同时携带分形与非分形特征，提升表征多样性；
3. 理论推导二阶邻域风险近似，证明方法可同时增强生成编辑不变性、抑制扰动方向曲率。
### 关键结果
在CNN、ViT、VLM等不同规模backbone、7个视觉基准上，InstructMixup优于9种现有增强方法，全面超过所有测试的最强基线。
