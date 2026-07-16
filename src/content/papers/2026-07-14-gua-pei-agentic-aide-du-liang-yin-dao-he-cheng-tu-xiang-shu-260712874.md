---
title: Metric-Guided Synthetic Image Data Rendering for Deep Learning compatible with
  Agentic AI
title_zh: 适配Agentic AI的度量引导合成图像数据渲染方法
authors:
- Martina Radoynova
- Samuel Pantze
- Trina De
- Ulrik Günther
- Artur Yakimovich
affiliations:
- Center for Advanced Systems Understanding (CASUS), Görlitz, Germany
- Helmholtz-Zentrum Dresden-Rossendorf e. V. (HZDR), Dresden, Germany
- Institute of Computer Science, University of Wrocław, Wrocław, Poland
- Cluster of Excellence Physics of Life, TU Dresden, Dresden, Germany
arxiv_id: '2607.12874'
url: https://arxiv.org/abs/2607.12874
pdf_url: https://arxiv.org/pdf/2607.12874
published: '2026-07-14'
collected: '2026-07-16'
category: Agent
direction: Agent技能封装 合成数据生成优化
tags:
- Synthetic Data
- Agent Skill
- Domain Gap
- Data Rendering
- Object Detection
one_liner: 提出度量引导的合成图像渲染工具包GraNatPy，及Agent自动优化技能SynthClaw缩小虚实数据域差
practical_value: '- 生成电商/广告业务合成训练数据时，可借鉴量化度量引导优化的思路，替代主观视觉评估，有效降低域差提升下游模型性能

  - 可将高频重复的参数调优类任务封装为Agent Skill，实现自动化参数寻优，大幅降低人工调参成本

  - 小样本目标检测场景可采用虚实数据混合策略，提升小目标识别精度，可复用在电商商品识别、广告素材质检等场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：科学领域CV任务的数据集采集标注成本高、误差大，合成渲染生成数据的过程缺乏系统量化指导，虚实数据域差缩小仅依赖主观视觉判断，无统一优化标准。
**方法关键点**：1. 开源Python工具包GraNatPy，内置量化度量体系引导渲染场景优化，可定量衡量合成数据集的真实度、多样性、规模；2. 推出SynthClaw，将程序化数据渲染封装为Agent技能，自动完成渲染参数寻优；3. 针对小目标检测场景，提出虚实数据混合的性能优化策略。
**关键结果**：合成数据集真实度、多样性、规模的量化提升，可直接匹配目标检测模型的零样本性能提升；病毒噬菌斑检测场景下，梯度相似度是影响小目标检测效果的核心指标，虚实数据混合可显著提升小目标检测精度。
