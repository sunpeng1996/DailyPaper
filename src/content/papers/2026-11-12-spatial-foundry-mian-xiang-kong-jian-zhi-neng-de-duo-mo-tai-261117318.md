---
title: 'Spatial Foundry: A Multimodal Dataset for Spatial Intelligence'
title_zh: Spatial Foundry：面向空间智能的多模态数据集
authors:
- Ethan Lin
- Yang Song
affiliations:
- Ranolabs
arxiv_id: '2611.17318'
url: https://arxiv.org/abs/2611.17318
pdf_url: https://arxiv.org/pdf/2611.17318
published: '2026-11-12'
collected: '2026-11-15'
category: Multimodal
direction: 多模态空间智能数据集构建
tags:
- Multimodal Dataset
- Spatial Intelligence
- 3D Scene
- World Model
- 3D Generation
one_liner: 发布含5280个住宅3D场景的对齐多模态数据集，支撑空间智能与世界模型研究
practical_value: '- 家居电商做3D商品场景化展示、AR试摆业务的团队，可复用其多模态对齐标注规范构建自有商品+场景数据集

  - 做空间交互Agent（如家装设计Agent、线下门店导航Agent）的团队，可直接用该数据集补充世界模型预训练数据

  - AR购物场景研发团队，可参考其统一场景坐标跨视图对齐方案，优化虚拟商品放置的空间一致性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有空间智能研究数据存在两类缺陷：仅提供图像缺少显式几何关联，或标注分散无法在统一参考系下研究外观、相机运动、场景变化的关联关系。
### 方法关键点
1. 构建Spatial Foundry数据集，包含5280个带家具的住宅3D场景配置，覆盖平面图、多视角/全景RGB、度量深度、点云、网格、实例级3D bounding box、相机轨迹+对应视频等对齐多模态数据
2. 采用共享场景坐标关联跨视图、跨时间的所有观测，同时提供可编辑源场景，支持自定义相机路径与受控对象修改
### 关键结果
数据集可支撑平面图条件3D生成、几何重建、实例级感知、相机条件视频生成、世界建模、场景编辑等多方向研究，公开项目页配套提供视频与交互式彩色点云预览。
