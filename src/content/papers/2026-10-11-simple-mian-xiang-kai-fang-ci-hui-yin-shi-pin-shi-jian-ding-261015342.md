---
title: 'SIMPLE: Semantic Structure-Aligned Prompt Learning for Open-Vocabulary Audio-Visual
  Event Localization'
title_zh: SIMPLE：面向开放词汇音视频事件定位的语义结构对齐提示学习框架
authors:
- Hanyu Xuan
- Haoran Xu
- Min Yin
- Shuo Wang
- Cheng Zhao
- Kun Li
- Fei Wang
- Zhiliang Wu
- Guanghui Yue
- Hehe Fan
affiliations:
- 安徽大学大数据与统计学院
arxiv_id: '2610.15342'
url: https://arxiv.org/abs/2610.15342
pdf_url: https://arxiv.org/pdf/2610.15342
published: '2026-10-11'
collected: '2026-10-17'
category: Multimodal
direction: 跨模态开放词汇任务 · 提示学习优化
tags:
- Prompt Learning
- Open Vocabulary
- Cross-modal Alignment
- Semantic Topology Drift
- Regularization
one_liner: 提出语义结构对齐提示学习框架解决开放词汇音视频定位的语义拓扑漂移问题，参数减半训练时间降为1/3
practical_value: '- 做开放词汇推荐/跨模态内容理解时，可引入语义拓扑一致性正则化约束可学习prompt，避免过拟合已见类目、提升泛化到未见过的商品/内容类目的能力

  - 可复用随机类目子集采样下对齐可学习prompt与手工prompt相似度分布的思路，降低prompt tuning对人工模版设计的依赖

  - 跨模态内容召回场景下，可借鉴LCPT+正则化的轻量化prompt tuning方案，减少训练参数、降低训练成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
开放词汇音视频事件定位任务中，手工prompt模板对措辞高度敏感；仅基于已见事件训练的可学习prompt易过拟合，发生语义拓扑漂移，无法泛化到未见类目。
### 方法关键点
SIMPLE语义结构对齐提示学习框架融合两大模块：1）可学习连续提示调优（LCPT）：数据驱动自动完成prompt工程，无需人工调优模板；2）语义拓扑一致性正则化（STCR）：在随机类目子集采样下，对齐可学习prompt与手工prompt的类目间相似度分布，缓解语义拓扑漂移，同时适配异步音视频流的跨模态语义对齐需求。
### 关键结果
在OV-AVEBench数据集上实现SOTA效果，可训练参数仅为原有方案的1/2，训练时间压缩至1/3，在已见、未见类目分割集上性能均最优
