---
title: 'Theia: Large-Scale Multimodal Captioning and Automated Validation of the Incidents1M
  Dataset for Data-Free Distillation'
title_zh: Theia：面向无数据蒸馏的Incidents1M数据集大规模多模态标注与自动验证
authors:
- Simone Giano
- Lorenzo Severini
- Alessandro Galdelli
- Adriano Mancini
affiliations:
- Università Politecnica delle Marche, Italy
arxiv_id: '2607.28269'
url: https://arxiv.org/abs/2607.28269
pdf_url: https://arxiv.org/pdf/2607.28269
published: '2026-07-30'
collected: '2026-08-01'
category: Multimodal
direction: 多模态数据集构建 · LLM自动校验
tags:
- Multimodal
- LLM-as-a-Judge
- MoE
- Knowledge Distillation
- Dataset Construction
one_liner: 提出无数据蒸馏专用多模态数据集构建框架，用图像盲LLM-as-a-Judge保障标注质量
practical_value: '- 电商多模态商品标注可复用「双模型生成+图像盲LLM校验」流程，低成本生成高精准商品图文描述，降低人工标注成本与噪声

  - 多模态小模型蒸馏场景可借鉴图像盲校验思路，模拟模态gap适配学生模型能力边界，提升无数据蒸馏的知识迁移准确率

  - 多模态召回/推荐的标注质量校验可参考高Precision低Recall的保守生成策略，最小化假阳性标注对排序效果的负向影响'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
灾害管理等关键领域VLM落地需高质量多模态数据集支撑无数据知识蒸馏（DFKD），现有领域数据集要么缺失描述文本，要么存在严重的图文语义对齐问题。
### 方法关键点
1. 基于纯图像数据集Incidents1M恢复10万张图像，分别用Qwen3.5-4B dense、Qwen3.5-35B MoE两个架构生成高保真文本描述
2. 提出图像盲LLM-as-a-Judge校验流水线，故意向校验模型隐藏原始图像，模拟无数据蒸馏时学生模型的模态gap，保障生成标注适配蒸馏需求
### 关键结果
173179组标签对验证两个生成架构的语义一致性达78.65/100；自动评估显示标注策略精度77.6%、召回46.0%，高精准低召回的保守生成模式最小化假阳性噪声，同时暴露原始人工标注的不一致问题。
