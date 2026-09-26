---
title: 'AD-WM: Action-Discriminative World Models for Counterfactual Model Predictive
  Control'
title_zh: AD-WM：面向反事实模型预测控制的动作判别式世界模型
authors:
- Jiabin Qiu
- Zixuan Chen
- Hongye Cao
- Jieqi Shi
- Jing Huo
- Yang Gao
affiliations:
- Nanjing University
arxiv_id: '2609.30264'
url: https://arxiv.org/abs/2609.30264
pdf_url: https://arxiv.org/pdf/2609.30264
published: '2026-09-24'
collected: '2026-09-26'
category: Agent
direction: Agent 反事实规划世界模型优化
tags:
- World Model
- Model Predictive Control
- Counterfactual Reasoning
- Embedding Regularization
- Zero-shot Transfer
one_liner: 引入动作判别正则优化世界模型，提升反事实规划的动作选择精度与跨场景迁移性能
practical_value: '- 电商/广告场景做反事实评估（如不同营销动作对用户转化的影响预测）时，可引入动作恢复正则化损失，约束隐空间保留动作差异信息，避免仅优化事实预测精度导致的动作区分度不足问题

  - 训练新增的辅助头推理时可直接丢弃，不增加线上推理开销，适配推荐/广告实时决策的低延迟要求

  - 跨场景迁移决策模型可复用「冻结预训练编码器+动作判别正则」范式，在无领域适配数据的情况下提升零样本迁移性能'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有隐空间世界模型仅优化事实轨迹预测精度，无法有效区分同一状态下的不同候选动作，导致反事实MPC决策准确率不足。
### 方法关键点
1. 提出AD-WM动作判别式联合嵌入世界模型，在残差隐动力学基础上新增两类动作信息保留约束：逆动力学损失、基于条件互信息的归一化动作恢复正则项
2. 训练新增的辅助头推理时直接丢弃，不改动原有MPC逻辑，无额外推理开销
### 关键结果
- OGBench-Cube任务硬启动成功率从LeWM基线3.7%提升至52.0%，5个仿真环境中4个平均成功率优于基线
- 搭配冻结V-JEPA 2编码器时，Franka机械臂抓取零样本迁移成功率从42.2%提升至71.1%，无需领域适配
