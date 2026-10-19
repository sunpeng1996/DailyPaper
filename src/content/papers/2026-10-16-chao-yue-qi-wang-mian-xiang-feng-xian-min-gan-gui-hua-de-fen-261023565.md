---
title: 'Beyond Expected Values: Risk-Sensitive Planning with Distributional Monte-Carlo
  Tree Search'
title_zh: 超越期望：面向风险敏感规划的分布型蒙特卡洛树搜索
authors:
- Quynh Trinh
- Trung Nguyen
- Nam Nguyen
- Tuan Dam
affiliations:
- Hanoi University of Science and Technology
- Center for AI Research, VinUniversity
arxiv_id: '2610.23565'
url: https://arxiv.org/abs/2610.23565
pdf_url: https://arxiv.org/pdf/2610.23565
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent · 风险敏感树搜索规划
tags:
- MCTS
- CVaR
- Thompson Sampling
- Risk-sensitive Planning
- Distributional RL
one_liner: 提出CATSO、PATSO两种非参数分布型MCTS算法，兼顾O(n^-1/2)收敛率与风险敏感规划能力
practical_value: '- 电商大促预算分配、库存规划等高风险决策场景，可复用CVaR+非参数分布建模思路，替换原有均值最优MCTS模块，避免极端亏损场景出现

  - 推荐系统极端负向体验（如用户投诉、低质内容推送）规避场景，可借鉴「Q边存分布、V节点用访问加权CVaR标量回传」的架构，平衡尾部建模精度和计算开销，无需全链路存储分布

  - 基于MCTS的推荐Agent路径规划落地时，可直接复用PATSO的自适应粒子压缩策略，通过限制单边粒子数上限，在可控精度损失下降低内存占用，适配在线部署要求'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
传统MCTS仅存储Q边标量均值估计，无法区分均值相同但尾部风险差异极大的动作，无法满足自动驾驶、金融、电商高风险决策等场景的尾部风险规避需求；现有分布型MCTS依赖参数化分布假设，容易掩盖多峰、重尾分布下的真实尾部特征。

### 方法关键点
- 两种非参数分布MCTS算法：CATSO用固定/自适应网格分类原子+Dirichlet Thompson采样表示Q边分布，PATSO用自适应加权粒子表示Q边分布，无需预定义分布形式
- 动作选择阶段计算Thompson采样得到的Q边分布的CVaR，叠加多项式乐观bonus保证探索充分
- V节点仅保留标量值，通过子节点Q边CVaR的访问加权平均回传，避免分布卷积带来的高计算开销
- 理论证明两种算法根节点值误差为O(n^{-1/2})，CATSO存在固定网格离散偏差，带粒子数上限的PATSO存在可调Wasserstein压缩偏差

### 关键结果
在自动驾驶、风险迷宫、赌博游戏等5个均值最优与风险敏感最优动作存在差异的基准上，对比UCT等标量MCTS基线，CATSO/PATSO将蒙特卡洛CVaR回报最高提升37%，灾难性事件发生次数降低62%，根节点CVaR值缺口随rollout次数增加以O(n^{-1/2})速率下降。

最值得记住的一句话：风险敏感决策场景中，仅保留均值的MCTS会系统性偏向高均值高尾部风险的动作，仅在Q边保留分布、V节点回传标量风险指标的架构可在几乎不增加额外开销的前提下大幅降低尾部风险。
