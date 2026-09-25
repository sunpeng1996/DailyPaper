---
title: 'MILO: Efficient Many-shot In-Context Learning with Block-wise Low-rank Compression'
title_zh: MILO：基于块级低秩压缩的高效多示例上下文学习框架
authors:
- Youpeng Zhao
- Tian Tan
- Liqian Peng
- Jun Wang
- Alec Go
affiliations:
- Google
- University of Central Florida
arxiv_id: '2609.29913'
url: https://arxiv.org/abs/2609.29913
pdf_url: https://arxiv.org/pdf/2609.29913
published: '2026-09-24'
collected: '2026-09-25'
category: LLM
direction: LLM推理优化 · KV缓存压缩
tags:
- KV-cache
- In-Context Learning
- Low-rank Compression
- LLM Inference
- Many-shot ICL
one_liner: 提出块级低秩压缩+动态秩分配的KV缓存框架，实现多示例ICL缓存减半、吞吐量升1.8倍且精度损失可忽略
practical_value: '- 电商多示例RAG/ICL场景（如用户意图分类、商品文案生成）可直接复用块级低秩压缩方案，KV缓存内存降低50%，支撑更大规模示例库在线部署

  - 熵驱动的动态秩分配策略可迁移到用户行为序列压缩、多模态特征压缩场景，固定存储预算下信息保留率高于均匀压缩2-4%

  - 融合Triton内核、CUDA流/Graph的工程优化方案可直接复用在LLM推理服务中，端到端吞吐量提升3倍以上，适配高QPS广告/推荐实时生成场景

  - MILO可与INT8/KIVI量化叠加，KV缓存最高降低5.3倍，适合端侧Agent/离线推荐场景的轻量化部署'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多示例ICL可让LLM无需微调即逼近微调模型精度，但KV缓存随示例数线性增长，上千示例的KV缓存可达10GB以上，成为在线服务和端侧部署的核心瓶颈；现有KV压缩方案未针对多示例场景的跨示例冗余优化，要么精度损失大，要么压缩效率低。
### 方法关键点
- 块级低秩压缩：将多示例KV缓存按块拆分（每块含多个示例），对每个块的K/V矩阵分别做SVD低秩分解，平衡压缩效率和细粒度信息保留
- 动态秩分配：基于每个块的奇异值熵计算信息密度，在全局秩预算下贪心给高信息密度块分配更高秩，冗余块则激进压缩
- 工程优化：自研融合Triton内核，搭配CUDA流并行重建、CUDA Graph降低启动开销，最大化端到端收益
### 关键实验
基于Qwen2.5-3B/7B模型，在Banking77、MathQA等6个分类/推理数据集测试，对比Full Cache、ASVD、Palu等基线：相同50%压缩率下，精度比SOTA基线高4.5%，仅比全缓存低2-3%；端到端吞吐量比全缓存高1.8倍，比Palu/ASVD高37%/60%；叠加INT8/KIVI量化后，KV缓存最高可降低5.3倍，精度损失仍控制在5%以内。
### 核心结论
多示例ICL的KV缓存天然存在跨示例低秩冗余，块级自适应压缩是兼顾精度、内存、吞吐量的最优落地方案。
