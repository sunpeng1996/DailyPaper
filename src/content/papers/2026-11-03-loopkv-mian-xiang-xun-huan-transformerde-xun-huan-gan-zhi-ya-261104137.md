---
title: 'LoopKV: Loop-Aware KV Cache Compression for Serving Looped Transformers'
title_zh: LoopKV：面向循环Transformer的循环感知KV缓存压缩算法
authors:
- Tianle Zhou
- Yang Zhang
- Tianyu Wu
- Zhuohan Wang
- William Nixon
- Juncheng Yang
affiliations:
- Harvard University
- University of California San Diego
- University of Chicago
arxiv_id: '2611.04137'
url: https://arxiv.org/abs/2611.04137
pdf_url: https://arxiv.org/pdf/2611.04137
published: '2026-11-03'
collected: '2026-11-04'
category: LLM
direction: LLM推理 · KV cache压缩
tags:
- KV cache
- Looped Transformer
- Quantization
- LLM Serving
- vLLM
one_liner: 面向循环Transformer的(循环,层)粒度KV缓存压缩，精度无损下较均匀4位量化goodput提升1.7-2.2倍
practical_value: '- 针对多轮迭代的Looped LLM推理场景（比如Agent思考链、多轮推荐reasoning），可以复用(循环,层)粒度的敏感性离线
  profiling + 多约束背包规划的思路，在精度损失可控前提下提升单卡服务并发

  - 存储INT4的V值时拆分为高低2个bit平面，运行时根据attention score动态决定是否读取低bit平面的trick，可以直接复用到普通LLM的KV
  cache优化，不需要改模型结构，实测能减少13-14%的V读取量

  - 若业务落地Looped类大模型（比如Ouro、Huginn这类低参高推理能力的模型），可以直接复用LoopKV的vLLM插件方案，单卡16K上下文下goodput比均匀4位量化高1.7-2.2倍，精度无显著下降'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Looped Transformer通过重复共享层迭代提升参效比，推理能力可匹配2-3倍参数量的普通Transformer，但每个循环单独存储KV cache导致显存开销是同规模普通Transformer的数倍，KV缓存成为服务batch扩容的核心瓶颈；现有通用KV量化方法或粗粒度按循环分配精度的方案，没有区分不同(循环,层)单元的量化敏感性，容易造成不必要的精度损失或显存浪费。

### 方法关键点
- 离线阶段：对每个(循环,层)单元（称为cell）单独profiling 4位存储、2位存储、复用最后一轮KV三种方案的精度损失，通过多约束背包算法在总精度、总存储预算下最小化KV读取量，生成读优化/存储优化两种配置
- 在线阶段：INT4的V值拆分为高低2个2bit平面，运行时根据当前循环的attention score，仅高权重token才读取低bit平面，减少无效读取
- 工程实现：基于vLLM实现融合kernel，全解码步骤支持CUDA graph replay，单步主机调用从504次降到17次

### 关键实验
在Ouro-1.4B/2.6B、Dory-4B上测试，对比BF16、FP8、KIVI-4（均匀4位量化）等基线；单RTX PRO 6000上16K上下文场景下，存储优化版LoopKV-M比KIVI-4少存35%KV，SLO约束下goodput是KIVI-4的1.7-2.2倍，6个公开基准测试精度无显著低于BF16的情况。

### 核心结论
Looped模型的KV缓存是二维网格而非一维堆栈，仅需一次低成本离线profiling即可按cell粒度分配精度和复用策略，实现精度与吞吐的最优平衡。
