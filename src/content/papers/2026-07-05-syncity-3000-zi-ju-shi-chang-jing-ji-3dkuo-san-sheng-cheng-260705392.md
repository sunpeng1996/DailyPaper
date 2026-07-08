---
title: 'SynCity 3000: Bootstrapping Scene-Scale 3D Diffusion'
title_zh: SynCity 3000：自举式场景级3D扩散生成框架
authors:
- Paul Engstler
- Iro Laina
- Christian Rupprecht
- Andrea Vedaldi
affiliations:
- Visual Geometry Group, University of Oxford
arxiv_id: '2607.05392'
url: https://arxiv.org/abs/2607.05392
pdf_url: https://arxiv.org/pdf/2607.05392
published: '2026-07-05'
collected: '2026-07-08'
category: Other
direction: 3D场景扩散生成 · 布局可控
tags:
- 3D Diffusion
- Scene Generation
- Synthetic Data
- Text-to-3D
- Convolutional Operator
one_liner: 将单物体图像转3D能力改造为卷积算子，实现可控布局的全局一致大尺度3D场景生成
practical_value: '- 训练数据稀缺场景可借鉴自研合成数据引擎生成伪数据做微调，降低对标注真实数据的依赖

  - 把单任务小尺度生成能力通过算子改造扩展到大规模任务的思路，可复用在电商3D卖场、虚拟直播间生成等业务

  - 先输出2D布局模板再转3D的两阶段生成范式，适合落地对布局可控性要求高的AIGC类需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文本转3D模型仅支持单物体生成，传统场景级3D生成方案存在网格割裂感强、全局一致性差的问题，同时3D场景训练数据稀缺难以支撑大模型端到端训练。
### 方法关键点
1. 自研合成数据引擎生成类场景训练数据，微调预训练图像转3D模型，将其改造为可卷积调用的算子，突破单物体生成的尺度限制
2. 两阶段生成流程：先基于用户prompt生成全场景等距2D图像作为布局模板，再将卷积化3D生成算子作用于模板，输出任意大小与复杂度的3D场景
### 关键结果
覆盖多类prompt与布局需求，生成的大尺度3D场景无明显网格割裂感，全局一致性、细节丰富度均显著优于此前方案，解决了场景级3D生成的核心痛点
