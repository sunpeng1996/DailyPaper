---
title: 'MoE-ViE: Mixture of Experts Vision Encoder for Efficient Image and Video Understanding'
title_zh: MoE-ViE：面向高效图像视频理解的混合专家视觉编码器
authors:
- Bonan Zhang
- Shiyu Dong
- Quan Hung Tran
- Katharina Gschwind
- Shuqi Yang
- Sijia Chen
- Adel Ahmadyan
- Seungwhan Moon
- Lu Zhang
- Ahmed Kirmani
affiliations:
- Meta
arxiv_id: '2608.17402'
url: https://arxiv.org/abs/2608.17402
pdf_url: https://arxiv.org/pdf/2608.17402
published: '2026-08-17'
collected: '2026-08-19'
category: Multimodal
direction: 多模态理解 · MoE视觉编码器优化
tags:
- MoE
- Vision Encoder
- CLIP
- Multimodal
- Latency Optimization
- Video Understanding
one_liner: 提出细粒度MoE结构的高效视觉编码器，性能超1.7倍规模稠密SOTA，延迟仅为其76%
practical_value: '- 电商多模态搜广推场景的视觉特征提取可复用细粒度MoE设计，在不增加推理计算量的前提下提升商品图、短视频的表征能力，平衡效果和成本

  - MoE类模型（含推荐排序MoE、多模态MoE）的负载均衡可采用无辅助损失的z-score修正方案，避免辅助损失干扰主任务优化，同时提升专家利用率

  - 多模态模型跨任务微调（如从通用图像到商品短视频）时，可采用帧级蒸馏+冻结MoE专家层的方案，无需混排原任务数据即可避免原能力退化

  - 基于Triton实现的MoE定制Kernel（分组GEMM+算子融合）可直接复用，比PyTorch原生实现提速2.5倍以上，解决MoE落地的延迟瓶颈'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
CLIP类视觉编码器是多模态大模型的核心组件，稠密缩放会大幅提升计算成本和推理延迟，现有MoE视觉编码器设计未达到SOTA性能，且缺少适配图像/视频统一编码的高效训练、工程优化方案，无法满足搜广推、多模态Agent等对低延迟高表征能力的需求。

### 方法关键点
- 架构设计：采用细粒度MoE替换视觉塔MLP层，每个专家宽度仅为稠密MLP的1/4，搭配1个恒激活的共享专家，用Sigmoid门控替代Softmax避免专家竞争
- 负载均衡：提出基于z-score的无辅助损失均衡策略，通过动态调整路由偏置实现专家负载均匀，不干扰主对比训练目标
- 工程优化：基于Triton实现MoE定制Kernel，通过分组GEMM聚合多专家矩阵运算、算子融合减少HBM访问，原生实现延迟降低2.5倍以上
- 训练策略：图像对比预训练后做视频微调时，加入帧级蒸馏+冻结MoE专家层+冻结文本塔MLP，避免图像理解能力退化，实现图像视频统一编码

### 关键结果
在3.5B图文对预训练，图像、视频零样本基准测试，对比SOTA稠密模型PEcoreG：最大模型MoE-ViE-H总参数3.5B，激活参数仅1.1B，零样本性能匹配1.7倍规模的PEcoreG，推理延迟仅为其76%；对齐Llama 3.1 8B后，在图像、视频多模态任务上性能超过激活参数5倍以上的SOTA模型；视频微调方案使K400分类精度提升的同时，ImageNet精度无下降。

MoE落地的性能增益不仅来自架构设计，更需要配套的工程优化、训练策略配合，才能把稀疏激活的理论效率转化为实际的性能-延迟收益。
