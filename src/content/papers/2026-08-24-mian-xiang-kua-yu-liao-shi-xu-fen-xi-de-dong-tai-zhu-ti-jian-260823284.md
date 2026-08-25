---
title: Dynamic Topic Modeling for Cross-Corpus Temporal Analysis
title_zh: 面向跨语料时序分析的动态主题建模方法
authors:
- Ruoxuan Li
- Bruce Kogut
affiliations:
- Columbia University
- Department of Sociology and Columbia Business School, Columbia University
arxiv_id: '2608.23284'
url: https://arxiv.org/abs/2608.23284
pdf_url: https://arxiv.org/pdf/2608.23284
published: '2026-08-24'
collected: '2026-08-25'
category: Other
direction: 动态主题建模 · 跨语料时序对齐
tags:
- Dynamic Topic Modeling
- Cross-Corpus Alignment
- Temporal Analysis
- Residual Adaptation
- Topic Embedding
one_liner: 提出共享动态主题空间+语料专属残差适配的D-ETM框架，实现稳定跨语料时序主题对齐
practical_value: '- 多域内容/用户评论主题分析场景可复用「共享 backbone 冻结+域专属残差适配」范式，既保证跨域主题可比，又保留域内语义特性

  - 跨时间周期的热点趋势对齐任务可参考该架构设计，避免匈牙利匹配等后对齐方案的不稳定问题，大幅提升时序主题匹配准确率

  - 电商多场景（商品/评论/搜索query）的主题演化分析可直接借鉴该方案，统一主题索引实现跨场景趋势对比'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有Dynamic Embedded Topic Models（D-ETM）仅支持单语料时序语义演化建模，跨语料对比依赖独立训练后的后对齐操作，无法保障跨语料、跨时间维度的主题对应关系稳定性。
### 方法关键点
1. 先在合并多语料集合上训练统一动态主题空间作为共享backbone并冻结；
2. 新增语料专属残差适配层，无需创建独立隐式主题空间，既保留统一主题索引支持跨语料对比，又允许各语料适配专属词汇表达特性。
### 关键结果
在跨度97年的3个时序语料上验证：相比同backbone全微调方案，轨迹Retrieval@1从17.9±1.1%提升至97.5±0.7%，对齐效果也显著优于独立训练+后匈牙利匹配方案，同时残差适配还提升了单语料的拟合效果。
