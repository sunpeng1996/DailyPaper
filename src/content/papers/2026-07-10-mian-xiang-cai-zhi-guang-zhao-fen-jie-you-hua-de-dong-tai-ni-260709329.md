---
title: Dynamic Inverse Rendering for Enhanced Material-Lighting Decomposition
title_zh: 面向材质-光照分解优化的动态逆渲染方法
authors:
- Raza Yunus
- Benjamin Ummenhofer
- Jan Eric Lenssen
- Eddy Ilg
affiliations:
- University of Technology Nuremberg
- Intel
- Max Planck Institute for Informatics
- Google
arxiv_id: '2607.09329'
url: https://arxiv.org/abs/2607.09329
pdf_url: https://arxiv.org/pdf/2607.09329
published: '2026-07-10'
collected: '2026-07-13'
category: Other
direction: 3D视觉 · 逆渲染材质光照分解
tags:
- Inverse Rendering
- 3D Reconstruction
- Relighting
- Material Decomposition
- Dynamic Capture
one_liner: 利用刚体运动的多光照交互约束优化逆渲染，实现更精准的材质-光照解耦
practical_value: '- 电商3D商品素材生产可复用该动态采集方案，仅需普通手持RGB视频即可完成商品材质光照解耦，无需专业多光照采集棚，大幅降低3D素材制作成本

  - AR试穿/试戴场景可接入该管线，快速还原商品真实物理材质，支持虚拟环境下的实时重光照，提升用户交互体验

  - 商品营销内容生成场景中，解耦后的独立材质、光照资产可直接用于生成不同场景下的商品宣传图，减少后期修图工作量'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
逆渲染的材质-光照分解是重光照、AR应用的核心基础，但该问题天然病态，多组材质光照组合可生成相同观测颜色，传统静态多视角采集易出现两者纠缠，解耦效果差。

### 方法关键点
1. 借助刚体运动物体的多帧观测，获取多样化表面-光照交互约束，消解分解歧义；
2. 融合目标跟踪、3D重建与逆渲染能力，构建通用刚体运动物体的可重光照处理管线。

### 关键结果
合成数据实验中，刚体运动观测下的材质重建精度显著优于静态观测；真实手持物体RGB视频测试中，即使存在真实环境噪声，管线仍保持性能优势。
