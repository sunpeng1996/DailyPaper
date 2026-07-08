---
title: 'Estimating Uncertainty from Reasoning: A Large-Scale Study of Multi- and Crosslingual
  MCQA Performance in LLMs'
title_zh: 大模型多语言跨语言MCQA场景下基于推理的不确定性估计大规模研究
authors:
- Andrea Alfarano
- Andrea Bacciu
- Saab Mansour
- Amin Mantrach
- Marcello Federico
affiliations:
- INSAIT, Sofia
- Amazon
arxiv_id: '2607.06327'
url: https://arxiv.org/abs/2607.06327
pdf_url: https://arxiv.org/pdf/2607.06327
published: '2026-07-07'
collected: '2026-07-08'
category: Eval
direction: 大语言模型 · 不确定性估计评测
tags:
- Uncertainty Estimation
- Multilingual LLM
- MCQA
- Selective Prediction
- Reasoning
one_liner: 覆盖22种语言9款模型的大规模评测，给出多语言不确定性估计的可落地选型策略
practical_value: '- 跨境电商/多语言Agent场景下，低资源语言请求可强制模型推理环节用英语生成，既能平均提升5.4%的任务准确率，还能将UE的AUROC从0.58提升至0.68，抹平与高资源语言的性能差距

  - UE方法选型匹配模型规模：部署<30B小模型优先用Token Entropy等开放盒概率类方法，部署≥30B大模型优先用Self Verbalized闭盒方法，AUROC最高可提升0.12

  - 多语言场景选择性预测阈值校准：资源有限时用英语单语种校准即可实现43%相对错误降低，多语言标注数据充足时用语言特定阈值可实现60%相对错误降低

  - 跨语言RAG/多语种搜索推荐场景下，UE方法对混合语言输入鲁棒性极强，无需额外适配即可直接复用'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM不确定性估计（UE）研究几乎全聚焦英语场景，低资源语言下的UE效果、方法选型、校准策略完全缺失可靠参考，且过往评测多依赖LLM-as-judge或嵌入打分，存在明显评估噪声，无法支撑多语言LLM落地的可信性需求。
### 方法关键点
- 覆盖9种主流UE方法：包含开放盒概率类（TokenEntropy、MaxProb等）、闭盒自报告类（Self Verbalized）、多采样一致性类（Semantic Entropy、图特征方法等）三类范式
- 评测9款模型：参数从0.27B到235B，覆盖Gemma3、Qwen3、Claude 4.5 Sonnet，包含密集与MoE架构
- 采用两份人工标注的多语言MCQA数据集，覆盖22种高/中/低资源语言，从平均150词的推理过程提取UE信号，用MCQA标签做客观正确性判定，完全避免评估噪声
### 关键结果数字
- 低资源语言下强制用英语做推理，可将UE的AUROC从0.58提升到0.68，抹平与高资源语言的性能差距，同时任务准确率平均提升5.4%，低资源语言最高提升17.6%
- 模型规模<30B时，开放盒TokenEntropy方法最优（AUROC≈0.71），规模≥235B时，Self Verbalized反超（AUROC≈0.77），采样类一致性方法在低资源语言下性能接近随机（AUROC≈0.5）
- 阈值校准方面，单英语校准即可实现43%相对错误降低，语言特定校准可实现60%相对错误降低，跨语言混合输入场景下UE性能无明显下降
> 最值得记住的一句话：多语言UE的瓶颈是生成而非理解，推理用英语即可大幅拉平高低资源语言的可信性差距
