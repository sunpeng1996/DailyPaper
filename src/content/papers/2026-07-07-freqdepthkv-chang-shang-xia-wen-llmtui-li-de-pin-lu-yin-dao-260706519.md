---
title: 'FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression
  in Long-Context LLM Inference'
title_zh: FreqDepthKV：长上下文LLM推理的频率引导深度共享KV缓存压缩方法
authors:
- Anna Córdoba
- Adam Puente Tercero
- Nerea Angulo Hijo
- Mar Linares Tercero
- Julia Barrientos
- Ainhoa Miranda
- Jesús Olivera
affiliations:
- Instituto de Investigación en Visión Artificial
arxiv_id: '2607.06519'
url: https://arxiv.org/abs/2607.06519
pdf_url: https://arxiv.org/pdf/2607.06519
published: '2026-07-07'
collected: '2026-07-08'
category: LLM
direction: LLM推理优化 · KV缓存压缩
tags:
- KV cache
- LLM inference
- long context
- compression
- depth sharing
one_liner: 通过层间频率分解与注意力敏感路由实现无训练KV缓存压缩，3.9倍压缩比下精度接近全缓存
practical_value: '- 电商场景下用LLM做长文案生成、多轮会话推荐、长文档RAG问答时，可直接集成FreqDepthKV降低KV缓存开销，支持32k长上下文的同时降低TTFT、提升单卡服务吞吐量

  - 可复用「低频共享+高频稀疏残差保留」的压缩思路，扩展到推荐系统的用户/物品语义向量缓存、RAG召回结果缓存场景，平衡压缩比与检索精度

  - 基于注意力logit扰动的自适应路由方法可借鉴到推荐特征选择环节：直接通过特征对排序得分的扰动程度决定是否保留，降低特征存储开销

  - 该方法无需模型重训练，可直接在现有LLM推理服务落地，可与KV量化、token eviction等现有优化叠加，进一步提升长上下文服务能力'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
长上下文LLM推理的瓶颈已从参数存储转移到KV缓存，现有压缩方案多采用token eviction、量化、粗粒度层间共享策略，容易丢失检索、推理任务依赖的稀疏层专属证据，导致精度大幅下降，亟需高压缩比下仍能保留关键信息的无训练KV缓存优化方案。

### 方法关键点
- 对相邻Transformer层的KV缓存做DCT变换，分解为跨层共享的低频分量和层专属的高频残差分量，低频分量仅存1份，大幅消除层间冗余
- Prefill阶段部署轻量在线探针，采样高熵注意力行、文档边界等关键位置，计算三种缓存模式（仅共享低频、共享+稀疏残差、全缓存）下的注意力logit重构误差，结合内存开销为每个注意力头分配最优模式
- 对残差模式的头，仅保留会导致logit扰动最大的Top-r个token的高频残差；解码时将分量重构与注意力计算融合，避免全缓存物化，无额外 overhead
- 无需模型重训练，兼容标准自回归解码框架，可与token eviction、量化等压缩方法叠加使用

### 关键实验
在32k上下文窗口下，对比全KV缓存、StreamingLLM、H2O、SnapKV、PyramidKV、MiniCache等9种基线，覆盖长上下文QA、摘要、代码生成三类任务：精度上Exact Match达58.3、F1 63.0、ROUGE-L 32.5、pass@1 48.1，和全缓存指标差距小于1%，比最优基线MiniCache的pass@1提升2.5个点；效率上解码吞吐量达70.4 tokens/s（较全缓存提升84%），TTFT降至2.06s，峰值KV内存仅6.2GB，实现3.9倍有效压缩比。

最值得记住的结论：KV缓存压缩不能只追求平均重构误差，保留对注意力logit影响大的稀疏高频残差，才能在高压缩比下避免长上下文检索、推理任务的精度损失。
