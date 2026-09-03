---
title: 'Influence-Directed Distillation: Solving the Diversity Bottleneck in Sampled-Token
  On-Policy Distillation'
title_zh: 基于影响导向蒸馏解决采样token on-policy蒸馏的多样性瓶颈
authors:
- Run Yang
- Runpeng Dai
- Jie Sun
- Jielei Zhang
- Fan Zhou
- Hongtu Zhu
- Peiyi Li
- Longwen Gao
affiliations:
- BiliBili.Inc
- University of North Carolina at Chapel Hill
- University of Science and Technology of China
- Shanghai University of Finance and Economics
arxiv_id: '2608.29846'
url: https://arxiv.org/abs/2608.29846
pdf_url: https://arxiv.org/pdf/2608.29846
published: '2026-08-29'
collected: '2026-09-03'
category: Training
direction: 大模型训练 · 知识蒸馏优化
tags:
- Knowledge-Distillation
- On-Policy-Distillation
- LLM-Training
- Entropy-Optimization
- Diversity-Preservation
one_liner: 提出仅依赖采样token教师信号的IDA-OPD蒸馏方法，低成本解决on-policy蒸馏多样性塌陷问题
practical_value: '- 蒸馏垂直场景小模型（如电商文案生成、Agent推理小模型）时，可直接复用IDA-OPD方法，无需全词表教师logit，大幅降低蒸馏成本同时保留生成多样性

  - 业务场景需要多样输出（如推荐多样化召回query、广告多版本文案）时，可借鉴一阶局部熵影响指标判断更新对多样性的影响，避免盲目加全局熵正则

  - 可复用低差异区域梯度收缩思路，在RLHF/PPO训练小模型时，对师生差异极小的token做梯度衰减，避免熵塌陷同时不损失精度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
采样token on-policy蒸馏（OPD）仅需教师对学生采样token的概率，成本远低于全词表蒸馏，已被GLM-5、Qwen3等大模型流水线采用，但存在严重多样性塌陷问题：学生pass@1提升但pass@k停滞，无法继承教师生成多样性；现有保多样性方法要么需要全词表教师信号成本极高，要么全局加熵正则会损失精度。

### 方法关键点
- 提出一阶局部熵影响（$I_H(y)$）指标，将单步更新对熵的影响拆解为师生对数概率差（优势$A_y$）和学生局部分布结构$D_y$的乘积，可精准识别熵收缩/扩张的更新
- 发现熵收缩主要集中在师生差异极小的低discrepancy区域，这类更新单步熵损失极小但数量极大，是熵塌陷的核心来源
- 提出IDA-OPD：对熵扩张更新保留原优势，对熵收缩更新用师生差异自适应权重衰减优势，差异越小衰减越强，仅需采样token的教师信号，无额外计算成本

### 关键实验结果
在数学推理、代码生成两个领域的蒸馏实验中，对比vanilla OPD，IDA-OPD在pass@1基本持平的前提下，pass@16最高提升8.3个百分点，性能持平需要全词表信号的SOTA方法，计算成本降低90%以上。

**最值得记住的一句话**：on-policy蒸馏的多样性塌陷并非来自高差异的核心学习信号，而是海量低差异、低价值的更新持续消耗熵导致的，精准衰减这类更新即可低成本保多样性。
