---
title: 'DTCA: Denoising Token Credit Assignment for Reinforcement Learning in Diffusion
  Language Models'
title_zh: DTCA：面向扩散语言模型强化学习的去噪Token信用分配框架
authors:
- Hongze Chen
- Miao Pan
- Lizhou Liang
- Qinfeng Li
- Xinyin Ma
- Yongliang Shen
- Weishi Wang
- Daniel Dahlmeier
- Xuhong Zhang
- Wenqi Zhang
affiliations:
- Zhejiang University
- National University of Singapore
- SAP
arxiv_id: '2610.35201'
url: https://arxiv.org/abs/2610.35201
pdf_url: https://arxiv.org/pdf/2610.35201
published: '2026-10-25'
collected: '2026-10-29'
category: Training
direction: 扩散大模型 · RL训练信用分配优化
tags:
- Diffusion Language Model
- Reinforcement Learning
- Credit Assignment
- POS Tagging
- Mathematical Reasoning
one_liner: 基于POS分组的token级信用分配框架，提升扩散语言模型RL训练的推理性能
practical_value: '- 电商生成式推荐/Agent RL微调场景，可借鉴POS分组思路，给商品名、属性词等高价值token分配更高权重，降低无效梯度，提升RL训练效率

  - 文案生成、query改写等RLHF场景，可复用「token贡献权重+熵校准」的组合策略，既强化高价值信号又避免熵坍缩，稳定训练过程

  - 迭代改写、并行生成类业务模型，可借鉴基于置信度提升的timestep选择方法，仅优化高价值生成步，降低训练算力成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
扩散语言模型（DLM）凭借双向上下文建模、并行生成的优势成为文本生成新范式，但将RL应用于DLM时，迭代去噪的生成过程导致信用分配困难，序列级奖励无法区分不同token对最终结果的贡献，限制了RL优化的效果。

### 方法关键点
- 离线统计不同POS类别的token对后续去噪的置信度提升贡献，归一化为[0.8,1.2]的固定权重，降低token级贡献估计的方差
- 基于POS权重+token置信度计算每个去噪步的重要性，自适应选择高价值训练步，减少冗余计算
- 用POS权重为每个token分配差异化学习信号，高贡献类别token获得更大梯度
- 新增熵校准模块，根据policy更新带来的token级熵变化调整信用权重，平衡熵增/熵减更新，避免训练坍缩

### 关键实验
基于LLaDA-8B-Instruct模型，在MATH、GSM8K数学推理数据集上训练，对比RLDF、Coupled-GRPO等7种DLM-RL方法，在128生成步约束下，MATH500准确率较基线提升9.0个百分点，GSM8K提升5.3个百分点，在256、512步设置下也稳定优于基线。

### 核心结论
迭代生成模型的RL优化中，基于token语义属性分组的细粒度信用分配，可在不增加过多算力的前提下显著提升训练效率与最终效果
