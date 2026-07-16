---
title: Knowledge- and Gradient-Guided Reinforcement Learning for Parametrized Action
  Markov Decision Processes
title_zh: 面向参数化动作MDP的知识与梯度引导强化学习算法KGRL
authors:
- Jonas Ehrhardt
- René Heesch
- Oliver Niggemann
affiliations:
- Helmut-Schmidt-University Hamburg
- HSU-AI Institute for Artificial Intelligence
- Institute of Automation Technology
arxiv_id: '2607.12924'
url: https://arxiv.org/abs/2607.12924
pdf_url: https://arxiv.org/pdf/2607.12924
published: '2026-07-14'
collected: '2026-07-16'
category: Agent
direction: Agent 强化学习样本效率优化
tags:
- Reinforcement Learning
- PAMDP
- Neuro-Symbolic
- Sample Efficiency
- Explainable RL
one_liner: 将Datalog知识库与梯度引导参数优化结合，提升参数化动作空间RL的样本效率与可解释性
practical_value: '- 电商动态调价、广告出价等同时涉及离散动作（选活动/投放位）+连续参数（折扣/出价）的场景，可复用KGRL的决策空间剪枝思路，把业务规则（最低折扣限制、出价上下限等）导入Datalog知识库，直接过滤无效决策，减少Agent探索浪费

  - 现有离散+连续混合动作空间的RL方案可替换one-shot参数预测为梯度引导的参数迭代优化，利用Q函数的梯度信息在约束范围内微调参数，提升决策精度，避免硬编码参数范围的次优问题

  - 对强监管类业务（营销活动合规、广告投放限制等），可复用本文的解释trace机制，记录每一步决策的规则触发日志，满足决策可解释、可审计的要求，降低合规风险'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
参数化动作MDP（PAMDP）的决策同时包含离散符号动作和连续参数，现有RL方案大多采用one-shot参数估计，样本效率极低，且容易输出违反业务规则的决策；而实际场景中普遍存在不完整的领域知识（规则、安全约束、专家启发式），却很少被直接用于提升RL训练效率。

### 方法关键点
- KGRL在DQN基础上新增两个核心模块：1）Datalog知识库，接收数值状态的符号化抽象结果，推理得到当前状态下的可用动作集合与参数可行范围，直接剪枝无效动作、约束参数空间；2）PARAMOPT梯度引导参数优化模块，对每个可用动作，基于Q函数的梯度做投影梯度上升，在可行参数范围内迭代找到最优参数，替代传统one-shot估计
- 训练阶段用知识库约束探索范围，部署阶段同样保留规则过滤，同时可记录每一步的规则触发日志，生成局部过程化解释，追溯动作剪枝和参数约束的原因

### 关键实验
在HardMoveX、CatchPoint、HardGoal、Platform 4类PAMDP基准数据集上，对比QPAMDP、PA-DDPG、P-DQN、HyAR、MP-DQN 5个SOTA基线，KGRL在所有数据集上AULC（学习曲线下面积）均为最高，样本效率比最优基线提升1~3倍；HardMove10数据集上回报比MP-DQN提升58%，HardGoal上回报达到49.76，比次优基线P-DQN高3.3%；消融实验显示部署阶段移除知识库后性能平均下降60%以上。

最值得记住的结论：把不完整的领域符号知识作为决策空间的硬约束，配合梯度引导的局部参数优化，是提升混合动作空间RL样本效率、可解释性的低成本有效路径
