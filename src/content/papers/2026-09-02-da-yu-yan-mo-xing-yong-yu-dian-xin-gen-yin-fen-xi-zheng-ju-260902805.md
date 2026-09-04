---
title: 'Large Language Models (LLMs) for Telecom Root Cause Analysis (RCA): A Structured
  Reasoning Framework for Evidence-Grounded Diagnosis'
title_zh: 大语言模型用于电信根因分析：证据驱动的结构化推理框架
authors:
- Hao Zhou
- Mandar Kulkarni
- Hao Chen
- Yan Xin
- Charlie
- Zhang
arxiv_id: '2609.02805'
url: https://arxiv.org/abs/2609.02805
pdf_url: https://arxiv.org/pdf/2609.02805
published: '2026-09-02'
collected: '2026-09-04'
category: Reasoning
direction: 大模型结构化推理 · 根因分析
tags:
- LLM
- Structured Reasoning
- Root Cause Analysis
- Hallucination Mitigation
- Knowledge Grounding
one_liner: 提出适配电信根因分析的LLM结构化推理框架，缓解幻觉，提升诊断准确率与决策一致性
practical_value: '- 做推荐/广告系统异常根因排查、投放故障诊断等垂直领域LLM任务时，可先将多源异构日志、业务指标统一整理为规范上下文，降低LLM理解成本

  - 垂直场景LLM推理可强制要求输出决策路径+对应支撑证据，能有效缓解幻觉，提升输出的稳定性和可解释性

  - 复杂跨层依赖场景的LLM落地，可先对齐领域知识设计推理流程，无需全量微调即可获得较明显的效果提升'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
电信5G/6G网络跨层依赖复杂，根因分析（RCA）难度高；原生LLM直接用于RCA易出现幻觉、推理不稳定、与结构化网络证据对齐差的问题，落地效果无法满足要求。
### 方法关键点
首先梳理了电信RCA从规则驱动、传统ML到LLM赋能的技术演进路径，总结了结构化推理、RAG知识接地、Agent编排、可验证推理等前沿范式；基于上述insights的结构化推理框架分三步执行：1）将异构网络遥测数据统一整理为规范上下文；2）诊断过程强制要求输出完整决策路径；3）最终生成证据支撑的诊断解释，实现可靠故障识别。
### 关键结果
在TeleLogs、TelecomTS两个5G RCA公开数据集上，相比各类基线方法，框架的诊断准确率、决策一致性均实现稳定提升，验证了结构化推理设计在垂直领域LLM落地中的核心价值。
