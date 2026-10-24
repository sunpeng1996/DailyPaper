---
title: 'Stream4D: Streaming 4D Reconstruction with Training-free Motion Decoupling
  via Causal KV-Cache Attention'
title_zh: Stream4D：基于因果KV缓存注意力的免训练运动解耦流式4D重建
authors:
- Wei Zhang
- Ying Feng
- Mengtong Wu
- Shiqiang Gong
- Huaqi Zhang
- Qi Zhang
affiliations:
- Northwestern Polytechnical University
- vivo BlueImage Lab
- vivo Mobile Communication Co., Ltd.
arxiv_id: '2610.31320'
url: https://arxiv.org/abs/2610.31320
pdf_url: https://arxiv.org/pdf/2610.31320
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 流式4D重建 · KV缓存利用
tags:
- KV-Cache
- Causal Attention
- 4D Reconstruction
- Streaming Processing
- Training-free
one_liner: 挖掘因果Transformer KV缓存内运动线索，免训练实现流式4D重建动静态区域解耦
practical_value: '- 可借鉴因果KV缓存隐式编码时序线索的思路，在流式推荐/广告排序场景中，无需额外训练即可从存量KV缓存中挖掘用户行为时序变化特征

  - 软掩码抑制干扰区的方案可迁移至长序列用户兴趣建模，动态屏蔽过时/无关历史行为的注意力权重，降低长序列推理噪声

  - 免训练兼容现有因果Transformer架构的设计思路，可用于低迭代成本升级已上线的LLM4Rec/生成式推荐系统，避免全量重训成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有流式4D重建方法默认场景静态，处理长序列时易出现位姿漂移、重影伪影问题，且多数方案需要额外训练，难以兼容已有因果Transformer流式架构。

### 方法关键点
核心观察是因果注意力的KV缓存内隐式编码了丰富的时序运动线索，通过自适应聚合多注意力层、多时间窗口的运动线索，融合深度先验生成精确动静态区域掩码；再用软键掩码方案抑制因果注意力中动态区域的干扰，提升位姿估计精度，整个框架免训练，可直接嵌入StreamVGGT、Stream3R等现有因果Transformer backbone。

### 关键结果
在多动态场景基准测试中，位姿估计、静态场景重建质量显著提升，长序列重影问题有效缓解，同时输出可靠的动态掩码，完全保留原有因果注意力的推理效率。
