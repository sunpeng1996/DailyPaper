---
title: 'Sequential Beats Joint: On the Interplay between On-Policy Distillation and
  RLVR'
title_zh: 顺序训练优于联合：On-Policy蒸馏与RLVR的互作用机制研究
authors:
- Boyan Li
- Bingsen Chen
- Chenghao Yang
- Ping Nie
- Chen Zhao
- Xi Ye
affiliations:
- University of Alberta
- New York University
- NYU Shanghai
- University of Chicago
- University of Waterloo
arxiv_id: '2609.04108'
url: https://arxiv.org/abs/2609.04108
pdf_url: https://arxiv.org/pdf/2609.04108
published: '2026-09-03'
collected: '2026-09-04'
category: Training
direction: LLM后训练 · OPD与RLVR结合
tags:
- On-Policy Distillation
- RLVR
- LLM Post-training
- GRPO
- Reasoning LLM
one_liner: 提出先OPD后RLVR的两阶段训练范式，效果超越所有单步联合融合方法
practical_value: '- 训练涉及规则化奖励（如商品点击率、Agent任务完成率）+ 大模型蒸馏的场景，优先采用两阶段顺序训练而非单步信号加权融合，避免信号干扰

  - 阶段切换可直接用前一阶段的验证集分数作为判定指标，等分数进入平台期再切换到下一阶段，能最大化最终效果

  - 用OPD作为RL的冷启动优于传统SFT，对小模型蒸馏提升更明显，可直接复用在垂域小模型（如电商客服Agent、推荐理由生成小模型）的训练流程中'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RLVR和OPD是当前大模型推理后训练的两大主流方法：RLVR用稀疏序列级奖励对齐任务目标，但样本效率低；OPD用稠密token级蒸馏信号提升学习效率，但上限受限于教师模型。现有方法均在单步内加权融合两类信号，存在严重的信号干扰问题，效果天花板低。

### 方法关键点
- 将现有OPD-RLVR融合方法统一归类为加权加和、教师调制两类单步融合范式，证明两类方法均存在参数更新方向的信号冲突
- 提出极简两阶段训练范式OPD-then-RL：第一阶段纯OPD训练，等验证集分数达标后，第二阶段切换为纯RLVR（GRPO）训练，完全避免单步内的信号冲突
- 切换判定规则：以OPD阶段的验证分数为核心指标，等分数进入平台期后再切换，保证前序阶段的能力边界扩展充分

### 关键实验
以Qwen3-8B为教师，Qwen3-1.7B/0.6B为学生，在逻辑推理（K&K、Zebra、Countdown）和数学推理（MATH-500、AMC23、AIME系列）数据集上，对比纯OPD、纯RLVR、7种单步融合方法、KDRL退火方法：
- 逻辑推理任务上pass@1平均达80.6，领先次优方法11.7个百分点，最大领先幅度达26.7个百分点
- 数学推理任务上pass@1平均达31.8，显著优于6种对比方法，和其余3种最强方法效果持平
- 0.6B小模型上同样稳定领先，逻辑推理平均pass@1达70.4，领先纯OPD21.5个百分点

### 核心结论
稠密蒸馏信号优先做能力边界扩展，稀疏奖励信号优先做分布sharpening，两类信号顺序执行的收益远大于单步加权融合
