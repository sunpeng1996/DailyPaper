---
title: 'PAGSL: Path-Augmenting Graph Structure Learning for explainable scholar recommendation'
title_zh: 路径增强图结构学习（PAGSL）的可解释学者推荐方法
authors:
- Jiale Xu
- Mingshu Ai
- Junjie Huang
- Tao Jia
affiliations:
- 西南大学计算机与信息科学学院
- 重庆师范大学计算机与信息科学学院
arxiv_id: '2611.09126'
url: https://arxiv.org/abs/2611.09126
pdf_url: https://arxiv.org/pdf/2611.09126
published: '2026-11-06'
collected: '2026-11-09'
category: RecSys
direction: 可解释图推荐 · 异构图结构学习
tags:
- Graph Structure Learning
- Explainable Recommendation
- GNN
- Heterogeneous Graph
- Scholar Recommendation
one_liner: 提出路径增强图结构学习模型PAGSL，同时提升学者推荐精度与解释的个性化分层深度
practical_value: '- 异构图推荐场景可复用「图增强激活潜在关联+路径编码」范式，缓解hub节点（如电商热门商品）偏差问题

  - 路径打分优化的掩码机制可直接迁移到可解释推荐场景，生成简洁个性化归因路径，适配电商推荐的解释文案生成

  - 异构图卷积+路径表示学习的组合可作为召回/粗排阶段的特征增强模块，提升稀疏交互场景下的推荐精度'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有可解释推荐框架存在优化噪声与hub节点偏差问题，生成的解释缺乏分层深度与个性化，无法同时满足推荐精度与可解释性要求。
### 方法关键点
1. PAGSL融合表示学习与语义路径知识，通过图增强激活实体间潜在关联路径；
2. 采用路径型神经网络编码路径特征用于推荐，引入带路径打分优化的掩码机制生成简洁高信息量的解释。
### 关键结果
在Scholat、AMiner、ResearchGate三个学术数据集（共4.9万作者、33万+交互记录）上测试，相比SOTA基线，F1-score提升6.31%，Accuracy提升6.29%，AUC提升5.95%，解释效果的量化与可视化表现均更优，ablation验证了异构图卷积与路径表示学习模块的有效性。
