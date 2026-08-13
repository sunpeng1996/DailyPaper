---
title: 'RA-ClipScore: Making Generative Model Evaluation More Interpretable'
title_zh: RA-ClipScore：提升生成模型评估的可解释性
authors:
- Yifan Lu
- Taras Kucherenko
- Hedvig Kjellström
- Judith Bütepage
affiliations:
- KTH Royal Institute of Technology
- National Library of Sweden
- Electronic Arts (EA)
arxiv_id: '2608.12088'
url: https://arxiv.org/abs/2608.12088
pdf_url: https://arxiv.org/pdf/2608.12088
published: '2026-08-12'
collected: '2026-08-13'
category: Eval
direction: 生成模型评估 · 可解释语义指标优化
tags:
- CLIP
- Generative Model Evaluation
- Interpretability
- Spatial Alignment
- Attribute Disentanglement
one_liner: 提出融合双prompt、局部patch特征的CLIP生成模型评估指标，支持属性解耦与空间偏差检测，更贴合人类感知
practical_value: '- 电商AI生成商品图、营销海报的效果评估可复用双prompt属性解耦思路，精准定位生成内容的属性错误、布局偏差，降低人工审核成本

  - 多模态生成式推荐的输出质量评测可引入局部patch语义匹配逻辑，提升生成内容与用户个性化需求匹配度的评估准确性

  - 生成模型的偏差排查场景可复用空间分布对齐检测方法，快速定位生成结果的布局、位置类系统性偏差'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有生成模型评估指标存在明显缺陷：FID仅输出全局标量，缺乏诊断信息；传统CLIP类语义指标受训练范式限制，无法做细粒度的属性拆分与空间维度分析，难以检测生成内容的布局偏差、属性混淆问题。
### 方法关键点
1. 设计双prompt机制解耦竞争属性，规避CLIP原生的属性混淆问题；2. 提取CLIP局部patch token捕捉细粒度区域语义，新增空间分布对齐度量，判断生成对象是否符合训练数据的位置先验；3. 输出区域单属性散度作为可解释诊断指标。
### 关键结果
在分布偏移、文本属性部分无关的场景下，鲁棒性显著优于现有CLIP类评估指标；用户评测证明其输出的区域单属性散度与人类视觉多样性感知的对齐度高于现有语义指标，可直接定位生成模型的空间偏见。
