---
title: 'Forward-Value Discretization: Faster Stochastic Diffusion Sampling Without
  High-Order Approximation'
title_zh: 前向值离散化：无需高阶近似的快速随机扩散采样方法
authors:
- Yuchen Jiao
- Na Li
- Changxiao Cai
- Yuting Wei
- Gen Li
arxiv_id: '2611.14328'
url: https://arxiv.org/abs/2611.14328
pdf_url: https://arxiv.org/pdf/2611.14328
published: '2026-11-10'
collected: '2026-11-12'
category: Other
direction: 扩散模型 · 免训练采样加速
tags:
- diffusion_model
- sampling_acceleration
- training_free
- stochastic_sampling
- NFE_optimization
one_liner: 提出免训练前向值离散化框架，无需高阶近似即可降低随机扩散采样NFE开销，缩小与确定性采样效率差
practical_value: '- 生成式推荐中使用扩散模型生成物品/文案/Semantic ID的场景，可直接复用F-DDPM的免训练采样加速方案，不损失生成质量的前提下降低推理延迟

  - 实时生成推荐物料等低NFE预算的扩散采样场景，可优先选择一阶前向值离散化方案，无需额外训练即可实现比基线随机采样更高的效率

  - 扩散模型落地工程优化时，可参考其复用历史预测和历史注入噪声的设计思路，进一步降低单步推理的计算开销'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
随机扩散采样达到与确定性采样相当的样本质量需要远更多的NFE，理论证明高阶近似无法提升随机采样的收敛阶，现有加速方案失效。
### 方法关键点
提出免训练前向值离散化框架，基于历史预测构造前向估计点做模型评估：
1. 确定性采样场景推出F-DPMSolver，低NFE预算下提升采样质量
2. 随机采样场景推出F-DDPM，复用历史预测与已注入噪声，单步仅需1次模型推理
### 关键结果数字
在CIFAR-10、ImageNet、FFHQ、LSUN数据集上，相同NFE预算下F-DDPM的FID低于所有对比随机基线；仅需1.5倍于确定性基线的NFE，即可达到相当的采样质量，大幅缩小两类采样的效率差距。
