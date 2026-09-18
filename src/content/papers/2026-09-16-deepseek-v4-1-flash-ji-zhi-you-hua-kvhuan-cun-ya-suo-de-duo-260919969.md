---
title: 'DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression'
title_zh: DeepSeek-V4.1-Flash：极致优化KV缓存压缩的多模态MoE大模型
authors:
- DeepSeek-AI
- Anyi Xu
- B. Li
- Bangcai Lin
- Bing Xue
- BingCheng Xian
- Bingzheng Xu
- Bochao Wu
- Bowei Zhang
- Boyi Deng
affiliations:
- DeepSeek-AI
arxiv_id: '2609.19969'
url: https://arxiv.org/abs/2609.19969
pdf_url: https://arxiv.org/pdf/2609.19969
published: '2026-09-16'
collected: '2026-09-18'
category: LLM
direction: 大模型推理优化 · KV缓存压缩
tags:
- KV Cache
- MoE
- Long Context
- Quantization
- Inference Optimization
one_liner: 推出552B多模态MoE模型，三层优化将KV缓存压缩至上一代1/8，支持百万token上下文
practical_value: '- KV缓存优化的三层组合思路（跨层复用+低比特量化+部署侧SWA回放）可直接复用在自建LLM推理服务中，降低长上下文Agent、多轮对话推荐场景的GPU显存占用，提升单卡并发量

  - FP4 KV缓存量化的实践方案（MXFP4格式、仅量化全局KV、保留SWA KV为FP8）可直接迁移到现有大模型推理栈，几乎不损失效果的前提下压缩近一半KV存储

  - CED架构将Prefill阶段激活参数量降低到8B的设计，适合Agent频繁工具调用、多轮搜索推荐query补全的Prefill密集场景，大幅降低推理延迟

  - CSA2的跨层KV/索引复用机制，可借鉴到RAG召回的向量索引优化中，减少重复计算和存储开销'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
长 horizon Agent 普及带来大量输入密集型 workload，现有长上下文模型的Prefill计算成本高、KV缓存占用大，HBM/SSD存储、数据传输带宽已经成为部署成本下降的核心瓶颈，亟需更极致的KV缓存压缩方案。

### 方法关键点
- 架构：采用552B参数多模态MoE的Causal Encoder-Decoder（CED）架构，Prefill阶段单token仅激活8B参数，Decode阶段激活16B参数，适配输入密集的Agent场景；设计Compressed Sparse Attention 2（CSA2），分Full/Reindex/Reuse三种模式跨层复用全局KV和Top-K索引，减少冗余存储
- 量化：采用FP4精度存储全局KV缓存，SWA KV保留FP8精度，平衡压缩率和效果
- 部署：推出SWA Bounded Replay策略，仅需回放最近n_win个token即可近似重建SWA KV，无需持久化存储SWA KV

### 关键结果
- 全局KV缓存单token占用仅890字节，是DeepSeek-V4-Flash的1/4，是DeepSeek-V1的1/437；持久化KV缓存占用仅为上一代的1/8
- 上下文从4K扩展到1M时，Decode FLOPs仅提升1/4，几乎保持恒定
- 45T token多模态语料预训练，在Agent、推理、多模态基准上性能超过DeepSeek-V4-Flash，与前沿闭源模型表现相当

### 核心结论
KV缓存压缩需要模型架构、量化策略、部署调度三层联合优化，才能在不损失效果的前提下实现数量级的成本下降。
