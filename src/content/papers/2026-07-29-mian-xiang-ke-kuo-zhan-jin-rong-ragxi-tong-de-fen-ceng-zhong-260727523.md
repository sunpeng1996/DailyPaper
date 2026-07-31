---
title: Hierarchical Reranking for Scalable Financial RAG System
title_zh: 面向可扩展金融RAG系统的分层重排序框架
authors:
- Joohyun Lee
- Sungwoo Hong
affiliations:
- Financial Security Institute
- Hanyang University
arxiv_id: '2607.27523'
url: https://arxiv.org/abs/2607.27523
pdf_url: https://arxiv.org/pdf/2607.27523
published: '2026-07-29'
collected: '2026-07-31'
category: RAG
direction: 垂直领域RAG · 分层重排序优化
tags:
- RAG
- Reranking
- Long-Context
- Domain-LLM
- Query-Processing
one_liner: 提出结合预检索优化、分层重排、长上下文管理的金融RAG框架，NDCG@20达0.7918，获ICAIF'24 FinanceRAG挑战赛亚军
practical_value: '- 预检索阶段的领域适配技巧可复用：针对电商/广告领域做术语归一化（如促销口径、SKU别名统一）、结构化信息规则化转换（如商品参数表格转JSON保留键值绑定关系），不引入幻觉即可提升召回准确性

  - 分层重排架构可直接迁移到大规模推荐/搜索场景：用轻量级模型做粗筛（如jina-reranker-v3）过滤90%以上低相关候选，再用高精度大模型做细排，平衡推理成本和效果

  - 长上下文管理策略可落地：实测64k为多数LLM的有效上下文阈值，超过阈值时做语义分片+答案融合，避免长上下文下数值/事实类信息识别准确率下降

  - 领域RAG优化优先级可参考：预检索的规则化优化>分层重排架构>长上下文适配，低复杂度优化可获得更高的边际收益'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有通用RAG在金融领域落地存在三类核心痛点：领域术语/缩写导致的查询-语料嵌入漂移、文本-表格混合结构的语义对齐差、长上下文下推理准确率骤降，同时金融场景对事实准确性、数值精度要求极高，亟需可规模化部署的高可靠性RAG方案。

### 方法关键点
- 预检索优化：对查询做归一化（术语/单位/缩写扩展）、关键词提取、语义改写；对语料做表格规则化转JSON（保留数值与表头绑定关系）、长文档摘要压缩，无幻觉提升语义匹配度
- 分层重排架构：两级级联模型，第一级用jina-reranker-v3轻量模型从全量候选中粗筛Top100，第二级用Qwen3-Reranker-8B大模型做细排输出Top20，兼顾效率与精度
- 长上下文管理：实测设定64k为有效上下文阈值，超过阈值时将Top20语料拆分为两个语义子集分别生成答案，再基于置信度做融合输出，避免长上下文性能衰减

### 关键实验
在FinQA、FinanceBench、ConvFinQA等5个金融RAG基准数据集上测试，预检索优化组合比基线NDCG@20提升5.9%，分层重排比单重排器基线NDCG@20提升6.5%，最优配置NDCG@20达0.7918；搭配长上下文管理后，Claude-4.6 Opus的生成准确率达81.52%，该方案获ACM-ICAIF'24 FinanceRAG挑战赛亚军。

### 核心结论
垂直领域RAG落地的核心是谨慎的规则化工程优化，而非单纯的模型规模堆叠，小大模型协作的分层架构是平衡成本与效果的最优路径之一
