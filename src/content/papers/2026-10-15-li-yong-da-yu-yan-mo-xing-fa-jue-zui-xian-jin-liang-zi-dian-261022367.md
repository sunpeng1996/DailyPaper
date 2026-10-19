---
title: Discovering state-of-the-art quantum circuits with large language models
title_zh: 利用大语言模型发掘最先进量子电路
authors:
- Andi Gu
- Alek H. Kemeny
- Susanne F. Yelin
- Mikhail D. Lukin
affiliations:
- Harvard Quantum Initiative for Science and Engineering
- Harvard University
- Anthropic STEM Fellows Program
- Anthropic
- QuEra Computing
arxiv_id: '2610.22367'
url: https://arxiv.org/abs/2610.22367
pdf_url: https://arxiv.org/pdf/2610.22367
published: '2026-10-15'
collected: '2026-10-19'
category: LLM
direction: 大语言模型 · 量子电路演化设计
tags:
- LLM
- Evolutionary Framework
- Quantum Circuit
- Evaluator-guided Generation
- Algorithm Co-design
one_liner: 提出LLM提案+独立评估器的演化框架，在多类量子计算任务中大幅降低量子电路资源消耗
practical_value: '- 可复用「LLM生成候选+独立评估器打分迭代」的演化架构：用于电商广告文案生成、推荐素材优化等场景，LLM输出候选后用业务预估模型（如CTR、CVR模型）作为评估器，迭代筛选最优解，降低人工标注成本

  - 硬约束生成任务的设计思路可迁移：将合规、业务规则等硬约束嵌入评估器的校验逻辑，而非完全依赖LLM自身对齐，可用于电商合规文案生成、受限商品池推荐等场景，降低LLM幻觉导致的违规风险

  - 跨领域算法迁移的验证范式可参考：先将其他领域成熟算法做场景适配，再通过评估链路验证收益，可用于将NLP、CV领域的成熟模型迁移到推荐召回、排序模块的迭代过程'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
大规模量子信息处理器落地进程中，量子算法优化需满足可逆性等经典计算不存在的独特约束，传统方法优化量子计算基元的资源开销难度高。

### 方法关键点
提出演化式量子电路设计框架：由LLM自主生成电路设计候选，通过独立评估器完成正确性校验、资源开销打分，迭代筛选最优方案。

### 关键结果
覆盖数值计算、化学、优化、量子模拟、数论等8类任务测试中：
1. 7类任务生成的电路相较SOTA方案同时降低Toffoli门数量与量子比特占用
2. 第8类任务首次提出素域模逆的可逆架构，让原本不适用于可逆整数运算的经典divsteps算法可落地，大幅优化模逆任务的Toffoli门-量子比特权衡收益
