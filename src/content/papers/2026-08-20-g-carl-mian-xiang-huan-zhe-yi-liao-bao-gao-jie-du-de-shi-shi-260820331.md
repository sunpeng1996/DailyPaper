---
title: 'G-CARL: Grounded Checklist-Aligned Reward Learning for Patient-Oriented Medical
  Report Interpretation'
title_zh: G-CARL：面向患者医疗报告解读的事实对齐清单奖励学习框架
authors:
- Shiao Xie
- Siyu Chen
- Jianwei Lv
- Bo Yuan
- Yujin Wang
- Xiandong Li
affiliations:
- Baidu Inc., China
arxiv_id: '2608.20331'
url: https://arxiv.org/abs/2608.20331
pdf_url: https://arxiv.org/pdf/2608.20331
published: '2026-08-20'
collected: '2026-08-22'
category: Training
direction: 多模态生成 · 奖励对齐训练
tags:
- Reinforcement Learning
- Reward Modeling
- Factuality Alignment
- Multimodal Generation
- Checklist Supervision
one_liner: 提出清单对齐的RL奖励学习框架，兼顾医疗报告解读的事实准确性与用户需求匹配度
practical_value: '- 可将拆分维度的加权清单奖励框架迁移到生成式推荐/商品文案生成的RLHF流程：分别设置事实性（商品参数、活动规则准确性）、用户需求匹配度（不同用户关心的特性权重）两个独立奖励分支，解决多目标联合优化难的问题，避免整体打分的模糊性。

  - 原子声明+多源检索的事实校验思路可直接复用到电商咨询Agent：将生成的回答拆分为独立原子claim，检索商品详情、售后规则、活动说明等多源知识库做校验，从训练环节降低生成幻觉。

  - 实例专属加权检查清单思路可用于个性化推荐理由、Push文案的生成优化：针对不同用户画像、query上下文生成对应权重的checklist做奖励监督，替代统一评估模板，提升生成内容的个性化匹配度。'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有医疗多模态生成任务无法同时满足面向患者的报告解读两大核心要求：基于证据的医疗事实性、适配上下文的患者沟通友好性，传统监督微调、整体强化学习范式难以联合优化可验证性差异大的两个耦合目标。
### 方法关键点
1. 定义全新开放式多模态生成任务PMRI，要求基于用户查询、对话历史，用准确易懂的语言解释医疗报告；
2. 提出G-CARL强化学习框架，融合多源检索做原子声明的事实性校验，搭配上下文感知的实例专属加权检查清单做响应覆盖度评估，同时对事实性、用户需求满足度、表达质量做结构化监督，且不限制生成多样性；
3. 构建真实世界PMRI基准MMedReport，配套临床专家设计的三维评估协议。
### 关键结果
相比现有post-training基线，整体质量、声明级精度、清单召回率全面领先；临床专家pairwise偏好评估显示，其生成的解读准确率、用户需求匹配度显著更优。
