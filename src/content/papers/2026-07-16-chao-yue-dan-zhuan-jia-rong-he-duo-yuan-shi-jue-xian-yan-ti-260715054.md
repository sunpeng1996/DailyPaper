---
title: 'Beyond Single Expert: Harmonizing Diverse Visual Priors in MLLMs for Spatial
  Understanding'
title_zh: 超越单专家：融合多源视觉先验提升多模态大模型空间理解能力
authors:
- Xiao Lin
- Xiaohu Huang
- Kai Han
affiliations:
- The University of Hong Kong
arxiv_id: '2607.15054'
url: https://arxiv.org/abs/2607.15054
pdf_url: https://arxiv.org/pdf/2607.15054
published: '2026-07-16'
collected: '2026-07-17'
category: Multimodal
direction: 多模态大模型 · 多源视觉先验融合
tags:
- MLLM
- Visual Prior
- Multimodal Fusion
- Spatial Understanding
- Dynamic Fusion
one_liner: 提出ViPS多视觉先验框架，低开销动态融合多模型先验，提升MLLM空间理解性能
practical_value: '- 电商多模态搜索/推荐场景可复用Efficient Prior Proxy思路，低开销抽取多预训练模型的互补视觉特征，规避单模型特征偏置

  - 动态先验融合机制可迁移至多模态召回/排序模块，根据query上下文自适应融合不同视觉模型特征，提升跨场景泛化性

  - 多模型先验互补结论可指导embodied Agent视觉感知模块选型，用多轻量模型组合替代单一大视觉模型，平衡性能与推理成本'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有MLLM空间理解方案普遍仅集成单一预训练基础模型的视觉先验，忽略不同模型输出的空间先验存在互补性，导致不同任务下性能波动大，无法充分释放多源知识的增益。

### 方法关键点
提出ViPS多模型先验框架，核心包含两个模块：1）Efficient Prior Proxy：以极低推理开销生成多个不同基础视觉模型的空间先验，避免多模型并行推理的高成本；2）Dynamic Prior Fusion：实现上下文感知的多先验和谐融合与自适应注入，替代传统单视觉编码器的先验输入范式。

### 关键结果
在多个复杂空间推理、3D空间理解基准测试集上取得新SOTA性能，全面超越单专家范式的MLLM空间理解效果。
