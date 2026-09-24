---
title: Zero-Shot Object Removal via Attention Masking, Latent Anchoring, and Refinement
title_zh: 基于注意力掩码、潜变量锚定与优化的零样本物体移除方法
authors:
- Arman Taghizadeh
- Ulf Krumnack
- Kai-Uwe Kühnberger
affiliations:
- Institute of Cognitive Science, Osnabrück University
arxiv_id: '2609.28342'
url: https://arxiv.org/abs/2609.28342
pdf_url: https://arxiv.org/pdf/2609.28342
published: '2026-09-23'
collected: '2026-09-24'
category: Other
direction: 零样本图像编辑 · 扩散模型优化
tags:
- Stable Diffusion
- Zero-Shot Editing
- Image Inpainting
- SAM
- Attention Masking
one_liner: 提出无需微调的零样本Stable Diffusion物体移除pipeline，兼顾残差抑制、非编辑区保留与背景一致性
practical_value: '- 电商商品图、场景图可快速去水印/多余杂物，无需定制训练模型，大幅降低美工修图人力成本

  - 背景复杂的场景图（如服饰街拍、家居实拍）可开启背景加权NTI模块提升效果，简单背景关闭NTI提速

  - 可复用局部多次重降噪优化技巧，消除图像编辑后的边界伪影、内容残留，提升出图最终质量'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有图像物体移除方案多需任务定制训练或微调，难以同时满足残差特征抑制、非编辑场景完整保留、补全内容与背景高度一致三大核心需求，零样本通用方案效果较差。
### 方法关键点
基于冻结的预训练Stable Diffusion搭建多阶段pipeline，集成SAM自动生成掩码、BLIP图像字幕条件引导、DDIM反演、背景加权掩码空文本优化、解码器自注意力掩码、掩码外硬潜变量锚定、局部重降噪优化多个模块，无需任何任务微调即可直接推理。
### 关键结果
定性+定量局部一致性指标验证物体移除效果优异，补全内容与背景高度匹配；消融实验显示背景加权NTI对结构复杂背景提升显著，简单场景可省略该模块降低耗时；多次重降噪优化可进一步减少首遍编辑后的物体残留与边界伪影。
