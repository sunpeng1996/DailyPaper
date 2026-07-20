---
title: 'Scientific Claim-Source Retrieval Revisited: A Comparative Study of Style
  Transfer and Re-Ranking'
title_zh: 科学主张来源检索再探：风格迁移与重排序对比研究
authors:
- Tobias Schreieder
- Harsh Khandelwal
- Yu-Ling Zhong
- Michael Färber
affiliations:
- TU Dresden & ScaDS.AI Dresden/Leipzig
- Friedrich-Alexander University of Erlangen–Nuremberg
arxiv_id: '2607.15875'
url: https://arxiv.org/abs/2607.15875
pdf_url: https://arxiv.org/pdf/2607.15875
published: '2026-07-17'
collected: '2026-07-20'
category: RAG
direction: RAG召回优化 · 跨风格跨语言检索
tags:
- Retrieval
- Style Transfer
- Re-Ranking
- Fact Verification
- Multilingual
one_liner: 对比多类检索、风格迁移、重排序方案，实现科学主张来源检索MRR@5达0.758的最优性能
practical_value: '- 跨风格/跨语言检索场景可先将query统一翻译为候选库覆盖最广的语言（如电商场景的目标市场主流语言），效果优于原语言/双语表征，可快速提升召回基线

  - 召回前置可增加风格迁移模块，将用户自然语言query转换为与候选库（如商品标题、内容摘要）匹配的风格，适配不同检索目标时灵活调整风格策略即可获得性能增益

  - 重排序阶段可在语义相似度基础上叠加实体重叠、业务场景相关的推理信号（如电商场景的属性匹配、口碑验证信号），分层重排序的架构可直接复用'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
社交媒体传播的科学主张与原始来源文献在语言、表述风格、信息颗粒度上差异极大，自动化溯源召回难度高，现有技术方案缺乏系统性对比与最优选型指引。
### 方法关键点
基于CheckThat! 2026基准，系统对比稀疏、稠密两类检索模型的效果，测试多语言表征策略、4类风格迁移方案对召回性能的影响；提出归因、实体重叠、验证式推理3类新型重排序模型，对比传统语义相似度重排序的效果差异。
### 关键结果
1. 非英语主张统一翻译为英语的表征效果优于原语言、双语表征，引入来源元数据可进一步获得召回收益；
2. 风格迁移对多数检索模型均有性能提升，最优风格选择与检索目标强相关；
3. 验证式推理重排序效果远超纯语义相似度方案，整体最优系统MRR@5达0.758
