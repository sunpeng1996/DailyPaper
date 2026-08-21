---
title: Training-Free LLM-Based Recommendation with Post-LLM Item Refinement Using
  Collaborative Signals
title_zh: 引入协同信号的后LLM物品优化免训练推荐框架
authors:
- Kyungho Kim
- Sunwoo Kim
- Geon Lee
- Shinhwan Kang
- Sojeong Kim
- Liam Collins
- Bhuvesh Kumar
- Donald Loveland
- Kijung Shin
affiliations:
- KAIST
- Snap Inc.
arxiv_id: '2608.19665'
url: https://arxiv.org/abs/2608.19665
pdf_url: https://arxiv.org/pdf/2608.19665
published: '2026-08-20'
collected: '2026-08-21'
category: GenRec
direction: 生成式推荐 · 免训练LLM4Rec
tags:
- Training-free Rec
- LLM4Rec
- Collaborative Filtering
- Embedding Refinement
- Post-LLM
one_liner: 免训练后LLM范式推荐框架CoRRe，用协同信号优化物品嵌入，性能超现有免训练方案媲美训练型模型
practical_value: '- 可复用后LLM注入协同信号的范式，避免pre-LLM RAG/重排的效果天花板，无需微调LLM即可引入业务共访、共购等协同数据，落地成本低

  - 物品嵌入优化的两个trick可直接复用：1）基于共购图的方向传播，权重λ可按业务域调优；2）基于物品热度的模长校准，α可根据业务对热门品的容忍度调整

  - 冷启动场景可直接参考该框架，无需积累大量用户交互训练推荐模型，仅需物品文本语义+轻量协同统计即可生成效果可观的推荐结果'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有免训练LLM推荐方案多采用pre-LLM范式注入协同信号，要么用CF做候选召回后再让LLM重排，要么通过RAG把协同相关信息塞进prompt，前者依赖初始候选集质量，后者协同信号利用不充分，导致LLM生成的用户兴趣语义过泛，无法做细粒度物品区分，推荐效果提升有限。

### 方法关键点
- 核心采用后LLM范式：先用LLM根据用户交互历史生成用户偏好profile，用同一个文本编码器把profile编码为用户嵌入，物品初始嵌入由物品标题编码得到
- 方向优化：构建物品共购图，对语义嵌入做图传播，再和原始语义嵌入加权融合后归一化，λ控制两者权重，让共购关系强的物品嵌入更接近
- 模长优化：按物品热度调整优化后嵌入的模长，α控制热度校准强度，热度越高模长越大，利用内积排序时自然引入热度先验
- 最终用用户嵌入和优化后的物品嵌入做内积匹配得到top-K推荐，全程无需任何模型训练或微调

### 关键实验
在Amazon Reviews的Sports、Toys、Beauty三个域数据集上测试，对比12个基线（包含LightGCN、SASRec等训练型推荐，以及ItemRAG、Coral等免训练方案），CoRRe在所有12个评测指标（H@10/20、NDCG@10/20跨三个域）上均优于免训练基线，最高提升132.43%，同时在8/12个指标上超过训练型基线。

### 核心结论
把协同信号注入LLM生成的物品表征而非LLM输入，是免训练LLM推荐突破效果瓶颈的低成本可行路径。
