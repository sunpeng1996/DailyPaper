---
title: Reinforcing the Generation Order of Multimodal Masked Diffusion Models
title_zh: 多模态掩码扩散模型的生成顺序强化优化方法
authors:
- Yidong Ouyang
- Zhe Wang
- Sourav Bhabesh
- Dmitriy Bespalov
affiliations:
- University of California, Los Angeles
- AGI Foundations for AWS
arxiv_id: '2607.08056'
url: https://arxiv.org/abs/2607.08056
pdf_url: https://arxiv.org/pdf/2607.08056
published: '2026-07-09'
collected: '2026-07-11'
category: Multimodal
direction: 多模态扩散模型 · 生成顺序优化
tags:
- Multimodal Diffusion
- GRPO
- Text-to-Image
- Multimodal Understanding
- Generation Order
one_liner: 通过GRPO训练的可学习控制模块优化多模态掩码扩散模型生成顺序，提升文生图对齐与多模态理解效果
practical_value: '- 电商多模态商品生成（如AI模特图、商详文生图）场景，可引入GRPO训练的可学习生成顺序控制模块，提升文图匹配度，减少属性、空间位置类生成错误

  - 多模态商品理解（如图文打标、多模态召回特征提取）场景，可复用该生成顺序优化思路，提升跨模态信息匹配精度

  - Semantic ID生成、多模态Prompt生成等离散token生成类任务，可参考用强化学习优化生成顺序而非固定解码顺序的思路，突破现有性能瓶颈'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
扩散语言模型（DLMs）的自适应token生成顺序在数学推理、代码合成等结构化任务表现优异，但仅靠模型logits无法确定文生图、多模态理解场景的最优生成序列，效果受限。
### 方法关键点
1. 针对多模态掩码扩散模型可任意顺序生成的特性，新增可学习控制模块，采用Group Relative Policy Optimization（GRPO）训练模块决策最优生成序列
2. 模块适配跨模态生成与理解逻辑，强化细粒度空间依赖、跨模态关联的捕捉能力
### 关键结果
- GenEval文生图对齐基准相对提升4.08%
- VLMEvalKit多模态理解基准相对提升4.85%
