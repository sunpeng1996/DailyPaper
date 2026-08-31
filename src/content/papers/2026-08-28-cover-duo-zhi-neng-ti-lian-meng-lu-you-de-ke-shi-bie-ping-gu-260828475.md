---
title: 'COVER: Identifiable Evaluation of Coalition Routing'
title_zh: COVER：多智能体联盟路由的可识别评估框架
authors:
- Raghul Sugumar
- Amrit Gopinath
affiliations:
- Sri Sivasubramaniya Nadar College of Engineering
arxiv_id: '2608.28475'
url: https://arxiv.org/abs/2608.28475
pdf_url: https://arxiv.org/pdf/2608.28475
published: '2026-08-28'
collected: '2026-08-31'
category: Agent
direction: Agent 多智能体路由效果评估
tags:
- MultiAgent
- Routing
- Evaluation
- CausalIdentification
- PolicyComparison
one_liner: 提出固定下游栈与信息边界的多智能体联盟路由可识别评估协议，消除端到端对比的混淆
practical_value: '- 做多智能体路由（如电商多客服Agent、多召回源路由、多工具选择）效果评估时，固定下游全链路栈（生成器、排序逻辑、判分规则）再做对比，避免把下游模块优化误判为路由效果提升

  - 对比多个路由策略时，无需穷举所有可能的Agent组合，仅执行所有策略选中团队的去重集合，即可无假设得到所有两两策略的对比结果，大幅降低评估算力成本

  - 拆分路由效果归因指标：先统计路由选中的团队是否覆盖了所需的全部信息（证据传输完成率），再看端到端业务指标，避免下游生成/推理模块的误差掩盖路由本身的优化效果'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
多智能体系统切换路由策略时，会同时改变团队选择、内部消息传递和下游输出，仅靠端到端精度差无法识别效果变化是否来自路由本身，传统评估存在严重混淆，也无法准确量化路由的真实优化空间。

### 方法关键点
- 定义COVER评估契约，提前固定5个核心要素：合法团队集合、路由器可见的公开信息边界、下游全链路协议（含Agent能力、通信规则、最终生成器、判分规则）、执行覆盖范围、推理规则，所有路由策略在完全相同的环境下对比。
- 最小支撑定理：对比多个冻结路由策略时，仅需执行所有策略选中团队的去重集合，即可无额外假设得到所有两两策略的对比结果；仅当需要计算相对最优团队的绝对Oracle regret时，才需要穷举所有合法团队组合。
- 拆分两类评估指标：证据传输完成率（仅衡量路由选队是否覆盖了任务所需的全部信息，不受下游生成逻辑影响）、最终端到端指标，实现路由效果的单独归因。

### 关键结果
- MuSiQue-12多跳QA数据集：特权控制策略将regret从0.532降至0.402，公开接口策略regret 0.424 vs 基线0.554。
- HotpotQA-4数据集：直接集打分器将regret从0.313降至0.110。
- 固定Llama执行栈：路由的证据传输regret相对提升0.190，但端到端原始答案增益仅0.010且置信区间跨零，证明下游生成模块会完全掩盖路由的真实优化效果。
- ToolSandbox真实工具环境：声明团队集合的Oracle完成率达0.768，而预冻结路由策略仅为0.637（regret 0.131），未达预设0.10的合格阈值，准确暴露了路由的优化空间而非虚造提升。

> 最值得记住的一句话：多智能体路由的效果评估必须隔离下游变量，否则所有端到端的提升都无法证明是路由本身的贡献。
