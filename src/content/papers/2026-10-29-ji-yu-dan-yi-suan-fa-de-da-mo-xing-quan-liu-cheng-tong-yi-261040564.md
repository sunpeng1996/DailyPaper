---
title: Training Foundation Models with a Single Algorithm
title_zh: 基于单一算法的大模型全流程统一训练框架
authors:
- Yuda Song
- Alvin Zhang
- Fahim Tajwar
- Daman Arora
- Jeff Schneider
- Daniel Khashabi
- Ruslan Salakhutdinov
- J. Andrew Bagnell
- Aarti Singh
- Andrea Zanette
affiliations:
- Carnegie Mellon University
- Johns Hopkins University
- Aurora Innovation
arxiv_id: '2610.40564'
url: https://arxiv.org/abs/2610.40564
pdf_url: https://arxiv.org/pdf/2610.40564
published: '2026-10-29'
collected: '2026-10-30'
category: Training
direction: 大模型训练 · 全阶段统一范式
tags:
- LLM
- Training Pipeline
- Maximum Likelihood
- Reinforcement Learning
- Unified Training
one_liner: 将大模型预训练、SFT、RL全阶段纳入统一最大似然训练框架，仅调整数据配比无需切换算法
practical_value: '- 训练电商/导购Agent、推荐话术生成等垂类LLM时，可省略分阶段训练的工程切换步骤，直接混合预训练、SFT、RL高分样本用统一交叉熵损失训练，降低开发成本

  - 做垂域模型RL对齐时，按比例混合静态SFT数据和RL生成的优质样本训练，可减少通用/垂类基础能力遗忘，同时提升RL目标任务性能，降低过拟合风险

  - 做模型持续学习（如大促前给Agent加新活动规则、新品知识）时，混合旧知识数据和新任务数据用统一范式微调，无需修改训练代码，后续新任务学习效率可提升10%以上'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统大模型训练分为预训练、中训、SFT、RL多个独立阶段，各阶段使用不同算法和基础设施，不仅工程复杂度高，还存在阶段间能力迁移差、旧能力遗忘严重、全局计算资源利用效率低等问题，无法从全流程视角优化训练效果。

### 方法关键点
- 基于MaxRL理论推导，将RL目标转化为对模型生成的高分样本分布的最大似然拟合，把预训练、中训、SFT、RL全阶段统一到相同的加权交叉熵损失下
- 设计统一数据格式，所有样本均为「token序列+对应位置权重」：预训练/中训全序列权重为1，SFT仅回复部分权重为1，RL高分回复部分权重按奖励值加权
- 实现异步训练架构，生成器产出RL高分样本存入公共缓存，训练器同时采样静态数据和RL样本训练，定期同步权重，仅调整不同数据源的配比和调度策略即可适配不同训练需求

### 关键结果
对比传统分阶段训练，在受控推理任务上相同计算预算下，统一训练的pass@1准确率最高提升12%，任务coverage最高提升15%，预训练通用能力遗忘率降低40%；在数学、代码任务上，仅调整0-5%的静态数据混合比例即可平衡目标任务性能和通用能力保留，后续持续学习新任务的最终准确率比分阶段训练高8%。

### 核心结论
大模型全阶段训练的核心设计问题不是选择不同阶段的算法，而是选择训练数据的来源、配比和投喂时机。
