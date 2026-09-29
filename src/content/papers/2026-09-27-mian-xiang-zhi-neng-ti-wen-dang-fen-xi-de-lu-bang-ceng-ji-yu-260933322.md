---
title: Robust Hierarchical Structures for Agentic Document Analysis
title_zh: 面向智能体文档分析的鲁棒层级语义树抽取框架SHED
authors:
- Ruiying Ma
- Yiming Lin
- Aditya G. Parameswaran
affiliations:
- UC Berkeley
arxiv_id: '2609.33322'
url: https://arxiv.org/abs/2609.33322
pdf_url: https://arxiv.org/pdf/2609.33322
published: '2026-09-27'
collected: '2026-09-29'
category: Agent
direction: Agent 长文档理解结构优化
tags:
- AgenticQA
- DocumentStructureExtraction
- LongDocumentUnderstanding
- SemanticHierarchy
- RAG
one_liner: 提出鲁棒且紧凑的文档层级语义树抽取框架SHED，大幅降低智能体长文档分析成本并提升准确率
practical_value: '- 电商场景下的长文档（商品详情页、合规合同、品牌手册、用户评价合集）处理可直接复用SHED逻辑，仅基于标题的视觉特征（字号、字体、缩进、编号）聚类生成层级树，无需调用大模型，抽取成本接近0

  - Agent做RAG时可放弃传统固定长度切片，基于SHED生成的层级结构做章节级召回：鲁棒性保证召回内容是真实范围的超集，不会漏关键信息；紧凑性控制token消耗，比碎片化的向量/关键词召回准确率更高

  - 做结构化信息抽取（如商品规格参数、合同条款、财报指标）时，可基于SHED的层级结构做分层遍历，避免跨层级语义歧义，比如不会把子章节的局部运营指标当成全局指标，大幅降低抽取错误率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM与Agent处理长文档时，全量读取会产生高额token成本且容易出现上下文腐烂；基于关键词/向量的召回方案忽略文档天然的章节层级结构，容易召回碎片化的错误内容。过往的层级结构抽取方法没有鲁棒性保证，基于LLM的方案成本高还存在结构幻觉问题，无法支撑Agent长文档分析的落地需求。

### 方法关键点
- 定义两个核心优化目标：鲁棒性要求每个标题下的文本范围是真实对应内容的超集，确保不会遗漏关键信息；紧凑性要求超集尽可能小，控制后续处理的token成本
- SHED采用两阶段可插拔架构：1）语义深度推理：将标题按视觉特征聚类，通过local-first/global-first等算法给每个聚类分配语义深度，约束父节点深度必须小于子节点；2）语义树组装：按文档顺序遍历所有标题，从当前树的右路径中选择符合深度约束的最近节点作为父节点，生成最终层级树
- 定义松格式文档类，覆盖60%以上真实文档，该类文档下SHED的所有推理算法都能100%保证鲁棒性

### 关键结果
在政务、合同、金融财报、学术论文4类数据集上测试：SHT抽取F1比非LLM基线高13%~68%，比昂贵的LLM基线高9%~15%；Agent搭载SHED结构后，问答准确率比基线高3%~23%，总处理成本最高降低10倍。

> 最值得记住的结论：长文档处理不需要追求完全精准的真实层级结构，只要保证召回内容的鲁棒性（不丢正确信息）同时控制紧凑性，就能在极低开销下实现远超现有方案的Agent处理效果。
