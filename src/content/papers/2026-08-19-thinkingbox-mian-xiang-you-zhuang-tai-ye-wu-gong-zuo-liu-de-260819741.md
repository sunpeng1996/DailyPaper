---
title: 'One Success Isn''t Reliability: Thinkingbox, a Sandbox and Benchmark for Agents
  in Stateful Business Workflows'
title_zh: ThinkingBox：面向有状态业务工作流的Agent沙箱与基准测试集
authors:
- Zhuochun Li
- Youngmin Ko
- Ali Keramati
- Nicola Ferri
- Susana Palmaz Lopez Pelaez
- Liang-Chun Tsai
- Calvin Wang
- Mirco Milletari
- Tuhin Kundu
- Vadim Smolyakov
affiliations:
- University of Pittsburgh
- Northwestern University
- University of California, Irvine
- Microsoft
arxiv_id: '2608.19741'
url: https://arxiv.org/abs/2608.19741
pdf_url: https://arxiv.org/pdf/2608.19741
published: '2026-08-19'
collected: '2026-08-25'
category: Agent
direction: Agent 有状态业务工作流评测与沙箱
tags:
- Agent_Evaluation
- MCP
- Stateful_Workflow
- Tool_Use
- Benchmark
one_liner: 提出MCP兼容的有状态业务Agent沙箱与507任务基准，揭示单次成功与可靠执行的差距
practical_value: '- 电商客服/售后Agent开发可复用ThinkingBox的side effect评估逻辑，不止校验工具调用合法性，还要校验最终后端状态变更、无冗余副作用，避免「看起来成功实际业务错误」的问题

  - 业务Agent性能评测不要只看pass@1，需增加多次重复实验的pass^k（全成功比例），更真实反映上线后的可靠性，避免偶发成功的误导

  - 多轮有状态Agent的故障分类可直接复用论文的4类划分（工具使用错误、无状态变更动作、用户回复不全、状态更新错误），快速定位业务Agent优化点

  - 涉及退款、改单等高风险电商业务流程的Agent，可参考论文的任务校验设计，把业务规则拆解为可执行的状态校验规则，实现自动化回归测试'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent基准多聚焦代码修复、工具调用语法正确性、单步任务完成度，无法覆盖有状态业务场景（如电商退款、预订修改、保单更新）的真实要求：这类任务需要多轮交互补全信息、遵守领域规则、保证后端状态变更正确无冗余副作用，偶发的单次成功无法代表上线后的可靠运行能力，行业缺乏专用的测试沙箱与基准数据集。
### 方法关键点
- 自研MCP兼容的ThinkingBox沙箱：实现模拟用户、LLM Agent、隔离后端工具的多轮交互编排，自动抽取轨迹与状态变更副作用，基于最终状态而非执行路径做可执行校验，允许合法的异轨完成
- 构建ThinkingBox-Bench基准：覆盖零售/电商、酒店预订、车险、数字银行IT支持、咨询IT/HR 5个领域共507个真实业务工作流任务，每个任务绑定初始状态、业务政策、模拟用户逻辑、专属状态校验规则
- 采用多维度评测指标：pass@1（单次尝试通过率）、pass@k（k次尝试至少1次成功）、pass^k（k次尝试全部成功），区分「可发现成功路径」和「稳定可靠执行」的能力差异
### 关键实验
测试12款闭源/开源LLM，每任务执行20次独立重复实验：最强模型GPT-5.4 pass@1仅65.36%，pass@20达91.12%，但pass^20仅25.25%；工具使用错误（含调用失败后无法修复）是首要故障类型，占所有失败案例的77.5%；开源模型中DeepSeek-V4-Pro表现最优，平均pass@1达43.26%。
> 最值得记住的结论：业务场景下Agent的单次成功不等于可靠，仅校验工具调用合法性或回复合理性不足以保证业务正确性，必须校验最终后端状态与副作用。
