---
title: 'Explainability Assistant: A Conversational XAI Interface for Interpreting
  Energy Consumption Models'
title_zh: 可解释性助手：用于能耗模型解读的对话式XAI交互接口
authors:
- Rodion Krjutškov
- Eduard Barbu
- Nikos Sakkas
- Sofia Yfanti
affiliations:
- Nupp Software
- University of Tartu
- Apintech Ltd
- POLIS-21 Group
- Hellenic Mediterranean University
arxiv_id: '2609.11860'
url: https://arxiv.org/abs/2609.11860
pdf_url: https://arxiv.org/pdf/2609.11860
published: '2026-09-10'
collected: '2026-09-12'
category: Agent
direction: 对话式XAI Agent · LLM函数调用落地
tags:
- XAI
- Conversational AI
- LLM
- Function Calling
- Open Source
- Forecasting
one_liner: 基于LLM函数调用能力构建开源对话式XAI系统，无需任务微调，意图解析准确率达94%
practical_value: '- 业务侧模型解释类Agent可复用这套LLM函数调用架构，无需针对特定解释任务微调，大幅降低落地成本

  - 意图解析模块可参考该方案替换原有规则语法方案，能显著提升识别准确率，适配用户动态、上下文相关查询

  - 面向非技术用户的工具类产品，对话式界面相比传统仪表盘的用户接受度更高，可优先试点落地'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
能耗预测领域的复杂ML模型可解释性差，传统XAI仪表盘技术门槛高、不支持动态上下文查询，过往对话式XAI方案受限于固定自定义语法，意图解析准确率仅76.8%，泛化能力弱。
### 方法关键点
提出开源Explainability Assistant对话式XAI系统，基于现代LLM的函数调用能力封装底层XAI计算逻辑，支持用户通过自然语言提问触发对应解释工具调用，无需针对特定ML任务做微调即可适配不同业务场景。
### 关键结果
意图解析准确率达94%；与传统XAI仪表盘的专家对比评测显示，所有能源领域专家一致更偏好对话式交互界面，系统可用性显著提升，任务完成准确率稳定。
