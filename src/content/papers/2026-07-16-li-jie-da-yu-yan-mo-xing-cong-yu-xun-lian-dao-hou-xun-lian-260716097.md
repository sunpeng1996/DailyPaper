---
title: Understanding Reasoning from Pretraining to Post-Training
title_zh: 理解大语言模型从预训练到后训练阶段的推理能力演化
authors:
- Jingyan Shen
- Ang Li
- Salman Rahman
- Yifan Sun
- Micah Goldblum
- Matus Telgarsky
- Pavel Izmailov
affiliations:
- New York University
- Modal Labs
- University of California, Los Angeles
- University of Illinois Urbana-Champaign
- Columbia University
arxiv_id: '2607.16097'
url: https://arxiv.org/abs/2607.16097
pdf_url: https://arxiv.org/pdf/2607.16097
published: '2026-07-16'
collected: '2026-07-20'
category: Training
direction: LLM训练 · 预训练-RL算力分配
tags:
- Scaling Law
- Reinforcement Learning
- Supervised Fine-Tuning
- Reasoning
- LLM
one_liner: 基于国际象棋与数学测试床，量化预训练与RL后训练交互规律，给出跨阶段算力最优分配法则
practical_value: '- 训练域专属Agent（电商客服/商品属性推理Agent）时可参考规律分配算力：低总预算优先投预训练，高预算逐步将RL算力占比提升到20%-30%区间

  - RL对齐可按任务难度分层设计：简单任务直接用RL放大现有正确模式提升pass@1，复杂任务先补充预训练数据覆盖长尾正确样例，避免RL放大错误模式

  - 预训练loss可作为RL提升潜力的前置筛选指标，无需跑完RL全流程即可筛选高潜力checkpoint，大幅节省训练算力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM训练中预训练与RL后训练的资源分配缺乏量化指导，RL对模型策略的实际影响机制不明确，自然语言场景下可控实验成本高、行为归因难，亟需低成本受控测试床研究跨阶段推理演化规律。

### 方法关键点
- 搭建国际象棋受控测试床，复刻标准LLM训练流程：5M-1B参数模型在人类棋谱数据上预训练，在合成推理轨迹上做SFT，采用GRPO在可验证奖励的象棋谜题任务上做RL训练
- 提出联合预训练-RL scaling law：固定RL算力下，预训练loss直接预测后RL的pass@1表现；RL reward曲线斜率与预训练token数近似线性正相关
- 按任务难度拆分RL对策略的影响机制，同时在1B参数数学推理模型上验证规律的跨域迁移性

### 关键结果
- 算力最优分配上，总预算提升时RL算力占比从20%（50M模型）逐步提升到28%（680M模型），最优预训练token分配未明显偏离Chinchilla准则
- 预训练loss与固定RL算力下的pass@1相关系数最高达-0.99，RL提升斜率与预训练token数皮尔逊相关系数达+0.84
- 简单任务中RL90%以上动作为放大SFT已有的正确策略，困难任务中RL同时存在5%左右的长尾正确策略发现和20%左右的错误模式放大

**最值得记住的结论**：RL效果上限由预训练质量决定，总算力不足时优先投入预训练比过早开展RL的收益更高。
