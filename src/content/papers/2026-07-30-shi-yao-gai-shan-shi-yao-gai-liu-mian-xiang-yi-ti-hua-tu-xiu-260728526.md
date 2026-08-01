---
title: 'What to Remove, What to Preserve: Dual-Ambiguity Rectification for All-in-One
  Image Restoration'
title_zh: 什么该删什么该留：面向一体化图像修复的双歧义校正网络
authors:
- Cencen Liu
- Wen Yin
- Dongyang Zhang
- Dongmin Li
- Shan Zhao
- Bing Su
- Tao He
- Jielei Wang
- Guoming Lu
affiliations:
- University of Electronic Science and Technology of China
- Jiigan Technology
arxiv_id: '2607.28526'
url: https://arxiv.org/abs/2607.28526
pdf_url: https://arxiv.org/pdf/2607.28526
published: '2026-07-30'
collected: '2026-08-01'
category: Other
direction: 多模态图像修复 · 特征解耦
tags:
- Image Restoration
- Feature Disentanglement
- Degradation Modeling
- Orthogonal Regularization
- Prompt Modulation
one_liner: 通过双歧义校正模块解耦退化特征与场景内容，提升多退化场景下统一图像修复效果
practical_value: '- 电商商品图预处理环节可复用退化感知prompt生成逻辑，针对模糊/水印/噪点等不同退化场景自适应调整修复策略，避免商品细节被误抹除

  - 特征正交正则化思路可迁移至多模态推荐的特征解耦任务，减少用户兴趣特征与内容质量特征的空间干扰，提升召回排序稳定性

  - 单纯形约束的原型混合建模方法可用于多模态内容质量分级，快速识别图像退化类型与程度，自动化筛选低质量公域/私域物料'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有一体化图像修复方法将异构退化条件编码到共享隐空间，导致退化特征与场景内容纠缠，引发两类歧义：通道调制的语义歧义、修复响应的空间歧义，最终出现内容损坏、残留伪影问题。

### 方法关键点
1. 设计DAR-Net双歧义校正网络，通过退化原型表征（DAR）模块基于单纯形约束的原型混合建模，构建结构化退化状态；
2. 语义歧义校正（SeAR）模块生成退化感知prompt，优化解码器的通道条件控制；
3. 空间歧义校正（SpAR）模块将退化感知特征与互补特征约束到正交响应子空间，减少去除/保留信号的空间干扰。

### 关键结果
在3种退化、5种退化的标准基准上均取得最优性能，平均PSNR对比最强基线分别提升0.14dB、0.34dB，在CDD-11、WeatherBench数据集上也表现出显著优势。
