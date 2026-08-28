---
title: Conversational Recommendation over Live E-Commerce Catalogues with Self-Refreshing
  Retrieval
title_zh: 面向动态更新电商目录的自刷新检索会话推荐系统
authors:
- Ante Kapetanovic
- Tomislav Duricic
- Dionizije Fa
- Andro Mercep
- Emanuel Lacic
affiliations:
- Infobip
arxiv_id: '2608.27006'
url: https://arxiv.org/abs/2608.27006
pdf_url: https://arxiv.org/pdf/2608.27006
published: '2026-08-27'
collected: '2026-08-28'
category: GenRec
direction: 生成式会话推荐 · 增量向量索引
tags:
- Conversational Recommendation
- Incremental Indexing
- RAG
- LLM4Rec
- E-commerce
one_liner: 提出基于双哈希增量更新的自刷新检索器，实现动态电商目录下低开销多轮会话推荐
practical_value: '- 可复用双哈希（全量哈希+语义哈希）增量索引方案：仅对语义变更的商品重嵌入，价格/库存等非语义元数据变更仅更新索引字段，大幅降低向量索引同步开销，适配电商千万级商品库的日常更新场景

  - 会话推荐可采用LLM仅做意图分类+偏好引导、检索/重排/多样性选择走独立模块的架构，既利用LLM的自然语言交互能力，又严格控制推理成本，适配大流量线上场景

  - 向量存储层统一抽象为VectorStore接口，可平滑切换不同向量数据库、嵌入模型、重排模型，大幅降低业务迭代的代码改造成本

  - 目录同步前先做快照合法性校验，拒绝空/不完整快照，避免误删全量索引，可直接复用作为生产级向量索引同步的稳定性保障手段'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM驱动的会话推荐系统大多基于静态商品索引评估，但生产环境电商目录是动态更新的，全量重索引开销极高，索引漂移会导致推荐下架/缺货商品，严重影响用户体验，是会话推荐落地的核心工程障碍。
### 方法关键点
- 自刷新检索器：每次同步时拉取最新商品快照，基于稳定商品ID匹配存量索引，用全量哈希检测任意字段变更，用语义哈希（仅覆盖名称/描述/品牌/类目字段）检测是否需要重嵌入，仅处理增量变更
- 变更分类处理：新增/语义变更商品走规则优先+LLM兜底的属性enrichment后重嵌入upsert；价格/库存等元数据变更仅更新索引字段不重嵌入；删除商品移除索引，无变更商品直接跳过
- 会话pipeline采用控制器架构：LLM仅负责用户意图分类与模糊偏好引导，商品检索/重排/多样性选择走独立非生成模块，成本可控且效果稳定；存储层将向量库/用户画像/会话状态完全解耦，索引同步与会话服务互不干扰
### 关键实验
基于500条商品的匿名电商目录测试，全量重建索引耗时2.914s；无变更时同步仅耗时0.053s（为全量的1.8%）；价格/库存变更同步耗时0.072s（为全量的2.5%）；新增/语义变更单商品同步耗时约0.32~0.36s（仅为全量的11%~12%）；删除商品同步耗时0.062s（为全量的2.1%）
### 核心结论
会话推荐落地的核心工程瓶颈不是LLM效果，而是商品索引的实时一致性，增量同步的核心是区分语义变更与非语义变更，最大化降低重嵌入开销
