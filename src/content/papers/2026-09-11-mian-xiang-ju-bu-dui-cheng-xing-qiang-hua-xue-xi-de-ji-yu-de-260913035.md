---
title: Groupoid-Based Internal State Representations for Reinforcement Learning with
  Local Symmetries
title_zh: 面向局部对称性强化学习的基于群胚的内部状态表示方法
authors:
- Ben Opperman
- Eduardo Alonso
- Esther Mondragón
affiliations:
- CitAI, AI Research Centre, City St George’s, University of London
arxiv_id: '2609.13035'
url: https://arxiv.org/abs/2609.13035
pdf_url: https://arxiv.org/pdf/2609.13035
published: '2026-09-11'
collected: '2026-09-14'
category: Agent
direction: 智能体强化学习 · 局部对称性利用
tags:
- Reinforcement Learning
- Groupoid
- State Representation
- Symmetry Exploitation
- Sample Efficiency
one_liner: 提出基于群胚的RL框架，动态捕捉局部状态对称性，提升样本效率与收敛表现
practical_value: '- 电商动态排序、广告实时出价等RL决策场景，可借鉴局部对称性挖掘思路，将相似上下文、用户行为状态映射到canonical空间，降低状态空间复杂度，提升策略样本效率

  - 可复用「轨道代表+转换器」的状态映射架构，对海量用户特征、上下文特征做等价类聚合，减少冗余特征的学习成本，加快策略迭代速度

  - 针对大规模稀疏电商环境的RL策略优化，无需强依赖全局统一的状态抽象假设，可优先挖掘局部上下文依赖的对称性，适配复杂多变的业务场景'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有RL对称性利用方法依赖固定群动作或预定义状态抽象，经典RL的全局MDP假设无法适配真实环境中普遍存在的模块化、局部上下文依赖规律，严重限制策略的样本效率与泛化能力。
### 方法关键点
提出基于群胚的RL框架，可在智能体与环境交互过程中动态发现局部、状态依赖的等价结构；智能体维护轨道代表集与转换器，将原始状态映射到统一规范形式，在对称性降维后的空间完成学习与决策，同时保留必要的局部特征差异。
### 关键结果
在具有强局部对称性的密集、大规模环境中，相比标准Q-learning，样本效率与收敛速度均有大幅提升，验证了动态局部对称性利用对RL可扩展性与泛化性的增益效果。
