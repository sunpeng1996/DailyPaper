---
title: 'When Users Change Their Minds: Measuring and Repairing Intent Drift in LLM
  Agents'
title_zh: LLM Agent多轮交互中的意图漂移度量与修复框架
authors:
- Yanjie Zhang
- Bowen Cao
- Zixin Chen
- Yushi Sun
affiliations:
- HKUST
- CUHK
- LIGHTSPEED (Shenzhen)
arxiv_id: '2609.32520'
url: https://arxiv.org/abs/2609.32520
pdf_url: https://arxiv.org/pdf/2609.32520
published: '2026-09-25'
collected: '2026-10-02'
category: Agent
direction: Agent多轮交互意图漂移优化
tags:
- LLM Agent
- Intent Drift
- Multi-turn Interaction
- State Tracking
- Benchmark
one_liner: 提出意图漂移评测基准INTENTFLUX与显式状态维护方法STATEFORGE缓解多轮意图漂移问题
practical_value: '- 电商导购/客服Agent可新增轻量意图状态跟踪模块，每次用户交互后同步更新活跃需求、删除已撤回的约束/参数，无需修改底座模型即可降低意图漂移带来的错误，9B
  tracker效果与122B无显著差异，部署成本低

  - Agent历史管理不要仅依赖滚动摘要、上下文压缩方案，这类方法无法区分信息有效性，需额外过滤基于过时意图推导的中间结论，避免残留错误影响生成结果

  - 多轮对话系统评测需加入用户中途变更需求的测试case，仅测试无变更多轮会高估上线后实际效果，8款主流大模型在意图漂移场景下全正确率较单轮平均下降30%以上

  - 2B小参数tracker经过on-policy distillation可将得分从0.266提升至0.445，适合算力有限的业务场景快速落地轻量化状态维护能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent在多轮交互中经常遇到用户中途修改参数、撤回约束的场景，现有系统普遍存在意图漂移问题：已被取代的旧意图仍会影响最终输出，导致任务完成率大幅下降。现有多轮评测无法单独隔离意图漂移带来的误差，也缺乏低成本的有效缓解方案。

### 方法关键点
- 构建INTENTFLUX评测基准：将可验证的代码、数学、SQL、工具调用等任务转换为带可控意图变更的多轮对话，引入两类可影响最终评分的过时信息：被替换的参数值VARIANT、被撤回的约束DECOY，严格控制评测难度
- 提出STATEFORGE修复框架：解耦意图状态维护与下游任务求解，每次用户输入后由跟踪器更新活跃意图状态，删除过时意图及基于其推导的中间结论，生成前将活跃状态插入prompt；支持两种落地路径：模块化轻量跟踪器，或通过蒸馏将状态维护能力内化进底座Agent

### 关键结果
在125条的GENERAL-TEST测试集上：裸多轮执行平均得分0.367，STATEFORGE提升至0.467，输入ground truth最终状态可进一步提升到0.549，但仍低于单轮场景的0.778，说明状态估计误差仅为性能缺口的部分原因；9B跟踪器效果与122B无统计差异，2B跟踪器经过OPD蒸馏得分从0.266提升至0.445；8款主流LLM在意图漂移场景下的全正确率较单轮平均下降30%以上，轮长匹配的无变更对照实验证明性能下降并非由对话长度增加导致。

### 核心结论
多轮Agent的历史管理不能仅做信息压缩，必须显式区分有效意图与过时意图，才能有效缓解意图漂移问题。
