---
title: 'EDGEGEN: Improving Tool-Calling Agents Beyond Happy Paths with Synthetic Edge
  Case Generation'
title_zh: EDGEGEN：生成合成边界用例提升工具调用Agent鲁棒性
authors:
- Harshavardhan Abichandani
- Penny Chong
- Jiyuan Shen
- Gunraj Singh
- Ashutosh Hathidara
- Marcus Duigan Xing Yu
- Jane Lo
- Atin Ghosh
- Yipeng Li
- Daniel Dahlmeier
affiliations:
- SAP
arxiv_id: '2609.24115'
url: https://arxiv.org/abs/2609.24115
pdf_url: https://arxiv.org/pdf/2609.24115
published: '2026-09-20'
collected: '2026-09-23'
category: Agent
direction: Agent 工具调用鲁棒性优化
tags:
- Tool-Calling-Agent
- Synthetic-Data-Generation
- Edge-Case
- Agent-Robustness
- Policy-Compliance
one_liner: 提出合规规则驱动的无标注合成边界用例生成框架，提升工具调用Agent鲁棒性
practical_value: '- 电商客服、订单处理类业务Agent可直接复用该框架，从业务规则文档提取合规约束，自动生成边界测试用例，覆盖退款拒单、异常权限申请等场景，无需人工标注即可完成Agent鲁棒性评估

  - 可复用「规则枚举+数据库状态绑定+双校验」流水线，为Agent的SFT、Prompt优化生成高质量训练数据，避免仅用happy path数据导致的过拟合问题

  - 针对无法微调的黑盒大模型，可使用框架生成的边界用例做Agent Harness优化，实测可带来10%-30%的业务流程完成率提升，同时降低工具调用次数与token消耗'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
工具调用LLM Agent在电商客服、企业流程处理等场景大规模落地，但现有训练与评估数据多为常规happy path场景，无法覆盖业务合规边界；真实生产数据受隐私限制难以获取，人工标注成本高、覆盖不全，导致Agent在真实异常请求下故障率高，常规合成数据方法不绑定数据库状态、不针对业务规则生成，质量差易出现幻觉。

### 方法关键点
- 从Agent的业务规则文档自动提取可校验的原子合规约束，枚举约束组合生成边界违规场景，过滤逻辑冲突的无效组合
- 构建工具调用依赖图，采样单工具、多步线性、分支等不同复杂度的工作流，结合场景需求用SQL Agent查询数据库，绑定真实可执行的数据库状态
- 双校验机制验证用例合法性：首先校验用例中实体、参数与数据库状态匹配，其次校验场景的合规响应（如拒单）是否可通过现有工具实现，仅保留合法用例
- 形成闭环优化流水线：生成的用例可直接用于Agent的SFT或Harness（系统Prompt/工具描述）优化，全程无需人工标注与生产数据

### 关键结果
在τ2-bench航空、零售领域，ToolSandbox三个基准测试，对比基础模型、人工标注数据集、Naive合成、TaskBench、FuncBenchGen等基线：
- SFT场景下，对Qwen 2.5-3b小模型平均流程完成率提升最高达42%，所有18组模型-基准组合均超过基线，而人工标注等基线在多规则场景下最高出现13%的性能下降
- Harness优化场景下，Gemma-4-e4b模型平均流程完成率较基础Harness提升30%，较人工标注数据优化的Harness提升10%，同时工具调用次数、token消耗均低于人工标注优化方案

**最值得记住的一句话**：仅用happy path数据训练/优化Agent不仅收益有限，还可能出现负向效果，针对业务合规规则生成的边界用例是提升Agent落地鲁棒性的核心抓手
