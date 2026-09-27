---
title: 'ScalarLens: Numerical Embeddings with Stable Coordinates and Contextual Responses
  for CTR Prediction'
title_zh: ScalarLens：面向CTR预测的稳定坐标上下文感知数值嵌入方法
authors:
- Heng Yao
- Tianying Liu
- Yulou Shu
- Yong He
- Chuan Yuan
- Kaibin Qiu
- Guowei Chen
- Jiayu Zhao
- Siyun Hou
affiliations:
- Ant Group
- Alibaba Inc.
- Independent Researcher
- Henan Polytechnic University
arxiv_id: '2609.29182'
url: https://arxiv.org/abs/2609.29182
pdf_url: https://arxiv.org/pdf/2609.29182
published: '2026-09-24'
collected: '2026-09-27'
category: RecSys
direction: CTR预测 · 数值特征嵌入优化
tags:
- CTR Prediction
- Numerical Embedding
- Recommender System
- Feature Engineering
- Context-aware
one_liner: 将数值嵌入拆为稳定坐标与上下文响应两部分，27个CTR任务设置中25个取得SOTA
practical_value: '- 数值特征处理可直接复用拆分思路，无需做全局归一化，仅将特征范围存在checkpoint中，省掉训练/服务端的归一化同步成本，尤其适合多上游独立更新特征的业务场景

  - 可直接替换现有CTR pipeline中的数值嵌入模块，无需修改原有categorical分支和backbone，适配DeepFM、DCNv2等主流CTR模型，迁移成本极低

  - 稀疏/少见上下文场景下增益更高，电商大促、冷启动场景可优先尝试，相比DEER等SOTA baseline在稀有组AUC提升0.0012-0.0016

  - 工程优化后训练latency低于DEER，推理仅高13%，性能损耗可接受，适合工业级部署'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有CTR数值嵌入默认同一个标量对应唯一表征，无法适配不同上下文下同数值的预测信号差异（如Criteo数据中同一数值区间在不同上下文下CTR残差正负反转）；同时工业场景多上游特征独立更新，全局归一化需要训练/服务端同步统计量，增加运维、存储和I/O成本。

### 方法关键点
- 拆分数值嵌入为两个独立部分：①稳定坐标：仅由标量本身通过单调局部网格插值生成，上下文不参与坐标计算，支持直接输入原始数值无需预处理；②上下文响应：基于低秩算子融合类别特征与其他数值特征的上下文信息，通过固定步长有界更新生成，不改变原始坐标取值。
- 模块化设计：仅输出数值嵌入，类别特征嵌入和CTR主干网络完全无需修改，适配所有主流CTR模型架构。

### 关键实验
在AutoML-A、AutoML-E、Criteo三个公开数据集，9种主流CTR backbone（DeepFM、DCNv2、AutoInt等）共27个测试设置下，对比18种SOTA数值嵌入方案（DEER、DAES、NaryDis等），ScalarLens在25个设置排名第一，剩余2个排名第二；相比DEER平均AUC提升0.0041，稀有上下文场景AUC额外多提升0.0005以上；工程优化后训练latency低于DEER，推理仅高13%。

### 核心结论
数值嵌入应同时包含不变的坐标属性和自适应的上下文响应属性，无需让同一个表征同时承担两个角色。
