---
title: Stochastic Gradient Optimization with Model-Assisted Sampling
title_zh: 基于模型辅助采样的随机梯度优化方法
authors:
- Jonne Pohjankukka
- Jukka Heikkonen
affiliations:
- University of Turku, Department of Computing
arxiv_id: '2606.27171'
url: https://arxiv.org/abs/2606.27171
pdf_url: https://arxiv.org/pdf/2606.27171
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: 深度学习训练 · 随机梯度方差优化
tags:
- Stochastic Gradient Descent
- Variance Reduction
- Model-Assisted Sampling
- Optimization
- Survey Sampling
one_liner: 结合调查抽样理论提出模型辅助采样梯度估计框架，降低随机梯度方差且兼容现有优化器
practical_value: '- 训练推荐排序、LLM4Rec、Agent大模型时，可引入梯度预测辅助模型做mini-batch采样，无需改动现有AdamW等优化器逻辑即可降低梯度噪声，提升收敛效率

  - 针对中规模输入空间的业务模型训练，可优先尝试该采样策略，超70%概率获得性能收益

  - 搭配动量类优化器训练时，接入该梯度估计器可在约一半训练轮次下达到更优泛化效果，大幅降低训练算力成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
深度学习训练依赖mini-batch SGD类方法，梯度估计存在固有噪声，需在收敛稳定性、速度、泛化性之间做权衡，现有方差降低方法与自适应优化器普遍引入额外计算开销。
### 方法关键点
1. 引入调查抽样理论视角，将数据集视为固定有限总体，mini-batch梯度视为抽样估计值
2. 接入辅助梯度预测模型构造更高效的梯度估计器，无辅助信息时可退化为均匀采样，无额外适配成本
3. 完全兼容现有各类优化器，无需改动优化器原有动态逻辑
### 关键结果
在合成数据+6个基准数据集实验中，71%~86%的实验场景下获得性能收益，中规模输入空间效果更突出；搭配AdamW等动量优化器时，仅需约一半训练轮次即可获得优于基线的泛化效果。
