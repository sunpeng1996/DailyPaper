---
title: 'ALADDIN: Adversarial Latent Diffusion Distillation for One-Step Identity Swapping'
title_zh: ALADDIN：面向单步人脸交换的对抗潜在扩散蒸馏方法
authors:
- Ivan Shchekotov
- Timofei Gritsaev
- Viacheslav Pirogov
- Dmitry Vetrov
affiliations:
- Constructor University, Bremen, Germany
- Sumsub, Berlin, Germany
arxiv_id: '2610.37503'
url: https://arxiv.org/abs/2610.37503
pdf_url: https://arxiv.org/pdf/2610.37503
published: '2026-10-27'
collected: '2026-10-29'
category: Multimodal
direction: 多模态生成 · 单步人脸交换
tags:
- Diffusion Distillation
- Face Swapping
- Adversarial Training
- One-step Generation
- Latent Diffusion
one_liner: 通过扩散蒸馏+对抗训练实现单步人脸交换，性能追平多步模型，推理速度提升28倍
practical_value: '- 电商虚拟试衣/试妆等需人脸交换的实时场景，可复用该扩散蒸馏方案，将多步扩散模型压缩为单步生成，推理速度提升28倍，适配低延迟业务要求

  - 多约束生成任务（如身份迁移+属性保留）可引入triplet伪标签监督，实现不同约束间的可控权衡，适配不同业务优先级（如试妆优先保留妆容属性）

  - 生成类模型效果评估需避免使用与训练对齐的编码器计算指标，建议采用独立第三方评估模型，消除评估偏差，保证业务迭代的指标可信度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有扩散-based人脸交换生成效果逼真，但需多次前向推理速度慢；GAN-based单步方法速度快，但生成质量差，同时标准评估协议存在编码器对齐偏差，指标可信度低。
### 方法关键点
1. 用预训练多步流匹配模型初始化生成器，结合对抗训练+身份/目标属性保留约束，蒸馏得到单步人脸交换模型ALADDIN
2. 引入triplet伪标签监督，实现身份迁移与目标属性保留效果的可控权衡
3. 采用独立身份编码器重新评估所有基线，消除原有评估协议的偏差
### 关键结果
单步方法中真实度与目标属性保留效果达到SOTA，身份迁移效果追平最优多步模型，推理网络前向次数减少28倍，训练所需配对数据量低一个数量级
