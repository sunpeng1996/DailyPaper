---
title: 'BoT-GRPO: Efficient Process-Reward RL for Reasoning via Bag-of-Token Aggregation'
title_zh: BoT-GRPO：基于词袋聚合的高效过程奖励RL推理训练算法
authors:
- Yingxiang Yang
- Weihang Xiao
- Zhunxuan Wang
- Joshua Flashner
- Niresh Agarwal
affiliations:
- Amazon AGI
- Virginia Tech
arxiv_id: '2610.09804'
url: https://arxiv.org/abs/2610.09804
pdf_url: https://arxiv.org/pdf/2610.09804
published: '2026-10-07'
collected: '2026-10-08'
category: Training
direction: LLM推理训练 · GRPO优化 过程奖励
tags:
- GRPO
- Reinforcement Learning
- Process Reward
- Token-level Credit Assignment
- LLM Training
one_liner: 无critic的GRPO扩展算法，通过长度不变的词袋聚合token级奖励，大幅提升RL训练收敛速度与最终效果
practical_value: '- 现有GRPO训练管线可直接替换为BoT-GRPO，只要能拿到token/step级奖励就能获得1.5~1.9倍的收敛速度提升，无需额外引入value
  network，工程改造成本极低

  - 奖励设计优先选择稳定有界的信号：全局业务目标（比如点击率、文案转化效果）权重远大于局部token/step级辅助奖励，既能加速收敛，又能避免奖励漂移和reward
  hacking问题

  - 生成类任务（商品文案、推荐理由、Agent话术）的奖励栈可复用其分层设计：免费规则检查为基础，轻量LLM judge做必选质量校验，高成本VLM/大模型judge仅作为可选高阶优化，大幅降低训练阶段的judge调用成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前GRPO是LLM推理能力RL训练的主流算法，但它给整条序列所有token分配相同的优势信号，粗粒度信用分配导致收敛慢、GPU成本高；过程奖励（PRM）虽能提供更细的监督信号，但现有方案要么需要额外训练value network/奖励模型，要么引入极大额外成本，无法兼顾训练效率和落地成本。

### 方法关键点
- 提出无critic的BoT-GRPO，可直接替换原生GRPO：将所有rollout的token级奖励汇聚为词袋，每个token按所属序列长度的倒数加权，计算长度无关的组统计量，避免长序列主导基线计算，解决原生GRPO的长度偏差问题，额外计算开销仅为O(总token数)
- 奖励设计遵循全局主导原则：token级奖励=全局结果奖励（高权重）+局部step/token辅助奖励（低权重），局部奖励需有界、与任务成功正相关，避免大幅改变原有优化目标导致的漂移
- 针对不同任务给出可落地的奖励构造方案：代码生成用静态检查+LLM代码judge+可选VLM视觉judge，数学推理用步骤正确性评价+错误传播机制（第一步错误后后续步骤奖励清零）

### 关键实验
在React代码生成和AIME数学推理两个任务上验证，对比基线包括原生GRPO、GSPO、DAPO、PURE等主流GRPO变体：React代码生成任务上，BoT-GRPO达到80%编译率的速度比原生GRPO快1.9倍，最终VLM pairwise胜率对GRPO达62%~90%；AIME数学推理任务上，Pass@2相对GRPO提升8.1个绝对百分点，收敛步数仅为GRPO的一半，效果提升在3个不同基座模型上均稳定存在。

### 最值得记住的一句话
奖励稳定性比丰富度更重要，干净、有界、稳定的细粒度信号能持续加速学习，而噪声更大的备选信号反而会导致训练停滞
