---
title: Invariant-Aware Harness Enforcement to Protect LLM Agents from Silent API Failures
title_zh: 基于不变量感知执行器的LLM Agent静默API失败防护方案
authors:
- Sajib Acharjee Dip
- Brian Ouyang
- Lala Motlhabi
affiliations:
- Virginia Tech
- Genentech
arxiv_id: '2611.20595'
url: https://arxiv.org/abs/2611.20595
pdf_url: https://arxiv.org/pdf/2611.20595
published: '2026-11-15'
collected: '2026-11-18'
category: Agent
direction: Agent鲁棒性 · 静默API故障防护
tags:
- LLM Agent
- Silent API Failure
- Guardrail
- Robustness
- Invariant Check
one_liner: 通过执行层不变量校验将LLM Agent受静默API故障影响的错误率从74%降至1.7%
practical_value: '- 搭建工具调用型Agent（如电商导购Agent、广告投放Agent）时，不要将工具结果校验的决策权交给LLM，在执行层做确定性校验的鲁棒性远高于LLM自检方案，且跨模型一致性更好

  - 对计数、列表类API结果可直接复用现成校验规则：计数类校验拆分条件后的数量恒等性，列表类校验每条记录符合过滤条件、无重复、总数匹配，入参类校验参数是否符合API文档规范

  - 对错误容忍度极低的业务场景，校验不通过时优先采用直接拒答（返回无法确定）的策略，不要让LLM自行判断是否采信可疑结果，可将错误率压到极低水平'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent的答案准确性完全依赖API返回结果，静默API失败（返回HTTP 200但结果错误，比如忽略过滤条件、截断分页）在11/15的公开API中普遍存在，现有依赖LLM自检、评审模型、LLM Judge的方案仅能拦截不到30%的错误，核心原因是LLM即使发现结果可疑，仍倾向于输出确定性答案而非拒答。

### 方法关键点
- 两类不变量校验规则：精确校验（计数恒等性、列表过滤合规性、参数与API文档匹配，无假阳性）、学习校验（从干净响应挖掘的字段类型、范围、线性关系等契约，存在少量假阳性）
- 执行层校验流程：API返回结果先过校验，失败则重试一次，再次失败时精确校验直接拦截错误结果，仅给Agent返回校验通过的值或「无法确定」提示，学习校验仅给结果附加警告
- 完全在工具调用执行层实现，无需额外LLM调用，不会增加推理成本

### 关键结果
基于自建AgentOrchBench、9个真实公开API、ToolMaze三类数据集，对比无防护、checklist提示、评审模型、Outcome Monitors等基线：7个开源模型上，静默故障下的错误答案占比从74.0%降至1.7%，无故障场景准确率无损失；3个前沿模型上错误占比从70.2%降至0.5%；真实API错误参数场景下错误占比从89.8%降至21.3%。

**最值得记住的一句话**：LLM默认倾向于输出确定性答案而非拒答，工具结果校验的决策权必须从模型移到执行层，只有确定性执行拦截才能保证跨模型的鲁棒性。
