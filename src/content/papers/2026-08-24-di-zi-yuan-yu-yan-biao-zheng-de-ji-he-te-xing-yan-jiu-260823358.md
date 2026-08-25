---
title: The Geometry of Low-Resource Language Representations
title_zh: 低资源语言表征的几何特性研究
authors:
- Francois Meyer
- Jan Buys
affiliations:
- University of Cape Town
arxiv_id: '2608.23358'
url: https://arxiv.org/abs/2608.23358
pdf_url: https://arxiv.org/pdf/2608.23358
published: '2026-08-24'
collected: '2026-08-25'
category: LLM
direction: 大语言模型 · 低资源语言适配优化
tags:
- Low-resource LLM
- Representational Geometry
- Continued Pre-training
- Regularization
- Cross-lingual LLM
one_liner: 从表征几何角度揭示低资源LLM性能差距成因，提出几何正则优化低资源语言持续预训练效果
practical_value: '- 跨境电商/小语种推荐场景做LLM适配时，可监测LLM最后层表征退化程度，快速判断小语种适配充分性

  - 小语种LLM持续预训练（CPT）阶段可引入余弦相似度正则项，抑制表征退化，提升小语种query理解、文案生成等任务性能

  - 低数据量垂域LLM微调（如小众品类推荐的prompt理解）可参考几何正则思路，降低对标注数据的依赖'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM在高低资源语言间性能差距显著，但导致差异的内部模型驱动因素尚不明确，缺乏针对性的低资源语言适配优化方案。
### 方法关键点
1. 分析30种语言的隐层表征几何特性，定位低资源语言在LLM最后层存在系统性的表征退化问题，且退化程度与语料数据量强相关
2. 在低资源语言持续预训练（CPT）阶段引入几何正则项惩罚表征退化，对比不同正则策略的适配效果
### 关键结果
- 9个基础LLM适配10种非洲语言的实验中，几何正则可有效降低CPT阶段的表征退化
- 大模型场景下，余弦相似度正则比原生CPT带来边际性能提升，在高难度任务上增益更稳定
