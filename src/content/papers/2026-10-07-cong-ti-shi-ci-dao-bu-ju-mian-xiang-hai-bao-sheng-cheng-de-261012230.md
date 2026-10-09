---
title: 'From Prompting to Composing: A Spatial Canvas Interface for Poster Generation'
title_zh: 从提示词到布局：面向海报生成的空间画布交互框架
authors:
- Yitong Wang
- Fangyun Wei
- Jinjing Zhao
- Sirui Zhang
- Hongyang Zhang
- Dong Chen
- Bo Dai
- Yan Lu
affiliations:
- Fudan University
- Microsoft Research
- The University of Sydney
- USTC
- University of Waterloo
arxiv_id: '2610.12230'
url: https://arxiv.org/abs/2610.12230
pdf_url: https://arxiv.org/pdf/2610.12230
published: '2026-10-07'
collected: '2026-10-09'
category: Multimodal
direction: 多模态可控生成 · 空间画布交互
tags:
- Controllable Generation
- Spatial Canvas
- Text-to-Image
- Multimodal Generation
- Human-AI Interaction
one_liner: 提出支持四类空间绑定的画布交互框架及适配模型Compo，大幅提升海报生成的布局可控性
practical_value: '- 电商活动海报、商品banner生成场景可直接复用四类绑定逻辑，将商品图、价格文案、营销slogan、背景分别绑定到指定空间区域，解决现有文生图布局乱、文字错的通病

  - 可复用「高层需求→结构化空间画布→多约束生成」的Agent链路，无需从零训练专属海报模型，仅需微调预训练文生图模型的输入理解模块即可快速落地

  - 可借鉴其自动标注pipeline，批量生成带空间绑定标注的训练数据，大幅降低可控生成场景的标注成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有文生图模型依赖一维文本prompt生成二维海报，用户需要将空间布局、元素属性、文字内容等多层意图压缩为自然语言，生成结果可控性差，无法满足电商、营销等场景的精准海报生成需求。
### 方法关键点
1. 空间画布交互框架支持语义、身份、文本、像素四类绑定，配合单元素细节描述与全局样式规范，可直接在二维空间结构化定义生成意图
2. 基于预训练图像编辑模型适配得到Compo，同时支持手动构造画布的直接推理模式，以及自动将高层用户需求转成结构化空间画布的Agent模式
3. 设计可扩展的自动监督数据生成pipeline，无需从零训练专属海报生成模型，仅需少量适配即可完成训练
### 关键结果
实验显示，Compo在自建的多绑定合规性benchmark上，布局约束满足率显著优于通用文生图模型与专用海报生成系统，同时视觉质量保持同等水平
