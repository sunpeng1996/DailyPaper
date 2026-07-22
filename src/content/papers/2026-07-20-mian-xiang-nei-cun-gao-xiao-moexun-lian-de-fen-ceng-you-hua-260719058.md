---
title: Where Should Optimizer State Live? Tiered State Allocation for Memory-Efficient
  Mixture-of-Experts Training
title_zh: 面向内存高效MoE训练的分层优化器状态分配方案SkewAdam
authors:
- Nuemaan Malik
affiliations:
- Independent Researcher
arxiv_id: '2607.19058'
url: https://arxiv.org/abs/2607.19058
pdf_url: https://arxiv.org/pdf/2607.19058
published: '2026-07-20'
collected: '2026-07-22'
category: Training
direction: 大模型训练 · MoE内存优化
tags:
- MoE
- Optimizer
- Memory Efficiency
- LLM Training
- SkewAdam
one_liner: 针对MoE三类参数特性差异化分配优化器状态，将6.78B MoE训练峰值内存压到31.3GB且效果优于AdamW
practical_value: '- 训练MoE模型时可直接复用分层状态分配策略：骨干网络保留fp32动量+因子化二阶矩、专家层仅保留因子化二阶矩、路由层保留全量二阶矩，可省90%+优化器内存，降低对高显存加速卡的依赖

  - 对稀疏更新的参数组（如MoE专家、推荐系统长尾物品embedding），可验证去掉动量仅保留因子化二阶矩的效果，在不损失精度的前提下大幅降低内存开销

  - 低精度训练时，bf16权重更新加±1ULP均匀噪声的抖动随机舍入方案可直接复用，避免小更新被四舍五入抵消，提升训练稳定性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
MoE训练中优化器状态是最大内存开销项：6.78B参数MoE用AdamW训练时，优化器状态占50.6GB，是bf16权重的4倍，现有内存高效优化器均将网络视为同质结构，未针对MoE不同参数的梯度特性差异化设计，内存压缩幅度不足，无法在40GB级加速卡上运行大参数量MoE训练。

### 方法关键点
- 将MoE参数分为三类：占比5%的稠密骨干（embedding、注意力、稠密FFN）、占比95%的专家层、占比<0.01%的路由层
- 分层分配优化器状态：骨干层保留fp32动量+因子化二阶矩；专家层仅保留因子化二阶矩，移除动量；路由层保留全量fp32二阶矩，不做因子化
- 加入更新RMS截断，bf16权重写回时叠加±1ULP均匀噪声的抖动随机舍入，避免低精度更新损失

### 关键实验结果
基于OpenWebText数据集训练82M token，对比AdamW、Lion、Muon、Adafactor等基线：
- 优化器状态仅1.29GB，为AdamW的2.6%，峰值训练内存31.3GB，适配40GB级加速卡
- 验证困惑度108.4，优于原生AdamW（126.8）、Muon（120.2）、调优后AdamW（118.5）
- 路由负载均衡误差控制在1%以内，与AdamW持平

### 最值得记住的结论
MoE不是同质参数集合，针对不同参数组的梯度特性分配优化器状态的优先级，比单纯压缩总状态量的收益更高。
