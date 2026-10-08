---
title: Towards Explaining Query Expansion Performance in Information Retrieval
title_zh: 信息检索场景下查询扩展（QE）性能的归因解释研究
authors:
- Sourav Saha
- Aditya Dutta
- Soumajit Pramanik
- Mandar Mitra
affiliations:
- Indian Statistical Institute, India
- IIT Bombay, India
- IIT Bhilai, India
arxiv_id: '2610.09724'
url: https://arxiv.org/abs/2610.09724
pdf_url: https://arxiv.org/pdf/2610.09724
published: '2026-10-07'
collected: '2026-10-08'
category: QueryRec
direction: 查询扩展 · 性能归因解释
tags:
- QueryExpansion
- InformationRetrieval
- ExplainableIR
- BM25
- PerformanceAttribution
one_liner: 从理想扩展查询、正负文档可分性两个维度解释查询扩展的效果异质性
practical_value: '- 电商搜索QE选型时可引入Cohen''s d计算正负样本可分性，预判不同QE方案效果，降低全量AB测试成本

  - 可基于IEQ近似计算方法反向指导QE策略优化，筛选更接近IEQ的扩展词组合提升检索效果

  - 可针对不同query类型构建QE效果预判规则，动态选择最优QE方法，解决单方法适配性差的问题'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有QE是解决检索词汇不匹配问题的核心手段，广泛应用于包括LLM在内的现代检索系统，但没有单一QE方法能在所有query上稳定最优，QE效果异质性缺乏系统的归因框架。
### 方法关键点
1. 定义理想扩展查询（IEQ）：下游采用BM25检索时可取得最大效果的假设查询，给出可落地的近似计算方案
2. 引入可分性度量：用Cohen's d量化给定扩展查询下，相关/非相关文档的得分区分度，从两个互补维度解释QE性能差异
### 关键结果
在TREC Robust、TREC DL 2019-2022段落集、TREC DL 2019-2020文档集上验证：扩展查询与IEQ相似度越高，检索效果越好；可分性指标可补充解释IEQ覆盖不到的QE性能差异，两个维度结合可解释绝大多数QE效果波动
