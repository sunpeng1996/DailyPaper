---
title: Sparse Additive Off-Policy Evaluation for Reinforcement Learning with Potentially
  Limited Number of Trajectories
title_zh: 面向有限轨迹场景的强化学习稀疏加性离轨策略评估框架
authors:
- Tuoyi Zhao
- Chengchun Shi
- Zhengling Qi
- Lan Wang
affiliations:
- Yale University
- London School of Economics and Political Science
- George Washington University
- University of Miami
arxiv_id: '2608.22595'
url: https://arxiv.org/abs/2608.22595
pdf_url: https://arxiv.org/pdf/2608.22595
published: '2026-08-23'
collected: '2026-08-25'
category: Eval
direction: 强化学习离轨策略评估优化
tags:
- Off-Policy Evaluation
- Reinforcement Learning
- Sparse Learning
- High Dimensional Data
- Feature Screening
one_liner: 提出带稀疏加性结构的OPE框架，缓解维数灾难，支持少轨迹场景下精准策略价值评估
practical_value: '- 电商推荐/广告的RL策略迭代中，可复用该框架基于少量历史轨迹做OPE，避免在线测试带来的流量损失和业务风险

  - 高维用户/物品特征场景下，可借鉴组稀疏特征筛选流程，快速定位影响策略效果的核心特征，降低模型推理复杂度

  - 长周期会话推荐的RL策略评估中，可复用其有限样本误差边界理论，灵活平衡轨迹采集数量和观测时长的成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有无限 horizon 强化学习的离轨策略评估（OPE）方法高度依赖大量轨迹数据，且在高维状态空间下易受维数灾难影响，难以适配电商广告、推荐等轨迹获取成本高、特征维度高的业务场景。
### 方法关键点
1. 采用带稀疏加性结构的非线性函数族建模Q函数，适配高维状态空间；
2. 推导有限样本高概率误差边界，边界仅对环境维度d取对数，大幅缓解维数灾难；
3. 提出组稀疏特征筛选流程，可高概率筛选出包含所有相关协变量的精简特征集；
4. 理论支持仅需轨迹数量或时间 horizon 任一足够大，即可输出准确价值估计。
### 关键结果
数值实验验证该方法在高维状态、有限轨迹场景下的评估精度显著优于现有OPE基线，特征筛选可高概率保留全部有效特征。
