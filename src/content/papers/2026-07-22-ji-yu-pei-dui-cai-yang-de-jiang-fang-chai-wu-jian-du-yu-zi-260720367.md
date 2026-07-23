---
title: Variance-reduced Domain Adaptation using Paired Sampling
title_zh: 基于配对采样的降方差无监督域自适应方法
authors:
- Andrea Napoli
affiliations:
- University of Southampton, UK
arxiv_id: '2607.20367'
url: https://arxiv.org/abs/2607.20367
pdf_url: https://arxiv.org/pdf/2607.20367
published: '2026-07-22'
collected: '2026-07-23'
category: Training
direction: 无监督域自适应 · 训练方差优化
tags:
- Unsupervised Domain Adaptation
- Variance Reduction
- Paired Sampling
- MMD
- CORAL
- Stochastic Optimization
one_liner: 提出适配域自适应分布匹配损失的配对采样SVR方法PSDA，降低梯度方差提升目标域精度
practical_value: '- 跨域推荐（如公域到私域迁移、新品冷启动）场景下，针对MMD/CORAL类域对齐损失训练不稳定问题，可直接引入PSDA的四元组配对采样逻辑，降低梯度方差避免训练震荡

  - 小batch训练资源受限场景下，无需修改原有域对齐损失，复用PSDA的线性分配配对方法即可提升域适配效果，降低调参成本

  - 跨站点/跨场景的用户/物品特征迁移任务中，可将PSDA与现有特征对齐模块结合，提升目标域的推荐/排序精度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有无监督域自适应（UDA）主流的CORAL、MMD等分布匹配损失，在小批量优化场景下梯度方差极高，易导致训练不稳定甚至效果劣于无对齐方案，且这类损失不具备有限和结构，无法直接适配传统随机方差降低（SVR）方法。

### 方法关键点
提出PSDA配对采样策略，通过构造域内+跨域样本的同步采样四元组，以最小化期望梯度方差为目标设计配对规则，可转化为线性分配问题求解，无需修改原有损失函数即可适配SVR优化。

### 关键结果数字
仿真实验验证相比同类方法梯度方差显著降低，在3个域漂移基准数据集上测试，目标域分类精度有明确提升
