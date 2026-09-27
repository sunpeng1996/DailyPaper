---
title: 'Direct Message Approximation (DMA): A Consistency-Based Framework for Tractable
  Approximate Inference on Factor Graphs'
title_zh: 直接消息近似(DMA)：因子图可处理近似推理的一致性框架
authors:
- Ralf Herbrich
- Rainer Schlosser
- Jan Lemcke
- Johann Ukrow
- Anna Kazachkova
- Nicolas Alder
- Leonhard Hennicke
- Theo Bardey
- Nico Grimm
- Luca Kleinschmidt
affiliations:
- Hasso Plattner Institute
- University of Potsdam
arxiv_id: '2609.29466'
url: https://arxiv.org/abs/2609.29466
pdf_url: https://arxiv.org/pdf/2609.29466
published: '2026-09-24'
collected: '2026-09-27'
category: Other
direction: 概率图近似推理 · 消息传递优化
tags:
- Factor-Graph
- Approximate-Inference
- Message-Passing
- BNN
- Probabilistic-Inference
one_liner: 提出直接近似因子到变量消息的DMA框架，解决现有近似消息传递算法迭代、负精度等问题
practical_value: '- 推荐系统贝叶斯建模（如不确定性感知排序、冷启动分布估计）场景，可替换现有EP/VMP消息传递算法，降低推理迭代开销

  - 冷启动、分布外样本识别需求中，可复用DMA无负精度、一致性保证的推理结果，提升稀疏场景预估可靠性

  - 用BNN做多场景鲁棒性推荐建模时，可直接复用DMA版BNN的单轮前向后向训练流程，无需调学习率超参，降低落地成本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有因子图近似消息传递算法EP、VMP需迭代轮询调度，易出现负精度消息，VMP在Dirac-delta因子下会坍缩为点估计，缺乏可证明的精度边界。

### 方法关键点
1. 直接近似因子到变量的消息而非边缘分布，针对可归一化因子定义一致性条件（其余输入为Dirac delta时输出精确）指导消息构建；
2. 证明主定理，可从消息KL边界推导边缘KL边界，自带Dirac输入一致性、无EP内循环迭代、无负精度消息三大特性；
3. 给出乘积因子反向消息$O(1/r^2)$精度保证，推导乘积、leaky-ReLU因子的显式DMA消息，实现单轮前向后向的BNN推理算法，无需学习率超参。

### 关键结果
验证DMA生成的预测不确定性在数据稀疏区域（含模型失配场景）会合理拓宽，符合概率建模预期。
