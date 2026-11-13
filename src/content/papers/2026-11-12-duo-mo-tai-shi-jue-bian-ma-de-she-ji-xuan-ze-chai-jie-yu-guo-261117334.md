---
title: Unbundling Multimodal Vision Encoding
title_zh: 《多模态视觉编码的设计选择拆解与效果对比研究》
authors:
- Ellis Brown
- Chris Hoang
- Shengyi Qian
- Shang-Wen Li
- Mike Lewis
- Marjan Ghazvininejad
- Luke Zettlemoyer
- Lucas Beyer
- Mengye Ren
- Jakob Verbeek
affiliations:
- Meta FAIR
- New York University
arxiv_id: '2611.17334'
url: https://arxiv.org/abs/2611.17334
pdf_url: https://arxiv.org/pdf/2611.17334
published: '2026-11-12'
collected: '2026-11-13'
category: Multimodal
direction: 多模态大模型 · 视觉编码架构优化
tags:
- Multimodal-LLM
- Vision-Encoder
- Multimodal-Fusion
- VQA
one_liner: 通过受控实验拆解多模态视觉编码三大设计要素的作用，给出最优架构选型方向
practical_value: '- 做多模态商品理解、多模态生成式推荐时，无需单独预训练视觉编码器，和LLM主干联合从零训练即可达同等效果，简化训练流程降低成本

  - 不要为了简化架构砍掉专用视觉模块，哪怕把无编码器的LLM主干扩容到对应参数量，视觉理解效果仍显著落后

  - 可将视觉专用模块嵌入LLM主干早期层做融合（而非预融合阶段单独放编码器），能降低首token耗时，适配多模态对话Agent、实时图文检索场景'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
多模态大模型视觉编码方案选型缺乏统一结论，现有视觉编码器耦合「上游预训练视觉先验、专用视觉容量、预融合部署位置」三大设计选择，过往模型对比因数据、架构、算力差异无法隔离变量，无法明确各选择的实际收益。
### 方法关键点
搭建全受控实验框架，所有模型在统一数据集、相同总算力约束下从零预训练，仅调整单一设计变量，在VQA、通用语言基准上对齐评测。
### 关键结果
1. 视觉预训练先验非必需，与语言主干联合从零训练的编码器效果和预训练编码器持平，可省去单独预训练流程；
2. 专用视觉容量是核心影响因素，无编码器方案即使主干扩容对应参数量，视觉理解效果仍显著落后；
3. 视觉容量无需放在预融合阶段，嵌入主干早期层的融合方案效果与预融合编码器相当，可显著降低首token耗时，该结论跨主干尺寸、预训练LM初始化场景均成立。
