---
title: 'Verdict Without the Rule: Diagnosing and Auditing Regulatory Rule Sensitivity
  in LLM Compliance Systems'
title_zh: LLM 合规系统的监管规则敏感度诊断与审计方法
authors:
- Saisab Sadhu
- Aadit Sengupta
- Vinay kumar Sankarapu
- Pratinav Seth
affiliations:
- Lexsi Labs
arxiv_id: '2610.12313'
url: https://arxiv.org/abs/2610.12313
pdf_url: https://arxiv.org/pdf/2610.12313
published: '2026-10-08'
collected: '2026-10-10'
category: Eval
direction: LLM 合规系统可解释性评估
tags:
- LLM-compliance
- rule-sensitivity
- counterfactual-auditing
- activation-probing
- regulatory-NLP
one_liner: 通过反事实规则扰动测试，发现LLM合规系统判决常不依赖输入规则，专用guard模型表现远逊于通用模型
practical_value: '- 搭建电商内容审核、广告合规校验等规则驱动LLM系统时，不能仅以准确率为核心指标，需新增规则扰动测试验证输出确实依赖输入规则

  - 规则敏感的合规类任务无需优先选型专用guard模型，通用大模型准确率可达90%-92%，远高于专用guard模型的51%随机水平，可通过LoRA快速适配业务规则

  - 做Agent执行规则校验模块时，可复用本文OCS（输出规则敏感度）、ICS-delta（表征规则敏感度）指标做可解释性校验，避免规则不生效的隐形故障'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM合规系统默认判决结果依赖输入的监管/平台规则，但常规准确率评估无法验证规则是否真的被系统使用，易产生不可靠的法律类判定结果。
### 方法关键点
跨5个LLM、20个监管/平台政策域开展反事实测试：固定待审核案例不变，分别对规则做删除、跨域替换、义务取反三类扰动，设计两个维度评估规则敏感度：①OCS：输出判决结果是否变化；②ICS-delta：模型内部合规表征是否发生偏移。
### 关键结果数字
1. 多数模型判决对规则大幅扰动不敏感，专用guard模型规则敏感度、准确率最低，仅51%接近随机水平，通用大模型准确率达90-92%；
2. 仅在删除规则会改变原正确预测的难例上，模型才会紧密跟踪输入规则；
3. 优化prompt、干预模型内部表征都无法解决规则不敏感问题，仅准确率指标无法证明合规判决基于输入规则生成。
