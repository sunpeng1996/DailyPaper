---
title: Taking Tokenization off the Host for Agentic LLM Serving
title_zh: 面向智能体LLM服务的GPU全链路分词方案GRAPHTOK
authors:
- Mohammad Siavashi
- Pascal Schwinte
- Ali Banaei
- Gerald Q. Maguire
- Marco Chiesa
- Dejan Kostić
affiliations:
- KTH Royal Institute of Technology
arxiv_id: '2610.13325'
url: https://arxiv.org/abs/2610.13325
pdf_url: https://arxiv.org/pdf/2610.13325
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: LLM服务 · GPU端分词加速
tags:
- LLM Serving
- Tokenization
- CUDA Graph
- Agent Workload
- TTFT Optimization
one_liner: 提出基于CUDA Graph的GPU全链路分词器，兼容主流分词语义，大幅降低Agent场景TTFT提升服务容量
practical_value: '- 长上下文Agent服务（如电商客服、商品长文本理解）若已优化KV prefix cache，tokenization成为TTFT瓶颈时，可采用长短请求分流的GPU+CPU混合分词方案，无需改业务逻辑即可快速落地

  - GRAPHTOK可无缝对接vLLM、NVIDIA Dynamo等主流serving框架，121k token场景下可将单前端支撑的GPU集群规模从2台提升到56台，大幅降低前端服务器成本

  - Token ID缓存与GPU分词是互补关系，优先落地缓存消除可复用前缀的分词开销，剩余跨边界的分词需求用GPU方案加速，两者结合收益最大'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Agent类LLM请求普遍存在长上下文重复的特点，KV prefix cache已将prefill开销压到极低，但CPU侧分词步骤反而成为TTFT的最大瓶颈；中心化CPU分词前端会限制后端GPU集群规模，加CPU核会引发资源竞争、长尾延迟升高，而缓存token ID又受BPE分词的边界依赖限制，无法完全消除分词需求。
### 方法关键点
- 实现GPU端全链路分词，覆盖预分词、BPE合并、token ID生成全流程，完全对齐GPT-2、Llama 3、Qwen 2.5等主流分词器的输出语义，无结果偏差
- 把整个分词流水线封装为可重放CUDA Graph，提前预分配buffer，避免每次请求的内核启动、内存分配、主机同步开销
- 自适应路由：短请求走CPU分词（基于gigatoken），长请求走GPU分词，平衡GPU执行固定开销
- 无缝对接vLLM、NVIDIA Dynamo，无需修改原有框架代码即可集成
### 关键结果
基于H100 NVL测试，对比gigatoken、TokTier等SOTA方案：
- Llama 3场景下长文本分词速度是gigatoken的4.7~6.0倍，单请求性能最高比TokTier快18.1倍
- 接入带prefix cache的vLLM，平均TTFT降低2.1~2.4倍
- 2s P99延迟约束下，121k token Agent请求场景，单Dynamo前端支撑QPS从gigatoken的296提升到518，对应可支撑GPU数量从32台提升到56台，百万token场景P99延迟比gigatoken低64倍

**最值得记住的结论**：Agent场景下当KV cache优化充分后，CPU分词会成为首要瓶颈，GPU全链路分词可在完全兼容现有语义的前提下，同时大幅降低延迟和提升服务容量。
