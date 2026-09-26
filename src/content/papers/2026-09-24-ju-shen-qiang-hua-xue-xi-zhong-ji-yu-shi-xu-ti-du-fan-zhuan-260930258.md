---
title: Temporal Gradient Inversion for Private Trajectory Reconstruction in Embodied
  Reinforcement Learning
title_zh: 具身强化学习中基于时序梯度反转的私有轨迹重构攻击
authors:
- Sudip Bhujel
- Shanghao Shi
- Ruiquan Huang
- Ning Zhang
- Yang Xiao
affiliations:
- University of Kentucky
- Washington University in St. Louis
arxiv_id: '2609.30258'
url: https://arxiv.org/abs/2609.30258
pdf_url: https://arxiv.org/pdf/2609.30258
published: '2026-09-24'
collected: '2026-09-26'
category: Agent
direction: 具身Agent · 梯度隐私攻击
tags:
- Reinforcement Learning
- Privacy Attack
- Gradient Inversion
- Trajectory Reconstruction
- Embodied Agent
one_liner: 提出TRACE时序梯度反转攻击，可从具身RL传输的梯度中高精度重构私有观测-动作序列
practical_value: '- 分布式训练/联邦学习场景下传输梯度时，需额外叠加序列感知的隐私保护机制，避免用户行为时序序列被逆向还原

  - 梯度泄露防护可针对性对本文挖掘的「时序关联特征」「策略头梯度结构」做梯度扰动，提升攻击成本

  - 涉及用户行为序列的端侧Agent（如购物导航Agent、端侧推荐推理Agent），梯度上传前建议加差分隐私或梯度裁剪防护'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
分布式具身RL默认仅传输梯度不上传原始数据即可保障隐私，但时序结构会放大梯度泄露风险，现有单帧梯度反转攻击无法还原完整轨迹序列。

### 方法关键点
1. 提出TRACE amortized时序梯度反转攻击，自回归地从每步策略学习梯度中重构私有观测-动作时序轨迹
2. 利用两个被现有单帧方法忽略的结构信号：连续梯度的跨时间相关性（用条件互信息界形式化）、策略头梯度结构的闭式动作恢复（熵正则足够小时可精确恢复）

### 关键结果
在未知具身场景下PSNR达18.8dB，动作恢复接近完美，每帧重构仅需3-4.5ms，性能优于所有基线，速度比优化类攻击快几个数量级；兼容RNN、Transformer等多种架构、多模态输入及大离散动作空间，现有防护需引入序列感知隐私机制才能有效防御
