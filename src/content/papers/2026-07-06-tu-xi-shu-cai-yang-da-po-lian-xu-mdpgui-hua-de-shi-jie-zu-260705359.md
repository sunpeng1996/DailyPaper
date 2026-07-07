---
title: 'Graph Sparse Sampling: Breaking the Curse of the Horizon in Continuous MDP
  Planning'
title_zh: 图稀疏采样：打破连续MDP规划的视界诅咒
authors:
- Idan Lev-Yehudi
- Vadim Indelman
affiliations:
- Technion – Israel Institute of Technology
arxiv_id: '2607.05359'
url: https://arxiv.org/abs/2607.05359
pdf_url: https://arxiv.org/pdf/2607.05359
published: '2026-07-06'
collected: '2026-07-07'
category: Agent
direction: Agent 连续MDP在线规划优化
tags:
- MDP-Planning
- Graph-Sampling
- GPU-Parallel
- Online-Planning
- Monte-Carlo-Search
one_liner: 提出GPU友好的图稀疏采样GSS算法，打破连续MDP规划的指数视界复杂度瓶颈，性能优于树结构规划器
practical_value: '- 电商多步决策场景（会话推荐、长周期用户转化规划）可复用GSS的状态共享思路，替代MCTS子树独立采样，大幅降低长horizon规划成本，适配GPU并行加速

  - 生成式推荐/Agent决策推理模块可借鉴分层采样+反向备份架构，通过SNIS平滑备份解决用户行为低秩隐式建模的密度估计问题，提升长序列决策准确率

  - 在线规划业务（广告动态出价、促销策略寻优）可复用其理论结论，满足状态转移与提议分布重叠度约束时，可保证多项式复杂度下的决策误差上界，降低调参盲目性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
连续MDP在线规划是Agent决策、机器人控制等场景的核心问题，传统树结构搜索方法（如MCTS）的采样预算随规划视界指数增长，在连续状态/动作空间下算力瓶颈严重，现有非树方法要么无法适配GPU批量并行，要么无多项式复杂度的理论保证。

### 方法关键点
- 采用无分支分层图结构替代搜索树，所有候选动作共享同一后继状态层采样结果，避免子树重复采样，所有操作均为固定批量结构，天然适配GPU并行加速
- 前向pass交替执行动作采样、共享状态层采样，终端层用启发式函数赋值；反向pass执行图备份计算动作价值，支持SNIS、KDE、最近邻、学习式四类备份方式，适配不同场景的转移模型可获得性
- 针对低秩转移模拟器设计平滑SNIS备份，通过核平滑解决奇异转移的密度估计问题，理论证明满足重叠度、正则性、动作覆盖条件下，采样复杂度随视界多项式增长，打破指数诅咒

### 关键结果
在三个连续控制基准上对比DPW、VPW等MCTS类树规划器：1）旋转DDI场景下，GSS仅用0.7s以内规划时间，性能超过1s预算的DPW/VPW，rollout引导失配时性能下降幅度远低于树规划器；2）月球着陆器场景下，GSS在中等预算即可达到最高回报，而树规划器性能随预算增加反而下降；3）Reacher场景下，所有测试GSS预算均优于PD基线控制器，性能随采样预算提升稳步增长。

### 核心结论
长horizon在线规划的优化方向可以从树的分支剪枝转向共享状态层的批量采样，只要保证提议分布与真实转移的重叠度，就能在多项式成本下拿到接近最优的决策效果
