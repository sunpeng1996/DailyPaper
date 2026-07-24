---
title: Interpretable Fuzzy Rule-Based Regression Extension for Ex-Fuzzy Library
title_zh: 面向Ex-Fuzzy库的可解释模糊规则回归扩展
authors:
- Cayan Deniz Kucuktopana
- Javier Fumanal-Idocin
- Richard Pitts
- Javier Andreu-Perez
affiliations:
- University of Essex
arxiv_id: '2607.20277'
url: https://arxiv.org/abs/2607.20277
pdf_url: https://arxiv.org/pdf/2607.20277
published: '2026-07-22'
collected: '2026-07-24'
category: Other
direction: 可解释机器学习 · 模糊规则库扩展
tags:
- Fuzzy System
- Interpretable ML
- Regression
- Mamdani Inference
- Library Extension
one_liner: 为Ex-Fuzzy库新增可解释Mamdani模糊回归支持，兼顾预测精度与规则可读性
practical_value: '- 电商推荐需满足可解释监管要求的场景，可用该模糊回归方法替代部分黑盒排序分预测模块，生成的规则可直接作为推荐理由支撑

  - 特征工程环节可借鉴target-aware的Fuzzy C-Means思路做目标相关的特征离散化，替代传统等频/等宽分桶，提升召回/排序模型的特征有效性

  - 营销预算分配、流量调控等需可回溯的运营决策回归场景，可直接调用该扩展快速落地，规避黑盒模型不可解释的合规风险'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有回归任务的机器学习模型精度高但多为黑盒，在受监管、高安全要求场景部署存在合规障碍，且主流机器学习库普遍缺少Mamdani风格模糊回归的工具支持。
### 方法关键点
为Ex-Fuzzy库新增Mamdani模糊推理回归扩展，支持直接从数据学习标量后件；提出基于Fuzzy C-Means的目标感知分区初始化策略，通过增强输入输出空间生成语言变量，强化特征空间中与输出相关区域的权重。
### 关键结果
在KEEL的10个回归数据集上测试，高斯分区效果始终优于均匀梯形分区，平均决定系数R²约0.86，仅生成10-15条人类可读的紧凑规则集，性能接近线性回归、MLP、随机森林等基线，可作为黑盒回归模型的透明替代方案
