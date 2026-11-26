---
title: Privacy-Aware Adaptive Client Selection for Federated Retrieval-Augmented Generation
title_zh: 面向联邦检索增强生成的隐私感知自适应客户端选择机制
authors:
- Ali Shams Saryazd
- Abolfazl Gandomi
affiliations:
- Yazd University
- Islamic Azad University, Yazd Branch
arxiv_id: '2611.33890'
url: https://arxiv.org/abs/2611.33890
pdf_url: https://arxiv.org/pdf/2611.33890
published: '2026-11-25'
collected: '2026-11-26'
category: RAG
direction: 联邦RAG · 隐私保护路由优化
tags:
- FedRAG
- Client Selection
- Differential Privacy
- RRF
- Semantic Matching
one_liner: 提出无需监督训练的联邦RAG自适应客户端选择方案，兼顾语义匹配、系统开销与轻量隐私保护
practical_value: '- 分布式多数据源RAG路由可复用该启发式评分框架，无需额外训练监督路由模型，快速平衡语义匹配度、历史召回贡献、延迟、通信成本和探索需求，适合跨部门/多商家的联邦检索场景

  - 多源召回结果融合时需明确定义RRF等排序融合策略的tie-breaking规则，避免随机排序导致的反馈信号偏置，影响路由策略的长期迭代效果

  - 对于有隐私合规要求的多主体协作检索场景，可参考其高斯扰动语料质心的方案，在不泄露本地语料明细的前提下完成跨源语义匹配路由'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
联邦RAG需要从分布式语料召回证据支撑生成，但全量广播查询会大幅提升多端检索计算量、通信开销，同时扩大查询信息泄露范围；现有监督式路由方案需要额外标注训练，不适用于动态异构的多主体联邦协作场景，且缺乏针对本地语料的隐私保护设计。

### 方法关键点
- 客户端侧计算本地语料嵌入均值作为质心，经高斯扰动加噪后生成对外公开的语义profile，满足差分隐私要求，避免本地语料明细泄露
- 协调侧路由评分融合5维信号：query与客户端profile的语义相似度、客户端历史证据贡献EWMA、历史检索延迟、返回payload大小、低选择频率客户端的探索bonus，加权后选择Top-K客户端
- 多源召回结果采用RRF融合，根据各客户端召回结果在全局融合列表中的留存占比计算反馈奖励，迭代更新客户端的历史贡献、延迟、payload统计值

### 关键结果
实验基于PubMedQA、BioASQ共200个生物医学问题，搭建10客户端模拟联邦环境，对比全量广播、随机选择、轮询、静态profile选择4个baseline，固定选择3个客户端的场景下：PACS-FedRAG将查询接收方减少70%，与全量广播的证据重叠率达0.372（接近0.375的结构上限），端到端回答准确率0.287与全量广播持平，端到端延迟较静态profile选择降低7%。

> 最值得记住的结论：联邦RAG路由设计需同时权衡检索效果、系统开销、隐私保护三个维度，RRF等融合策略的tie-breaking规则会直接影响路由反馈信号的有效性。
