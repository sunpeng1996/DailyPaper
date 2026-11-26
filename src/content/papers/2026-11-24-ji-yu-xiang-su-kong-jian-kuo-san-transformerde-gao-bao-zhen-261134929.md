---
title: High-Fidelity Image Matting with Pixel-Space Diffusion Transformers
title_zh: 基于像素空间扩散Transformer的高保真图像抠图
authors:
- Baihan Yang
- Xin Lin
- Yufan Wei
- Baiang Li
- Yuheng Liu
- Juanxi Tian
- Xiaohui Xie
- Truong Nguyen
affiliations:
- University of California, San Diego
- Princeton University
- University of California, Irvine
- Nanyang Technological University
arxiv_id: '2611.34929'
url: https://arxiv.org/abs/2611.34929
pdf_url: https://arxiv.org/pdf/2611.34929
published: '2026-11-24'
collected: '2026-11-26'
category: Multimodal
direction: 多模态 · 高保真图像抠图扩散模型优化
tags:
- Diffusion Transformer
- Image Matting
- Pixel-Space Diffusion
- Generative Model
- High-Fidelity Generation
one_liner: 复用预训练像素空间扩散Transformer，无需额外条件编码器实现高保真单步图像抠图
practical_value: '- 电商商品素材生产场景（商品图抠图、背景替换、主图制作）可直接复用PixelMatte框架，大幅降低人工修图成本

  - 适配预训练大模型到下游高精度视觉任务时，可复用主干原生patch embedding做多输入空间对齐，无需新增条件编码器降低工程复杂度

  - 对边界、高频细节敏感的生成任务，可参考LayerShift+High-Pass Refiner的轻量校准方案，以极小参数量代价提升输出精度'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有基于潜空间扩散的抠图方案依赖VAE重建，压缩表征会损失高频细节，无法满足抠图所需的边缘精度、区域透明度精度要求。
### 方法关键点
提出PixelMatte框架，直接适配预训练像素空间扩散Transformer：复用主干原生patch embedding联合对齐处理输入图像、trimap、带噪alpha matte，无需额外条件编码器或适配器；加入LayerShift和High-Pass Refiner两个轻量校准模块，分别优化区域透明度精度和边界保真度；结合像素级合成监督+真实图像微调，可单步前向输出alpha matte。
### 关键结果数字
在4个基准测试集上显著优于现有方案，相比RenderMatte在P3M-500-NP和AM-2K数据集上SAD和梯度误差降低24%-44%，在AIM-500、RenderMatte-2K上性能持平SOTA。
