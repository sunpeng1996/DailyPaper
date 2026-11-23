---
title: Autoregressive View Model
title_zh: 自回归视图模型（AVM）：无需显式3D表征的场景视频生成
authors:
- Jensen
- Zhou
- Samuel Rota Bulo
- Denis Rozumny
- Duncan Zauss
- Peter Hedman
- Nikhil Keetha
- Philip Torr
- Christian Rupprecht
- Andrea Vedaldi
affiliations:
- Meta
- University of Oxford
arxiv_id: '2611.23417'
url: https://arxiv.org/abs/2611.23417
pdf_url: https://arxiv.org/pdf/2611.23417
published: '2026-11-16'
collected: '2026-11-23'
category: Multimodal
direction: 多模态生成 · 3D场景视频合成
tags:
- Video Generation
- In-Context Learning
- Diffusion Transformer
- Autoregressive Model
- 3D Scene Synthesis
one_liner: 提出无需显式3D表征的自回归视图模型，通过统一上下文接口生成指定相机路径的场景视频流
practical_value: '- 上下文动态管理思路可复用：从输入和历史生成结果中检索相关内容构建有限活跃上下文，降低长序列生成的显存占用与漂移问题，适合长对话推荐Agent、多轮搜索场景的上下文窗口优化

  - 两阶段微调范式可参考：先基于预训练大模型用N进1出范式适配下游任务，再用模型自生成输出迭代微调，提升生成质量、降低推理步数，适合LLM4Rec的小样本快速适配

  - 统一in-context接口设计思路：单接口适配多输入输出场景的方案，可用于跨模态推荐系统（如图搜、视频带货素材生成）的多任务入口设计'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有3D场景视频生成方法存在明显局限：依赖显式3D表征的方案（如NeRF、3D高斯溅射）需要密集输入才能实现高质量渲染，普通视频生成器易出现长序列漂移、场景一致性差的问题，无法同时适配重建、插值、外推等多场景需求。
### 方法关键点
1. 采用自回归生成范式，无需构建显式3D表征，从输入和历史生成视图中检索相关内容构建有限活跃上下文
2. 第一阶段用流匹配目标微调预训练双向视频扩散Transformer，采用N进1出的生成范式
3. 第二阶段用模型自生成的rollout微调因果模型，优化生成真实感、减少降噪步数、抑制长序列漂移
### 关键结果
训练数据规模达8M场景与视频片段，在相机控制、文本控制、视觉质量、4D重建、长序列一致性等多个基准上，实现了多输入输出场景的统一适配。
