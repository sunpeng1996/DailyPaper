---
title: 'MixPT: Point Transformer with Interleaved Window and Global Attention'
title_zh: MixPT：采用交错窗口与全局注意力的点Transformer
authors:
- Minkyun Seo
- Hyungtae Lim
- Jaesik Park
affiliations:
- Seoul National University
- Massachusetts Institute of Technology
arxiv_id: '2610.31455'
url: https://arxiv.org/abs/2610.31455
pdf_url: https://arxiv.org/pdf/2610.31455
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 3D点云处理 · Transformer注意力优化
tags:
- PointTransformer
- AttentionOptimization
- WindowAttention
- GlobalAttention
- LowLatencyInference
one_liner: 以固定序列化+交错窗口与全局注意力调度，平衡点云Transformer的精度与推理延迟
practical_value: '- 长序列用户行为建模等场景可复用「交错窗口+全局注意力」调度模式，平衡全局信息捕捉能力与计算开销

  - 大Token量任务可借鉴「对池化后低分辨率Token做全局注意力+残差回传原序列」的技巧，大幅降低全局注意力算力成本

  - 窗口注意力模块复用固定序列化规则，可减少多轮序列化的额外开销，适配低延迟推理的业务需求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
点云Transformer现有方案存在明显权衡：窗口注意力计算成本低，但跨窗口信息传递效率差；全局注意力能捕捉全场景关联，但Token量大时算力开销极高，难以平衡推理延迟与模型效果。
### 方法关键点
1. 采用交错式注意力调度策略，固定一次Token空间序列化后，重复执行「2次窗口注意力+1次全局注意力」的循环单元，无需跨轮调整窗口划分；
2. 针对大Token量场景，先对Token做空间池化再执行全局注意力，将计算得到的残差更新回传至原始分辨率流，进一步降低全局注意力算力开销。
### 关键结果
在室内、室外点云基准数据集上精度与SOTA基线持平，推理延迟显著低于主流窗口、全局注意力基线；可通过重复交错注意力单元直接加深模型深度，效果稳定提升。
