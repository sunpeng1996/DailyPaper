---
title: Robust Interpretation of Historical Documents in Knowledge Graphs Through Query
  Inference and Execution
title_zh: 基于查询推理与执行的知识图谱历史文档鲁棒解析框架
authors:
- Sebastià Nicolau
- Adrià Molina
- Oriol Ramos Terrades
- Josep Lladós
affiliations:
- Centre de Visió per Computador
- Universitat Autònoma de Barcelona
arxiv_id: '2607.24475'
url: https://arxiv.org/abs/2607.24475
pdf_url: https://arxiv.org/pdf/2607.24475
published: '2026-07-27'
collected: '2026-07-28'
category: Agent
direction: Agent 知识图谱检索优化
tags:
- GraphRAG
- Agentic RAG
- Word Spotting
- Knowledge Graph
- Query Generation
- OCR Robustness
one_liner: 融合word spotting与Agentic GraphRAG实现含OCR噪声的历史文档知识图谱可靠查询
practical_value: '- 电商搜索拼写纠错、变体召回场景可借鉴word spotting思路：结合PHOC字符级嵌入与语义嵌入召回实体变体，将精确匹配查询替换为多变体正则匹配，提升下沉市场等拼写错误高发场景的召回率

  - 商品/用户行为KG的Agent查询系统可复用「Cypher生成→语法校验→实体动态扩展→执行」流程，对商品名、地名等高变体字段做自动扩展，减少漏召回与空查询问题

  - 生成式搜索/推荐的结果评估可参考NERO-ANLS设计思路：优先考量召回率，对实体做模糊匹配容忍拼写变体，避免过度惩罚回答冗余，更贴合用户实际体验

  - 中小模型部署代码生成类Agent时，增加实体扩展类工具调用可有效弥补模型能力不足，实验中Phi-4加扩展后NERO-ANLS从0.53升至0.631，ROI高于单纯提升模型规模'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
历史档案类知识图谱存在大量OCR/手写识别错误、古今拼写变体，传统RAG无法处理统计聚合、多跳推理类复杂查询，普通GraphRAG依赖精确字符串匹配漏召严重，而档案馆等场景要求检索结果可溯源、低幻觉，亟需兼顾查询灵活性与结果可靠性的解决方案。
### 方法关键点
- 采用Agentic GraphRAG流程：自然语言Query结合KG本体schema与少样本示例生成Cypher查询→多轮语法/拓扑结构校验修正→对标记的模糊匹配字段调用word spotting模块扩展变体→执行查询后LLM生成回答
- 词扩展模块：用PHOC字符级嵌入或MPNet语义embedding召回相似拼写变体，将原查询的精确匹配条件替换为覆盖所有变体的正则表达式，不破坏原有查询逻辑
- 对比两种KG建模方案：属性图结构简单，查询生成门槛低；RDF图将属性单独建模为节点，更适配复杂多跳检索场景
### 关键结果
基于自建的100条人工标注Esposalles DocVQA数据集（46%统计聚合、31%实体关系、11%多跳推理、12%复杂过滤查询），对比普通RAG、无扩展GraphRAG：
1. 普通RAG的NERO-ANLS最高仅0.469，GraphRAG+PHOC扩展在纯净转录下最高达0.876
2. 加word spotting后小模型Phi-4在78.3%准确率的OCR转录下，NERO-ANLS从0.53提升至0.631
3. LLM规模到32B后性能饱和，Qwen3-VL 32B与GPT-5.1表现无显著差异

> 最值得记住的结论：结构化KG检索场景中，对易出错实体做动态变体扩展，比单纯优化RAG召回或增大模型规模，能更有效提升噪声场景下的查询准确率与鲁棒性
