---
title: '4Director: Controlling Video World Models with Rigid 3D Geometry'
title_zh: 4Director：基于刚性3D几何的视频世界模型控制方法
authors:
- Wei Cao
- Hao Zhang
- Vikram Voleti
- Yuqun Wu
- Mallikarjun B R
- Shimon Vainer
- Mark Boss
- Yaoyao Liu
affiliations:
- Stability AI
- University of Illinois Urbana-Champaign
arxiv_id: '2610.02160'
url: https://arxiv.org/abs/2610.02160
pdf_url: https://arxiv.org/pdf/2610.02160
published: '2026-10-01'
collected: '2026-10-03'
category: Other
direction: 视频世界模型 · 3D运动控制
tags:
- VideoWorldModel
- 3DGeometry
- MotionControl
- AIGC
- EvaluationMetric
- Dataset
one_liner: 提出基于显式4D场景表示的视频世界模型4Director，实现相机与物体运动的精准控制
practical_value: '- 电商商品短视频、广告动效素材生产场景可复用刚性3D几何控制逻辑，实现商品旋转、镜头推拉等精准运镜，避免生成内容中物体形变、视角跳变问题

  - 多视角商品内容生成场景可借鉴Motion Adapter设计，将深度几何骨架转换为符合真实光影、材质一致性的视觉内容，大幅降低素材制作成本

  - 生成类内容效果评估可参考IG-IoU指标思路，同时兼顾动作符合度与主体身份一致性，解决单指标评估偏科问题'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频世界模型对相机、物体运动控制精度低：基于图像平面的cues存在深度、旋转歧义，基于3D轨迹/blob的方案缺少完整几何信息，跨视角一致性差，无法满足专业视频生产的精准控制需求。
### 方法关键点
1. 4Director框架以显式4D场景表示为条件：单张输入图像中每个物体仅重建一次为标准网格，每帧按预设刚性变换移动，避免非观测几何重复生成
2. 配套Motion Adapter模块，将受控场景渲染的深度视频（几何骨架）转换为符合视角一致性的外观、光照、非刚性动态的完整视频
3. 构建包含20774个片段的RealCOD-Rigid数据集，配套自动标注流水线生成刚性3D场景标注；提出IG-IoU评估指标，同时衡量物体运动符合度与身份保留度
### 关键结果
实验显示4Director在视觉质量、相机与物体控制效果上全面优于现有SOTA方法。
