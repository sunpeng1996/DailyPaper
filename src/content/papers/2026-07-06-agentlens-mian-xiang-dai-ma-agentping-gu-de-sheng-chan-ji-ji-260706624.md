---
title: 'AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation'
title_zh: AgentLens：面向代码Agent评估的生产级轨迹评审基准
authors:
- Andrey Podivilov
- Vadim Lomshakov
- Sergey Savin
- Matvei Startsev
- Roman Pozharskiy
- Maksim Parshin
- Sergey Nikolenko
affiliations:
- Explyt
- St. Petersburg Department of the Steklov Institute of Mathematics
- St. Petersburg State University
arxiv_id: '2607.06624'
url: https://arxiv.org/abs/2607.06624
pdf_url: https://arxiv.org/pdf/2607.06624
published: '2026-07-06'
collected: '2026-07-10'
category: Eval
direction: Agent 全交互轨迹评估基准设计
tags:
- Agent Evaluation
- Trajectory Review
- Production Benchmark
- LLM Assisted Evaluation
- Coding Agent
one_liner: 提出面向代码Agent的全交互轨迹评估开源基准，结合形式校验与LLM评审支持问题诊断与版本迭代
practical_value: '- 业务Agent（如电商导购、客服、选品Agent）评估可复用全轨迹评估思路，不局限于最终任务成败，新增指令遵循度、工具调用合理性、错误恢复能力、交互友好度等维度，更贴近真实用户体验

  - 评估流程可复用「形式化规则校验+LLM自动轨迹评审+多版本横向对比」的组合方案，兼顾指标客观性与结果可解释性，大幅降低人工评审成本

  - 可参考其nightly流水线回归校验机制，自动捕捉Agent版本迭代中的体验劣化问题，适配生产环境Agent的快速持续迭代'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有代码Agent评估基准仅采用最终任务成败的二元指标，既无法覆盖用户真实感知的全交互体验（如工具调用合理性、错误恢复能力、交互友好度等），也无法适配无明确二元结果的任务场景，且评估结果无解释性，难以支撑生产环境Agent的迭代优化与问题定位。

### 方法关键点
AgentLens全轨迹评估基准核心方案为：1）存在客观校验规则的环节采用形式化验证保证准确性；2）其余评估环节通过LLM自动生成轨迹评审报告，输出可解释的打分依据；3）支持多版本/多模型的横向对比。

### 关键结果
基准已开源，可直接接入生产环境nightly评估流水线，支持Agent行为诊断、版本效果对比、产品回归问题自动捕捉，大幅降低生产级Agent的评估成本。
