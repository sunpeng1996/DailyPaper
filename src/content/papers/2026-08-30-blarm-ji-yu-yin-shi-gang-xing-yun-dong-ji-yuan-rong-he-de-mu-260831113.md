---
title: 'BLARM: Animating 3D Objects from Video via Blending Latent Rigid Motion Primitives'
title_zh: BLARM：基于隐式刚性运动基元融合的单目视频3D物体动画生成方法
authors:
- Pradyumn Goyal
- Yizhak Ben-Shabat
- Hsueh-Ti Derek Liu
- Haomiao Jiang
- Snehasish Mukherjee
- Kyle Spence
- Mark Stauber
- Evangelos Kalogerakis
- Yunze Zeng
affiliations:
- Roblox
- UMass Amherst
- TU Crete
arxiv_id: '2608.31113'
url: https://arxiv.org/abs/2608.31113
pdf_url: https://arxiv.org/pdf/2608.31113
published: '2026-08-30'
collected: '2026-09-02'
category: Other
direction: 3D内容生成 · 视频驱动网格动画
tags:
- 3D_Animation
- Latent_Representation
- Spatial-Temporal_Attention
- Contrastive_Learning
- Mesh_Deformation
one_liner: 无需显式绑定标注，仅用单目视频即可驱动静态3D网格生成时序一致动画的前馈方法
practical_value: '- 电商3D商品动态展示场景可复用低维形变表示思路，无需人工绑定骨骼即可通过实拍视频快速生成3D商品动态素材，大幅降低内容制作成本

  - 时序类生成任务可借鉴因子化时空注意力架构，降低跨模态特征对齐的计算开销，同时提升输出结果的时序稳定性

  - 虚拟人/数字人动作生成任务可复用运动感知对比学习+熵正则的训练策略，减少高维动作预测的跳变问题，提升结果连贯性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有3D网格动画生成高度依赖骨骼、蒙皮权重等人工标注，直接回归顶点运动维度高、时序一致性差，无法满足4D内容低成本快速生成的业务需求。
### 方法关键点
1. 采用可学习时变刚性运动组件+时不变顶点-组件蒙皮权重表示动画，构造无骨架、无人工标注的低维形变空间，大幅降低运动预测的维度
2. 通过因子化时空注意力实现几何形变隐变量与视频特征的跨模态对齐，经预测蒙皮权重融合刚性变换后解码得到完整动画序列
3. 训练组合采用轨迹重建损失、熵正则、运动感知对比学习三类损失，兼顾动画准确性、时序稳定性与运动结构可解释性
### 关键结果
无需任何绑定、骨架类标注即可从单目视频生成时序连贯的3D动画，时序稳定性、重建精度均优于现有SOTA方法，输出的隐式运动结构可直接用于后续编辑
