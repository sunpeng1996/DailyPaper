---
title: What Is Redundant at High Resolution? Efficient Attention and Feed-Forward
  Design for All-in-One Image Restoration
title_zh: 高分辨率冗余分析：面向一体化图像复原的高效注意力与前馈设计
authors:
- Dongheon Lee
- DongJae Lee
- Sewhan Chun
- Chanseul Cho
- Youngwook Kim
- Youngmin Ro
- Yonghyun Jeong
affiliations:
- University of Seoul
- NAVER Cloud
- Kookmin University
arxiv_id: '2611.33636'
url: https://arxiv.org/abs/2611.33636
pdf_url: https://arxiv.org/pdf/2611.33636
published: '2026-11-24'
collected: '2026-11-26'
category: Multimodal
direction: 多模态图像复原 · 高效Transformer优化
tags:
- EfficientTransformer
- ImageRestoration
- AttentionOptimization
- FFNOptimization
- HighResolutionProcessing
one_liner: 定位注意力与FFN三类冗余，设计高效多尺度图像复原网络，推理速度最高提4.24倍
practical_value: '- 高分辨率特征冗余分析思路可迁移至多模态推荐的商品图像/视频特征编码环节，降低大尺寸特征计算开销

  - 块路由混合注意力+邻域路由共享的设计可复用在多模态召回的粗/细粒度特征融合模块，提升推理速度

  - Dual-Space FFN的分空间计算思路可优化现有LLM/多模态模型的FFN计算延迟，适配低算力部署场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
多尺度架构是一体化图像复原（AIO-IR）的主流方案，可在低分辨率阶段捕获大尺度上下文、高分辨率阶段补全细节，但高分辨率阶段处理大尺寸特征图带来极高计算与内存开销，成为落地瓶颈。
### 方法关键点
首先定位三类核心冗余：最细尺度阶段的逐query读取、中间阶段邻域query的key路由、ConvFFN扩展特征空间的空间混合；针对性优化：1. 最细尺度阶段用输入无关可学习核替代高开销自注意力；2. 中间阶段提出块路由混合注意力，结合粗尺度密集注意力与细尺度块稀疏注意力，邻域query共享路由索引；3. 提出Dual-Space FFN，紧凑空间做空间混合、扩展空间做点态非线性变换，支持高效核融合。
### 关键结果
HiGLR达到SOTA性能，推理速度较现有方法最高提升4.24倍。
