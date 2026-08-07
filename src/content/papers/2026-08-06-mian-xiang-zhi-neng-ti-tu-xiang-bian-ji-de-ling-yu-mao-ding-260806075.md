---
title: 'Domain-Grounded Candidate Selection for Agentic Image Editing: A Shadow Removal
  Case'
title_zh: 面向智能体图像编辑的领域锚定候选选择方法：以去阴影任务为例
authors:
- Shilin Hu
- Jingyi Xu
- Dimitris Samaras
- Hieu Le
affiliations:
- Stony Brook University
- UNC Charlotte
arxiv_id: '2608.06075'
url: https://arxiv.org/abs/2608.06075
pdf_url: https://arxiv.org/pdf/2608.06075
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: 智能体图像编辑 · 领域先验约束生成
tags:
- Agentic_Editing
- Candidate_Selection
- Physics_Prior
- Image_Editing
- Shadow_Removal
one_liner: 提出融合物理先验的智能体候选筛选流水线，解决商用生成编辑去阴影的幻觉问题，性能超SOTA 47%
practical_value: '- 生成类业务可复用「多候选生成+先验规则筛选+最优选择+失败重试」的Agent流水线，有效降低大模型幻觉，可直接落地电商主图修图、商品文案生成、广告素材创作等场景

  - 垂类场景无需微调大模型，仅需将领域原生物理/业务规则注入生成、评估环节的prompt，即可大幅提升输出的合规性与准确性，适合缺少标注数据的小众垂类需求

  - 对生成结果的校验环节可加入轻量失败重试逻辑，仅增加极少量调用成本即可获得生成质量的显著提升，可迁移到AI商品图修复、海报自动生成等业务'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
商用多模态生成编辑器做去阴影等低阶视觉任务时，易出现内容幻觉、误判阴影为材质/几何结构的问题，输出看似合理但不符合物理规律，且低阶视觉任务成对标注数据规模化采集难度极高。
### 方法关键点
1. 搭建Agent式候选筛选流水线：编辑器生成引导探测结果，评估器筛查严重错误，失败自动重试，多候选采样后过滤，最终选择兼顾去阴影效果与场景还原度的最优结果；
2. 引入阴影形成物理先验约束生成、评估阶段的prompt，明确要求模型将阴影视为光照遮挡效应而非物体本身属性。
### 关键结果
在ShadowRemovalRefine基准上CDD达0.0075，相比此前最优方法CDD降低至少47%，验证了垂类领域先验对通用生成模型的约束价值远高于直接调用大模型
