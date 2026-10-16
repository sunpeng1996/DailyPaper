---
title: 'When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel
  Prefill'
title_zh: 面向上下文并行预填充的远程KV缓存层扩展优化
authors:
- Muhammad Ibrahim
affiliations:
- Multiverse Computing
arxiv_id: '2610.21500'
url: https://arxiv.org/abs/2610.21500
pdf_url: https://arxiv.org/pdf/2610.21500
published: '2026-10-14'
collected: '2026-10-16'
category: LLM
direction: LLM serving · KV cache 性能优化
tags:
- KV cache
- LLM Serving
- Context Parallelism
- Prefill Optimization
- LMCache
one_liner: 提出上下文并行场景下远程KV缓存分片方案，将高命中率流p99延迟降低124倍
practical_value: '- 长上下文LLM服务（比如商品多模态信息总结、用户多轮对话Agent、长文本召回语义匹配）可复用本文的成本模型，先计算当前硬件下远程KV的带宽阈值，低于阈值优先选择重算，避免反而劣化性能

  - 采用上下文并行部署LLM服务时，可直接复用论文提交到LMCache上游的分片优化、按rank拆分远程KV实例、异步加载三个补丁，无需二次开发即可降低长尾延迟

  - 部署远程KV缓存时，短于阈值（本实验为17k token）的prompt（如电商query理解、短文案生成、商品标题改写）直接跳过KV读取，避免固定开销导致的性能损失

  - 排查KV缓存长尾问题时，优先检查本文提到的三个工程bug：丢失完成信号、缺键GET卡住、异步GET键名错误，都是线上易踩的共性坑'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文LLM预填充阶段耗时占比极高，远程共享KV cache是降低预填充成本的通用方案，但生产部署中出现远程KV读取比GPU直接重算还慢、长尾延迟数倍飙升的问题，甚至导致服务回滚，亟需针对性优化。

### 方法关键点
- 提出双参数成本模型：远程KV命中收益仅当带宽高于阈值B*=s*R（本场景下为2.53GB/s），且存在固定开销T0≈0.33s，短于17k token的prompt命中收益永远低于重算
- 上下文并行（PCP）场景下分片存储MLA KV：按chunk索引对rank取模分配所有权，复用现有调度逻辑即可正确返回最长缓存前缀，无额外通信开销
- 按rank拆分远程KV实例：每个rank对应独立Valkey实例，无需集群协议或客户端哈希，GET带宽提升6.3倍至10.76GB/s
- 新增分片场景下的异步加载逻辑，修复三个导致无限卡顿的客户端bug

### 关键实验
基于生产流量trace replay，测试GLM-5.3 FP8 MoE模型在8×B300节点上的表现，对比原生LMCache：
- 98.5% token命中的高命中率流量下，p99延迟从83.32s降至0.67s，降幅达124倍
- 仅用分片优化预填充吞吐量提升14%，搭配上游FlashInfer内核优化共提升34%
- 16k token场景下远程KV读取p50延迟从0.88s降至0.4s，p99表现优于直接重算

### 核心结论
判断KV缓存层收益要对标所服务硬件的预填充速度，而不是单纯看网络延迟，当前GPU算力增长下重算的性能基线已经很高。
