---
title: Regularised RL improves sim-to-real transfer
title_zh: 正则化强化学习提升仿真到现实的迁移效果
authors:
- Danilo Vucetic
- Mohamad H. Danesh
- Florence Clerc
- Hsiu-Chin Lin
- Jonathan Tremblay
affiliations:
- Université de Montréal
- McGill University
- Mila - Québec AI Institute
- Polytechnique Montréal
- NVIDIA
arxiv_id: '2610.32855'
url: https://arxiv.org/abs/2610.32855
pdf_url: https://arxiv.org/pdf/2610.32855
published: '2026-10-23'
collected: '2026-10-26'
category: Training
direction: 强化学习训练 · sim-to-real迁移优化
tags:
- Reinforcement Learning
- Regularization
- Sim-to-Real
- Actor-Critic
- Robustness
one_liner: 提出基于soft mellowmax的正则化RL算法SMM-AC，提升sim-to-real迁移鲁棒性与实际部署表现
practical_value: '- 推荐/广告系统离线训练到线上部署的gap优化场景，可借鉴强正则化RL思路，提升策略对线上流量扰动、环境动态变化的鲁棒性，缓解离线效果好、线上表现差的问题。

  - 交互类Agent（如电商导购Agent、流量调度Agent）训练时，可引入soft mellowmax值函数替代传统softmax，增强策略对观测噪声、用户行为波动的抗干扰能力。

  - 做RL4Rec的策略预训练验证时，可参考本文鲁棒性评估范式，新增观测扰动、环境动态变化的测试case，提前预判上线风险。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前sim-to-real场景默认使用PPO等弱正则化RL算法，正则化对迁移效率的实际增益缺乏明确量化；且真实部署中策略需要应对仿真无法穷尽的观测、环境、动态扰动，对鲁棒性要求极高。

### 方法关键点
1. 提出新型正则化RL算法SMM-AC，基于soft mellowmax值函数设计，具备强鲁棒性理论保障；
2. 系统性对比不同正则化强度RL算法的sim-to-real表现，量化正则化的实际作用。

### 关键结果
- MuJoCo连续控制基准上，SMM-AC性能与SAC等基线持平；
- 真实机器人部署中，SMM-AC取得更高回报，对观测、环境、动态扰动的鲁棒性显著优于基线，验证强正则化RL可有效缓解sim-to-real gap，适配真实世界动态变化条件。
