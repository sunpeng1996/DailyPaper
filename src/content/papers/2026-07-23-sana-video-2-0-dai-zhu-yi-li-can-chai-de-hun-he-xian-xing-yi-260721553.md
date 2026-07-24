---
title: 'SANA-Video 2.0: Hybrid Linear Attention with Attention Residuals for Efficient
  Video Generation'
title_zh: SANA-Video 2.0：带注意力残差的混合线性注意力高效视频生成方案
authors:
- Junsong Chen
- Jincheng Yu
- Yitong Li
- Shuchen Xue
- Haozhe Liu
- Jingyu Xin
- Yuyang Zhao
- Tian Ye
- Zhangjie Wu
- Zian Wang
affiliations:
- NVIDIA
arxiv_id: '2607.21553'
url: https://arxiv.org/abs/2607.21553
pdf_url: https://arxiv.org/pdf/2607.21553
published: '2026-07-23'
collected: '2026-07-24'
category: Multimodal
direction: 多模态视频生成 · 高效Transformer架构优化
tags:
- Diffusion Transformer
- Linear Attention
- Video Generation
- Efficient Inference
- Kernel Optimization
one_liner: 提出5B/14B统一架构混合注意力视频扩散Transformer，单GPU可生成720p高质量视频，效率大幅领先同规模软注意力模型
practical_value: '- 混合线性-软注意力3:1配比的设计思路可迁移到长序列用户行为建模、多轮对话召回等场景，在O(N)复杂度下保留全秩交互能力，平衡效果与推理延迟

  - Block Attention Residuals的特征复用机制可用于大模型推荐的深层结构优化，提升深层有效秩的同时降低特征重复计算开销

  - 端到端全栈优化（kernel fusion、caching、稀疏注意力结合）的工程技巧可直接复用在大模型推理服务部署中，大幅降低在线延迟'
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**：纯线性注意力长序列扩展性优但缺失全秩token交互，全软注意力视频DiT效果好但复杂度随序列长度平方增长，高分辨率/长视频生成部署成本极高，现有预训练模型线性化方案效果折损明显。
**方法关键点**：1. 采用3:1比例混合门控线性注意力与周期门控软注意力锚点，兼顾O(N)复杂度与全秩交互能力；2. 引入Block Attention Residuals路由块汇总特征到后续线性层，实现锚点特征复用，提升深层有效秩约12%；3. 从头训练完整混合架构，搭配Sol-Engine全栈优化（kernel fusion、缓存、稀疏注意力）进一步提升推理效率。
**关键结果**：单H100上40步采样480p视频VBench得分84.30，耗时13.2s；720p场景编译后DiT前向速度是全软注意力基线的3.2倍；叠加Sol-Engine后5B模型生成720p/5s视频仅需13.06s，速度为Wan 2.2-A14B的120倍。
