---
title: 'StableVQ: Practical Guidelines for Stable Vector-Quantized Tokenizer Training'
title_zh: StableVQ：向量量化Tokenizer稳定训练实用指南
authors:
- Bao Tang
- Jiahao Guo
- Haoxiang Cao
- Wenyu Liu
- Changqian Yu
- Kun Gai
- Xinggang Wang
affiliations:
- Huazhong University of Science and Technology
- KlingAI Research
- South China Normal University
arxiv_id: '2609.26774'
url: https://arxiv.org/abs/2609.26774
pdf_url: https://arxiv.org/pdf/2609.26774
published: '2026-09-21'
collected: '2026-09-23'
category: Training
direction: VQ Tokenizer · 训练稳定性优化
tags:
- VQ
- Tokenizer
- Training Stability
- Codebook
- Discrete Representation
one_liner: 推出无额外参数的StableVQ训练范式，解决VQ Tokenizer训练不稳定、码本利用率低问题
practical_value: '- 做生成式推荐Semantic ID离散化时，可直接复用Dynamic STE、Region VQ Loss无参trick，大幅提升VQ训练稳定性与码本利用率，避免码本坍塌问题

  - 多模块耦合训练场景（如用户建模+召回联合训练、多模态特征融合）可借鉴解耦学习率调度思路，给不同子模块分配独立学习率策略，降低训练崩溃概率

  - 电商多模态内容生成（商品图生成、图文匹配特征Token化）场景可直接用StableVQ替换现有VQ模块，无需修改原有模型结构即可提升Tokenizer重建质量与鲁棒性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有共享投影码本的VQ Tokenizer训练稳定性差，核心诱因是编解码器与码本训练深度耦合，仅当两个子系统恰好适配时才能正常工作，高压训练场景下极易崩溃，相关优化方向此前研究不足。

### 方法关键点
StableVQ无额外可学习参数，包含三大核心设计：1）Dynamic STE修正编码器学习目标的不稳定性，即使码本利用率低也能在离散正则下鲁棒优化重建空间；2）Region VQ Loss重构码本学习目标，可独立跟踪编码器输出分布，无需依赖编码器振荡驱动激活；3）Decoupled Schedule为编解码器、码本分配独立学习率调度，适配不同模块的优化动力学。

### 关键结果数字
ImageNet实验验证，跨不同码本大小、初始化设置下，训练稳定性、码本利用率、重建质量均实现一致提升，无额外推理开销。
