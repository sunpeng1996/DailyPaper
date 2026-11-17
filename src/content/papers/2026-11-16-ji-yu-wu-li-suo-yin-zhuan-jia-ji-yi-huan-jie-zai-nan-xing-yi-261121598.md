---
title: 'Mitigating Catastrophic Forgetting with Physics-Indexed Specialist Memory:
  the Evolutionary Neuroplastic Agent'
title_zh: 基于物理索引专家记忆缓解灾难性遗忘的进化神经可塑性智能体
authors:
- Blas Eugenio Vicco Zarate
- Miguel Hernán Vicco
affiliations:
- Universidad Nacional del Litoral, Santa Fe, Argentina
- Facultad de Ingeniería y Ciencias Hídricas
- Facultad de Ciencias Médicas
arxiv_id: '2611.21598'
url: https://arxiv.org/abs/2611.21598
pdf_url: https://arxiv.org/pdf/2611.21598
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: 持续强化学习 · 灾难性遗忘缓解
tags:
- Continual Reinforcement Learning
- Neuroevolution
- Catastrophic Forgetting
- Policy Reuse
- Non-stationary Environment
one_liner: 提出基于物理索引专家记忆的进化神经塑性智能体，缓解持续强化学习灾难性遗忘
practical_value: '- 可借鉴「环境动态检测+按场景归档策略+贝叶斯检索复用」框架，解决电商推荐/广告系统在大促、季节变动等非稳态场景的效果退化问题，避免频繁全量重训

  - 无梯度进化小网络的思路可用于端侧轻量推荐Agent的策略迭代，无需反向传播，降低端侧计算开销

  - 失败驱动的搜索触发机制可迁移到推荐系统的异常降级流程，当当前策略效果下降时自动触发历史优质策略召回'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
持续强化学习落地需适配非稳态环境，同时保留历史场景性能，但常规单策略RL易发生灾难性遗忘，过往方案多依赖梯度优化、权重正则或经验回放，泛化性与开销难以平衡。
### 方法关键点
1. 采用无梯度进化生成小型神经网络策略，无需反向传播
2. 按检测到的环境动态模式归档策略，构建物理索引的专家记忆库
3. 基于贝叶斯策略复用机制检索匹配的历史策略，仅在策略失败时触发新搜索
### 关键结果
- 30次重复CartPole消融实验中，完整架构在5个测试环境下平均成功率达83.2%
- 是所有变体中对高难度CartPole场景记忆保留最稳定的方案，检索规则对性能影响显著
- 当前版本在CartPole上适配速度慢于PPO，HalfCheetah环境下收益低于SAC，暂未证明优于其他持续学习方法
