---
title: 'How to Tame Grokking: Representation Geometry as a Control Signal'
title_zh: 如何驯服Grokking：将表示几何作为控制信号
authors:
- Maksim A Kazanskii
affiliations:
- Independent Researcher
arxiv_id: '2607.11666'
url: https://arxiv.org/abs/2607.11666
pdf_url: https://arxiv.org/pdf/2607.11666
published: '2026-07-13'
collected: '2026-07-15'
category: Training
direction: 模型训练优化 · Grokking泛化加速
tags:
- Grokking
- Regularization
- Generalization
- Representation Learning
- Transformer Training
one_liner: 通过调控隐层表示维度的GeomDR正则项，最高可将Grokking泛化启动速度提升52倍
practical_value: '- 训练电商推荐/广告场景的小样本泛化模型时，可引入GeomDR正则抑制隐层维度坍缩，加速泛化落地

  - LLM微调（如LoRA微调电商导购Agent场景）时可监控隐层表示有效维度，提前预判泛化拐点，减少训练资源浪费

  - Transformer结构的排序/召回模型长期训练不泛化时，可尝试按阶段调整GeomDR的目标维度，加快泛化启动速度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Grokking（延迟泛化）现象下模型先记忆训练数据，经长期优化才获得泛化能力，现有方案对其出现时机调控能力不足，制约小样本/低数据场景的训练效率。
### 方法关键点
1. 实验验证隐层表示维度坍缩始终发生在Grokking泛化启动之前；
2. GeomDR光谱正则项可在训练过程中动态调整隐层表示有效维度，按需调控泛化启动时机。
### 关键结果数字
在模运算、排列组合任务上，对比AdamW基准训练，GeomDR最高可将Grokking泛化启动速度提升52倍，在MLP和Transformer架构上均有一致效果。
