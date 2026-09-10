---
title: 'RelightFormer: Feed-forward Generative Transformer for Multiview Object Relighting'
title_zh: RelightFormer：用于多视角物体重光照的前馈生成式Transformer
authors:
- Hejun Wang
- Jinxi Li
- Junwei Jiang
- Shiwei Mao
- Hu Cheng
- Shouwang Huang
- Bo Yang
affiliations:
- Shenzhen Research Institute, The Hong Kong Polytechnic University
arxiv_id: '2609.07414'
url: https://arxiv.org/abs/2609.07414
pdf_url: https://arxiv.org/pdf/2609.07414
published: '2026-09-06'
collected: '2026-09-10'
category: Multimodal
direction: 多视角图像重光照 · 生成式Transformer
tags:
- Transformer
- Generative Model
- Multi-view
- Image Rendering
- Foundation Model
one_liner: 提出基于视频基础模型的前馈生成Transformer，实现高保真多视角物体重光照
practical_value: '- 电商商品素材制作场景可直接复用该模型生成不同光照下的商品图，无需额外拍摄，大幅降低素材生产成本

  - 3D商品展示、AR购等交互场景可快速生成任意光照下的多视角商品渲染图，提升用户消费决策效率

  - 电商直播场景可接入该模型，基于多视角摄像头输入实时调整商品光照效果，优化直播观感'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统图像重光照方案存在两类缺陷：依赖复杂逆渲染管线的方案面临病态优化问题；单视图生成模型忽略多视角下3D几何、材质交互等关键线索，生成真实度不足。
### 方法关键点
1. 基于视频基础模型改造前馈生成式Transformer，跳过显式固有属性估计，直接实现单/多视图图像重光照
2. 设计隐式光照模块，通过交叉注意力将目标环境光照动态注入空间特征
3. 采用排列不变位置编码，对称处理无序多视角输入，无序列偏差
4. 构建包含90K物体、39K唯一光照的大规模Laval Objaverse Dataset（LOD）用于模型训练
### 关键结果
在单视图、多视图、新视图重光照任务上均达到SOTA视觉质量与photorealistic效果，零样本泛化表现优异
