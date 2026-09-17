---
title: 'ResLRP: The Role of Residual Cancellation in Attribution Instability in Vision
  Transformers'
title_zh: ResLRP：视觉Transformer中残差抵消对归因不稳定的作用
authors:
- Jim Berend
- Reduan Achtibat
- Daniel Schäffer
- Alexander Binder
- Wojciech Samek
- Sebastian Lapuschkin
- Maximilian Dreyer
affiliations:
- Fraunhofer Heinrich Hertz Institute
- Technische Universität Berlin
- Leipzig University
- Berlin Institute for the Foundations of Learning and Data
- Singapore Institute of Technology
arxiv_id: '2609.17152'
url: https://arxiv.org/abs/2609.17152
pdf_url: https://arxiv.org/pdf/2609.17152
published: '2026-09-15'
collected: '2026-09-17'
category: Other
direction: ViT可解释性 · 归因方法优化
tags:
- ViT
- LRP
- Attribution
- Explainability
- VLM
- Transformer
one_liner: 提出残差感知的LRP变体ResLRP，大幅提升ViT及多模态模型的归因质量
practical_value: '- 做多模态商品理解、图文召回模型的badcase排查时，可引入ResLRP替换原有LRP方法，准确定位VLM预测依赖的视觉特征，大幅提升归因效率

  - 自研Transformer类推荐/多模态模型架构时，可复用论文提出的残差放大诊断指标，提前定位归因不稳定的层，优化模型可解释性

  - 做Sparse Autoencoder特征与输入空间对齐的工作时，可直接复用ResLRP的定位能力，辅助黑盒Transformer模型的可解释性改造'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
ViT及衍生多模态模型的输入归因存在噪声大、保真度低的问题，原有适配Transformer的LRP方法未考虑残差连接的抵消效应，导致归因爆炸，且ViT中该抵消效应远强于语言Transformer。
### 方法关键点
提出ResLRP，是LRP的轻量扩展，传播规则显式建模残差分支的抵消效应，满足严格守恒性，可证明限制归因爆炸；通过因果通道干预验证了残差抵消是归因不稳定的核心原因，而非通用正则化效应。
### 关键结果
在全类别ViT架构（监督/自监督/对比/分层/多模态）及FunnyBirds基准上，归因保真度、定位性能均显著提升；在VLM上收益最大，定位指标提升27-29%，保真度最高达原有方法的3.4倍；额外支持Sparse Autoencoder特征的输入空间定位，残差放大指标可作为架构级诊断工具预测归因退化位置。
