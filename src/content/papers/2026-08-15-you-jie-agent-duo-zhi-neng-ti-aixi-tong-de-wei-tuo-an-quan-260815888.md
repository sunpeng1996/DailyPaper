---
title: 'Bounded Agents: Delegation Security for Multi-Agent AI Systems'
title_zh: 有界Agent：多智能体AI系统的委托安全架构
authors:
- Xabier Muruaga
affiliations:
- Independent Researcher
arxiv_id: '2608.15888'
url: https://arxiv.org/abs/2608.15888
pdf_url: https://arxiv.org/pdf/2608.15888
published: '2026-08-15'
collected: '2026-08-20'
category: Agent
direction: 多Agent系统 委托权限安全架构
tags:
- Multi-Agent Security
- Authorization
- Prompt Injection
- Delegation Control
- Access Control
one_liner: 提出APC架构在模型外通过会话级权限校验阻断多Agent权限滥用与Prompt注入攻击
practical_value: '- 电商导购Agent、广告投放Agent等需要调用工具/子Agent的业务，可直接在工具网关层复用APC的6项权限校验逻辑，不要将权限校验规则写在System
  Prompt中，避免被Prompt注入绕过

  - 可借鉴composition closure设计，针对业务高风险操作组合（如读取用户隐私+发送外部消息、修改订单+触发转账）做会话级联动拦截，避免单步权限校验遗漏组合风险

  - 多Agent协作场景（如电商运营多Agent分工、推荐系统多Agent调优）可复用blast radius monotonicity设计，每向下委托一级就收缩一次权限范围与操作预算，避免单Agent被攻陷后全链路权限泄露

  - 做Agent安全评估时可参考论文的compromised-model评估方法，直接注入攻击工具调用跳过模型鲁棒性干扰，单独验证权限架构的防御能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent权限机制面向人类设计，采用静态单步校验，不感知会话历史、不做委托时的权限收缩，也无法拦截多个合法操作组合出的风险结果（如读取机密文档+发送外部邮件会造成数据泄露，但两步操作单独校验均合法）；且多数部署将安全规则写在Prompt中，极易被Prompt注入绕过，本质上是权限架构缺陷而非模型对齐问题。

### 方法关键点
- 采用PEP/PDP分离的网关层架构，所有工具调用必须经过模型外的网关校验，Agent无法绕过
- 权限范围每次委托时取交集，仅能收缩不能放大；委托预算（深度、风险半径、操作成本等）逐跳递减，保证blast radius monotonicity，越下层Agent风险边界越小
- 基于会话级动作历史做composition closure校验，禁止预设的风险操作组合，支持k阶连续动作拦截多步复杂攻击
- 绑定初始预声明的任务意图，所有操作必须匹配任务范围，偏离直接拦截

### 关键结果
在InjecAgent、AgentDojo、ASB共3154个测试用例上验证，对比无防御基线：所有数据窃取/外漏攻击拦截率100%，破坏类攻击成功率从38.6%降至4.0%，操作篡改类成功率从90.5%降至12.1%；99分位权限校验延迟仅0.24ms，人工审批模式下对合法任务的效用损失仅8.6个百分点。

最值得记住的一句话：Prompt注入的风险本质是权限架构问题，而非单纯的模型鲁棒性问题，Agent没有对应操作权限的话，无论注入什么内容都无法造成实质危害。
