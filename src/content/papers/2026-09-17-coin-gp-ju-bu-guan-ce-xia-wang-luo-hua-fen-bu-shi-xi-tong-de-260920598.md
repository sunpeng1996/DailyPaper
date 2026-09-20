---
title: 'COIN-GP: Cooperative Online Learning in Networked Distributed Systems with
  Partial Measurements via Gaussian Process Regression'
title_zh: COIN-GP：局部观测下网络化分布式系统的高斯过程协同在线学习
authors:
- Zewen Yang
- Xiaobing Dai
- Zhenxiao Yin
- Hang Zhao
- Zhijun Li
- C. C. Chan
affiliations:
- Chair of Robotics and Systems Intelligence, Munich Institute of Robotics
- Technical University of Munich
arxiv_id: '2609.20598'
url: https://arxiv.org/abs/2609.20598
pdf_url: https://arxiv.org/pdf/2609.20598
published: '2026-09-17'
collected: '2026-09-20'
category: Other
direction: 分布式系统协同学习 · 高斯过程回归
tags:
- Gaussian-Process
- Distributed-Learning
- Online-Learning
- Cooperative-Learning
- State-Estimation
one_liner: 提出融合在线分布式GP回归的协同学习框架，解决局部观测下分布式系统状态与未知动态联合估计问题
practical_value: '- 分布式GP的误差上界推导逻辑可复用在联邦推荐场景的局部模型偏差量化，优化跨节点模型融合策略

  - 局部观测下的协同数据采集规则可借鉴到多端用户行为数据补全，降低全量埋点的采集成本

  - 在线分布式GP协同更新框架可迁移至多Agent协同感知场景，提升局部观测下的联合决策准确率'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前传感器网络、多机器人等网络化分布式系统的协同学习场景中，普遍仅能获取局部状态观测、且系统动态存在部分未知，传统状态观测器依赖完全已知的系统动态，无法适配离散非线性系统的联合状态与未知函数估计需求。
### 方法关键点
1. 提出基于观测器的动态协同学习框架COIN-GP，融合在线分布式高斯过程（GP）回归，可在测量不完整、GP模型存在缺陷的情况下仍实现准确估计
2. 设计全新数据采集策略，给出理论可行的数据采集约束条件，保证训练数据有效性
3. 基于GP的确定性误差边界，推导得到同时覆盖状态估计、模型估计的整体误差上界，提供可解释的效果保障
### 关键结果
仿真实验验证，相比现有分布式GP类基线方法，该方案在局部观测场景下的状态与动态估计精度显著更优
