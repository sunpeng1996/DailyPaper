---
title: Multi-State Linear Attention with Generalized Second-Order Routing
title_zh: 基于广义二阶路由的多状态线性注意力机制MERLIN
authors:
- Hee Seung Hwang
- Sanghyuk Chun
- Xindi Wu
- Olga Russakovsky
- Zhiwei Deng
affiliations:
- Princeton University
- Google DeepMind
arxiv_id: '2610.37645'
url: https://arxiv.org/abs/2610.37645
pdf_url: https://arxiv.org/pdf/2610.37645
published: '2026-10-27'
collected: '2026-10-28'
category: LLM
direction: 长上下文LLM · 线性注意力优化
tags:
- Linear-Attention
- Long-Context-LLM
- Multi-State-Attention
- Routing-Mechanism
- Efficient-Inference
one_liner: 引入键的一二阶矩设计路由权重，大幅提升多状态线性注意力的长上下文建模效果
practical_value: '- 电商RAG/长会话Agent场景可直接集成MERLIN优化多状态线性注意力的分段路由，仅增加不到13%的内存开销即可提升长上下文检索准确率8%以上，同时缓解近因偏置，提升历史埋点/商品信息的召回率

  - 推荐系统用户长序列建模可复用二阶矩聚合思路：计算用户兴趣query和历史行为序列的匹配度时，在均值匹配外加入方差项，可精准捕捉用户的低频强兴趣，避免平均池化淹没小众高意向行为信号

  - 端侧部署的轻量化LLM可通过设置小维度dr（32/64）集成该机制，仅增加不到5%的参数即可提升端侧长会话处理能力，几乎不影响推理延迟'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多状态线性注意力（MSLA）将长上下文切分为多个分段独立压缩存储，解决了标准自注意力的平方复杂度瓶颈，但现有分段聚合方法仅通过位置或键的一阶矩（均值）计算分段权重，忽略了查询与分段键匹配的方差信息，无法区分“整体弱匹配但存在少量强匹配键”的高价值分段，导致长上下文检索、推理性能受限，还存在明显的近因偏置。
### 方法关键点
- 设计MERLIN路由机制，为每个分段存储键的一阶（均值）、二阶（外积均值）矩，可快速计算查询与该分段键匹配的均值和方差
- 聚合权重由均值匹配分数、方差匹配分数分别做softmax后，通过学习到的动态门控加权混合得到，搭配可学习温度参数调整两类分数的尖锐度
- 用于计算矩的K/Q独立于主注意力的K/Q，可通过缩小矩维度dr控制额外开销，对原有模型的参数增量最高仅4.6%
### 关键实验
在Gated DeltaNet-1.3B、Mamba-2-780M两个骨干上验证，对比位置路由、均值路由等基线：16K上下文的RULER基准平均提升7.0%~8.3%，LongBench多任务平均提升12.0%~13.5%；256分段长度下，性能超过消耗4倍内存的基线模型，仅增加最高12.6%的内存开销。
### 核心结论
长上下文分段聚合仅用均值会丢失强匹配信号，引入二阶矩可以用极低的开销大幅提升检索精准度，同时缓解位置偏置
