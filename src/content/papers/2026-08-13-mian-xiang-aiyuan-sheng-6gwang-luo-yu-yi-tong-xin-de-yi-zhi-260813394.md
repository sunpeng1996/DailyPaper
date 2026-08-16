---
title: Heterogeneity-Aware Belief Synchronization for Semantic Communication in AI-Native
  6G Networks
title_zh: 面向AI原生6G网络语义通信的异质性感知信念同步框架
authors:
- Muhammad Hannan Akram
- Muhammad Abubakar Rashid
- Wassi Haider Kabir
- Haejoon Jung
- Kapal Dev
- Syed Ali Hassan
arxiv_id: '2608.13394'
url: https://arxiv.org/abs/2608.13394
pdf_url: https://arxiv.org/pdf/2608.13394
published: '2026-08-13'
collected: '2026-08-16'
category: MultiAgent
direction: 多智体语义通信 · 信念对齐
tags:
- MultiAgent
- Semantic Communication
- Belief Alignment
- Edge Computing
- Heterogeneous Systems
one_liner: 面向6G异构多Agent场景，提出基于MEC潜层翻译模型的低成本无联合训练信念同步框架
practical_value: '- 多Agent部署在异构算力节点（端/边/云不同规格LLM/推荐模型）时，无需强制模型同构或联合训练，可通过边侧中间翻译层实现跨模型知识同步，大幅降低架构改造成本

  - 仅在必要时同步压缩后的信念更新参数而非全量知识/原始数据，可显著降低跨节点通信开销，适合电商端边云协同推荐、多Agent导购等分布式场景

  - 潜层翻译模式不传递原始本地数据，可满足电商用户行为数据的隐私合规要求，避免跨域数据泄露风险'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
6G原生AI网络将部署大量跨星/空/边/端的异构Agent，语义通信效率高度依赖Agent间的信念对齐，但异构模型架构、差异化算力约束、本地知识异质性导致对齐难度极高，现有方案需强制模型同构或联合训练，落地成本极高。
### 方法关键点
1. 在MEC（多接入边缘计算）服务器部署潜层翻译模型，无需Agent模型同构或联合训练，即可将源Agent输出的信念更新翻译为目标Agent可识别的专属知识格式；
2. 仅在必要时交换压缩后的信念更新参数，而非全量原始数据或模型参数。
### 关键结果
多层地/非地网络案例验证显示，框架可保持极低的同步成本（以传输参数量衡量），同时异构Agent间的信念对齐误差维持在较低水平，还可兼顾隐私保护、降低本地知识漂移。
