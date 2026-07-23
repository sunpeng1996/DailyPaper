---
title: Importance-Aware OBS Pruning for Diffusion Models
title_zh: 面向扩散模型的重要性感知OBS剪枝方法
authors:
- Ba-Thinh Lam
- Srijan Das
- Hieu Le
affiliations:
- UNC Charlotte
arxiv_id: '2607.20048'
url: https://arxiv.org/abs/2607.20048
pdf_url: https://arxiv.org/pdf/2607.20048
published: '2026-07-22'
collected: '2026-07-23'
category: Training
direction: 扩散模型 · 无训练剪枝压缩
tags:
- Diffusion Model
- OBS Pruning
- Training-free
- Model Compression
- Semantic Awareness
one_liner: 提出无训练的重要性感知OBS剪枝框架，高压缩比下保留扩散模型生成语义关键区域的保真度
practical_value: '- 电商商品图、营销素材等扩散模型生成场景，可直接复用该无训练剪枝方案，无需重训即可降低模型推理成本，同时保留主体商品的生成质量

  - 剪枝时引入语义重要性权重替代均匀重构误差的思路，可迁移到LLM、多模态推荐模型的压缩优化，优先保留和用户兴趣、商品语义强相关的参数

  - 无训练剪枝的框架设计可复用在业务侧快速落地模型压缩需求，避免重训带来的算力、时间成本消耗'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
扩散模型参数量大、推理步数多，部署成本高；现有OBS类无训练剪枝方法基于均匀重构误差优化，高压缩比下会导致生成内容的语义关键区域质量明显退化，无法满足业务对生成内容的感知保真要求。
### 方法关键点
1. 设计无训练的重要性感知OBS剪枝框架，将从条件信号、模型注意力中提取的空间重要性图引入剪枝目标
2. 基于语义感知相关性做参数优先级排序，而非传统的均匀重构误差，优先保留语义显著区域对应的参数
### 关键结果
在MS-COCO数据集上，30%、40%稀疏度的结构化剪枝场景下，相比OBS-Diff基线，生成内容的主体保真度、结构正确性显著更优，高压缩比下无基线的明显生成退化问题。
