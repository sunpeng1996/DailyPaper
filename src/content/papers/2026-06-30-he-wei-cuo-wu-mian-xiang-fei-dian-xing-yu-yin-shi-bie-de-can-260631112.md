---
title: What Counts as an Error? Dual-Reference Benchmarking for Atypical ASR
title_zh: 何为错误？面向非典型语音识别的双参考基准测试方法
authors:
- Hawau Olamide Toyin
- Srinivasan Umesh
- Hanan Aldarmaki
affiliations:
- MBZUAI, UAE
- SPRING Lab, IIT Madras, India
arxiv_id: '2606.31112'
url: https://arxiv.org/abs/2606.31112
pdf_url: https://arxiv.org/pdf/2606.31112
published: '2026-06-30'
collected: '2026-07-02'
category: Eval
direction: 语音识别评估 · 非典型语音双参考基准
tags:
- ASR
- Evaluation Benchmark
- Atypical Speech
- Dual Reference
- Stuttered Speech
one_liner: 提出非典型ASR的双转录参考评估基准，对比11类主流ASR模型的性能与排名差异
practical_value: '- 语音搜索/智能客服等涉及ASR的电商场景，可按下游任务选择转录参考：需还原用户真实表达（如客服质检）选逐字参考，需理解用户意图（如语音搜索Query改写）选去口癖的意图参考

  - 面向有口音、口吃等非典型用户的语音交互场景，评估ASR模型时不能用单一真值，需按业务目标设置双评估指标，避免误筛适配性更好的模型

  - 多模态交互Agent的语音模块选型，可复用该双参考评估框架，平衡转录忠实度和意图准确率两个维度的性能'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
非典型语音（如口吃、带口音语音）的ASR评估长期混淆两类有效真值：逐字转录（含重复、拖音等真实表达）和意图转录（去除口语化不流畅片段的规范文本），单一真值评估会导致模型选型与业务适配性脱节，甚至系统性歧视非典型用户。
### 方法关键点
以口吃语音为测试案例，覆盖encoder-decoder、CTC、transducer三类主流架构的11款ASR模型，分别采用逐字、意图两类转录参考开展基准测试，对比不同参考下的模型性能、排名差异。
### 关键结果
两类参考下的模型性能、排名存在显著差异，无任何一款模型可同时在两类参考下拿到最优结果，验证了必须按下游场景选择对应评估参考才能得到有效选型结论
