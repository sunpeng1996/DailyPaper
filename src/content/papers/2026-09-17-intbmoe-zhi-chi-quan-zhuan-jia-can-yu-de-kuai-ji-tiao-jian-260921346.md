---
title: 'IntBMoE: Integrating Block-Level Conditioning into Expert Composition for
  Full-Participation Mixture-of-Experts'
title_zh: IntBMoE：支持全专家参与的块级条件混合专家架构
authors:
- Ran Cheng
- Longfei Xu
- Zheng Liu
- Kaikui Liu
- Xiangxiang Chu
affiliations:
- Alibaba Group
- AMap
arxiv_id: '2609.21346'
url: https://arxiv.org/abs/2609.21346
pdf_url: https://arxiv.org/pdf/2609.21346
published: '2026-09-17'
collected: '2026-09-21'
category: GenRec
direction: 生成式推荐 · MoE架构优化
tags:
- MoE
- Generative Recommendation
- HyperNetwork
- Sparse Routing
- Inference Optimization
one_liner: 解耦MoE专家参与度、执行开销、存储开销三大指标，落地高德推荐获2.4%相对UVCTR提升
practical_value: '- 架构设计可直接复用：采用「预构建全专家融合可复用块 + 块级稀疏路由」的思路，既保证全专家池知识参与计算不损失效果，又通过缓存块参数将请求时延与专家池规模完全解耦，适配延迟敏感的电商/广告/POI推荐场景

  - 工程落地可快速迁移：直接替换现有Transformer架构中的FFN层为开源的IntBMoE模块，默认选K=8个候选块、Top-2路由，在增加少量固定存储开销的前提下即可获得效果提升

  - 落地效果可参考：高德POI推荐场景亿级流量下，预缓存块参数后平均时延19ms、P99 38ms，远低于60ms预算，拿到2.4%的相对UVCTR提升，验证了工业级可用性'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有MoE架构存在不可调和的三角矛盾：稀疏路由仅激活少量专家，限制参与度导致效果上限低；稠密输出混合需计算所有专家，执行开销随专家数线性增长；参数合并法针对每个输入动态合并专家，运行时参数量无界膨胀，无法同时满足工业级推荐场景的效果、时延、存储要求。

### 方法关键点
- 解耦块构建与token执行：基于小规模学习到的codebook，用轻量超网络提前将每层所有专家基合并为固定数量的可复用组合块，保证全专家池参与每个块的构建
- 稀疏块路由：每个token仅路由到Top-k个块执行，计算开销稳定不随专家数增长
- 双路径残差门控（DPRG）：每个块独立构建价值、门控两个路径，通过乘法门控引入非线性，不扩大专家池即可提升表达能力
- 推理缓存：组合块与输入无关，可提前预计算缓存，彻底消除请求时的专家合并开销

### 关键实验结果
- ImageNet-1K图像分类：Top-1准确率73.76%，领先SOTA MoE基线SMEAR 1.98个百分点
- MiniPile语言建模：PPL 14.59，相对最强基线降低2.9%
- IntTravel序列推荐：HR@1 0.6852、NDCG@5 0.7850，优于所有对比基线
- 高德POI生成式推荐线上A/B：服务亿级用户，平均时延19ms、P99 38ms，相对UVCTR提升2.4%

### 核心结论
预构建固定数量的全专家融合块+稀疏块路由的设计，可在不增加推理时延的前提下让每个token享受全专家池的知识增益，完全适配工业级C端推荐场景的部署要求
