---
title: 'RollVerify: Bridging Efficiency and Accuracy in Long-Tail Rollout Reinforcement
  Learning'
title_zh: RollVerify：解决长尾Rollout RL训练的效率与精度平衡问题
authors:
- Yongqiang Yao
- Jinru Tan
- Kaihuan Liang
- Zixin Yin
- Yazhe Niu
- Ruihao Gong
- Dahua Lin
- Ningyi Xu
affiliations:
- Shanghai Jiao Tong University
- SenseTime Research
- Central South University
- The Chinese University of Hong Kong
- Beihang University
arxiv_id: '2610.09914'
url: https://arxiv.org/abs/2610.09914
pdf_url: https://arxiv.org/pdf/2610.09914
published: '2026-10-07'
collected: '2026-10-08'
category: Training
direction: RL训练优化 · 长尾Rollout效率提升
tags:
- Rollout
- Reinforcement Learning
- Off-Policy
- Training Efficiency
- LLM
one_liner: 提出基于OPS度量的双阶段验证框架，在保留部分Rollout效率的同时达到全On-policy RL相当的精度
practical_value: '- 做LLM4Rec的RL训练（如个性化文案生成、多轮导购Agent策略优化）时，可直接复用部分Rollout+OPS双阶段验证方案，解决长尾生成样本导致的GPU
  idle问题，在不损失生成质量的前提下提升训练效率1.5x以上

  - OPS度量比基于生成步数的staleness度量更精准反映样本离轨程度，做异步RL训练、批量生成样本校验时可优先采用OPS作为样本过滤指标，比训练端重加权的修正效果更稳定

  - 先序列级后token级的分段截断思路可复用在生成式推荐的样本提纯场景，比如生成的Semantic ID序列、推荐理由文案，仅截断不符合要求的后缀无需丢弃整段，能提升30%以上的样本利用率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM RL训练（如RLHF、推理能力强化）中Rollout阶段占总耗时70%-80%，且生成的轨迹长度呈长尾分布，全同步On-policy训练会导致大量GPU气泡，资源利用率低；异步/部分Rollout方案虽然能减少气泡提升效率，但会引入stale离轨样本，导致精度下降；现有方案仅在训练阶段对离轨样本重加权，无法消除劣质样本的负面影响，亟需兼顾效率和精度的方案。

### 方法关键点
- 提出Off-Policy Shift（OPS）度量，通过当前策略和生成轨迹的行为策略的重要性比偏离1的程度，量化样本的离轨程度，比传统staleness度量和精度的相关性更高
- 设计双阶段验证流程：先序列级扫描，截断OPS超过阈值的完整段；再token级扫描，截断超出阈值的单个Token，仅保留符合OPS要求的前缀，无需丢弃整段样本，大幅提升样本利用率
- 新增条件切换策略，监控验证后的样本接受率，低于阈值（如0.5）时切回全On-policy训练，避免后期离轨样本过多导致效率反而下降

### 关键实验结果
在数学推理、工具调用、代码生成任务上测试，对比On-policy GRPO、部分Rollout基线、GSPO/SAPO/VESPO等离轨修正方案：
- Qwen3-8B上，RollVerify精度和On-policy基线持平，训练成本从98.1 GPU天降到57.5 GPU天，提速1.7x；MoE模型Qwen3-30B上同样持平精度，提速1.7x
- 上下文越长收益越高，64K上下文下，训练成本从261 GPU天降到137 GPU天，提速近2倍
- 验证overhead仅占总训练时长7%左右，几乎不增加额外负担

### 最值得记住的一句话
对离轨样本提前做截断修复，比训练阶段被动重加权的效果更好，能在几乎不损失精度的前提下最大化异步Rollout的效率收益
