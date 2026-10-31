---
title: 'AB-Attention: Accurate Block Attention for Accelerating Video Diffusion Transformers'
title_zh: AB-Attention：加速视频扩散Transformer的精准块注意力机制
authors:
- Bin Xu
- Mo Zhang
- Zhengfeiyang Zhang
- Xinfeng Yang
- Yixing Ma
- Wei Wang
- HeXin Wang
- Pengfei Zhou
- Wangbo Zhao
affiliations:
- InfRec
- The Chinese University of Hong Kong, Shenzhen
- Shandong University
- The University of Tokyo
- Fudan University
arxiv_id: '2610.39663'
url: https://arxiv.org/abs/2610.39663
pdf_url: https://arxiv.org/pdf/2610.39663
published: '2026-10-28'
collected: '2026-10-31'
category: Other
direction: 稀疏注意力优化 · Transformer推理加速
tags:
- Sparse-Attention
- Diffusion-Transformer
- Inference-Optimization
- Kernel-Optimization
- Video-Generation
one_liner: 训练无关的精准块注意力方案，高稀疏度下保持生成精度同时显著提升视频扩散Transformer推理速度
practical_value: '- 块内聚类评估KV块重要性的思路可迁移到生成式推荐长序列用户行为建模的注意力计算，大幅降低高维attention开销

  - 带逆概率重加权的采样方法可用于推荐召回/粗排阶段的候选集偏差修正，避免粗筛截断导致的有效候选丢失问题

  - 小KV块聚合为tensor-core友好tile的算子优化技巧可直接复用在LLM推理服务的attention算子开发，无额外成本提升吞吐'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
视频扩散Transformer的3D全注意力二次复杂度是推理核心瓶颈，现有动态块稀疏注意力在高稀疏度下精度退化严重，存在块重要性评估不准、截断导致softmax信息丢失、块粒度与张量核适配效率低等问题。
### 方法关键点
AB-Attention为训练无关的稀疏注意力方案，核心设计三点：1. 块内查询聚类Selector（IBCS）低成本精准评估块重要性，无需打乱token；2. 带包含概率加权的采样（SIP）按重要性比例采样KV块并逆概率重加权，单轮即可估计稠密注意力避免截断损失；3. 定制化算子将小KV块聚合为张量核友好的tile，无额外成本优化选择粒度。
### 关键结果
在Wan2.1、混元视频模型上实现89%-92%注意力计算跳过，比基线少计算1.8-3.6倍注意力量，PSNR较最强基线最高提升4.4dB，端到端推理速度最高提升2.23倍。
