---
title: 'EvoX: Rethinking the Agent Harness as a Runtime Policy'
title_zh: EvoX：将Agent执行框架抽象为运行时策略的多模型运行时系统
authors:
- Haoyang Zhang
- Qumeng Sun
- Xiao Zhang
- Xiang Liu
- Zhidong Fan
- Junjie Wang
affiliations:
- Infinite Evolution Lab, EvoMap
arxiv_id: '2611.15006'
url: https://arxiv.org/abs/2611.15006
pdf_url: https://arxiv.org/pdf/2611.15006
published: '2026-11-11'
collected: '2026-11-13'
category: Agent
direction: Agent运行时设计 · 多模型适配与公平评测
tags:
- Agent Runtime
- LLM Agent
- Evaluation Framework
- Operational Policy
- Multi-Model
one_liner: 提出语义-操作双策略Agent运行时架构，配套可控评测框架，跨模型平均成功率提升3个百分点
practical_value: '- 可复用双策略拆分思路：将业务Agent拆为LLM负责的Semantic Policy层（意图理解、个性化策略生成）和运行时负责的Operational
  Policy层（工具调用校验、异常重试、结果对齐），无需修改模型即可降低LLM输出不稳定带来的业务错误，适配电商导购、客诉Agent等场景

  - Action Realization机制可直接落地到工具调用链路：对LLM输出的tool-call做格式校验、参数归一化、意图匹配，可降低20%+的工具调用失败率，比如电商Agent调用订单查询、优惠券发放接口的场景

  - Contrast评测框架的公平性设计可迁移到业务效果评测：区分锁定条件（模型版本、调用参数）、共享条件（测试用例、环境）、原生条件（不同Agent的prompt、流程），解决不同版本Agent、不同厂商LLM的效果对比公平性问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent的语义决策往往合理，但常因tool-call格式错误、流程中断、结果虚报等问题导致执行失败，现有Agent harness的设计对最终效果影响极大，但缺乏统一的设计范式和公平的跨框架评测方法，优化方向不明确。

### 方法关键点
- 提出「第二策略」设计原则：将Agent系统拆分为Foundation Model负责的**Semantic Policy**（意图理解、决策规划、反馈推理），和harness负责的**Operational Policy**（执行控制、状态管理、异常恢复），无需修改模型参数即可提升执行成功率
- 三个核心机制实现Operational Policy：Action Realization做工具调用检测、schema校验、参数归一化，解决格式不匹配问题；Execution Continuity做失败重试引导、重复错误检测、熔断、上下文压缩，避免无效循环和提前终止；Outcome Grounding引导LLM基于实际执行结果输出结论，避免虚报完成
- 推出Contrast评测框架：明确划分锁定/共享/原生三类评测条件，配套前置任务校验、provider-bound调用参数审计、证据导向的结果判定，实现不同harness的公平对比，排除外部因素干扰

### 关键结果
覆盖5个基准测试集、6个主流LLM、6个主流Agent harness，在691个共有的任务-模型对下评测：EvoX成功率达56.2%，比其他5个harness的平均水平高3.0个百分点，在GLM-5.3、Kimi K3上分别领先10.7、7.9个百分点，跨厂商模型适配优势明显。

### 核心结论
Agent系统的效果上限由LLM的语义能力决定，但下限由运行时框架的操作控制能力决定，无需调整模型参数，仅优化运行时逻辑即可实现显著效果提升。
