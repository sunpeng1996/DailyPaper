---
title: 'Hide and Seek: HIDE Concepts to SEEK explanations for black box models'
title_zh: Hide and Seek：通过隐藏概念实现黑盒模型的可解释归因
authors:
- Bhanu Tokas
- Rahul Nair
- Rockwell Jackson
- Hannah Kerner
affiliations:
- Arizona State University
arxiv_id: '2610.13935'
url: https://arxiv.org/abs/2610.13935
pdf_url: https://arxiv.org/pdf/2610.13935
published: '2026-10-09'
collected: '2026-10-13'
category: Other
direction: 黑盒视觉模型 · 概念级归因方法
tags:
- Model Interpretability
- Black-box Model
- Concept Attribution
- Vision-Language Model
- Mask Intervention
one_liner: 提出无需权重与概念标注数据集的黑盒视觉模型概念级归因方法，覆盖多类视觉任务
practical_value: '- 电商多模态推荐场景可复用HnS的掩码对比逻辑，分析黑盒排序模型对商品图特定视觉概念（如logo、模特、促销标签）的依赖度，优化选品与素材规则

  - 无需访问模型权重的归因思路可直接复用，针对部署在第三方的黑盒推荐/广告模型，用「VLM对齐概念+区域掩码+输出差计算」流程做归因分析，无需申请模型权限

  - 多模态概念匹配思路可迁移到推荐归因的语义对齐环节，用通用VLM替代人工标注的概念数据集，大幅降低归因工具的标注成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有基于概念的黑盒模型归因方法仅支持分类、回归任务，需访问模型权重或大量概念标注数据集，且大多无法提供图像级局部归因，难以适配图像生成、分割等复杂视觉任务。
### 方法关键点
提出HnS轻量归因框架，核心流程：1）用通用VLM检索与指定概念对齐的图像集；2）定位每张图像中概念对应区域并做掩码；3）对比黑盒模型在原图与掩码图的输出差异计算概念归因得分，无需访问模型权重或预标注概念数据集，支持单图像级局部归因。
### 关键结果
在CelebA、COCO-Stuff数据集上验证，归因结果与ground truth一致性优于现有SOTA方法，可适配图像描述生成、卫星图像分割等现有归因方法无法支持的任务。
