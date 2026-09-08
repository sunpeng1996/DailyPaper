---
title: How do LLMs Evaluate Perceived Moral Agency? Investigating Moral Decision-Making
  in Human-Artificial Agents Interactions
title_zh: LLM如何评估感知道德主体性？人-智能代理交互的道德决策研究
authors:
- Fernanda Mansilla
- Aloysius Tok
- Bahia Guellaï
- Farah Benamara
- Nancy F. Chen
affiliations:
- CNRS@CREATE, Singapore
- IRIT, Université de Toulouse, France
- CLLE, Université de Toulouse, France
- IPAL, Singapore
- Institute for Infocomm Research (I2R), A*STAR, Singapore
arxiv_id: '2609.05037'
url: https://arxiv.org/abs/2609.05037
pdf_url: https://arxiv.org/pdf/2609.05037
published: '2026-09-04'
collected: '2026-09-08'
category: Agent
direction: Agent 人-智能体交互道德决策评估
tags:
- Moral Agency
- LLM Evaluation
- Human-Agent Interaction
- Moral Decision Making
- Smart City
one_liner: 首次实证对比人类与多类LLM在智慧城市场景下对人和智能代理的感知道德主体性评估差异
practical_value: '- 开发客服、导购等面向用户的服务Agent时，可参考结论优先对高伤害、高紧急度场景做定向伦理规则约束，降低道德决策偏差

  - 涉及人机协同的配送、上门服务类Agent的合规校验模块，可引入危害严重性、场景紧急度两个核心特征做道德风险分级

  - 评估大模型伦理对齐效果时，可复用文中验证过的PMA量表框架设计测试Case，提升评估信效度'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM越来越多承担需提供道德建议的角色，各类智能代理广泛嵌入智慧城市场景，但LLM对不同主体的道德责任归因机制尚不明确，缺乏与人类评估基准的系统性对比。
### 方法关键点
适配经过学界验证的感知道德主体性（PMA）量表，面向190名人类受试者和多类主流LLM，在包含不同具身形态的人类/自主智能代理的拟真智慧城市场景下开展对比测试。
### 关键结果数字
1. 人类对人类主体的道德主体性感知显著高于人工代理；
2. LLM在具体道德困境决策中优先考虑伤害严重性、上下文紧急度，而非对代理本身的稳定评估，其上下文敏感度是人类评估者同类特征的放大版。
