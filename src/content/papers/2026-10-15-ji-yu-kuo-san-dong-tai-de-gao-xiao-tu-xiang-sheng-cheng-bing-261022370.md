---
title: Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation
title_zh: 基于扩散动态的高效图像生成Token合并策略
authors:
- SeungJu Cha
- Ye-Chan Kim
- HyunGee Kim
- Sungho Koh
- Dong-Jin Kim
affiliations:
- Hanyang University, South Korea
arxiv_id: '2610.22370'
url: https://arxiv.org/abs/2610.22370
pdf_url: https://arxiv.org/pdf/2610.22370
published: '2026-10-15'
collected: '2026-10-17'
category: Multimodal
direction: 扩散模型推理优化 · Token合并
tags:
- Token Merging
- Diffusion Model
- Image Generation
- Inference Acceleration
- Training-free
one_liner: 提出训练无关的动态感知Token合并框架DaTMe，加速扩散图像生成同时保留全图视觉保真度
practical_value: '- 电商多模态生成场景（如商品图、营销素材生成）可直接复用DaTMe的训练无关加速方案，无需额外训练模型即可降低文生图推理成本，同时避免背景/未提及细节失真

  - 做生成类任务的Token压缩时，可借鉴「时序信号+结构高频信号」结合的重要性打分逻辑，替代纯语义对齐的筛选规则，提升压缩后的生成质量

  - 扩散模型落地业务时，可将DaTMe作为推理侧优化组件，搭配KV cache、量化等策略进一步降低生成延时，适配实时素材生成需求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有扩散模型Token合并策略仅保留与prompt对齐的前景区域，忽略背景及prompt未明确提及的局部细节，导致生成结构一致性下降；同时扩散模型迭代推理的高算力成本限制了其在实时业务场景的落地。
### 方法关键点
提出训练无关的动态感知Token合并框架DaTMe，基于Tweedie去噪估计构建动态重要性图，融合两类信号：1）衡量预测干净图像步间变化的时序信号；2）捕捉边界、精细细节的局部高频结构信号。按给定压缩比自适应分配Token角色：高重要性Token保留为锚点，时序稳定且结构同质的Token作为安全合并候选。
### 关键结果
在PixArt-α、FLUX两个主流文生图扩散模型上验证，相同压缩比下，DaTMe可维持全图视觉保真度，无明显背景或细节退化。
