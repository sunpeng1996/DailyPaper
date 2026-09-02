---
title: 'Selective Agent Guidance via Entropy: Learning Autonomous Policies from Imperfect
  VLM Teachers'
title_zh: 基于熵的选择性Agent引导：从不完美VLM教师学习自主策略
authors:
- Matteo Merler
- Giovanni Bonetta
- Davide Zago
- Rossella Cancelliere
- Bernardo Magnini
affiliations:
- Fondazione Bruno Kessler
- University of Torino
arxiv_id: '2609.01567'
url: https://arxiv.org/abs/2609.01567
pdf_url: https://arxiv.org/pdf/2609.01567
published: '2026-09-01'
collected: '2026-09-02'
category: Agent
direction: Agent 大模型教师引导强化学习
tags:
- RL
- VLM
- Knowledge Distillation
- Policy Optimization
- Entropy
one_liner: 提出SAGE框架，仅在RL智能体不确定时查询VLM教师，蒸馏得到无VLM依赖的低成本自主策略
practical_value: '- 搜索推荐稀疏冷启动场景可复用熵门控逻辑：仅当排序/召回模型置信度（熵）低于阈值时调用大模型打标/提供引导信号，大幅降低大模型调用成本，同时避免全量蒸馏引入的噪声

  - 大模型蒸馏到小模型时可复用优势加权BC损失：根据业务真实反馈（如点击、转化）调整大模型输出的蒸馏权重，避免盲目模仿大模型的错误输出

  - 电商导购、内容推荐等交互式Agent训练可借鉴该范式：用大模型作为训练阶段的临时引导，部署用小模型，兼顾训练效果和部署时延、成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
直接将VLM作为交互式决策Agent部署成本极高，且冻结VLM无法从环境交互中迭代、易重复系统性错误；纯RL在稀疏奖励场景下探索效率极低，难以发现高收益轨迹，需要低成本的引导机制弥补两者缺陷。

### 方法关键点
- 熵门控选择性查询：用RL策略的归一化熵作为不确定性代理，仅当熵超过阈值时查询VLM获取动作，其余时间由RL智能体自主决策，同时新增状态缓存进一步降低VLM调用量
- 分区损失函数：将经验分为学生自主生成、VLM引导两类，仅用前者更新PPO策略避免off-policy偏差，两类经验都用于训练价值函数
- 优势加权行为克隆（AWBC）：用环境反馈得到的优势值调整VLM动作的蒸馏权重，优先蒸馏带来高收益的VLM动作，抑制错误引导的负面影响

### 关键实验
在FrozenLake、MiniGrid、EZPoints等7个稀疏奖励视觉决策任务上测试，对比PPO、VLM-as-policy、LVLM2P、DAgger等基线：SAGE仅在1.2%~13.3%的训练步骤查询VLM，部署阶段无VLM调用；CardMaze任务上VLM-as-policy准确率为0，SAGE达到最优准确率1.0，超过其VLM教师；长周期5M步训练下，纯PPO在FrozenLake、EZPoints等任务上准确率仍接近0，SAGE+Oracle达到接近最优性能。

### 核心结论
VLM不需要作为固定策略才能产生价值，它可以作为临时的、不完美的引导源，其价值可以通过交互被测试并内化到小模型中。
