---
title: Language-Critique Imitation Learning from Suboptimal Demonstrations
title_zh: 基于语言批评框架的次优演示模仿学习方法
authors:
- Chih-Han Yang
- Dai-Jie Wu
- Yun-Ping Huang
- Ping-Chun Hsieh
- Kenneth Marino
- Shao-Hua Sun
affiliations:
- National Taiwan University
- University of Utah
- National Yang Ming Chiao Tung University
- NTU Artificial Intelligence Center of Research Excellence
arxiv_id: '2607.01225'
url: https://arxiv.org/abs/2607.01225
pdf_url: https://arxiv.org/pdf/2607.01225
published: '2026-07-01'
collected: '2026-07-02'
category: Training
direction: 模仿学习 · 结构化语言监督训练
tags:
- Imitation Learning
- Language Supervision
- Suboptimal Demonstration
- Behavior Cloning
- Diffusion Policy
one_liner: 提出以自然语言结构化反馈替代标量监督的次优演示模仿学习框架，性能超越现有基线
practical_value: '- 处理电商/推荐场景的次优业务行为数据（如非最优推荐策略、用户低质交互轨迹）时，可引入自然语言结构化标注（如"该推荐未匹配用户价格偏好""该召回遗漏高转化商品"）替代传统标量权重（如置信度、重要性权重），保留更多优化信息

  - 训练推荐/广告策略模型时可借鉴语言批评损失设计，直接用结构化文本监督训练，避免将多维度反馈压缩为单标量导致的信息损失，适配行为克隆、扩散策略等多种建模范式

  - 做离线RL优化推荐/广告策略时，可复用本框架的理论结论，基于结构化语言反馈的训练目标可对专家性能差距做上界约束，降低策略迭代的不确定性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统次优演示模仿学习依赖置信度、判别器分数、重要性权重等标量监督信号，无法显式表达任务进度、失败模式、修正动作等中间推理信息，压缩反馈的信息损失大，难以训练鲁棒策略。
### 方法关键点
1. 提出语言批评模仿学习框架，从演示中构建自然语言标签，显式描述当前进度、识别次优行为、输出细粒度修正指导，避免反馈压缩为标量的信息损失；
2. 设计语言批评损失，直接用结构化语言信号训练策略，无需降维为标量，分别适配行为克隆与扩散策略，得到LC-BC和LC-DP两种实现；
3. 理论证明标准假设下，该训练目标是专家性能差距的上界。
### 关键结果
在导航、机械臂操控、游戏等多类连续控制任务上，LC-BC、LC-DP均稳定超越强imitation learning与离线强化学习基线
