---
title: Evaluating VLMs on Multimodal Aristotelian Persuasion Tasks
title_zh: 多模态亚里士多德说服任务下的视觉语言模型评估
authors:
- Khondoker Ittehadul Islam
affiliations:
- Saarland University
- Department of Language Science & Technology
arxiv_id: '2608.01238'
url: https://arxiv.org/abs/2608.01238
pdf_url: https://arxiv.org/pdf/2608.01238
published: '2026-08-02'
collected: '2026-08-06'
category: Eval
direction: 多模态大模型 · 说服任务评估
tags:
- VLM
- Multimodal
- Evaluation
- Persuasion Detection
- Qwen
- Argument Mining
one_liner: 在亚里士多德三类说服要素多模态检测任务上评估多款VLM，给出Qwen系列模型的性能对比结果
practical_value: '- 电商广告素材说服力评估可复用Logos（逻辑）、Ethos（可信度）、Pathos（情感）三要素拆解框架，量化素材投放效果的影响因子

  - 多模态广告/内容召回排序场景，可参考评估结论优先选择Qwen3作为Logos、Pathos类内容理解的底座VLM，Qwen2作为可信度类内容识别底座

  - 内容营销Agent的文案/配图生成效果核验环节，可引入本次开源的三要素检测代码，提升生成素材的转化效率'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有VLM在通用多模态任务上表现优异，但在涉及主观偏差、复杂语义的说服类高价值任务上缺乏系统性评估，难以支撑营销、广告等落地场景的多模态内容理解选型。
### 方法关键点
基于公开ImageArg数据集，针对亚里士多德说服三要素（Logos逻辑、Ethos可信度、Pathos情感）设计三类检测任务，对主流VLM进行横向对比测评，相关代码已开源可复用。
### 关键结果
Qwen家族模型整体F1得分领先，其中Qwen3在Logos、Pathos检测任务上表现最优，Qwen2在复杂度更高的Ethos检测任务上具备竞争性表现。
