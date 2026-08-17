---
title: 'RankT2I: A Submodular Framework for Discovering Interpretable and Diverse
  Semantics in Text-to-Image Models'
title_zh: RankT2I：面向文本生成图像模型的可解释多样语义发现子模框架
authors:
- Ritika Allada
- Pinar Yanardag
affiliations:
- Virginia Tech
arxiv_id: '2608.14226'
url: https://arxiv.org/abs/2608.14226
pdf_url: https://arxiv.org/pdf/2608.14226
published: '2026-08-14'
collected: '2026-08-17'
category: Multimodal
direction: 多模态生成 · 可编辑语义挖掘
tags:
- Submodular Optimization
- Text-to-Image
- Semantic Discovery
- Model-Agnostic
- Multimodal
one_liner: 提出训练无关、模型无关的RankT2I框架，自动挖掘T2I模型的可编辑语义
practical_value: '- 电商商品图智能编辑场景可复用子模优化思路，自动筛选适配T2I模型的可编辑属性（如服饰颜色、图案），降低人工试错成本

  - 生成式营销物料生产链路可直接复用「候选语义召回→子模排序」的训练无关框架，快速适配不同T2I底座

  - 子模目标同时优化相关性、可执行性、多样性的思路，可迁移到生成式推荐候选集筛选、query推荐排序场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前T2I模型的可编辑语义依赖人工手动指定，需大量试错，效率极低，无法适配批量图像编辑等落地场景需求。
### 方法关键点
1. 框架训练无关、模型无关，可直接适配diffusion、FLUX等主流T2I底座；
2. 先基于多模态视觉语言模型召回指定视觉领域的全量候选语义池；
3. 将语义发现建模为集合选择问题，通过子模目标函数同时优化语义的相关性、可编辑性、多样性三个核心维度。
### 关键结果
跨服饰、家居等多个视觉领域的语义发现效果显著优于现有基线方法，可高效挖掘覆盖范围广的高质量可编辑语义
