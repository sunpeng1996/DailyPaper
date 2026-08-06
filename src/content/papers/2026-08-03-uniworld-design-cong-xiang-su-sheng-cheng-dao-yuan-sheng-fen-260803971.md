---
title: 'UniWorld-Design: From Pixel Generation to Layer-Native Design'
title_zh: UniWorld-Design：从像素生成到原生分层设计框架
authors:
- Zongjian Li
- Zhiyuan Yan
- Chenxu Bai
- Chen Chen
- Haoxiang Sun
- Shaodong Wang
- Feize Wu
- Shenghai Yuan
- Bin Lin
- Zheyuan Liu
affiliations:
- Peking University
- RabbitpreAI
arxiv_id: '2608.03971'
url: https://arxiv.org/abs/2608.03971
pdf_url: https://arxiv.org/pdf/2608.03971
published: '2026-08-03'
collected: '2026-08-06'
category: Multimodal
direction: 多模态生成 · 原生分层视觉设计
tags:
- Multimodal Generation
- RGBA Layer
- Text-to-Image
- Instruction Tuning
- Design Automation
one_liner: 提出以语义RGBA分层为原子单元的多模态生成框架，支持文本生成透明素材、指令驱动图像分层编辑
practical_value: '- 电商商品图/营销海报自动化生产场景可复用T2RGBA能力，直接生成带透明通道的素材元素，省去后期抠图成本

  - 营销素材智能编辑Agent可接入I2L的指令化分层接口，支持用户自然语言指令拆分海报、提取指定元素、修改局部图层

  - 个性化商品推荐的素材生成环节可基于分层能力灵活拼接不同元素，快速生成千人千面的营销物料，降低AIGC素材的重复生成开销'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有文生图模型仅输出扁平化像素结果，无法对齐设计师分层创作逻辑，后续编辑、元素复用成本极高，难以支撑Agent化的智能设计场景。
### 方法关键点
1. 提出以语义RGBA分层为生成、理解、编辑的原子单元，对齐人类设计师的分层创作范式
2. 框架包含两个核心模型：T2RGBA直接从文本生成独立的带透明通道素材；I2L支持输入成品图+全局指令+分层prompt，输出有序的完整语义RGBA层，支持顶层分解、递归分解、定向提取三类指令操作
3. 分层学习完整语义对象而非可见像素分区，生成的图层可独立移动、删除复用
### 关键结果
- Crello基准上，I2L对比Qwen-Image-Layered，层间RGB L1误差降低37%，Alpha Soft IoU相对提升34%
- T2RGBA的CLIP Score优于LayerDiffuse、OmniAlpha，达到当前SOTA
