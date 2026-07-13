---
title: 'PanoWorld: Real-World Panoramic Generation'
title_zh: PanoWorld：真实场景全景内容生成框架
authors:
- Haoyuan Li
- Dizhe Zhang
- Yuemei Zhou
- Xiangkai Zhang
- Haoran Feng
- Xiaofan Lin
- Wenjie Jiang
- Bo Du
- Ming-Hsuan Yang
- Lu Qi
affiliations:
- Insta360 Research
- Institute of Automation Chinese Academy of Sciences
- Tsinghua University
- Wuhan University
- UC Merced
arxiv_id: '2607.09661'
url: https://arxiv.org/abs/2607.09661
pdf_url: https://arxiv.org/pdf/2607.09661
published: '2026-07-09'
collected: '2026-07-13'
category: Multimodal
direction: 多模态生成 · 全景世界模型
tags:
- Panoramic Generation
- World Model
- Memory Augmentation
- 3D Vision
- Dataset Construction
one_liner: 利用全向表征旋转等变特性优化全景世界模型长程记忆，搭配专属数据集实现高精度可控全景生成
practical_value: '- 电商全景逛店、3D商品展示场景的内容生成，可复用DPRC+GMA几何感知记忆增强方案，提升长序列场景生成的物理一致性

  - 构建垂直领域生成模型评测数据集时，可参考「真实采集+仿真生成」的混合思路，覆盖现有数据集缺失的极端、稀缺场景

  - 具身Agent导航、空间交互类应用的世界建模，可借鉴将旋转转化为隐式几何变换、简化相机轨迹为平移的处理思路，降低轨迹建模复杂度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有全景世界模型长程记忆能力不足，大空间变换、复杂光照场景下生成内容物理一致性差，且现有评测数据集场景偏稳定，无法覆盖真实复杂环境。
### 方法关键点
1. 利用全向表征旋转等变特性，将旋转作为隐式几何变换，通过固定朝向把相机轨迹简化为平移
2. 设计Dense Panoramic Ray-Conditioning (DPRC)、Geometry-aware Memory Augmentation (GMA)模块，分别优化当前动作建模与长程记忆
3. 采用三阶段渐进式训练pipeline逐组件优化，同时构建混合真实采集+仿真生成的World360大规模评测数据集
### 关键结果
在World360数据集上效果大幅领先现有对比方案，可实现复杂运动下高精度轨迹控制，且生成内容保持高保真度与物理一致性。
