---
title: 'Real Long-Term Memory for AI: A 50-Million-Token Window That Is Faster and
  Cheaper Than Recompute'
title_zh: 面向AI的真实长时记忆：比重计算更快更省的5000万Token窗口
authors:
- Sietse Schelpe
affiliations:
- Corbenic AI
arxiv_id: '2610.10845'
url: https://arxiv.org/abs/2610.10845
pdf_url: https://arxiv.org/pdf/2610.10845
published: '2026-10-06'
collected: '2026-10-09'
category: LLM
direction: LLM推理优化 · 持久化KV存储
tags:
- KV cache
- Long Context
- Inference Optimization
- LLM Serving
- Memory System
one_liner: 开源galahad-kv实现5000万Token级持久化KV存储，零重计算恢复，性能能耗远优于重计算
practical_value: '- 电商智能客服、长会话推荐场景可提前将用户全量历史行为、店铺全商品库的KV预计算加密存储到本地NVMe，每次请求无需重复prefill，可降低2.8~4.3倍的推理延迟，减少能耗成本

  - RAG场景下固定知识库（如商品介绍、售后规则）的KV可一次性预存，无需每次检索到文本都重新计算KV，相比普通RAG大幅降低prefill开销，提升用户查询响应速度

  - 做LLM效果评测时可复用论文的反作弊协议：用随机nonce替换真实敏感数据、插入诱饵样本、盲测注入，避免数据污染导致的评测结果失真，得到更准确的业务效果指标'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Transformer原生上下文窗口限制了长历史信息的访问，且每次请求重算KV cache的prefill成本高，现有KV offloading方案多为临时缓存、无法跨请求复用超窗口历史KV，大模型长会话、大规模知识库场景的推理成本居高不下。
### 方法关键点
- 开源galahad-kv持久化记忆层，适配vLLM框架，将每16k Token块的KV状态经AES-256加密后写入本地NVMe存储，VRAM仅保留当前块KV，内存占用恒定
- 恢复时直接从磁盘读取对应块KV graft到模型中，无需重计算Token，支持字节级精确恢复，恢复延迟与KV块深度无关
- 设计5种反作弊评测机制：随机nonce替换真实信息、盲注入、高熵针样本+诱饵样本、磁盘存储审计，避免评测作弊
### 关键结果
单NVIDIA H100 GPU上测试Gemma 4 12B/31B模型，5000万Token混合公开语料（含对话、代码、论文、教育文本），对比16k块全prefill重计算baseline：
- 100个不同深度探针全部实现零重计算恢复，31B模型文本召回率98/100，12B为82/100，零幻觉
- 恢复速度比重计算快2.8~4.3倍，GPU能耗低8.8~12.3倍，恢复延迟与Token深度无关，全流程VRAM恒定
### 核心结论
越大的模型从KV复用中获得的性能与成本收益越高，持久化KV存储可同时优化大模型的记忆能力与推理成本。
