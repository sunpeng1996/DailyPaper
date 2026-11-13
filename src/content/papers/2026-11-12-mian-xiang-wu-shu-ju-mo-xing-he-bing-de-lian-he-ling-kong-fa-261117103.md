---
title: Joint Null-Space Projection for Data-Free Model Merging
title_zh: 面向无数据模型合并的联合零空间投影方法
authors:
- Tian Xia
affiliations:
- Tohoku University
arxiv_id: '2611.17103'
url: https://arxiv.org/abs/2611.17103
pdf_url: https://arxiv.org/pdf/2611.17103
published: '2026-11-12'
collected: '2026-11-13'
category: Training
direction: 多任务专家模型无数据合并优化
tags:
- Model Merging
- Data-free
- Task Vector
- SVD
- Multi-task Learning
one_liner: 提出无数据无梯度的JNSP合并方法，解决多任务专家合并的向量干扰问题，精度显著优于现有基线
practical_value: '- 多场景LLM4Rec/广告大模型的多任务专家合并可复用JNSP思路，无需额外标注数据就能降低点击率、转化率、好评率等不同任务的向量干扰，提升合并后模型的多任务表现

  - JNSP纯闭式计算、无需前向传播的特性，适合工程端快速合并多场景微调的LoRA权重，减少多模型部署的资源开销

  - 合并时优先保留各任务特征更新专属子空间、剔除交叉重叠分量的思路，可迁移到多目标排序模型的参数融合场景'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有无数据多任务专家模型合并方法逐参数操作，忽略任务更新的低秩子空间特性，不同任务向量干扰严重，合并后精度损失大。
### 方法关键点
将合并问题转化为子空间干扰问题，对每个二维权重张量，取各任务delta的top-r右奇异子空间（任务表征更新最显著的输入方向），剔除每个任务向量中落在其他任务子空间并集的分量；JNSP为闭式解、无顺序依赖、无需前向传播，仅依赖输入checkpoint集合。
### 关键结果
8个CLIP图像分类任务上，合并ViT-B/16专家平均准确率达89.45%，比SOTA无数据基线TIES-Merging高11.88个点，比Task Arithmetic高14.22个点，优于带数据的WUDI合并0.98个点；不同ViT骨干下均稳定优于基线9~12个点；RoBERTa-large场景下效果劣于普通任务算术
