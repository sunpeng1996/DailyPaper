---
title: 'Working Around the Compute Ceiling: Byte-Exact Memory in Galahad Makes LLM
  Reading a One-Time Cost LLM Reading a One-Time Cost'
title_zh: 突破计算天花板：Galahad字节精确内存让LLM读文本仅需一次成本
authors:
- Sietse Schelpe
affiliations:
- Corbenic AI
arxiv_id: '2609.39358'
url: https://arxiv.org/abs/2609.39358
pdf_url: https://arxiv.org/pdf/2609.39358
published: '2026-09-29'
collected: '2026-10-01'
category: LLM
direction: LLM推理 · 持久化KV缓存优化
tags:
- KV cache
- LLM Serving
- Persistent Memory
- Inference Optimization
- RAG
one_liner: 兼容三大主流LLM运行时的字节精确持久化内存层，大幅降低重复长文本推理成本
practical_value: '- 电商客服、商品详情问答场景可复用字节精确KV缓存方案，重复的商品手册、平台规则文档仅需一次prefill，后续请求推理延迟最高降14倍、能耗降92%，成本优势显著。

  - 长上下文Agent任务可对接该持久化KV缓存，避免每轮对话重复加载代码库、知识库的KV状态，大幅提升多轮迭代效率。

  -  RAG系统可参考其fail-closed设计，缓存加载失败时自动回退到正常prefill，完全不影响输出正确性，上线风险极低。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM serving是无状态的，重复请求相同文档时会反复计算KV状态，7个真实数据集统计显示98.7%的prompt token是模型已经读过的内容，长上下文prefill占据了大部分推理时延与能耗，现有运行时的前缀缓存仅保存在GPU内存，易被驱逐、进程重启即丢失，重复计算浪费严重。

### 方法关键点
- 分为两大模块：Taliesin持久化KV内存，按文本字节、模型、租户的指纹存储精确KV状态，加载失败自动回退重算，保证输出bit一致；Blaise文本内存，CPU侧精准定位问题关联的文档段落，仅将必要文本传给模型，减少无效读取。
- 以共享库形式兼容vLLM、SGLang、llama.cpp三大主流运行时，无需修改模型权重与运行时代码，支持跨GPU类型、跨进程重启的状态复用。

### 关键实验
在9.7万token的长语料召回测试（Gemma 4 31B）中，无Galahad的基线仅能答对10/100题，单靠Taliesin答对98/100题，时延从9.3s降到3.0s，能耗降79%；叠加Blaise后答对100/100题，时延降到0.59-0.64s，能耗降92%，显著优于调优后RAGFlow的77/100准确率。7个真实数据集测试中98.7%的prompt token可从缓存加载，兼容30/30款主流LLM，H100下吞吐量提升29.6%，一次性prefill的成本仅需13次请求即可回本。

### 核心结论
LLM推理的成本单位应该是新文本，而非总文本，从无状态推理转向有状态持久化推理是降本提效的核心方向。
