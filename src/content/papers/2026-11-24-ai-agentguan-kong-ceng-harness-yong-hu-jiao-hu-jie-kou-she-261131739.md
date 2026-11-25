---
title: Where is the Interface for the AI Harness?
title_zh: AI Agent管控层（Harness）用户交互接口设计方向研究
authors:
- Wafa Johal
- Sarah Schombs
affiliations:
- The University of Melbourne
arxiv_id: '2611.31739'
url: https://arxiv.org/abs/2611.31739
pdf_url: https://arxiv.org/pdf/2611.31739
published: '2026-11-24'
collected: '2026-11-25'
category: Agent
direction: Agent人机交互 · Harness 设计优化
tags:
- AI Agent
- HCI
- Agent Harness
- Human-Agent Collaboration
- User Control
one_liner: 提出AI Agent交互的规范、监督两大新鸿沟，明确终端用户可配置的Harness设计框架
practical_value: '- 搭建业务Agent（如选品Agent、投放Agent）时，必须拆分Harness的默认规则和用户可配置规则，核心红线（如不得爬取涉密数据、不得超预算投放）设为不可修改的默认规则，避免用户漏写prompt导致违规

  - 给运营/商家的Agent操作界面不能仅留空白prompt框，要预置可勾选的边界规则模板（如「遇到权限拒绝立即上报」「预算消耗超80%暂停通知」）、自定义checkpoint配置项，降低用户的规范鸿沟

  - Agent执行长链路任务（如跨平台投放效果调研、大促用户分层运营）时，要在关键节点主动上报执行日志、决策依据，异常场景立即中断等待人工确认，缩小用户的监督鸿沟'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有Agent交互仅提供空白prompt框，用户委托长链路任务时既无法完整预设所有边界规则、意外处理逻辑，也无法全程监控Agent多步执行过程，已出现AI Agent违规爬取政府敏感数据等生产事故。传统HCI领域的执行、评估两大交互鸿沟建立在用户全程在场的交互假设上，完全不适用Agent委托式、用户离线的交互场景，急需明确Agent管控层（Harness）的用户交互设计范式。
### 方法关键点
1. 提出两大适配Agent场景的新交互鸿沟：①**规范鸿沟**：用户真实需求与用prompt准确传达边界规则、意外处理逻辑的能力差，属于认知层面问题，无法靠prompt工程彻底解决；②**监督鸿沟**：Agent多步执行的决策、工具调用动作与用户感知、控制能力的差距，长链路任务下Agent执行逻辑会逐渐偏离用户初始请求，用户缺席时无法及时纠正。
2. 明确Harness分层设计原则：拆分Harness为默认规则层和用户可配置层，核心红线（如不得入侵系统、不得违规获取隐私数据）设为全局默认规则，无需用户指定；边界规则、触发上报阈值、checkpoint规则等对应用户业务需求的部分，提供可视化配置界面而非要求用户写在prompt中。
3. 给出跨鸿沟落地路径：执行前支持用户与Agent共同规划任务路径、预设边界；执行中异常场景立即中断请求人工输入；执行后输出完整的动作、决策、跳过项报告。
本研究为HCI领域观点性论文，无量化实验结果。
### 核心结论
设计Agent系统时必须回答两个核心问题：Harness的哪些部分应该开放给终端用户配置，哪些应该作为默认规则由设计侧提供？
