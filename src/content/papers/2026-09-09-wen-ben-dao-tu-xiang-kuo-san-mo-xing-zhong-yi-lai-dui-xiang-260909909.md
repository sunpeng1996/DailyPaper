---
title: Interpreting Object-Dependent Concept Brittleness in Text-to-Image Diffusion
  Models
title_zh: 文本到图像扩散模型中依赖对象的概念脆性解释
authors:
- Yifan Yuan
- Xiangyu Liu
- Hongming Shan
- Yu Han
- Yu Jiang
- Hao Tan
- Junping Zhang
- Linlin Shen
affiliations:
- Shenzhen University
- Fudan University
- National University of Singapore
arxiv_id: '2609.09909'
url: https://arxiv.org/abs/2609.09909
pdf_url: https://arxiv.org/pdf/2609.09909
published: '2026-09-09'
collected: '2026-09-11'
category: Other
direction: 扩散模型可解释性 · 概念脆性修正
tags:
- Diffusion Model
- Sparse Autoencoder
- Concept Interpretability
- Inference Correction
- Text-to-Image
one_liner: 识别扩散模型依赖对象的概念脆性问题，提出基于SAE空间的审计与推理阶段轻量修正框架
practical_value: '- 电商文生图营销素材生成场景，可引入SAE空间概念原型校验逻辑，降低特定商品+风格/属性组合的生成失败率

  - 无需重新训练扩散模型，仅在推理阶段做特征插值修正，工程落地成本低，可直接嵌入现有文生图生产链路

  - 可复用该SAE空间概念分析方法，定位现有生成链路的系统性错误盲点，针对性优化素材生成效果'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
文生图扩散模型存在依赖对象的概念脆性问题：相同生成配置下，仅替换prompt中对象词就会导致目标风格/属性概念无法稳定生成，属于系统性盲点而非随机噪声，此前研究关注较少。

### 方法关键点
1. 构建基于分步SAE空间的可解释性审计框架，SAE空间中风格、属性概念比原始去噪表征更易分离，可对比成功/失败生成的去噪轨迹，定位缺失、弱化或时序延迟的概念维度，基于可靠样本构建类级别概念原型；
2. 推理阶段轻量修正策略，将去噪特征向对应SAE空间原型插值，无需任务专属重训练。

### 关键结果
跨多个扩散骨干测试，概念一致性、文本保真度、修复成功率均有显著提升；深层去噪表征概念结构更清晰，早期阶段干预修正效果最优。
