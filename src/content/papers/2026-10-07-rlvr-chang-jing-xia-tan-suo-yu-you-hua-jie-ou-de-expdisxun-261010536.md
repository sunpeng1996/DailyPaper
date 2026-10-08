---
title: Decoupling Exploration from Optimization in RLVR
title_zh: RLVR 场景下探索与优化解耦的ExpDis训练框架
authors:
- Saif Punjwani
- Micah Goldblum
affiliations:
- Columbia University
arxiv_id: '2610.10536'
url: https://arxiv.org/abs/2610.10536
pdf_url: https://arxiv.org/pdf/2610.10536
published: '2026-10-07'
collected: '2026-10-08'
category: Training
direction: LLM训练 · RLVR探索优化解耦
tags:
- RLVR
- Exploration
- Knowledge Distillation
- LLM Reasoning
- Reinforcement Learning
one_liner: 通过探索-蒸馏双路解耦架构，在RLVR训练中兼顾探索效率、推理精度与通用能力保留
practical_value: '- 做电商导购Agent、推荐文案生成的RL微调时，可复用双路架构：单独训练带探索奖励的离线探索模型，仅将过滤后的高转化率/正确轨迹蒸馏到上线模型，避免探索过程导致的通用能力退化，不影响线上稳定性

  - RL训练中加新奇度奖励时，可复用「仅对正确样本叠加新奇度奖励、训练迭代中逐步退火新奇度权重」的trick，平衡探索多样性和输出质量，避免生成大量无效新奇内容

  - 生成式推荐、搜索Query推荐的策略探索场景，可复用多并行Explorer+多轮迭代的架构，相同算力下提升探索覆盖度，且不增加线上推理耗时，快速试错新的推荐策略'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有RLVR（带可验证奖励的强化学习）直接在单个模型上叠加新奇度奖励提升探索能力，会导致模型通用能力退化（非训练域任务性能下降、已有知识遗忘），且探索强度受上线模型精度约束无法放大，限制了新策略的发现效率。
### 方法关键点
- 双路解耦架构：独立训练带RND新奇度奖励的Explorer模型，仅将过滤后的正确、无重复、最短的高质量轨迹通过SFT蒸馏到Student模型，Student仅用正确性奖励做RLVR训练，完全不接触新奇度奖励
- 可双维度扩展：单轮可并行多个Explorer，混合多模型轨迹提升探索多样性；可多轮迭代，用前一轮Student初始化下一轮的Explorer和Student，同时退火新奇度权重，逐步巩固探索收益
- 兼容性强：支持任意新奇度奖励、任意RLVR基底算法，Explorer不直接上线，可使用激进探索策略无需担心稳定性
### 关键实验
在7个数学推理基准、3个基座模型（Qwen3-1.7B/4B、Ministral-3B）上测试，相同算力下：ExpDis比SOTA DAPO基线pass@1平均提升4.2~5.1pp，pass@64提升7.9~12.4pp，甚至超过4倍训练步数的DAPO；对比直接加新奇度奖励的DAPO，ExpDis无通用能力退化，MMLU等通用任务性能波动<0.2pp（基线下降>1.5pp）。
### 核心结论
给模型独立的离线安全探索空间，允许探索过程出错，仅把经过验证的有效经验同步到上线模型，是平衡探索效率、性能、稳定性的通用路径
