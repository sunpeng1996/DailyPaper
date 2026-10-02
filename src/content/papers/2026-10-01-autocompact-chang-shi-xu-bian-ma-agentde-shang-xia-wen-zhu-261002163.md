---
title: 'AutoCompact: Learning When to Compact Context in Long-Horizon Coding Agents'
title_zh: AutoCompact：长时序编码Agent的上下文主动压缩时机学习方法
authors:
- Xuan Zhang
- Longtao Zheng
- Cunxiao Du
- Bo An
- Xin Dong
affiliations:
- Singapore Management University
- Nanyang Technological University
- Harvard University
arxiv_id: '2610.02163'
url: https://arxiv.org/abs/2610.02163
pdf_url: https://arxiv.org/pdf/2610.02163
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: 长时序Agent · 主动上下文压缩
tags:
- Long-Horizon Agent
- Context Compression
- SFT
- Reinforcement Learning
- GRPO
one_liner: 通过judge校正轨迹与RL联合训练，让长时序Agent自主决策上下文压缩的时机、内容与后续执行
practical_value: '- 给长会话推荐/导购Agent新增`compact()`主动工具，无需等待KV cache溢出才压缩，可在用户会话阶段切换（如浏览转加购、搜索转下单）时主动压缩历史，丢弃过时浏览/点击行为，保留核心兴趣与待执行动作，降低推理成本同时减少冗余信息干扰。

  - 训练主动压缩策略可复用「在线judge校正+RL联合优化」范式：先用人或强模型标注压缩时机、保留内容、后续动作的校正轨迹做SFT，再用最终业务目标（如下单转化率、搜索满意度）作为RL奖励，无需设计额外压缩相关辅助奖励。

  - 低推理预算场景收益显著：在流量高峰降本需求下，开启主动压缩可比全量上下文推理提升低算力预算下的任务成功率，尤其适合搜索推荐的实时高并发推理链路。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长时序LLM Agent执行多步任务时会积累大量过时探索信息、失败尝试、冗余工具输出，传统固定长度触发的压缩要么在任务中途强制压缩丢失关键信息，要么保留全量上下文导致推理冗余、成本升高；现有主动压缩方法未解决压缩后动作一致性问题，容易出现压缩后重复执行已完成步骤的情况。

### 方法关键点
- 给Agent新增`compact()`主动工具，可在任务阶段切换时自主调用，将历史上下文替换为仅保留核心结论、当前状态、后续动作的工作摘要，丢弃过时探索信息。
- 训练分为两阶段：第一阶段用强模型作为在线judge，校正Agent三类行为：压缩时机是否合理、摘要是否保留关键信息、压缩后动作是否符合摘要规划，用校正后的1052条轨迹做SFT初始化模型；第二阶段用GRPO做RL训练，仅以最终任务成功为二进制奖励，联合优化任务执行能力和压缩策略，无需设计压缩相关的奖励函数。

### 关键实验
在SWE-bench Verified和SWE-PolyBench Verified两个编码Agent基准上，对比无压缩基线、固定长度压缩、其他主动压缩方法，AutoCompact相对基线分别提升9.2%和5.0%的任务通过率；在$0.1低推理预算下相对基线提升最高达55%，即使在16K小上下文窗口带强制压缩fallback的场景下也在全预算范围领先。

### 核心结论
即使上下文窗口足够容纳全量历史，主动丢弃过时信息、保留紧凑工作状态也能提升Agent的任务成功率和推理效率，而非一味追求保留完整交互历史。
