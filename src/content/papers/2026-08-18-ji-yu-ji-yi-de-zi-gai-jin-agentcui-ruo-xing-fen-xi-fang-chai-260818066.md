---
title: 'On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification'
title_zh: 基于记忆的自改进Agent脆弱性分析：方差、任务顺序与欠指定问题
authors:
- Qinyuan Ye
- Yu Li
- Yada Pruksachatkun
- Jiaxin Zhang
- Chien-Sheng Wu
affiliations:
- Salesforce AI Research
arxiv_id: '2608.18066'
url: https://arxiv.org/abs/2608.18066
pdf_url: https://arxiv.org/pdf/2608.18066
published: '2026-08-18'
collected: '2026-08-19'
category: Agent
direction: 自改进Agent可靠性评估与优化
tags:
- Self-Improving-Agent
- Agent-Memory
- Agent-Reliability
- Underspecification
- Agent-Evaluation
one_liner: 量化记忆型自改进Agent的三类脆弱性，给出欠指定问题的缓解方向
practical_value: '- 上线记忆型自改进Agent前必须做多轮重复测试+乱序任务压力测试，避免单轮结果高估收益，默认任务顺序的easy-to-hard隐式课程会虚高性能

  - 构建Agent记忆时必须明确写入环境约束（比如电商场景不允许调用未对接的API、不得要求用户额外确认等），避免生成不可执行的无效记忆

  - 记忆生成阶段可补充任务评估规则、环境动作反馈信息，能降低31%的乱序场景性能衰减，适合电商客服、运营自动化等Agent场景

  - 不要盲目上线自改进记忆模块，当前强基线LLM下记忆模块的普遍收益<2%且统计显著性低，还会放大运行方差'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前记忆型自改进Agent的评估普遍仅报告单轮默认任务顺序下的结果，完全忽略系统可靠性风险，而企业级落地场景（如电商客服、运营自动化Agent）对错误容忍度极低，早期随机错误会随自改进过程级联放大，甚至不可逆地损失用户信任，亟需系统性的脆弱性量化分析。
### 方法关键点
- 选取两类主流记忆自改进方案AWM、RBank，以GPT-5-mini作为基线模型，在WebArena、VisualWebArena、SCUBA三个网页Agent基准上开展测试
- 拓展两个评估维度：同一配置重复3次运行量化性能方差、随机打乱任务顺序测试任务顺序敏感度
- 针对发现的欠指定问题，提出三类优化：补充任务评分规则、补充环境动作反馈、记忆生成Prompt明确禁用环境不支持的动作
### 关键实验结果
- 71%的实验场景下自改进模块会放大运行方差，相同配置最好与最差轮次的性能差最高达10个百分点；默认任务顺序下RBank仅带来1.5%的性能提升，无统计显著性
- 随机打乱任务顺序后，自改进Agent性能平均下降4.5%，而非预期的性能提升；补充欠指定相关信息可缓解31%的乱序场景性能衰减，但仍无法追平无记忆基线的性能
### 核心结论
记忆型自改进Agent存储的不是经验，而是未验证的假设，缺乏校验的记忆会级联引发后续任务失败
