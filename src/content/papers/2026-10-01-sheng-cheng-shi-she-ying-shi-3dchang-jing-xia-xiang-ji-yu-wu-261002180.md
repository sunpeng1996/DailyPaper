---
title: 'Generative Cinematographer: Composing Camera and Object Motion in 3D'
title_zh: 生成式摄影师：3D场景下相机与物体运动联合可控生成
authors:
- Jiahan Zhang
- Chaohao Yang
- Namitha Guruprasad
- Vivekjyoti Banerjee
- Trong-Tung Nguyen
- Alan Yuille
- Anand Bhattad
affiliations:
- Johns Hopkins University
arxiv_id: '2610.02180'
url: https://arxiv.org/abs/2610.02180
pdf_url: https://arxiv.org/pdf/2610.02180
published: '2026-10-01'
collected: '2026-10-03'
category: Other
direction: 可控3D视频生成 · 运动控制
tags:
- Controllable Video Generation
- 3D Motion Control
- LoRA
- Guidance Map
- Single Image To Video
one_liner: 提出GenCine系统，基于单图构建3D支架实现相机与前景运动联合可控的视频生成
practical_value: '- 电商商品3D展示视频制作可参考3D运动手柄+统一世界坐标系方案，避免相机运动时商品运动偏移

  - 对预训练生成模型做可控性适配时，可复用轻量引导分支+LoRA的低成本微调方案，无需全量重训

  - 短视频/广告创意生成场景，可借鉴单图升3D支架的方案，快速自定义相机与主体运动路径，降低制作成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前可控视频生成依赖2D运动轨迹或稀疏拖拽信号，存在歧义性：同一2D轨迹可对应多种3D运动，相机与物体同时运动时控制精度极低。

### 方法关键点
1. 提出GenCine系统，将单张图像升维为可编辑3D场景支架，支持自定义相机路径与前景区域3D运动手柄，无需物理模拟器或类别先验即可实现非刚性运动的分段刚性近似；
2. 设计跨帧统一颜色编码的引导图，将3D控制信号投影到2D对接预训练视频模型，保持世界坐标系一致，实现相机运动下的相对运动控制；
3. 从真实视频恢复控制信号、合成视频取真值轨迹，在预训练Wan模型上微调轻量引导分支与LoRA适配器完成控制对齐。

### 关键结果
相机相对运动一致性显著提升，视角变化下几何一致性明显优化，跨多类真实场景均具备强可控性。
