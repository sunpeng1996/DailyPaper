---
title: 'D-Score: A Spectral Hidden-State Signal for Hallucination Detection in Large
  Language Models'
title_zh: 基于大语言模型隐藏态奇异谱信号的幻觉检测指标D-Score
authors:
- Bianca Raimondi
- Davide Evangelista
- Maurizio Gabbrielli
- Elena Loli Piccolomini
affiliations:
- University of Bologna, Italy
arxiv_id: '2607.24586'
url: https://arxiv.org/abs/2607.24586
pdf_url: https://arxiv.org/pdf/2607.24586
published: '2026-07-27'
collected: '2026-07-28'
category: LLM
direction: 大语言模型 · 幻觉检测内部信号挖掘
tags:
- Hallucination Detection
- Hidden Activations
- Spectral Method
- D-Score
- LLM Interpretability
one_liner: 通过单次前向传播计算隐藏激活矩阵相对数值秩实现无外部依赖的高效幻觉检测
practical_value: '- 电商导购、售后客服等RAG Agent场景可直接基于开源LLM的某层隐藏态计算D-Score，快速过滤高风险幻觉回复，降低调用外部事实校验工具的成本

  - D-Score可通过幂迭代只计算前K个奇异值实现优化，无需全量SVD，适配低延迟的线上业务场景，如实时对话、直播话术的幻觉拦截

  - 商品文案生成、卖点总结场景可直接在业务校验数据集上校准τ和对应层的判定阈值，无需额外训练分类头，快速上线轻量幻觉检测模块'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有幻觉检测方法要么依赖外部检索校验，要么需要多次采样生成对比，推理成本高，无法适配低延迟线上场景；基于隐藏态的检测方法大多需要额外训练分类探针，部署成本高，亟需仅靠单次前向传播、无额外依赖的轻量幻觉检测信号。

### 方法关键点
- 核心假设：当LLM处理和内部知识/给定上下文冲突的内容时，隐藏态会同时编码断言内容、冲突证据、不确定性等信号，导致隐藏轨迹的奇异谱分布更分散，而非集中在少数主方向上
- D-Score定义为隐藏激活矩阵的相对数值秩：统计满足σ₁/σ_i ≤τ的奇异值数量，τ为自定义容忍阈值，值越大代表隐藏态能量分布越分散，幻觉概率越高
- 工程优化：无需全量SVD，只需计算前K个奇异值直到低于相对阈值即可，用幂迭代实现可大幅降低计算量

### 关键结果
在FAVA-Annotation、RAGTruth两个公开幻觉检测数据集上测试Llama-2-7B、Llama-3-8B、Vicuna-7B三个开源模型，对比Hidden Score、PPL、熵等基线：
- Llama-3-8B上，FAVA数据集AUROC达66.98%，比次优基线高9.88个百分点；RAGTruth数据集AUROC达61.53%，比次优基线高6.58个百分点
- 在模型能明确识别的幻觉子集上，Llama-3-8B的AUROC可进一步提升到72.51%

> 最值得记住的一句话：LLM的幻觉风险会直接反映在隐藏态的拓扑结构上，仅靠简单的谱统计就能实现效果不错的轻量检测，无需复杂外部依赖。
