---
title: Planning to Learn
title_zh: 面向长期学习规划的损失函数优化方法
authors:
- Ian Osband
affiliations:
- Google DeepMind
arxiv_id: '2610.03667'
url: https://arxiv.org/abs/2610.03667
pdf_url: https://arxiv.org/pdf/2610.03667
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: 训练优化 · 损失函数设计
tags:
- Policy Gradient
- Loss Function
- Cross Entropy
- LLM Post-Training
- Supervised Learning
one_liner: 提出随剩余训练时长动态调整的horizon损失，兼顾交叉熵与策略梯度优势提升训练效果
practical_value: '- 做LLM微调/RLHF时可直接替换cross-entropy为horizon损失，仅需一行代码改动，无额外计算开销，适配平学习率训练场景

  - 处理带噪电商样本（如用户行为噪声、标注错误的商品/内容样本）时优先尝试horizon损失，其抗噪增益远高于cross-entropy

  - 优化Agent策略训练时可参考其长期学习视野的设计思路，缓解现有policy gradient的短视问题，提升策略收敛后的最终效果'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
Policy gradient是LLM post-training的核心方法，受短视问题限制（仅关注当前步更新收益，忽略对后续训练的影响），即使在无探索/标注噪声的分类场景下，精确policy gradient效果也远差于cross-entropy损失，现有损失无法兼顾当前收益与长期学习潜力。
### 方法关键点
1. 重新解构损失的长期价值：cross-entropy等价于无限训练视野下的总误差，精确policy gradient是零视野（仅当前步）的极限
2. 提出horizon损失：根据剩余训练时长截断总误差计算，训练初期更接近cross-entropy，训练末期逐渐向精确policy gradient切换，仅需一行代码修改
### 关键结果
- 固定平学习率下，在MNIST、ImageNet的ResNet-50/101、ViT-S/16任务上top-1准确率均优于cross-entropy
- 标注噪声越高，horizon损失的增益越显著；基线中精确policy gradient在ImageNet ResNet-50上仅达4.2%准确率，cross-entropy达62%，horizon损失进一步提升了cross-entropy的精度
