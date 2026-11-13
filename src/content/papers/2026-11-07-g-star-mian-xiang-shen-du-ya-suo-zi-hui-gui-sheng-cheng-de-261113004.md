---
title: 'G-STAR: Group-Scaled Token Capacity for Deeply Compressed Autoregressive Generation'
title_zh: G-STAR：面向深度压缩自回归生成的分组缩放Token容量
authors:
- Xu Huang
- Ye Huang
- Xiaotong Li
- Zhengrong Yue
- Jialv Zou
- Minhao Jing
- Haodong Li
- Wenhao Yan
- Yaxin Luo
- Duomin Wang
affiliations:
- Peking University
- Meituan Longcat
- Shanghai Jiao Tong University
- Huazhong University of Science and Technology
- The Chinese University of Hong Kong
arxiv_id: '2611.13004'
url: https://arxiv.org/abs/2611.13004
pdf_url: https://arxiv.org/pdf/2611.13004
published: '2026-11-07'
collected: '2026-11-13'
category: LLM
direction: 自回归生成 · Token高倍压缩提速
tags:
- Autoregressive Generation
- Token Compression
- Product Quantization
- Inference Acceleration
- Semi-autoregressive Decoder
one_liner: 提出空间-分组共缩放框架G-STAR，实现自回归生成高倍压缩同时提20倍推理速度
practical_value: '- 高分辨率商品图、营销素材生成场景可复用空间-分组共缩放规则，固定信息预算下实现32×以上Token压缩，降低推理成本

  - 半自回归解码器设计可迁移到文案、商品标题生成类自回归任务，平衡并行计算效率与生成语义连贯性

  - 乘积量化的分组大小缩放规则可复用在推荐系统Semantic ID编码压缩环节，降低向量检索与序列建模算力开销'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
离散自回归生成存在固有trade-off：长Token序列保留高质量表征但生成速度慢，高空间压缩又会显著降低表征能力，现有方案难以同时满足高压缩比、生成质量与低推理延迟要求。
### 方法关键点
1. 基于乘积量化推导得到固定信息预算下，分组大小需与单轴空间压缩因子呈二次缩放的核心规则；
2. 提出空间-分组共缩放框架G-STAR，支持32×乃至有效64×的高压缩比，同时保留重建、理解与生成性能；
3. 设计半自回归解码器，结合并行特征计算与轻量因果建模，高效解决大分组带来的组内依赖建模问题。
### 关键结果
在GenEval、DPG-Bench等5个主流文本生成图像基准上性能比肩SOTA模型；1024×1024分辨率下推理速度较过往离散自回归模型提升20×，单张NVIDIA H200上生成单图仅需2.5秒。
