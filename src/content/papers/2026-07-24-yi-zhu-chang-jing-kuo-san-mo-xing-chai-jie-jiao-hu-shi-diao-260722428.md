---
title: 'Unboxing Diffusion Models for the Arts: Interactive Model Bending and Practice-Based
  Explainability'
title_zh: 艺术场景扩散模型拆解：交互式调校与实践导向可解释性
authors:
- Ahmed M. Abuzuraiq
- Philippe Pasquier
affiliations:
- School of Interactive Arts and Technology, Simon Fraser University, Canada
arxiv_id: '2607.22428'
url: https://arxiv.org/abs/2607.22428
pdf_url: https://arxiv.org/pdf/2607.22428
published: '2026-07-24'
collected: '2026-08-02'
category: Multimodal
direction: 多模态生成 · 实践导向可解释性
tags:
- Diffusion Model
- XAI
- Interactive Interface
- Generative Art
- Model Intervention
one_liner: 提出艺术场景扩散模型实践导向可解释性方案，支持交互式层级干预调校
practical_value: '- 电商商品图AIGC生产场景可复用层级干预思路，定向调整生成图的风格、光影、纹理等属性，无需全量微调模型，降低调优成本

  - 面向运营/非技术用户的AIGC工具设计可参考交互式干预+效果对齐的思路，降低生成效果调试门槛，提升生产效率

  - 自定义AIGC能力可参考ComfyUI节点化集成方案，将干预能力封装为可复用节点，适配现有生产工作流'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
传统XAI偏技术导向，现有大规模文生图扩散模型多为黑盒端到端工具，无法满足艺术创作场景下用户对模型做检查、修改、调试的实操需求。
### 方法关键点
提出以实验与干预为核心的实践导向可解释性思路，开发模型调校能力与交互式检查界面，集成进ComfyUI节点式工作流，支持交互式层选择、定向干预等控制能力。
### 关键结果
在Stable Diffusion 1.5上的定性定量验证表明，针对扩散pipeline特定组件的操控可产生一致性较高的视觉效果族，帮助用户建立层级别操作与生成效果关联的实用直觉。
