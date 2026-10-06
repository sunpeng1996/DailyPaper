---
title: 'PaLoRA: Paced Low-Rank Adaptation for Continual Learning'
title_zh: PaLoRA：面向持续学习的自适应步调低秩适配方法
authors:
- Yuxuan Li
- Fanhu Zeng
- Hao Tang
affiliations:
- 北京大学
- 中国科学院自动化研究所
arxiv_id: '2610.04226'
url: https://arxiv.org/abs/2610.04226
pdf_url: https://arxiv.org/pdf/2610.04226
published: '2026-10-02'
collected: '2026-10-06'
category: Training
direction: 持续学习 · LoRA训练优化
tags:
- LoRA
- Continual Learning
- Catastrophic Forgetting
- PEFT
- Gradient Projection
one_liner: 提出秩感知自适应步调的LoRA持续学习方法，长序列任务准确率最高提升4%
practical_value: '- 电商推荐多垂类/多场景持续适配场景，可复用秩感知梯度缩放策略替代固定小学习率，基于历史LoRA更新的有效秩动态调整更新约束强度，缓解多任务灾难性遗忘

  - 多任务LoRA适配工程实现可加入自适应SVD压缩模块，定期合并历史LoRA更新并按能量阈值裁剪冗余奇异值，既降低存储开销，又能精准量化历史知识复杂度

  - 持续学习场景下可搭配easy-positive triplet loss作为辅助正则，补偿梯度投影导致的新任务学习能力下降，平衡旧知识保留与新知识获取的 trade-off'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于LoRA的持续学习方法普遍依靠固定小学习率限制梯度更新幅度来缓解灾难性遗忘，缺少理论支撑；随着任务数累积，历史知识的复杂度持续上升，固定学习率无法自适应调整约束强度，会逐渐失衡稳定性（旧知识保留）和可塑性（新知识学习），甚至无法阻止遗忘累积。

### 方法关键点
- 理论推导得出最优梯度缩放系数 `s* = √(R/c)`：R为历史LoRA更新的有效秩，c为遗忘容忍超参，梯度约束强度随历史知识复杂度的平方根自适应增长，最优平衡稳定-可塑性 trade-off
- 两阶段训练流程：学习新任务前先合并历史LoRA更新做SVD分解，按能量阈值保留Top-R奇异值压缩历史知识，同时计算历史子空间的零空间投影矩阵
- 新任务训练时，LoRA的A矩阵梯度先投影到零空间减少旧知识干扰，B矩阵梯度额外乘以`√(C/R)`做秩感知步长缩放，搭配easy-positive triplet正则补偿可塑性损失

### 关键结果
在CIFAR-100、ImageNet-R、ImageNet-A三个基准上，全任务序列准确率均优于SOTA基线；50任务长序列场景下，比LoRA-DRS高4.09个百分点（ImageNet-R）、3.99个百分点（ImageNet-A）；任务数从10增长到50时，最终准确率仅下降0.65~2.19个百分点。

**最值得记住的一句话**：LoRA持续学习中，梯度更新的约束强度应随历史知识的有效秩呈平方根级增长，才能最优平衡旧知识保留与新知识学习。
