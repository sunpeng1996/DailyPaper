---
title: 'Predicting What Answer Engines Cite: Open Decision Models, Rerankers and a
  Distilled 4B Student on Ten Engines under Controlled Retrieval'
title_zh: 生成式回答引擎引用预测：开源决策模型与4B蒸馏重排器
authors:
- Elisha Bajemon
- Andre-Louis Rochet
affiliations:
- TW3 Partners (Citead)
arxiv_id: '2610.38090'
url: https://arxiv.org/abs/2610.38090
pdf_url: https://arxiv.org/pdf/2610.38090
published: '2026-10-28'
collected: '2026-10-30'
category: RAG
direction: RAG重排 · 知识蒸馏落地
tags:
- Reranker
- Knowledge Distillation
- LoRA
- Generative Engine Optimization
- Citation Prediction
one_liner: 蒸馏得到4B参数引用预测重排器，性能与27B开源决策模型及商用Jev无显著差异
practical_value: '- 做RAG/生成式搜索的重排时，可直接用开源的GEO Citation Ranker 4B替代大模型judge做引用优先级预测，推理成本远低于27B决策模型，性能差异可忽略

  - 小参数重排器蒸馏可采用大模型judge+开源决策模型双教师打标，仅需几百条训练数据加LoRA微调就能接近大模型效果，4B模型单卡RTX 3090仅需2小时训练

  - 引用预测类排序任务中，listwise（多候选同时打分）比pointwise（单候选打分）有稳定3%-5%的效果提升，资源允许时优先采用listwise范式

  - 生成式引擎对候选源的位置有偏好，但仅靠位置排序效果和BM25相当（Spearman相关0.131），无需过度依赖位置特征做增益'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式引擎优化（GEO）需要提前预测哪些候选页面会被回答引擎作为引用源，直接调用引擎测试成本高、速度慢、结果非确定，现有预训练重排器、LLM judge未针对引用预测场景做专项验证，小参数模型的性能天花板不明确。

### 方法关键点
- 数据集：采用GEO-Bench的229条测试query，10个生成式回答引擎输入相同5个候选源，标签为各源的位置加权引用占比，共1220组有效样本
- 对比方案覆盖预训练重排器（Qwen3-Reranker、bge等）、8款开源决策模型、商用Jev模型；蒸馏方案采用Jev+LLM judge双教师打标，基于Qwen3-Reranker用秩16 LoRA微调，优化pairwise logistic loss
- 评估指标为组内Spearman相关系数（和真实引用占比的相关性）、top-1准确率

### 关键结果
- 不同引擎间的引用一致性Spearman达0.704，是所有打分器的性能上限参考；27B开源决策模型（JEV-27B、pplx-decider-27B）零-shot效果和商用Jev相当，达0.575~0.578
- 蒸馏得到的4B GEO Citation Ranker Spearman达0.542~0.549，和27B模型、Jev的差异在95%置信区间下不显著，比原预训练Qwen3-Reranker-4B提升0.09，top-1准确率达0.567
- 4B模型比8B模型性价比更高，8B模型效果没有显著优于4B；仅用1/4训练数据就能达到全量数据99%的效果

### 核心结论
4B参数的蒸馏重排器在生成式引擎引用预测任务上，可达到27B决策模型94%以上的性能，训练和推理成本降低一个数量级
