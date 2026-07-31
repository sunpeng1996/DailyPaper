---
title: 'RAG-HAR+: Towards Cost-Efficient LLM-Based Human Activity Recognition for
  Edge Deployment'
title_zh: RAG-HAR+：面向边缘部署的低成本LLM人体活动识别方案
authors:
- Hansi Karunarathna
- Nirhoshan Sivaroopan
- Chamara Madarasingha
- Anura Jayasumana
- Kanchana Thilakarathna
arxiv_id: '2607.26631'
url: https://arxiv.org/abs/2607.26631
pdf_url: https://arxiv.org/pdf/2607.26631
published: '2026-07-29'
collected: '2026-07-31'
category: RAG
direction: RAG+Agent 边缘部署成本优化
tags:
- RAG
- LLM
- Cost-Optimization
- Edge-Deployment
- Agent
one_liner: 提出检索优先的RAG-HAR+框架，大幅降低边缘场景下LLM驱动HAR的推理成本同时保持精度
practical_value: '- 检索优先的推理降级策略可直接复用：召回结果置信度足够时走轻量规则（如多数投票），仅不确定样本调用LLM，大幅降本提效，适合大流量推荐/搜索场景

  - 离线Agent自动适配数据集特征的思路可迁移：针对不同业务场景（如不同品类电商推荐）自动生成适配的召回特征组，提升跨场景适配效率，减少人工特征工程

  - 边缘端RAG架构的优化思路可参考：离线预构造检索库+轻量检索逻辑前置边缘，仅少量请求回源调用大模型，降低端侧智能应用的延迟与带宽成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
传统人体活动识别（HAR）深度学习方案需数据集专属训练、大量标注数据，适配新传感器/活动分类体系成本极高；原有RAG-HAR方案重度依赖LLM推理，边缘部署的成本、延迟均无法满足落地要求。

### 方法关键点
1. 新增离线Retrieval Designer Agent，从海量运动描述符中自动生成数据集专属特征组，提升检索匹配与区分度；
2. 推理采用检索优先降级策略：高置信度检索样本直接用近邻多数投票输出结果，仅低置信度歧义样本交由LLM Ambiguity Resolver Agent处理。

### 关键结果
6个HAR基准测试中，性能与原有方案持平或更优，同时大幅降低LLM调用量、token消耗与推理延迟，已验证移动端边缘部署可行性。
