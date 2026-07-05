---
title: 'WorldSample: Closed-loop Real-robot RL with World Modelling'
title_zh: WorldSample：结合世界建模的闭环真实机器人强化学习框架
authors:
- Yuquan Xue
- Le Xu
- Zeyi Liu
- Zhenyu Wu
- Zhengyi Gu
- Xinyang Song
- Bofang Jia
- Ziwei Wang
affiliations:
- Nanyang Technological University
- Tsinghua University
- Central South University
- Beijing University of Posts and Telecommunications
arxiv_id: '2607.02431'
url: https://arxiv.org/abs/2607.02431
pdf_url: https://arxiv.org/pdf/2607.02431
published: '2026-07-02'
collected: '2026-07-05'
category: Other
direction: 实体机器人 · 强化学习数据增强
tags:
- Reinforcement Learning
- World Model
- Data Augmentation
- Robotics
- Policy Training
one_liner: 提出基于真实交互轨迹的世界模型数据增强框架，降低实体机器人RL训练成本并提升策略性能
practical_value: '- 真实+合成闭环数据生成思路可迁移到推荐系统RL训练：用真实用户交互数据打底生成合成训练样本，降低纯仿真数据的分布偏移问题

  - Policy-Paced Learning的动态样本调度机制可复用：在推荐排序/广告出价的RL训练中，动态筛选合成样本，平衡数据增益与价值高估风险，避免噪声干扰

  - 世界模型后训练校准方法可迁移到RAG/生成式推荐场景：基于真实交互样本校准生成结果，大幅降低大模型幻觉'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
实体机器人部署强化学习（RL）面临交互成本极高的瓶颈，单条物理交互轨迹仅能覆盖单条动作-结果路径，纯模仿学习又受演示数据覆盖度限制难以泛化。
### 方法关键点
1. 构建真实交互-世界模型生成-策略优化的闭环数据增强框架，基于真实交互轨迹后训练世界模型，生成高保真合成状态转移样本，大幅降低视觉幻觉
2. 引入Policy-Paced Learning（PPL）机制，通过样本选择和调度动态调控训练过程，平衡数据增强收益与价值高估风险，缓解幻觉带来的噪声干扰
### 关键结果
机器人接触式精细操作任务上，相比基线策略成功率提升28%，训练步数减少59%；世界模型视觉保真度相比仅用演示数据训练的方案，PSNR提升19.4dB，SSIM提升0.47
