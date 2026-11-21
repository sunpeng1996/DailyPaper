---
title: Language-Oriented Semantic Modeling for Target Language Extraction
title_zh: 面向目标语言提取的语言导向语义建模方法
authors:
- Mehmet Sinan Yıldırım
- Ke Zhang
- Shuai Wang
- Haizhou Li
affiliations:
- National University of Singapore
- The Chinese University of Hong Kong, Shenzhen
- Nanjing University
arxiv_id: '2611.26317'
url: https://arxiv.org/abs/2611.26317
pdf_url: https://arxiv.org/pdf/2611.26317
published: '2026-11-19'
collected: '2026-11-21'
category: Other
direction: 跨语言语音处理 · 目标语言提取
tags:
- Semantic Modeling
- Prompt Adaptation
- Multilingual Speech Processing
- Parameter-Efficient Fine-Tuning
- Speech Separation
one_liner: 通过语言感知Prompt与参数高效微调，为目标语言提取提供超越ID标签的细粒度语义引导，最高获1.16dB SI-SDR增益
practical_value: '- 可复用「将粗粒度类别标签替换为细粒度语义表征做引导」的思路，优化现有推荐中仅用用户/物品标签召回排序的粗粒度方案

  - 语言感知Prompt+参数高效微调的预训练模型适配方法，可用于垂域大模型轻量调优，降低落地成本

  - 核心方案属于语音信号处理领域，其余部分和电商/推荐业务适配性有限'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
目标语言提取（TLE）任务现有方案依赖带语言ID标签的声学建模，仅能提供粗粒度分类引导，提取效果存在明显瓶颈。

### 方法关键点
提出语言导向语义建模框架，在传统声学提取能力基础上融入特定语言的语义表征：通过语言感知Prompt条件调控+参数高效微调适配预训练语音语义模型，从多语言混合语音中生成聚焦目标语言的语义表征，提取声学层面的高层语义结构，为提取模型提供超越ID标签的结构化语义指导。

### 关键结果
在CommonVoiceMix数据集上，相比纯声学基线方案效果持续提升，最高实现1.16dB的SI-SDR增益。
