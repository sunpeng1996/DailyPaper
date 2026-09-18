---
title: 'Intrinsic Sequence-Likelihood Confidence in Retrieval-Dominated Extractive
  QA: Two Pre-Specified Negatives, and What They Do and Do Not Attribute'
title_zh: 检索主导抽取式QA的序列似然置信度：预设负例的作用边界
authors:
- Gunwoo Lee
- Changmin Sung
- Sang-Hwan Gwak
- Ina Kim
- Ji-Young Choi
- Kyong-Ha Lee
affiliations:
- Korea Institute of Science and Technology Information (KISTI)
- University of Science and Technology (UST)
arxiv_id: '2609.19942'
url: https://arxiv.org/abs/2609.19942
pdf_url: https://arxiv.org/pdf/2609.19942
published: '2026-09-17'
collected: '2026-09-18'
category: RAG
direction: RAG 抽取式QA置信度效果评估
tags:
- Extractive QA
- Confidence Estimation
- Sequence Likelihood
- Retrieval Augmented Generation
- Model Evaluation
one_liner: 验证检索主导抽取式QA中置信度驱动机制增益极低，提供可复用预设负例集合
practical_value: '- 电商RAG问答/商品属性抽取等召回准确率≥92%的场景，无需额外叠加热门的置信度路由/拒答模块，ROI极低

  - 序列似然作为LLM输出置信度的方案效果上限低（AUC仅0.65~0.81），标量重校准、token级温度缩放均无法稳定提升，无需投入资源优化这类方案

  - 做LLM抽取类任务的效果验证时，可直接复用论文公开的预设负例集合，降低负例构造成本'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前RAG/抽取式QA场景普遍尝试用LLM序列似然作为置信度信号，支撑路由、拒答、蒸馏触发等逻辑，但缺乏严格预注册的效果验证，大量方案实际ROI不明。
### 方法关键点
针对4个7-9B参数开源LLM，在检索准确率极高的抽取式QA场景下，按照预定义的固定评估标准，测试置信度驱动的蒸馏触发、路由拒答两类机制的效果，同时验证标量重校准、token级温度缩放对置信度信号的优化作用。
### 关键结果
- 单独检索即可覆盖92%~99.8%的最优组合准确率，置信度驱动机制无统计显著增益
- 序列似然置信度的AUC仅为0.65~0.81，微调、重校准、温度缩放均无法稳定提升效果
- 多数场景下移除置信度项不会降低效果，Gemma模型移除后反而通过全部注册评估标准
- 输出一套可复用的预定义负例集合
