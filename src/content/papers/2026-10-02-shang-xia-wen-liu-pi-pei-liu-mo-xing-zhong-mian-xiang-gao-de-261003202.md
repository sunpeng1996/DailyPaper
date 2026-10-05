---
title: 'Contextual Flow Matching: Adaptive Step Selection in Flow Models for Efficient
  Visual Generation'
title_zh: 上下文流匹配：流模型中面向高效视觉生成的自适应步长选择
authors:
- Divya Jyoti Bajpai
- Arun Verma
- Manjesh Kumar Hanawal
affiliations:
- IIT Bombay
- SMART Centre
arxiv_id: '2610.03202'
url: https://arxiv.org/abs/2610.03202
pdf_url: https://arxiv.org/pdf/2610.03202
published: '2026-10-02'
collected: '2026-10-05'
category: Multimodal
direction: 多模态生成 · 推理加速优化
tags:
- Flow Matching
- Visual Generation
- Inference Acceleration
- Adaptive Step Selection
- Plug-and-Play
one_liner: 提出即插即用的COFLOW推理方法，基于prompt特征自适应选生成步长，实现视觉生成2.5x以上提速且保质量
practical_value: '- 自适应推理步长的思路可迁移到电商AIGC素材生成场景，根据prompt复杂度动态分配计算资源，平衡主图/短视频的生成效率与质量

  - 即插即用、无需重训基底模型的优化思路可复用，针对已部署的生成式模型做推理加速时，可单独训练轻量的上下文感知调度模块，避免全量重训成本

  - 平衡效率与效果的无监督奖励函数设计思路，可迁移到推荐系统动态计算资源调度场景，为高价值请求分配更多计算资源以提升效果'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
Flow Matching（FM）基于连续时间动力学实现高质量视觉生成，但推理需多次串行函数评估，延迟高；现有加速方案普遍存在额外训练开销、生成质量下降、未考虑输入特性差异等问题。
### 方法关键点
1. 提出COFLOW推理端自适应方案，基于prompt特征为每个生成任务动态选择推理步长
2. 采用无监督奖励在线训练，平衡推理效率与生成保真度
3. 即插即用架构，无需重训底层生成模型，可泛化到图像、视频生成场景
### 关键结果
- 实现2.5倍以上推理提速，同时完全保留感知与语义质量
- 理论证明常规正则条件下前向欧拉离散误差界为O(1/K)
