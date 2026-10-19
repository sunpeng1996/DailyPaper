---
title: Robust Reinforcement Learning for Dynamic Treatment Regimes under Model and
  Measurement Uncertainty
title_zh: 模型与测量不确定性下动态治疗方案的鲁棒强化学习框架
authors:
- Chengze Xie
- Xuan Wang
- Ying Ding
- Hairong Wang
- Yan Li
arxiv_id: '2610.22336'
url: https://arxiv.org/abs/2610.22336
pdf_url: https://arxiv.org/pdf/2610.22336
published: '2026-10-15'
collected: '2026-10-19'
category: Other
direction: 鲁棒强化学习 · 动态治疗策略优化
tags:
- Reinforcement-Learning
- Robustness
- Contextual-MDP
- Dynamic-Treatment-Regime
- Generalization
one_liner: 提出基于隐上下文鲁棒上下文MDP的RL框架，解决测量误差与环境偏移下的策略泛化与鲁棒性问题
practical_value: '- 可将用户建模为隐上下文，引入鲁棒上下文MDP解决推荐系统中用户行为观测误差、兴趣漂移导致的策略鲁棒性问题

  - 鲁棒RL训练可参考其在无误差/无漂移场景下几乎无性能损失的设计思路，平衡鲁棒性与正常场景效果

  - 多场景策略优化可借鉴其帕累托最优评估思路，兼顾不同分布偏移下的效果表现'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有动态治疗场景下的RL策略未同时覆盖观测数据误差、环境动态分布偏移两类问题，跨个体泛化性差，落地可靠性不足。

### 方法关键点
将患者个体差异建模为隐上下文，基于鲁棒上下文MDP框架统一优化策略的泛化性与鲁棒性，无需依赖完全准确的观测输入与固定环境动态假设。

### 关键结果
在经临床数据校准的转移性前列腺癌自适应治疗仿真器上测试：
1. 策略效果大幅优于现有主流AT50自适应疗法
2. 当生物标志物测量准确、疾病动态符合预期时，鲁棒性提升几乎无性能损失
3. 覆盖测量误差、动态偏移的所有测试场景中，策略均帕累托占优现有方法
