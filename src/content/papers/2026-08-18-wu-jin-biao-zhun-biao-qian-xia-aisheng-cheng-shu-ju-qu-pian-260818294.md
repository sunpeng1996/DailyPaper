---
title: 'Debiased Inference for AI-Generated Data without Gold-Standard Labels: Identification
  via Multiple Imperfect Measurements'
title_zh: 无金标准标签下AI生成数据去偏推断：多误差测量识别方法
authors:
- Naoki Egami
- Sooahn Shin
affiliations:
- Massachusetts Institute of Technology
arxiv_id: '2608.18294'
url: https://arxiv.org/abs/2608.18294
pdf_url: https://arxiv.org/pdf/2608.18294
published: '2026-08-18'
collected: '2026-08-20'
category: Other
direction: 无金标数据去偏 · 多源测量融合
tags:
- Debiasing
- Weak Supervision
- Data Annotation
- Statistical Inference
- No Gold Label
one_liner: 无需金标准标签，融合多个带误差的AI测量结果实现下游任务无偏推断
practical_value: '- 电商场景下做LLM批量标注用户评论情感、商品属性时，无需采购昂贵人工金标，融合多个不同LLM的标注结果用DMM框架去偏，可大幅降低标注成本

  - 推荐系统离线效果评估缺少真实用户反馈金标时，可融合点击、停留、加购等多个弱监督信号用DMM做无偏推断，显著提升评估结果置信度

  - 可直接复用DMM配套的条件独立性诊断工具，验证多源弱标注信号的可用性，提前规避标注偏置导致的下游模型效果衰减'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
当前AI生成/标注的数据直接用于下游分析时，即使测量准确率超过90%，忽略预测误差也会导致严重偏置、置信区间失效；现有去偏方案均依赖金标准标签，获取成本高，部分业务场景难以获得。
### 方法关键点
提出DMM（多误差测量去偏推断）框架，基于CP decomposition理论，假设多个带误差的AI测量在隐式真实标签和观测单元特征（如文本embedding）下条件独立，支持不同标注方法、不同标注单元的错分率存在差异，结合半参数推断理论构造一致且渐近正态的估计器，同时配套条件独立性假设的诊断工具。
### 关键结果
仿真实验验证DMM可实现有效推断，新增哪怕仍存在误差的高准确率测量源，即可进一步提升估计效率。
