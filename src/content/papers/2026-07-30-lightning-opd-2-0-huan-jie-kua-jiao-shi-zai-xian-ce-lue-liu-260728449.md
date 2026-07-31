---
title: 'Lightning OPD 2.0: Mitigating Style Bias in Cross-Teacher On-Policy Distillation
  for Large Reasoning Models'
title_zh: Lightning OPD 2.0：缓解跨教师在线策略蒸馏的风格偏见
authors:
- Yecheng Wu
- Song Han
- Han Cai
affiliations:
- NVIDIA
arxiv_id: '2607.28449'
url: https://arxiv.org/abs/2607.28449
pdf_url: https://arxiv.org/pdf/2607.28449
published: '2026-07-30'
collected: '2026-07-31'
category: Training
direction: 大模型训练 · 跨教师在线策略蒸馏
tags:
- On-Policy Distillation
- Knowledge Distillation
- LLM Training
- Reasoning LLM
- Style Bias
one_liner: 提出跨拟合风格残差化方法，解除OPD教师一致性约束，跨教师场景下推理性能显著提升
practical_value: '- 业务中蒸馏小规格Agent、生成式推荐模型时，若SFT数据来源混杂无法保证教师一致性，可直接复用该风格残差化trick，避免强教师反而效果退化的问题

  - 风格偏差估计方法工程实现成本极低：仅需基于token ID、归一化回复位置、参考模型surprisal构建两个查表，跨折统计平均偏差即可，无需额外训练

  - 垂直领域（电商文案生成、query理解）小模型蒸馏时，可分别选择SFT数据生成、蒸馏阶段的最优模型，无需为满足一致性重新生成SFT数据，大幅降低成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
标准On-Policy Distillation (OPD) 要求SFT数据生成模型与蒸馏教师完全一致，否则即使能力更强的教师也无法带来性能增益，但实际场景中SFT数据往往来源混杂、或两个阶段的最优模型不同，该约束很难满足，会直接导致蒸馏效果退化。

### 方法关键点
- 拆分教师与SFT参考模型的token级对数概率差为两部分：跨rollout重复出现的风格偏差项（措辞、格式、推理节奏差异）、上下文相关的有效推理信号项，仅保留后者用于蒸馏
- 采用rollout级交叉拟合，用其他折的数据构建两个查表：分别按token ID、归一化回复位置+参考模型surprisal分组的平均偏差，两者取平均作为风格偏差的无偏估计
- 从原始对数概率差中减去风格偏差得到残差信号，替换原OPD目标中的差异项，整体流程与Lightning OPD完全兼容，可离线预计算所有信号，无额外训练开销

### 关键实验
以Qwen3-30B-A3B-Thinking为跨场景教师，在Qwen3-4B-SFT、Klear-Reasoner-8B-SFT两个参考模型上验证，对比SFT基线、原版Lightning OPD、IW-OPD、TA-OPD：Qwen3-4B场景下平均数学推理提升3.1个点、代码生成提升1.4个点；Klear-Reasoner-8B场景下平均数学推理提升1.0个点、代码生成提升1.4个点，最高达到AIME 2024 82.4%、LiveCodeBench v5 63.0%的精度。

### 核心结论
跨教师OPD中教师与参考模型的差异不都是有效推理信号，仅需通过跨折统计的简单方法剔除重复出现的风格偏差，即可在不增加训练成本的前提下大幅提升蒸馏效果。
