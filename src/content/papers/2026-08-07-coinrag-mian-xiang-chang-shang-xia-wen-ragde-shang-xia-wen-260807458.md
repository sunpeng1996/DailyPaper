---
title: 'CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context
  RAG'
title_zh: CoinRAG：面向长上下文RAG的上下文信息单元KV缓存复用框架
authors:
- Gyuwan Kim
- Cheoneum Park
- Tao Yang
affiliations:
- University of California, Santa Barbara
- Hanbat National University
arxiv_id: '2608.07458'
url: https://arxiv.org/abs/2608.07458
pdf_url: https://arxiv.org/pdf/2608.07458
published: '2026-08-07'
collected: '2026-08-10'
category: RAG
direction: 长上下文RAG · KV缓存效率优化
tags:
- RAG
- KV Cache
- Long Context
- Retrieval Efficiency
- Question Answering
one_liner: 提出细粒度信息单元级KV缓存复用的长上下文RAG框架，100ms P99时延约束下F1相对提升5.3%
practical_value: '- 电商客服/商品问答类RAG系统可复用离线细粒度信息单元（如商品属性、售后规则片段）KV缓存的思路，在100ms P99交互时延约束下提升回答准确率，同时降低GPU显存占用

  - 可直接复用两阶段检索+KV切片+RoPE位置对齐的工程架构：先召回top-k候选粗chunk，再在chunk内召回query相关细粒度片段，通过预计算KV切片拼接大幅降低prefill时延

  - 针对RAG系统训练-推理结构差问题，可参考nugget-aware fine-tuning思路：用线上实际拼接的非连续片段构造训练数据，对齐推理逻辑消除分布差

  - 短平快业务可先跳过微调步骤，直接用现有LLM做离线信息单元提取，仅靠检索+KV拼接就能拿到大部分性能收益'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

#### 动机
现有基于粗粒度chunk的KV缓存复用RAG方案存在大量冗余信息和噪声，在互联网服务标准的100ms P99交互时延约束下，不得不限制检索范围导致回答准确率下降；同时长上下文prefill时延高、GPU显存占用大，难以支撑高并发用户请求。

#### 方法关键点
- 离线预处理：对每个512-token chunk用LLM提取细粒度信息单元（nugget），对齐到原文本token span，预计算全chunk KV缓存持久化存储
- 在线两阶段检索：先召回top-kc相关粗chunk，再在候选chunk内检索query相关的top-kn个信息单元
- 上下文拼接：从预计算KV中切出对应nugget的KV片段，通过RoPE位置偏移对齐后拼接为上下文前缀，无需在线编码
- 可选微调：用非连续nugget拼接的样本做nugget-aware微调，消除训练-推理的结构分布差

#### 关键结果
在LongBench的3个多跳QA数据集（HotpotQA、2WikiMQA、MuSiQue）上对比5种基线方案：
- P99 100ms时延约束下，比最优基线TurboRAG平均F1相对提升5.3%，上下文长度缩短1.84倍
- 无时延约束时，平均F1相对提升5.2%，上下文长度缩短6.8倍

#### 核心结论
在低交互时延SLA约束下，细粒度关键信息KV缓存复用带来的噪声减少收益，远大于丢失跨chunk注意力的损失。
