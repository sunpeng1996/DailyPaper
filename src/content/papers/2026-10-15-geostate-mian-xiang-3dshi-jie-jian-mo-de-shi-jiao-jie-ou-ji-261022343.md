---
title: 'GeoState: Learning View-Decoupled Geometry States for 3D World Modeling'
title_zh: GeoState：面向3D世界建模的视角解耦几何状态学习方法
authors:
- Hongchang Liu
- Jian Liu
- Yujuan Ding
- Liang Peng
- Xun Jiang
- Fei Ma
- Xing Xu
- Yi Bin
affiliations:
- Tongji University
- Hong Kong Polytechnic University
- Tencent
- Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ)
arxiv_id: '2610.22343'
url: https://arxiv.org/abs/2610.22343
pdf_url: https://arxiv.org/pdf/2610.22343
published: '2026-10-15'
collected: '2026-10-19'
category: Other
direction: 3D世界建模 · 几何表征学习
tags:
- 3D_World_Modeling
- Geometry_Representation
- View_Decoupling
- Autoregressive_Prediction
- Embodied_AI
one_liner: 提出视角解耦几何表征GeoState，解决3D世界建模视角依赖导致的状态演化预测难问题
practical_value: '- 涉及AR/VR电商场景3D商品/门店建模的团队，可借鉴视角解耦表征思路，消除不同拍摄视角的特征扰动，提升3D表征的跨视角一致性

  - 多视角特征融合场景（如用户实拍UGC的3D商品重建、多直播间同品特征对齐）可复用多视角特征聚合为统一状态的tokenizer架构

  - 做具身Agent、线下无人配送场景环境预测的团队，可参考场景状态与相机运动分离建模的框架，降低未来状态预测的复杂度'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有3D世界模型基于几何基础模型（GFM）的特征存在视角依赖问题，将场景动态与相机引入的变化耦合，大幅提升了状态演化的预测难度。
### 方法关键点
1. 设计场景tokenizer聚合多视角GFM特征，生成与视角解耦的统一场景状态；
2. 几何解码器基于相机光线查询即可输出对应视角的结果，将相机运动与场景状态演化分开建模；
3. 采用自回归世界模型预测未来场景状态，推理全程保持统一上下文派生尺度，无需逐帧尺度对齐。
### 关键结果
在Waymo数据集上性能优于此前最优3D世界模型，支持几何一致的跨视角查询，可零样本泛化到KITTI和nuScenes数据集。
