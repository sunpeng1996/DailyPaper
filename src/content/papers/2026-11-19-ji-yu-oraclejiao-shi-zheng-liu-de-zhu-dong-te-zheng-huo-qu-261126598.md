---
title: Active Feature Acquisition by Distilling an Oracle Teacher
title_zh: 基于Oracle教师蒸馏的主动特征获取方法
authors:
- Yang Meng
- Zixin Ding
- Robert L. Grossman
- Yuxin Chen
affiliations:
- University of Chicago
arxiv_id: '2611.26598'
url: https://arxiv.org/abs/2611.26598
pdf_url: https://arxiv.org/pdf/2611.26598
published: '2026-11-19'
collected: '2026-11-20'
category: Training
direction: 主动特征获取 · 知识蒸馏
tags:
- Active Feature Acquisition
- Knowledge Distillation
- Feature Selection
- Cost Optimization
- Model Training
one_liner: 提出OracleImitator框架，通过蒸馏显式Oracle教师策略实现低成本高收益的主动特征获取
practical_value: '- 推荐/广告场景特征获取成本高时（如用户隐私属性付费获取、实时特征计算耗时高），可复用该蒸馏思路，训练时用全量特征构造Oracle教师排序特征价值，蒸馏出低部署成本的特征选择策略

  - 预算约束下的特征选型可直接借鉴核心逻辑：仅需在训练阶段利用全量特征标注特征对下游预测误差的影响排序，不用在线端到端优化特征选取目标，落地难度低

  - 可迁移至大模型推理成本优化场景，给不同Query构造特征/工具调用的价值排序，蒸馏出轻量的工具调用决策策略，降低RAG/Agent调用成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
主动特征获取(AFA)旨在预算约束下选择高价值特征采集，降低特征获取的金钱、时间、隐私成本，现有方法均通过优化自构造效用目标训练采集策略，无显式教师引导，性能上限低、优化难度高。
### 方法关键点
1. 训练阶段利用全量可见的标签与未观测特征值，构造显式Oracle教师：按每个特征对下游预测器误差的影响程度排序所有候选特征；
2. 提出OracleImitator通过软目标模仿将排序结果蒸馏为可部署的特征采集策略，无需在线端到端优化采集目标。
### 关键结果
在多模态医疗诊断、AFABench基准上全预算区间性能持平或超越现有AFA方法，仅用不到1/4的采集成本即可恢复90%的可达到精度增益。
