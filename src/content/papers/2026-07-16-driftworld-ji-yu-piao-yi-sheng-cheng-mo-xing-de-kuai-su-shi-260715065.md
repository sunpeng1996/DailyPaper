---
title: 'DriftWorld: Fast World Modeling through Drifting'
title_zh: DriftWorld：基于漂移生成模型的快速世界建模
authors:
- Susie Lu
- Haonan Chen
- Weirui Ye
- Yilun Du
affiliations:
- Massachusetts Institute of Technology
- Harvard University
arxiv_id: '2607.15065'
url: https://arxiv.org/abs/2607.15065
pdf_url: https://arxiv.org/pdf/2607.15065
published: '2026-07-16'
collected: '2026-07-19'
category: Agent
direction: Agent 世界模型 漂移生成推理加速
tags:
- World Model
- Drift Generative Model
- Inference Acceleration
- Action-Conditioned Generation
- Robot Agent
one_liner: 提出基于漂移生成的动作条件世界模型，单步前向生成帧，速度比扩散基线高17倍，决策性能达SOTA
practical_value: '- 低延迟生成场景可借鉴漂移生成替代扩散的思路，比如实时推荐的商品文案/图生成、Agent实时决策场景，替换多步扩散采样大幅降低推理延迟

  - 世界模型离线评估策略的思路可复用：推荐/广告新策略上线前，用用户行为预测模型做离线rollout排序，降低线上实验风险

  - 条件生成任务可复用「训练阶段学习条件漂移、推理单步前向」的范式，大幅削减推理计算开销'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
扩散类世界模型依赖多步迭代去噪采样，生成rollout的推理速度慢，成为Agent大规模动作搜索、实时规划的核心瓶颈。
### 方法关键点
基于漂移生成模型构建动作条件世界模型DriftWorld，训练阶段学习动作关联的漂移函数，推理阶段无需迭代去噪，仅单次前向传播即可基于当前观测和候选动作序列生成未来帧。
### 关键结果
推理速度达30+fps，平均比扩散基线快17倍；在Bridge-V2、RT-1等多个机器人操作基准上决策性能达SOTA；作为离线模拟器做策略排序时，rollout得分与真实值相关性最高达0.99
