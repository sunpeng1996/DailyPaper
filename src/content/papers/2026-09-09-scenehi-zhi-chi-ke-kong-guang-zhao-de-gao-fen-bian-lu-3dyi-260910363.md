---
title: 'SceneHI: High-Resolution 3D-Consistent Scene Texturing with Controllable Illumination'
title_zh: SceneHI：支持可控光照的高分辨率3D一致场景纹理生成框架
authors:
- Athanasios Tragakis
- Marco Aversa
- Daniela Ivanova
- Chaitanya Kaul
- Roderick Murray-Smith
- Daniele Faccio
- Paul Henderson
affiliations:
- University of Glasgow, UK
- Independent Researcher, Switzerland
arxiv_id: '2609.10363'
url: https://arxiv.org/abs/2609.10363
pdf_url: https://arxiv.org/pdf/2609.10363
published: '2026-09-09'
collected: '2026-09-11'
category: Other
direction: 3D场景生成 · 可控光照纹理合成
tags:
- 3D_Generation
- Diffusion_Model
- Texture_Synthesis
- XR
- Digital_Twin
one_liner: 无需微调优化即可直接为3D场景生成高分辨率、3D一致、光照合理的纹理
practical_value: '- 电商3D商品展示/AR试穿场景可复用其2D扩散先验免微调迁移3D纹理的思路，大幅降低高保真3D商品内容生产成本

  - 多视角一致的像素到纹素映射方法可直接嵌入3D内容生产流水线，解决多视角纹理不匹配的常见痛点

  - 光照感知生成通道可直接复用，无需额外后期处理即可生成物理合理的阴影效果，提升3D内容生产效率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
高保真3D纹理是XR、数字孪生、电商3D商品展示的核心基础，但手动制作成本极高，现有3D纹理生成方案普遍存在需微调优化、分辨率低、多视角一致性差、光照效果不符合物理规律等问题，无法适配复杂多物体场景的生产需求。
### 方法关键点
1. 设计精确的像素到纹素分析映射机制，对齐多视角扩散轨迹，严格保证几何一致性；
2. 引入High-Resolution Latent Textures (HRLTs)作为持久画布存储去噪纹理，在潜像素空间执行多视角去噪步骤，高分辨率优化时不破坏多视角一致性；
3. 新增光照感知生成通道，直接在纹理图集嵌入几何一致的真实阴影，无缝对接现有工业生产流。
### 关键结果
相比现有场景级3D纹理生成方法，视觉保真度更高，生成速度降低80%，无需模型微调或优化即可直接生成高分辨率3D纹理。
