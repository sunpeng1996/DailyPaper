---
title: Learning Sparse Decision Trees via Transformer Variational Auto-Encoders
title_zh: 基于Transformer变分自编码器的稀疏决策树学习方法
authors:
- Giacomo Fidone
- Alessio Cascione
- Riccardo Guidotti
affiliations:
- University of Pisa
- ISTI-CNR
arxiv_id: '2609.01430'
url: https://arxiv.org/abs/2609.01430
pdf_url: https://arxiv.org/pdf/2609.01430
published: '2026-09-01'
collected: '2026-09-03'
category: Training
direction: 可解释模型训练 · 决策树优化
tags:
- Decision Tree
- Transformer
- VAE
- Sparse Learning
- Interpretable ML
one_liner: 提出TREVIS框架，基于树Transformer VAE的连续隐空间搜索实现决策树性能与稀疏性的联合优化
practical_value: '- 电商风控、广告准入等强可解释需求场景，可借鉴TREVIS生成稀疏决策树，在不损失预测精度的前提下压缩规则规模，提升运算效率与可解释性

  - 离散规则类任务的搜索优化可复用「离散结构映射至VAE连续隐空间+梯度优化」范式，替代传统贪心搜索，平衡搜索效率与全局最优性

  - 推荐系统规则冷启动、大模型兜底规则生成场景，可采用该方法快速产出轻量化可解释决策树，降低复杂模型的运维风险'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有决策树学习算法存在明显短板：贪心策略仅优先优化预测性能，忽略结构稀疏性，可解释性不足；全局最优搜索的计算成本随特征/样本量指数级上升，无法适配高stakes场景对效果、效率、可解释性的多重要求。
### 方法关键点
1. 提出TREVIS框架，基于Tree Transformer Variational Auto-Encoder（TTVAE）将离散决策树结构映射到连续隐空间，把原有的离散组合搜索转化为连续空间的梯度优化问题
2. 引入可微分代理模型实现多目标联合优化，同时对齐预测准确率、结构稀疏度两个核心指标
### 关键结果
生成的决策树预测性能与现有近最优决策树算法完全持平，同时结构稀疏性获得显著提升
