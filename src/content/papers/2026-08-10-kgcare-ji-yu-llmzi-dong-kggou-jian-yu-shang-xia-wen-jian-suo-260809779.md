---
title: 'KGCaRe: Explainable Complex Conditional Question Answering using Automatic
  Knowledge Graph Construction and Context Retrieval with LLMs'
title_zh: KGCaRe：基于LLM自动KG构建与上下文检索的可解释复杂条件问答
authors:
- Ghanshyam Verma
- Simanta Sarkar
- Devishree Pillai
- Hotaka Shiokawa
- Yourong Xu
- Fiona Veazey
- Peter Hubbert
- Hui Su
- Paul Buitelaar
affiliations:
- University of Galway
- Fidelity Investments
- Insight Research Ireland Centre for Data Analytics
arxiv_id: '2608.09779'
url: https://arxiv.org/abs/2608.09779
pdf_url: https://arxiv.org/pdf/2608.09779
published: '2026-08-10'
collected: '2026-08-11'
category: RAG
direction: RAG · 知识图谱增强复杂条件问答
tags:
- RAG
- Knowledge Graph
- Complex QA
- LLM Reasoning
- Multi-prompt
one_liner: 提出融合结构化KG推理与向量检索的混合RAG框架，在多类复杂QA任务上超越现有基线
practical_value: '- 多prompt KG抽取trick可迁移到电商领域知识库构建，把商品规则、活动政策、售后条款拆成结构化三元组，提升合规问答、活动咨询类智能客服的准确率

  - LLM引导的迭代KG遍历+线索实体扩展逻辑，可用于优化电商多轮推荐Agent，比如面向用户多约束的商品咨询场景，沿着用户画像→禁忌条件→适配商品的路径迭代检索，减少漏召回

  - KG+向量检索的混合上下文融合方案，可直接复用在生成式推荐RAG pipeline，同时保留结构化规则约束（限购、满减条件）和非结构化的商品评价、卖点信息，提升推荐解释性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有通用LLM与Vanilla RAG在领域复杂条件QA任务上性能退化，纯向量检索无法捕获逻辑约束与隐含条件易漏召回，纯KG检索依赖图完整性、稀疏场景下效果差，且答案缺乏可解释性、hallucination风险高。

### 方法关键点
- 多阶段prompt KG抽取：分4轮用LLM从文档抽取三元组，依次覆盖基础实体关系、if-then条件/例外逻辑、隐含关系推理补全、标准化存入Neo4j，大幅提升KG对规则类信息的覆盖度
- LLM引导迭代KG遍历：以query提取的主题实体为锚点，首步模糊匹配、后续深度精确匹配，每步用LLM剪枝无关三元组，判断上下文不足时自动生成线索实体继续遍历，最高支持3层多跳推理
- 混合上下文融合：KG遍历得到的路径化三元组与FAISS向量检索得到的top10语义片段，经Cohere重排取top2后共同输入LLM生成答案，兼顾结构化精度与语义丰富度

### 关键结果
在ConditionalQA（政策类复杂条件QA）、HotpotQA（多跳QA）两个数据集上，跨Mistral、Mixtral、GPT-3.5、GPT-4o四类模型均超越所有基线：GPT-4o下ConditionalQA平均F1达67.55（较次优基线高3.84个点），HotpotQA平均F1达80.21（较次优基线高6.84个点）；Mistral小模型下ConditionalQA平均F1达57.89，较次优基线提升12.72个点，小模型增益更显著。

### 核心结论
规则约束强、需多跳推理的垂直场景下，混合结构化KG推理与向量检索的RAG方案，对大小模型均能带来稳定性能提升，且天然具备可解释性。
