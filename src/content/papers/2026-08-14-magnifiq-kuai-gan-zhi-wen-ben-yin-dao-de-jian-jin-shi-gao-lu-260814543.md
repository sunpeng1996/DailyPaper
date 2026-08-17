---
title: 'MagnifiQ: Patch-aware Text Guided Progressive Upscaling for High-Resolution
  Image Restoration'
title_zh: MagnifiQ：块感知文本引导的渐进式高分辨率图像修复框架
authors:
- Mahesh Reddy
- Yashesh Savani
- Antoine Mercier
- Hong Cai
- Fatih Porikli
- Guillaume Berger
affiliations:
- Qualcomm AI Research
arxiv_id: '2608.14543'
url: https://arxiv.org/abs/2608.14543
pdf_url: https://arxiv.org/pdf/2608.14543
published: '2026-08-14'
collected: '2026-08-17'
category: Multimodal
direction: 多模态图像修复 · 渐进式超分效率优化
tags:
- Diffusion Model
- Image Restoration
- Super Resolution
- SDXL
- Efficient Inference
one_liner: 基于SDXL改造的块感知渐进式4K图像修复框架，兼顾推理效率与生成画质
practical_value: '- 电商商品图/直播画面4K超分场景可复用渐进式分阶段升采样思路，避免直接生成高分辨率图出现的纹理错乱、内容漂移问题，降低算力消耗

  - 复用预训练文生图扩散模型做下游视觉任务时，可尝试用卷积替换原模型自注意力层的优化方案，实现计算量随分辨率线性增长，大幅提升高分辨率推理效率

  - 对图像分区域(patch)生成/修复场景，可引入块级专属文本提示做局部语义引导，在保留全局一致性的同时提升局部细节还原度，适配电商商品细节图生成需求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有扩散模型直接做4K分辨率图像修复计算成本极高，易出现纹理重复、不一致问题，同时难以兼顾全局结构一致性与局部细粒度细节还原。
### 方法关键点
1. 基于预训练SDXL改造，将原U-Net中的自注意力层替换为卷积运算，计算成本随分辨率线性增长，提升高分辨率推理扩展性；
2. 采用渐进式升采样策略，多分辨率阶段迭代修复、逐步优化中间输出，而非直接生成4K结果，减少伪影提升全局一致性；
3. 引入块专属文本提示，提供空间局部语义引导，增强局部细节的同时控制内容漂移。
### 关键结果
在合成与真实退化图像数据集上，感知质量、人类偏好均优于此前扩散式修复方法，可支持最高32倍缩放、生成4096×4096清晰连贯结果，可通过可扩展backbone实现灵活的速度-质量权衡。
