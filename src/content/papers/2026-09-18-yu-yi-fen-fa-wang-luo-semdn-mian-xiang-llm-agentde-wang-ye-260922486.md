---
title: 'Semantics Delivery Network: Rethinking Web Retrieval Infrastructure for LLM
  Agents'
title_zh: 语义分发网络（SemDN）：面向LLM Agent的网页检索基础设施重构
authors:
- Peichun Hua
- Yunming Xiao
affiliations:
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2609.22486'
url: https://arxiv.org/abs/2609.22486
pdf_url: https://arxiv.org/pdf/2609.22486
published: '2026-09-18'
collected: '2026-09-22'
category: Agent
direction: Agent 检索架构 · 语义分发缓存
tags:
- Semantic Caching
- RAG
- Agentic Search
- CDN
- Vector Retrieval
one_liner: 提出面向LLM Agent的chunk粒度语义分发网络，替代传统URL粒度网页检索架构
practical_value: '- 电商客服RAG、商品检索Agent场景可复用chunk粒度缓存架构，相比整页缓存减少6.9-15.5倍带宽消耗，降低LLM上下文推理成本

  - 多租户RAG服务可复用「共享归一化内容块+租户定制排序」架构，既降低重复爬取/切分/embedding成本，又保留业务策略灵活性

  - 多轮Agent检索场景可利用任务级语义locality优化缓存策略，同任务内32%-55%的chunk可复用，大幅降低检索延迟

  - RAG检索置信度评估可参考语义覆盖缺失判断逻辑，通过检索分数分布、跨层一致性信号触发补召，提升回答准确率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM Agent、多轮Agentic RAG依赖的网页检索基础设施仍面向人类用户设计，存在四大结构性错配：排序目标为通用相似度而非任务效用；传输整页的粒度比LLM需要的短chunk大2-3个数量级；URL缓存无法利用语义locality；多租户重复爬取/清洗/切分/embedding的冗余成本极高，还易触发反爬限制。

### 方法关键点
- 分层边缘架构：边缘节点直接以chunk为粒度做索引、检索、智能缓存，Agent提交查询直接返回所需chunk，无需下载整页
- 语义覆盖缺失判断：不同于URL缓存的明确miss，通过检索分数分布、跨层一致性、新鲜度元数据判断是否需要触发外部内容发现与刷新
- 共享+定制解耦设计：统一爬取、清洗的归一化内容块跨租户共享，租户可自定义切分策略、embedding模型、重排器，私有策略和数据不泄露
- 语义感知缓存置换：根据chunk的语义复用率做缓存置换，而非传统URL热度，边缘存热chunk、区域层存冷分片、全局层维护目录

### 关键实验
基于Natural Questions、wiki-18、CRAG等RAG基准，对比传统SERP+整页下载的基线方案：
1. 带宽消耗：中位数下Agent仅需7.1KB的chunk，传统轻量HTML下载需761KB（107倍），全页面渲染需18.1MB（2532倍）
2. 缓存效率：1.34MB的chunk级LRU缓存可达73.8%命中率，同命中率下URL缓存需近100MB，chunk缓存回源字节数比URL缓存少13-41倍
3. 回答质量：同token预算下，chunk检索的平均F1比整页检索高6.9%，CRAG任务下reranked chunk的准确率达0.6，显著优于整页和SERP snippet

### 核心洞见
LLM Agent的检索核心是语义chunk的分发，而非传统网页的URL分发，将语义检索作为一级网络抽象可带来数量级的成本下降和质量提升
