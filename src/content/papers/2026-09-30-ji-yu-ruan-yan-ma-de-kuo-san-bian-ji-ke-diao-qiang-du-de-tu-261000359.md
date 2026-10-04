---
title: 'Diffusion Editing with Soft Mask: Pixel Level Redo of Image and Video with
  Adjustable Strength'
title_zh: 基于软掩码的扩散编辑：可调强度的图像视频像素级重绘
authors:
- Candi Zheng
- Yuan Lan
affiliations:
- 香港科技大学数学系
- 独立研究者
arxiv_id: '2610.00359'
url: https://arxiv.org/abs/2610.00359
pdf_url: https://arxiv.org/pdf/2610.00359
published: '2026-09-30'
collected: '2026-10-04'
category: Multimodal
direction: 多模态生成 · 扩散模型软掩码可控编辑
tags:
- Diffusion Model
- Soft Mask
- Image Editing
- Video Editing
- Zero-shot Sampling
one_liner: 提出零样本采样方法SoftPaint，实现免训练可调强度的图像视频像素级扩散编辑
practical_value: '- 电商商品图/营销短视频素材生产场景，可复用该方法实现局部内容微调（如改模特穿搭、背景、促销标签），软掩码控制编辑强度可避免边缘违和，无需重拍大幅降本

  - 生成式推荐场景的个性化商品图生成需求，可直接集成该梯度免、低内存的采样方案，适配现有扩散backbone无需额外训练，降低部署门槛

  - 多模态Agent自动生成营销素材链路中，可接入该方法实现像素级精准编辑，仅修改指定区域同时保留其他内容一致性，提升素材生成准确率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有prompt、参考图引导的扩散编辑方法控制颗粒度较粗，支持空间可变编辑强度的软掩码方案要么需昂贵的像素级标注训练，要么零样本方案编辑效果不佳，无法满足像素级精准可控的图像视频编辑需求。
### 方法关键点
零样本采样方法SoftPaint基于朗之万迭代设计采样器，严格遵循每像素软掩码对应的编辑强度权重，无需梯度计算、无需额外训练适配，可直接泛化到图像、视频两类扩散模型backbone。
### 关键结果
内存效率优于同类零样本编辑方法，可实现从完全保留原内容到完全重绘掩码区域的连续可调编辑，在多类图像、视频扩散backbone上均实现平滑无违和的像素级编辑效果。
