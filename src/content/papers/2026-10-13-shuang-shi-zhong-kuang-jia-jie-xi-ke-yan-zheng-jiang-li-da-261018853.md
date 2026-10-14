---
title: 'Two Clocks: Why Larger Rollout Batches Learn Slower but Fail on Schedule in
  Reinforcement Learning with Verifiable Rewards'
title_zh: 双时钟框架：解析可验证奖励RL中大批次训练的效率与故障规律
authors:
- Yuante Li
- Junwei Quan
- Kai Qiu
- Kate Zhang
- Yicheng Tao
affiliations:
- Carnegie Mellon University
- University of Toronto
arxiv_id: '2610.18853'
url: https://arxiv.org/abs/2610.18853
pdf_url: https://arxiv.org/pdf/2610.18853
published: '2026-10-13'
collected: '2026-10-14'
category: Training
direction: 大模型RL训练 · 批次缩放优化
tags:
- RLVR
- GRPO
- Batch Scaling
- Training Stability
- Sample Efficiency
one_liner: 提出双时钟框架解释RLVR批次缩放的进度损失与故障规律，给出高效调度策略
practical_value: '- 调优GRPO/RLVR训练时，优先选择低于临界批次的最大rollout batch，既保样本效率又稳，临界批次可通过小范围扫批次的样本成本指数α估算

  - 吞吐量需求必须用大批次的场景，可采用「先小批量训练到接近收敛前，再切换到大批量加ratio clip」的调度策略，75%样本用大批次仍能接近最优固定批次效果

  - 平方根缩放规则下无需随批次调整故障预警阈值，直接按消耗样本数设置统一的故障触发阈值即可，大批次不会更早崩溃'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RLVR是当前大模型数学、代码、推理能力对齐的核心方案，但rollout生成成本占比极高，业界普遍通过增大rollout批次+平方根学习率缩放来降本，但多步训练（如DAPO用16步每rollout）下该规则的样本效率损失、故障规律长期缺乏统一解释，调参全靠试错。

### 方法关键点
- 提出双时钟框架，拆分进度时钟和故障时钟：平方根规则仅保留每样本一阶漂移一致，不保留进度，大批次更少更长的优化步会因曲率损失更多进度
- 提出漂移阈值假设：训练崩溃当累积漂移达固定阈值，平方根规则下故障时钟与样本数强绑定，和批次大小无关
- 给出实用批次调度策略：先低于临界批次训练保证样本效率，故障前切换到大批次兼顾吞吐量与稳定性

### 关键实验
基于Qwen2.5-Math-1.5B做GRPO实验，覆盖16倍rollout批次范围：① 超过临界批次后，样本成本指数随学习率从0.15升到0.44，即批次翻8倍最多需要多1.34倍样本达相同精度；② 无ratio clip时，512批次648步崩溃、4096批次仅80步崩溃，但两者崩溃样本量均为30-50k；③ ratio clip可让大批次崩溃延迟4倍、小批次延迟2倍，不会消除进度gap；④ 批次调度策略接近最优固定批次效果，75%样本用大批次。

### 核心结论
RLVR多步训练下平方根缩放规则保漂移不保进度，调参优先选临界批次内的最大批次，大批次可通过先小后大的调度兼顾效率与稳定
