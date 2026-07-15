---
title: Backbone-Agnostic Perturbation-Induced Uncertainty Learning for End-to-End
  Real-World Image Dehazing
title_zh: 面向端到端真实图像去雾的Backbone无关扰动诱导不确定性学习
authors:
- Bingcai Wei
affiliations:
- School of Computer Science, Wuhan University
arxiv_id: '2607.11623'
url: https://arxiv.org/abs/2607.11623
pdf_url: https://arxiv.org/pdf/2607.11623
published: '2026-07-13'
collected: '2026-07-15'
category: Other
direction: 图像去雾 · 可插拔不确定性学习
tags:
- Image Dehazing
- Uncertainty Learning
- Plug-and-Play
- Contrastive Loss
- Reparameterization
one_liner: 提出可插拔BPUL不确定性学习框架，提升多类去雾backbone性能仅增微量推理开销
practical_value: '- 电商户外商品实拍图、线下商家到店图的质量增强环节可集成BPUL框架，低成本提升雾天图像清晰度，优化商品/POI展示效果

  - 可复用「训练阶段引入复杂约束模块、推理阶段仅保留轻量化核心组件」的架构设计思路，平衡算法效果与线上推理延迟

  - 多模态推荐/搜索的图像特征提取场景可借鉴重参数化随机扰动估计特征敏感度的方法，提升特征鲁棒性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
真实场景图像去雾存在空间非均匀、光照依赖、物理歧义等问题，现有端到端去雾网络多为确定性映射，未充分挖掘退化特征、雾先验、跨域负样本中隐藏的不确定性，效果受限。
### 方法关键点
可插拔BPUL不确定性学习框架包含三个核心模块：
1. 可学习扰动诱导不确定性调制器(LPUM)：通过重参数化随机扰动估计通道与空间维度的特征敏感度
2. 先验感知不确定性引导的重建模块(PURM)：利用透射率与大气光先验从复原结果重建雾天观测，约束退化一致性
3. 双空间域多样化分布感知对比损失(D³CL)：用真实与合成负样本同时正则化干净复原与雾天重建空间
训练阶段使用全部模块，推理阶段仅保留LPUM。
### 关键结果
在5个真实场景成对基准数据集上测试，可稳定提升多个主流去雾backbone性能，仅带来可忽略的额外推理开销。
