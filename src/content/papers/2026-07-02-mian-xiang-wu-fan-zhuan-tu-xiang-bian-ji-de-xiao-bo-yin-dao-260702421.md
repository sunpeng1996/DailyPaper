---
title: Wavelet-Guided Semantic Signal Compensation for Inversion-Free Image Editing
title_zh: 面向无反转图像编辑的小波引导语义信号补偿方法
authors:
- Anqi Tang
- Wenhao Sun
- Zhaoqiang Liu
arxiv_id: '2607.02421'
url: https://arxiv.org/abs/2607.02421
pdf_url: https://arxiv.org/pdf/2607.02421
published: '2026-07-02'
collected: '2026-07-04'
category: Multimodal
direction: 多模态 · 文本引导无反转图像编辑
tags:
- Text-guided Image Editing
- Inversion-free Editing
- Wavelet Transform
- Semantic Compensation
- Rectified Flow
one_liner: 针对无反转图像编辑全局属性修改能力弱问题，提出小波引导频域语义补偿策略，兼顾编辑效果与背景保真
practical_value: '- 电商商品主图、营销海报批量修图场景可直接复用该方法，修改商品全局属性（如颜色、风格）时无需重绘背景，大幅降低人工修图成本

  - 频域分治的信号增强思路可迁移至多模态生成式推荐场景，生成商品展示素材时强化主体语义信号同时保留场景结构一致性

  - 无反转编辑的轻量优化逻辑可降低AI作图的计算开销，适合C端实时商品图生成、个性化营销素材生成类需求落地'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有无反转图像编辑框架（如FlowEdit）在全局属性偏移类编辑需求下表现不佳：早期生成步骤中编辑轨迹难以脱离源数据分布，高噪声阶段流向数据流形的主导流会大幅削弱文本条件引导信号的影响，最终导致全局修改效果有限、背景结构保存效果不达预期。
### 方法关键点
提出无需反转的频域感知语义补偿策略，基于小波分解在生成早期阶段针对性增强文本引导的有效语义信号，同时在全生成流程中约束背景结构保持一致性，无需额外的语义反转步骤。
### 关键结果
无需牺牲背景保真度即可显著提升全局属性编辑能力，效果优于主流无反转图像编辑方案，无额外推理 overhead。
