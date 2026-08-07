---
title: 'EXCISE: Query-Side Exclusion for Late-Interaction Retrieval'
title_zh: EXCISE：晚交互检索的查询端排除约束优化方法
authors:
- Mohammed Ali
- Abdelrahman Abdallah
- Adam Jatowt
affiliations:
- University of Innsbruck
arxiv_id: '2608.05497'
url: https://arxiv.org/abs/2608.05497
pdf_url: https://arxiv.org/pdf/2608.05497
published: '2026-08-06'
collected: '2026-08-07'
category: RecSys
direction: 晚交互检索 · 否定查询优化
tags:
- ColBERT
- Late-Interaction Retrieval
- Exclusion Query
- Negation Handling
- LoRA
one_liner: 完全冻结检索索引前提下，通过轻量化查询端模块解决晚交互检索的排除查询反转问题
practical_value: '- 电商/搜索业务处理“不要XX”类否定查询时，可直接复用EXCISE架构：不改动现有召回索引，仅新增查询端1.5M参数的轻量LoRA模块识别排除主题，对top100候选重排降权，成本极低且不影响普通查询效果

  - 降权规则可直接复用：基于短列表内匹配排除主题的证据分均值+标准差做自适应阈值，无需设置全局硬阈值，避免误识别排除词时误伤正常结果；搭配最多移除3个高匹配候选的硬规则，平衡效果和安全性

  - 做否定查询评测可参考X-BENCH设计：覆盖显式否定、隐式否定、复合否定3种难度，同时加入无损害测试集验证普通查询效果，避免优化否定查询时伤及大盘指标

  - 若业务使用ColBERT类晚交互召回，无需全量重训编码器和重索引，仅训练查询端轻量化模块即可解决排除查询反转问题，ROI远高于全量微调方案'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
晚交互检索（如ColBERT）的MaxSim加法打分规则存在**排除反转**问题：用户查询中明确要排除的词汇会给匹配的文档加正向分，导致需排除的内容被排到最前面，在电商搜索、法律检索、RAG等场景下严重影响体验。现有解决方案要么需全量重训编码器、重索引成本极高，要么用交叉编码器重排效率低，且都会损害普通查询的检索效果。

### 方法关键点
- 核心思路：将学习完全限制在查询端，全程冻结检索索引，仅新增总参数量1.5M的两个轻量化模块：1）基于LoRA的排除主题检测器，识别查询中是否存在排除内容及对应语义span，无排除内容时直接返回原检索结果，无额外开销；2）排除适配器，仅对top100候选做临时重嵌入，区分候选是否匹配排除主题
- 降权机制：采用自适应阈值，基于当前短列表的证据分（候选匹配排除主题的平均相似度）均值+κ倍标准差作为cutoff，仅对超过阈值的候选施加软惩罚；额外加最多移除3个高匹配候选的硬规则，搭配防护机制避免误判时删除正常Top结果

### 关键结果
跨6个数据集、3个ColBERT backbone测试，对比冻结基线、LoRA微调、全量微调、交叉编码器等所有baseline：
1. ExcluIR数据集的exclusion success@10从0.058提升至0.691
2. Boolean NOT准确率从0.25~0.29提升至0.90~0.92
3. 在最强backbone上完全对齐原冻结模型的普通查询nDCG@10，无效果损失，而其他微调方案均存在明显的普通查询效果下降

> 最值得记住的结论：解决晚交互检索排除查询问题的核心难点不是打分规则，而是从查询中精准识别排除主题，将学习约束在查询端可在完全不改动索引的前提下，用极低成本获得远高于全量微调的效果。
