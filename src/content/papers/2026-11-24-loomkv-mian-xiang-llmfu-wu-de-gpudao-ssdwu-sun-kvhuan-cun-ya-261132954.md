---
title: 'LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving'
title_zh: LoomKV：面向LLM服务的GPU到SSD无损KV缓存压缩
authors:
- Wentao Zhu
- Ziao Sheng
- Peng Deng
- Huiqi Hu
- Xuan Zhou
- Xing Wei
- Zhuang Wang
affiliations:
- East China Normal University
- ZTE Corporation
arxiv_id: '2611.32954'
url: https://arxiv.org/abs/2611.32954
pdf_url: https://arxiv.org/pdf/2611.32954
published: '2026-11-24'
collected: '2026-11-25'
category: LLM
direction: LLM服务 · KV缓存无损压缩
tags:
- KV Cache
- Lossless Compression
- LLM Serving
- GPU Optimization
- Tiered Storage
one_liner: 提出无损KV缓存压缩框架LoomKV，兼容原生vLLM/LMCache，同时优化分层存储与GPU池容量
practical_value: '- 部署多轮对话Agent、RAG检索服务的业务可直接复用Tier模式，无需修改vLLM/LMCache原有逻辑，即可将DRAM+SSD分层缓存有效容量提升1.4倍，KV淘汰引发的重计算开销大幅降低，TTFT最高下降1.7倍。

  - 长上下文LLM推理场景（如长用户行为序列建模、多轮Agent会话）可复用Pool模式的FragPack布局+融合解码Attention Kernel，无精度损失前提下GPU
  KV池并发请求容量提升30%以上，推理速度优于FlashAttention-3。

  - 可直接迁移per-head双级3比特固定宽编码设计，避免可变长编码的GPU并行瓶颈，GPU解压速度可达1182GB/s，远高于nvCOMP等通用压缩方案，适配低延迟线上服务要求。

  - 分层存储的异步长度回读、多缓冲流水线设计可直接复用，解决压缩后可变长块的同步开销问题，不会阻塞核心推理链路。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM服务中KV缓存占显存/存储开销极高，多轮Agent、RAG请求的长前缀复用依赖GPU→DRAM→SSD分层缓存，现有有损压缩会改变输出精度需要逐模型逐任务重验，通用无损压缩GPU解压速度慢、适配现有推理引擎成本高，同时分层缓存容量不足和GPU KV池容量不足是两个独立的性能瓶颈，直接限制服务并发和响应速度。

### 方法关键点
- 核心编码：对BF16 KV的高字节（符号+7位指数）采用per-head校准的双级3比特固定宽编码，低字节原封不动存储，避免可变长编码的GPU并行瓶颈，BF16压缩比稳定在0.71，FP8压缩比0.85-0.87。
- Tier模式：设计TileStream布局，支持GPU并行解压直接写入散列的KV页，无需中间拷贝，兼容现有分层缓存的淘汰、预取逻辑，无需修改推理引擎源码。
- Pool模式：设计FragPack布局，将压缩KV按线程访问顺序排列，配合融合解码-attention kernel，直接从压缩缓存读取数据做计算，无需解压到GPU显存。
- 工程优化：异步存储长度回读、多缓冲流水线设计，避免可变长块的同步开销，兼容原生vLLM、LMCache。

### 关键结果
在AgentX多轮Agent trace、生产AI IDE trace上测试，基线为原生vLLM+LMCache、FlashAttention-3：
- Tier模式：分层缓存有效容量提升1.4倍，LRU淘汰临界点的goodput提升2.7-3.6倍，TTFT降低1.9-3.1倍，重复请求TTFT最多降1.7倍，仅损失最多2.2%吞吐量，精度与原生实现完全一致。
- Pool模式：GPU KV池可容纳1.31-1.34倍token数，并发请求数从8提升到12时goodput不变，融合Kernel速度优于FlashAttention-3。
- 混合约束场景：生产trace下Tier、Pool模式goodput分别提升1.24倍、1.59倍。

最值得记住的结论：无损KV压缩可以在几乎不损失性能和精度的前提下，同时缓解分层存储和GPU显存的KV容量瓶颈，适配成本极低，适合直接落地到线上LLM服务。
