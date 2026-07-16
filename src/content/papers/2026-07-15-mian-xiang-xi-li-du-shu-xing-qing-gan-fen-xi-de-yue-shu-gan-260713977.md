---
title: Constraint-Aware Counterfactual Editing for Aspect-Based Sentiment Analysis
title_zh: 面向细粒度属性情感分析的约束感知反事实编辑框架
authors:
- S M Rafiuddin
- Vamsi Krishna Pavuluri
- Atriya Sen
affiliations:
- Department of Computer Science, Oklahoma State University
arxiv_id: '2607.13977'
url: https://arxiv.org/abs/2607.13977
pdf_url: https://arxiv.org/pdf/2607.13977
published: '2026-07-15'
collected: '2026-07-16'
category: Eval
direction: 细粒度情感分析 · 反事实样本生成
tags:
- ABSA
- Counterfactual Editing
- Data Augmentation
- Robustness Evaluation
- Semantic Verification
one_liner: 约束感知验证编辑框架CAVE-ABSA，可生成符合多维度约束的属性级情感分析反事实样本
practical_value: '- 电商商品评论ABSA场景可复用多约束过滤逻辑，生成仅改变目标属性情感的反事实样本，扩充训练数据提升模型鲁棒性

  - 推荐系统评论情感特征模块做鲁棒性评估时，可套用「生成-验证分离」架构，测试模型是否依赖属性级情感推理而非全局极性捷径

  - Agent处理用户多属性反馈场景下，可借鉴意见跨度定位+最小化编辑思路做反事实用户偏好模拟，提升偏好理解准确率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
Aspect-Based Sentiment Analysis (ABSA)需识别特定属性的情感而非全局极性，现有反事实生成方法多聚焦句子级标签翻转，易产生属性无效、语义漂移、自相矛盾的样本，无法支撑属性级情感模型的鲁棒性评估与数据增强。

### 方法关键点
约束感知验证编辑框架CAVE-ABSA采用生成与验证分离架构：1）定位目标属性对应的意见跨度，做可控反事实改写；2）通过修复模块优化候选样本；3）用属性级验证、语义相似度、AMR引导结构保留、编辑最小化、流畅度、矛盾检测6个维度过滤样本。

### 效果
可生成仅翻转目标属性情感、保留其余非目标属性情感、语义/结构/事实一致性均达标的反事实样本，可用于ABSA数据集构建、模型鲁棒性测试，验证模型是否真正基于属性级情感推理。
