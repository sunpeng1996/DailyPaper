---
title: Divergence controls entropy in distillation
title_zh: 大语言模型蒸馏过程中散度对模型熵的调控机制研究
authors:
- Nicolas Zucchet
- Scott W. Linderman
affiliations:
- Stanford University
arxiv_id: '2610.03529'
url: https://arxiv.org/abs/2610.03529
pdf_url: https://arxiv.org/pdf/2610.03529
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: 大语言模型蒸馏 · 熵调控机制
tags:
- Knowledge Distillation
- Entropy Regularization
- KL Divergence
- LLM Training
- Self-Distillation
one_liner: 解耦蒸馏的采样与散度选择，揭示不同散度对学生模型熵的调控规律，为蒸馏调参提供量化依据
practical_value: '- 做电商/推荐场景的轻量化LLM蒸馏（如query理解、个性化文案生成小模型）时，可根据输出需求选散度：需要高生成多样性（如推荐理由、营销文案）选forward
  KL，需要输出确定性高（如商品属性抽取、合规应答）选reverse KL，无需被序列级推导绑定散度与采样策略

  - 做Agent迭代、推荐模型自蒸馏时，避免直接使用纯reverse KL，可选择广义JS散度（λ取0.25~0.5区间）配合EMA指数滑动平均更新教师模型，有效防止熵坍缩导致的输出多样性暴跌

  - 蒸馏时需要做top-k截断降低计算量时，若要保留输出多样性，优先选择tail bucket策略而非重归一化策略，适配个性化生成类业务需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM蒸馏已成为训练轻量化模型、增强推理能力的核心手段，但散度选择、采样策略对学生模型输出熵（直接关联生成多样性、探索性）的影响机制不清晰，实践中常被序列级推导绑定散度和采样策略，无法按需调控输出熵，甚至出现熵坍缩等问题。

### 方法关键点
1. 解耦蒸馏的采样分布（on-policy/off-policy）和token级散度选择，独立分析两者对熵的影响，打破序列级推导的绑定关系
2. 提出适配语言模型softmax头的轻量化玩具模型，理论推导不同散度的熵调控规律，降低分析复杂度
3. 覆盖三种主流蒸馏场景：预训练/监督微调、跨模型知识蒸馏、自蒸馏，全面验证理论结论的普适性

### 关键结果
在OLMo 2、Qwen3、OLMo3等系列模型上实验验证：
1. 预训练/SFT场景下，收敛模型的平均熵与训练交叉熵损失完全相等，大模型收敛后熵更低
2. 知识蒸馏场景中，散度对熵的影响幅度是采样策略的2~3倍，forward KL会抬升学生模型熵，reverse KL会降低熵
3. 自蒸馏场景下，纯reverse KL会触发熵坍缩，广义JS散度λ取0.5左右配合EMA教师更新可稳定熵，性能波动小于2个百分点

### 核心结论
蒸馏时散度是独立的熵调控旋钮，无需与采样策略绑定，可根据业务对输出多样性的需求灵活选择。
