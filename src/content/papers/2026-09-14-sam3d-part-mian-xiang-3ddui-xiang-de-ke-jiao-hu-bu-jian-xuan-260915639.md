---
title: 'SAM3D-Part: Interactive Part Selection and Generation from 3D Objects'
title_zh: SAM3D-Part：面向3D对象的可交互部件选择与生成框架
authors:
- Jiahao Chang
- Dong Du
- Wanhu Sun
- Yujian Zheng
- Chuanyu Pan
- Bowen Zhao
- Chongjie Ye
- Yuanming Hu
- Xiaoguang Han
affiliations:
- CUHKSZ
- Meshy AI
- Nanjing University of Science and Technology
- MBZUAI
- GenuX
arxiv_id: '2609.15639'
url: https://arxiv.org/abs/2609.15639
pdf_url: https://arxiv.org/pdf/2609.15639
published: '2026-09-14'
collected: '2026-09-15'
category: Other
direction: 3D可控生成 · 提示驱动部件级生成
tags:
- 3D Generation
- Promptable Generation
- Mesh Processing
- Controllable Generation
- Part Cache
one_liner: 提出提示驱动的3D部件选择性生成框架，可输出对齐原模型的完整可复用部件网格
practical_value: '- 电商3D商品建模场景可复用该框架的部件级生成能力，快速生成同商品多属性局部变体（如不同材质的包带、不同款式的家具腿），降低3D资产制作成本

  - 多轮交互式生成任务可借鉴其part cache机制，缓存历史生成组件作为上下文约束，减少多轮生成结果冲突，提升输出一致性

  - 多模态条件生成任务可参考其像素级通道融合方案，对齐异构特征（几何、视觉、掩码），提升生成结果与输入条件的匹配精度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
3D资产生产流程中用户常仅需特定部件而非完整模型，现有方法存在三类缺陷：生成全量部件不符合用户意图，提示式3D分割仅输出不完整曲面不可复用，图像条件的部件生成难以保留隐藏几何与对齐精度。
### 方法关键点
1. 将源mesh编码为紧凑特征，通过像素级通道融合对齐渲染图像、选择掩码、点云观测特征，基于融合特征前馈生成查询部件的完整mesh
2. 预测稠密体素对应关系，从分布式空间证据估计部件变换实现源坐标系对齐，无需依赖单一全局姿态编码
3. 新增part cache缓存历史生成部件作为上下文约束，降低多部件连续查询的结果冲突
### 关键结果
在3D部件生成任务上达到SOTA，大幅提升源模型对齐度，降低条件输入成本，支持连续一致的选择性部件生成
