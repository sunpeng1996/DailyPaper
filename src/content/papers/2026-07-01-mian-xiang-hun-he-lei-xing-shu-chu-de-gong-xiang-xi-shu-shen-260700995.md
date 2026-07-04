---
title: Deep Multitask Learning for Mixed-Type Outcomes with Shared Sparsity
title_zh: 面向混合类型输出的共享稀疏深度多任务学习方法
authors:
- Huichao Li
- Tong Wang
- Sanguo Zhang
- Shuangge Ma
affiliations:
- School of Mathematical Sciences, UCAS
- School of Statistics and Data Science, Southeast University
- Key Laboratory of Big Data Mining and Knowledge Management, CAS
- Department of Biostatistics, Yale School of Public Health
arxiv_id: '2607.00995'
url: https://arxiv.org/abs/2607.00995
pdf_url: https://arxiv.org/pdf/2607.00995
published: '2026-07-01'
collected: '2026-07-04'
category: Training
direction: 多任务训练 · 混合输出类型适配
tags:
- Multitask Learning
- Deep Learning
- Group Lasso
- Sparsity
- Variable Selection
one_liner: 提出带共享稀疏约束的深度多任务框架，解决不同类型输出任务损失不可比、跨任务信息共享难的问题
practical_value: '- 电商多任务排序场景（点击/加购/成交等不同类型任务）可借鉴单调变换+统一秩损失的思路构造统一优化目标，避免不同损失量级对齐的繁琐工作

  - 多任务共享层加group-Lasso稀疏约束，可自动筛选跨任务通用的高价值特征，降低高维用户/商品特征的冗余干扰，提升模型泛化性

  - 第一层共享的轻量化多任务架构落地门槛低，训练稳定性优于全共享/全分离结构，适合快速迭代的业务场景'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有多任务学习依赖各任务定制的损失函数，不同类型（连续/二分类/混合）输出的损失不可直接比较，难以构造统一优化目标，限制跨任务信息共享；高维特征场景下大量冗余特征进一步降低模型效率与效果。
### 方法关键点
1. 引入未知单调变换适配不同任务的输出类型，构造平滑秩准则作为统一优化目标，消除不同任务的损失量级差异；
2. 加入group-Lasso惩罚实现跨任务共享稀疏，仅保留所有任务共用的有效预测因子，降低冗余特征干扰；
3. 采用第一层共享的多任务深度神经网络实现该框架，兼顾底层特征共享与上层任务定制。
### 关键结果
仿真实验中预测和变量选择性能优于基线方法；在包含连续、二分类混合输出的基因表达数据集上，预测准确率提升且可识别有生物学意义的共享预测因子。
