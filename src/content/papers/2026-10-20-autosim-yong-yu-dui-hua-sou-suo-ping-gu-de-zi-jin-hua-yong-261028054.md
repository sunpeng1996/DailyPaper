---
title: 'AutoSim: A Self-Improving User Simulator for Conversational Search Evaluation'
title_zh: AutoSim：用于对话搜索评估的自进化用户模拟器
authors:
- Saber Zerhoudi
- Jelena Mitrovic
- Michael Granitzer
affiliations:
- University of Passau
- Interdisciplinary Transformation University Austria
arxiv_id: '2610.28054'
url: https://arxiv.org/abs/2610.28054
pdf_url: https://arxiv.org/pdf/2610.28054
published: '2026-10-20'
collected: '2026-10-22'
category: Eval
direction: 对话搜索评估 · 自进化用户模拟器
tags:
- UserSimulation
- ConversationalSearch
- Evaluation
- SelfEvolvingAgent
- LoRA
one_liner: 通过权重级微调实现的对话搜索用户模拟器，行为与真人无异且评估无偏
practical_value: '- 搭建用户模拟器时优先做权重级优化：prompt级优化最多将真假判别AUC降至0.85，要实现真人级仿真需用LoRA+对抗拒绝采样SFT微调生成模块，避免高估系统效果

  - 评估对话搜索/智能导购系统时，若使用prompt式用户模拟器，在低检索准确率场景会高估nDCG达0.136，极易做出错误上线决策，建议优先选用无偏的权重微调模拟器

  - LLM的相关性判断能力已接近真人标注，和NIST标注的系统排序Kendall''s τ最高达0.91，无需额外优化判断prompt，可直接用于系统排序评估，节省标注成本

  - 自进化类Agent迭代时必须加真实数据校准门限，仅保留不降低核心指标的更新，避免无约束迭代导致行为漂移'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
对话搜索、智能导购等交互式系统的评估依赖真人实验，成本高、周期长，无法支撑快速迭代。现有基于prompt构建的LLM用户模拟器行为与真人差异大，会系统性高估检索/推荐效果，甚至导致错误的上线决策，亟需高逼真度的无偏用户模拟器。

### 方法关键点
- 混合编排架构拆分相关性判断模块和对话生成模块：相关性判断模块直接复用通用LLM的原生能力，自进化循环仅优化生成模块，避免影响评估准确性
- 支持两类自进化路径：prompt级迭代优化，以及权重级优化（采用LoRA微调小尺寸生成模型，基于对抗式拒绝采样SFT，用真人-模拟判别器筛选高仿真样本迭代训练）
- 所有更新需通过校准集验收，只有不降低和真人标注排序一致性的更新才会被保留，避免行为漂移

### 关键实验结果
- 数据集覆盖3年TREC iKAT对话搜索公开集、TREC CAsT 2020数据集，对比baseline包括默认prompt、调优prompt、少样本prompt三类prompt级方案
- 权重级优化后真人-模拟判别器AUC降至0.45，人类也无法区分模拟和真实对话；和NIST标注的系统排序Kendall's τ最高达0.91
- prompt级模拟器在用户难检索的场景会高估nDCG达0.136，权重级方案偏差仅0.014，无统计显著性

### 核心结论
仅靠prompt优化无法消弭用户模拟器的Sim2Real差距，必须通过权重级微调才能实现无偏的交互式系统评估
