---
title: A Three-Layer Caching Architecture for Low-Latency LLM Web Search on Commodity
  CPU Hardware
title_zh: 面向普通CPU硬件的低延迟LLM网页搜索三层缓存架构
authors:
- Ayushman Bhattacharya
- Nihal Gazi
affiliations:
- pollinations.ai
arxiv_id: '2609.05463'
url: https://arxiv.org/abs/2609.05463
pdf_url: https://arxiv.org/pdf/2609.05463
published: '2026-08-11'
collected: '2026-09-11'
category: LLM
direction: LLM工程 · 多层缓存优化
tags:
- LLM Caching
- Semantic Cache
- Redis
- Session Management
- Embedding Reuse
one_liner: 提出普通CPU上运行的LLM网页搜索三层缓存架构，降低落地成本与查询延迟
practical_value: '- 可直接复用三层缓存架构思路：会话层存上下文、语义缓存挡同义重复查询、URL embedding缓存省计算，适配电商RAG导购、Agent客服等场景，无需额外向量数据库，用Redis逻辑分库即可落地

  - 小体量会话历史归档优先选纯Python实现的Huffman编码，压缩率比lz4高5%以上，无原生依赖，特别适合容器化部署场景

  - 语义缓存按会话隔离避免跨用户隐私泄露，相似度阈值设0.9即可覆盖大部分同义改写查询，电商搜索、客服等重复查询多的场景可节省30%以上LLM调用成本

  - Redis缓存不用key前缀区分不同业务域，改用逻辑分库可实现独立监控、选择性刷写，大幅降低中小团队运维成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
商用AI搜索API成本极高，单查询费用达0.03-0.1美元，自研基于浏览器Agent的LLM搜索系统落地时遇到三个核心痛点：多轮会话上下文存储成本高无法水平扩展、用户同义改写查询重复触发全链路计算、热门URL embedding跨会话重复计算浪费算力，现有缓存方案无法同时覆盖三类需求且依赖重型组件，落地成本高。

### 方法关键点
- 三层缓存架构统一部署在单Redis实例，分3个逻辑数据库独立配置TTL和存储格式：
  1. 会话上下文层：Redis存最近20条消息，超出部分用Huffman压缩存磁盘，后台LRU守护进程自动迁移空闲会话，支持会话跨天恢复
  2. 语义查询缓存层：计算query的384维embedding，cosine相似度≥0.9时直接返回缓存结果，按会话隔离避免隐私泄露，TTL5分钟保障内容新鲜
  3. URL embedding缓存层：跨会话全局存embedding的原始float32字节，TTL24小时，避免重复计算
- 用统一协调器封装三层缓存接口，仅暴露4个操作API，接入成本极低

### 关键结果
部署在8vCPU 32GB内存的普通Intel服务器（无GPU）：Redis总内存开销仅1.38MB，读延迟0.1ms，整体keyspace命中率89.3%；Huffman编码对小于5KB的会话历史压缩率达65-69%，仅比zlib差5-6个百分点，无原生依赖；单查询成本仅0.015美元，比主流商用搜索API低50%以上。

可恢复的长会话能力不是LLM本身的特性，而是取决于LLM外围的缓存基础设施设计。
