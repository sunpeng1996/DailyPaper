---
title: 'UGG: Unified Generative Geometry Model'
title_zh: UGG：统一生成式几何模型
authors:
- Amani Kiruga
- Zhiyi Li
- Ruojin Cai
- Hansen Lillemark
- Xiaoshan Wu
- Ayush Tewari
- Yilun Du
affiliations:
- Harvard University
- MIT
- UC San Diego
- University of Cambridge
arxiv_id: '2611.14440'
url: https://arxiv.org/abs/2611.14440
pdf_url: https://arxiv.org/pdf/2611.14440
published: '2026-11-10'
collected: '2026-11-12'
category: Other
direction: 4D场景理解 · 跨模态统一生成
tags:
- Generative Model
- 4D Scene Understanding
- Multimodal Learning
- Geometry Prediction
- Video Generation
one_liner: 提出统一生成式框架，同时实现4D场景几何预测与视觉生成任务
practical_value: '- 常规电商/搜推业务可直接借鉴点有限，核心为计算机视觉领域4D场景理解的学术贡献

  - 跨任务统一建模思路可复用：对不同任务/模态分配差异化噪声权重，将多任务转化为统一条件补全问题，降低多任务对齐成本

  - 异构数据集训练策略可迁移：针对标注不全的多源业务数据，可采用该框架灵活适配不同标注子集的数据集，降低标注成本

  - 推理阶段无标注优化思路可参考：对于缺乏标注的线上场景，可基于观测业务信号动态筛选多候选结果，提升预测精度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有4D场景理解方法割裂为几何预测前馈模型、视觉生成模型两类，难以适配异构标注数据集，且稀疏观测下预测精度不足。
### 方法关键点
1. 提出统一生成框架UGG，同时建模RGB视频、深度、相机位姿等多模态表征；
2. 对跨模态、跨时间维度分配不同噪声水平，将视觉生成与几何预测统一为单模型内的条件补全任务，可适配异构标注数据集训练；
3. 支持推理阶段基于观测RGB帧提取的几何证据，搜索多个合理场景假设优化预测结果，无需几何标注。
### 关键结果
在相机可控视频生成、深度估计、相机位姿预测三类任务上效果全面优于非统一基线，稀疏观测场景下优势更显著。
