---
title: 'MicroZoom: Structure-Preserving Detail Synthesis at Extreme Scale'
title_zh: MicroZoom：极端尺度下保留结构的细节合成框架
authors:
- Huy Huynh
- Jingwei Ma
- Brian Curless
- Ira Kemelmacher-Shlizerman
- Steven M. Seitz
affiliations:
- University of Washington, USA
arxiv_id: '2607.24729'
url: https://arxiv.org/abs/2607.24729
pdf_url: https://arxiv.org/pdf/2607.24729
published: '2026-07-27'
collected: '2026-07-29'
category: Other
direction: 极端超分辨率 · 十亿像素图像生成
tags:
- Super-Resolution
- Gigapixel Synthesis
- Two-stage Network
- Texture Generation
- Reference-based Generation
one_liner: 采用两阶段级联设计结合分割掩码，实现最高350倍、十亿像素级的参考式极端超分辨率生成
practical_value: '- 电商商品素材生产可复用两阶段级联生成思路：先保证面料、珠宝等商品的全局纹理结构一致，再补局部高清细节，降低专业高清拍摄成本

  - 多模态商品素材生成场景可借鉴分割掩码引导边界合成的trick，解决不同材质/部件拼接处的纹理失真问题

  - AR试穿、商品3D展示等需极端放大材质的场景，可参考少量参考图生成全局高分辨率素材的方案，减少3D扫描成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有极端尺度超分辨率（最高350倍放大）存在两大核心痛点：一是模糊材质边界处难以恢复符合真实材质特性的细节，二是百万级局部预测难以保证全局大尺度结构（如织物编织重复纹理）的一致性，无法基于普通消费级照片加少量显微参考图生成全局连贯的十亿像素级图像。
### 方法关键点
采用两阶段级联生成框架：第一阶段优先恢复全局图案一致性，避免局部生成破坏大尺度结构；第二阶段细化局部纹理细节，同时引入分割掩码引导模糊边界处的合成，保证生成内容对齐真实参考的材质特征。
### 关键结果
可实现最高350倍放大的十亿像素级图像生成，在自采集的日常物体数据集上验证，生成结果全局结构连贯、材质细节符合真实参考，可支撑物体全范围微观纹理的探索式可视化。
