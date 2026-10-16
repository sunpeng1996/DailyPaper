---
title: Baselines and Score Centering in Policy Gradient Estimation
title_zh: 策略梯度估计中的基线机制与分数中心化方法研究
authors:
- Shuo Han
- Ziqing Hu
affiliations:
- University of Illinois Chicago
- Perplexity AI
arxiv_id: '2610.22263'
url: https://arxiv.org/abs/2610.22263
pdf_url: https://arxiv.org/pdf/2610.22263
published: '2026-10-15'
collected: '2026-10-16'
category: Training
direction: 大模型RL对齐训练 · 策略梯度优化
tags:
- PolicyGradient
- RLHF
- ImportanceSampling
- LLMAlignment
- GradientEstimation
one_liner: 从协方差视角统一解释策略梯度中基线与分数中心化作用，给出RLHF训练最优实践指南
practical_value: '- 做电商商品文案、搜索query改写的RLHF对齐时，序列级重要性采样仅用同prompt分组的均值奖励作为基线即可，无需额外实现分数中心化，降低工程复杂度

  - 采用Token级重要性采样且对ratio做裁剪/截断正则时，必须加Token级分数中心化，否则梯度会引入恒定偏差，导致训练崩掉或效果不达标

  - 优化RL训练稳定性时，优先对齐训练与推理引擎的数值逻辑（精度、采样规则、Kernel实现），比调整梯度估计技巧的收益更直接

  - 若单prompt生成样本量少（<2），可采用分数中心化+固定基线的梯度估计器，避免分组均值基线无法计算的问题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前大语言模型RL类后训练（RLHF、GRPO等）普遍采用离轨采样，训练与推理引擎的实现差异导致必须用重要性采样校正分布偏差，而工业界常用的ratio裁剪、截断等正则手段会破坏传统策略梯度对奖励常数偏移的不变性，现有分组均值基线、分数中心化等优化技巧的适用边界不清晰，易出现训练不稳定、梯度有偏的问题。

### 方法关键点
- 从协方差视角重新建模策略梯度估计目标，将奖励与加权分数的协方差作为目标，天然恢复正则化下奖励偏移的不变性，且无正则时与原始策略梯度完全等价
- 明确两类中心化方法的本质差异：分组均值基线用同批次样本均值做中心化，分数中心化用总体均值做中心化，二者均为无偏估计但方差特性不同
- 分别推导序列级、Token级两种重要性采样场景下的协方差估计性质，给出不同场景下的最优组合规则

### 关键结论（理论推导无实验）
- 序列级重要性采样下，使用分组均值基线后无需再加分数中心化，二者效果完全等价，不会引入偏差
- Token级重要性采样下，若对ratio做了正则化，不加分数中心化会引入额外固定偏差，仅当无正则时偏差消失
- 当基线足够接近方差最优基线时，分数中心化估计器的方差比分组均值基线小O(1/n²)，反之方差会无边界升高

### 核心记忆点
优先对齐训练与推理引擎的数值实现降低分布偏差，再根据重要性采样层级选择对应中心化策略，不要盲目叠加优化技巧。
