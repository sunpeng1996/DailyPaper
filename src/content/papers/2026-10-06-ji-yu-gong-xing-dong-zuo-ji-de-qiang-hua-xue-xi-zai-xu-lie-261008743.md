---
title: 'Reinforcement Learning with Conformal Action Sets: An Application to Sequential
  Recommendation'
title_zh: 基于共形动作集的强化学习在序列推荐中的应用
authors:
- Wenwen Si
- Honghao Wei
affiliations:
- University of Pennsylvania
- Washington State University
arxiv_id: '2610.08743'
url: https://arxiv.org/abs/2610.08743
pdf_url: https://arxiv.org/pdf/2610.08743
published: '2026-10-06'
collected: '2026-10-07'
category: RecSys
direction: 序列推荐 · RL共形动作集动态优化
tags:
- Reinforcement Learning
- Conformal Prediction
- Sequential Recommendation
- Slate Optimization
- Online Calibration
one_liner: 提出RLCP共形强化学习框架，动态调整推荐候选集大小，兼顾会话深度与品类多样性
practical_value: '- 可直接复用「critic价值打分+在线共形校准阈值」的动态候选集裁剪逻辑，替代固定slate size：偏好明确的成熟用户缩小候选集提升效率，冷启动/偏好模糊用户放大候选集探索潜在兴趣

  - 价值损失拆解为过滤损失+选择损失的思路可落地到推荐链路调优：单独定位召回/粗排的高价值item漏选问题、精排/重排的选品错误问题，拆分优化目标

  - 共形阈值更新规则可迁移到任意候选集规模控制场景，在预设的高价值item漏选率约束下，最小化候选集大小，降低下游排序算力消耗'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有基于RL的序列推荐普遍采用固定大小的slate，无法适配会话内用户偏好的动态变化：偏好清晰时小候选集足以覆盖需求，偏好模糊时需要更大的探索空间，固定大小既可能浪费曝光资源、限制多样性，也可能漏选高价值item，难以平衡用户长期体验与平台生态诉求。
### 方法关键点
- 提出RLCP框架，通过critic计算每个item与最优值的差距分，用在线更新的阈值裁剪动作集，空集时取分最高的item兜底，保留的动作集约束下游选品策略
- 阈值采用自适应共形校准更新：若当前集合未命中代理高价值目标则升阈值扩大候选集，反之降阈值缩小，给出路径层面的代理漏选率确定性上界，无需假设分布平稳
- 首次将序列价值损失精确分解为过滤损失（漏选高价值item）和选择损失（保留了高价值item但未被选中），无需参数收敛即可给出有限会话的奖励上界
### 关键实验
在KuaiRand-Pure、MovieLens 1M两个公开数据集上，对比DDPG、TD3、A2C、HAC 4种主流RL序列推荐基线，19组实验配置下至少1个RLCP变种取得最高catalog diversity，达最强基线的1.11×~5.21×，同时会话深度与基线持平，平均候选集大小不超过基线的固定slate规模。
### 核心结论
固定slate大小无法适配会话内的偏好动态变化，通过共形校准的动态候选集裁剪可在不损失用户会话体验的前提下，大幅提升推荐多样性，拓展平台内容生态的曝光效率。
