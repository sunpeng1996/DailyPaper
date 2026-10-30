---
title: 'Beyond IPS: Reliable Counterfactual Evaluation in Multi-Stage Ad Systems without
  Logged Propensities'
title_zh: 无需记录曝光倾向的多阶段广告系统可靠反事实评估方法
authors:
- Mohsen Malmir
- Mohamed A. Radwan
- Houssam Nassif
- Murat Ali Bayir
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2610.40112'
url: https://arxiv.org/abs/2610.40112
pdf_url: https://arxiv.org/pdf/2610.40112
published: '2026-10-29'
collected: '2026-10-30'
category: Eval
direction: 推荐系统 · 反事实离线评估
tags:
- Counterfactual Evaluation
- Off-Policy Evaluation
- Ad Ranking
- Direct Method
- Doubly Robust
one_liner: 提出混合加权奖励建模框架，无需记录倾向即可实现多阶段广告系统可靠反事实评估
practical_value: '- 多阶段电商/广告推荐系统无曝光倾向日志时，可直接复用混合加权奖励建模方案替代IPS类方法，通过多分类域分类器估计密度比加权训练reward
  model，缓解候选策略与历史日志的分布偏移

  - 可复用论文提出的冷启动质量µj(τ)作为离线评估可靠性诊断指标，当最大冷启动质量低于预设regret预算时直接信任离线排序结果，否则送入在线A/B测试，大幅节省实验流量

  - 密度比权重裁剪阈值可参考经验值：低重叠场景选c=20~100，高重叠场景可选更小的c，同时监控ESS/n指标判断分布偏移程度，避免长尾权重破坏训练稳定性

  - 离线策略排序优先选择混合加权DR方案：低/中重叠场景Top-1准确率比未加权DR高3~8pct，生产环境Top-1准确率达0.44，远高于随机选择的0.2'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多阶段广告/推荐系统的离线反事实评估是上线前风险管控、实验流量优先级筛选的核心环节，但传统IPS类方法依赖的曝光倾向因多阶段链路的拍卖、过滤、业务规则等未记录操作无法获取，而直接方法(DM)因候选策略和日志数据的分布偏移存在严重预测偏差，亟需无需记录倾向的可靠评估方案。
### 方法关键点
- 提出混合加权奖励建模：将所有候选策略的分布混合作为目标分布，通过多分类域分类器区分日志策略和候选策略生成的曝光，估计混合分布到日志分布的密度比作为样本权重训练reward model，降低分布偏移带来的误差
- 推导DM评估的误差上界，分解为重叠误差、冷启动误差、重放采样误差三类，基于冷启动质量（候选策略生成的曝光中日志数据无支撑的比例）给出渐近路由规则：当冷启动质量低于regret预算时信任离线结果，否则走A/B测试
- 结合DR修正进一步降低偏差，通过密度比权重裁剪+ESS指标监控避免长尾权重影响训练稳定性
### 关键结果
在广告模拟器（7万条曝光）和Meta大规模CTR排序生产流量上对比6类基线：模拟器低重叠场景（ESS<0.4）下混合加权DR的Top-1准确率达0.90，比未加权DR高8pct，比IPS高30pct，Value MAE%仅1.71%；生产环境中混合加权DR的Top-1准确率达0.44，比未加权DR高6pct，远高于随机选择的0.2。

最值得记住的结论：多阶段推荐/广告系统的离线评估可靠性上限由候选策略与日志数据的重叠度决定，低重叠场景下的候选必须送入在线A/B测试，仅靠离线数据无法消除冷启动误差。
