---
title: 'PCap: Personalized Retrieval-Stage Diversity Capping in Facebook Marketplace'
title_zh: PCap：Facebook Marketplace检索阶段个性化多样性限流框架
authors:
- Guangchao Yuan
- Janis Fuh
- Christopher Choate
- Xun Tang
- Wenqi Zhu
- Chengyi Zhang
- Pavan Kumar Paalya Chandrashekar
- Jiang Han
- Jiangyuan Li
- Hongyan Wang
affiliations:
- Meta
arxiv_id: '2609.16452'
url: https://arxiv.org/abs/2609.16452
pdf_url: https://arxiv.org/pdf/2609.16452
published: '2026-09-15'
collected: '2026-09-16'
category: RecSys
direction: 推荐系统 · 召回阶段多样性优化
tags:
- Retrieval Diversification
- Personalized Recommendation
- A-B Testing
- E-commerce Recommendation
- Online Parameter Tuning
one_liner: 在电商推荐检索阶段引入个性化多样性约束，配合自动调参显著提升用户engagement
practical_value: '- 可复用基于用户历史点击品类香农熵分桶的个性化策略，给不同偏好用户分配不同品类召回上限，检索阶段做多样性控制的延迟远低于排序阶段重排方案

  - 参数调优可复用PTS在线网格搜索思路，比贝叶斯优化更适配工业界现有A/B测试基础设施，结果透明易解释，尤其适合高维参数空间调优场景

  - 多样性优化遵循「edge-heavy」原则，重点覆盖高聚焦/高探索两类极端用户，中间用户无需额外个性化，可平衡效果与系统复杂度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐系统的反馈闭环容易导致结果同质化，过往多样性优化多在排序阶段落地，检索阶段的个性化多样性方案面临高延迟、高维参数难调的工业落地难题，且一刀切的非个性化多样性策略仅能提升曝光，无法转化为用户深度 engagement。

### 方法关键点
- 用用户近期点击的品类分布香农熵计算多样性偏好，归一化后分6个桶，解决HHI指标未考虑用户点击量的缺陷
- 检索阶段分别在分片扫描、聚合两层做品类级限流，不同偏好桶用户配置不同限流乘数：低多样性偏好用户放宽品类上限，高多样性偏好用户收紧上限以提升品类覆盖
- 采用PTS在线顺序调参框架，通过多轮小流量A/B测试缩小参数范围，自动找到各桶最优限流乘数，避免人工调参的低效问题

### 关键实验
在Facebook Marketplace开展两阶段大规模线上A/B测试，基线为无节流、统一节流。第一阶段统一节流仅VPV提升0.3088%，深度转化指标无显著提升，延迟增加8.6ms；第二阶段PCap对比统一节流，VPV提升0.2243%、PDP点击提升0.2250%、会话数提升0.1708%，额外延迟仅0.8ms，高探索用户多样性分提升0.2469%，高聚焦用户多样性分降低1.0537%，完全符合预期。

### 核心结论
多样性优化不能一刀切，个性化要重点覆盖偏好极端的用户，中间用户的个性化投入ROI极低
