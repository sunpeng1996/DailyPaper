---
title: 'Dr. OPD: Learning What to Follow for Optimal On-Policy Distillation of Large
  Language Models'
title_zh: Dr. OPD：大模型最优On-Policy蒸馏的token级权重自适应方法
authors:
- Zhenyu Wang
- Tianze Wang
- Linjun Zhang
- Yifan Hu
affiliations:
- Rutgers University
arxiv_id: '2609.38025'
url: https://arxiv.org/abs/2609.38025
pdf_url: https://arxiv.org/pdf/2609.38025
published: '2026-09-29'
collected: '2026-09-30'
category: Training
direction: 大模型训练 · On-Policy蒸馏优化
tags:
- On-Policy Distillation
- Knowledge Distillation
- Bilevel Optimization
- LLM Training
- Token Weighting
one_liner: 通过双层优化自适应调整On-Policy蒸馏的token级权重，提升学生模型表现甚至超越教师
practical_value: '- 垂直领域小模型（如电商客服、商品文案生成模型）蒸馏可复用token加权思路：无需全量对齐大模型输出，仅给对业务指标（应答准确率、文案转化率）有增益的token分配高权重，降低蒸馏成本同时提升效果

  - 现有OPD蒸馏管线改造成本极低：仅需基于业务reward计算token credit，通过JVP高效计算无需存储全量参数梯度，额外算力开销可忽略

  - Agent能力蒸馏可借鉴该逻辑：无需强行对齐大Agent的所有思考步骤，仅保留对任务完成有帮助的步骤监督，避免无效对齐拉低小Agent性能'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统On-Policy蒸馏（OPD）对所有token的教师信号赋予相同权重，但不同token的监督价值差异极大：比如数学题的关键推理步骤纠错能直接提升正确率，而同义表述差异对最终结果无影响，全量对齐反而会引入无效信号甚至拉低学生模型性能，需要自适应判断哪些教师信号值得学习。

### 方法关键点
- 构造双层优化框架Dr. OPD：下层是带token权重的加权OPD训练学生模型，上层优化token权重以最大化学生模型的最终任务奖励
- 设计高效迭代求解器：交替更新token权重和学生模型，权重更新有闭式解，无需额外训练权重预测模型；用JVP（雅可比向量积）批量计算token credit，避免显式存储每个token的参数梯度，算力开销极低
- 权重更新逻辑：基于教师信号梯度与任务奖励梯度的对齐度计算token credit，credit为正说明该token对齐教师能提升奖励，赋予高于1的权重，反之降低权重，同时做权重截断保证训练稳定

### 关键实验
在数学、代码两个任务上覆盖强到弱、同尺寸两种蒸馏设置，对比OPD、ExOPD、GRPD、OPD+GRPO四个基线：强到弱蒸馏下，将Qwen3-4B蒸馏到Qwen3-1.7B，数学平均准确率比vanilla OPD高9.7个百分点，甚至超过4B教师模型（35.0 vs 34.1）；同尺寸蒸馏下，比vanilla OPD高2.3-3.0个百分点，稳定超过RL训练的同尺寸教师。

### 最值得记住的一句话
蒸馏的核心目标是提升学生的最终任务性能，对齐教师只是手段而非目的，不需要盲目对齐所有教师信号。
