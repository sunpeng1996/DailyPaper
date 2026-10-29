---
title: 'Conservative Dueling Bandits: Preference Learning under Baseline Constraints'
title_zh: 带基线约束的保守决斗老虎机偏好学习方法研究
authors:
- Rohan Deb
- Mohammad Ghavamzadeh
- Arindam Banerjee
affiliations:
- University of Illinois, Urbana Champaign
- Qualcomm AI Research
arxiv_id: '2610.36708'
url: https://arxiv.org/abs/2610.36708
pdf_url: https://arxiv.org/pdf/2610.36708
published: '2026-10-27'
collected: '2026-10-29'
category: RecSys
direction: 偏好学习 · 在线约束优化
tags:
- Dueling Bandits
- Preference Learning
- Conservative Learning
- Online Learning
- Constraint Optimization
one_liner: 提出两种带基线约束的保守决斗老虎机算法，在保障安全性的同时实现次线性 regret
practical_value: '- 电商搜索推荐的在线A/B测试两两对比场景，可复用基线约束逻辑，避免给用户暴露劣质候选，降低线上实验负向体验影响

  - RLHF偏好标注阶段可采用基线配对策略，fallback时仍能有效收集偏好信号，减少无效标注开销

  - 在线排序的动态探索场景，可复用基于效用差的安全验证方法，平衡探索收益和用户体验损伤'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统上下文决斗老虎机为提升偏好学习效果会激进探索，易向用户同时暴露两个劣质选项，造成体验损伤；直接迁移现有保守老虎机的安全验证方法会产生线性 regret，无法满足线上业务要求。
### 方法关键点
1. 定义安全约束：每轮展示的较优物品累积得分需不低于可信基线的$(1-\alpha)$倍，得分定义为物品击败全局最优物品的概率，无需绝对reward即可计算
2. 线性效用场景下提出MaxInP-BC算法，通过效用差做安全验证，fallback时将基线与高信息增益候选配对，保障 fallback 轮次仍能贡献学习信号
3. 通用效用场景下提出BTIGW-BC算法，基于在线逻辑回归预言机的保证生成累积安全证书
### 关键结果
两种算法均能高概率满足安全约束，无约束版本常出现约束违反；MaxInP-BC的regret为$\tilde{O}(d\sqrt{T}/\kappa)$，保守成本为不随时间步长增长的加性项；BTIGW-BC仅发生有限次fallback，在预言机逻辑回归regret为次线性时可实现次线性regret，仅需付出适中的regret代价
