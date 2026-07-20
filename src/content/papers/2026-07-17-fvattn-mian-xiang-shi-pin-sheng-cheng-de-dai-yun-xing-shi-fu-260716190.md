---
title: 'FVAttn: Adaptive Sparse Attention with Runtime Load Balancing for Video Generation'
title_zh: FVAttn：面向视频生成的带运行时负载均衡的自适应稀疏注意力
authors:
- Hao Liu
- Chenghuan Huang
- Ye Huang
- Zhiying Wen
- Hao Liu
- Mohan Zhang
- Chen Li
- Ziyang Ma
- Jing Lyu
- Jiangsu Du
affiliations:
- Sun Yat-sen University
- WeChat HPC, Tencent Inc.
- WeChat Vision, Tencent Inc.
- Peking University
arxiv_id: '2607.16190'
url: https://arxiv.org/abs/2607.16190
pdf_url: https://arxiv.org/pdf/2607.16190
published: '2026-07-17'
collected: '2026-07-20'
category: Multimodal
direction: 多模态视频生成 · 稀疏注意力推理优化
tags:
- Sparse-Attention
- Load-Balancing
- Video-Diffusion
- Distributed-Inference
- DiT
- Inference-Optimization
one_liner: 提出免训练多GPU序列并行稀疏注意力系统，解决负载不均问题，大幅提升视频DiT推理速度
practical_value: '- 多GPU序列并行部署生成式推荐/多模态大模型服务时，可复用Top-p路由+Top-k保底的免训练稀疏注意力策略，直接降低推理延迟

  - 运行时负载均衡的P2P高负载头迁移+调度开销隐藏技巧，可迁移至MoE推荐模型分布式推理场景，解决专家负载不均导致的慢节点问题

  - 非关键节点空闲算力填充高价值计算块的思路，可用于生成式推荐批量推理场景，不增加核心路径延迟的前提下提升推荐效果'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：视频扩散Transformer（Video DiT）处理长时空序列时，自注意力是高分辨率视频生成的核心瓶颈；免训练稀疏注意力能降低计算成本，但多GPU序列并行下自适应Top-p路由会导致各头负载不均，引发慢节点问题，反而抵消稀疏收益。
**方法关键点**：1. 稀疏路由前端采用Top-p路由+Top-k安全保底+视频感知块组织策略，保证稀疏后效果不下降；2. 运行时负载均衡通过P2P通信迁移少量高负载头，缩短关键路径；3. 空闲感知稀疏增强利用非关键节点的剩余算力填充高价值块，同时通过计算重叠隐藏调度和迁移开销。
**关键结果数字**：在Wan2.2 I2V模型上，平均负载不均程度从1.34降至1.08；注意力速度相比FlashAttention提升4.41倍；DiT整体推理速度提升2.02~2.11倍，视频质量无明显下降。
