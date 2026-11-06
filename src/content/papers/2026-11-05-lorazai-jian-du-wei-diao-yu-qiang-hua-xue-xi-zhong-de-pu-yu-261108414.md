---
title: Spectral and Subspace Dynamics of LoRA in Supervised Fine-Tuning and Reinforcement
  Learning
title_zh: LoRA在监督微调与强化学习中的谱与子空间动态特性研究
authors:
- Chenruo Liu
- Zihan Wang
- Yijun Dong
- Qi Lei
affiliations:
- New York University
- Institute of Science and Technology Austria
arxiv_id: '2611.08414'
url: https://arxiv.org/abs/2611.08414
pdf_url: https://arxiv.org/pdf/2611.08414
published: '2026-11-05'
collected: '2026-11-06'
category: Training
direction: 大模型高效微调 · LoRA 分阶段优化
tags:
- LoRA
- SFT
- RL
- Optimization
- Singular Spectrum
- Subspace Dynamics
one_liner: 揭示SFT与RL下LoRA动态差异根因，提出分阶段适配的优化策略提升微调性能
practical_value: '- 做LLM4Rec的SFT阶段（如商品文案生成、推荐理由生成微调）可直接复用论文配置：LoRA的A矩阵用Adam更新，B矩阵用SGD加Muon谱平坦化，稳定提升下游任务准确率

  - 做基于RLHF的推荐Agent偏好对齐（如个性化回复、推荐结果满意度优化）时，用论文RL优化配置：仅对LoRA B矩阵更新中正交于当前子空间的部分做谱平坦化，适配RL动态提升效果

  - 调参可直接复用结论：SFT用中等学习率（1e-4~1e-3量级）提升LoRA有效秩，RL用小学习率（1e-6~1e-5量级）适配基线抵消后的动态，大幅降低调参成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LoRA是SFT和RL阶段通用的高效微调方案，但两类场景下LoRA更新的低秩增量动态差异机制长期不明确，现有通用优化策略未适配场景特性，存在显著性能提升空间。

### 方法关键点
- 从奇异谱有效秩、子空间旋转两个维度量化LoRA增量动态，通过控制变量插值实验定位**组均值基线抵消**是SFT与RL动态差异的核心根因
- 基于二次多索引模型推导基线抵消对相干拟合与梯度噪声的平衡作用，解释两类场景学习率偏好差异：SFT适配中高学习率、RL适配低学习率
- 提出分阶段LoRA优化策略：SFT阶段对B矩阵全更新做谱平坦化提升有效秩，RL阶段仅对正交于当前子空间的更新分量做谱平坦化促进子空间旋转

### 关键实验
在GSM8K、MATH数学推理数据集上测试Llama-3.2、Qwen2.5系列共8个模型，对比基线Adam优化：SFT阶段最高提升2.73%准确率，RL阶段最高提升5.3%准确率，8个模型-数据集组合中6个取得最优效果。

**核心结论**：LoRA优化需适配SFT与RL的不同动态特性，通过针对性调控奇异谱分布与子空间旋转可稳定提升微调效果。
