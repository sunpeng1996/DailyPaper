---
title: 'AutoAnchor: Stable Diffusion Unlearning Using Cross-Attention as a Manifold
  Surrogate'
title_zh: AutoAnchor：基于交叉注意力流形代理的Stable Diffusion遗忘方法
authors:
- Siyuan Wen
- Jiahao Zeng
- Ningning Ding
affiliations:
- Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2607.08337'
url: https://arxiv.org/abs/2607.08337
pdf_url: https://arxiv.org/pdf/2607.08337
published: '2026-07-09'
collected: '2026-07-11'
category: Multimodal
direction: 多模态大模型 · 扩散模型概念遗忘
tags:
- Diffusion Unlearning
- Stable Diffusion
- Cross-Attention
- Manifold Learning
- Concept Erasure
one_liner: 提出自动生成流形近邻锚的两阶段框架，用交叉注意力损失做代理实现稳定无偏的扩散模型概念遗忘
practical_value: '- 电商生成式营销场景中，若需让文生图模型遗忘侵权IP、违禁风格/内容，可直接复用AutoAnchor框架替换手动选锚的遗忘方案，降低偏置同时提升遗忘稳定性

  - 所有需要做大模型遗忘的业务场景，均可借鉴交叉注意力一致性损失替代高复杂度的流形几何优化，在保证效果的前提下大幅降低计算开销

  - AutoAnchor可低成本接入现有扩散模型遗忘模块，平均提升6.3%目标概念移除率、6.65%非目标生成能力保留率，适配性强'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有扩散模型遗忘方法分为两类：锚点法依赖手动选取语义锚易引入遗忘偏置，无锚法隐空间更新无约束导致遗忘效果不稳定；理论证明缺乏流形近邻锚会引发严重法向空间漂移，大幅降低遗忘性能。
### 方法关键点
两阶段AutoAnchor框架自动合成流形近邻锚；为规避直接流形几何优化的极高计算开销，设计交叉注意力一致性损失作为流形邻近度的高效代理指标。
### 关键结果
- 相比SOTA基线，目标概念移除效果CLIP score最高提升31.04%，非目标生成能力CLIP score最高提升4.18%
- 可无缝接入现有扩散遗忘方法，平均提升6.30%概念移除效果、6.65%非目标效用保留率
