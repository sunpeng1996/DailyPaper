---
title: 'Bursts That Outlast Themselves: Persistent Degradation in Prefix-Cached Agent
  Serving'
title_zh: 前缀缓存Agent服务的亚稳态失效：突发流量后的持续性性能降级
authors:
- Wen Huang
- Jack Liu
affiliations:
- Microsoft
- Independent Researcher
arxiv_id: '2611.13412'
url: https://arxiv.org/abs/2611.13412
pdf_url: https://arxiv.org/pdf/2611.13412
published: '2026-11-10'
collected: '2026-11-11'
category: Agent
direction: Agent 推理服务 · KV cache 优化
tags:
- KV cache
- prefix caching
- LLM serving
- metastable failure
- agentic system
one_liner: 发现前缀缓存LLM Agent服务的亚稳态失效，提出无调优KV预算控制方案完全避免故障
practical_value: '- 电商导购Agent、LLM推荐rerank等多轮会话服务，不要仅做新请求准入控制，必须支持已接入会话的暂停调度，否则突发流量后会陷入KV
  cache命中率持续走低的死循环，吞吐量砍半也无法自行恢复

  - 可直接复用论文的KV需求预算器方案，将活跃会话总KV需求控制在KV池的75%~95%滞后区间，无需按业务workload调参，仅在网关层实现即可完全避免前缀缓存亚稳态失效

  - 若服务出现GPU利用率高但吞吐量低、KV cache命中率持续低于20%的异常，不要仅限流新请求，暂停部分已接入会话可在5分钟内恢复90%+命中率，恢复效率是单纯限流的4倍以上'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent类服务（编码助手、电商导购、多轮推荐交互）重度依赖prefix caching降低推理成本：缓存命中时仅需增量prefill千级token，未命中需重算10~40K token全上下文，成本差10倍以上。此前未发现的问题是：短暂突发流量后即使负载回落到正常承载水平，服务会持续陷入低命中率、低吞吐量的亚稳态，常规限流手段无法恢复。
### 方法关键点
- 配对对照实验：两组服务跑完全相同的基准流量，仅一组注入5分钟突发流量，严格控制变量验证亚稳态存在
- 根因定位：Agent会话是闭环的，响应变慢会提升系统并发会话数，总KV需求超过KV池后，LRU会在会话下一次请求前淘汰其前缀缓存，形成「miss→响应变慢→并发升高→更多miss」的正反馈
- 网关层KV预算控制：限制活跃会话总KV需求在KV池的75%~95%滞后区间，超过阈值则暂停部分已接入会话，无需workload调参，无需修改推理引擎
- 对比baseline：仅准入限流、AIMD自适应并发、固定会话数上限
### 关键结果
- vLLM + Qwen3-8B实验：12组配对实验中9组突发流量后持续降级，命中率从95%跌到10%，吞吐量砍半，70分钟无法自行恢复，无突发对照组全程健康
- 恢复实验：KV预算器5分钟内100%恢复所有崩溃实例，命中率回到93%~95%；仅新请求限流仅恢复1/7实例，耗时21分钟以上
- 失效可复现于SGLang、Qwen3-32B + SWE-bench真实Agent轨迹场景，CPU KV offload仅能延迟失效无法避免
### 核心结论
带prefix caching的闭环Agent服务性能瓶颈不是GPU算力，而是KV池能承载的活跃会话工作集，仅限流新请求救不了崩溃的服务，暂停部分已接入会话是最高效的恢复手段
