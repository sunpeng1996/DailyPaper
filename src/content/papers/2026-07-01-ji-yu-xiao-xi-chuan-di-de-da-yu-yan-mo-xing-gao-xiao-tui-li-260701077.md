---
title: Message Passing Enables Efficient Reasoning
title_zh: 基于消息传递的大语言模型高效推理框架
authors:
- Xuecheng Liu
- Daman Arora
- Gokul Swamy
- Andrea Zanette
affiliations:
- Carnegie Mellon University
arxiv_id: '2607.01077'
url: https://arxiv.org/abs/2607.01077
pdf_url: https://arxiv.org/pdf/2607.01077
published: '2026-07-01'
collected: '2026-07-02'
category: Reasoning
direction: LLM分布式推理 · 并行线程通信
tags:
- Message Passing
- LLM Reasoning
- Parallel Inference
- Long Context
- Preemption
one_liner: 提出支持LLM并行线程点对点通信的MPLM框架，大幅降低推理上下文开销与延迟
practical_value: '- 电商大促高并发LLM导购/商品文案生成场景，可基于vLLM等批推理引擎加轻量控制层实现MPLM，复用持久化线程上下文，提升GPU利用率与吞吐

  - 长文案/多文档商品评价检索类Agent任务，可复用spawn/send/recv原语，将长上下文分块给并行线程处理，避免重复加载上下文，最高降本2倍以上

  - 搜索多路召回/粗排结果的LLM打分聚合场景，可借鉴preemption机制，某路候选满足阈值时直接终止其余分支计算，减少算力浪费'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有串行CoT推理延迟高、上下文开销随任务复杂度指数增长，主流fork-join并行方案依赖中心化聚合，线程无状态无法点对点通信，限制了大复杂度推理任务的扩展性，解决该痛点可大幅降低LLM推理成本、支撑更复杂的Agent任务。
### 方法关键点
- 设计spawn/send/recv/stop 4种可被模型生成的指令原语，让LLM自主控制并行线程的创建、点对点消息传递、阻塞等待与终止
- 基于现有批推理引擎（如vLLM）新增轻量控制层实现，无需修改底层KV cache、token采样逻辑，兼容现有推理部署框架
- 原生支持preemption机制，某线程获得足够结果后可直接终止整个子树的冗余计算，还支持线程respawn压缩上下文，突破单线程长度限制
### 关键实验结果
- Sudoku任务：25×25规模下MPLM准确率达72%，远高于GPT-5 Pro的20%，最大上下文开销比fork-join低一个数量级，推理延迟仅为fork-join的1/7
- 3-SAT任务：相比fork-join基线最大提速3.45倍，串行CoT在变量数超过12时直接超出上下文窗口
- LongBench-v2：无需微调，Qwen3.6-35B上与RLM基线准确率相当，平均延迟从223.5s降至102.2s，提速2.2倍
### 核心结论
把分布式计算的MPI思想迁移到LLM推理，通过去中心化的线程间消息传递，能获得比串行、fork-join范式好得多的复杂度扩展性，是未来LLM并行推理的重要方向
