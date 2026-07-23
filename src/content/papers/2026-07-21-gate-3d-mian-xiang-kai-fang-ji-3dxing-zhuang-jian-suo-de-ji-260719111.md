---
title: 'GATE-3D: Geometry-Aware Test-time Adaptive Reranking for Open-Set 3D Shape
  Retrieval'
title_zh: GATE-3D：面向开放集3D形状检索的几何感知测试时自适应重排序
authors:
- Hao Wu
- Heyi Lin
- Zilin Wang
- Huizai Yao
- Hao Wang
- Hui Xiong
affiliations:
- Hong Kong University of Science and Technology
- Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2607.19111'
url: https://arxiv.org/abs/2607.19111
pdf_url: https://arxiv.org/pdf/2607.19111
published: '2026-07-21'
collected: '2026-07-23'
category: RecSys
direction: 3D内容检索 · 跨模态自适应重排序
tags:
- 3D Retrieval
- Reranking
- Cross-modal Fusion
- Test-time Adaptation
- Geometry-aware Feature
one_liner: 无需重训检索backbone，基于跨模态分歧动态融合多特征实现3D检索重排序增益
practical_value: '- 多模态召回/重排场景可借鉴「跨模态分歧特征判断是否融合」的思路，避免强制融合带来的负向收益，可落地到图文商品检索、短视频内容检索等场景

  - 测试时自适应优化无需重训 backbone，适合业务上快速迭代试错，降低大模型微调成本

  - 低数据量下的路由模块优先用线性层而非MLP，减少参数同时提升泛化性，适配小样本冷启动场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
预训练视觉模型主导的3D形状检索易混淆外观相似但几何差异大的样本，直接强制融合几何与外观特征在模态对齐较好时反而损伤检索效果。

### 方法关键点
- 轻量query自适应重排序方案GATE-3D，无需重训原有检索backbone
- 基于跨模态分歧特征预测几何特征得分的调整权重，仅在模态分歧大时引入几何特征修正排序，避免强制融合的负向影响
- 低数据场景下路由模块优先采用线性层而非小MLP，特征设计比模型容量更关键

### 关键结果
主基准上mAP@10比仅用外观的检索方案提升2.00个百分点（p=0.041），几何相关假阳率降低10.8%，留一类别泛化性、零-shot性能均优于常启融合基线
