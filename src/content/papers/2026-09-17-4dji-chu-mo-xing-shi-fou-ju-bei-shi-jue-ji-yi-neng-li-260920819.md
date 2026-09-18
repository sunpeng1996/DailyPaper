---
title: Can 4D Foundation Models Remember?
title_zh: 4D基础模型是否具备视觉记忆能力？
authors:
- Guangzhao He
- Hadar Averbuch-Elor
- Wei-Chiu Ma
affiliations:
- Cornell University
arxiv_id: '2609.20819'
url: https://arxiv.org/abs/2609.20819
pdf_url: https://arxiv.org/pdf/2609.20819
published: '2026-09-17'
collected: '2026-09-18'
category: Eval
direction: 4D基础模型 · 视觉记忆评测
tags:
- 4D Foundation Model
- Visual Memory
- Evaluation Benchmark
- Object-centric
- 360° Video
one_liner: 提出PersistBench评测套件，从三维度评估4D基础模型视觉记忆，揭示现有模型离视野记忆退化缺陷
practical_value: '- 做多模态商品3D/4D展示、虚拟试穿的4D生成模型，可复用PersistBench的三维度评测逻辑（物体存续、运动连续、外观保留）评估生成内容的时空一致性

  - 电商实景导购Agent、线下AR导航机器人的环境感知模块，可参考该评测逻辑优化移出视野物体的记忆召回策略

  - 长时序多模态用户行为建模场景，可参考object-centric的评估思路，避免仅用像素/行为级指标忽略核心实体的一致性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有4D基础模型（相机可控视频模型、4D重建模型）已可感知重构动态环境，但对其感知后记忆能力的评估存在空白；现有基准仅依赖像素级指标，无物体移出视野后的真值，无法实现物体中心的对比评估。
### 方法关键点
提出PersistBench数据集与评测套件，以360°视频作为全知真值，从三个维度开展评估：1. 物体永久性 2. 运动连续性 3. 外观保留度。
### 关键结果
对多类不同架构的4D模型评测显示，现有模型仅能维持短期一致性，物体一旦移出视野，记忆表现大幅退化，验证了「看见不等于记住」的能力缺口，为后续4D模型优化提供明确方向。
