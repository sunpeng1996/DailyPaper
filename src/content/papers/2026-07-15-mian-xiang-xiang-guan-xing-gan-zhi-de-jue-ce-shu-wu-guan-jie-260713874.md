---
title: 'Relevance-Aware Rule: Structural Deletion of Irrelevant Conditions in Decision
  Trees'
title_zh: 面向相关性感知的决策树无关条件结构性删除方法
authors:
- Jung-Sik Hong
- Jeongeon Lee
- Min Kyu Sim
- Sangheum Hwang
affiliations:
- Seoul National University of Science and Technology
arxiv_id: '2607.13874'
url: https://arxiv.org/abs/2607.13874
pdf_url: https://arxiv.org/pdf/2607.13874
published: '2026-07-15'
collected: '2026-07-16'
category: Training
direction: 决策树规则简化 · 冗余条件删除
tags:
- Decision Tree
- Interpretability
- Rule Simplification
- Pruning
- Model Compression
one_liner: 基于决策树分叉结构规律，提出无精度损失的规则冗余条件删除框架
practical_value: '- 电商人群圈选、风控、粗排等场景的决策树规则可直接复用该框架简化，降低规则执行延时，且不损失原有预测精度

  - 可解释性要求高的业务场景（如广告投放理由、推荐驳回解释）可通过该方法压缩规则长度，提升解释可读性

  - 线上低延时场景的轻量化树模型优化，可复用其「结构校验+可靠性评估」的冗余删除逻辑，避免过剪枝'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
决策树生成的可解释if-then规则普遍存在无关冗余条件（IRCs），现有删除方法要么规则保留太宽松导致可靠性下降，要么太严格无法实现有效简化，且均未考虑决策树分叉的固有结构特性。
### 方法关键点
1. 从理论层面证明二叉分叉会在两个子分支分别提升正负类占比，对应生成C1-link和C0-link；
2. 对每个叶子节点，匹配提升叶子对应类别占比的link，标记反向link为IRCs候选；
3. 进一步评估删除候选后的预测可靠性，仅删除结构和经验上均无关的条件，严格保护会降低可靠性的条件。
### 关键结果
实验验证该框架可实现大幅规则简化，同时100%保留原决策树的预测可靠性，无精度损失。
