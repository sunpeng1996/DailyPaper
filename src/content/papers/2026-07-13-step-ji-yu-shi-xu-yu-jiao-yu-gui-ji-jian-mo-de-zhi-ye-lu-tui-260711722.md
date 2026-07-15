---
title: 'STEP: Career-Path Recommendation via Temporal and Educational Trajectory Modeling'
title_zh: STEP：基于时序与教育轨迹建模的职业路径推荐系统
authors:
- Iman Johary
- Guillaume Bied
- Alexandru C. Mara
- Tijl De Bie
affiliations:
- AIDA-IDLab, Ghent University, Belgium
arxiv_id: '2607.11722'
url: https://arxiv.org/abs/2607.11722
pdf_url: https://arxiv.org/pdf/2607.11722
published: '2026-07-13'
collected: '2026-07-15'
category: RecSys
direction: 序列推荐 · 职业轨迹预测
tags:
- Sequential Recommendation
- Contrastive Learning
- GRU
- FiLM
- Domain Adaptation
- Representation Learning
one_liner: 提出融合时序与教育信号的职业路径推荐系统STEP及对比预训练框架ROUTE
practical_value: '- 序列推荐场景可复用time-decay GRU建模用户行为时序衰减特性，优化长期行为权重分配

  - 多属性特征融合可借鉴FiLM模块，将用户静态属性（如等级、学历）作为条件动态调制序列特征

  - 垂直领域语义编码可复用ROUTE两阶段训练范式：先无监督领域自适应，再监督对比微调优化表示'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
非结构化、多语言的简历数据长期无法规模化解析用于职业路径建模，现有方案未有效结合时序工作经验、教育背景两类核心信号，下一份职位预测精度无法满足业务需求。
### 方法关键点
1. 搭建STEP推荐框架：集成time-decay GRU建模职业轨迹的时序动态，用FiLM模块以教育背景为条件动态调制序列特征，搭配注意力序列池化筛选任务相关特征；
2. 提出ROUTE两阶段对比预训练范式：先通过无监督去噪自编码将多语言编码器适配职业领域，再引入引导负样本选择做监督对比微调，优化职位语义表示质量。
### 关键结果
在4套职业轨迹数据集（含升级的公开JobHop数据集）上，下一份职位预测性能全面超越SOTA基线，代码与数据集已开源。
