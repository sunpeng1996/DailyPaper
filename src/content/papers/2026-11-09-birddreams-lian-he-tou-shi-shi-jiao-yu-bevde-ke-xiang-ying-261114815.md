---
title: 'BirdDreams: Joint Perspective and BEV Video Generation for a Plausible, Reactive
  Driving World Model'
title_zh: BirdDreams：联合透视视角与BEV的可响应驾驶世界模型视频生成
authors:
- Junyoung Seo
- Jaewoo Seo
- Seungryong Kim
- Laura Leal-Taixé
- Xiuming Zhang
- Seung Wook Kim
affiliations:
- NVIDIA
- KAIST
arxiv_id: '2611.14815'
url: https://arxiv.org/abs/2611.14815
pdf_url: https://arxiv.org/pdf/2611.14815
published: '2026-11-09'
collected: '2026-11-14'
category: Other
direction: 自动驾驶 · 世界模型多模态生成
tags:
- World Model
- BEV
- Video Generation
- Diffusion Transformer
- Autonomous Driving
one_liner: 提出联合透视与BEV视频生成的自回归驾驶世界模型，无需HD地图即可生成高拟真可控驾驶场景
practical_value: '- 多模态互补生成架构可迁移至GenRec场景：同时生成商品展示内容与Semantic ID表征，通过跨流注意力约束双模态生成一致性，提升推荐结果合理性

  - 软条件注入技巧可用于生成控制：需约束生成轨迹（如推荐转化目标、多样性要求）时，可将最新生成帧做数值/逻辑变换后作为软条件注入，避免硬约束破坏生成自然度

  - 可复用减少输入依赖的训练思路：业务场景缺少高精输入特征时，可将隐式布局（如用户兴趣分布）作为预测输出而非前置输入，降低推理阶段数据门槛'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
驾驶世界模型需同时满足周边车辆运动拟真、自车轨迹精准控制要求，仅基于透视视频训练存在运动与外观耦合、车辆易遮挡的痛点，现有方案需预先输入未来车辆轨迹，部署门槛高。
### 方法关键点
1. 自回归架构同时生成透视视角视频与BEV视频：BEV由标注渲染用于训练，以固定公制尺度输出道路、车辆简化形态，缓解遮挡问题补充几何布局信息，透视视频保留交通信号、物体外观等细节；
2. 双路视频Diffusion Transformer采用联合注意力机制，实现两个生成流的信息互补；
3. 预测得到的BEV作为自车控制几何接口，将最新生成帧沿输入自车轨迹平移旋转后作为软条件注入后续生成，无需额外HD地图、车辆状态输入。
### 关键结果
在PhysicalAI-AV、nuScenes数据集上自车轨迹跟随保真度优于现有SOTA模型，无自车动作约束场景下生成运动合理性更优，人工评估显示周边车辆行为真实度显著优于仅透视视角基线。
