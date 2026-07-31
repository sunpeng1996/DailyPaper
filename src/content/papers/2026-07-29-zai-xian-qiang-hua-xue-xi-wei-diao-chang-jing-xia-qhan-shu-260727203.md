---
title: Do You Really Need to Pretrain Q-Functions for Online RL Fine-Tuning?
title_zh: 在线强化学习微调场景下Q函数预训练的必要性研究
authors:
- Perry Dong
- Ron Polonsky
- Dorsa Sadigh
- Chelsea Fin
affiliations:
- Stanford University
arxiv_id: '2607.27203'
url: https://arxiv.org/abs/2607.27203
pdf_url: https://arxiv.org/pdf/2607.27203
published: '2026-07-29'
collected: '2026-07-31'
category: Training
direction: 强化学习微调 · Q函数初始化优化
tags:
- Reinforcement Learning
- Fine-tuning
- Q-function
- Policy Ensemble
- Online RL
one_liner: 发现朴素Q函数预训练收益有限，提出IPE方法用多策略池化轨迹初始化Q函数提升在线RL微调性能
practical_value: '- 做LLM/推荐系统RLHF微调时，无需强行预训练Q函数，随机初始化可达到接近效果，节省离线预训练算力开销

  - 需优化Q函数初始化效率时，可复用IPE思路，用多源多样化策略的生成轨迹做bootstrapping，提升微调收敛速度

  - 涉及价值函数的在线微调场景，需警惕预训练价值函数与最终收敛目标价值函数的分布mismatch问题，避免盲目做离线价值预训练'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前预训练+RL微调是策略学习的主流范式，价值-based RL领域默认需同步预训练Q函数，但近期实践发现随机初始化Q的在线RL也能产出高性能策略，亟需系统验证Q函数预训练的实际价值。
### 方法关键点
1. 系统实验证实朴素Q函数预训练相比随机初始化几乎无增益，核心原因是预训练阶段拟合的是预训练策略对应的Q分布，与在线微调最终收敛的目标Q分布存在本质mismatch，该gap甚至无法通过离线价值最大化消除；
2. 提出Initialization via Policy Ensemble（IPE）方法，训练多个差异化策略，用其pooled轨迹数据做Q函数初始化的bootstrapping，提升对目标Q分布的覆盖度。
### 关键结果
在多组连续控制基准测试中，IPE相比朴素Q预训练的微调性能平均提升26%（达1.26倍）。
