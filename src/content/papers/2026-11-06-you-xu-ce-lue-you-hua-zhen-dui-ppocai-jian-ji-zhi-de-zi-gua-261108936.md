---
title: Ordered Policy Optimization
title_zh: 有序策略优化：针对PPO裁剪机制的自适应改进方法
authors:
- Dongkyu Derek Cho
- Pan Xu
affiliations:
- Duke University
- Department of Statistical Science, Duke University
- Department of Biostatistics & Bioinformatics, Duke University
- Department of Computer Science, Duke University
- Department of Electrical & Computer Engineering, Duke University
arxiv_id: '2611.08936'
url: https://arxiv.org/abs/2611.08936
pdf_url: https://arxiv.org/pdf/2611.08936
published: '2026-11-06'
collected: '2026-11-09'
category: Training
direction: 强化学习训练 · 策略优化
tags:
- PPO
- Policy Optimization
- Reinforcement Learning
- Importance Sampling
- Training Optimization
one_liner: 改进PPO固定裁剪机制，按小批量重要性比排序给极端值分配自适应样本级裁剪半径
practical_value: '- 做LLM RLHF、Agent策略调优时，可替换原有PPO的固定裁剪逻辑，对每个minibatch的重要性比排序后给极端值自适应裁剪阈值，降低训练抖动

  - 电商推荐/广告的在线RL调优场景（如排序策略迭代、出价优化）可复用该思路，减少极端样本对策略更新的负向干扰

  - 工程实现成本极低，仅需新增minibatch排序和损失计算逻辑，无需改动原有PPO训练Pipeline，可快速AB验证'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
PPO通过裁剪新旧策略的重要性比稳定更新，但全局固定裁剪阈值无法区分统计有害的极端比值与可容忍的大幅比值变化，易导致更新不稳定。
### 方法关键点
1. 提出Ordered Policy Optimization（OPO），每个minibatch内先对重要性比排序，筛选对更新影响最大的极端比值
2. 基于预设尾分布轮廓为极端比值分配逐样本的自适应裁剪半径，替代全局固定阈值
3. 优化目标保持一阶特性，仅新增minibatch排序和策略损失修改，实现成本极低
### 关键结果
在MuJoCo、Atari标准强化学习基准测试中，相比主流基线方法取得更优性能，代码已开源
