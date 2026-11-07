---
title: 'Understanding AI from the Inside: The State of Mechanistic Interpretability
  for AI Safety'
title_zh: 从内部理解AI：面向AI安全的机制可解释性研究现状
authors:
- Fazl Barez
- Tung-Yu Wu
- Hunar Batra
- Gabriele Dominici
- Florent Draye
- Yanai Elazar
- Damiano Fornasiere
- Antía García
- Abir Harrasse
- Riley Harris
affiliations:
- University of Oxford
- MIT
- Anthropic
- Mila, Université de Montréal
- Max Planck Institute for Intelligent Systems
arxiv_id: '2611.08438'
url: https://arxiv.org/abs/2611.08438
pdf_url: https://arxiv.org/pdf/2611.08438
published: '2026-11-05'
collected: '2026-11-07'
category: LLM
direction: 大模型机制可解释性 · AI安全
tags:
- Mechanistic Interpretability
- AI Safety
- Transformer
- Model Editing
- Survey
one_liner: 系统综述面向AI安全的机制可解释性研究，提出统一评估框架并开源实操代码库
practical_value: '- 可复用Transformer电路发现、特征提取方法，定位推荐/Agent大模型的不良输出触发神经元，优化内容风控效果

  - 借鉴训练数据归因方法，回溯大模型推荐/Agent决策的训练数据来源，满足业务合规性要求

  - 参考文中机制可解释性评估框架，量化验证垂直领域大模型的可控性，替代部分人工case评审

  - 复用知识编辑相关研究结论，低成本修正推荐/Agent大模型的错误偏好，无需全量微调'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
大模型能力与自主性持续提升，黑箱属性导致不可控风险上升，传统行为评估无法覆盖未知场景下的安全隐患，亟需从内部机制层面理解模型行为以保障AI安全。
### 方法关键点
系统梳理机制可解释性核心基础（特征、多语义性、Transformer计算、电路），覆盖特征提取分析、电路发现与因果验证、中间表征自然语言解释、学习动态、训练数据归因五大类方法；提出机制可解释性主张的统一评估框架，梳理6类研究方向的目标、假设与权衡。
### 关键结果
明确机制可解释性可支撑知识编辑、模型引导、运行监控三类AI安全能力，开源配套代码notebook库复现核心方法，降低实操门槛
