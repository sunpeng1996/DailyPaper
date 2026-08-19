---
title: 'Delegation Asymmetry in Agentic Recommender Systems: Measuring Two-Sided Receptivity
  in Online Dating'
title_zh: 智能体推荐系统的委托不对称性：在线约会场景双边接受度测量
authors:
- Daria Leshchikova
- Valentina V. Kuskova
- Dmitry Zaytsev
- Valerii Klimov
affiliations:
- Fleamily, Inc.
- University of Notre Dame
- Lucy Family Institute for Data & Society
arxiv_id: '2608.18058'
url: https://arxiv.org/abs/2608.18058
pdf_url: https://arxiv.org/pdf/2608.18058
published: '2026-08-18'
collected: '2026-08-19'
category: Agent
direction: Agent 推荐系统用户接受度度量
tags:
- LLM Agents
- Agentic Recommender
- User Acceptance
- Two-sided Market
- Online Dating
one_liner: 通过大规模调研量化智能体推荐场景代发/接收智能体消息的意愿差异，给出可落地设计优化杠杆
practical_value: '- 上线Agent代沟通类功能前可复用论文提出的四阶段接受度审计流程，提前摸底双边用户意愿，避免上线后大量无效请求损耗用户信任

  - 双边匹配类场景（约会、招聘、二手交易等）的Agent功能必须将接收方同意作为第一优先级设计原语，不能仅做发送方授权

  - 可将接收方接受度评分作为路由特征，把Agent发起的请求优先分发给高接受度用户，实测可将单请求 engagement 提升3倍

  - 功能上线可按侵入度梯度推进：先上被动生成类功能（如简介、话术建议），再上可控辅助沟通，最后试点全自主代聊'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM智能体代用户沟通的产品模式快速落地，但现有研究仅关注发送方使用智能体的意愿，忽略了接收方接受他人智能体消息的意愿，双边意愿错配会导致大量无效请求、损耗用户信任，尤其是双边匹配类信任敏感场景，该问题此前未被联合量化。
### 方法关键点
- 数据：面向头部约会平台活跃用户开展两次大规模调研，N=2894用于生成式功能接受度调研，N=2617用于自主对话智能体接受度调研，覆盖两种语言
- 模型：基于分级响应模型构建双维度潜变量测量模型，分别拟合用户发送接受度（愿意用智能体代发消息）、接收接受度（愿意接他人智能体消息）两个独立构念
- 框架：提出可复用的四阶段接受度审计流程：工具设计→测量建模→外样本验证→市场反事实仿真
### 关键结果
- 双维度模型显著优于单维度模型（ΔBIC=52），发送/接收接受度相关系数达0.92但属于完全独立的构念
- 存在显著委托不对称性：用户愿意使用智能体代发的阈值为θ=-0.38，愿意接收他人智能体消息的阈值为θ=+0.32，差值达0.71个标准差，整体部署意愿是接受意愿的3倍
- 反事实仿真：随机配对下仅4-13%的双边组合同时满足发送/接受意愿；基于接收接受度路由可将单请求engagement提升3.1倍，外样本验证AUC达0.88；强制互惠规则会排除2/3潜在使用者，交互量减半
### 最值得记住的一句话
Agent 推荐系统按发送方需求建设，但成败完全由接收方意愿决定
