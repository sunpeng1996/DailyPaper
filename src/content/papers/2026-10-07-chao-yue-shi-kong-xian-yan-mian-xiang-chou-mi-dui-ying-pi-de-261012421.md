---
title: 'Beyond Spatio-Temporal Priors: A Generalizable Approach for Dense Correspondence
  Matching'
title_zh: 超越时空先验：面向稠密对应匹配的可泛化方法
authors:
- Luping Liu
- Bingyi Kang
- Yifan Wang
- Dong Xu
affiliations:
- The University of Hong Kong
- ByteDance Seed
- Zhejiang University
arxiv_id: '2610.12421'
url: https://arxiv.org/abs/2610.12421
pdf_url: https://arxiv.org/pdf/2610.12421
published: '2026-10-07'
collected: '2026-10-09'
category: Other
direction: 稠密对应匹配 · 生成内容保ID评价
tags:
- DenseMatching
- ImageEditing
- GenerativeEvaluation
- FoundationRepresentation
- WeakSupervision
one_liner: 提出无稠密标注的FreeMatching框架，适配保身份变换场景的稠密匹配需求
practical_value: '- 电商商品图AI编辑/风格迁移场景，可复用其保ID匹配逻辑作为自动评价指标，替代部分人工评测

  - 异源多数据集混合监督+教师引导迭代蒸馏的训练范式，可迁移到小样本跨域生成类任务训练

  - 无需稠密标注的弱监督训练思路，可降低生成式内容质检类模型的标注成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统稠密对应匹配依赖平滑运动、刚性几何等时空先验，在图像编辑、参考引导生成（IEG）场景下失效——这类场景的变换保留视觉身份但打破物理连续性，传统方法易出现匹配遗漏、失真。
### 方法关键点
1. 提出FreeMatching通用框架，融合生成式与语义基础模型表征，采用经典数据集、跟踪视频、合成场景的异源监督训练；
2. 引入教师引导迭代优化策略，无需稠密对应标注即可提升IEG场景匹配效果。
### 关键结果
单模型在高难度IEG图像对的匹配质量大幅提升，同时在经典基准上保持竞争力；其作为保身份定量评价指标的得分与人类判断高度相关。
