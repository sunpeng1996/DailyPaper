---
title: 'Skaling: Chinchilla''s Exponents Meet Kaplan''s Coupling'
title_zh: Skaling：耦合模型与数据的LLM缩放定律及低开销采样框架
authors:
- Mathurin Videau
- Badr Youbi-Idrissi
- David Lopez-Paz
- Kartik Ahuja
affiliations:
- FAIR at Meta
arxiv_id: '2608.07222'
url: https://arxiv.org/abs/2608.07222
pdf_url: https://arxiv.org/pdf/2608.07222
published: '2026-08-06'
collected: '2026-08-10'
category: Training
direction: LLM训练 · 缩放定律算力优化
tags:
- scaling_law
- LLM_pretraining
- compute_allocation
- performance_prediction
- low_resource_profiling
one_liner: 引入带单一耦合指数的缩放定律，损失预测误差降1.5-3倍，调优算力省10倍
practical_value: '- 训练电商/垂域LLM、Agent基座时，用Skaling替代Chinchilla做算力分配，在垂域数据稀缺等不均衡场景下损失预测误差降低1.5-3倍，避免资源浪费

  - 预训练前性能预估采用L型稀疏采样策略，仅用小模型扫数据量、小数据量扫模型量，即可获得与全网格采样相当的预测精度，省10倍调优算力

  - 垂域LLM缩放无需盲目遵循通用20token/参数配比，基于Skaling拟合的耦合系数计算最优配比，同算力下可获得更低预训练损失'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统Chinchilla缩放定律默认模型参数量、训练数据量对损失的影响完全独立，在数据稀缺、模型/数据配比极端失衡的场景下预测误差极大，无法支撑受限预算下的LLM预训练算力分配，也难以准确外推大参数量模型的性能。
### 方法关键点
- 提出Skaling定律，对Chinchilla的独立项之和新增单一外层耦合指数k，既保留原有参数的可解释性，又还原了模型与数据的真实交互作用，k=1时直接退化为Chinchilla定律
- 配套L型稀疏采样策略，仅在低算力边界采样（小模型上扫数据量、固定小数据量扫模型量）即可拟合所有参数，大幅降低预训练profiling的算力开销
- 完全继承Chinchilla的闭形式最优算力分配公式，仅需重新拟合参数即可得到更准确的最优token/参数配比，无需额外推导
### 关键实验
在Farseer（404组100M-6.4B参数的预训练配置）、SK-Grid（134组134M-4.9B参数的预训练配置）两个数据集上对比Chinchilla、Farseer基线：全网格拟合下Skaling的插值/外推MAPE比Chinchilla低1.5-3倍；用仅需1/10算力的L型采样拟合的Skaling，精度超过全网格采样的Chinchilla；高算力点外推任务上Skaling的MAPE仅0.6%，仅为Chinchilla的25%左右。
### 核心结论
缩放定律的核心误差不是来自内部拟合不足，而是来自忽略模型与数据的交互导致的边界预测偏差，仅新增1个耦合参数即可解决绝大多数场景的预测问题
