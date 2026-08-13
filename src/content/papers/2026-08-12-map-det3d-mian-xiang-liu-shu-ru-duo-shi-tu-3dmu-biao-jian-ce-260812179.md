---
title: 'Map-Det3D: Metric Feed-Forward 3D Reconstruction Prior for Multi-view 3D Object
  Detection from Streaming Inputs'
title_zh: Map-Det3D：面向流输入多视图3D目标检测的前馈3D重建先验
authors:
- Yung-Hsu Yang
- Luigi Piccinelli
- Samuel Rota Bulò
- Sunghwan Hong
- Denis Rozumny
- Johannes Schönberger
- Zuria Bauer
- Hermann Blum
- Peter Kontschieder
- Marc Pollefeys
affiliations:
- ETH Zürich
- Meta Reality Labs Zürich
- University of Bonn
arxiv_id: '2608.12179'
url: https://arxiv.org/abs/2608.12179
pdf_url: https://arxiv.org/pdf/2608.12179
published: '2026-08-12'
collected: '2026-08-13'
category: Agent
direction: 具身Agent · 3D环境感知
tags:
- 3D Object Detection
- Embodied Agent
- Metric Reconstruction
- Multi-view Perception
- Streaming Input
one_liner: 基于前馈度量3D重建骨干，跳过2D转3D实现流输入多视图鲁棒3D目标检测
practical_value: '- 做AR/VR电商具身导购Agent时，可复用该跳过2D转3D的感知架构，降低纯视觉3D商品定位的域迁移误差

  - 多模态场景理解任务中，可借鉴「将通用重建预训练模型微调为目标感知骨干」的范式，减少下游任务标注成本

  - 流输入连续感知场景（如直播内容3D结构化）可复用短时间窗口多视图映射的时序信息融合方法'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
具身Agent 3D目标检测当前多依赖LiDAR等深度传感器，成本、功耗高；纯单目方案采用2D检测后升维3D的范式，存在深度、绝对尺度约束不足问题，相机、环境域迁移时性能衰减严重。
### 方法关键点
1. 提出Map-Det3D在线多视图3D检测框架，直接在RGB重建的3D空间完成检测，跳过传统2D转3D步骤；
2. 基于短时间窗口多视图映射，复用前馈度量3D重建模型作为几何骨干，微调增强其目标感知能力；
3. 直接在度量3D空间输出检测框，规避升维过程的误差累积。
### 关键结果
多基准测试验证该方案在线性能优异，无需额外适配即可实现鲁棒跨域迁移，证明重建先验是单目视频稳定3D检测的可行路径。
