---
title: 'Know, then Draw: A New Learning Paradigm for Visual Generation'
title_zh: 先认知后生成：一种视觉生成领域的新型学习范式
authors:
- Yucheng Mao
- Chongjian Ge
- Zhuowen Tu
- Hao Tan
- Hanwen Jiang
affiliations:
- University of California, San Diego
- Adobe Research
arxiv_id: '2610.37626'
url: https://arxiv.org/abs/2610.37626
pdf_url: https://arxiv.org/pdf/2610.37626
published: '2026-10-27'
collected: '2026-10-29'
category: Multimodal
direction: 多模态生成 · 高效训练范式优化
tags:
- Visual Generation
- Autoregressive Pretraining
- Diffusion Model
- Semantic Tokenizer
- Scaling Law
one_liner: 拆分语义认知与高清渲染任务，提出AR预训练加扩散后训练的高效视觉生成新范式
practical_value: '- 电商商品图、广告图生成场景可复用任务拆分范式：先通过AR预训练学习商品、场景通用语义知识，再用轻量化diffusion模块完成高清渲染，大幅降低训练成本

  - 纯语义tokenizer可仅用语言监督训练，无需额外图像解码器与重建损失，适合电商场景下快速对齐品类、属性等多模态语义，降低tokenizer开发开销

  - 可直接复用该范式的算力分配scaling law，指导业务侧多模态生成模型的参数选型与算力预算规划，用最少算力达到目标生成效果'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视觉生成范式要求模型同时学习高层语义知识与细粒度像素渲染能力，训练效率低、算力成本高，AR与扩散模型的各自优势未得到有效协同。
### 方法关键点
1. 提出拆分式学习范式：AR预训练阶段负责语义知识获取，diffusion后训练阶段负责高保真像素渲染，两个任务解耦优化
2. 基于「AR生成质量与最终性能弱相关、语义质量更关键」的结论，设计仅靠语言监督训练的纯语义tokenizer，无需图像解码器与重建损失
3. 推导得到知识获取、渲染两个阶段的计算最优scaling law，指导算力分配
### 关键结果
3B参数文生图模型仅需6600 H100 GPU小时训练，GenEval得分86、DPG-Bench得分87，相比同类基准模型算力消耗降低48倍，性能提升10%
