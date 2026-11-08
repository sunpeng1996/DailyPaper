---
title: Multimodal Hierarchical Mixture-of-Experts for 3D Medical Vision-Language Modeling
title_zh: 面向3D医疗视觉语言建模的多模态层级混合专家模型
authors:
- Gizem Mert
- Szymon Płotka
- Pedro R. A. S. Bassi
- Wenxuan Li
- Zongwei Zhou
- Jarosław B. Ćwikła
- Arkadiusz Sitek
- Ewa Szczurek
affiliations:
- Helmholtz Munich
- Technical University of Munich
- Johns Hopkins University
- Harvard Medical School
- University of Warsaw
arxiv_id: '2611.08185'
url: https://arxiv.org/abs/2611.08185
pdf_url: https://arxiv.org/pdf/2611.08185
published: '2026-11-05'
collected: '2026-11-08'
category: Multimodal
direction: 3D医疗多模态 · 层级MoE建模
tags:
- MoE
- Multimodal
- Contrastive-Learning
- Vision-Language
- Hierarchical-Modeling
one_liner: 提出融合层级双模态SMoE与对比学习的3D医疗多模态框架MedHiVE，性能超越11种现有SOTA
practical_value: '- 可复用双层SMoE路由架构，针对电商多粒度用户/商品特征设计局部+全局两层专家，提升特征适配效率

  - 双粒度对比对齐方案可迁移至多模态推荐场景，同时对齐商品细粒度属性与全局语义表征

  - 动态槽位式跨模态信息流设计，可优化图文/短视频多模态召回阶段的特征融合效果'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有3D医疗视觉语言模型忽略数据天然的层级结构，无法聚焦临床相关解剖区域，静态特征池化、仅视觉侧层级路由的方案效果存在瓶颈。
### 方法关键点
1. 设计按解剖尺度组织的双层Soft Mixture-of-Experts（SMoE）架构，对视觉、文本token同时做动态路由
2. 采用局部SMoE处理单模态细粒度特征、全局SMoE融合生成统一多模态表征的两级流程
3. 新增解剖层级+全局双粒度对比学习任务，对齐不同尺度的跨模态表征
### 关键结果
在25000+带解剖标注CT数据上预训练后，在6个数据集的分割、分类、检测3类任务上，稳定超越11个SOTA方法
