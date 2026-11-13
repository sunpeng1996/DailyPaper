---
title: 'Termination Lag: Coding Agents Solve Early but Stop Late'
title_zh: 终止滞后：编码Agent提前解决任务却延迟停止
authors:
- Musa Cim
- Burak Topcu
- Mahmut Taylan Kandemir
affiliations:
- The Pennsylvania State University
arxiv_id: '2611.14960'
url: https://arxiv.org/abs/2611.14960
pdf_url: https://arxiv.org/pdf/2611.14960
published: '2026-11-11'
collected: '2026-11-13'
category: Agent
direction: Agent 运行效率优化 · 终止策略
tags:
- CodingAgent
- TerminationLag
- EfficiencyOptimization
- SWE-bench
- LLMAgent
one_liner: 量化编码Agent的终止滞后现象，验证早停可节省35%-60%开销还能避免正确结果被破坏
practical_value: '- 所有多步执行的业务Agent（电商选品Agent、营销文案生成Agent、用户问题解决Agent）都可引入TTFCP+终止滞后的度量体系，量化全链路无用开销，评估早停策略的业务收益

  - 任务执行类Agent的首次正确输出占比达38%~82%，可在首次输出后触发轻量自定义校验规则，符合要求则直接结束流程，大幅降低token消耗与响应延迟

  - 业务Agent需限制正确结果生成后的编辑操作，避免1%~8%的概率将正确结果改错，降低最终输出的错误率

  - 可复用论文的每步快照+离线评估方法，复盘业务Agent的历史运行轨迹，定位冗余步骤优化prompt设计与工具调用逻辑'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有编码Agent评估仅以最终补丁正确性为核心指标，完全掩盖了正确结果生成后到终止之间的冗余计算开销，既大幅提升token成本与推理延迟，还存在将正确补丁改错的风险，而终止决策能力本身是Agent性能的核心组成部分，此前缺乏跨模型、跨框架的系统性量化分析。
### 方法关键点
- 定义3个核心度量：TTFCP（首次生成正确补丁的步数）、TL（终止滞后步数）、NTL（归一化终止滞后占总步数的比例）
- 每步Agent执行后自动快照当前代码补丁，离线用官方基准测试评估正确性，全程不干扰Agent运行逻辑
- 测试覆盖5款LLM、2套Agent框架（OpenHands/mini-SWE-agent）、3个SWE-bench系列数据集
### 关键结果
- 38%~82%的成功运行中，首次代码编辑就生成了符合要求的正确补丁
- 成功运行的NTL中位数达35%~60%，其中48%~63%的冗余步骤用于校验、15%~29%用于代码探索，仅2%~19%为代码编辑
- 1%~8%的成功运行中，后续操作会破坏已有的正确补丁，导致最终输出错误

> 最值得记住的结论：Agent的问题解决能力远超过其判断任务完成的能力，优化终止策略带来的效率收益甚至超过模型本身迭代的收益
