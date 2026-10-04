---
title: 'ShieldCLIP: Selective Safety Alignment for Harmful Content Mitigation in Multimodal
  Foundation Models'
title_zh: ShieldCLIP：面向多模态基础模型有害内容过滤的选择性安全对齐框架
authors:
- Tobia Poppi
- Silvia Cappelletti
- Samuele Poppi
- Marcella Cornia
- Lorenzo Baraldi
- Diego Garcia-Olano
- Rita Cucchiara
affiliations:
- University of Modena and Reggio Emilia
- University of Pisa
- MBZUAI
- Meta Superintelligence Labs
arxiv_id: '2609.39688'
url: https://arxiv.org/abs/2609.39688
pdf_url: https://arxiv.org/pdf/2609.39688
published: '2026-09-30'
collected: '2026-10-04'
category: Multimodal
direction: 多模态基础模型 · 安全对齐
tags:
- CLIP
- Multimodal Alignment
- Safety Alignment
- Content Moderation
- Dataset
one_liner: 提出基于单模态独立安全标注的选择性对齐框架ShieldCLIP及195k规模多模态安全数据集ViSUv2
practical_value: '- 电商多模态内容审核、合规管控场景可复用分模态独立标注+选择性对齐思路，无需全量调整模型表征，可大幅降低正常内容的误判率

  - 生成式商品配图、AI营销文案生成场景可直接接入ShieldCLIP做前置安全校验，相比现有安全对齐CLIP，合规内容的检索/生成准确率损失更低

  - 可复用生成样本加单模态标注的训练数据构建方案，无需收集大量真实有害样本，降低合规训练数据的收集门槛'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
CLIP等多模态编码器是跨模态检索、文生图/图生文下游任务的基础组件，但web规模训练数据嵌入的有害关联会引发合规风险；现有安全对齐方案要么过度修改正常内容表征，要么依赖粗粒度的生成样本全量标注，误判率高。
### 方法关键点
1. 开源ViSUv2数据集，包含195k四元组样本，覆盖578个概念、28个分类，每个模态独立标注安全标签
2. 设计四元条件对齐目标：锚定安全内容表征、仅重定向不安全模态表征、混合安全-不安全对仅更新不安全分支、双模态均不安全时强制语义一致
### 关键结果
在跨模态检索、Stable Diffusion v1.4/SDXL文生图、LLaVA图生文任务上，有害输出率显著优于现有安全对齐基线，同时原embedding空间的效用几乎无损失
