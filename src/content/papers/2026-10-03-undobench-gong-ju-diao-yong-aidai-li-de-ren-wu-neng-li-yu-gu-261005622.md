---
title: 'UndoBench: Separating Task Competence from Recovery Capability in Tool-Using
  AI Agents'
title_zh: UndoBench：工具调用AI代理的任务能力与故障恢复拆分评测基准
authors:
- Dolly Sah
- Tanmay Sah
- Harshul Jain
- Tanya Sah
affiliations:
- Independent Researcher
arxiv_id: '2610.05622'
url: https://arxiv.org/abs/2610.05622
pdf_url: https://arxiv.org/pdf/2610.05622
published: '2026-10-03'
collected: '2026-10-06'
category: Agent
direction: 工具型Agent 故障恢复能力评测
tags:
- Agent
- Benchmark
- Fault Tolerance
- Tool Calling
- LLM
one_liner: 提出首个拆分任务能力与故障恢复能力的工具型Agent评测基准，量化不同故障阶段的恢复表现差异
practical_value: '- 电商/广告场景的Agent工具调用（如优惠券发放、订单改价、广告扣费接口）必须优先加服务端idempotency key校验，实验验证全链路支持后CRSR从33%提升至97%，可完全消除重复操作风险

  - Agent故障恢复策略要按故障阶段设计：PRE_MUTATION阶段直接重试无风险，POST_MUTATION_PRE_ACK阶段必须先校验远程状态再重试，禁止统一使用naive
  retry，否则会产生50%+的重复操作（如重复发券、重复扣费）

  - 现有Agent效果评估不能仅看标称成功率，要增加故障注入下的CRSR指标，标称83%的成功率下CRSR可能不到47%，会严重漏判生产环境的可靠性

  - 自研Agent框架可直接复用UndoBench的配对反事实评测范式，相同种子下跑无故障/有故障对照，精准定位恢复能力短板，不会混淆任务本身的规划能力问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent评测基准仅评估无故障标称场景的任务完成率，混淆了基础规划能力与分布式环境下的故障恢复能力；生产环境中网络丢包、服务超时、中间件错误等故障频发，通用naive retry策略会导致重复扣费、重复发券、重复创建订单等严重业务风险，行业缺乏可量化恢复能力的标准化评测体系。

### 方法关键点
- 采用配对反事实评测范式：相同随机种子下分别执行无故障控制组与故障注入组试验，定义**CRSR（条件恢复成功率）**指标，仅统计标称任务成功样本的恢复表现，完全排除规划能力的干扰
- 覆盖8个企业域共36个基础工作流+36种故障场景，按故障发生阶段划分为PRE_MUTATION（调用前传输失败）、DURING_MUTATION（调用中部分状态修改）、POST_MUTATION_PRE_ACK（调用成功但返回丢失）三类核心故障
- 配套双验证Oracle：状态Oracle校验最终业务逻辑正确性，链路Oracle统计重复/缺失操作率，量化操作安全风险

### 关键实验结果
- 主实验共执行2880组配对试验，覆盖2个开源LLM、2个Agent框架、3种恢复策略：标称任务成功率达83.54%，但CRSR仅为46.72%，naive retry策略会导致53.33%的试验出现重复副作用
- 全链路服务端支持idempotency key后，CRSR提升至97.24%，重复副作用率降为0
- 商用大模型（Gemini 3.8 Flash、GLM-5.2）存在相同的能力-恢复差距：标称成功率约80%，naive retry下CRSR仅21%，重复副作用率达50%+

> 最值得记住的结论：Agent标称任务完成率会严重高估生产环境可靠性，故障恢复是与任务规划完全独立的能力维度，必须按故障发生阶段设计对应恢复策略
