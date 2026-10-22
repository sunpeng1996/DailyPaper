---
title: Asymmetric On-Policy Distillation Learns In-Context Exploration
title_zh: 非对称同策略蒸馏框架ASTEROID：实现高效上下文内探索学习
authors:
- Sriyash Poddar
- Yanda Bao
- Jacob Krantz
- Matthew Chang
- Xavier Puig
- Roozbeh Mottaghi
- Natasha Jaques
- Abhishek Gupta
affiliations:
- University of Washington
- Meta
arxiv_id: '2610.30105'
url: https://arxiv.org/abs/2610.30105
pdf_url: https://arxiv.org/pdf/2610.30105
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: Agent决策 · 部分可观测场景探索优化
tags:
- Distillation
- In-Context Exploration
- POMDP
- Imitation Learning
- Reinforcement Learning
one_liner: 通过学生同策略轨迹+特权专家标注的蒸馏范式，让部分可观测下的Agent学会高效上下文探索
practical_value: '- 搜索推荐/电商Agent冷启动探索可借鉴该范式：用全量业务数据训练特权专家（如能看到全量用户/物品特征的排序模型），再蒸馏给仅能看到用户历史行为的线上部署模型，降低探索成本

  - 部分可观测场景的策略训练可复用同策略数据标注逻辑：无需覆盖全量上下文空间，只需收集当前部署模型产生的真实轨迹做专家标注，大幅降低训练数据量需求

  - 多轮交互推荐/导购Agent的探索策略训练可参考课程式上下文长度设计：逐步扩充训练时的上下文窗口长度，提升长序列交互下的探索效率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
部分可观测序贯决策（POMDP）是真实世界Agent落地的核心难题，传统在线RL学习探索行为样本效率极低，离线模仿学习只能拟合专家平均行为，无法学会自适应探索；现有基于离线上下文的探索方法需要覆盖指数级增长的上下文空间，高维场景下不可行。

### 方法关键点
- 提出ASTEROID非对称学生-教师蒸馏框架：训练时仅能看到部分观测的学生自主生成同策略交互轨迹，能观测全量隐藏状态的特权教师针对学生轨迹的每个状态给出最优动作标注
- 无需显式建模贝叶斯后验，通过迭代蒸馏让学生隐式学会根据历史上下文排除无效假设，实现不确定时探索、确定后利用的类后验采样高效探索逻辑
- 采用上下文长度课程训练：每轮迭代逐步增加学生的rollout长度，提升样本效率和长上下文适应能力

### 关键实验
在11个不同场景（离散探索基准、机器人操纵、导航、Procgen环境等）测试，固定探索预算时回报是基线的~2倍，训练交互量比RL基线少~100×；真实世界无视觉机器人抓取任务上，比标准蒸馏成功率高+40%；机械臂插钉任务上比Claude Opus 5.5成功率高28%。

### 核心结论
不需要复杂的RL或显式后验建模，仅通过同策略轨迹+特权专家蒸馏，就能让Agent高效学会上下文内探索行为。
