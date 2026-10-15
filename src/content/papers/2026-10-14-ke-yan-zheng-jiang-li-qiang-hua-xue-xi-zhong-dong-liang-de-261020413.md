---
title: When Does Momentum Help in Reinforcement Learning with Verifiable Rewards?
title_zh: 可验证奖励强化学习中动量的生效机制与调优原则
authors:
- Kaifei Wang
- Zikang Shan
- Liwei Wang
- Yinyu Ye
- Han Zhong
affiliations:
- Peking University
- Shanghai Jiao Tong University
- Stanford University
arxiv_id: '2610.20413'
url: https://arxiv.org/abs/2610.20413
pdf_url: https://arxiv.org/pdf/2610.20413
published: '2026-10-14'
collected: '2026-10-15'
category: Training
direction: LLM RL训练 · 动量系数调优
tags:
- RL_VR
- EMA
- Momentum
- Optimizer
- LLM_Post_Training
one_liner: 推导RL VR场景下EMA动量的生效条件，提出随学习率缩放动量系数的调优原则
practical_value: '- 做LLM对齐（比如Agent工具调用正确性奖励、电商商品文案生成的RLHF训练）时，可直接调高AdamW的β1参数远高于默认0.9，Qwen2.5-32B实测可涨近2个点。

  - RL训练调参时，保持η/(1-β)在安全区间（推荐≤1/(4γ)，γ是KL正则系数），随学习率缩放动量系数，能避免采样波动掩盖动量收益，提升训练稳定性。

  - 小学习率+大动量系数的组合，可在相同训练预算下降低不同种子的训练波动，适合电商/推荐线上模型的高可靠性迭代需求。'
score: 9
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
RL VR是当前提升LLM推理、对齐能力的核心技术路径，现有RL VR训练普遍直接沿用预训练阶段的默认动量配置，已有实证结果显示常规动量设置在RL VR中收益不稳定甚至会造成性能下降，亟需明确动量的生效机制与可落地的调优规则，解决采样波动导致动量收益被掩盖的问题。
### 方法关键点
- 采用KL正则的响应级bandit建模RL VR过程，分析带偏差校正EMA动量的自然策略梯度更新动态，推导得出β的安全区间避免优化过冲。
- 证明固定EMA系数β时，随学习率η下降动量的期望收益衰减速度快于采样波动，导致收益不可观测；提出随学习率缩放β，保持η/(1-β)为安全区间内的常数，可获得不随学习率衰减的稳定收益。
- 证明大β搭配小学习率的组合，可在相同训练、采样预算下实现更低的训练方差，且性能与常规配置相当甚至更优。
### 关键实验
- 10臂bandit模拟验证：缩放β配置的信噪比是固定β=0.9的80倍以上，胜率接近100%。
- Qwen3-4B-Base GRPO训练：SGD-EMA调大β到0.9992、AdamW调β1到1-1e-6，相比默认β=0.9，验证集准确率提升4-5个百分点；小学习率+大β配置的训练方差比常规配置低30%以上。
- Qwen2.5-32B GRPO训练：仅将AdamW的β1从0.9提升到1-1e-9，验证集准确率从44.3%提升到46.1%，涨近2个百分点。
### 核心结论
RL VR场景下无需额外成本，仅增大动量系数并保持η/(1-β)在安全区间，即可实现性能提升与训练稳定性优化。
