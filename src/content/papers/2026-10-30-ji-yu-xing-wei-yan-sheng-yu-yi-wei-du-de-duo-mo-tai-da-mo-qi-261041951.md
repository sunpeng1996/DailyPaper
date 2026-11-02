---
title: Aligning MLLMs with the Latent Structure of Human Cognition via Behavior-Derived
  Semantic Dimensions
title_zh: 基于行为衍生语义维度的多模态大模型人类认知结构对齐
authors:
- Ning E
- Changde Du
- Yizhuo Lu
- Huiguang He
affiliations:
- ShanghaiTech University
- Institute of Automation, Chinese Academy of Sciences
- University of Chinese Academy of Sciences (School of Future Technology)
- University of Chinese Academy of Sciences (School of Artificial Intelligence)
- Zhongguancun Academy
arxiv_id: '2610.41951'
url: https://arxiv.org/abs/2610.41951
pdf_url: https://arxiv.org/pdf/2610.41951
published: '2026-10-30'
collected: '2026-11-02'
category: Training
direction: 多模态大模型 · 认知对齐训练
tags:
- MLLM
- Cognitive Alignment
- Semantic Embedding
- Representation Learning
- Human Alignment
one_liner: 基于470万人类标注构建66维可解释语义空间对齐MLLM，提升认知与表征一致性
practical_value: '- 可复用「人类行为标注→可解释语义维度→对齐监督信号」的pipeline，优化生成式推荐的用户感知对齐

  - 66维可解释语义维度的构建思路，可迁移到商品/内容的多维度语义标签体系建设，提升召回可解释性

  - 「最终决策+决策理由」双监督训练对齐方案，可用于优化Agent决策逻辑与用户预期的一致性'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有MLLM对齐范式仅关注输出结果的行为模仿，未对齐人类认知的内在潜在结构，模型决策逻辑与人的认知一致性差，可解释性不足。
### 方法关键点
1. 基于470万人类Odd-One-Out（三选一异常判断）标注，构建包含66个可解释维度的行为衍生语义嵌入空间，每个对象沿固定维度表征
2. 对每个判断三元组，推理最显著的决策维度，转换为基于维度的语言理据
3. 用「最终选择+符合人类决策逻辑的理由」双监督信号微调MLLM，实现认知层面的对齐
### 关键结果
- 模型与人类相似性判断的一致性显著提升，同时在标准多模态基准上保持竞争力
- 基于fMRI自然场景数据集的表征相似性分析显示，模型与人类大脑的表征对齐度明显提升
