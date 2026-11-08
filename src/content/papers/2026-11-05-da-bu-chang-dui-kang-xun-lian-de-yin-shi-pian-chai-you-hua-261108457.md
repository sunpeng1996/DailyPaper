---
title: 'Adversarial Training with Large Step Sizes: Implicit Bias, Optimization, and
  Sharpness'
title_zh: 大步长对抗训练的隐式偏差、优化特性与损失锐度研究
authors:
- Yi Feng
- Andrea Paudice
affiliations:
- Aarhus University, Denmark
arxiv_id: '2611.08457'
url: https://arxiv.org/abs/2611.08457
pdf_url: https://arxiv.org/pdf/2611.08457
published: '2026-11-05'
collected: '2026-11-08'
category: Training
direction: 对抗训练 · 梯度下降优化分析
tags:
- Adversarial Training
- Gradient Descent
- Large Step Size
- Implicit Bias
- Loss Sharpness
one_liner: 揭示大步长梯度下降在对抗训练中的优化动态与三类异于标准训练的特性
practical_value: '- 训练鲁棒性召回/排序模型时，可尝试用更大的常数步长做对抗训练，隐式偏差增益不会消失，还能大幅提升训练效率

  - 用对抗训练做模型鲁棒优化时，无需强行追求统一收敛率，可根据业务场景动态设置停止阈值，降低训练算力消耗

  - 对抗训练调参时，可观测损失锐度的两阶段变化特征判断模型训练阶段，避免过早停止导致鲁棒性不足'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有对抗训练（AT）的梯度下降（GD）优化分析多聚焦小步长场景，训练效率极低，工业界几乎不会使用，亟需明确大步长下AT的动态优化规律。
### 方法关键点
先针对对抗线性逻辑回归场景，分析大步长GD的参数收敛方向（隐式偏差）与损失下降速率（优化特性），再扩展到神经网络场景，分析训练过程中损失锐度的演化规律。
### 关键结果
1. 此前仅在小步长下验证的AT与标准训练（ST）的隐式偏差差，在任意大常数步长下依然存在；
2. 与ST不同，AT的优化误差不存在统一收敛率；
3. AT的损失锐度呈两阶段动态，异于ST观测到的稳定边缘演化行为。
