---
title: 'Resume Means Resume: A Machine-Checked Conformance Contract for Checkpoint,
  Interrupt, and Resume Semantics in Workflow Persistence Layers'
title_zh: 工作流持久化层 checkpoint/中断/恢复语义的机器校验一致性契约
authors:
- Sajjad Khan
affiliations:
- Independent Researcher, London, UK
arxiv_id: '2608.03836'
url: https://arxiv.org/abs/2608.03836
pdf_url: https://arxiv.org/pdf/2608.03836
published: '2026-08-04'
collected: '2026-08-05'
category: Agent
direction: Agent工作流 持久化恢复语义验证
tags:
- AgentWorkflow
- Checkpoint
- CrashRecovery
- FormalVerification
- ExactlyOnceSemantics
one_liner: 定义可机器校验的工作流恢复语义契约，实测5款主流Agent框架均不符合，提供验证后的修复方案
practical_value: '- 电商/广告Agent工作流中涉及非幂等操作（扣库存、发券、广告扣费、发短信）时，不要依赖框架宣称的exactly-once语义，必须自行加幂等校验层；实测LangGraph/CrewAI在crash、跨进程并发恢复场景下均会重复执行已完成的副作用任务，最高重复率100%

  - 可复用论文提出的RESUMECONTRACT 6项核心属性（前缀连续性、exactly-once、分叉确定性、checkpoint有效性、单次消费、恢复确定性），作为自研工作流系统的一致性测试标准，避免版本迭代中的语义漂移

  - 跨进程并发恢复的重复消费问题，可参考REMIT的修复方案：在共享存储读路径加消费认领gate，仅允许第一个认领的进程执行任务，其余直接拒绝，实测可将并发重复执行率从93%+降至0'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
主流LLM Agent工作流框架均已支持checkpoint、中断、恢复能力，但无公开可机器校验的恢复语义契约，不同框架语义互不兼容，甚至实测不符合自身宣称的语义，会导致电商扣库存、广告扣费、发券等非幂等操作重复执行，引发资损。
### 方法关键点
1. 定义RESUMECONTRACT，包含6项核心语义属性：前缀连续性、副作用exactly-once、分叉确定性、checkpoint有效性、单次消费、恢复确定性，外加分叉意图协议、存活性两项义务
2. 基于TLA+对参考语义做全状态空间校验，覆盖7.4×10^6种不同状态，验证属性独立性
3. 开发无LLM的确定性测试框架，对5款主流Agent工作流框架的固定版本做一致性测试，覆盖39种故障场景
4. 实现Verus验证的参考序列器REMIT，修复核心故障，可兼容现有框架的checkpoint接口
### 关键结果数字
1. 实测5款框架（LangGraph 1.2.9、CrewAI 1.15.2等）无两款一致性特征相同，LangGraph在SIGKILL crash场景下exactly-once退化为at-least-once，CrewAI会重复执行已完成的副作用任务
2. 跨进程并发恢复时，单次消费属性失效，40个测试场景中36个重复执行率100%，最低达93.3%，跨主机场景10次测试全量重复执行
3. REMIT修复后，跨进程并发重复执行率降至0，所有核心语义属性符合契约要求
### 最值得记住的一句话
所有宣称的工作流恢复语义都必须经过校验，在非幂等操作前加幂等校验是避免资损的最后一道防线
