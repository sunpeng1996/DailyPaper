---
title: Differentially Private Policy Optimization in Linear MDPs with Adversarial
  Rewards
title_zh: 对抗奖励下线性马尔可夫决策过程的差分隐私策略优化
authors:
- Yi He
affiliations:
- Wayne State University, Detroit, USA
arxiv_id: '2611.33469'
url: https://arxiv.org/abs/2611.33469
pdf_url: https://arxiv.org/pdf/2611.33469
published: '2026-11-24'
collected: '2026-11-28'
category: Training
direction: 差分隐私 · RL策略优化
tags:
- Differential-Privacy
- PPO
- MDP
- Policy-Optimization
- Adversarial-Reward
one_liner: 提出带联合差分隐私的批量乐观PPO算法，对抗奖励线性MDP下仅引入低阶隐私代价
practical_value: '- 面向推荐/Agent等依赖用户敏感交互数据的RL场景，可复用批量PPO+私有回归统计的JDP实现方案，兼顾隐私保护与效果损失可控

  - 对抗性reward场景（如用户行为噪声/恶意反馈）下做隐私保护策略迭代时，可参考本文regret边界计算方法评估隐私开销

  - 涉及用户敏感数据的RLHF、个性化推荐策略迭代场景，可直接复用本文低阶隐私损失的理论结论做方案可行性预判'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
个性化服务的RL流程依赖用户敏感交互数据，现有策略优化未解决轨迹重复复用、对抗性奖励依赖已发布隐私统计这两大隐私风险，需在对抗奖励线性MDP场景下实现差分隐私保护的同时控制效果损失。

### 方法关键点
融合批量PPO更新与乐观策略评估的算法，基于私有回归统计与奖励估计，在联合差分隐私（JDP）框架下同时保护用户交互轨迹与奖励函数。

### 关键结果数字
高概率regret边界主项为$	ilde{O}(K^{3/4})$，与非隐私版本批量乐观PPO完全一致；额外隐私项仅为$	ilde{O}(K^{5/8})$与$	ilde{O}(K^{1/2})$的低阶加性开销，即便在自适应对抗奖励下隐私代价也可控。
