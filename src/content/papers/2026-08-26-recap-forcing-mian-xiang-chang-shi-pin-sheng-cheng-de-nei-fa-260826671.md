---
title: 'RECAP-Forcing: Retaining Content Appearances for Long Video Generation'
title_zh: RECAP-Forcing：面向长视频生成的内容外观留存方法
authors:
- Haiyang Xu
- Zheng Ding
- Zhuowen Tu
affiliations:
- UC San Diego
arxiv_id: '2608.26671'
url: https://arxiv.org/abs/2608.26671
pdf_url: https://arxiv.org/pdf/2608.26671
published: '2026-08-26'
collected: '2026-09-02'
category: Multimodal
direction: 多模态长视频生成 · KV cache优化
tags:
- KV cache
- Long Video Generation
- Inference Optimization
- Long Context
- Autoregressive Generation
one_liner: 无训练推理优化方法，按外观新颖度留存KV cache解决长视频自回归生成的记忆漂移问题
practical_value: '- 长上下文Agent推理场景可复用该KV cache淘汰策略，替换纯时序淘汰逻辑，优先留存首次出现的核心实体、规则对应的KV，降低长对话的信息漂移率

  - 生成式商品短视频、多模态广告素材生成场景，可直接复用该无训练推理优化方案，保留核心商品外观、标识的KV cache，提升生成内容的品牌/商品一致性

  - 长序列用户行为建模可参考该记忆组织逻辑，优先留存高novelty的首次行为特征，而非仅加权近期行为，提升长周期用户兴趣刻画的准确性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
自回归长视频生成存在固有记忆瓶颈，有限注意力窗口下现有方案仅按时间维度保留近期帧、压缩丢弃远期内容，易出现主体漂移、内容一致性退化的问题。

### 方法关键点
提出无训练的RECAP-Forcing推理优化方案，按外观新颖度而非时间先后组织KV cache：
1. 初始生成阶段用attention sink保留全量初始场景缓存；
2. 生成过程中基于光流检测新颖内容（新主体、新场景、新暴露区域），存入novelty bank留存对应KV cache，内存开销仅和新增内容量挂钩，而非视频时长。

### 关键结果
无需额外训练和新增参数，在多个主流长视频生成基线模型上，视觉质量、语义保真度均优于现有时序记忆优化方案，可稳定支撑分钟级长视频的主体一致性生成
