---
title: On the Diffusibility of High-Dimensional Latents
title_zh: 高维隐空间特征的可扩散性研究
authors:
- Chao Feng
- Zhiyang Xu
- Bowei Chen
- Yuanjun Xiong
- Xiyao Wang
- Jui-Hsien Wang
- Richard Zhang
- Zhe Lin
- Andrew Owens
- Yijun Li
affiliations:
- Cornell University
- Adobe
- Virginia Tech
- University of Washington
- University of Maryland
arxiv_id: '2609.28473'
url: https://arxiv.org/abs/2609.28473
pdf_url: https://arxiv.org/pdf/2609.28473
published: '2026-09-22'
collected: '2026-09-24'
category: Training
direction: 扩散模型训练 · 高维隐空间优化
tags:
- Diffusion Model
- Flow Matching
- Latent Space
- Text-to-Image
- Representation Autoencoder
one_liner: 发现高维隐空间流匹配速度预测效率低，采用x0预测可稳定提升文本生成图像性能
practical_value: '- 电商商品图AIGC场景中，若使用RAE做特征编码器，可直接将速度预测替换为x0-prediction，无需改架构即可提升生成精度

  - 多模态召回特征蒸馏时，可参考本文结论：重构微调会降低特征有效维度，需平衡特征维度与细粒度信息密度

  - Agent多模态输入表征优化时，高维特征空间下的生成类任务优先选聚焦信号流形的参数化方案，降低优化成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
Representation Autoencoders (RAE) 支持扩散模型在预训练视觉编码器的特征空间执行生成任务，但通用预训练编码器不面向重构优化，会丢失细粒度视觉细节；对编码器做重构微调虽能找回细节，却会降低表征有效维度，导致高维空间下流匹配的标准速度预测需要拟合低维信号流形外的正交噪声方向，优化效率极低。
### 方法关键点
放弃传统速度预测范式，改用x0预测（干净数据参数化），将学习过程聚焦在底层信号流形上，无需额外修改模型架构。
### 关键结果
在多款具备强重构能力的编码器上验证，x0预测可稳定提升文本生成图像的性能，优化效率与生成效果双优。
