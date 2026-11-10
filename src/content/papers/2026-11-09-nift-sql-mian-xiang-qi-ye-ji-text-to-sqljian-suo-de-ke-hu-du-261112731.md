---
title: 'NIFT-SQL: Customer-Supervised Table Scoring for Enterprise Text-to-SQL Retrieval'
title_zh: NIFT-SQL：面向企业级Text-to-SQL检索的客户监督表打分方法
authors:
- Arjun Rao
- Nishant Gopinath
affiliations:
- SAP
arxiv_id: '2611.12731'
url: https://arxiv.org/abs/2611.12731
pdf_url: https://arxiv.org/pdf/2611.12731
published: '2026-11-09'
collected: '2026-11-10'
category: RAG
direction: 企业级Text-to-SQL · 表检索排序融合
tags:
- Text-to-SQL
- Table Retrieval
- Cross-encoder
- Rank Fusion
- Zero-shot Reranker
one_liner: 融合客户微调检索器、交叉编码器与重排器，大幅提升企业级Text-to-SQL的表召回准确率
practical_value: '- 企业级多库多表检索场景可复用「客户侧微调检索器+560M小参数交叉编码器重排+逻辑回归融合」架构，平衡效果与推理成本

  - 无标注场景可引入按库路由的零样本8B重排器，将其得分作为额外融合特征可提升5~7个百分点的complete@15指标

  - 资源受限场景可直接使用按库分组的排序融合替代逻辑回归融合，二者效果无显著差异，可省去融合模型训练成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
企业级Text-to-SQL的核心瓶颈是跨库数百个歧义表的精准召回，现有通用检索方案准确率极低，严重制约下游SQL生成效果。
### 方法关键点
1. 基于客户侧标注问题微调检索器做混合搜索，搭配560M微调交叉编码器对全量表做必要性打分；
2. 用留存问题训练逻辑回归模型融合两路检索得分；
3. 可扩展加入按库路由的零样本8B重排器得分作为额外特征进一步提优，也支持无训练的按库分组排序融合方案。
### 关键结果
在BEAVER、LiveSQLBench、LiveSQLBench-Large（244~971张表）上，complete@15分别达69.2%、89.5%、85.6%，较纯混合搜索提升38.8~63.8个百分点，较同标注微调检索器提升8.1~15.2个百分点；加入零样本重排特征后complete@15进一步提升至72.4%、92.5%、88.6%。
