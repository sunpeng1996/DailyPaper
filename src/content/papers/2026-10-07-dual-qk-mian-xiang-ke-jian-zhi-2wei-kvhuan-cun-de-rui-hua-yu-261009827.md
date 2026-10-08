---
title: 'Dual-QK: Sharp Queries and Flat Keys for Prunable 2-bit KV Caches'
title_zh: Dual-QK：面向可剪枝2位KV缓存的锐化查询与平坦化键方法
authors:
- Sunjoo Whang
- Jungjun Oh
- Minsung Kim
- Dongho Seo
- Jisu Shin
- Gregory Kielian
- Hoi-Jun Yoo
- Sangjin Kim
affiliations:
- KAIST
- GIST
- Google Research
arxiv_id: '2610.09827'
url: https://arxiv.org/abs/2610.09827
pdf_url: https://arxiv.org/pdf/2610.09827
published: '2026-10-07'
collected: '2026-10-08'
category: LLM
direction: LLM推理优化 · KV缓存量化与剪枝
tags:
- KV Cache
- INT2 Quantization
- Dynamic Channel Pruning
- Long Context LLM
- Inference Optimization
one_liner: 通过配对非正交Q/K变换同时实现INT2 KV量化与动态通道剪枝，大幅提升长上下文LLM解码吞吐量
practical_value: '- 部署长上下文LLM驱动的电商导购Agent、个性化文案生成、用户长行为序列建模等服务时，可直接集成Dual-QK的SGLang实现，40%通道稀疏度下精度损失可忽略，单卡解码吞吐量最高提升3.75倍，降低服务成本

  - 推荐系统注意力层（召回/排序的Multi-Head Attention）可复用Q/K联合分布优化思路，对KV做低比特量化+动态通道剪枝，降低大模型排序服务的推理延迟，支撑更高并发

  - 支持128K以上超长上下文的LLM服务可直接复用Bucket-relative RoPE设计，无需重训模型即可解决长上下文下静态量化基的分布偏移问题，保障长序列推理精度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长上下文LLM推理中，KV缓存的存储与带宽开销随上下文长度线性增长，是长序列推理的核心瓶颈。低比特量化可降低存储开销，动态通道剪枝可减少KV读取量，但二者存在固有需求冲突：量化需要键（K）的通道分布尽可能平坦以降低离群值导致的量化误差，剪枝需要查询（Q）的通道分布尽可能尖锐以清晰分离重要/不重要通道；此前基于共享正交变换的方案无法同时满足两个需求，限制了优化收益的天花板。
### 方法关键点
- 配对非正交Q/K变换：对K做部分白化平坦分布，对Q做PCA集中能量，通过互逆变换保证QK点积不变，不损失原生注意力计算精度
- 通道0保护：将能量最高的首通道保留为BF16精度，剩余通道采用INT2非对称量化，同时缩小剩余通道的量化范围提升精度
- 桶相对RoPE：按2048 token将长上下文分桶，每个桶内K先做锚点RoPE逆变换，解决长上下文下静态量化基的分布偏移问题
- 动态通道剪枝：按GQA组内查询的L2范数动态选择Top 60%通道参与计算，进一步降低KV读取量
### 关键实验
在Llama-3.1-8B、Qwen3-4B/8B、Ministral-3-14B四个模型上测试，覆盖推理、代码生成、数学推理、长上下文检索5类基准，对比OSCAR、KIVI、TurboQuant等SOTA方案：40%通道稀疏度下多数任务精度超过OSCAR；128K上下文下实现6.8×KV缓存压缩、8.3×KV读取量降低，SGLang实现中解码吞吐量最高达未剪枝BF16的3.75倍
### 核心结论
Q/K变换不需要强制正交，通过联合优化二者分布可以在几乎不损失精度的前提下同时实现KV量化和剪枝的收益最大化
