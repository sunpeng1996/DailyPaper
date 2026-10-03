---
title: 'GeoLatent: Geometry-Guided Latent Structuring with Routed Optimization for
  3D Reasoning'
title_zh: GeoLatent：面向3D推理的几何引导潜变量结构化与路由优化方法
authors:
- Yakun Zhu
- Yi Bin
- Yujuan Ding
- Zheng Wang
- Pengpeng Zeng
- Duo Peng
- Jingkuan Song
- Heng Tao Shen
affiliations:
- Tongji University
- The Hong Kong Polytechnic University
arxiv_id: '2610.02091'
url: https://arxiv.org/abs/2610.02091
pdf_url: https://arxiv.org/pdf/2610.02091
published: '2026-10-01'
collected: '2026-10-03'
category: Reasoning
direction: 多模态3D空间推理 · 潜变量结构化
tags:
- 3D Reasoning
- Vision-Language Model
- Latent Representation
- Routed Optimization
- Geometry Alignment
one_liner: 提出融合CR-GEO对齐与路由优化的GeoLatent框架，提升多模态模型3D空间推理性能
practical_value: '- 潜变量拆分+路由优化思路可迁移至多模态推荐的多属性表征学习，避免表征坍缩到单一维度

  - 公共-残差对齐范式可复用在跨域推荐特征对齐场景，分离通用特征与场景特有特征

  - 训练阶段临时引导信息流通过瓶颈层的技巧可优化小样本推荐任务的表征泛化能力'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有多模态模型2D转3D空间推理能力不足：离散token描述几何信息会损失连续空间关系精度，单一连续潜变量无法拆分多维度空间线索，拆分后的几何表征仍存在坍缩、潜变量利用率低的问题。

### 方法关键点
1. 提出CR-GEO模块，拆分几何表征为教师模型共享通用部分与残差特有部分，避免表征坍缩
2. 设计路由优化策略，联合训练几何与语言分支，训练阶段临时引导视觉问答信息流通过潜变量瓶颈层，后续恢复全注意力保留几何监督

### 关键结果
- CR-GEO将几何表征有效秩从1.00提升至3.87
- 阻塞潜变量读出口会使方向推理准确率从89.1%降至25.8%
- GeoLatent在SPAR-Bench达73.0%、SPBench达72.1%，均优于现有SOTA
