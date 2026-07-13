---
title: 'Simon-SR: Spatially Adaptive Modulation and Visual Prompt Adaptation for Text-Reinforced
  Super-Resolution'
title_zh: Simon-SR：面向文本增强超分辨率的空间自适应调制与视觉提示适配
authors:
- Haotong Cheng
- Yuxuan Li
- Zijie Cui
- Rongling Tan
- Chenyuan Wang
affiliations:
- College of Electronic Science and Engineering, Jilin University
arxiv_id: '2607.09351'
url: https://arxiv.org/abs/2607.09351
pdf_url: https://arxiv.org/pdf/2607.09351
published: '2026-07-10'
collected: '2026-07-13'
category: Other
direction: 多模态图像超分辨率·提示学习优化
tags:
- Super-Resolution
- Multimodal Fusion
- Prompt Learning
- Contrastive Learning
- Image Restoration
one_liner: 提出融合对比提示学习与空间自适应细化的多模态超分辨率框架Simon-SR，性能全面超越SOTA
practical_value: '- 电商主图/商品详情图低清转高清场景可复用文本引导+对比prompt学习方案，降低人工标注成本，提升超分图像的语义一致性

  - 提示引导的空间自适应细化模块可直接迁移到商品图修复/美化流程，重点强化商品核心特征（如logo、纹理）的超分精度

  - 将文本作为可优化的语义变量而非固定先验的思路，可复用至多模态内容生成的对齐模块，减少错误文本priors对生成效果的干扰'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多模态单图超分辨率（SISR）方法依赖固定文本先验，对错误先验敏感度高、标注成本高昂，且文本-图像融合时存在语义偏差，核心细节还原度不足，极端下采样倍率下输出过于平滑。

### 方法关键点
1. 提出Simon-SR多模态SISR框架，不将文本作为固定真值先验，而是作为可学习的隐式语义变量与图像重建任务联合优化
2. 结合对比提示学习实现高效语义挖掘，搭配提示引导的空间自适应细化模块，强化多模态语义对齐能力

### 关键结果
性能全面超越现有SOTA方法，PSNR最高提升0.50dB，SSIM最高提升0.0133，LPIPS最高提升0.0695，后续将开源代码
