---
title: 'CRM-Agent-Bench: Benchmarking Tool-Using Agents in Stateful Enterprise Environments'
title_zh: CRM-Agent-Bench：有状态企业环境下工具调用Agent基准测试集
authors:
- Monojit Banerjee
- Zhujun Lan
- Defu Cao
affiliations:
- Salesforce, Inc.
arxiv_id: '2610.32004'
url: https://arxiv.org/abs/2610.32004
pdf_url: https://arxiv.org/pdf/2610.32004
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: Agent评测 · 企业CRM场景
tags:
- Agent-Benchmark
- CRM
- Tool-Use
- Policy-Compliance
- Stateful-Interaction
one_liner: 推出面向CRM场景的可执行合约式Agent基准，联合评估结果、路径、合规性、运营效率四个维度
practical_value: '- 上线电商客服、售后退款、优惠券发放等业务Agent时，可复用可执行合约设计，从结果、执行路径、合规、成本四个维度联合校验，避免仅看话术正确但实际操作错误的问题

  - 工具调用Agent的评估逻辑可直接迁移：采用多维度合取校验机制，必须同时满足动作、参数、顺序、状态、回复全部要求才算成功，大幅降低评估误判

  - 企业级Agent选型不要只看准确率：相同准确率下不同模型的成本差异可达89倍，需结合具体业务域准确率、延迟、成本综合选型

  - 多轮交互Agent评测可复用on-policy用户模拟器设计，模拟器仅观察Agent公开回复生成下一轮交互，更贴近真实用户流程，评测结果更可靠'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有Agent基准多仅评估回复或工具调用准确率，未覆盖企业场景落地必需的执行流程正确性、状态变更合规性、运营效率等维度，类似「客服Agent声称完成退款但实际未调用接口、重复发放优惠券」的错误会直接造成业务损失，现有评估体系无法有效捕捉这类「说对但做错」的问题。
### 方法关键点
- 覆盖9个CRM业务域、36个能力标签的555个有状态多轮合成任务，无需对接真实CRM系统即可运行
- 每个任务绑定专属可执行合约，包含动作、参数、顺序、回复内容、目标状态、合规约束6类检查项，仅当所有声明的检查项全部通过才算任务成功
- 采用on-policy用户模拟器，仅能观察Agent的公开回复生成下一轮交互，更贴近真实用户对话逻辑；延迟、成本等运营指标单独统计，不纳入成功判定
### 关键结果
评测16款主流闭源/开源LLM，严格成功率区间为64.32%~83.60%；仅用回复正确性评估会高估成功率10.5~11.0个百分点；有合规约束的任务中，91.2%的试次可通过合规检查，但仅66.8%能通过全量合约校验；不同模型的评测成本差异最高可达89倍。
### 核心结论
企业级Agent的落地评估不能只看回复正确性，必须同时校验执行路径、状态变更、合规性、运营成本，才能避免「说对但做错」的业务损失。
