---
title: '$\mathtt{DistP}$: Scaling Local-Update Training with Zero-Shot Hyperparameter
  Transfer'
title_zh: DistP：支持零样本超参迁移的本地更新分布式训练扩展框架
authors:
- Andrej Jovanović
- Alex Iacob
- Philipp Wiesner
- Christophe Roux
- Max Zimmer
- Lorenzo Sani
- Sebastian Pokutta
- Nicholas D. Lane
affiliations:
- University of Cambridge
- Zuse Institute Berlin
- CNRS - ENS PSL Research University
- Flower Labs
- Science of Fundamental AI Research Lab
arxiv_id: '2611.27808'
url: https://arxiv.org/abs/2611.27808
pdf_url: https://arxiv.org/pdf/2611.27808
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: 分布式大模型训练 · 零样本超参迁移
tags:
- Distributed Training
- Hyperparameter Transfer
- Local Update
- Zero-shot Transfer
- LLM Training
one_liner: 将DDP零样本超参迁移规则扩展到本地更新训练，无需目标规模重调即可提升模型质量
practical_value: '- 训练垂直领域LLM（电商商品理解/推荐用户建模LLM）时，可复用DistP的超参迁移规则，仅在小参数量模型上调参，直接迁移到大模型，大幅降低大模型调参的计算成本

  - 低带宽环境下采用本地更新分布式训练时，优先选择averaging作为外优化器，无需额外调外优化器超参即可实现与DDP相当的训练效果，同时降低通信开销

  - 分布式训练超参缩放可直接复用经验：扩大单worker本地batch时内学习率按√κ缩放，增加worker数量时内学习率保持不变，减少调参试错成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
本地更新训练是替代DDP的低通信开销分布式训练方案，但引入了worker数、本地步长、外优化器等额外超参，调参成本随模型规模上升急剧增加；现有DDP场景下的µP、CompleteP等零样本超参迁移方法无法适配本地更新的优化动态，缺少可直接复用小模型超参到本地更新大模型训练的通用框架。

### 方法关键点
- 提出DistP框架，将DDP的零样本超参迁移规则扩展到本地更新训练，覆盖不同worker数、本地步长、外优化器场景
- 若采用averaging作为外优化器，无需额外修正即可支持宽度、深度、本地batch、worker数、本地步长的超参迁移
- 线性外优化器（如Nesterov）无需额外修正即可支持宽度/深度迁移，自适应外优化器（如Adam）需额外对学习率和epsilon做缩放修正
- 明确两种batch缩放规则：单worker本地batch扩大κ倍时内学习率按√κ缩放，增加κ倍worker时内学习率保持不变

### 关键实验
在SmolLM多领域文本数据集上训练29.2M/162.3M/823M三种规模的Decoder-only Transformer，对比标准参数化（SP）、DiLoCo-fit基线：将小模型调优的超参迁移到823M大模型时，验证集损失相对降低8.1%，下游任务平均准确率相对提升10%，无需目标规模重调。

### 最值得记住的结论
本地更新训练优先选择averaging作为外优化器，可实现最简单的零样本超参迁移，效果优于带动量的外优化器+复杂调参的组合。
