---
title: 'The Context Access Divide: Interaction-Level Architecture as a Complementary
  Dimension of Agentic Inequality'
title_zh: 语境访问鸿沟：作为智能体不平等补充维度的交互层架构
authors:
- Masahiro Fujita
affiliations:
- Kansai University
arxiv_id: '2607.08495'
url: https://arxiv.org/abs/2607.08495
pdf_url: https://arxiv.org/pdf/2607.08495
published: '2026-07-09'
collected: '2026-07-10'
category: Agent
direction: 智能体不平等 · 语境访问架构分析
tags:
- Agentic Inequality
- RAG
- MCP
- Context Retrieval
- Knowledge Work
one_liner: 提出语境访问鸿沟这一交互层维度，补充现有智能体不平等框架，揭示RAG/MCP架构差异导致的AI效用分层
practical_value: '- 做企业级Agent服务时，优先配置Open DCRM能力（基于MCP对接跨生态数据源），可显著提升知识密集型岗位（如电商运营、策略分析、广告投放）的AI使用效率，参考Block的落地案例，部署MCP连通的Goose
  Agent后工程师产能提升40%

  - 面向C端的AI助理/电商导购Agent可分层设计语境架构：基础版用MAM，付费会员提供生态内Walled DCRM，高阶付费开放MCP对接能力，既降低用户门槛又制造付费梯度，同时可利用Walled
  DCRM实现生态锁客

  - 评估AI工具对业务的价值时，不能仅看模型参数/订阅 tier，要额外考核语境访问架构的适配性：若业务需要跨多数据源（如商家后台、电商平台、广告投放后台）分析，Open
  DCRM的收益远高于同模型等级的MAM方案'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有智能体不平等分析框架仅从个体/组织层面的可用性、质量、数量三个维度衡量差距，无法解释两名订阅同一AI服务、使用同等级模型的用户，因语境获取方式差异产生的AI效用断层；尤其对知识密集型工作者，手动梳理上传语境的认知负担会完全抵消AI的效率优势，这一结构型差异带来的生产力分层长期被忽略。

### 方法关键点
- 划分三类语境供给架构：Manual Attachment Model（MAM，用户手动上传所有语境）、Walled DCRM（单厂商生态内自动检索语境，如微软365 Copilot、谷歌Gemini联动自有生态数据）、Open DCRM（基于MCP等开放协议跨生态自动检索语境）
- 引入认知心理学fan效应建模用户手动召回语境的概率：随个人语料库规模N增大，召回准确率呈逻辑斯蒂衰减；多语境依赖任务的MAM成功率为单文档召回概率的k次方（k为任务所需关键语境数量），呈指数级衰减
- 对比三类架构的任务成功率随语料库规模的变化规律，结合MCP生态的真实落地数据拆解分层机制

### 关键结果
- 模拟显示当k=3（任务需要3份关键语境）、语料库规模N=10000时，Open DCRM任务成功率约0.86，是MAM的5300倍；Walled DCRM（60%语料在生态内）成功率稳定在0.19左右
- MCP协议发布13个月后SDK月下载量突破9700万，已有17468个公共MCP服务器上线，但仅41%的科技公司资深技术负责人实现了生产级MCP部署，普通知识工作者的DCRM渗透率更低
- 企业落地案例：Block部署MCP连通的内部Goose Agent后，工程师产能提升40%，原需1个季度开发的风险模型可在极短时间内交付

### 核心洞见
AI工具的实际效用不是由模型能力单独决定的，而是由「谁承担语境梳理的认知负担」这一交互架构决定的，手动上传语境的模式对大语料库高依赖任务的成功率会发生组合式崩溃
