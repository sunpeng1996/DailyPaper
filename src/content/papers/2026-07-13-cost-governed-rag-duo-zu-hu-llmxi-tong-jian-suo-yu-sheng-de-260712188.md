---
title: 'Cost-Governed RAG: Unified Per-Tenant Cost Attribution Across Retrieval and
  Generation in Multi-Tenant LLM Systems'
title_zh: Cost-Governed RAG：多租户LLM系统检索与生成的统一逐租户成本归因
authors:
- Navnit Shukla
arxiv_id: '2607.12188'
url: https://arxiv.org/abs/2607.12188
pdf_url: https://arxiv.org/pdf/2607.12188
published: '2026-07-13'
collected: '2026-07-15'
category: RAG
direction: RAG 多租户全链路成本管控优化
tags:
- RAG
- Multi-Tenant
- Cost Governance
- Vector Index
- LLM Observability
one_liner: 提出融合无码本向量索引与管控网关的RAG架构，实现多租户场景全链路成本精准归因
practical_value: '- 多租户RAG服务（如电商商家智能助手、品牌定制推荐Agent）可复用无码本向量索引的确定性成本公式，实现检索侧成本逐租户计量，避免跨租户成本均摊

  - 部署ToB类LLM/RAG服务时，可直接套用「Embedding+检索+生成」三层统一归因架构，支撑租户级成本核算、差异化定价与成本优化

  - 向量索引选型优先考虑无码本量化方案，在降低检索基础设施成本的同时，消除共享码本带来的租户隐私数据泄露风险'
score: 8
source: arxiv-cs.IR
depth: abstract
---

### 动机
企业级多租户RAG部署存在成本治理盲区：LLM生成成本可按Token计量，但检索层（向量存储、相似度计算、Embedding API调用）属于未归因的共享成本，存在租户间隐性交叉补贴问题。
### 方法关键点
1. 融合无码本向量索引TurboVec与多租户LLM管控网关，构建全链路可观测栈，实现逐租户的Embedding、检索、生成成本统一归因
2. 依托TurboVec的确定性闭式内存计算公式，实现近似精确的逐租户检索成本核算，解决图索引非线性内存开销无法精准计量的问题
3. 采用无码本量化，消除训练量化器共享码本带来的租户数据泄露风险
### 关键结果
100个模拟租户（10M向量，对数正态大小分布）场景下，端到端成本归因精度达99.96%，遥测开销低于查询延迟的0.04%，检索基础设施成本较托管向量数据库服务降低3.1-9.0x
