---
title: 'Real In, Real Out: What If We Only Use Real Data for Scene Text Editing?'
title_zh: 真进真出：仅使用真实数据实现场景文本编辑的探索
authors:
- Xingsong Ye
- Yongkun Du
- Jiaxin Zhang
- Chong Sun
- Zhineng Chen
affiliations:
- Institute of Trustworthy Embodied AI, Fudan University
- Shanghai Key Laboratory of Multimodal Embodied AI
- WeChat Vision, Tencent Inc.
arxiv_id: '2610.27592'
url: https://arxiv.org/abs/2610.27592
pdf_url: https://arxiv.org/pdf/2610.27592
published: '2026-10-19'
collected: '2026-10-23'
category: Multimodal
direction: 多模态 · 场景文本编辑自监督数据构造
tags:
- Scene Text Editing
- Diffusion Model
- Self-supervised Learning
- Data Construction
- Text Recognition
one_liner: 通过构造真实样本自配对监督训练条件扩散STE模型，大幅缓解合成到真实的域偏移
practical_value: '- 电商商品图/广告素材的文字修改（价格、促销文案替换）场景，可复用该自配对数据构造方法，无需依赖合成配对数据，避免生成文字出现伪影、违和感

  - 商品图文字识别、广告素材合规校验等OCR下游任务，可复用Shuffle&Crop扰动策略做数据增强，扩充真实场景训练集提升识别准确率

  - 基于条件扩散做风格保留的内容编辑任务时，优先采用该自监督训练范式，降低对人工标注配对数据的依赖'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有场景文本编辑（STE）高度依赖合成配对数据与复杂解耦策略，难以拟合自然场景的多样性，易生成伪影、幻觉，合成到真实的域偏移问题突出。
### 方法关键点
1. 提出单真实样本自构造配对监督的训练范式，探索裁剪、字符打乱、掩码等多种原始图像扰动方式构造训练数据；
2. 基于条件扩散架构搭建基线模型TextRIRO，验证Shuffle&Crop（字符列打乱+图像裁剪）组合可在破坏文本语义的同时保留完整风格特征，支持模型直接从真实文本图像学习编辑能力；
3. 基于TextRIRO构造3M规模的真实长文本识别数据集TextRIRO-3M。
### 关键结果
在真实场景STE基准上，TextRIRO的编辑准确率、视觉真实度表现优异，域偏移问题大幅缓解；使用TextRIRO-3M训练的文本识别模型准确率提升显著。
