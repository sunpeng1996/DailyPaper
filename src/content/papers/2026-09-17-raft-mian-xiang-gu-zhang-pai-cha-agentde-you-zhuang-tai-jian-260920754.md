---
title: 'RAFT: A Stateful Retrieval-Augmented Framework for Troubleshooting Agents'
title_zh: RAFT：面向故障排查Agent的有状态检索增强框架
authors:
- Mingxuan Zhang
- Xiaowen Wang
- Anupma Sharan
- Zhengyi Chen
- Chenyu Diana Zhang
- Shanshan Yang
- Chittibabu Pacharu
affiliations:
- Microsoft
arxiv_id: '2609.20754'
url: https://arxiv.org/abs/2609.20754
pdf_url: https://arxiv.org/pdf/2609.20754
published: '2026-09-17'
collected: '2026-09-18'
category: Agent
direction: Agent检索增强 · 多阶段状态感知
tags:
- RAG
- Stateful Retrieval
- Troubleshooting Agent
- GraphRAG
- Customer Support
one_liner: 将历史故障工单按状态结构化索引，实现多阶段状态感知的RAG检索，效果显著优于通用RAG/GraphRAG
practical_value: '- 可将多轮会话类数据（如电商客服工单、用户交互历史、搜索会话）按状态转成时间链条目索引，匹配时直接返回对应状态锚点的完整历史轨迹，大幅降低上下文噪声

  - 检索层独立于Agent端到端逻辑单独评测的方案可复用，不需要线上部署就能快速验证检索策略效果，适合内部算法迭代

  - 可选的同根因/同解决方案的case级图扩展机制，可直接迁移到推荐系统的相似item召回、相似用户行为路径拓展、售后问题解决方案匹配场景

  - 工单/会话类场景可先做离线可行动性过滤，筛掉无有效解决方案的无效数据，大幅降低检索噪声和推理token消耗'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有RAG将历史客服工单视为静态文档，忽略故障排查的多阶段状态演进特性，检索到的上下文噪声大、碎片化，难以支撑Agent基于当前工单阶段给出精准的同场景解决方案；通用GraphRAG依赖实体抽取建图，成本高且适配性差，同时多阶段故障排查公开数据集稀缺，算法迭代困难。

### 方法关键点
- 离线索引层将每个历史工单抽象为有向时间链条目，每个条目对应一个工单状态（症状/假设/根因/解决），仅保留有效信息，同时输出可行动性标签过滤无效工单
- 可选case级图，基于根因+解决方案的混合相似度（语义+BM25经RRF融合）关联相似工单，用于初始检索后的结果拓展
- 在线检索基于时间链条目做混合相似度匹配，贪心将匹配条目升级为所属完整工单，返回匹配锚点+完整工单轨迹，Agent可按需触发图拓展

### 关键实验结果
在826条微软Windows Server合成工单数据集、Apache Jira真实工单数据集上，对比Vanilla RAG、HippoRAG2、Fast-GraphRAG基线，RAFT在工单0%/30%/60%进度的Case Hit分别达84.2%/87.1%/88.8%，较最强基线Vanilla RAG分别提升16.9/15.2/11.9个百分点，根因覆盖率、解决方案覆盖率也全面领先。

### 核心结论
多轮交互类场景的RAG不需要盲目上复杂GraphRAG，将交互按状态结构化做细粒度检索，往往能以更低成本获得更好的效果。
