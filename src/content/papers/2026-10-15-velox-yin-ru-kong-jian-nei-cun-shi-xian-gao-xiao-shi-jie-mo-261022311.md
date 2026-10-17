---
title: 'Velox: Spatial Memory Makes World Models Efficient'
title_zh: Velox：引入空间内存实现高效世界模型推理
authors:
- Qiuhong Shen
- Shizun Wang
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2610.22311'
url: https://arxiv.org/abs/2610.22311
pdf_url: https://arxiv.org/pdf/2610.22311
published: '2026-10-15'
collected: '2026-10-17'
category: Multimodal
direction: 多模态世界模型 · KV缓存推理优化
tags:
- KV Cache
- World Model
- Attention Routing
- Video Generation
- Inference Optimization
one_liner: 实现训练无关的空间注意力路由机制，解决长视频世界模型KV缓存膨胀导致的推理延迟问题
practical_value: '- 长序列生成场景可复用该训练无关的注意力路由思路，仅基于几何/语义 overlap 筛选KV缓存条目，无需重训模型即可降低推理延迟

  - 固定Token块粒度匹配FlashAttention tiled执行的工程技巧，可直接迁移到生成式推荐、多模态Agent的长上下文推理链路

  - 异步执行非核心计算的调度策略，可用于优化生成式文案/商品短视频的实时响应性能'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
长视频世界模型生成需保留历史上下文保证一致性，现有分块扩散方案依赖持续膨胀的KV缓存，生成越靠后的分块推理延迟越高，无法满足交互式场景的响应要求。
### 方法关键点
1. Velox为训练无关的注意力路由，将历史块表示为带深度区间的相机视锥体 slab，通过近邻优先多翘曲算法获取当前块深度
2. 对已覆盖区域用视锥体 slab 重叠度软调制各层块重要性，未覆盖区域保留原生模型路由，固定Token块粒度适配FlashAttention分块执行，消除随生成长度增长的注意力开销
3. 视锥体 slab 构造与去噪步骤在同一GPU上异步执行，无额外硬件成本
### 关键结果
- 第48个分块时，注意力加速4.36×，去噪步骤加速2.43×
- 158个用例的WBench导航测试集上，性能仅比全量KV缓存的LingBot-Fast-Cam低0.15平均点
