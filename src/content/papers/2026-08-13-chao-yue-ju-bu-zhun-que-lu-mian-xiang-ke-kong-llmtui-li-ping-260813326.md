---
title: 'Beyond Local Accuracy: A Protocol-Level Identifiability Audit for Controlled
  LLM Reasoning Evaluation'
title_zh: 超越局部准确率：面向可控LLM推理评估的协议层可识别性审计
authors:
- Junhao Luo
- Ning Huang
- Ziqi Sha
- Wenxuan Tang
- Wei Deng
affiliations:
- School of Statistics and Data Science, Southwestern University of Finance and Economics
arxiv_id: '2608.13326'
url: https://arxiv.org/abs/2608.13326
pdf_url: https://arxiv.org/pdf/2608.13326
published: '2026-08-13'
collected: '2026-08-14'
category: Eval
direction: LLM推理评估 · 协议可识别性校验
tags:
- LLM Evaluation
- Identifiability Audit
- Reasoning Benchmark
- Protocol Validity
- Evaluation Design
one_liner: 提出无需调用模型的LLM推理评估协议可识别性审计方法，验证静态准确率不等于干预响应保真度
practical_value: '- 做Agent/LLM4Rec能力评估时，可复用零模型调用的协议有效性预校验方法，避免仅靠静态准确率高估推理/召回排序能力

  - 评估LLM推理干预响应保真度时，可借鉴最小识别支持集O*的构造思路，大幅压缩评估所需case数量，降低评估成本

  - 做搜索推荐干预（规则调整、item池干预）后的效果评估时，需区分静态准确率和干预响应保真度两类指标，避免评估结论偏差'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM评估过度依赖静态基准准确率，混淆了静态正确性和干预响应保真度两类不同指标，评估协议本身的可识别性缺乏校验，导致得分高也无法反映真实推理能力。

### 方法关键点
1. 形式化有限行为策略类上的协议层可识别性审计框架，给定策略集、观测支撑集、待估指标，测试观测支撑集能否区分所有待估指标不同的策略对；
2. 审计全程无需调用模型，可在推理前完成评估设计有效性校验；
3. 可自动合成最小识别支撑集，压缩评估所需样本量。

### 关键结果数字
1. 仅用基础观测时7种确定性策略被归为同一等价类，全支撑集可完全区分7类策略；
2. 两种约束生成变体配对有效性均达1.0，但基础准确率0.620与选择性响应保真度0.324差距显著，另一确定性数据源上差距为0.646 vs 0.331；
3. 最小识别支撑集仅需2个单元，远低于全量36单元的张量规模。
