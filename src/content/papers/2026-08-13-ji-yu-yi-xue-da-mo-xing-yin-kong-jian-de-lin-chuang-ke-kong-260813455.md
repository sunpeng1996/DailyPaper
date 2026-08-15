---
title: Evaluation of Clinically Steerable Retinal Image Generation from Foundation
  Model Latent Spaces
title_zh: 基于医学大模型隐空间的临床可控视网膜图像生成评估
authors:
- Zuzanna A. Wakefield-Skórniewska
- Bartłomiej W. Papież
affiliations:
- Big Data Institute, Nuffield Department of Population Health, University of Oxford,
  UK
arxiv_id: '2608.13455'
url: https://arxiv.org/abs/2608.13455
pdf_url: https://arxiv.org/pdf/2608.13455
published: '2026-08-13'
collected: '2026-08-15'
category: Other
direction: 医疗多模态·可控图像生成与大模型评估
tags:
- Foundation Model
- Diffusion Model
- Controllable Generation
- Medical Imaging
- Representation Learning
one_liner: 评估4种视网膜大模型可控生成能力，揭示合成-真实数据间未被定义的表征Gap
practical_value: '- 可控生成任务的评估可复用「同源模型内评估+跨域真实数据模型评估」的双维度框架，避免单方面高估生成内容的下游可用性

  - 基于大模型隐空间做属性可控生成时，属性保留度显著优于普通扩散模型，可复用该思路实现电商商品素材、广告文案的定向属性编辑

  - 生成式任务落地时需额外增加合成-真实表征对齐步骤，否则生成内容在真实场景下游任务的泛化性会大幅下降'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
医学大模型隐空间已被证明编码了大量有临床价值的表型信息，但基于其隐空间实现可控图像生成的能力尚未被系统验证，合成数据的属性保留度、下游任务适配性缺乏量化评估。
### 方法关键点
在表征分词器框架下对4种视网膜大模型开展可控生成评估，对比生成过程中隐空间编码的人口统计、临床特征的保留程度，同时引入传统隐扩散模型作为基线，分别采用「同源大模型内评估」「真实图像训练的第三方分类器评估」两种范式验证生成效果。
### 关键结果
- 同源大模型内评估时，生成的表征与图像可完整继承原始表型信息，下游预测任务表现显著优于传统隐扩散模型
- 采用真实图像训练的分类器评估时，上述性能优势基本消失，验证了此前未被发现的合成-真实表征Gap的存在
