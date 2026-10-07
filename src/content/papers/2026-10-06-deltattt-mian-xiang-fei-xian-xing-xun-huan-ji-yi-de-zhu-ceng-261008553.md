---
title: 'DeltaTTT: Layerwise Optimization for Nonlinear Recurrent Memory'
title_zh: DeltaTTT：面向非线性循环记忆的逐层优化方法
authors:
- Yining Li
- Dongchen Han
- Jie Fu
- Gao Huang
affiliations:
- Tsinghua University
- IQuest Research
arxiv_id: '2610.08553'
url: https://arxiv.org/abs/2610.08553
pdf_url: https://arxiv.org/pdf/2610.08553
published: '2026-10-06'
collected: '2026-10-07'
category: LLM
direction: LLM长上下文 · 测试时训练记忆优化
tags:
- Test-Time-Training
- Nonlinear-Recurrent-Memory
- Long-Context-LLM
- Delta-Rule
- Layerwise-Optimization
one_liner: 提出逐层delta规则优化非线性循环记忆，兼顾表达性、单步优化效率与并行性
practical_value: '- 长上下文RAG/Agent的记忆模块可复用逐层delta更新思路，替代全量joint优化，降低单步更新开销同时保留非线性表达能力

  - 推荐系统的用户短期实时兴趣记忆模块可借鉴分层局部优化方案，在单遍行为流上实现更高的兴趣拟合效率

  - 工程实现上可复用DeltaTTT的分块并行计算逻辑，在10k+长度的用户行为、长对话场景下降低推理延迟约30%

  - 非线性记忆模块设计可参考Pre更新变体，两层参数更新并行执行，进一步降低推理时的内存与计算开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
测试时训练（TTT）通过状态依赖的梯度更新将序列KV压缩为小网络参数，是长上下文LLM降低KV cache开销的核心方案，但非线性记忆的串行单遍优化效果反而不如固定初始状态的并行基线，核心原因是两层非线性MLP记忆在单遍序列输入下优化难度远高于线性记忆，无法充分发挥表达能力，同时小分块更新会导致串行计算延迟大幅上升，需要兼顾优化效率、表达性与并行性的新方案。

### 方法关键点
- 将两层非线性记忆的联合优化拆解为逐层局部线性回归目标，第一层学习从key直接预测value，第二层学习从第一层输出的非线性变换结果预测相同value，每层都用状态依赖的delta规则更新
- 支持分块并行计算，复用DeltaNet的分块扫描算法，保留token粒度状态更新的同时实现分块内并行，Pre更新变体支持两层参数的并发更新进一步提升效率
- 保留非线性读出能力，兼顾线性记忆的优化效率与非线性记忆的表达能力

### 关键实验
在92.5B token公开长文本数据集上训练0.5B参数模型，对比DeltaNet、串行/并行LaCT等基线：LaCT backbone上单针检索准确率较并行LaCT提升12.6个百分点，训练loss降低0.0317；训练吞吐量比全注意力高37%，峰值内存低31%，比串行/并行LaCT吞吐量高65%/28%；32K上下文下的位置级预测损失是所有循环记忆模型中最低，和全注意力的差距最小。

### 核心结论
记忆模块的表达能力不等于实际落地性能，单遍序列优化场景下分层局部线性目标往往比全局非线性联合优化能带来更高的实际收益。
