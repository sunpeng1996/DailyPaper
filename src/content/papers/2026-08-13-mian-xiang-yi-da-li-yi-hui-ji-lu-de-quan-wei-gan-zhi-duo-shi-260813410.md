---
title: 'Who Speaks Matters: Authority-Aware Multi-View RAG over Italian Parliamentary
  Proceedings'
title_zh: 面向意大利议会记录的权威感知多视角RAG系统
authors:
- Mirko Tritella
- Riccardo Pozzi
- Matteo Palmonari
affiliations:
- University of Milano-Bicocca
arxiv_id: '2608.13410'
url: https://arxiv.org/abs/2608.13410
pdf_url: https://arxiv.org/pdf/2608.13410
published: '2026-08-13'
collected: '2026-08-14'
category: RAG
direction: RAG · 多视角权威感知生成
tags:
- RAG
- Knowledge Graph
- Multi-View Generation
- Citation Faithfulness
- Expert Finding
one_liner: 融合知识图谱与查询相关权威打分的多视角RAG，保障议会内容生成的平衡性与引用保真
practical_value: '- 做分群体公平性生成（如电商不同品牌视角聚合、多用户群体观点汇总）时，可借鉴「分层打分+按群体选权威代表」的架构，从rerank阶段保障群体覆盖，效果比纯prompt控制更稳定

  - 对引用溯源要求高的场景（如客服话术合规校验、政策类内容生成），可采用「LLM生成引用占位符+原文offset替换」的设计，从架构层面完全避免引用幻觉

  - RAG结合知识图谱时可采用向量+结构化双检索通道，把语义匹配和实体关系的权威信号结合，解决纯语义匹配导致的高相关低权威内容排序靠前问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
议会记录体量庞大、立场分散，普通RAG应用在这类多视角公共文本场景存在三类核心缺陷：高频发言者内容占比过高、无法按主题区分发言人权威度、敏感内容引用错配，普通用户、记者、研究者很难快速获取平衡、可信的立场汇总。

### 方法关键点
- 构建统一议会知识图谱存储所有会议记录、发言人属性、议会关系数据，支持向量检索、关键词检索、图遍历三类查询，演讲拆分为15w+ chunk作为最小检索单元
- 双检索通道：稠密通道做chunk语义匹配，图通道从相关法案签署人反向关联发言内容，额外优先召回主题相关委员会成员的发言
- 融合权威打分的rerank：打分综合相关性、多样性、群体覆盖、发言人查询相关权威度（结合职业、教育、委员会身份、法案参与、发言历史、时间衰减等可解释维度），每个议会群体选最高权威发言人作为代表
- 四阶段生成流水线：先拆分query诉求，再按群体生成内容，再整合叙事，最后用原文offset填充引用占位符，从架构层面保障引用完全保真

### 关键实验
在15个政策主题query上对比Google NotebookLM，自动评估显示ParliamentRAG引用保真度1.00（vs 0.95）、议会群体覆盖率0.97（vs 0.95）；6位领域专家盲测显示，系统在源覆盖、源权威度、平衡感知维度显著优于基线，整体满意度与基线持平（4.24 vs 4.27）。

### 核心结论
流利度缺陷可以通过升级LLM或后置改写缓解，但引用保真、群体覆盖这类强约束只能通过架构设计保障，无法靠纯prompt控制可靠实现
