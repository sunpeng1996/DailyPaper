---
title: 'Hybrid Semantic Tool Discovery for Enterprise MCP Gateway: Architecture and
  Implementation'
title_zh: 企业级MCP网关混合语义工具发现系统的架构与实现
authors:
- Olympia Saha
- Amy Wang
- Srinivasan Manoharan
affiliations:
- PayPal, Inc.
arxiv_id: '2608.23992'
url: https://arxiv.org/abs/2608.23992
pdf_url: https://arxiv.org/pdf/2608.23992
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: Agent工具发现 · MCP协议优化
tags:
- MCP
- Tool Discovery
- Hybrid RAG
- Agent Infrastructure
- Context Optimization
one_liner: PayPal提出SCOUT混合RAG系统，将MCP工具token消耗降低99%，支持所有MCP客户端无改造接入
practical_value: '- 电商/广告Agent平台若存在大量内部API/运营工具，可复用meta-tool设计，仅暴露tool_search和execute_tool两个元工具，无需修改Agent客户端即可实现千级工具的按需检索，彻底解决上下文窗口饱和问题

  - 结构化schema（如商品属性、API参数）检索场景下，可复用「BM25稀疏匹配+稠密向量检索+RRF融合+3倍候选集扩容」的方案，同时覆盖精确关键词匹配和语义意图匹配，Hit@5可提升至95%以上

  - 企业级RAG系统可复用分级降级策略：embedding服务不可用时回退到纯BM25检索，索引故障时回退到全量加载模式，完全兼容原有协议，避免业务中断

  - 多角色/多租户的Agent工具/商品推荐场景，可将权限过滤下推到向量数据库检索层，而非后置过滤，既避免权限泄露又减少后处理开销'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
企业级LLM Agent部署中，MCP网关聚合了上百个服务的数千个工具，传统全量加载工具schema的模式会占用70%以上的上下文窗口，既推高推理成本，又会因无关信息干扰降低工具选择准确率，同时用户无法手动遍历千级工具目录，prompt缓存仅能降低重处理成本，无法解决上下文占用和准确率下降的核心问题。

### 方法关键点
- 协议层设计两个标准MCP元工具`tool_search`和`execute_tool`，将工具发现与执行解耦：Agent先调用`tool_search`按需检索top-k相关工具，再调用`execute_tool`路由执行，全程无需客户端改造
- 检索层采用混合RAG架构：BM25稀疏匹配+OpenAI text-embedding-3-large稠密向量检索，两个分支各取3倍top-k候选，通过Reciprocal Rank Fusion无参数融合结果，同时覆盖精确关键词匹配和语义意图匹配
- 工程侧实现零 downtime 索引更新、权限过滤下推到向量数据库、分级降级机制，支持生产/开发环境基于自然语言意图自动路由

### 关键结果
在PayPal生产环境2000+工具的场景下测试：45条业务基准query的Hit@1达84.8%，Hit@5达95.6%，MRR为0.821；工具token消耗从140.2k（占200k上下文的70.1%）降至1.3k（占0.8%），降幅达99%；p95检索延迟为936ms，24小时生产运行零降级，支持Claude、ChatGPT、GitHub Copilot等6种主流MCP客户端无改造接入。

### 核心结论
将工具发现本身封装为标准协议的元工具，是大规模Agent工具生态实现可扩展、低改造成本落地的核心设计思路。
