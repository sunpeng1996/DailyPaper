---
title: 'DocMaster: A Hierarchical Structure-Aware System for Document Analysis'
title_zh: DocMaster：面向文档分析的层级结构感知系统
authors:
- Ziqi Chen
- Yingli Zhou
- Fangyuan Zhang
- Quanqing Xu
- Chuanhui Yang
- Yixiang Fang
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- The Chinese University of Hong Kong
- OceanBase, AntGroup
arxiv_id: '2607.08539'
url: https://arxiv.org/abs/2607.08539
pdf_url: https://arxiv.org/pdf/2607.08539
published: '2026-07-09'
collected: '2026-07-10'
category: RAG
direction: RAG文档处理 · 层级结构感知索引
tags:
- RAG
- Document Parsing
- Semantic Index
- Hierarchical Structure
- QA System
one_liner: 提出层级结构感知的文档分析系统DocMaster，优化文档筛选与深度问答性能
practical_value: '- 电商商品详情页、商家规则、客服知识库解析可复用层级文档树构建方案，保留段落、表格、属性模块的结构关联，提升RAG问答准确率

  - 多模态商品素材（图文规格、参数表）的索引构建可参考结构感知语义索引方案，避免打平切块丢失结构信息，提升搜索召回匹配精度

  - Agent处理复杂文档类任务（如商品资质审核、活动规则理解）时，可引入层级结构解析模块，降低上下文冗余，提升推理效率'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM文档分析方案普遍将复杂文档（论文、报告、手册等）打平为纯文本切块，丢弃章节、表格、图片、公式等层级结构信息，导致大规模文档集筛选准确率低、下游问答等深度分析任务性能下降，无法满足工业界复杂文档处理需求。

### 方法关键点
1. 设计结构感知的文档解析链路，将原始文档转换为保留完整布局信息的层级文档树；
2. 构建树状多视图语义索引，同时支持自然语言条件下的精准文档筛选，以及过滤后文档子集的深度问答；
3. 封装全流程交互式web界面，覆盖文档上传、索引构建、自然语言检索、后续问答全链路操作。

### 关键结果
全量代码、测试数据集与交互Demo已开源，可直接接入现有RAG系统，层级结构保留设计可有效解决传统切块方案的上下文关联丢失问题，显著提升下游任务表现。
