---
title: 'ADATEX4D: adaptive texture capacity allocation for 4D gaussian splatting'
title_zh: AdaTex4D：面向4D高斯溅射的自适应纹理容量分配方法
authors:
- De Jiang
- Peiqiang Wang
- Kehong Yuan
- Shaohua Ma
affiliations:
- Tsinghua Shenzhen International Graduate School, Tsinghua University
arxiv_id: '2609.29963'
url: https://arxiv.org/abs/2609.29963
pdf_url: https://arxiv.org/pdf/2609.29963
published: '2026-09-24'
collected: '2026-09-27'
category: Other
direction: 4D高斯溅射 · 高效纹理表示优化
tags:
- 4D_Gaussian_Splatting
- adaptive_allocation
- texture_optimization
- memory_efficiency
- novel_view_synthesis
one_liner: 提出4D高斯溅射自适应纹理分配模块，保重建质量前提下纹理存储减半
practical_value: '- 自适应差异化资源分配思路可迁移到搜推场景：替代全局统一配置，针对高价值对象（高曝光item、高转化query）分配更多存储/计算资源

  - 多维度加权的动态调度规则设计逻辑，可复用在Embedding维度自适应调优、链路算力优先级调度等业务场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
带纹理的4D高斯溅射可有效提升局部外观表达能力，但所有基元采用统一纹理分辨率的方案，会在低细节、弱可见区域造成大量存储冗余，固定全局分辨率无法兼顾高细节区域表达需求与整体内存效率。
### 方法关键点
1. 设计面向形变类4D高斯溅射的自适应纹理容量分配模块，每个高斯单元携带打包RGBA三平面纹理，两个轴的分辨率可独立动态调整
2. 分辨率调整依据为经可见性归一化的屏幕空间梯度、形变后的局部尺度两个指标，实现各向异性的动态纹理容量分配
### 关键结果数字
在N3DV、PanopticSports数据集上，纹理存储减少50%以上同时完全保留重建质量；固定内存预算下，重建质量优于统一纹理分配方案，同时降低整体模型内存与峰值内存。
