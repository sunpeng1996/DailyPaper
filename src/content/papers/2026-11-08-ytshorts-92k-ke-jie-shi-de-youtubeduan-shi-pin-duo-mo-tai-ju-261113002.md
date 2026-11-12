---
title: 'YTShorts-92K: An Interpretable Multimodal Dataset of YouTube Shorts'
title_zh: YTShorts-92K：可解释的YouTube短视频多模态数据集
authors:
- Celian Charrin
- Sidonie Abuzakuk
- Artúr Vlaszov
- Nándor Birher
- Roland Molontay
affiliations:
- Grenoble INP - ENSE3
- Grenoble INP - Phelma
- Department of Stochastics, Institute of Mathematics, Budapest University of Technology
  and Economics
- Institute of Biostatistics and Network Science, Semmelweis University
- Pázmány Péter Catholic University
arxiv_id: '2611.13002'
url: https://arxiv.org/abs/2611.13002
pdf_url: https://arxiv.org/pdf/2611.13002
published: '2026-11-08'
collected: '2026-11-12'
category: Multimodal
direction: 多模态数据集 · 短视频内容理解
tags:
- Multimodal Dataset
- Short-form Video
- Interpretable Feature
- Content Analysis
- YouTube Shorts
one_liner: 发布含9.2万条YouTube Shorts的可解释多模态数据集，配套全流程特征提取pipeline
practical_value: '- 可复用其多模态特征提取pipeline，覆盖元数据、文本、视觉、跨模态一致性4类可解释特征，适配短视频内容理解场景

  - 其12类人工标注的短视频分类体系，可直接参考用于内容平台的短视频类目体系搭建

  - 可基于该数据集训练短视频热度预测模型，优化短视频推荐、广告投放的内容选品策略'
score: 6
source: arxiv-cs.MM
depth: abstract
---

## 动机
当前短视频已成为主流线上内容形态，但现有相关数据集多仅包含发布后热度信号，或依赖不可解释的高维embedding，缺乏支撑内容成功要素分析的大规模可解释多模态数据集。
## 方法关键点
发布YTShorts-92K数据集，包含从345个创作者采集的92654条YouTube Shorts，覆盖12个人工定义内容类目；每条样本配套可解释多模态特征集，涵盖元数据、文本信息、帧/封面视觉特征、跨模态一致性度量；完整公开数据采集、清洗、特征提取全流程。
## 关键结果数字
数据集覆盖12个内容类目、345位创作者、92654条短视频，特征维度覆盖4大类可解释多模态信号，可直接用于短视频内容分析、用户注意力研究、多模态算法训练等场景。
