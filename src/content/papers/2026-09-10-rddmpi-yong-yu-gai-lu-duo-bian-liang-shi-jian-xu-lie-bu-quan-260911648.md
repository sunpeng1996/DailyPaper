---
title: 'RDDMPI: Residual Denoising Diffusion Model for Probabilistic Multivariate
  Time Series Imputation'
title_zh: RDDMPI：用于概率多变量时间序列补全的残差去噪扩散模型
authors:
- Ramiro Valdes Jara
- David Chapman
- Adam Meyers
arxiv_id: '2609.11648'
url: https://arxiv.org/abs/2609.11648
pdf_url: https://arxiv.org/pdf/2609.11648
published: '2026-09-10'
collected: '2026-09-12'
category: Other
direction: 多变量时间序列补全 · 扩散模型应用
tags:
- Diffusion Model
- Time Series Imputation
- Residual Learning
- Uncertainty Quantification
- Probabilistic Generation
one_liner: 提出残差空间条件扩散补全框架，结合预训练确定性补全结果提升补全精度与不确定性量化效果
practical_value: '- 电商用户行为时序、销量/流量时序缺失值补全可复用基线-残差分解思路，先用轻量确定性模型输出初值，再用扩散模型修正残差，降低生成任务难度

  - 时序特征缺失场景的不确定性量化可借鉴可靠性感知条件控制机制，动态调整预训练基线信息权重，减少噪声引入的偏差

  - 推荐系统冷启动用户交互序列补全、稀疏行为序列补全场景可尝试残差扩散方案，平衡补全准确率与结果多样性'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有基于扩散的多变量时序补全方案直接在原始数据空间建模，要求去噪网络同时捕捉全局结构、时序动态与随机不确定性，任务复杂度过高，而当前成熟的确定性补全模型已能输出精度较高的初始重建结果。
### 方法关键点
1. 采用基线-残差分解思路重构概率补全任务：预训练确定性模型捕捉主信号，扩散过程仅在残差空间建模剩余不确定性，大幅简化扩散模型的学习目标，使其聚焦结构化修正而非完整信号重建。
2. 反向去噪过程同时以基线补全信号及其隐层表征为条件，搭配可靠性感知条件机制，残差生成阶段自适应控制基线信息的影响权重。
### 关键结果
在多个公开时序补全基准数据集上，重建精度、不确定性量化效果均显著优于现有主流方案。
