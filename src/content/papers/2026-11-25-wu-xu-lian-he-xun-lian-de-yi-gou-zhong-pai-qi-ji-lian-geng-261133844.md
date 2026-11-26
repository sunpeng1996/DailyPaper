---
title: 'When Rerankers Work Together: Better and Faster Reranking without Joint Training'
title_zh: 无需联合训练的异构重排器级联：更高精度更快的RAG重排
authors:
- Yanqiao Chen
- Dongsheng Hou
- Yuhan Rui
affiliations:
- Southern University of Science and Technology
arxiv_id: '2611.33844'
url: https://arxiv.org/abs/2611.33844
pdf_url: https://arxiv.org/pdf/2611.33844
published: '2026-11-25'
collected: '2026-11-26'
category: RAG
direction: RAG多阶段重排 · 无联合训练级联
tags:
- Reranking
- RAG
- Multi-stage Pipeline
- Cacheable
- Semantic Matching
one_liner: 提出两款可缓存轻量语义粗排器，与现有精排无联合训练级联，同时提升精度与推理速度
practical_value: '- 电商搜索/推荐、广告的多阶段排序架构可直接复用这套无联合训练级联思路，新增轻量粗排时无需改动现有精排权重，即可同时提升效果、降低精排算力消耗

  - 可缓存语义粗排的特征构造方法可直接迁移到召回/粗排特征工程：拼接query与item的向量、元素积、差、余弦相似度，训练成本低，item向量可离线预存大幅降低在线计算延迟

  - RAG类智能客服、商品问答场景可直接落地Cache-Pointwise+RRF+ColBERTv2架构，实测相对单ColBERTv2提4.6个点答案准确率，同时加速1.36倍

  - 多阶段排序的效果评估可复用论文的stage-removal对比方法，单独衡量每个阶段的增益/损失，避免盲目新增排序阶导致负收益'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RAG系统的多阶段重排架构往往需要跨阶段联合训练才能适配，否则轻量粗排易损失有效证据、降低精度，单独使用高精度精排又存在算力消耗大、延迟高的问题。异构重排器的无训练组合效果尚未被系统研究，无法在不改动现有精排权重的前提下同时实现精度提升与降本提速。
### 方法关键点
- 提出两款轻量可缓存语义粗排器Cache-Pointwise、Cache-Shapley，复用冻结MiniLM编码器，item向量可离线预存，在线仅需编码query一次，推理复杂度为O(n)
- 粗排特征拼接query向量、item向量、两者元素积、差的绝对值、余弦相似度共1537维，经两层MLP映射输出单值相关性分数
- 两款粗排分别采用pointwise pairwise损失、基于Shapley值的边际贡献损失训练，无需与下游精排、Reader联合训练，可直接与现有精排级联
- 支持RRF（Reciprocal Rank Fusion）融合多阶段排序结果，进一步提升精度
### 关键结果
在NoLiMa 32K数据集上，Cache-Pointwise与CrossEncoder级联相对单CrossEncoder提升7.01个点QA精度、推理加速1.58倍；与Provence级联相对单Provence提升9.43个点精度、加速1.86倍；Cache-Pointwise搭配RRF与ColBERTv2级联，相对单ColBERTv2提升4.6个点精度、加速1.36倍。实验还发现级联可能优于最终精排但劣于单独粗排，增益受Reader类型、重排器配对、知识类型影响。
> 最值得记住的结论：无需联合训练的异构重排器级联可同时提升精度与速度，但每个阶段的价值完全取决于整体组合，不要盲目增加排序阶
