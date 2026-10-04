---
title: 'Zero Flux: Flow-Based Comparison of High-Dimensional Discrete Distributions'
title_zh: Zero Flux：面向高维离散分布的流基准比较方法
authors:
- Leyang Wang
- Yakun Wang
- Song Liu
- Taiji Suzuki
affiliations:
- Department of Mathematical Informatics, The University of Tokyo
- Center for Advanced Intelligence Project, RIKEN
- School of Mathematics, University of Bristol
arxiv_id: '2610.01472'
url: https://arxiv.org/abs/2610.01472
pdf_url: https://arxiv.org/pdf/2610.01472
published: '2026-10-01'
collected: '2026-10-04'
category: Other
direction: 高维离散分布差异度量 · 流模型扩展
tags:
- Distribution Comparison
- Flow Matching
- Discrete Distribution
- Distribution Shift
- Sample Efficient
one_liner: 将连续域流匹配分布比较方法扩展到离散域，提出零通量准则衡量高维离散分布差异
practical_value: '- 可用于电商推荐场景的用户行为分布、商品类目分布漂移监控，高维离散场景下比传统统计指标鲁棒性更强

  - 可复用其局部差异分解思路，用于AB实验中实验组/对照组的离散特征分布一致性校验，快速定位差异维度

  - 可迁移样本高效估计方法，解决小流量实验下高维离散特征分布差异无法准确衡量的问题'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
高维离散分布比较面临状态空间指数膨胀、变量交互关系复杂的痛点，现有连续域流匹配分布比较方法无法直接适配离散场景，传统离散分布差异指标对离散结构建模方式敏感，鲁棒性不足。
### 方法关键点
将连续域流匹配的零向量场判定准则扩展到离散域，提出Zero Flux差异衡量标准：独立耦合下若中点处所有局部概率通量消失，则两个分布完全等价；将整体分布差异拆解为局部贡献之和，无需遍历全状态空间，仅通过样本即可高效估计，同时给出了有限样本下的误差边界。
### 关键结果
在合成、真实分类数据实验中验证：可可靠恢复稀疏依赖信号，高维场景下分布漂移追踪稳定性显著优于传统离散分布差异指标。
