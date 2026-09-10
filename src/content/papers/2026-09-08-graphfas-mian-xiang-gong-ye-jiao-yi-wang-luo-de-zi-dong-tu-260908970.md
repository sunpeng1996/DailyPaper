---
title: 'GraphFAS: A Distributed System for Automated Graph Feature Generation and
  Selection in Industrial Transaction Networks'
title_zh: GraphFAS：面向工业交易网络的自动图特征生成与选择分布式系统
authors:
- Yice Luo
- Yun Zhu
- Xi Chen
- Yongchao Liu
- Xintan Zeng
- Chengying Huan
- Kai Zhang
- Jinrui Zhang
- Juelu Zhang
- Jiajun Zheng
affiliations:
- Ant Group
- Nanjing University
arxiv_id: '2609.08970'
url: https://arxiv.org/abs/2609.08970
pdf_url: https://arxiv.org/pdf/2609.08970
published: '2026-09-08'
collected: '2026-09-10'
category: Other
direction: 工业图特征自动生成选择 · 风控落地
tags:
- Feature Selection
- Graph Feature Generation
- Interpretability
- Distributed Graph Mining
- Fraud Detection
one_liner: 提出无参数图特征生成与分布式改进Boruta选择框架，满足风控可解释要求已落地支付宝
practical_value: '- 做电商交易反欺诈、恶意账号挖掘时，可复用无参数多跳子图+多尺度聚合的特征生成范式，不需要训练GNN即可拿到可解释结构特征，兼容现有树模型pipeline

  - 分布式特征选择可借鉴改进Boruta的跨分区中位数聚合方案，在大规模数据下无需全量拉取数据即可稳健筛选有效特征，降低工程成本

  - 特征生成与模型训练解耦的设计思路，可迁移到需要强可解释性的推荐场景（如广告风控、内容合规召回），兼容现有TreeSHAP解释链路，无需重构整套系统'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
工业风控场景依赖专家人工构造特征成本高，易遗漏图结构关联信号；端到端GNN可解释性差，无法满足金融风控的部署与监管要求。
### 方法关键点
1. 无参数图特征生成模块：通过多跳子图提取、多尺度聚合构造显式可解释的结构特征，无训练参数；
2. 分布式特征选择算法：扩展Boruta算法，新增跨分区中位数聚合逻辑，无需过多领域知识即可在大规模数据下稳健筛选有效特征；
3. 解耦特征聚合与模型训练，可直接对接tabular模型，兼容TreeSHAP可解释链路。
### 关键结果
落地支付宝后，工程效率提升一个数量级，效果优于专家构造特征、GNN等基线。
