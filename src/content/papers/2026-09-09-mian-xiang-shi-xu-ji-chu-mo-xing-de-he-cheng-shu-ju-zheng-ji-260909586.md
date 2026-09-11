---
title: Distillation of Synthetic Data for Time Series Foundation Models
title_zh: 面向时序基础模型的合成数据蒸馏技术
authors:
- Niloy Biswas
- Noureddine El Karoui
affiliations:
- Meta AI
arxiv_id: '2609.09586'
url: https://arxiv.org/abs/2609.09586
pdf_url: https://arxiv.org/pdf/2609.09586
published: '2026-09-09'
collected: '2026-09-11'
category: Training
direction: 大模型预训练 · 合成数据蒸馏优化
tags:
- Time-Series-Foundation-Model
- Synthetic-Data
- Knowledge-Distillation
- Training-Optimization
- Gradient-Variance
one_liner: 合成数据蒸馏SDD方法可降低时序基础模型预训练梯度方差，大幅提升收敛速度
practical_value: '- 电商销量、流量等时序预测场景的大模型预训练，可直接复用SDD思路，用已知合成数据的条件分布替代单轨迹真值计算损失，减少训练步数

  - 所有使用合成数据预训练的大模型（含推荐场景用户行为序列合成预训练），可借鉴Rao-Blackwell化目标优化思路，降低梯度方差加速收敛

  - 训练资源有限场景下，引入SDD损失可在不损失效果的前提下减少10%-40%训练迭代量，显著降低预训练成本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
时序基础模型（TSFM）预训练高度依赖合成时序数据，现有训练目标仅对比模型输出与单条轨迹未来真值，存在梯度方差大、收敛效率低的问题。
### 方法关键点
1. 合成数据蒸馏（SDD）直接将模型输出与轨迹的条件预测分布对比计算损失，无需生成大量轨迹样本；
2. SDD本质是训练目标的Rao-Blackwell化，可保证随机梯度期望不变，同时可证明在Loewner偏序下降低随机梯度协方差。
### 关键结果
在4M~2.5B参数量的全系列TSFM上验证，所有模型规模下验证损失收敛速度均提升；在高斯过程数据上，SDD达到或超过基线效果的同时，训练迭代量减少10%~40%。
