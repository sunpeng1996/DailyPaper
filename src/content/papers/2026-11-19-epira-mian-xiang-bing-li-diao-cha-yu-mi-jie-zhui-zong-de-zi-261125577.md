---
title: 'Design and Evaluation of Epira: An Automated Interview System for Case Investigation
  and Contact Tracing'
title_zh: Epira：面向病例调查与密接追踪的自动化访谈系统设计与评估
authors:
- Ishita Asnani
- Shaghayegh Fazliani
- Zachary Ryan
- Kriyoshig Prasai
- Chirag Kumar
- Indra Gonzalez Ojeda
- Marc Lipsitch
- Madeleine Udell
affiliations:
- University of Illinois Urbana-Champaign
- Stanford University
arxiv_id: '2611.25577'
url: https://arxiv.org/abs/2611.25577
pdf_url: https://arxiv.org/pdf/2611.25577
published: '2026-11-19'
collected: '2026-11-22'
category: Agent
direction: 可控LLM Agent 结构化信息采集优化
tags:
- LLM Agent
- Structured Information Collection
- Protocol Control
- Local LLM
- User Evaluation
one_liner: 提出规则控制器搭配LLM的协议可控访谈系统Epira，提升结构化信息采集完整度与用户接受度
practical_value: '- 做用户偏好采集、售后访谈、调研类Agent时，可复用「规则控制器+LLM对话」架构：规则层强制要求采集字段、流程跳转，LLM负责自然语言交互，兼顾采集完整度与用户体验

  - 隐私敏感的用户信息采集场景，可优先测试本地开源LLM方案：论文验证了本地LLM与云端大模型的结构化采集效果差异极小，可兼顾隐私合规与业务效果

  - 评估信息采集类Agent时，可参考双实验框架：先做带标答的模拟测试验证采集准确率，再做真人测试验证可用性、信任度，全面覆盖效果与体验指标'
score: 6
source: arxiv-cs.HC
depth: abstract
---

## 动机
病例调查、密接追踪等结构化信息采集场景，传统表单灵活度不足无法解答用户疑问，开放式LLM chatbot容易偏离采集协议，人工采集人力成本极高。
## 方法关键点
1. 采用LLM对话层+规则控制器双层架构：规则层强制约束必问问题、安全流转逻辑、结构化输出格式，支持上传问卷快速适配新采集场景；
2. 同时兼容本地开源LLM（Qwen2.5）与云端大模型（GPT-5.4）两种部署方案。
## 关键结果数字
- 模拟测试：Epira比同底座开放式LLM的必填字段采集率高31.1~41.9pct，本地LLM版本必填字段采集率达88.9%、密接信息采集率达60.1%；
- 真人测试：任务完成率100%，SUS系统可用性得分82.95，用户信任度得分3.85/5
