---
title: 'CoWeaver: A Bi-directional, Learnable and Explainable Matching Engine for
  Mixed Human-Agent Science Collaboration'
title_zh: CoWeaver：面向人-Agent混合科研协作的双向可解释匹配引擎
authors:
- Jiayao Gu
- Kexin Chu
- Peidong Liu
- Yue Yang
- Lynn Ai
- Qi Zhang
- Ling Yang
- Tianyu Shi
affiliations:
- McGill University
- Mila – Québec AI Institute
- University of Connecticut
- Sichuan University
- Stanford University
arxiv_id: '2607.15545'
url: https://arxiv.org/abs/2607.15545
pdf_url: https://arxiv.org/pdf/2607.15545
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: 人-Agent混合协作 · 双向匹配
tags:
- Human-Agent Collaboration
- Matching Engine
- Explainable AI
- LLM Agent
- Cold Start
- Two-stage Ranking
one_liner: 提出双向可解释匹配框架，结合分析打分与LLM模拟重排，实现人-Agent混合网络高质量协作匹配
practical_value: '- 双向匹配思路可直接复用在电商供需匹配场景（商家-达人带货、服务商-品牌需求匹配等），用「需求侧缺口覆盖率+供给侧价值满足率」双向打分替代传统单向相似度匹配，大幅提升双边满意度

  - 两阶段排序trick可迁移到推荐/广告重排层：第一阶段用轻量MapScore类规则模型做粗排保效率，第二阶段用LLM模拟交互（比如用户-商品适配、达人-品牌合作可行性）做软特征重排，平衡效率和效果

  - UCB+贝叶斯能力估计的冷启策略可直接用于新用户/新商家/新Agent的冷启动推荐，给低观测样本的候选分配探索权重，避免冷启锁死

  - MapScore的可解释分解方法可复用在需强解释性的推荐场景（金融产品、企业服务匹配等），直接输出匹配归因（覆盖的缺口、满足的需求）提升用户接受度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent擅长单任务执行，但无法适配科研等场景的人-Agent协作匹配需求：协作匹配需要同时满足需求侧能力缺口填补、供给侧参与价值匹配、硬可行性约束、冷启动处理四大要求，传统推荐、团队匹配方法只能覆盖部分维度，且缺乏可解释性，用户接受度低。

### 方法关键点
- 统一表示层：将人、Agent、可复用技能统一表示为「能力集+需求集」的语义向量，能力集包含熟练度、不确定性两个维度，任务同时建模能力要求、参与激励、硬约束三类属性
- 核心MapScore双向打分：先通过硬可行性门控过滤无效候选，再加权计算需求侧能力缺口覆盖率、供给侧需求满足率，得分可直接分解为可解释的匹配因子
- 两阶段排序：第一阶段用MapScore做高效粗排，第二阶段通过LLM DREAMING模拟双方谈判交互，评估时间、协作风格、性格适配等软特征重排，平衡效率和实际可行性
- 反馈与探索：基于用户反馈贝叶斯更新能力估计和打分权重，用UCB策略给低观测候选分配探索权重，解决冷启动问题

### 关键实验
基于20个合成协作匹配任务测试，对比Greedy、Random、AgenticPay、PeopleJoin等基线：1）UCB+Greedy策略在6/20任务上超过纯Greedy分析最优解，匹配质量ρmode达0.953；2）加入LLM DREAMING后，任务可用率从45%提升到90%，组合效用从0.865提升到0.904；3）所有指标均超过AgenticPay基线，命中最优候选的命中率达75%，找到最优候选的平均轮数仅4.4轮。

### 核心结论
协作匹配不是单向的全局最优排序，而是任务条件下的双向互补性适配，兼顾能力匹配、双向价值、可行性与可解释性才能真正落地。
