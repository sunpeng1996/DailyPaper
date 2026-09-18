---
title: 'Null importance: Disentangling relevance for interpretable machine learning'
title_zh: 零重要性：面向可解释机器学习的相关性解耦
authors:
- Garvesh Raskutti
- Kris Sankaran
- Jiaxin Ye
arxiv_id: '2609.19511'
url: https://arxiv.org/abs/2609.19511
pdf_url: https://arxiv.org/pdf/2609.19511
published: '2026-09-16'
collected: '2026-09-18'
category: Eval
direction: 可解释机器学习 · 特征重要性评估
tags:
- feature importance
- interpretable ML
- null hypothesis
- model interpretability
- fairness
one_liner: 提出基于零重要性的统一框架，解耦多类特征相关性定义，规范可解释性分析适用边界
practical_value: '- 做推荐/广告特征重要性分析时，先明确业务目标对应的相关性定义（关联/因果/预测风险等），避免误判特征价值

  - 算法公平性校验场景，可对应不同null importance定义设计针对性指标，适配不同监管/业务公平要求

  - 特征工程冗余校验时，可复用框架区分边际/条件相关性，精准裁剪冗余特征降低模型推理开销'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有特征重要性定义缺乏统一规范，不同维度的「相关性」概念混同，导致可解释分析结论易矛盾、不可靠，甚至误导业务决策。
### 方法关键点
基于null importance构建统一分析框架，覆盖边际统计相关、条件统计相关、预测风险、函数不变性、因果效应5类主流相关性定义，明确每类定义对应的适用场景、数据与模型假设，同时给出不同定义等价的充分条件，以及假设不满足时的偏差反例。
### 关键结果
仿真实验覆盖特征依赖、冗余、非线性、隐特征等常见场景，搭配图像、多组学真实案例验证，框架可精准明确不同特征重要性算法的适配边界，大幅降低跨方法结论冲突，为可解释分析提供统一统计语言。
