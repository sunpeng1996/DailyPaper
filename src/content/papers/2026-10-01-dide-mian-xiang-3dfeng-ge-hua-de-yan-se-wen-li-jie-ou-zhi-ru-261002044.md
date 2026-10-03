---
title: DiDE:Direct Injection with Color-Texture DEcoupling for 3D Stylization
title_zh: DiDE：面向3D风格化的颜色纹理解耦直接注入方法
authors:
- Tao Wu
- Alexandra Gomez-Villa
- Senmao Li
- Yaxing Wang
- Joost van de Weijer
- Kai Wang
affiliations:
- Computer Vision Center, Universitat Autònoma de Barcelona (Spain)
- Mohamed bin Zayed University of Artificial Intelligence (UAE)
- Jilin University (China)
- City University of Hong Kong (Dongguan, China)
arxiv_id: '2610.02044'
url: https://arxiv.org/abs/2610.02044
pdf_url: https://arxiv.org/pdf/2610.02044
published: '2026-10-01'
collected: '2026-10-03'
category: Other
direction: 3D生成 · 风格化属性解耦
tags:
- 3D Stylization
- Training-free
- Disentangled Representation
- Generative Model
- Attribute Control
one_liner: 首个免训练可独立控制颜色纹理的3D风格化框架DiDE，多指标优于现有2D/3D基线
practical_value: '- 电商3D商品个性化生成场景可复用免训练通道拆分机制，无需重训3D生成模型即可独立调整商品颜色、纹理属性，降低定制化成本

  - 商品3D素材生产可借鉴颜色纹理分离注入逻辑，分别批量修改同一款商品的配色、纹理款式，快速生成多SKU对应的3D素材

  - AR试穿/虚拟展厅场景可套用该框架实现用户自定义商品外观，支持用户上传面料、配色参考实时生成对应3D商品'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有基于整流流的image-to-3D风格化方法只能整体迁移参考图视觉属性，无法独立控制颜色、纹理的迁移效果，限制了3D资产生成的灵活性。

### 方法关键点
1. 发现image-to-3D模型的隐空间过完备，纹理信息仅占用少部分风格相关通道，剩余空间可独立编码颜色信息
2. 设计通道拆分机制，内容图、纹理参考、颜色参考分别走专用分支，在每个自注意力层无干扰融合两种风格信号，全程保留内容几何结构
3. 无需训练原有3D生成模型，即可实现解耦3D风格化

### 关键结果
在自建的多参考基准Disen3D-Bench上测试，DiDE在颜色保真度、纹理迁移效果、内容保留度三个核心指标上均优于现有2D、3D风格化基线
