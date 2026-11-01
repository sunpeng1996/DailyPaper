---
title: A Low-Rank Space Captures Linear Alignment Between LLM and Human Neural Activity
  During Naturalistic Language Listening
title_zh: 低秩空间可捕捉自然语言聆听时LLM与人类神经活动的线性对齐
authors:
- Zach Paris
- Emily Finn
affiliations:
- Dartmouth College Department of Psychological and Brain Sciences
arxiv_id: '2610.40511'
url: https://arxiv.org/abs/2610.40511
pdf_url: https://arxiv.org/pdf/2610.40511
published: '2026-10-29'
collected: '2026-11-01'
category: LLM
direction: LLM表征与人脑对齐机制研究
tags:
- LLM Representation
- Neural Alignment
- Low-Rank Regression
- Dimensionality Reduction
- fMRI
one_liner: 用岭降秩回归发现仅需LLM嵌入1-3%维度即可完全复现神经活动预测性能
practical_value: '- 做LLM下游任务（如用户意图理解、Query语义匹配）时，可通过岭降秩回归提取任务相关低维子空间，仅保留1-3%核心维度即可达到全维度性能，大幅降低存储与推理开销，效果优于PCA降维

  - 用户行为建模/语义召回的特征筛选阶段，无需优先选择LLM表征方差最大的维度，可针对业务目标（点击/转化）训练降秩子空间，筛选与业务对齐的核心维度

  - 不同业务场景训练得到的低维表征子空间可尝试跨场景迁移，可降低小流量场景、新场景的冷启动成本'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM已被证实可较好预测人类语言处理过程中的神经活动，但此前未明确其高维表征中哪些成分驱动了与人脑的对齐。
### 方法关键点
采用岭降秩回归识别LLM表征中的脑预测子空间，跨3个覆盖颅内电生理、fMRI的自然语言聆听数据集，以及自回归、双向掩码、随机初始化在内的6类LM模型条件开展验证，同时对比降秩回归与PCA的表征提取效果。
### 关键结果
仅需原始嵌入1-3%的维度即可恢复完整的神经活动线性预测性能；该低维子空间可跨被试泛化，跨数据集也有一定泛化性；PCA需要显著更多维度才能达到同等预测效果，说明与神经活动对齐的表征方向和LLM自身方差最大的方向并不重合；可通过子空间分析挖掘出神经活动中高占比的可解释特征。
