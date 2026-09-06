---
title: 'Catalogue Photography as a Cold Start: Toward Deployable Carbide Burr Recognition'
title_zh: 以目录摄影为冷启动源的可部署硬质合金旋转锉识别方法
authors:
- Abilash Philip Madavath
- Chandra Yuvesh Aubeeluck
- Augustin Raju
- Nicolas Pyschny
- Felix Hackelöer
- Florian Zwanzig
affiliations:
- TH Köln – University of Applied Sciences, Cologne, Germany
arxiv_id: '2609.03995'
url: https://arxiv.org/abs/2609.03995
pdf_url: https://arxiv.org/pdf/2609.03995
published: '2026-09-03'
collected: '2026-09-06'
category: Other
direction: 工业视觉 · 跨域冷启动识别
tags:
- domain_shift
- metric_learning
- cold_start
- industrial_CV
- fine-grained_recognition
one_liner: 利用厂商目录摄影作为冷启动监督源，给出工业视觉跨域识别的优化方案与评估基线
practical_value: '- 冷启动场景下可复用公开物料（如电商商品白底图、详情页图）作为唯一监督源，替代高成本人工标注

  - 跨域迁移优化优先尝试低成本降域敏感度操作（如图像风格统一、转灰度），性价比远高于盲目提升模型规模

  - 检索/匹配类任务可结合已知业务约束（如电商订单SKU范围、推荐候选池限制）通过匈牙利匹配做召回约束，快速提效'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
工业精密刀具出厂质检依赖人工核验批次与订单一致性，错误率高达20%-30%，自动化CV识别无标注训练数据，仅厂商目录摄影可作为监督源，存在目录图与生产现场实拍图的强域偏移问题。
### 方法关键点
对比不同特征提取、表示学习方案的跨域迁移效果，重点验证低成本降域敏感度操作、业务约束嵌入的收益，建立目录到现场的迁移评估协议。
### 关键结果
- 冻结预训练特征提取器无法有效区分刀具头部形状、齿廓两个核心属性，度量学习可在目录图上实现无监督聚类ARI 0.94~0.97，但跨域到现场图后收益不足50%
- 跨域增益核心来自低复杂度操作：图片转灰度提效+0.22，结合已知订单约束做匈牙利匹配检索约束提效+0.11，模型规模/表征复杂度无明显增益
