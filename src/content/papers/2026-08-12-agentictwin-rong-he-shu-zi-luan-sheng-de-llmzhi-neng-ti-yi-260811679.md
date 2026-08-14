---
title: 'AgenticTwin: An Agentic LLM Framework Integrated with Digital Twin for Anomaly
  Detection'
title_zh: AgenticTwin：融合数字孪生的LLM智能体异常检测框架
authors:
- Touseef Hasan
- Mounika Ghanta
- Souvika Sarkar
- Ujjwal Guin
arxiv_id: '2608.11679'
url: https://arxiv.org/abs/2608.11679
pdf_url: https://arxiv.org/pdf/2608.11679
published: '2026-08-12'
collected: '2026-08-14'
category: Agent
direction: Agent 工业场景异常检测框架
tags:
- Agent
- LLM
- Digital Twin
- Anomaly Detection
- Framework
one_liner: 提出融合LLM智能体与数字孪生的异常检测框架，配套可复用基准评测流程
practical_value: '- 可借鉴结构化Agent协作+知识grounding思路，升级电商/广告系统的异常流量检测模块，提升刷单、恶意点击等异常行为的归因解释性

  - 可复用「传统规则/模型做异常初筛→LLM做推理解释」的分层架构，在降低大模型调用成本的同时，保障业务异常判定的可靠性

  - 构建业务自定义异常检测的评测体系时，可借鉴合成异常注入真实数据集的方法，低成本生成可控的评测样本集'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
数字孪生（DT）用于信息物理系统监测时，异常检测结果可解释性差，海量传感器数据人工分析难度极高，现有LLM的推理与解释能力尚未被有效整合进DT异常分析链路。
### 方法关键点
1. AgenticTwin框架将DT输出的异常分类结果作为LLM推理的事实基础，支持操作人员用自然语言查询异常相关信息
2. 构建基准评测流程：向真实气象传感器数据集注入合成异常，生成可控的操作人员查询样本
3. 验证轻量开源LLM在工业场景落地的可行性
### 关键结果
结构化Agent协作+知识 grounded 推理模式，在多类异常场景下，诊断质量、上下文检索效果、异常缓解方案质量均实现显著提升
