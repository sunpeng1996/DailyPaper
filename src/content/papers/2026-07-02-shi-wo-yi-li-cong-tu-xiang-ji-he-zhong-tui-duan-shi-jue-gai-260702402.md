---
title: 'Show Me Examples: Inferring Visual Concepts from Image Sets'
title_zh: 示我以例：从图像集合中推断视觉概念
authors:
- Nick Stracke
- Kolja Bauer
- Stefan Andreas Baumann
- Miguel Angel Bautista
- Josh Susskind
- Björn Ommer
affiliations:
- CompVis @ LMU
- Munich Center for Machine Learning
- Apple
arxiv_id: '2607.02402'
url: https://arxiv.org/abs/2607.02402
pdf_url: https://arxiv.org/pdf/2607.02402
published: '2026-07-02'
collected: '2026-07-04'
category: Multimodal
direction: 多模态视觉语言模型 · 视觉概念推理
tags:
- VLM
- Visual Reasoning
- Concept Inference
- Multimodal
- Generative Model
one_liner: 提出VICIS视觉概念推断任务与配套训练架构，解决现有VLM无法从图像集提取共享概念并迁移到新输入的缺陷
practical_value: '- 电商素材生成场景可复用该架构：给定一组同风格/同系列商品图，提取视觉概念后批量生成符合该概念的新商品营销图、种草图，大幅降低素材制作成本

  - 推荐系统用户建模可借鉴概念提取思路：从用户历史点击的多张商品图中提取共享视觉偏好（如极简风、多巴胺配色），补充用户画像的多模态维度，提升召回排序准确率

  - 多模态导购Agent可参考该训练框架：支持Agent从商家提供的多张示例图中隐式学习商品风格规则，无需人工标注文本描述，降低多模态Agent落地成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有VLM仅能跟随复杂文本指令，无法从纯视觉上下文完成推理，尤其无法从多示例图像集中提取共享概念并迁移应用到新输入，SOTA VLM在该类任务上表现极差，常忽略视觉上下文或生成有偏结果。

### 方法关键点
1. 定义VICIS（Visual Concept Inference from Sets）任务：给定共享同一概念的小批量上下文图像集+查询图像，要求输出同时保留上下文定义概念、与查询一致的新图像；
2. 推出配套训练框架与架构，支持从图像集推断视觉概念，并从查询中提取概念专属embedding。

### 关键结果
在合成数据、大规模ImageNet/WordNet数据集上验证，生成结果准确率、多样性均优于现有SOTA，可泛化到未见过的概念及草图等其他模态。
