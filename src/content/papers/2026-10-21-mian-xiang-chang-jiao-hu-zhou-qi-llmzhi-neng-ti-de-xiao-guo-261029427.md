---
title: 'One Act, Many Masks: Effect-Marginal Policy Optimization for Long-Horizon
  Agents'
title_zh: 面向长交互周期LLM智能体的效果边际策略优化EMPO算法
authors:
- Shaojin Ma
- Ruitao Wang
- Pengyi Li
- Jie Yang
- Liangyu Chen
- Gangyi Zhao
- Hongyao Tang
- Yan Zheng
- Jianye Hao
affiliations:
- Tianjin University
- Fudan University
- Renmin University of China
arxiv_id: '2610.29427'
url: https://arxiv.org/abs/2610.29427
pdf_url: https://arxiv.org/pdf/2610.29427
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: 长周期Agent · RL策略优化
tags:
- LLM Agent
- Reinforcement Learning
- Policy Optimization
- GRPO
- Long-Horizon Task
one_liner: 针对长horizon LLM Agent RL训练的credit-更新错位问题，提出无额外开销的EMPO优化算法
practical_value: '- 做电商导购Agent、搜索Agent的RL训练时，可复用EMPO的执行等价分组逻辑，把不同表述但执行结果相同的响应（比如不同话术的搜索指令、加购指令）归为同一effect
  cell，共享策略ratio，减少更新波动

  - 无需额外采集数据、新增critic或奖励模型，仅在策略更新阶段修改ratio计算逻辑，可无缝嵌入现有GRPO、PPO等RL训练管线，改造成本极低

  - 训练时新增的响应长度归一化trick可直接复用，避免长回复的log ratio累积偏差导致的更新不稳定问题'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
长horizon LLM Agent的RL训练中，credit分配是长期核心痛点，现有方案大多聚焦优化credit估计的粒度与准确性，但忽略了策略更新阶段的固有错位：不同文本表述的响应可能产生完全相同的执行效果（比如不同措辞的跳转指令最终都跳转到商品详情页），但传统PPO/GRPO会按文本响应单独计算策略ratio，导致相同执行效果的响应获得完全不同的更新方向，产生更新波动、收敛慢、性能抖动的问题。

### 方法关键点
- 明确credit-update misalignment问题的数学本质：通过梯度分解证明错位误差来自执行等价响应组内credit与策略方向的协方差项
- 核心设计EMPO算法：先将相同上下文、相同执行效果的响应划分为同一effect cell，对cell内所有响应的长度归一化后的策略ratio取均值作为共享ratio
- 完全保留原有credit估计结果，无需额外rollout、critic或辅助模型，可兼容GRPO、GiGPO等各类轨迹级/步级credit估计器

### 关键实验结果
在ALFWorld、WebShop、Sokoban三个长horizon Agent基准上测试，对比GRPO、GiGPO等SOTA RL方案：1.5B参数下EMPO-G相对GRPO，ALFWorld成功率从69.5%提升到83.3%，WebShop成功率从62.8%提升到70.3%，训练收敛速度最多提升36.5%；所有测试场景下EMPO均稳定优于基线算法。

### 最值得记住的一句话
LLM Agent的RL优化不要只盯着credit分配做，策略更新阶段的执行等价对齐是成本极低、收益极高的优化方向
