---
title: Untangling the Mechanisms of Misleading Context in Medical Question Answering
title_zh: 医学问答场景下误导性上下文的作用机制拆解
authors:
- Robin Linzmayer
- Noémie Elhadad
affiliations:
- Department of Computer Science, Columbia University
- Department of Biomedical Informatics, Columbia University
arxiv_id: '2609.02754'
url: https://arxiv.org/abs/2609.02754
pdf_url: https://arxiv.org/pdf/2609.02754
published: '2026-09-02'
collected: '2026-09-04'
category: LLM
direction: 大模型安全 · 误导性上下文干扰机制
tags:
- LLM Safety
- Medical QA
- Chain-of-Thought
- Misleading Context
- Monitorability
one_liner: 拆解医学问答中两类误导性上下文的干扰机制，验证开放推理链可大幅提升错误决策检出率
practical_value: '- 搭建电商RAG导购、Agent咨询系统时，优先对无支撑的断言类误导输入做检测过滤，这类干扰对LLM决策的影响远高于伪造证据类

  - 自研Agent/LLM业务应用时强制留存完整推理链，基于推理链做异常决策监控的准确率比仅看最终输出高2倍以上

  - 做LLM输出质检时，针对断言类误导输入增加专项校验规则，这类干扰被模型主动披露的概率更低，更容易漏判'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
LLM已达到医学问答专家级性能，但误导性上下文会严重破坏其医学判断，干扰机制与可监控性缺乏系统性研究
### 方法关键点
在经临床评审的MedMisBench医学推理子集（共8627条QA）中，注入伪造证据、无支撑断言两类误导性上下文，测试3款推理模型（2款开放全量推理链、1款仅输出结果的前沿模型）的抗干扰表现、误导信息披露行为、推理干扰路径与异常检测效果
### 关键结果数字
- 所有模型对断言类干扰的接受度比伪造证据高10~27个百分点
- 误导信息在推理链中披露率达81%~98%，但仅在7%~90%的最终输出中披露，断言类披露率更低
- 基于开放推理链的LLM监控在5%假阳性率下可检出78%的错误决策，远高于仅看输出的最高32%检出率
