---
title: Posterior Matching Distillation
title_zh: 后验匹配蒸馏：兼顾多样性与效率的扩散模型蒸馏新方法
authors:
- Hidir Yesiltepe
- Julius Berner
- Arash Vahdat
- Pinar Yanardag
affiliations:
- Virginia Tech
- NVIDIA
arxiv_id: '2611.26629'
url: https://arxiv.org/abs/2611.26629
pdf_url: https://arxiv.org/pdf/2611.26629
published: '2026-11-18'
collected: '2026-11-20'
category: Training
direction: 扩散模型蒸馏 · 生成效率与多样性优化
tags:
- Diffusion Model
- Knowledge Distillation
- Generative AI
- Training Optimization
- FID
one_liner: 提出后验匹配蒸馏PMD，解决扩散蒸馏reverse-KL模式坍缩问题，实现少步高多样性生成
practical_value: '- 电商生成式素材（商品图、营销海报、AIGC种草图）蒸馏可直接复用PMD框架，替代传统reverse-KL蒸馏方案，在4步低延迟生成的同时保留样本多样性，避免营销素材同质化

  - 蒸馏后的模型支持训练时间步内的任意步采样无需重训，可灵活适配业务端不同算力节点：高算力场景用多步生成提质量，边缘/低算力场景用少步生成保响应速度

  - 无需额外引入辅助学生score网络即可实现全条件分布监督，降低蒸馏训练的工程实现复杂度与显存开销，适合中小团队落地扩散模型轻量化'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
扩散模型原生采样步数多、推理延迟高，难以落地实时生成场景；现有基于reverse-KL的分布匹配蒸馏方法存在模式寻求偏置，为拟合主流模式牺牲样本多样性，无法满足电商营销素材等场景的多样性生成需求。
### 方法关键点
1. 提出PMD蒸馏框架，结合模式覆盖的后验采样与任意步生成能力，零群体损失下可在每个训练噪声水平恢复教师模型的干净图像全后验；
2. 通过匹配固定噪声状态下学生样本的指数重加权平均与对应教师后验均值，实现全条件分布监督，无需额外辅助学生score网络；
3. 蒸馏后的随机学生模型无需重训，即可支持训练时间步网格内的任意步采样。
### 关键结果
在SDXL和FLUX.2 [klein] 4B模型上，4步生成的FID为同类方法最优，同时在prompt对齐度、感知质量指标上达到领先或可比水平。
