---
title: 'VikingRAG: Accurate and Token-efficient Retrieval-augmented Generation over
  Structured Documents'
title_zh: VikingRAG：面向结构化文档的高精度低Token开销检索增强生成系统
authors:
- Peiyuan Gao
- Gaoyuan Zhang
- Haojie Qin
- Yahui Sun
- Qianyi Zhang
- Yunhao Zhang
- Zeyu Wang
- Wei Lu
affiliations:
- 中国人民大学
- 复旦大学
- 独立研究者
arxiv_id: '2609.11390'
url: https://arxiv.org/abs/2609.11390
pdf_url: https://arxiv.org/pdf/2609.11390
published: '2026-09-10'
collected: '2026-09-11'
category: RAG
direction: 检索增强生成 · 结构化文档优化
tags:
- RAG
- Structured Document
- Token Efficiency
- Agentic Retrieval
- Experience Reuse
one_liner: 提出目录感知的层级语义RAG系统，结合检索轨迹复用与自适应升阶，降Token开销同时保精度
practical_value: '- 电商规则、商品手册、商家合规文档等结构化知识库的RAG落地，可复用其URI路径绑定层级结构+按需暴露目录片段的设计，避免全量目录塞入Prompt的Token浪费

  - 多轮Agent检索场景可借鉴历史检索轨迹固化为经验边的思路，相似Query直接复用历史路径，减少重复探索的Token与耗时，尤其适合高频Query集中的电商客服、商品咨询场景

  - 可借鉴自适应升阶策略，先做低成本单轮检索+证据充足性校验，仅必要时触发多轮Agent检索，平衡成本与效果，适合大流量RAG落地场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有结构化文档RAG方案要么忽略结构特征导致召回精度不足，要么将全量目录序列化到Prompt、依赖多轮无差别交互，带来极高Token开销，无法同时满足高精度与低成本要求，制约企业知识库、电商合规查询等场景的规模化落地。

### 方法关键点
- 层级语义存储模型：将文档目录、文本Chunk、多粒度节点摘要映射为带URI的可寻址对象，URI路径天然保留层级包含关系，同时构建覆盖Chunk与各级摘要的向量索引，打通语义检索与结构导航路径
- 证据缺口驱动的多轮检索：Agent仅通过Search/List/Grep/Read四个工具按需访问目标目录片段，无需加载全量文档结构，大幅降低结构上下文Token开销
- 经验边优化：将历史多轮检索轨迹固化为带Query语义标签的经验边，相似Query可直接通过边扩展获取跨章节/跨文档的分散证据，缩短检索路径
- 自适应升阶策略：先执行单轮经验增强检索，经证据充足性校验通过则直接生成回答，校验不通过才触发多轮Agent检索，避免不必要的交互开销

### 关键实验
在VersionQA、SyllabusQA、FinanceBench等6个跨领域结构化文档数据集上，对比DeepRead、MoDora等SOTA结构感知RAG方案：基础版VikingRAG精度持平SOTA，仅消耗其11.6%~51.9%的Token；叠加经验边与自适应升阶的VikingRAG-E+，Token开销进一步降至5.1%~32.5%，同时推理延迟低于主流SOTA方案。

### 核心结论
结构化RAG的Token开销优化核心是把文档结构从Prompt中剥离为可按需访问的外部状态，同时用历史经验复用降低多轮交互成本。
