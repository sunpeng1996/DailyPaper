---
title: 'Interlock: From Local Correctness to Task Completion in Long-Horizon Agents'
title_zh: Interlock：长程Agent从局部正确性到任务完成度的任务合成框架
authors:
- Linji Hao
- Yanji He
- Zihan Wang
- Hansi Yang
- Jiayuan Zhang
- Hongyan Hao
- Qi Gu
- Yan Feng
- Han Wu
affiliations:
- 北京大学
- 香港科技大学（广州）
- 清华大学
- 美团
arxiv_id: '2610.19686'
url: https://arxiv.org/abs/2610.19686
pdf_url: https://arxiv.org/pdf/2610.19686
published: '2026-10-13'
collected: '2026-10-20'
category: Agent
direction: 长程Agent · 任务合成与训练优化
tags:
- Long-Horizon Agent
- Task Synthesis
- Completion Graph
- RFT
- Agent-as-Judge
one_liner: 提出基于类型化完成图的长程Agent任务合成与训练方案，解决局部正确但整体任务未闭环的问题
practical_value: '- 电商长程Agent（如全链路售后处理、供应链规划、履约调度）可直接复用类型化完成图设计，建模证据、决策、下游约束的关联，避免局部操作正确但整体任务未闭环的问题，例如改地址后未同步物流、发票的场景

  - 合成Agent训练数据时可复用双审查机制：源覆盖审查保证原始需求不丢失，公共输入审查保证评测规则可基于公开材料落地，大幅提升合成数据的有效性

  - Agent轨迹筛选阶段用支持脚本执行的Agent-as-Judge替代纯文本LLM-as-Judge，筛选出的SFT数据训练后效果提升更显著，可直接用于调优电商客服、工单处理等垂直场景Agent'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长程Agent在多约束、长流程的复杂场景中，常出现单步操作符合规则但整体任务未完成的问题，例如预订机票后未同步更新行程、预算，核心原因是未显式建模环境证据、决策、下游效果三者之间的关联约束，现有训练数据也缺乏对完整任务完成度的监督，导致迁移到真实场景时完成率低。

### 方法关键点
- 提出**类型化完成图**作为任务的核心表示，包含三类关系：grounding边连接公开证据到决策，coupling超边跨组件施加联合约束，realization边连接决策到所有必要的下游效果
- 基于完成图生成可重置工作区、公开任务请求、私有评测规则，通过「源覆盖审查+公共输入审查」双校验保证任务需求无遗漏、评测标准可落地
- 采用**完成过滤的RFT（拒绝采样微调）**：用支持脚本执行的Agent-as-Judge筛选满足所有约束的轨迹作为SFT训练数据，仅用模型自身生成的合格轨迹做训练

### 关键实验
基于Qwen3.6-27B和Qwen3.6-35B-A3B两个基座，对比原生基座、ClawGym-SFT基线：
- AutomationBench任务通过率提升4.00~4.50个百分点，JobBench加权得分提升3.20~6.64分，Harvey LAB准则通过率提升3.89~4.16个百分点
- 固定轨迹数量时，训练域覆盖越广，模型迁移效果越好；Agent-as-Judge比纯文本LLM-as-Judge筛选的训练数据带来的效果提升更显著

> 最值得记住的一句话：长程Agent的核心能力不是单步操作正确，而是建立证据、决策、下游效果的全局关联，保证所有约束被满足的任务闭环能力。
