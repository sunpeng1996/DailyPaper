---
title: 'SparseGraph-I2P: Consistency-Guided Hypothesis Selection for Efficient Image-to-Point-Cloud
  Registration'
title_zh: SparseGraph-I2P：一致性引导假设选择的高效图像到点云配准方法
authors:
- Ziyang Yu
- Xiang Li
- Qiong Chang
- Jun Miyazaki
affiliations:
- Institute of Science Tokyo
- Nanjing University
arxiv_id: '2611.04591'
url: https://arxiv.org/abs/2611.04591
pdf_url: https://arxiv.org/pdf/2611.04591
published: '2026-11-03'
collected: '2026-11-07'
category: Other
direction: 3D视觉 · 图像到点云配准优化
tags:
- Image-to-Point-Cloud-Registration
- Sparse-Graph
- Depth-Aware-Filtering
- Pose-Estimation
- Coarse-to-Fine-Matching
one_liner: 提出融合深度兼容性的粗假设图与稀疏精匹配策略，实现高召回低延迟的I2P配准
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有粗到精I2P配准方案存在两难：要么丢弃模糊但正确的patch对导致召回低，要么保留过多候选引发重叠patch重复精匹配，算力浪费严重。
### 方法关键点
1. 构建Coarse Hypothesis Graph，融合外观特征与深度衍生的一/二阶兼容性，按固定预算筛选patch对，提升正确候选占比
2. 设计Sparse Fine Matching策略，每个查询像素仅解码一次，跳过同点云区域已匹配祖先patch覆盖的像素-点对比计算
3. 传感器深度场景下用SC2谱支持度排序对应关系，单轮EPnP求解位姿；单目深度场景下先基于对应几何校准深度再过滤
### 关键结果
- 传感器深度输入：在RGB-D Scenes V2、7-Scenes数据集上，取得所有对比方法中最高配准召回率与最低延迟
- 单目预测深度输入：在RGB-D Scenes V2上仍保持最高召回率，仅增加少量校准开销
