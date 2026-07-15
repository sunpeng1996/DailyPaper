---
title: 'VisCo: Leveraging Large Language Models as Intrinsic Encoders for Visual Token
  Compression'
title_zh: VisCo：复用大语言模型作为内在编码器实现视觉Token压缩
authors:
- Yupeng Zheng
- Kai Zou
- Bin Liu
- Nenghai Yu
arxiv_id: '2607.12756'
url: https://arxiv.org/abs/2607.12756
pdf_url: https://arxiv.org/pdf/2607.12756
published: '2026-07-14'
collected: '2026-07-15'
category: Multimodal
direction: 多模态大模型 · 视觉Token压缩
tags:
- VLM
- Visual Token Compression
- Parameter Sharing
- Multimodal Inference
- Autoencoder
one_liner: 提出参数共享的自压缩框架VisCo，低训练成本实现VLM视觉Token高效压缩
practical_value: '- 多模态生成式推荐/广告场景中，可直接用VisCo压缩商品图像的视觉token，大幅降低VLM推理时延与显存开销，提升在线多模态排序/召回服务的吞吐量

  - 无需新增外部压缩模块，仅复用预训练VLM做参数共享式自压缩，避免全量微调的高额成本，适配中小团队多模态推荐落地需求

  - 高压缩比下性能损失远低于无训练策略，可用于多模态Agent的实时商品图像理解场景，端侧/边缘侧部署时也能保障响应速度'
score: 8
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有VLM处理大量视觉token带来极高推理时延与显存开销：无训练压缩策略依赖启发式规则，高压缩比下性能衰减严重；有训练压缩方法需引入外部模块并重训VLM主干，成本高且破坏预训练先验，预训练VLM本身的强编码能力未被充分利用。
### 方法关键点
提出训练高效的自压缩框架VisCo，直接复用预训练VLM本身作为内在编码器，基于参数共享的自编码器结构，通过少量记忆token压缩视觉信息，同时实现编码侧到解码侧的分层信息传递，无需新增外部压缩模块。
### 关键结果
所有评估压缩比下性能均超越此前SOTA方法，压缩越激进收益越高，极端单token压缩场景下仍保持性能稳定；生成的记忆token搭配原始视觉token使用时，可进一步提升基础VLM性能，能输出额外互补表征。
