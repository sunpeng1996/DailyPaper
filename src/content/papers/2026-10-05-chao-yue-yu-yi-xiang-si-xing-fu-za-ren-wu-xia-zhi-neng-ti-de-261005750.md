---
title: 'Beyond Semantic Similarity: Performance and Costs of Agentic Retrieval for
  Complex Tasks'
title_zh: 超越语义相似性：复杂任务下智能体检索的性能与成本
authors:
- Reza Esfandiarpoor
- Radek Osmulski
- Yauhen Babakhin
- Gabriel de Souza P. Moreira
- Oliver Holworthy
- Jie He
- Ronay Ak
- Jiarui Cai
- Ryan Chesler
- Bo Liu
affiliations:
- NVIDIA
- University of Edinburgh
arxiv_id: '2610.05750'
url: https://arxiv.org/abs/2610.05750
pdf_url: https://arxiv.org/pdf/2610.05750
published: '2026-10-05'
collected: '2026-10-06'
category: Agent
direction: Agent 智能检索性能与成本评估
tags:
- Agentic Retrieval
- ReAct
- Dense Retrieval
- LLM
- RAG
- Cost Benchmark
one_liner: 基于ReAct的智能体检索较同配置标准稠密检索nDCG@10提升8.7点，量化其部署成本与泛化性
practical_value: '- 电商多跳语义搜索、客服RAG问答等高价值复杂检索场景，可直接复用该ReAct检索Agent架构，搭配现有embedding模型即可提升检索效果，无需重新训练embedding

  - 部署时可抛弃MCP协议，改用进程内线程安全单例retriever，消除网络往返开销，提升GPU利用率与并发吞吐量

  - 故障兜底可借鉴RRF融合策略：Agent执行异常（上下文溢出、合规拦截）时，融合已生成的多次检索排序结果作为输出，保证服务可用性

  - 当前Agent检索 latency 与token消耗是标准检索的上百倍，仅适合低并发高价值场景，暂不适合公域搜索等大规模高吞吐场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统稠密检索仅依赖query与文档的语义相似度匹配，无法满足RAG、深度研究类Agent等场景下的模糊意图、多跳推理类复杂检索需求，且当前缺乏对智能体检索方案的效果、泛化性、落地成本的系统性量化评估。
### 方法关键点
- 基于ReAct loop搭建检索Agent，开放三类工具：Retrieve调用稠密检索取top-k结果、Think支持推理规划查询策略、Final_Results输出最终排序结果，支持根据已检索内容动态迭代改写查询、分解复杂query，无需固定静态pipeline
- 输入侧引入原始query的初始检索结果作为上下文，帮助Agent快速理解语料特征，调整搜索策略，减少无效检索
- 异常降级机制：Agent触发上下文溢出、内容合规错误时，用RRF融合已完成的多次检索排序结果兜底输出
- 工程优化：替换MCP协议为进程内线程安全单例retriever，减少服务启动与网络往返开销，提升GPU利用率
### 关键实验结果
- 数据集：跨域企业文档基准ViDoRe v3、推理密集型检索基准BRIGHT
- 对比基线：同embedding的标准稠密检索、领域专用方案INF-X-Retriever
- 效果指标：同embedding配置下，Agent检索较标准检索nDCG@10平均提升8.7个点；同一无修改的Agent pipeline在ViDoRe v3排行榜排第1、BRIGHT排第2，泛化性远优于专用方案（专用方案跨域效果甚至低于标准检索基线）；可将不同能力embedding模型的效果差距缩小57%
- 成本指标：平均latency 107.4s为标准检索的160倍，单query消耗764.1k输入token、5.8k输出token
### 核心结论
智能体检索是复杂检索场景的核心突破方向，但当前推理成本远高于传统方案，仅适合高价值低并发场景落地，大规模部署需优先解决效率优化问题
