---
title: Configurable Semantic Chunking for Biomedical Information Extraction in Retrieval-Augmented
  Generation
title_zh: 面向生物医学RAG信息抽取的可配置语义分块框架
authors:
- Riya Ahuja
- Tim Kacprowski
- Roya Shiasi Sardoabi
affiliations:
- Institute of Data Science in Biomedicine, Technische Universität Braunschweig, Germany
- Braunschweig Integrated Centre of Systems Biology (BRICS), Technische Universität
  Braunschweig, Germany
arxiv_id: '2608.31139'
url: https://arxiv.org/abs/2608.31139
pdf_url: https://arxiv.org/pdf/2608.31139
published: '2026-08-31'
collected: '2026-09-01'
category: RAG
direction: RAG语义分块优化 · 生物医学信息抽取
tags:
- RAG
- Semantic Chunking
- Information Extraction
- Biomedical NLP
one_liner: 提出可配置语义分块框架替换RAG固定分块，生物医学信息抽取任务最高提升F1 8.4个点
practical_value: '- 垂直领域RAG落地可复用实体保留窗口、触发词居中的分块策略，避免固定分块割裂语义信息，提升召回与信息抽取准确率，可直接迁移到电商商品属性抽取、用户评论观点抽取等场景

  - RAG系统可将分块逻辑外置为配置文件，针对不同任务快速适配分块规则，无需改动后续嵌入、检索、生成模块，大幅降低迭代成本

  - 跨任务RAG选型可参考研究结论：有明确关系线索的抽取任务优先用语义分块，密集信息抽取、二分类场景固定分块性价比更高'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有BioMedRAG依赖固定尺寸分块，易割裂语义证据，拉低信息抽取效果，且分块逻辑僵硬适配性差。

### 方法关键点
可配置语义分块框架融合实体保留窗口、触发词居中切块、命题优先提取、分层触发词优先级、层级关系解析5种策略，仅替换BioMedRAG的分块构建环节，无需改动嵌入、打分器、生成器等其他模块，分块逻辑可通过配置文件外置调整。

### 关键结果
在GM-CIHT关系抽取数据集上F1达82.6%，较固定分块基线提升8.4个点；跨数据集验证显示，有明确关系线索的抽取任务（如GM-CIHT、DDI）语义分块效果更优，密集生化抽取、二分类场景（如ChemProt、ADE）固定分块仍具竞争力。
