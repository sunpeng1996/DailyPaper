---
title: Prototype Language Models
title_zh: 原型语言模型PRISM：高可解释性的序列建模架构
authors:
- Dan Ley
- Giang Nguyen
- Himabindu Lakkaraju
- Julius Adebayo
affiliations:
- Harvard University
- Guide Labs Inc.
arxiv_id: '2607.00510'
url: https://arxiv.org/abs/2607.00510
pdf_url: https://arxiv.org/pdf/2607.00510
published: '2026-07-01'
collected: '2026-07-02'
category: LLM
direction: 可解释LLM · 训练数据归因
tags:
- Interpretable LLM
- Prototype Learning
- Training Attribution
- Model Editing
- Sparse Architecture
one_liner: 提出基于稀疏原型混合的PRISM架构，精度接近稠密LLM的同时实现500倍更快的训练数据归因
practical_value: '- 可复用稀疏原型架构思路，落地LLM4Rec/导购Agent的训练数据归因，快速定位bad case对应的训练样本，跳过复杂的事后归因流程

  - 借鉴原型抑制方法，无需全量finetune即可快速删除LLM生成的违规内容、错误推荐逻辑，适配电商推荐/客服Agent等高合规要求场景

  - 复用原型控制器校准方法，快速提升电商文案生成、商品推荐垂域LLM的下游效果，同时保留可追溯性，方便效果迭代归因'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：现有稠密LLM的训练数据影响分散在全量参数中，事后归因成本高、精度低，无法支撑模型审计、快速纠错需求。
**方法关键点**：提出PRISM原型语言模型架构，每次预测通过已学习原型的稀疏非负混合生成，搭配聚类目标训练，每个原型锚定对应训练样本的相干邻域，训练数据影响可通过原型直接追溯。
**关键结果**：130M~1.6B参数、最高50B tokens训练规模下，PRISM下游精度要么超过同规模稠密基线，要么平均差距≤2.5pp；训练数据归因速度比事后基线快~500x，内存消耗相当；校准线性原型控制器可提升下游精度约3pp，同时可追溯修正对应的训练邻域；定向抑制原型可删除指定模型行为，无需finetune且无可测生成质量损失。
