---
title: 'FoundSurface: Feedforward Ray-Based 3D Scene Surface Reconstruction from Unposed
  Images'
title_zh: FoundSurface：基于前馈光线的无位姿图像3D场景表面重建
authors:
- Shenxing Wei
- Jinxi Li
- Zihui Zhang
- Ajay Kumar
- Wei Wang
- Bo Yang
affiliations:
- vLAR Group, The Hong Kong Polytechnic University
- DSAI, The Hong Kong Polytechnic University
- Regressor, Inc.
arxiv_id: '2611.34128'
url: https://arxiv.org/abs/2611.34128
pdf_url: https://arxiv.org/pdf/2611.34128
published: '2026-11-24'
collected: '2026-11-26'
category: Other
direction: 3D视觉 · 无位姿3D表面重建
tags:
- 3D_Reconstruction
- Zero_Shot
- FeedForward
- Computer_Vision
- Foundation_Model
one_liner: 融合点图与光线表示的无位姿3D表面重建管线，零样本泛化表现远超现有SOTA基线
practical_value: '- 若业务涉及电商3D商品建模、AR试穿/AR逛街场景，可复用其无需相机位姿的3D表面重建管线，大幅降低商品3D素材制作成本

  - 「预训练先验提取→相关参考筛选→粗结果生成→局部细节精细化」的四阶段架构可迁移至多模态内容生成、多模态特征融合类任务的Pipeline设计

  - 基于surfel投票机制的相关参考视图筛选思路可复用在多模态召回、多模态检索的相关性过滤环节'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
无位姿图像的高精度3D表面重建是计算机视觉基础难题，现有前馈点图类方法无需相机位姿，但仅能生成离散稀疏表示，精度与细节表现不足。
### 方法关键点
1. 先通过预训练点图模型提取显式几何先验
2. 采用查询视图中心选择模块，通过surfel投票机制筛选几何相关的参考视图
3. 交叉注意力回归器关联目标查询光线与参考特征，输出连续粗表面
4. 基于raylet的模块聚合局部3D特征，补全高频细节与解析法向量
### 关键结果
在9个异构数据集上训练为单基础模型，在6个未见过的数据集上零样本泛化表现优异，几何精度与细节保留能力显著超越现有SOTA基线。
