---
title: 'AID-Guard: Stateful Authorization for Delegated Agent Effects'
title_zh: AID-Guard：面向Agent委托执行的有状态授权协议
authors:
- Yingzhe Tong
- Leyu Dai
- Songhui Guo
affiliations:
- Information Engineering University
arxiv_id: '2608.21159'
url: https://arxiv.org/abs/2608.21159
pdf_url: https://arxiv.org/pdf/2608.21159
published: '2026-08-21'
collected: '2026-08-24'
category: Agent
direction: Agent工具调用安全 · 有状态授权
tags:
- Agent Security
- Authorization Protocol
- Tool Calling
- Idempotency
- Access Control
one_liner: 提出有状态授权协议AID-Guard，解决Agent工具调用一次授权多次生效的安全问题
practical_value: '- 电商/广告场景下的高风险Agent操作（自动发券、自动退款、广告预算调整），不要只在请求入口做权限校验，必须在提交到第三方执行的最终节点二次校验请求参数和当前系统状态，避免中间链路被篡改

  - 重试流程不要直接生成新的授权凭证，必须先通过第三方接口确认前序请求未生效，且安装交付栅栏拦截前序延迟请求后，才能释放原配额或生成唯一的后继授权，完美适配支付、短信等高幂等要求的场景

  - 全链路授权状态和执行证据要独立持久化存储，和授权、执行节点做强绑定，支持可审计的追溯，满足电商交易、广告投放的合规要求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前工具调用型AI Agent的授权仅在入口请求阶段校验，后续存在请求被篡改、响应丢失导致重试重复触发操作的风险，出现一次授权多次生效、执行内容与授权不一致的安全问题，现有方案未覆盖授权到执行的全链路状态绑定，无法解决重试、崩溃、并发场景下的授权滥用问题。
### 方法关键点
- 设计三段式强制授权校验节点：H1绑定用户授权上下文，H2下发单次使用能力凭证并预留配额，H3在执行边界校验凭证并标记授权已使用，每个节点重新校验上下文状态
- 提交到第三方执行的commit节点D2二次校验请求内容与当前第三方状态，确保与授权内容完全一致
- 结果不明确（如响应丢失）场景下保留原始授权配额，必须拿到第三方出具的未生效证明、安装交付栅栏后，才能释放配额或生成唯一后继授权，避免重复执行
- 全链路操作证据独立存证，支持公开完整性校验和特权重放，满足审计要求
### 关键实验
在MCP回环、Stripe支付、Resend邮件三个场景下测试：13次实时请求篡改无未授权操作；210次Stripe流程测试全部符合预期；30次并发确认/取消竞争、10次崩溃恢复场景无重复执行；完全控制请求方的情况下拦截全部44次攻击；严格匹配模式下良性请求通过率下降35.4~43.8pct，Typed 3x宽松模式下比严格模式多9~10次良性通过且无安全风险。

最值得记住的结论：Agent高风险操作的授权不能仅做入口校验，必须与最终执行结果做全生命周期的状态绑定，才能避免授权滥用风险。
