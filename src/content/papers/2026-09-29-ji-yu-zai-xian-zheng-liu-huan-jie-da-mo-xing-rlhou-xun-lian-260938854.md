---
title: Mitigating the Length-Scaling Tax with Online Distillation
title_zh: 基于在线蒸馏缓解大模型RL后训练中的长度缩放税问题
authors:
- Xu Wan
- Wenyue Xu
- Shengjie Zhao
- Mingyang Sun
affiliations:
- ByteDance Seed
- Tongji University
- Peking University
arxiv_id: '2609.38854'
url: https://arxiv.org/abs/2609.38854
pdf_url: https://arxiv.org/pdf/2609.38854
published: '2026-09-29'
collected: '2026-10-01'
category: Training
direction: 大模型RL后训练优化 · 在线自蒸馏
tags:
- Reinforcement Learning
- Online Distillation
- Length Scaling Tax
- RL Post-training
- Self-Distillation
one_liner: 提出长度自蒸馏LSD算法，在不损失推理能力的前提下大幅降低RL后训练的冗余输出长度
practical_value: '- 做Agent/LLM4Rec的RL微调时，可复用LSD的难度路由逻辑：对模型已经能100%答对的高频query（如电商常见导购问题、推荐场景固定规则类query），用EMA自蒸馏保留简洁输出，避免训练后期冗余变长，降低推理token成本

  - 可直接复用LST（长度缩放税）指标度量业务场景下模型冗余度：固定已经100%解决的query集，跟踪后续训练后输出长度的涨幅，量化不必要的token浪费，作为训练优化的核心监控指标

  - 多轮电商导购Agent的RL训练中，可参考LSD的混合损失设计：难query走RL奖励优化探索能力，易query走蒸馏保留高效交互模式，既能提升复杂问题解决率，又能减少多轮交互轮次，降低用户等待时间'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
RL后训练是目前LLM提升推理、Agent能力的核心手段，但训练过程中会出现「长度缩放税（LST）」问题：已经能完全解决的简单query的输出长度会无意义变长，没有准确率收益还大幅增加推理成本。现有全局长度惩罚方法会损失难query的探索能力，也没有针对性的量化指标和解决框架。

### 方法关键点
- 提出LST量化指标：固定锚点checkpoint下100%解决的query集，跟踪后续训练中该集合的输出长度相对最短达标长度的涨幅，避免幸存者偏差
- 设计长度自蒸馏（LSD）算法：① 在线路由：按当前batch的rollout准确率，将100%正确的query组路由到蒸馏分支，未全对的组保留原RLVR目标；② EMA自教师：用在线模型的指数滑动平均作为教师，不需要额外外部模型；③ 三种蒸馏损失实现：SG-FKL、SG-RKL、PG-RKL，适配不同的压缩-精度tradeoff需求

### 关键结果
- 单轮推理任务：基于Qwen3-4B在数学推理数据集上训练，对比基线RL，SG-FKL版本LST从19.0%降至-3.7%，Pass@1提升1.3pp，难query平均输出长度反而增加8%，不损失探索能力
- 多轮Agent任务：基于Qwen3-8B在浏览检索Agent数据集上训练，对比基线RL，SG-FKL版本LST从31.4%降至13.7%，Pass@1提升1.22pp，平均交互轮次减少3.1%

最值得记住的一句话：RL后训练中易样本的梯度消失会导致行为漂移，针对性加轻量蒸馏信号的性价比远高于全局加长度惩罚
