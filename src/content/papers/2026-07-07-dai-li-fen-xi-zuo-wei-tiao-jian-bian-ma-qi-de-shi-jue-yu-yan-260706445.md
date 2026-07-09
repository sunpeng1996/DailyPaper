---
title: 'Analysis-by-Proxy: Localization Signals in VLMs Operating as Condition Encoders'
title_zh: 代理分析：作为条件编码器的视觉语言模型中的定位信号
authors:
- Yoav Baron
- Sara Dorfman
- Roni Paiss
- Daniel Cohen-Or
- Or Patashnik
affiliations:
- Tel Aviv University
- Google DeepMind
arxiv_id: '2607.06445'
url: https://arxiv.org/abs/2607.06445
pdf_url: https://arxiv.org/pdf/2607.06445
published: '2026-07-07'
collected: '2026-07-09'
category: Multimodal
direction: 多模态模型 · VLM表征分析
tags:
- VLM
- localization
- diffusion model
- image editing
- representation analysis
one_liner: 提出代理分析框架，揭示VLM作为条件编码器时空间定位能力下降的底层机制
practical_value: '- 电商商品图AI编辑场景，不要直接用VLM固定层输出作为扩散模型条件，可基于代理模型动态提取中间层的定位相关表征，提升多商品场景的编辑准确性

  - 多模态表征挖掘场景可复用轻量代理模型方案，无需微调大模型即可快速定位VLM中目标信号所在的层位置，大幅降低实验成本

  - 跨模态商品召回场景可借鉴该思路，挖掘VLM中间层隐藏的空间/属性信号，提升商品图文匹配的精度'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
基于扩散模型的图像编辑管线将VLM作为条件编码器时，在多实体复杂场景下的空间定位精度远低于VLM独立运行时的原生能力，性能缺口的底层成因尚未明确。
### 方法关键点
提出Analysis-by-Proxy分析框架：针对定位辅助任务训练轻量可解释的代理模型，拟合VLM各层的中间表征，无需修改VLM本身即可定位其内部编码空间信息的具体表征位置。
### 关键结果
1. 单前向传播约束下，现有编辑管线常用的预定义固定层输出无法稳定传递定位信号；
2. 核心定位信号隐藏在VLM的中间层，且其所在位置随输入prompt动态变化，证明现有条件提取策略与VLM的空间知识表征方式存在根本性 mismatch。
