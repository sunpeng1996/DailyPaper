---
title: 'FlashMask-3: Efficient and Expressive Mask-Aware Distributed Attention'
title_zh: FlashMask-3：高效高表达性的掩码感知分布式注意力
authors:
- Guoxia Wang
- Qianyue He
- Siming Wu
- Haoyang Xie
- Qiwen Bao
- Jinle Zeng
- Jiabin Yang
- Tian Wu
- Dianhai Yu
affiliations:
- Baidu Inc.
arxiv_id: '2610.17901'
url: https://arxiv.org/abs/2610.17901
pdf_url: https://arxiv.org/pdf/2610.17901
published: '2026-10-12'
collected: '2026-10-16'
category: Training
direction: 长上下文LLM训练 · 分布式注意力优化
tags:
- FlashAttention
- Distributed Training
- Long Context
- Hopper GPU
- Structured Attention Mask
one_liner: 针对Hopper GPU优化的零通信分布式结构化注意力内核 吞吐量最高提升3.71倍
practical_value: '- 做长上下文RAG Agent、生成式推荐的长用户序列建模时，可直接替换现有FlashAttention为FlashMask-3，单H100上结构化掩码场景最高提效141%，降低推理/训练成本

  - 分布式训练长上下文LLM时，可复用其零通信掩码本地化+计算通信重叠方案，4~32路上下文并行下最高可获得3.71倍的吞吐量提升

  - 分布式计算负载不均衡场景，可借鉴HCC-IPO分层负载均衡策略，在保证计算均衡的同时减少跨节点通信量，适配多机多卡集群'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文LLM/多模态模型训练中，结构化注意力掩码（文档、滑动窗口、前缀LM等）与多机上下文并行结合时，掩码成为核心性能瓶颈；原有FlashMask不支持Hopper GPU的TMA/WGMMA特性，也无分布式适配，无法满足大模型长序列训练的效率需求。
### 方法关键点
- 利用列稀疏掩码的结构特性，零通信clip-shift-max变换仅通过边界向量的逐元素操作完成各节点掩码本地化，无跨卡通信开销
- 针对Hopper GPU设计三角色warp专用内核，集成到FlashAttention-3的TMA/WGMMA流水线，新增KV索引生成角色处理掩码逻辑，几乎无额外开销；搭配PPT抢占式持久化tile调度器解决不规则掩码下的SM负载不均衡问题
- 提出HCC-IPO分层负载均衡器，交替优化跨卡计算均衡、跨节点通信量、节点内计算均衡，兼顾计算和通信效率
- 实现掩码感知的计算通信重叠，裁剪完全屏蔽的KV块通信，搭配拓扑感知分层路由进一步降低通信开销
### 关键实验
单H100上，4K~128K上下文、12种结构化掩码下，比FlashMask、FlexAttention、MagiAttention分别提升45%~141%、34%~71%、2%~44%的TFLOPs；4~32路上下文并行下，吞吐量比Megatron-Core CP（ring）、Megatron-Core CP（all-gather）、MagiAttention分别高1.80×~3.71×、1.71×~2.92×、1.09×~1.46×；118B-A14B MoE模型128K上下文端到端训练，比基线提升7.3%~11.0%吞吐量，注意力前后向提速24.5%~44.9%。
### 核心结论
列稀疏掩码的O(n)表示不仅是单卡内存优化手段，也是零通信分布式掩码适配的核心接口，可在不损失精度的前提下大幅提升长上下文训练效率。
