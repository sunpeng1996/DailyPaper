---
title: 'TOOD: Task-Aware Out-of-Distribution Score Calibration for Continual Learners'
title_zh: TOOD：面向持续学习模型的任务感知OOD分数校准方法
authors:
- Mostafa ElAraby
- Samer B. Nashed
- Liam Paull
affiliations:
- Mila - Quebec AI Institute
- Université de Montréal
- CIFAR
arxiv_id: '2607.29592'
url: https://arxiv.org/abs/2607.29592
pdf_url: https://arxiv.org/pdf/2607.29592
published: '2026-07-31'
collected: '2026-08-03'
category: Training
direction: 持续学习 · OOD检测分数校准
tags:
- Continual Learning
- OOD Detection
- Score Calibration
- Post-hoc Method
- Energy-based Detection
one_liner: 提出无训练的事后校准方法TOOD，缓解持续学习场景下OOD检测性能退化
practical_value: '- 推荐系统持续更新新类目/新场景时，可复用TOOD的无训练后处理思路校准OOD分数，避免误判未知类目请求，无需重新训练全量模型

  - 多任务排序模型迭代时，可基于replay buffer统计值校准不同任务的分类置信度，缓解新增任务带来的旧任务OOD检测性能下降

  - 电商Agent的用户意图识别模块，可借鉴分任务能量分数分解思路，快速区分未知意图请求，降低错误响应率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
持续学习（CL）系统需同时保留旧任务性能、检测OOD输入，但现有CL方案普遍存在OOD检测遗忘（OODF）问题，且OODF与旧任务分类性能弱负相关，背后机制独立于分类遗忘：能量类OOD检测器存在置信度Gap，特征类检测器存在流形拥挤问题。

### 方法关键点
TOOD是无训练的事后校准方法，将logits拆解为分任务能量分数，利用replay buffer的统计值完成分数重校准，无需修改模型结构或训练流程。

### 关键结果数字
在CIFAR-10、CIFAR-100、100任务的ImageNet-1K流上测试，多数场景下OOD检测性能优于未校准的能量基线，10组CIFAR配置中8组排名前二，置信度Gap严重时增益最大，证实OOD退化主要来自分数校准误差而非判别结构丢失。
