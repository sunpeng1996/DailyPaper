---
title: 'MixTok: Adaptive Visual Tokenization with Global 1D Tokens and Sparse 2D Refinement'
title_zh: MixTok：结合全局1D Token与稀疏2D精修的自适应视觉Token化方法
authors:
- Chenge Li
- Yefei He
- Xinyu Liu
- Feng Chen
- Hong Zhou
- Bohan Zhuang
affiliations:
- Zhejiang University
- The Hong Kong University of Science and Technology
- University of Adelaide
arxiv_id: '2610.13181'
url: https://arxiv.org/abs/2610.13181
pdf_url: https://arxiv.org/pdf/2610.13181
published: '2026-10-08'
collected: '2026-10-13'
category: Multimodal
direction: 多模态 · 自适应视觉Token化优化
tags:
- Visual Tokenization
- Multimodal
- Efficient Inference
- Adaptive Routing
- Feature Compression
one_liner: 提出混合视觉Tokenizer MixTok，平衡表征紧凑性与细粒度信息保留，降低视觉token开销
practical_value: '- 电商多模态内容（商品图、短视频）压缩存储可借鉴混合1D+稀疏2D token方案，相同token预算下保留更多商品细节，降低多模态召回/排序计算成本

  - 内容自适应路由的token分配逻辑可迁移至多模态推荐特征抽取阶段，对高信息密度区域（商品logo、核心卖点区）分配更多计算资源，提升表征质量

  - 混合特征解码架构可用于生成式推荐的商品图生成环节，低token开销下保障生成图细节还原度，提升推荐物料（配图+文案）质量'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视觉token化方案存在明显缺陷：网格2D tokenizer统一分配token忽略空间视觉复杂度差异，token开销极高；紧凑1D tokenizer聚合全局信息但丢失局部细粒度特征，无法满足多模态任务对细节的需求。

### 方法关键点
- 提出混合架构MixTok，结合全局1D紧凑表征与稀疏2D局部精修token
- 设计内容自适应路由模块，按精修优先级对候选位置排序，在固定平均token预算下动态决定每张图的2D token数量
- 将高分位置的2D特征替换1D表征恢复的对应空间特征，通过共享解码器从混合特征重建图像

### 关键结果
在ImageNet 256×256数据集上，平均128 token预算下rFID达1.195，131 token预算下gFID达1.95，重建与生成性能达到同期最优水平
