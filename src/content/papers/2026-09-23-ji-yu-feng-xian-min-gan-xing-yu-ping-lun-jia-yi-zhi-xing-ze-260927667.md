---
title: Robust Adversarial Reinforcement Learning with Risk Sensitivity and Critic
  Consistency Regularization
title_zh: 基于风险敏感性与评论家一致性正则的鲁棒对抗强化学习
authors:
- Jiaxi Wu
- Tiantian Zhang
- Yuxing Wang
- Yongzhe Chang
- Xueqian Wang
affiliations:
- Shenzhen International Graduate School, Tsinghua University
arxiv_id: '2609.27667'
url: https://arxiv.org/abs/2609.27667
pdf_url: https://arxiv.org/pdf/2609.27667
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: 鲁棒强化学习 · 训练稳定性优化
tags:
- Reinforcement Learning
- Adversarial Training
- Robustness
- Regularization
- Q-Learning
one_liner: 提出RACER框架，通过自适应扰动与评论家一致性正则提升对抗RL的性能鲁棒性与训练稳定性
practical_value: '- 电商推荐/广告场景下基于RL的动态排序、出价策略模块，可引入状态依赖的自适应扰动机制，平衡探索鲁棒性与避免无意义流量损耗

  - 采用双critic结构的RL训练任务，可添加critic一致性正则项，降低Q值估计偏差，提升训练稳定性，适配用户偏好漂移、流量分布变化的业务场景

  - 强化学习Agent上线面临分布偏移问题时，可复用RACER的风险敏感对抗训练思路，无过多额外计算开销即可提升部署鲁棒性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
鲁棒对抗强化学习（RARL）通过最坏扰动提升序列决策鲁棒性，但存在优化不稳定、值估计退化问题：过强对抗会让Agent进入无信息失败状态，且扰动会放大双评论家分歧、引入有偏值目标，限制其在存在分布偏移的真实场景落地。
### 方法关键点
1. 推出统一框架RACER，从风险敏感视角优化对抗RL
2. 引入状态依赖的对抗目标，自适应调节扰动强度，抑制有害扰动同时保留有效探索
3. 新增评论家一致性正则，降低Q值估计器之间的分歧，稳定训练过程
### 关键结果
在连续控制基准测试中，相比SOTA鲁棒RL基线，RACER在性能、鲁棒性、训练稳定性三个维度均实现一致性提升
