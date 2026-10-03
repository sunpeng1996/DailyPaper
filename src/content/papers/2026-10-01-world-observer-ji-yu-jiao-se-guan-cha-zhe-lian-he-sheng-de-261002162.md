---
title: 'World Observer: Joint Actor-Observer Generation for Persistent World Modeling'
title_zh: World Observer：基于角色-观察者联合生成的持久世界建模
authors:
- Hyunwook Choi
- Dahyun Chung
- Hyunsung Kim
- Siyoon Jin
- Jinhyeok Choi
- Junyoung Seo
- Seungryong Kim
affiliations:
- KAIST AI
arxiv_id: '2610.02162'
url: https://arxiv.org/abs/2610.02162
pdf_url: https://arxiv.org/pdf/2610.02162
published: '2026-10-01'
collected: '2026-10-03'
category: Agent
direction: Agent 世界建模 · 多视角协同生成
tags:
- World Modeling
- Agent Perception
- Multi-View Generation
- Dynamic State Tracking
one_liner: 解耦智能体行动与观察链路，通过多全景观察者实现视野外物体状态持续精准建模
practical_value: '- 可迁移到电商3D虚拟导购Agent场景：解耦用户视角与全局观察模块，解决用户视角移动后虚拟商品、导购角色状态丢失的问题

  - 多观察者自由部署架构可复用在直播/短视频内容生成场景：针对被遮挡的商品、主播状态做持续追踪，优化动态剪辑的连贯性

  - Observer Sink高分辨率参考库设计可借鉴到生成式推荐场景：缓存细粒度视觉特征，提升跨场景召回时的内容视觉一致性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有以智能体（Actor）为中心的视频世界模型，对脱离Actor视野的物体无法持续追踪状态，当物体重回视野时往往无法还原正确动态，世界建模一致性差。
### 方法关键点
1. 解耦行动与观察链路，同步生成Actor视角内容与1~N个全景观察者内容，覆盖Actor视野外的指定区域，持续追踪移出视野物体的动态演化；
2. 基于共享全景源做视角变换，对齐Actor与观察者的几何对应关系，引入高分辨率视角参考库Observer Sink，还原物体重回视野时的精细外观；
3. 观察者支持自由部署、多节点扩展、控制信号驱动，可灵活覆盖场景盲区。
### 关键结果
提出世界空间维度的专用评估指标与覆盖真实/合成场景的基准数据集，视野外动态建模效果显著提升，同时视觉保真度、相机控制精度、3D一致性均保持业内竞争力
