---
title: A Study of the Limits of Collaborative DCT-Based Image Denoising via Interpretable
  Neural Networks
title_zh: 基于可解释神经网络的协作DCT图像去噪能力边界研究
authors:
- Cristian Comellas
- Julia Navarro
- Antoni Buades
affiliations:
- Universitat de les Illes Balears
arxiv_id: '2609.29334'
url: https://arxiv.org/abs/2609.29334
pdf_url: https://arxiv.org/pdf/2609.29334
published: '2026-09-24'
collected: '2026-09-25'
category: Other
direction: 可解释图像去噪 · 传统算法可微分改造
tags:
- Image Denoising
- BM3D
- Differentiable Architecture
- Collaborative Filtering
- DCT
- Interpretability
one_liner: 将传统BM3D去噪框架改造为全可微分架构，兼顾可解释性与优秀去噪性能
practical_value: '- 成熟传统规则链路的可微分改造思路可复用：将业务中已验证有效的规则链路拆解为模块，仅替换不可微分硬规则为轻量可学组件，无需全链路推翻重做，兼具可解释性和性能收益

  - 多阶段结构化pipeline的端到端训练思路可迁移到推荐链路联合优化，保留各模块原有逻辑可解释性的同时实现全局调优

  - 若业务涉及商品主图/素材画质提升，可直接复用DeepBM3D轻量化架构，中低噪声场景下无需大模型即可获得可观效果'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
传统DCT类协作去噪算法（如BM3D）结构清晰可解释，但依赖手工设计的不可微分算子，性能上限固定；深度学习去噪模型性能优越，但多为黑盒大模型，可解释性差，结构化传统滤波框架的可微分改造性能边界尚不明确。
### 方法关键点
提出全可微分轻量化架构DeepBM3D，完全复用BM3D的成熟流水线逻辑：用轻量卷积特征提取器引导非局部patch分组，替换原有的硬匹配规则；DCT域滤波采用可学习的Wiener权重；保留多阶段精炼流程，整体结构完全可解释。
### 关键结果
性能全面优于经典与混合基线方案；中低噪声水平下与SOTA黑盒去噪模型FFDNet效果持平；针对重复纹理场景的去噪效果显著优于其他对比方案。
