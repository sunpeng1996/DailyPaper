---
title: Privacy Preference Controls for Agentic Systems
title_zh: 面向智能体系统的可执行隐私偏好控制框架与落地方案
authors:
- Shreya Kochar
- Peeranat Sugsavanvit
- Vidur Gupta
- Joseph A. Calandrino
- Deepak Kumar
- Brett Frischmann
- Sebastian Zimmeck
affiliations:
- University of California, San Diego
- Wesleyan University
- Stanford University
- Carnegie Mellon University
- Villanova University
arxiv_id: '2610.29929'
url: https://arxiv.org/abs/2610.29929
pdf_url: https://arxiv.org/pdf/2610.29929
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: Agent 系统隐私偏好控制与合规落地
tags:
- AI Agents
- Privacy Preference
- MCP
- A2A Protocol
- Data Minimization
one_liner: 提出覆盖Agent全生命周期的5类隐私控制分类法，完成30款AI产品审计并实现8个开源协议适配原型
practical_value: '- 搭建电商导购Agent、个性化推荐Agent时，可直接复用论文的5类（存在、采集、二次使用、留存、自治）隐私控制维度，快速对齐GDPR/CCPA等监管要求，降低合规风险

  - MCP/A2A协议下无需修改原生协议结构，可通过meta字段自定义传递用户隐私信号，搭配Interceptor在工具调用、Agent级联的每一跳做权限校验，工程落地成本极低

  - 审计显示当前仅14/29的主流AI产品支持广告相关数据分享的用户opt-out，电商Agent可优先上线该粒度的隐私控制选项，既能满足监管要求也能提升用户信任'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有Web隐私控制（如GPC）基于用户主动交互的模式，完全无法适配Agent自主行动、多跳级联调用、长期驻留的新特性；Agent访问用户敏感数据时易出现过度采集、无感知分享、私自二次使用等问题，且当前主流AI产品的隐私控制覆盖度极低，合规风险极高。

### 方法关键点
1. 结合现有隐私法规、过往用户隐私行为研究、30款主流AI Agent产品的实证审计结果，提出覆盖Agent全生命周期的5大类可执行隐私偏好分类法，下分14个细分控制维度，覆盖从Agent激活到任务结束后销毁的全流程
2. 适配MCP、A2A两大主流Agent协议，利用协议原生meta字段传递用户隐私信号，在工具调用、Agent级联的各个节点通过拦截器实现权限校验，无需改动协议原生结构
3. 开发8个覆盖旅行规划、医疗咨询、商品调研等场景的开源原型，验证控制框架的落地可行性

### 关键结果
审计30款头部AI产品发现，仅72%的现有隐私控制可被分类法覆盖，仅14/29的产品支持用户opt-out广告相关的数据售卖/分享，仅6/30支持关闭人工审核，仅40%的控制项公开默认状态；8个场景原型验证隐私控制可在不降低用户任务体验的前提下实现。

### 最值得记住的一句话
Agent系统的隐私治理需从设计阶段嵌入，以用户授权的任务边界替代企业定义的业务目的作为数据最小化的判断标准，才能从根源上避免重蹈Web时代监控资本主义的覆辙。
