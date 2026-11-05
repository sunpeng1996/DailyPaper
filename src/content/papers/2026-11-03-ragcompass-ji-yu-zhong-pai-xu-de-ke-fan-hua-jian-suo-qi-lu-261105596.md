---
title: 'RAGCompass: Generalizable Retriever Routing via Reranking'
title_zh: RAGCompass：基于重排序的可泛化检索器路由方法
authors:
- Valentin Six
- Mufei Li
- Dongqi Fu
- Yinglong Xia
- Hong Li
- Pan Li
affiliations:
- University of Virginia
- Georgia Institute of Technology
- Meta
arxiv_id: '2611.05596'
url: https://arxiv.org/abs/2611.05596
pdf_url: https://arxiv.org/pdf/2611.05596
published: '2026-11-03'
collected: '2026-11-05'
category: RAG
direction: RAG优化 · 检索器路由
tags:
- RAG
- Retriever Routing
- Reranking
- Generalization
- Utility Supervision
one_liner: 通过对各检索器返回的证据集做效用监督的重排序，实现可泛化的检索器路由
practical_value: '- 电商客服、商品问答类RAG系统可直接复用该路由逻辑，新增检索器无需重训路由模块即可适配，避免系统迭代的重训成本

  - 路由/排序任务优先用下游业务效用做监督信号，而非中间相关性指标，可避免中间指标和业务目标错配的问题，该经验可复用在召回、排序模块的端到端优化上

  - 多检索器并行调用成本可接受的场景（如离线推理、低吞吐在线场景），该方法比固定单一检索器可带来显著的下游效果提升

  - 尽量避免使用仅基于query特征的路由逻辑，其在跨域、新增检索器场景下泛化性极差，收益甚至低于固定最优检索器'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG系统通常固定单一检索器，但不同检索范式（稀疏、稠密、late interaction等）在不同query下表现差异大，基于query特征的检索器路由方法泛化性极差，新增检索器、换语料、换Reader时完全失效；而如果能为每个query动态选最优检索器，回答F1的上限是最优固定检索器的近3倍，有巨大优化空间。

### 方法关键点
- 将检索器路由转化为对各检索器返回的证据集的重排序任务，直接读取段落内容而非query特征或检索器身份，天然支持未见过的检索器和语料
- 用Reader基于各证据集生成的回答与标准答案的F1作为监督信号，而非检索相关性标签，避免中间指标与下游目标错配
- 架构上先用共享的0.6B Qwen3重排序模型给每个证据集打分，再加2层Transformer比较头做跨检索器联合对比，全链路无检索器专属参数

### 关键实验
在Natural Questions、HotpotQA等4个QA数据集上，路由5种不同范式的检索器，用Llama-3.1-8B做Reader；RAGCompass比最优固定检索器的回答F1相对提升28%，比最强融合基线MoR高3.5pp；跨unseen语料时保留80%以上增益，跨unseen检索器时仅损失0.16~1.17pp，而query-only路由方法全部失效，收益甚至低于最优固定检索器；单query路由开销仅0.22s，占整个RAG pipeline耗时的3.9%。

**最值得记住的一句话**：检索器路由的核心收益来自对检索内容的效用监督，而非对query特征的拟合，泛化能力的本质是不绑定检索器身份、只看内容质量
