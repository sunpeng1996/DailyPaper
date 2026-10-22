---
title: Learning Marginal Viewpoint Utility for Budgeted Evidence Selection in RAG
title_zh: 面向RAG预算约束证据选择的边际视角效用学习方法
authors:
- Yiyang Duan
- Ziqi Yu
- Tiantong Wu
- Yebo Wu
- Wei Yang Bryan Lim
affiliations:
- Nanyang Technological University
- University of Toronto
arxiv_id: '2610.29234'
url: https://arxiv.org/abs/2610.29234
pdf_url: https://arxiv.org/pdf/2610.29234
published: '2026-10-21'
collected: '2026-10-22'
category: RAG
direction: RAG 多视角上下文选择优化
tags:
- RAG
- Context Selection
- Viewpoint Coverage
- Learning to Rank
- Budget Constraint
one_liner: 提出轻量级排序器LMVU，在固定token预算下最大化RAG上下文的多视角覆盖
practical_value: '- 电商导购/问答类RAG场景可复用LMVU的边际增益排序逻辑，替代MMR做上下文选择，在固定token预算下覆盖更多商品优缺点、不同用户评价等多元视角，避免重复信息占用预算

  - 预算约束下的多样性排序可借鉴其轻量实现方案：仅用18维可离线计算的特征（相关性、候选长度、与已选集合相似度等）做线性排序，训练成本极低，推理速度接近规则方法，无需大模型打分即可落地

  - 多视角内容召回场景（如评价聚合、争议性话题导购）可复用其训练思路：用小批量开发集的视角标注做成对排序训练，无需全量标注即可迁移到不同业务数据集'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG证据选择优先高相关性内容，易出现大量高相关内容重复覆盖同一视角、其他关键视角缺失的问题，尤其在固定token预算约束下，视角覆盖不足会导致下游生成回答片面，无法满足多视角查询需求；传统MMR等多样性方法仅基于语义相似度判断冗余，无法区分语义不同但观点一致、语义相似但观点不同的情况，效果不佳。

### 方法关键点
- 核心是基于已选上下文状态，计算每个候选证据带来的边际视角覆盖增益，以此排序选择
- 训练阶段用开发集的视角标注构造同状态下的成对偏好样本（能带来新增视角的为正例，重复视角的为负例），优化成对逻辑损失，学习18维特征的权重，所有特征可复用预训练embedding计算，无额外模型依赖
- 推理阶段采用贪心迭代策略，每次选预算范围内得分最高的候选加入上下文，更新状态后重新打分，直到预算耗尽

### 关键结果
在4个多视角标注基准（WVS、Perspectrum、ArgKP、ESS10）上，1024token预算下，LMVU的RVC1（视角覆盖率）较最优非Oracle基线最高提升0.047，RVC2（双证据支持的视角覆盖率）最高提升0.052，在2个基准上达到理论视角覆盖上限；对比7B参数的RichRAG等神经排序器，LMVU训练仅需CPU秒级完成，推理开销低2个数量级，跨数据集平均表现更优。

最值得记住的结论：固定预算下的RAG上下文选择，单纯优化相关性或语义多样性远不如直接优化边际视角覆盖增益，轻量监督排序即可大幅超过复杂规则和大模型排序器的跨场景表现。
