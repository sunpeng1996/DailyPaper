---
title: 'Explore Once, Evaluate Many: Multiple Policy Evaluation for Stochastic Linear
  Bandits'
title_zh: 单次探索多次评估：面向随机线性老虎机的多策略评估方法
authors:
- Spyros Dragazis
- Yilei Chen
- Aldo Pacchiano
affiliations:
- Boston University
- Broad Institute of MIT and Harvard
arxiv_id: '2610.22252'
url: https://arxiv.org/abs/2610.22252
pdf_url: https://arxiv.org/pdf/2610.22252
published: '2026-10-15'
collected: '2026-10-17'
category: Eval
direction: 上下文老虎机 · 多策略并行评估
tags:
- Contextual Bandit
- Policy Evaluation
- Linear Model
- Sampling Design
- Offline Evaluation
one_liner: 提出PRISMA算法实现随机线性上下文老虎机下多目标策略的高效并行评估
practical_value: '- 推荐系统多召回/排序策略批量评测可复用「共享采样+单一回归器」架构，大幅降低评估采样成本

  - 自适应正则化参数的doubling procedure可迁移到线性模型超参调优，无需预定义搜索空间

  - 给出的多策略评估复杂度边界可作为AB测试样本量计算参考，有效缩短测试周期'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
上下文老虎机广泛应用于推荐系统、医疗、金融等决策场景，不同模型结构、超参数会生成大量候选策略，现有单策略逐一评估方案采样成本极高，无法支撑批量评测需求。
### 方法关键点
提出PRISMA算法，融合无奖励规划、正则化采样设计、跨所有目标策略共享的单一ridge regression估计器，通过自适应加倍流程选择正则化系数，无需预先知晓分布难度参数$\rho^\star$。
### 关键结果数字
仅需$\widetilde{\mathcal{O}}\left( \frac{(L^2S^2+\beta^2)(1\vee\rho^\star)}{\varepsilon^2} \cdot \log(K) \right)$次上下文采样与奖励观测，即可将所有K个目标策略的价值估计误差控制在$\varepsilon$以内（置信度≥1-$\delta$），无上下文、动作空间基数依赖，仅需每个共享规划上下文调用K次策略查询。
