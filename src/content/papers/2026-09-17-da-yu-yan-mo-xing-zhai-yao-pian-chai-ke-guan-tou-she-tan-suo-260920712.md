---
title: 'Summarization Bias: The Directional Collapse of Objective Projection into
  Told-Mode Labels in Large Language Models --- A Conceptual Framework and Registered
  Test Protocol'
title_zh: 大语言模型摘要偏差：客观投射坍缩为明示标签的框架与预注册测试
authors:
- Levent Bulut
affiliations:
- Independent Researcher
arxiv_id: '2609.20712'
url: https://arxiv.org/abs/2609.20712
pdf_url: https://arxiv.org/pdf/2609.20712
published: '2026-09-17'
collected: '2026-09-18'
category: LLM
direction: LLM偏差 · 叙事理解与评估
tags:
- LLM Bias
- Narrative Understanding
- LLM-as-Judge
- Reward Model
- Pre-registration
one_liner: 定义LLM叙事处理的摘要偏差概念，提出双运行机制与预注册验证方案
practical_value: '- 搭建LLM-as-judge的文案/内容评估链路时，需补充对隐含表达（如软种草文案、暗示情绪）的识别校验，避免LLM偏好直白表达导致优质内容被误判

  - 训练营销话术/种草文案生成LLM时，可加入shown模式（间接表达）的显式监督，缓解摘要偏差导致的生成内容过于生硬、用户接受度低的问题

  - 做用户评论情感分析任务时，需针对性优化间接情绪表达样本的识别逻辑，降低LLM偏向明示标签带来的分类误差'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM越来越多地作为内容评估器、Reward Model使用，但其叙事处理方向的系统性偏差未被明确界定，可能导致内容质量评估失真、生成内容向直白表达退化。
### 方法关键点
1. 提出「摘要偏差」概念，基于叙事told-shown轴做定义：told模式为直接明示信息/情绪，无需读者推理；shown模式为通过线索间接传递内容，需读者推理重构（即客观投射）
2. 假设偏差存在两种运行机制：生成机制下LLM被要求间接表达情绪时会默认输出明示内容；评估机制下LLM作为评估器会偏好直白内容、低估间接表达的质量
3. 预注册双机制的验证测试方案，明确偏差不成立的判定规则
### 关键结果
目前尚未完成正式验证，已完成的独立信度研究结果与该偏差假设方向一致
