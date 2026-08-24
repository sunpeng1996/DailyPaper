---
title: Difficulty-Calibrated Interpolation Paths for Conditional Flow Matching
title_zh: 面向条件流匹配的难度校准插值路径
authors:
- Airin Akter Tania
- Md Raihan Khan
affiliations:
- Khulna University of Engineering & Technology
- North Western University
arxiv_id: '2608.21286'
url: https://arxiv.org/abs/2608.21286
pdf_url: https://arxiv.org/pdf/2608.21286
published: '2026-08-21'
collected: '2026-08-24'
category: Training
direction: 生成模型训练 · 流匹配调度优化
tags:
- Flow Matching
- Generative Model
- Training Optimization
- Interpolation Schedule
- Low-Compute Training
one_liner: 根据模型训练难度动态调整条件流匹配插值调度，仅增2%开销，低算力场景效果优于固定调度
practical_value: '- 训练生成式推荐的流/扩散模型时，可复用难度校准调度逻辑：先做短预跑记录各时间步损失，将更多训练资源分配给难学的时间步，提升少迭代场景下的模型效果。

  - 该方法仅增加2%训练开销、无需修改原有训练目标，可直接嵌入现有基于CFM的生成式召回、商品文案生成管线，无额外迁移成本。

  - 低算力训大模型的场景（比如小流量业务快速迭代生成式推荐模型），可直接用该校准策略替代固定插值调度，在相同计算预算下取得更好的生成效果。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有Conditional Flow Matching（CFM）的插值路径调度均为预定义固定值，与数据、模型训练状态无关，严重影响收敛速度与生成样本质量，未利用不同时间步的回归难度差异优化训练效率。

### 方法关键点
提出难度校准流匹配（DCFM），首先用线性路径做短预跑，记录每个时间步的损失作为难度剖面，将插值调度设置为该难度剖面的分位数函数，让训练轨迹在速度最难拟合的时间步停留更久；仅新增1个超参数，不改变原有训练目标与梯度等价性，可兼容Classifier-Free Guidance，训练开销仅增加2%。

### 关键结果
在CIFAR-10、MNIST、Fashion-MNIST数据集上用相同紧凑型U-Net测试，全采样预算下CIFAR-10的FID达到最优；在大批次、少更新的低算力场景下，效果明显优于所有固定调度策略。
