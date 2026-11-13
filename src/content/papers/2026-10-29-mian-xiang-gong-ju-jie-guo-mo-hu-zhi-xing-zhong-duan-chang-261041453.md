---
title: Evidence-Guided Recovery for AI Agents with Ambiguous Tool Outcomes and Partial
  Execution
title_zh: 面向工具结果模糊、执行中断场景的AI Agent证据引导恢复机制
authors:
- Genliang Zhu
- Xiaobo Chen
- Ziyuan Wang
- Chu Wang
affiliations:
- Accentrust
- Georgia Institute of Technology
- University of Massachusetts Amherst
- Duke University
- University of Illinois Urbana-Champaign
arxiv_id: '2610.41453'
url: https://arxiv.org/abs/2610.41453
pdf_url: https://arxiv.org/pdf/2610.41453
published: '2026-10-29'
collected: '2026-11-13'
category: Agent
direction: AI Agent 工具调用故障恢复
tags:
- AI Agent
- Tool Use
- Failure Recovery
- Partial Observation
- Planning
one_liner: 提出基于公开证据的AI Agent故障恢复框架，解决工具调用超时后的未知状态安全续跑问题
practical_value: '- 电商/广告自动化Agent（如订单处理、券包发放、售后履约Agent）遇到第三方API超时（支付、物流、短信接口）时，可复用本文的公共证据可准入检查逻辑，避免重复扣款、重复发券、重复通知等不可逆操作风险

  - Agent工具调用模块可直接接入本文的终端证书校验逻辑，区分「实际任务完成」和「公开证据可证的安全完成」，避免向用户返回虚假成功状态（如显示支付成功实际未到账）

  - 多工具串联的推荐运营Agent（如自动发push、生成优惠券、更新商品标签的工作流）遇到部分执行失败时，可复用本文的部分观察规划方法，优先执行独立无依赖的任务，降低故障对整体工作流的影响'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
AI Agent调用第三方工具时经常遇到超时、响应丢失、部分执行失败等问题，无法判断操作是否实际生效：直接重试可能导致重复扣费、重复通知等不可逆风险，直接终止则会遗漏未完成的业务义务，现有恢复机制大多依赖服务端配合的原子性保证，无法适配无协作能力的第三方工具场景。

### 方法关键点
- 维护与公开观测兼容的所有可能状态集合，所有恢复动作需经过可准入检查，确保不会在任何可能状态下引入新的违规（如重复操作、依赖错误）
- 设计终端证书机制，只有所有可能状态均满足任务目标、不存在未决延迟副作用时，才判定为安全完成，避免将实际未生效的操作判定为成功
- 结合Partial Observation下的规划方法，在安全动作范围内选择证据获取、续跑、重试、补偿、等待、人工移交等最优动作，优先级为完成概率>义务完成度>恢复成本

### 关键实验结果
- 37个合成业务场景测试：规则基线、贪心策略、本文规划方法的安全完成率均为28/37，规划方法相比规则基线节省4个合成费用单位，多消耗约9.4秒计算资源
- 58对预注册LLM对照实验：仅提供证据提示的基线安全完成率为9/58，叠加本文规划建议后完成率达30/58，提升36.2个百分点（p=0.0078），总请求数从399降至272

### 核心结论
Agent故障恢复的核心不是追求100%任务完成，而是在不引入新风险的前提下最大化可验证的安全完成率，未知状态必须明确标记，而非默认判定为成功或失败。
