---
title: 'Calibration in One Go: Jointly Learning Accurate and Calibrated Neural Networks'
title_zh: 《一步校准：端到端联合学习高精度高校准度神经网络》
authors:
- Nektarios Kalampalikis
- Pablo M. Olmos
- Isabel Valera
affiliations:
- Saarland University, Germany
- Universidad Carlos III de Madrid, Spain
arxiv_id: '2610.13693'
url: https://arxiv.org/abs/2610.13693
pdf_url: https://arxiv.org/pdf/2610.13693
published: '2026-10-09'
collected: '2026-10-12'
category: Training
direction: 神经网络校准 · 端到端联合训练
tags:
- Calibration
- Bilevel Optimization
- End-to-End Training
- Neural Networks
- Multi-Task Learning
one_liner: 基于双层Stackelberg框架实现校准器与主干网络端到端联合训练，无需额外校准集与参数，性能超现有SOTA校准方法
practical_value: '- 推荐/广告排序模型的置信度校准可复用该端到端训练框架，无需单独拆分校准集、训练后校准模块，降低链路复杂度

  - 多任务推荐场景下可直接复用该方法避免多任务分别校准的乘法级开销，仅需新增校准器学习率1个超参

  - 分类类召回/粗排模型可直接用最后一层全连接层作为校准器，无额外参数开销即可同时提升精度与校准度'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
神经网络输出的预测概率常存在校准偏差，现有后校准方法需单独拆分校准数据集、额外训练校准模块，链路繁琐开销大，多任务场景下还会产生乘法级额外成本。
### 方法关键点
提出基于双层Stackelberg博弈的端到端联合训练框架，将现有各类后校准器与主干网络联合优化，仅用交叉熵损失即可同时优化精度与校准度，无需单独校准集、额外校准损失，仅新增校准器学习率1个超参；支持温度缩放、矩阵缩放、神经网络层等多种校准器，最优方案可直接复用模型最后一层分类层作为校准器，无额外参数。
### 关键结果
性能超越现有SOTA校准方案，仅引入可忽略的训练开销；复用最后分类层作为校准器的方案无额外推理参数与延迟，多任务场景下彻底消除独立校准带来的乘法级链路开销。
