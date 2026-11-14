---
title: 'The RenAIssance: Caption-Guided Diffusion Models for Historical-Art Visual
  Media'
title_zh: RenAIssance：描述引导扩散模型的历史艺术视觉媒体生成
authors:
- Zhanyu Tuo
affiliations:
- Sorbonne University
arxiv_id: '2611.10599'
url: https://arxiv.org/abs/2611.10599
pdf_url: https://arxiv.org/pdf/2611.10599
published: '2026-11-07'
collected: '2026-11-14'
category: Multimodal
direction: 多模态生成 · 垂类LoRA适配
tags:
- Diffusion Model
- LoRA
- Text-to-Image
- BLIP
- Caption Generation
one_liner: 通过自动标注历史艺术品构建图文对训练SD LoRA适配器，实现可控历史艺术风格图像生成
practical_value: '- 电商商品图风格化生成场景可复用该流程：用现有资产自动打标签生成图文对，仅训练轻量LoRA即可完成专属风格适配，无需全量微调大模型

  - 缺少标注的垂类视觉内容生成任务可先通过BLIP等caption模型自动构建图文训练集，大幅降低数据标注成本

  - 个性化推荐的虚拟试穿、场景化商品展示等场景可借鉴「基础大模型+垂类LoRA」架构，兼顾通用能力与垂类风格一致性'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有文生图模型适配历史艺术等垂类风格时，普遍缺少成对图文标注数据，无法直接微调，限制垂类视觉生成落地。
### 方法关键点
1. 搭建可扩展pipeline，用BLIP为DEArt数据集的历史艺术作品生成场景级caption，构建约1.5万条图文对；
2. 基于标注数据训练Stable Diffusion v1.5的轻量LoRA适配器，解耦基础模型通用生成能力与垂类风格表示。
### 关键结果
所有不同长度的历史、当代Prompt测试场景下，生成图像相对DEArt参考分布的FID均有提升，仅CLIP图文相似度有轻微下降；单个LoRA可同时生成符合时代特征的内容、用历史风格渲染当代概念。
