---
title: Action-Aligned Retrieval with Pairwise Multimodal Reranking for Text-Based
  Person Anomaly Search
title_zh: 面向文本驱动人员异常搜索的动作对齐检索与成对多模态重排
authors:
- Thanh-Khoi Nguyen
- Thanh-Nhan Vo
- Trong-Thuan Nguyen
- Minh-Triet Tran
affiliations:
- University of Science, VNU-HCM, Vietnam
- Vietnam National University, Ho Chi Minh City, Vietnam
arxiv_id: '2608.23503'
url: https://arxiv.org/abs/2608.23503
pdf_url: https://arxiv.org/pdf/2608.23503
published: '2026-08-24'
collected: '2026-08-25'
category: Multimodal
direction: 多模态检索 · 跨模态重排优化
tags:
- Multimodal-Retrieval
- Reranking
- VLM
- Action-Alignment
- Query-Rewriting
one_liner: 提出三阶段ActPair框架，融合动作对齐表征、双查询检索与成对重排，提升文本驱动人员异常搜索性能
practical_value: '- 跨模态检索场景可复用「原始query+LLM改写query」的并行晚融合检索策略，减少query改写的信息丢失，可直接迁移到电商图文搜、短视频搜场景

  - 重排阶段可借鉴pivot-promote成对比较算法，替代全量pointwise打分，在兼顾效果的同时降低推理成本，适合广告、商品搜推的多模态重排链路

  - VLM微调阶段可加入动作/属性对齐的多任务目标，强化表征对细粒度语义的编码能力，适配电商场景下按穿搭、使用场景等细粒度query检索商品的需求'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有文本驱动人员异常搜索方法难以捕获上下文依赖的细粒度行为特征，普遍存在query改写丢失原始细节、多模态校验依赖绝对pointwise打分精度不足等问题，无法有效区分外观相似但行为不同的个体。
### 方法关键点
1. 三阶段粗到精ActPair框架：首先微调VLM引入动作对齐多任务目标，强化表征对动作区分性语义的编码能力；
2. 并行执行原始query与LLM生成的上下文感知改写query的晚融合检索，保留双视角互补语义信息；
3. 基于pivot-promote算法的即插即用重排模块，直接完成成对视觉比较，消除空间与组合歧义，避免全量评估带来的过高推理成本。
### 关键结果
在Pedestrian Anomaly Behavior（PAB）公开测试集上效果优于所有对比方法，且可有效迁移到未见过的非异常专属数据集。
