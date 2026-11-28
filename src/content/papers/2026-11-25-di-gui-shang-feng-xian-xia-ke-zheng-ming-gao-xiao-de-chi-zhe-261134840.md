---
title: Provably Efficient Offline Discounted Reinforcement Learning under Recursive
  Entropic Risk
title_zh: 递归熵风险下可证明高效的离线折扣强化学习
authors:
- Amirparsa Bahrami
- Oliver Mortensen
- Mohammad Sadegh Talebi
arxiv_id: '2611.34840'
url: https://arxiv.org/abs/2611.34840
pdf_url: https://arxiv.org/pdf/2611.34840
published: '2026-11-25'
collected: '2026-11-28'
category: Other
direction: 风险敏感离线强化学习理论分析
tags:
- Offline_RL
- Entropic_Risk_Measure
- Sample_Complexity
- PAC_Bound
- Risk_Sensitive_RL
one_liner: 首次给出递归熵风险下离线RL跨风险偏好场景的样本复杂度上下界及对应算法
practical_value: '- 若在电商/广告场景落地风险敏感离线RL策略，需限制ERM系数β的绝对值，避免样本需求指数级上升

  - 折扣因子γ不宜设置过接近1，否则会放大风险系数对样本量的要求，提升训练成本

  - 暂无配套可直接复用的工程实现方案，仅可参考其理论下界结论做落地可行性预判'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统离线RL默认采用风险中性目标，仅优化期望收益，无法满足高风险场景对收益波动的管控要求，此前递归熵风险度量(ERM)下的离线RL缺乏严谨的样本复杂度理论支撑。
### 方法关键点
针对有限状态无限horizon折扣MDP场景，同时覆盖风险厌恶(β>0)、风险寻求(β<0)两类设置，提出基于模型的ERM-VI-LCB算法，推导其PAC型样本复杂度上界，同时给出对应匹配的理论下界。
### 关键结果
首次为跨两类风险偏好的递归ERM下离线RL提供了严谨的样本复杂度保证，验证了最坏情况下样本复杂度对|β|/(1-γ)的指数依赖是不可避免的。
