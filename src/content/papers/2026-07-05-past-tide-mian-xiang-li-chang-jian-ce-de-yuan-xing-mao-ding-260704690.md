---
title: 'PAST-TIDE: Prototype-Anchored Statement Tuning with Topic-Invariant Normalization
  for Stance Detection'
title_zh: PAST-TIDE：面向立场检测的原型锚定陈述调优与主题不变归一化
authors:
- Md. Shakhoyat Rahman Shujon
- MD Jahid Hasan Jim
- Md. Milon Islam
- Md Rezwanul Haque
- Fakhri Karray
affiliations:
- Khulna University of Engineering & Technology
- University of Waterloo
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2607.04690'
url: https://arxiv.org/abs/2607.04690
pdf_url: https://arxiv.org/pdf/2607.04690
published: '2026-07-05'
collected: '2026-07-11'
category: LLM
direction: 低资源NLP · 立场检测微调
tags:
- stance_detection
- prompt_tuning
- contrastive_learning
- low_resource_NLP
- cross_topic_generalization
one_liner: 提出融合原型对比学习、主题条件归一化的低资源跨语言立场检测方案PAST-TIDE
practical_value: '- 电商评论立场分类、用户反馈情感识别等低资源分类任务，可复用cloze式MLM+verbalizer方案替代随机初始化分类头，降低标注量需求

  - 跨类目/跨topic的文本分类场景（如不同品类商品的评论极性识别），可引入主题条件层归一化提升跨域泛化性能

  - 小batch训练场景下的对比学习任务，可采用可学习类原型替代样本级对比，消除batch size对训练效果的约束'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有立场检测方法大多针对高资源英语场景设计，低资源跨语言、跨主题场景下泛化表现不佳，prompt类方法在这类场景的有效性尚未得到充分验证。
### 方法关键点
1. 将立场检测重定义为cloze式MLM任务，通过verbalizer把标签词映射到立场类别，无需额外新增随机初始化分类头，适配低资源场景；
2. 引入原型锚定对比学习，采用可学习类原型实现与batch size无关的对比训练，降低训练资源要求；
3. 新增主题条件层归一化模块，提升跨主题场景下的模型泛化能力。
### 关键结果
在StanceNakba共享任务官方排行榜上，子任务A（英语actor级立场分类）macro-F1达0.75，子任务B（阿拉伯语跨主题立场分类）macro-F1达0.74，仅对预训练模型做极少量架构修改即可在低资源场景下达到有竞争力的效果。
