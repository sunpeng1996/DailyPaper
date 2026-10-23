---
title: 'VerifierBench: Benchmarking the Generation of Executable Verifiers for LLM
  Agents'
title_zh: VerifierBench：面向LLM Agent可执行验证器生成的基准测试
authors:
- Jianing Yin
- Ziyi Chen
- Hao Wang
- Yiyou Sun
- Zijian Jin
- Dawn Song
- Daoan Zhang
affiliations:
- University of Pennsylvania
- University of Illinois at Urbana-Champaign
- University of California, Berkeley
- New York University
- University of Rochester
arxiv_id: '2610.28679'
url: https://arxiv.org/abs/2610.28679
pdf_url: https://arxiv.org/pdf/2610.28679
published: '2026-10-18'
collected: '2026-10-23'
category: Agent
direction: Agent 可执行验证器生成基准评测
tags:
- LLM-Agent
- Verifier-Generation
- Benchmark
- Agent-Evaluation
- Executable-Verifier
one_liner: 构建含222个任务的Agent验证器生成基准，配套6项审计流程，系统评测19款大模型的验证器生成性能
practical_value: '- 可直接复用V4V的6项审计流程，校验电商/广告Agent生成的工具调用规则、内容审核逻辑、活动规则校验器的正确性，减少合法请求被误拦截、违规请求被放行的问题

  - 构建业务Agent的自校验模块时，可参考本文的测试用例分层设计：覆盖黄金解、合法变体、普通错误、对抗攻击四类用例，避免验证规则仅适配单一解法

  - 做Agent自测试时要预留专门的执行预算，区分任务执行和校验逻辑测试的资源配额，避免因预算耗尽导致校验逻辑未经验证就上线

  - 发现验证器的非法解拒绝率很高时，优先排查是否存在全拒型验证器，这类验证器看似准确率高实则完全不可用，需重点治理'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent在递归自迭代训练数据筛选、任务执行结果校验、RL奖励信号生成等场景都需要可靠的可执行验证器，错误的验证器会反复丢弃合法解、放行违规解，直接影响Agent迭代效果。现有评测仅覆盖代码单元测试、断言生成等场景，未覆盖Agent工具调用、环境状态校验等核心场景，也缺乏对验证器是否接受全量合法解、拒绝所有非法解的系统性校验。

### 方法关键点
- 构建VerifierBench基准：从6个开源Agent基准中筛选出222个合格任务，覆盖工具调用、状态校验、代码校验三类场景，共4993个隐藏测试用例，分为黄金解、合法变体、普通错误、攻击用例四类
- 提出V4V 6项审计流程（重放、可重复性、来源校验、输入标签一致性、trivial基线校验、变异测试），过滤45个有缺陷的原始任务，确保基准标签100%可靠
- 采用归一化平衡准确率BAnorm作为核心指标，同等权重衡量合法解通过率（TPR）和非法解拒绝率（TNR）

### 关键结果
- 测试19款主流大模型+17种模型+Agent框架组合，BAnorm得分范围为10.6~62.1，最优的Claude Opus 4.8+原生Claude Code组合仅得66.2分，远未达完美水平
- 所有模型的TPR（21.1%~70.2%）显著低于TNR（79.2%~96.3%），核心痛点是生成的验证器普遍过度严格，错误拒绝合法解
- 分析显示87.9%~96.0%的错误拒绝来自全拒型验证器，这类验证器的自测试仅覆盖符合自身错误假设的用例，或未完成任何合法解的通行校验

### 核心结论
验证器自测试不能仅验证预期解能通过，还要主动测试任务允许的合法变体是否能通行，否则极易生成过度严格的无效验证器
