---
title: Embodied Active Learning under Limited Annotation and Navigation Budget for
  Object Detection
title_zh: 有限标注与导航预算约束下的目标检测具身主动学习
authors:
- Hadrien Crassous
- Mohamed Yassine Kabouri
- Minahil Raza
- Joni Pajarinen
- Riad Akrour
arxiv_id: '2607.15974'
url: https://arxiv.org/abs/2607.15974
pdf_url: https://arxiv.org/pdf/2607.15974
published: '2026-07-17'
collected: '2026-07-21'
category: Agent
direction: 具身Agent · 主动学习优化
tags:
- Embodied AI
- Active Learning
- Object Detection
- Budget Constraint
- Robot Navigation
one_liner: 提出基于空间不一致性的具身批量主动学习方案，在双预算约束下优化未知环境目标检测效果
practical_value: '- 线下商品盘点/机器人巡检类业务可复用空间不一致性筛选高价值标注样本的思路，大幅降低标注成本

  - 双预算约束下的样本+采集路径联合选择框架，可迁移到有限算力/流量预算的推荐主动学习场景，优先选择对模型提升最大的样本做标注/AB实验

  - 无监督筛选模型表现不稳定样本的逻辑，可用于LLM/多模态模型微调，有限标注预算下最大化微调效率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
预训练目标检测器落地未知具身场景时，同时面临机器人导航耗时高、人工标注成本贵的双重约束，现有主动学习方案未同时兼顾两类预算限制，适配新场景效率低下。
### 方法关键点
1. 提出具身批量主动学习范式，每轮迭代同步在有限导航预算下选择最优采集轨迹、在有限标注预算下选择高价值图像重训检测器，定向优化模型失败case
2. 基于空间一致性识别标注不一致的图像，这类样本对视觉模型提升效果最优，无需外部监督即可完成筛选
### 关键结果
在AI2-THOR仿真大场景、波士顿动力Spot实体机器人搭载YOLOv5的真实场景下测试，相同导航与标注预算条件下，相比多个基线方案检测精度达到最优。
