---
title: 'CLUIE: Clustering-Aware Recurrent Propagation with Local Structural Compensation
  for Underwater Image Enhancement'
title_zh: CLUIE：融合聚类感知循环传播与局部结构补偿的水下图像增强
authors:
- Kui Jiang
- Zefan Feng
- Laibin Chang
- Yan Luo
- Junjun Jiang
- Xiaopeng Fan
arxiv_id: '2607.21467'
url: https://arxiv.org/abs/2607.21467
pdf_url: https://arxiv.org/pdf/2607.21467
published: '2026-07-23'
collected: '2026-07-26'
category: Other
direction: 水下图像增强 · 自适应RWKV序列建模
tags:
- RWKV
- Image Enhancement
- Dynamic Token Reordering
- Clustering
- Local Structure Compensation
one_liner: 提出聚类感知RWKV框架CLUIE，适配异质退化模式实现高性能水下图像自适应增强
practical_value: '- 核心为水下图像增强领域学术贡献，电商/搜推/Agent业务直接可借鉴点有限

  - 若业务中采用RWKV做长序列建模，可参考语义聚类动态调整token顺序的优化思路

  - 动态重排序列导致局部结构损失的问题，可复用局部分支补全结构信息的设计思路'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
水下图像受波长相关的光吸收、散射、后向散射影响，普遍存在颜色失真、对比度下降、细节丢失问题，且同图内不同区域退化模式异质，需要区域自适应修复；传统视觉RWKV采用固定扫描顺序，与内容无关，无法适配空间非均匀的修复需求。

### 方法关键点
1. 设计聚类感知语义动态重排序（CSDR）模块，按语义特征相似度对token分组，基于簇间上下文关系生成动态遍历顺序，让WKV状态沿语义相关区域而非固定空间/光谱顺序累积；
2. 提出暗响应调制局部传播（DMLP）模块，通过深度可分离卷积提取局部结构响应，基于邻域感知伪暗响应图自适应调制传播强度，补偿动态重排序破坏的原始空间邻域局部连续性。

### 关键结果
在多个水下图像增强基准数据集上取得SOTA定量性能，视觉质量显著优于现有方案，同时具备优异的计算效率。
