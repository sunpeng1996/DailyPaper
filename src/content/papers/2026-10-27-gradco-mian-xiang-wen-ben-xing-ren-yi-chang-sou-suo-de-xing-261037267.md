---
title: 'GradCO: Behavior-Aware Gradient-Conflict Offloading for Text-Based Person
  Anomaly Search'
title_zh: GradCO：面向文本行人异常搜索的行为感知梯度冲突卸载方法
authors:
- Zhiheng Fu
- Zixu Li
- Zhiwei Chen
- Jiale Huang
- Fangxu Liu
- Jinhe Bi
- Yupeng Hu
affiliations:
- Shandong University
- National University of Singapore
- Intelligent Media Research Center
arxiv_id: '2610.37267'
url: https://arxiv.org/abs/2610.37267
pdf_url: https://arxiv.org/pdf/2610.37267
published: '2026-10-27'
collected: '2026-10-29'
category: Multimodal
direction: 多模态检索 · 梯度冲突优化
tags:
- Multimodal Retrieval
- MoE
- Gradient Optimization
- Text-to-Image Search
- TPAS
one_liner: 提出含B-MoE、COL、HIA的GradCO框架，解决TPAS梯度冲突与特征遮蔽问题，性能超越现有SOTA
practical_value: '- 多模态召回场景可复用B-MoE无监督分域设计，将静态/动态/异常特征拆分到不同expert流，避免强特征遮蔽弱特征，可适配电商文本搜商品等场景

  - 难负例导致的梯度冲突场景可借鉴COL的pair-conditioned offload anchor设计，降低冲突梯度对主表征学习的干扰，提升细粒度匹配精度

  - 多expert结果融合可复用HIA的query条件加权机制，根据用户query动态调整不同特征流权重，适配个性化检索需求'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
文本驱动行人异常搜索（TPAS）需同时保留身份特征、区分细粒度行为，存在两大核心痛点：同身份不同行为的难负例导致细粒度对齐阶段梯度冲突；强外观特征易掩盖弱行为证据，聚合阶段特征表达失衡。
### 方法关键点
提出GradCO框架，包含三大互补模块：1. 行为感知MoE（B-MoE）：无监督生成外观、正常行为、异常行为三个特征流，无需额外专家语义标注，直接从检索目标学习角色分工；2. 冲突卸载学习（COL）：相似度计算阶段引入对级卸载锚点，降低主文本表征的梯度冲突负担；3. 层级意图对齐（HIA）：基于query条件权重聚合多专家的相似度与特征。
### 关键结果
在5个TPAS/TIPR基准数据集上性能显著超越SOTA方法，全模块消融实验验证各组件有效性
