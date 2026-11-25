---
title: 'Weight Scale Rebalancing: Transferable Training Recipes for Transformers'
title_zh: 权重尺度重平衡：可跨场景迁移的Transformer训练方案
authors:
- Yikun Hou
- Naomi Graham
- Alp Yurtsever
affiliations:
- Umeå University, Sweden
arxiv_id: '2611.32866'
url: https://arxiv.org/abs/2611.32866
pdf_url: https://arxiv.org/pdf/2611.32866
published: '2026-11-24'
collected: '2026-11-25'
category: Training
direction: Transformer训练 · 超参免搜索重参数化
tags:
- Transformer
- Reparameterization
- Hyperparameter Transfer
- Training Optimization
- UDV-Rebalance
one_liner: 提出UDV-Rebalance重参数化方案，无需逐模型超参搜索即可跨尺度、架构、任务迁移训练Transformer
practical_value: '- 训练垂直域LLM、生成式推荐/广告Transformer时可直接复用UDVR方案，省去逐模型扫查学习率、权重衰减的算力成本，尤其适合小算力团队快速迭代模型

  - UDVR仅增加极小的存储与计算开销，训练完成后可将UDV合并为原始权重格式，完全不影响推理速度，可直接用于线上推荐/广告排序模型的训练优化

  - 跨任务迁移特性可复用：在图文召回ViT上调好的UDVR全局超参，可直接迁移到同结构的用户行为序列Transformer、垂直域LLM，大幅减少调参工作量

  - 可参考UDVR的权重方向-尺度解耦思路，优化SwiGLU、MoE类生成式推荐模型的训练稳定性，避免训练初期loss spike问题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Transformer训练的学习率、权重衰减等超参高度依赖模型尺度、结构与任务域，每次迭代模型都需重新扫参，算力成本极高；现有重参数化方法仅降低超参敏感度，仍无法提供开箱即用的免搜索配置。
### 方法关键点
- 在Transformer天然成对的权重矩阵（Attention的Q-K、V-O，FFN的上下投影层）间插入辅助对角矩阵D，D不参与梯度更新，仅通过定期重平衡步骤更新
- 每次梯度更新后将U的列、V的行重缩放至固定范数，剥离的尺度被D吸收，实现权重方向与尺度完全解耦，保证前向增益稳定
- 仅需在小ViT模型上一次性校准2个全局超参（范数缩放系数α、学习率常数C），后续所有模型的层级学习率仅由矩阵形状推导，无需额外扫参
### 关键结果
实验覆盖CIFAR、ImageNet、DomainNet视觉任务与120M~1.3B参数GPT类语言预训练任务，对比全扫参的Vanilla、Weight Normalization、σReparam基线：
- CIFAR数据集上平均精度比全扫参Vanilla高1.55pp，比Weight Normalization高3.05pp
- 1.3B参数LLM预训练上无需扫参的效果与全扫参Vanilla持平，跨域迁移时DomainNet Sketch任务上比最强基线高8.5pp
### 最值得记住的结论
仅需小模型一次性校准超参的重参数化方案，即可覆盖绝大多数Transformer结构训练，大幅降低中小算力团队的训模成本
