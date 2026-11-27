---
title: Who Makes the Decision? Auditing an Agentic LLM Pipeline for Illicit Cryptocurrency
  Transaction Monitoring
title_zh: 面向加密货币非法交易监控的智能体LLM链路决策归因审计
authors:
- Vaishnavi Chaughule
- Yuchen Zhang
- Mohammed Ahnaf Tajwar
- Sai Akshay Menta
- Saanidhya Vats
- Vinija Jain
- Aman Chadha
- Divya Chaudhary
affiliations:
- Khoury College of Computer Sciences, Northeastern University
- Meta
- Apple
arxiv_id: '2611.29829'
url: https://arxiv.org/abs/2611.29829
pdf_url: https://arxiv.org/pdf/2611.29829
published: '2026-11-21'
collected: '2026-11-27'
category: Agent
direction: Agent 决策归因与可解释性审计
tags:
- Agent
- LLM
- RAG
- Decision Attribution
- Explainability
- Audit
one_liner: 提出三层决策溯源协议审计Agent pipeline，量化各组件贡献与LLM裁判行为缺陷
practical_value: '- 多组件Agent pipeline上线前可复用三层归因协议（实际因果、干预式Shapley值、上游风险传导）量化各模块决策权重，快速定位系统瓶颈

  - 风控类LLM决策系统需单独测试LLM对输入特征的偏向性，避免上游隐含特征干扰LLM独立判断，降低误判率

  - LLM生成合规性依据场景，不能仅用子串匹配校验引用有效性，需叠加规则+语义匹配双重校验，避免虚假引用'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前结合图检测器、规则、RAG、LLM裁判的Agent pipeline多用于加密货币非法交易监控，仅评估端到端精度或生成理据质量，无法追溯决策来源，可解释性不足。
### 方法关键点
设计三层决策溯源协议：1）单案例实际因果判定；2）干预式Shapley值量化各组件决策贡献；3）上游风险评分传导中介分析。同时控制变量测试LLM裁判在不同backbone、prompt、输入证据下的行为。
### 关键结果
- 确定性钱包分规则贡献94%的异常标记决策，验证闸门过滤了LLM裁判标注的大部分合法交易误判
- LLM优先跟随注入的风险评分，上下文过短无输出，会引用不相关合规条款且能被子串校验通过
- 隐藏风险评分无法修正偏差，因证据收集阶段已隐含评分信息
