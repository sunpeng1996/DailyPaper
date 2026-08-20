---
title: Assessing Quality of Experience in Natural Language Generation of German Text
title_zh: 德语文本自然语言生成（NLG）的用户体验质量评估
authors:
- Dinh Nam Pham
- Shushen Manakhimova
- Vivien Macketanz
- Sebastian Möller
affiliations:
- Technische Universität Berlin
- German Research Center for Artificial Intelligence (DFKI)
arxiv_id: '2608.18888'
url: https://arxiv.org/abs/2608.18888
pdf_url: https://arxiv.org/pdf/2608.18888
published: '2026-08-19'
collected: '2026-08-20'
category: Eval
direction: NLG生成质量 · QoE人因评估
tags:
- QoE
- NLG Evaluation
- LLM Evaluation
- Text Quality
- Human Annotation
one_liner: 发布面向德语NLG的人因QoE评估数据集TextQ-German，配套三类自动预测基线
practical_value: '- 电商德语站文案生成、机器翻译等NLG场景落地时，可参考「语言学特征+微调Transformer」的混合评估框架，相比纯大模型评估成本更低、效果更稳定

  - 小语种NLG业务可复用该研究的多维度感知质量标注框架，快速搭建对齐真实用户体验的自动评估流水线

  - 低资源场景下，单独基于语言学特征构建的评估模型性能接近微调LLM，可快速上线降低研发成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统NLG自动指标无法捕捉用户感知质量的多维度属性，德语场景缺乏对齐人因体验的公开评估资源，无法支撑LLM生成文本的落地效果校验。

### 方法关键点
1. 通过德语母语者众包标注，构建覆盖自动摘要、机器翻译两类任务的TextQ-German数据集，补充LLM生成样本的整体QoE评分标注；
2. 开发三类自动QoE预测基线：Transformer类、纯语言学特征类、混合架构类。

### 关键结果数字
混合模型在几乎所有实验设置下效果优于纯Transformer基线，纯语言学特征模型性能可接近微调语言模型水平，留存集验证证明模型可泛化到未见过的样本，所有资源公开可复用。
