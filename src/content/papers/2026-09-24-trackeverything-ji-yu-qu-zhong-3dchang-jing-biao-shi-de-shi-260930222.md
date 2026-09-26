---
title: 'TrackEverything: Long Horizon Dense Tracking via De-Duplicating 3D Scene Representations'
title_zh: TrackEverything：基于去重3D场景表示的长时序稠密点跟踪
authors:
- Ayush Jain
- Sreeharsha Paruchuri
- Ishita Gupta
- Fan Zhang
- Tanner Schmidt
- Jakob Engel
- Katerina Fragkiadaki
- Adam W. Harley
affiliations:
- Carnegie Mellon University
- Meta
arxiv_id: '2609.30222'
url: https://arxiv.org/abs/2609.30222
pdf_url: https://arxiv.org/pdf/2609.30222
published: '2026-09-24'
collected: '2026-09-26'
category: Other
direction: 3D视觉 · 长时序稠密点跟踪
tags:
- 3D-Tracking
- Dense-Tracking
- Long-Horizon
- Voxelization
- Scene-Representation
one_liner: 提出基于去重3D场景表示的长时序稠密点跟踪器，打破稀疏长时/稠密短时的跟踪权衡
practical_value: '- 基于体素的去重机制可迁移至推荐系统冗余用户行为、重复物品特征的清洗场景，降低存储与计算开销

  - 静态/动态目标拆分处理的思路可复用在用户偏好建模中，分别建模长期静态偏好与短期动态兴趣

  - 3D WAFT用轻量采样替代高内存开销的高维相关计算的思路，可优化RAG、特征检索等场景的内存占用'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有3D点跟踪模型存在固有权衡：要么长时序仅跟踪稀疏查询点，要么仅能在短片段上跟踪所有点，内存开销随视频时长线性增长，无法兼顾长时序、稠密跟踪需求。

### 方法关键点
1. 滑动窗口边界引入基于体素化的去重机制，合并同位置轨迹，避免同表面重复观测的冗余累积；
2. 跟踪任务拆分为端点精炼模块（预测点目的地 + 静/动态分类）+ 轻量轨迹精炼模块，仅对动态点解码稠密轨迹；
3. 提出3D WAFT，用场景云中的高效特征采样替代内存开销极高的4D相关体计算。

### 关键结果数字
首个可在40GB GPU内存内完成1000+帧视频全可见点跟踪的3D跟踪器；在TAPVid-3D数据集上，短片段APD领先所有开源全帧稠密3D跟踪器20%以上，长序列性能与SOTA稀疏跟踪器持平，跟踪点数量远高于后者。
