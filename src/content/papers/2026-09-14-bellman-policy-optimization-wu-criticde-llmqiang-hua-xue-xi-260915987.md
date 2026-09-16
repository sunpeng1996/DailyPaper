---
title: Bellman Policy Optimization
title_zh: Bellman Policy Optimization：无Critic的LLM强化学习训练算法
authors:
- Zhuoqing Song
- Haotian Xu
- Xikun Zhang
- Lidong Bing
affiliations:
- Apodex US, Inc.
- Princeton University
arxiv_id: '2609.15987'
url: https://arxiv.org/abs/2609.15987
pdf_url: https://arxiv.org/pdf/2609.15987
published: '2026-09-14'
collected: '2026-09-16'
category: Training
direction: 大语言模型 · RL训练策略优化
tags:
- RLHF
- Policy Optimization
- LLM Reasoning
- Bellman Equation
- GRPO
one_liner: 基于PMD与贝尔曼方程推导无critic策略优化方法，在LLM推理任务上显著优于GRPO等主流方案
practical_value: '- 对于用RL优化Agent决策、生成式推荐文案/query的场景，可直接替换现有GRPO损失为BPO损失，无需额外训练critic模型，仅需增加互补token概率的平滑权重计算，工程改造成本极低

  - BPO的mismatch-correction权重用互补token概率比替代GRPO的重要性采样比，可缓解训练-推理分布漂移问题，可复用到所有需要token级权重调整的序列生成RL训练场景

  - 超参数可直接复用论文默认配置：平滑系数ϵ=0.1、权重上限C=3.0，对0.05-0.2的ϵ、2.0-4.0的C鲁棒性强，无需大量调参'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有RLVR（可验证奖励强化学习）是提升LLM推理能力的核心路径，主流GRPO类无critic方法依赖token级重要性采样比，易受训练-推理分布漂移影响；原始PMD（策略镜像下降）需要估计中间状态价值，额外增加计算开销且推理场景下价值估计精度低，亟需兼顾无critic、低偏差、高稳定性的策略优化方案。

### 方法关键点
- 基于贝尔曼方程对PMD做轨迹级重构，利用相邻状态价值差的telescoping性质消去中间状态价值估计需求，仅保留终端奖励与初始状态价值，初始价值通过同prompt下多采样响应的奖励均值估算
- 推导实用损失时用二元KL近似全KL降低计算量，设计加性平滑的mismatch-correction权重（互补token概率的平滑比值）替代GRPO的重要性采样比，保留GRPO的组内归一化优势、裁剪掩码逻辑，训练稳定性更优

### 关键结果
在Qwen3-30B模型上使用DAPO-Math-17k数据集训练，对比GRPO-ClipHigher、GSPO、CISPO、DPPO四个主流基线，AIME24-26基准集峰值平均准确率达50.5%，分别超出基线11.0、7.0、3.1、4.1个百分点；超参数鲁棒性强，ϵ在0.05-0.2、C在2.0-4.0区间性能波动小于1pct。

> 最值得记住：无critic的RL优化无需依赖重要性采样，基于贝尔曼方程重构的轨迹级目标可在更低计算成本下实现更优训练效果
