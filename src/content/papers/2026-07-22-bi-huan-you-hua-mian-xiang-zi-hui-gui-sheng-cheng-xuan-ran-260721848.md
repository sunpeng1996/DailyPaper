---
title: 'Closing the Loop: Training-Free Revisit Consistency for Autoregressive Generative
  Rendering'
title_zh: 闭环优化：面向自回归生成渲染的免训练重访一致性方案
authors:
- Wenchao Ma
- Changran Liu
- Sharon X. Huang
- Haomiao Jiang
affiliations:
- Roblox
- The Pennsylvania State University
arxiv_id: '2607.21848'
url: https://arxiv.org/abs/2607.21848
pdf_url: https://arxiv.org/pdf/2607.21848
published: '2026-07-22'
collected: '2026-07-28'
category: Other
direction: 自回归视频生成 · KV cache一致性优化
tags:
- KV cache
- Autoregressive Generation
- Video Generation
- Generative Rendering
- Training-Free
one_liner: 无需额外训练，利用3D引擎时空对应关系解决自回归生成渲染的长序列重访一致性问题
practical_value: '- KV cache动态召回历史匹配块的思路可复用，解决长序列生成中上下文被淘汰后的一致性问题，可落地到生成式推荐的长用户会话、Agent多轮交互场景

  - 免训练利用现有系统原生对应关系做注意力偏置的方案，可降低多模态生成（如电商商品图、营销文案生成）一致性优化的落地成本，无需额外微调模型

  - 时空匹配的检索逻辑可迁移到推荐系统的重复交互场景，如用户复访同品类商品时的召回结果风格、价格区间一致性对齐'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
长horizon自回归视频生成受限于有限的KV cache容量，当视角重访历史位置时，对应上下文已被淘汰，即使深度等3D输入条件完全对齐，生成内容的外观仍会出现不一致，无法满足游戏、沉浸式内容等场景对3D世界一致性的要求。
### 方法关键点
1 无需额外训练/微调，直接复用3D引擎原生提供的时空对应关系优化；
2 时间维度：检索姿态匹配的历史latent块注入KV cache，作为闭环记忆补充上下文；
3 空间维度：基于相机姿态和深度重投影，引导token级注意力偏向检索块的几何对应区域，保证生成一致性。
### 关键结果
在TartanAir、TartanGround数据集的真实场景闭环轨迹上，重访一致性表现优于所有现有免训练基线，同时无整体视频生成质量损失。
