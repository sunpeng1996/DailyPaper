---
title: 'Your LR Schedule May Not Be Principled: Effective Learning Rate Scheduling
  in Weight-Normalized Training'
title_zh: 权重归一化训练的有效学习率调度方法AIR
authors:
- Qifan Yu
- Xinyu Ma
- Xingyan Bin
- Di He
affiliations:
- ByteDance Seed
- Peking University
arxiv_id: '2610.40362'
url: https://arxiv.org/abs/2610.40362
pdf_url: https://arxiv.org/pdf/2610.40362
published: '2026-10-28'
collected: '2026-10-30'
category: Training
direction: 大模型预训练 · 学习率调度
tags:
- Learning Rate Scheduling
- Weight Normalization
- Effective Learning Rate
- MoE Pretraining
- Optimization
one_liner: 提出以有效学习率为核心的AIR调度器，在MoE预训练上较余弦调度损失降低0.01
practical_value: '- 训练电商垂域LLM、生成式推荐/广告大模型、Agent基座时，可直接替换现有余弦调度为AIR，在相同计算量下降低预训练损失约0.01，同步提升下游任务效果

  - 做大模型训练调优时，统一以ELR（名义LR/参数块范数）为调度观测指标，而非仅看名义LR，可对齐WN和WD两种训练范式的动态，减少调参成本

  - 训练资源有限无法全流程调参时，可重点优化训练后期30%步数的LR调度，复用AIR后期调度即可抹平42%~94%的早期调度差异带来的损失差距'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前权重归一化（WN）训练相比传统权重衰减（WD）在LLM预训练上可获得更低损失、更高 token 效率，但相同名义LR调度下两者训练动态差异极大，收益来源长期不明；现有LR调度仅针对名义LR设计，缺乏统一的理论调度目标，导致WN下调度效果波动极大。

### 方法关键点
- 明确有效学习率ELR（名义LR/参数块范数）是调度的核心优化目标，匹配ELR轨迹可完全对齐WN和WD的训练损失动态
- 基于WN下参数方向对齐最大化理论推导得到无约束最优1/√t衰减曲线，通过仿射变换适配有限训练周期的峰值、终止LR约束，提出AIR（Affine Inverse-square-Root decay）调度器
- 验证训练后期ELR调度的核心作用，共享后期调度可大幅衰减早期调度差异对最终效果的影响

### 关键实验结果
在128B token MoE（110M激活/4.7B总参）预训练上，对比余弦、线性等10余种主流调度器，AIR在累计LR相同的条件下，较余弦调度终端训练损失降低约0.01，下游12个任务平均得分提升0.73，且峰值LR鲁棒性最优；在500B token更大MoE（790M激活/35.7B总参）上稳定生效，下游平均得分提升1.56；共享后期AIR调度可抹平42%~94%的早期调度带来的损失差距。

### 核心结论
学习率调度的核心优化目标应该是有效学习率ELR而非名义LR，训练后期的调度对最终效果的影响远大于早期。
