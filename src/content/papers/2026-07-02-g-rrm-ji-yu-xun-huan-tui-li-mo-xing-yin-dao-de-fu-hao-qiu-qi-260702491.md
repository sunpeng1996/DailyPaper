---
title: 'G-RRM: Guiding Symbolic Solvers with Recurrent Reasoning Models'
title_zh: G-RRM：基于循环推理模型引导的符号求解器优化方法
authors:
- Timo Bertram
- Sidhant Bhavnani
- Richard Freinschlag
- Erich Kobler
- Andreas Mayr
- Günter Klambauer
affiliations:
- ELLIS Unit Linz, LIT AI Lab & Institute for Machine Learning, Johannes Kepler University
  Linz, Austria
- Institute for Symbolic Artificial Intelligence, Johannes Kepler University Linz,
  Austria
- Clinical Research Institute for Medical AI, Johannes Kepler University Linz, Austria
arxiv_id: '2607.02491'
url: https://arxiv.org/abs/2607.02491
pdf_url: https://arxiv.org/pdf/2607.02491
published: '2026-07-02'
collected: '2026-07-05'
category: Reasoning
direction: 神经符号推理 · 约束满足问题求解
tags:
- Neuro-Symbolic
- Recurrent Reasoning Model
- Symbolic Solver
- Constraint Satisfaction Problem
- SAT Solver
one_liner: 提出融合符号等变循环推理模型与传统符号求解器的G-RRM框架，提升约束满足问题求解效率
practical_value: '- 当业务场景涉及组合优化（如广告排期、满减凑单路径规划）时，可先用轻量推理模型生成候选解引导传统求解器，在保证解正确性的前提下大幅提速

  - 推理模型引导求解器的前提是业务问题搜索空间足够大，且求解器支持动态覆盖错误的模型引导分支，否则overhead会抵消收益

  - 针对跨尺寸泛化需求的推理任务，可优先选择符号等变的循环推理模型结构，降低大尺寸问题的适配成本'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
传统循环推理模型（RRMs）在多步推理任务上表现优异，但无法保证解的全局正确性；经典符号求解器结果准确，但在大组合搜索空间下求解效率极低，两者结合的增益适用边界尚不明确。
### 方法关键点
提出G-RRM神经符号框架：先使用符号等变的SE-RRMs生成完整候选解，为回溯、SAT求解器等传统符号求解器提供分支搜索引导；求解器支持动态覆盖错误的模型引导，最终输出全局正确的解。
### 关键结果
满足「搜索空间足够大、求解器支持动态覆盖分支」两个条件时增益显著：9×9数独任务上SE-RRM解准确率91.1%，回溯求解器提速33.3×，Glucose 4.1提速1.70×（p<0.001）；25×25数独上Glucose 4.1仍保持1.17×提速；不支持覆盖分支的CaDiCaL 3.0.0无显著收益，甚至出现10%的平均降速。
