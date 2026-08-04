---
title: 'Structured Memory for Edge Language Models: Persistent Context and Corpus
  Retrieval via O(1) SSM State Injection'
title_zh: 面向边缘SSM大模型的O(1)结构化记忆与预计算上下文注入机制
authors:
- Anusha Madan Gopal
- Aras Pirbadian
- Kristofor D. Carlson
- M Anthony Lewis
- Jonathan Tapson
affiliations:
- BrainChip Inc.
arxiv_id: '2608.02560'
url: https://arxiv.org/abs/2608.02560
pdf_url: https://arxiv.org/pdf/2608.02560
published: '2026-08-03'
collected: '2026-08-04'
category: RAG
direction: RAG 边缘侧SSM隐状态复用优化
tags:
- SSM
- RAG
- Edge Inference
- KV cache
- State Injection
- Latency Optimization
one_liner: 通过预计算SSM隐状态实现O(1) RAG上下文注入，边缘侧预填充延迟降4500倍且效果无损
practical_value: '- 若用Mamba等SSM架构做端侧电商导购Agent、个性化推荐、客服系统，可直接复用PRECOG思路：预编码商品库、用户历史、知识库为SSM隐状态，RAG预填充延迟从秒级降至毫秒级，无效果损失

  - 端侧个性化推荐可复用SMC分层记忆机制：将用户短期交互、长期偏好预编码为不同层级隐状态，会话启动O(1)直接注入，无需每次重跑用户长历史序列

  - 现有Transformer RAG面临KV缓存膨胀、预填充慢问题的团队，可参考SSM架构的RAG工程优势：同规模下SSM隐状态存储比Transformer
  KV缓存低85倍，长上下文场景优势更显著'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Transformer架构RAG存在两大核心瓶颈：KV缓存随上下文长度线性增长、位置纠缠导致缓存无法跨上下文复用，边缘侧部署时RAG预填充延迟高达几十秒，无法满足交互式体验要求；SSM虽天生解决KV缓存膨胀问题，但仍需逐token重灌检索上下文，预填充开销仍与上下文长度正相关。
### 方法关键点
- 提出PRECOG机制：离线预编码所有语料chunk为SSM固定大小隐状态，查询时通过轻量语义索引召回匹配隐状态直接注入SSM初始状态，完全跳过上下文重灌，预填充开销从O(L)降至O(1)
- 提出SMC结构化记忆巩固机制：分层存储用户交互的短期episodic状态与长期semantic状态，支持可调的精度-存储tradeoff，会话启动直接注入对应领域长期记忆状态，开销同样为O(1)
- 理论证明单chunk注入效果与原生in-context RAG完全等价，无精度损失，该特性仅SSM等位置无关循环架构可实现，Transformer因位置纠缠从架构上无法支持
### 关键结果
在SQuAD v1.1数据集上测试，1.2B参数TENNs-SSM底座，边缘硬件上PRECOG预填充延迟从~27s降至<6ms，加速约4500倍，EM、F1指标与原生in-context RAG仅差0.2，在FP16量化误差范围内；SSM单chunk隐状态存储仅192KB，比同规模Transformer KV缓存小85倍。
**最值得记住的一句话**：SSM的位置无关固定大小隐状态特性，可实现Transformer架构从数学上不可能做到的跨上下文隐状态复用，是边缘侧低延迟RAG/Agent部署的核心优势方向。
