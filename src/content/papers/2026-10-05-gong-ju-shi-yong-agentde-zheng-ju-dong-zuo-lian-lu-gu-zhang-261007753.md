---
title: 'From Evidence to Action: How Tool-Using Agents Fail'
title_zh: 工具使用Agent的证据-动作链路故障分析与评测基准SAFEACTBENCH
authors:
- Hongzhan Lin
- Shidong Cao
- Ziyang Luo
- Wenhao Chai
- Mong-Li Lee
- Wynne Hsu
affiliations:
- National University of Singapore
- Hong Kong Baptist University
- Amazon Web Services
- Princeton University
arxiv_id: '2610.07753'
url: https://arxiv.org/abs/2610.07753
pdf_url: https://arxiv.org/pdf/2610.07753
published: '2026-10-05'
collected: '2026-10-07'
category: Agent
direction: Agent 工具调用证据合规性评测
tags:
- Tool-Using Agent
- Agent Evaluation
- Evidence Grounding
- Consequential Action
- Benchmark
one_liner: 提出面向工具使用Agent证据-动作链路合规性的评测基准SAFEACTBENCH，定位链路各环节故障模式
practical_value: '- 电商售后/客服Agent的改状态操作（退款、发券、改权益）可复用Evidence Ledger机制，对每个consequential
  action前置校验必填证据（用户身份、订单状态、政策匹配），从流程上避免误操作

  - 多步Agent工作流可引入确定性轨迹校验逻辑，无需LLM裁判，通过依赖DAG和证据溯源即可自动审计工作流合规性，大幅降低线上巡检成本

  - 开发Agent时不要仅用静态工具调用准确率评估性能，实测显示静态准确率95%的模型在交互式执行场景下准确率仅52%，需优先在真实交互场景做证据合规性压测

  - 相同模型下不同Harness的性能差距可达4-6个百分点，优先适配官方配套Harness可提升证据收集和动作执行的准确性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前工具使用Agent广泛应用于退款、状态更新、消息推送等会改变外部状态的consequential action场景，现有评测仅校验最终结果正确性，忽略动作执行前是否已收集到对应合法证据，极易出现结果正确但流程违规的问题（如查询A订单信息却给B订单退款），且多步工作流中这类故障定位难度极高，亟需可量化的证据-动作链路评测体系。
### 方法关键点
- 推出SAFEACTBENCH基准，覆盖客户运营、财务、智能家居等6个业务域共656个评测用例，包含静态决策、调查后终止、单动作执行、线性多步工作流、DAG依赖多步工作流5种交互协议
- 设计带溯源的Evidence Ledger，绑定每条证据对应的实体、状态、来源，仅当目标动作所有前置证据都在执行前完成采集才判定为合规
- 实现确定性轨迹评估器，无需LLM裁判，仅通过交互轨迹、工具返回值、环境状态即可自动判案，可复现性100%
### 关键实验
测试5个主流大模型+官方/通用2种Harness共10组配置，核心结果：静态决策任务模型准确率普遍超90%，但交互式多步任务最高准确率仅67.2%；静态准确率95%的模型在交互式单动作任务中准确率仅52%；证据完备前提下单动作执行准确率可达93%以上，70%以上故障来自证据收集不全就提前执行、调查不充分就终止的环节。
### 核心结论
工具Agent的正确性不仅要看最终结果，更要看动作执行前的证据链是否合规，静态工具调用准确率无法代表交互式场景下的真实可靠性。
