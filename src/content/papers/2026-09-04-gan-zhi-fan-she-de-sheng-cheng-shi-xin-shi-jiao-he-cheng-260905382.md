---
title: Reflection-aware Generative Novel View Synthesis
title_zh: 感知反射的生成式新视角合成
authors:
- GeonU Kim
- Shin Dong-Yeon
- Tae-Hyun Oh
affiliations:
- KAIST
arxiv_id: '2609.05382'
url: https://arxiv.org/abs/2609.05382
pdf_url: https://arxiv.org/pdf/2609.05382
published: '2026-09-04'
collected: '2026-09-08'
category: Other
direction: 生成式新视角合成 · 反射感知优化
tags:
- Novel View Synthesis
- Diffusion Model
- Reflection Awareness
- Multi-view Diffusion
- Training-free
one_liner: 提出无需训练的Ref-GeNVS方法，解决含镜像场景生成式新视角合成的反射不一致问题
practical_value: '- 电商AR试穿、3D商品展示等含镜面的场景下，可借鉴镜像虚拟视图构造方法优化新视角渲染的一致性，降低展示内容的违和感

  - 无需微调预训练主干、仅通过前置信息注入+注意力门控适配垂域场景的思路，可迁移到垂域LLM/多模态模型适配，显著降低训练成本

  - 多模态内容生成场景中，对特殊结构（如镜像、透明物体）的显式建模思路，可有效提升生成内容的逻辑自洽性'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有多视角扩散模型处理含镜像的场景时，无法正确识别镜像、利用反射内容，生成的新视角存在反射不一致、镜面糊化、内容泄露等问题，且现有优化方案通常需要额外微调，泛化性较差。
### 方法关键点
提出训练-free的Ref-GeNVS框架：
1. 前置处理：从输入图像估计镜像平面，反射相机位姿生成虚拟视图，将镜像内容作为场景的互补视角引入
2. 两阶段生成：设计Mirror-gated attention显式建模镜像与真实场景的对应关系，搭配Reflection injection注入反射一致性约束，全程无需微调多视角扩散主干
### 关键结果
在含镜像的合成、真实场景数据集上，Ref-GeNVS性能超过现有SOTA生成式新视角合成方法，可生成反射一致、上下文连贯的新视角，还原仅在镜像中可见的场景结构。
