---
title: 'GRAS: Guided Reduced-Variance Proposals and Adaptive Selection for Training-Free
  Reward Alignment in Discrete Diffusion'
title_zh: GRAS：离散扩散无训练奖励对齐的引导降方差与自适应选择方法
authors:
- Kwanyoung Kim
affiliations:
- Gwangju Institute of Science and Technology (GIST)
arxiv_id: '2608.26585'
url: https://arxiv.org/abs/2608.26585
pdf_url: https://arxiv.org/pdf/2608.26585
published: '2026-08-27'
collected: '2026-08-29'
category: Training
direction: 离散扩散 · 无训练奖励对齐
tags:
- Discrete Diffusion
- Reward Alignment
- Training-Free
- Variance Reduction
- Sequence Generation
one_liner: 针对离散扩散无训练奖励对齐的两大痛点，提出零额外成本的GRAS方法，性能追平甚至超过奖励微调模型
practical_value: '- 生成式推荐场景用离散扩散生成候选item/文案时，可复用GRAS的无训练奖励对齐方案，避免每次换业务指标就要重训扩散模型，节省算力成本

  - 梯度引导的方差优化思路可迁移到RAG/Agent的输出校准场景，非可微业务指标（如点击率、转化率）可直接复用留一基线降方差方法

  - 自适应重采样温度机制可直接替换现有生成式推荐扩散推理的固定温度超参，适配不同去噪步的奖励分布，提升生成结果的业务指标'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
离散扩散是主流序列生成方案，现有推理时无训练奖励对齐方案存在两大缺陷：引导提议从单噪声样本估计梯度方差大，搜索阶段固定温度重采样未适配各去噪步的奖励分布差异，适配新奖励重训成本极高。
### 方法关键点
1. 可微奖励场景采用Rao-Blackwellized reveal降低梯度估计方差，非可微奖励场景采用留一基线降方差，全程无额外降噪计算成本；
2. 将每步奖励值标准化为组相对优势，推导得到自适应重采样温度替代原有固定温度。
### 关键结果
在调控DNA、蛋白质设计任务上，GRAS取得最优无训练奖励指标，性能超过所有此前无训练方法，追平甚至超过奖励微调模型，且对非可微奖励依然有效。
