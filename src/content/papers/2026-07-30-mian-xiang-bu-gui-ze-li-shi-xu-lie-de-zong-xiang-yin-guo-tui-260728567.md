---
title: Doubly Robust Functional Representation Learning for Longitudinal Causal Inference
  with Irregular Histories
title_zh: 面向不规则历史序列的纵向因果推断双稳健函数表示学习方法
authors:
- Mengfei Ran
- Yifeng Shen
- Ruijie Guan
affiliations:
- 西安交通利物浦大学生命与自然科学学院
- 中国科学院空天信息创新研究院
arxiv_id: '2607.28567'
url: https://arxiv.org/abs/2607.28567
pdf_url: https://arxiv.org/pdf/2607.28567
published: '2026-07-30'
collected: '2026-08-02'
category: Other
direction: 纵向因果推断 · 双稳健表征学习
tags:
- causal_inference
- representation_learning
- doubly_robust
- longitudinal_data
- functional_data_analysis
one_liner: 提出DR-FRL双稳健表征学习框架，解决不规则时序片段纵向因果推断的估计偏差问题
practical_value: '- 处理电商用户非均匀采样的不规则行为时序（如零散点击/浏览记录）做uplift建模时，可复用「功能编码器+时序编码器」结构，将点云式行为序列映射为目标对齐的状态表征，避免手动特征聚合的信息损失

  - 做因果效应估计任务时，可引入EIF（高效影响函数）对齐的验证校准、重叠度诊断流程，降低表征误差对最终估计结果的影响

  - 当业务数据稀疏、采样不均、伪标签重尾时，可借鉴Catoni聚合方法做有界影响点估计，提升预估结果鲁棒性'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
纵向因果研究的历史数据多为非均匀采样的不规则功能片段，传统双稳健估计器依赖人工标量摘要损失关键信息，常规序列学习的预测损失无法稳定高效影响函数（EIF），易导致估计偏差。
### 方法关键点
1. 提出DR-FRL交叉拟合工作流，通过功能编码器+时序编码器将非均匀点云、历史序列映射为估计目标对齐的状态表征；
2. 设计nuisance头估计结果、治疗、删失三类函数，配套EIF对齐的验证、校准、重叠度、尾部、消融诊断流程，保障表征满足估计方程要求；
3. 表征误差与普通nuisance误差同属二阶余项，搭配Catoni聚合做有界影响点估计，保证估计渐近线性。
### 关键结果
- 模拟实验中，在高维功能混淆、信息性采样、支撑集弱、伪结果重尾场景下效果显著优于基线；
- VitalDB数据集测试中，可直接处理不规则实验室检查点云数据，验证了标量实验室摘要已承载大量ICU处置终点相关信息的阴性结论。
