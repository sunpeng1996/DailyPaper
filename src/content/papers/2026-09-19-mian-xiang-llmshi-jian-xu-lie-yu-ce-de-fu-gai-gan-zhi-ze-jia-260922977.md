---
title: 'Beyond Similarity: Coverage-Aware Prompt Selection for Time Series Forecasting
  with LLMs'
title_zh: 面向LLM时间序列预测的覆盖感知Prompt选择框架
authors:
- Daeun Ji
- Minkyoung Kim
- Dongkuk Kim
- Yohan Lee
- Beomsoo Kim
- Beakcheol Jang
affiliations:
- Yonsei University
arxiv_id: '2609.22977'
url: https://arxiv.org/abs/2609.22977
pdf_url: https://arxiv.org/pdf/2609.22977
published: '2026-09-19'
collected: '2026-09-22'
category: LLM
direction: LLM时序预测 · 覆盖感知Prompt检索
tags:
- LLM
- Time Series Forecasting
- Prompt Learning
- Retrieval Optimization
- Regularization
one_liner: 提出无额外参数的跨批次覆盖感知正则化，解决LLM时序预测的相似性检索Prompt选择偏差
practical_value: '- RAG、检索式推荐、生成式推荐的Prompt Pool检索场景可复用该跨批次覆盖正则化，无需修改推理逻辑、不新增参数，即可解决头部Prompt过度调用、长尾模式覆盖不足的问题，适配电商大促、用户突发行为等稀有场景的预测需求

  - 所有基于相似性检索的训练pipeline可借鉴EMA使用统计+饱和门+stop-gradient的正则化设计，仅在训练侧新增损失项即可缓解检索偏差，工程改造成本极低

  - 电商销量预测、流量预测、用户行为序列预测等业务适配LLM时，可复用该时序语义对齐方案：将时序拆分为趋势、季节、残差分量后再投影到LLM语义空间，更好对齐预训练知识，提升数值序列的建模效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
基于余弦相似度的top-K检索是LLM时序预测、ICL、RAG等场景的主流范式，但存在严重的Prompt选择偏差：检索结果集中在头部主流模式，完全忽略稀有但信息价值高的异常/突发事件，现有单批次内的多样性优化方案（如MMR、DPP）无法解决跨训练批次累积的选择偏差问题。

### 方法关键点
- 提出CASP-LLM框架，完全保留现有top-K相似性检索逻辑，仅在训练阶段新增无额外可学习参数的覆盖正则化项
- 用EMA指数滑动平均跟踪每个语义锚点的跨批次使用统计，通过饱和min算子构造覆盖损失，搭配stop-gradient操作防止优化器恶意压低相似度降低正则惩罚
- 时序输入先拆解为趋势、季节、残差三个分量，再投影到预训练LLM语义空间，与从GPT-2词表线性投影得到的语义锚点做匹配

### 关键结果
- 在6个长时序基准（Weather、ETT系列、Electricity）+ M4短时序基准上测试，18/24的长时序数据集-预测周期组合取得MSE前2的成绩，相比纯相似性检索基线最高降低4.2%的MSE
- 单批次内的多样性优化（如MMR）对该偏差完全无效，只有跨批次的覆盖正则化能提升效果

### 核心结论
相似性检索的偏差核心是跨训练批次的锚点使用集中，而非单批次内的候选冗余，无参数的跨批次使用正则化比单批次多样性改造的性价比高得多。
