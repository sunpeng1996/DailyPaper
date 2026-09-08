---
title: Can Large Language Models Anticipate Behavioral Responses to Social Policies?
  A Case of Pension Enrollment Prediction among China's Flexible Workers
title_zh: 大语言模型预测社会政策行为响应：中国灵活就业者参保预测案例
authors:
- Yumiao Li
- Peixin Liu
- Donglin Di
- Chen Li
- Runhuan Feng
affiliations:
- Tsinghua University
- University of Illinois Urbana-Champaign
- Harbin Institute of Technology
arxiv_id: '2609.05189'
url: https://arxiv.org/abs/2609.05189
pdf_url: https://arxiv.org/pdf/2609.05189
published: '2026-09-04'
collected: '2026-09-08'
category: LLM
direction: LLM领域适配 · 政策行为预测
tags:
- LLM
- Knowledge Distillation
- LoRA
- MoE
- Domain Adaptation
one_liner: 提出面向灵活就业者参保预测的领域专用LLM及知识蒸馏方法，性能接近Claude Opus
practical_value: '- 可复用DKI-RDistill的领域知识注入思路，做电商营销/补贴政策的用户行为预测时，将业务规则、统计特征作为prompt
  cue注入，提升预测准确率

  - 蒸馏流程的错误样本重标trick可直接迁移：用闭源大模型做教师蒸馏小模型时，对教师预测错误的样本用真实标签重生成训练数据，减少误差传导

  - LoRA+SFT适配开源MoE模型的方案可复用，业务小样本场景下用远低于全量微调的成本获得接近闭源SOTA的效果'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
社会政策落地前效果评估难度大，计量经济学方法外推假设场景可靠性低，线下试点成本高，亟需低成本的个体层面政策响应模拟方案。
### 方法关键点
1. 提出DKI-RDistill框架，prompt注入政策相关线索（含Probit模型输出的边际效应、户籍-省份对应养老金规则）
2. 用LoRA/SFT将带推理过程的监督信号蒸馏到开源MoE学生模型，对教师预测错误的样本用真实标签重生成训练数据修正误差
3. 输出领域专用模型FlexPension-LLM，解决中国灵活就业者分层参保预测任务
### 关键结果
在CHFS2019盲测集上综合F1达0.9316，超过教师模型Claude Sonnet 4.5，17个基线中赢过15个，性能与Claude Opus 4.6无统计差异；4个外部调查集平均综合F1 0.7549，是同性能梯队系统中表现波动最小的
