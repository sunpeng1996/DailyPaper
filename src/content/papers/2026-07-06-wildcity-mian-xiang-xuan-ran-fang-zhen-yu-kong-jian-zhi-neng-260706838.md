---
title: 'WildCity: A Real-World City-Scale Testbed for Rendering, Simulation, and Spatial
  Intelligence'
title_zh: WildCity：面向渲染、仿真与空间智能的真实城市级测试床
authors:
- Xiangyu Han
- Mengyu Yang
- Jiaqi Li
- Bowen Chang
- Ziyu Chen
- Hexu Zhao
- Rahul Kumar Agrawal
- Anthony Rodriguez
- Fiona Hua
- Marco Pavone
affiliations:
- May Mobility
- New York University
- NVIDIA
- Stanford University
arxiv_id: '2607.06838'
url: https://arxiv.org/abs/2607.06838
pdf_url: https://arxiv.org/pdf/2607.06838
published: '2026-07-06'
collected: '2026-07-11'
category: Other
direction: 空间智能 · 城市场景数据集与仿真测试
tags:
- Spatial AI
- Dataset
- 3D Reconstruction
- Embodied Agent
- Neural Rendering
one_liner: 推出覆盖6个城市总里程超1500km的多模态城市场景数据集及配套仿真基线
practical_value: '- 本地生活电商具身Agent可复用城市级空间数据建模的问题拆解思路，优化到店、配送场景的路径推理能力

  - 线下POI推荐、到店导航相关业务团队可参考其多模态空间特征构建逻辑，提升推荐结果的空间合理性

  - 真实场景Agent开发可借鉴其适配真实感知噪声（动态物体、光线变化）的模型鲁棒性评估方案'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
当前基础模型已推动场景重建、具身智能取得较大进展，但缺乏真实城市级数据集，导致AI构建媲美人类的大范围空间表征能力仍存在瓶颈。
### 方法关键点
1. 由自动驾驶车队在复杂真实城市环境采集多模态数据，保留真实感知挑战（动态物体、光线变化、不完美相机位姿）
2. 配套面向城市场景定制的重建基线，将重建结果转换为闭环仿真器
3. 系统性分析可落地城市数字孪生的三大核心挑战：可扩展性、外推性、不确定性
### 关键结果
数据集覆盖6个真实城市，共18条轨迹，单条平均里程83.7km，总里程超1500km，可支撑城市级渲染、空间感知推理等方向研究。
