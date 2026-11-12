---
title: 'One Table, Many Queries: Benchmarking Generalist Tabular Models Across Generation,
  Imputation, and Prediction'
title_zh: 跨生成、补全、预测任务的通用表格模型基准测试
authors:
- Yuanrui Wang
- Kaifang Li
- Xuanyue Li
- Ziyun Li
- Yan Lu
- Xingxuan Zhang
- Peng Cui
affiliations:
- StableAI
- Tsinghua University
- Beijing University of Posts and Telecommunications
- Southeast University
arxiv_id: '2611.13001'
url: https://arxiv.org/abs/2611.13001
pdf_url: https://arxiv.org/pdf/2611.13001
published: '2026-11-07'
collected: '2026-11-12'
category: Eval
direction: 通用表格模型 · 多任务基准评测
tags:
- Tabular Model
- Benchmark
- Multi-task Training
- Imputation
- Synthetic Generation
- Prediction
one_liner: 推出OTBench通用表格模型基准，解析三类表格任务能力关联与多目标训练规律
practical_value: '- 电商用户/商品特征补全、样本生成、CTR预测多任务训练可优先加入生成目标，其正向辅助增益覆盖最广

  - 多任务训练优先保留核心任务自身loss，为最大增益来源，多目标增益不具备可加性，需结合backbone适配

  - 冻结大模型可直接用于电商数值类特征预测、补全场景，无需微调即可获得不错效果，降低落地成本

  - 业务场景若追求分布保真选单任务专家模型，若追求下游任务效用选多任务通用模型，按需做trade-off'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有表格场景的生成、补全、预测三类任务独立评测，无法明确不同任务的能力共享性、训练目标交互规律，也无法验证单模型是否可同时胜任三类任务。
### 方法关键点
推出OTBench通用表格模型基准，覆盖56个数据集、46种方法、20个能力维度，统一数据划分与任务协议；对比对齐设置下的任务排名，在5个数据集上训练5种backbone的7种非空目标组合，对比通用模型与专家模型组合的效果。
### 关键结果
1. 补全与预测通过数值恢复、依赖保留能力关联，生成通过预测效用与二者关联，分布保真的排名逻辑与前三者独立甚至相反；
2. 加入目标任务自身目标带来的增益最大，生成类目标正向辅助覆盖最广，多目标增益不满足可加性；
3. 部分通用模型下游效用超过专家模型组合，分布保真仍专家模型更优；冻结大模型在预测、数值补全、合成数据效用上表现优异。
