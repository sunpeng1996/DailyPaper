---
title: Expressivity and Statistical Trade-offs in Diffusion Policy Learning
title_zh: 扩散策略学习中的表达能力与统计性能权衡
authors:
- Viet Vu
- Renyuan Xu
- Jiacheng Zhang
- Yufei Zhang
arxiv_id: '2607.07967'
url: https://arxiv.org/abs/2607.07967
pdf_url: https://arxiv.org/pdf/2607.07967
published: '2026-07-08'
collected: '2026-07-13'
category: Other
direction: 扩散强化学习策略理论分析
tags:
- Diffusion Policy
- Reinforcement Learning
- Lipschitz Constraint
- Statistical Trade-off
- Policy Optimization
one_liner: 揭示扩散策略漂移Lipschitz预算K的表达性-统计复杂度权衡规律，给出落地调参准则
practical_value: '- 业务落地扩散策略做Agent决策/多候选生成时，可根据可用样本量调整漂移网络Lipschitz约束K：样本充足时调大K提升表达性，样本不足时调小K降低过拟合风险

  - 用扩散策略建模多模态动作分布（如电商Agent多路径运营动作、推荐多候选集生成）时，优先选择单侧耗散型漂移网络架构，相同样本量下收敛速率更优

  - 扩散模型调参可参考「先按样本量确定K上限，再匹配对应Lipschitz约束的神经网络结构（如加谱归一化）」的流程，避免盲目堆叠网络复杂度'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
扩散策略在强化学习中可建模复杂多模态、非高斯动作分布，但表达性的底层驱动机制、有限样本下的最优使用方法缺乏理论支撑。
### 方法关键点
1. 定义漂移项Lipschitz预算$K$为核心调控变量，量化其与策略表达性的关联：$K$-Lipschitz漂移的扩散策略值函数近似误差阶为$1/K$，且存在匹配的下界；
2. 分析$K$的统计代价：$K$越大网络泛化难度越高，需平衡近似误差与泛化误差。
### 关键结果数字
通用神经网络漂移的有限样本性能gap为$	ilde{O}(n^{-2/(m+6)})$，单侧耗散型漂移可提升到$	ilde{O}(n^{-2/(m+4)})$，其中$n$为样本量、$m$为状态空间维度；实验验证了$K$随样本量调整的权衡规律，给出根据样本量选$K$再匹配对应Lipschitz网络架构的落地原则。
