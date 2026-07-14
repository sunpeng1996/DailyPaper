---
title: 'Proxy Exploration and Reusable Guidance: A Modular LLM Post-Training Paradigm
  via Proxy-Guided Update Signals'
title_zh: 基于代理引导更新信号的模块化大语言模型后训练范式
authors:
- Daocheng Fu
- Rong Wu
- Yu Yang
- Xuemeng Yang
- Jianbiao Mei
- Licheng Wen
- Pinlong Cai
- Yong Liu
- Botian Shi
- Yu Qiao
affiliations:
- 上海AI实验室
- 复旦大学
- 浙江大学
- 上海交通大学
- 上海创新研究院
arxiv_id: '2607.11505'
url: https://arxiv.org/abs/2607.11505
pdf_url: https://arxiv.org/pdf/2607.11505
published: '2026-07-13'
collected: '2026-07-14'
category: Training
direction: 大语言模型后训练 · 弱到强信号迁移
tags:
- Post-Training
- Weak-to-Strong
- Knowledge Distillation
- RLHF
- Proxy Model
one_liner: 用轻量代理模型探索高奖励更新信号，跨模型迁移复用，大幅降低大语言模型后训练成本
practical_value: '- 做垂直域LLM微调（如电商文案生成、query理解模型）时，可先用小参数量代理模型做RLHF/GRPO探索最优优化方向，再把更新信号迁移到大模型，能节省70%以上训练成本，还可复用同域更新信号到多个不同尺寸的业务模型

  - 跨模型迁移更新信号时，可根据代理模型和目标业务模型的参数量差调整校准系数λ：代理模型越弱、和目标模型差距越大，λ要调得越大，避免过度更新导致性能下降，实测1.7B→8B最优λ约1.5，4B→8B最优λ约1.1，可作为业务调参基准

  - 可将不同业务场景（如搜索召回优化、商品文案生成、客服话术优化）的更新信号缓存成可复用资产，新模型上线时直接迁移已有信号，不需要每次从0做全流程RL，大幅缩短迭代周期'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM后训练方法（PPO、GRPO、OPD等）均将策略探索与分布对齐强耦合，必须在目标大模型上执行高成本的on-policy采样探索，导致优化信号无法异步生成、跨模型复用，弱模型的优化经验无法迁移给强模型，后训练成本随模型规模增长急剧抬升，多模型多业务域的迭代效率极低。
### 方法关键点
- 提出PUST框架，完全解耦更新信号探索与分布对齐阶段：用轻量代理模型作为低成本探索沙箱，先在代理模型上执行GRPO等奖励优化，得到优化前后的代理模型对。
- 不直接蒸馏优化后的代理模型，而是提取代理模型优化前后的token对数概率相对差值作为更新方向信号，该信号仅代表奖励诱导的改进方向，与代理模型绝对能力解耦，可缓存复用。
- 迁移阶段引入锚定校准机制，以目标主模型的初始策略为锚点，通过校准系数λ控制更新强度，避免过度拟合代理的弱分布，实现稳定的弱到强迁移。
### 关键实验结果
基于Qwen3系列模型在数学、代码两个域验证，对比基线为原生GRPO、OPD：
1. 1.7B小代理的更新信号迁移给8B主模型，数学域平均性能提升19.9%；4B代理信号迁移给8B主模型，数学域平均性能提升30.2%，甚至超过代理模型自身的优化增益；代码域4B→8B迁移后平均性能提升4.6%。
2. 同一份更新信号可复用迁移给1.7B/4B/8B等多个不同尺寸的主模型，迁移仅需50步收敛，相比原生GRPO的500步探索，训练效率提升90%。
### 核心结论
LLM后训练的优化信号本质是可抽象、可缓存、可跨模型迁移的相对改进方向，而非绑定特定模型的绝对分布，一次探索可多次复用，大幅降低后训练边际成本
