---
title: 'Floor It, Then Fill It: Simulating Creator Ecosystems for Fair Video-Content
  Recommendation Systems at Billion User Scale'
title_zh: 十亿级规模下基于创作者生态仿真的公平视频推荐框架
authors:
- Sohini Roychowdhury
- Long Sha
- Sunand Agarwal
- Payal Kamboj
- Shuyang Chen
- Junlin Zhang
- Scott Chen
- Hui Zhang
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2610.38155'
url: https://arxiv.org/abs/2610.38155
pdf_url: https://arxiv.org/pdf/2610.38155
published: '2026-10-28'
collected: '2026-10-30'
category: RecSys
direction: 推荐系统公平性 · 创作者生态仿真
tags:
- Fairness in RecSys
- Multi-Armed Bandit
- User Simulation
- Creator Ecosystem
- Cold Start
one_liner: 提出创作者生态仿真框架与带公平约束的多臂老虎机分配策略 缓解推荐马太效应
practical_value: '- 创作者/商家侧公平策略可直接复用两阶段分配逻辑：先为每个主体设置动态曝光保底，有机曝光可抵扣保底配额，剩余预算拆分小主体专属储备池+开放池，兼顾公平与效率

  - 新策略上线前可搭建耦合供给侧（创作者/商家）+消费侧的仿真环境，先完成多配置ablation再推进线上实验，大幅降低实验成本与伦理风险

  - 冷启扶持规则可参考动态保底目标设计，根据创作者/商家的粉丝/销量规模阶梯调整保底额度，避免资源浪费在已经起量的头部主体

  - 公平策略落地可复用Sim2Real验证协议：小流量实验先验证策略排名、指标趋势与仿真结果的一致性，再逐步放大流量'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
以engagement为优化目标的推荐系统普遍存在马太效应，新兴创作者、中小商家的曝光被头部主体挤压，而公平干预策略的线上评估周期长、成本高、伦理风险大；现有推荐仿真器大多仅建模用户消费行为，未覆盖供给侧成长动态与供需反馈循环，导致仿真结论可信度不足，难以支撑长期策略迭代。
### 方法关键点
- 搭建耦合创作者+内容+用户交互的高保真仿真框架，基于真实平台分布生成4.2万异构创作者队列，覆盖冷启、成长、毕业全生命周期，可模拟12周的生态演化
- 将公平曝光分配建模为带约束的预算Multi-Armed Bandit问题，采用两阶段分配：第一阶段优先兑付每个创作者90%的曝光保底，有机曝光可直接抵扣保底配额；第二阶段剩余预算按奖励函数贪心分配，额外设置小创作者储备池倾斜资源
- 对比4种奖励函数，优先采用曝光缺口奖励扶持未达保底的创作者，同时设计随粉丝数动态调整的graduated保底目标，平衡扶持力度与预算效率
### 关键实验
基于Meta真实短视频平台创作者数据校准仿真器，最优配置（graduated动态目标+70%小创作者储备池+曝光缺口奖励）下，每周90%的创作者可达成曝光目标，小创作者有机周涨幅达33%，周度受扶持创作者集合Jaccard系数达0.819，分配稳定性优于其他配置。
### 核心结论
短周期单步评估会系统性低估推荐马太效应的负面影响，也会低估公平扶持策略的长期收益。
