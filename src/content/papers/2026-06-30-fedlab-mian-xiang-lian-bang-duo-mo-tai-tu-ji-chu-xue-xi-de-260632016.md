---
title: 'FedLAB: Traceable Semantic Codebooks for Federated Multimodal Graph Foundation
  Learning'
title_zh: FedLAB：面向联邦多模态图基础学习的可追踪语义码本
authors:
- Zekai Chen
- Kairui Yang
- Xuaner Chen
- Xunkai Li
- Xun Wu
- Rong-Hua Li
- Guoren Wang
affiliations:
- Beijing Institute of Technology
arxiv_id: '2606.32016'
url: https://arxiv.org/abs/2606.32016
pdf_url: https://arxiv.org/pdf/2606.32016
published: '2026-06-30'
collected: '2026-07-01'
category: Training
direction: 联邦多模态图基础模型训练
tags:
- Federated Learning
- Multimodal Graph
- Semantic Codebook
- Foundation Model
- Traceable Learning
one_liner: 提出分层可追踪语义码本框架FedLAB，在隐私约束的联邦多模态图场景下兼顾性能与语义可追溯
practical_value: '- 跨商家/跨区域的联邦多模态电商推荐场景可复用分层语义码本设计，分别对模态特征、节点语义、拓扑上下文独立编码，兼顾隐私保护与语义可解释性

  - 联邦训练阶段的语义重心预训练策略可直接迁移，无需回传原始数据与图结构，仅传递码本单元更新即可降低跨节点传输成本与隐私泄露风险

  - 可追溯语义码本可复用至推荐决策归因场景，快速定位推荐结果的触发来源（商品模态/用户语义/行为拓扑），提升推荐可解释性与合规性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
多模态图基础模型需融合文本、图像、属性、拓扑等多源信息，但工业场景中多模态图往往分散在不同独立客户端，受隐私合规约束无法集中共享原始数据与结构；现有联邦学习方案通过参数、原型、嵌入等传递知识，无法追溯模态证据、节点语义、拓扑上下文对预测结果的贡献，缺乏可解释性。

### 方法关键点
提出FedLAB可追踪语义码本框架，将多模态图知识拆解为模态证据、节点语义、拓扑上下文三类分层结构化码本；采用联邦语义重心预训练策略迭代优化码本单元，全程保留原始多模态内容与图结构在本地，无原始数据泄露风险。

### 关键结果
在10个基准数据集、6个下游任务上验证，FedLAB相比SOTA基线性能最高提升7.53%，同时自带原生语义追溯接口，支持全链路决策归因。
