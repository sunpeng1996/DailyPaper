---
title: Advancing Relevance Measurement with Vision-Language Models for Web-Scale Search
title_zh: 基于视觉语言模型的大规模网页搜索相关性评估优化
authors:
- Han Wang
- Alex Whitworth
- Pak Ming Cheung
- Zhenjie Zhang
- Krishna Kamath
- Xi Chen
- Roberto Konow
- Kurchi Subhra Hazra
affiliations:
- Pinterest
arxiv_id: '2608.02446'
url: https://arxiv.org/abs/2608.02446
pdf_url: https://arxiv.org/pdf/2608.02446
published: '2026-08-03'
collected: '2026-08-04'
category: RecSys
direction: 搜索推荐 · 多模态相关性评估
tags:
- VLM
- Relevance Evaluation
- A-B Testing
- Multimodal
- Search Ranking
one_liner: Pinterest落地VLM驱动的搜索相关性自动标注流水线，降本同时大幅提升A/B实验灵敏度
practical_value: '- 图文/短视频类电商/内容平台的相关性标注可直接复用「开源多模态VLM+80万级人工标注微调」的方案，单卡A100可2小时标注10万级样本，相比人工标注成本降99.98%、周转时间提升20倍。

  - A/B实验相关性度量可采用按查询兴趣/热度分层采样方案，替代简单随机采样，无需依赖CUPED的预处理数据即可降低67%的指标方差，MDE最高下降6倍。

  - 多语言场景可直接复用英文微调的多语言VLM做相关性标注，配对实验的系统偏差几乎为0，不需要额外标注多语言训练数据。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统搜索相关性评估依赖人工标注，成本高、周期长，无法支撑大规模A/B实验快速迭代；同时用户行为指标（点击、收藏等）受位置、展示样式干扰，无法完全反映语义相关性，亟需低成本、高一致性的自动标注方案作为实验 guardrail。

### 方法关键点
- 微调开源Qwen3-VL模型，输入为查询文本、内容的多模态特征（图片+标题/描述/落地页信息/所属板块标题/历史高互动查询），输出1-5级相关性标签，训练用80万人工标注对，验证集2万对。
- 采用按查询兴趣、热度分层的采样方案，替代简单随机采样，消除层间方差降低指标波动；A/B评估采用配对采样查询组，用sDCG@25作为相关性指标，通过配对差消除VLM标注的系统偏差。

### 关键结果
4B参数VLM与人工标注的exact match率达82.9%，94.2%的标签差不超过1级，sDCG平均误差低于0.03，对齐度接近人工内部标注一致性；对比人工标注，VLM标注周转时间从2天降至2小时（降96%），单条标注成本降99.98%，支撑的评估任务量提升4倍；分层采样+大样本方案将A/B实验MDE从1.3%-1.5%降至0.25%以下，灵敏度提升6倍；仅用英文数据微调的模型在法、德、巴西市场的配对差误差几乎为0，可直接复用。

### 核心结论
VLM自动相关性标注不仅是降本工具，更能通过扩大样本量、优化采样设计大幅提升A/B实验灵敏度，加快搜索推荐迭代效率。
