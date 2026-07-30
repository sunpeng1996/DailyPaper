---
title: Evidence Attribution in Visual Document Understanding without Coordinates or
  Region Labels
title_zh: 无需坐标或区域标签的视觉文档理解证据归因方法
authors:
- Zhuchenyang Liu
- Yao Zhang
- Yu Xiao
affiliations:
- Aalto University
arxiv_id: '2607.24651'
url: https://arxiv.org/abs/2607.24651
pdf_url: https://arxiv.org/pdf/2607.24651
published: '2026-07-26'
collected: '2026-07-30'
category: Multimodal
direction: 多模态文档理解 · 证据归因优化
tags:
- Visual Document Understanding
- Evidence Attribution
- Attribution Hallucination
- GRPO
- Vision-Language Model
one_liner: 提出用语言接口替代坐标输出做文档证据归因，结合GRPO无区域标注训练，大幅降低归因幻觉
practical_value: '- 电商商品详情页/广告素材信息抽取场景，可放弃坐标输出方案，改用「原文引用+布局解析器匹配」pipeline，提升证据召回率、降低幻觉

  - 无区域标注的多模态任务训练时，可复用GRPO奖励策略，用金标答案+检索区域切片作为奖励信号，省去昂贵的区域标注成本

  - Agent做文档问答/商品信息溯源场景，可直接复用该引用-检索架构，保证回答可溯源的同时不降低问答质量'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有视觉文档理解的证据归因依赖坐标输出接口，VLM即使回答正确也常出现归因幻觉，且区域级标注成本极高。

### 方法关键点
对比坐标接口与纯文本语言接口，后者让VLM直接逐字引用证据，再通过多模态检索+布局解析器定位引用区域，表格/图通过caption引用；进一步将引用-检索pipeline作为训练支架，提出GRPO训练策略，奖励为裁判模型对金标答案与检索区域切片的匹配打分，无需任何区域标签。

### 关键结果
在双语CiteVQA子集上测试6个开源VLM，证据召回率从最高8%提升至26-47%，幻觉率减半，回答质量无明显变化；8B backbone的严格归因准确率从22.4提升至33.8。
