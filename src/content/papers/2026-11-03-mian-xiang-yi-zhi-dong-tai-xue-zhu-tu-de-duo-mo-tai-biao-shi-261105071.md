---
title: Dataset Recommendation for Heterogeneous and Dynamic Scholarly Graphs via Multimodal
  Representation Learning
title_zh: 面向异质动态学术图的多模态表示学习数据集推荐方法
authors:
- Ornella Irrera
- Matteo Lissandrini
- Daniele Dell'Aglio
- Gianmaria Silvello
affiliations:
- University of Padua, Italy
- University of Verona, Italy
- Aalborg University, Denmark
arxiv_id: '2611.05071'
url: https://arxiv.org/abs/2611.05071
pdf_url: https://arxiv.org/pdf/2611.05071
published: '2026-11-03'
collected: '2026-11-05'
category: RecSys
direction: 异质图推荐 · 多模态表示学习
tags:
- Heterogeneous Graph
- Multimodal Embedding
- Graph Representation Learning
- Inductive Recommendation
- Cold Start
one_liner: 提出融合拓扑与文本嵌入的MM-SAN多模态图模型，实现动态异质学术图下无需重训练的高鲁棒数据集推荐
practical_value: '- 异构图推荐场景可复用「拓扑感知嵌入+文本嵌入融合」架构，解决侧信息缺失场景的推荐效果退化问题

  - 动态更新推荐场景（如电商新品/新用户冷启动）可借鉴其无需重训练的归纳推理设计，降低服务运维成本

  - 多模态特征融合可参考其注意力加权机制，平衡不同模态信息贡献权重，提升弱模态场景下的模型鲁棒性'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
学术知识图（SKG）规模大、结构异质、动态更新频繁且普遍存在元数据缺失/错误问题，现有数据集推荐方案依赖完整元数据或静态图假设，难以适配动态SKG场景，导致大量数据集孤立未被复用，人工检索效率低、漏检率高。

### 方法关键点
提出Multimodal Scholarly Attention Network（MM-SAN）异质多模态图表示学习模型：1）融合拓扑感知图嵌入与文本语义嵌入，无需依赖完整元数据即可生成有效表征；2）原生支持直推、半归纳、全归纳三种推理模式，SKG新增节点/边时无需重新训练即可适配动态变化。

### 关键结果
实验效果全面超越同领域SOTA方案，可支撑大规模动态异质图下的高鲁棒、可扩展数据集推荐任务。
