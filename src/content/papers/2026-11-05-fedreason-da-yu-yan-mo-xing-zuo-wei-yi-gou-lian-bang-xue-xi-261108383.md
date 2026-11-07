---
title: 'FedReason: Large Language Models as Weight-Space Meta-Aggregators for Heterogeneous
  Federated Learning'
title_zh: FedReason：大语言模型作为异构联邦学习的权重空间元聚合器
authors:
- Ali Mohammadi Ruzbahani
- Abbas Yazdinejad
- Hadis Karimipour
affiliations:
- University of Calgary
- University of Regina
arxiv_id: '2611.08383'
url: https://arxiv.org/abs/2611.08383
pdf_url: https://arxiv.org/pdf/2611.08383
published: '2026-11-05'
collected: '2026-11-07'
category: Training
direction: 联邦学习 · LLM自适应权重聚合
tags:
- Federated Learning
- LLM
- Model Aggregation
- Heterogeneous FL
- Meta Aggregator
one_liner: 无需服务端训练，用LLM自适应选择异构联邦学习场景下的最优模型聚合规则
practical_value: '- 隐私合规要求的跨端联邦推荐场景，可复用LLM自适应聚合规则思路，无需提前适配不同数据/模型异构场景，降低规则开发成本

  - 工业级LLM驱动系统可复用降级方案：LLM输出非法时自动fallback到基线规则，避免系统崩溃，保障服务稳定性

  - 小批量proxy验证集打分筛选候选策略的trick可复用，大幅降低全量评估的计算开销，适合推荐系统快速迭代场景'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
传统联邦学习采用固定聚合规则，每类规则仅适配单一异构场景，部署前无法预判场景匹配度，且服务端训练定制规则成本高。
### 方法关键点
1. 每10轮调用1次LLM，服务端沙箱内运行代码分析客户端模型权重，仅返回打印结果给LLM，不泄露全量权重；
2. LLM基于500样本的proxy集对候选规则打分，输出Python聚合程序，输出非法时自动fallback到FedAvg。
### 关键结果
168次实验对比14个基线，标签偏移场景下平均精度比FedAvg高1.26pp（12次实验赢10次），比同预算的固定规则选择对照组高1.08pp；10个客户端含3个恶意节点时，首轮即可排除所有符号翻转攻击客户端，精度仅比需根模型训练的FLTrust低1pp；60轮训练平均API成本仅0.79美元，无proxy反馈时精度从73.8%暴跌至38.8%。
