---
title: 'ToolTurns: Benchmarking LLM Agents in Multi-Turn Dialogue'
title_zh: ToolTurns：面向多轮对话场景的LLM智能体工具使用评测基准
authors:
- Milad Gholami
- Brendan King
- Jeffrey Flanigan
affiliations:
- University of California, Santa Cruz
arxiv_id: '2611.14925'
url: https://arxiv.org/abs/2611.14925
pdf_url: https://arxiv.org/pdf/2611.14925
published: '2026-11-11'
collected: '2026-11-13'
category: Agent
direction: Agent多轮工具调用能力评测
tags:
- Agent
- Benchmark
- Tool Calling
- Multi-turn Dialogue
- LLM Evaluation
one_liner: 提出覆盖1.8k+工具的多轮工具调用评测基准，配套带校验修复的用户模拟器
practical_value: '- 电商导购/客服Agent多轮能力评测可复用模糊初始query+动态follow-up的测试范式，避免单轮测试高估线上实际效果

  - 自研用户模拟器时可直接套用checker-fixer pipeline，先校验对话缺陷再修复，可降低41%的检测缺陷，人类偏好提升63.3%

  - 多轮Agent效果评估不要仅依赖对话流畅度等rubric分数，需单独测试任务完成率，两者相关性仅0.23，rubric高分模型可能任务完成率极低

  - 部署多轮交互Agent时需针对性优化上下文继承逻辑，实测所有模型第二轮follow-up成功率比初始请求低2~16个百分点'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有工具调用评测大多聚焦单轮孤立请求，忽略真实对话中用户初始请求模糊、需要Agent主动澄清、后续会发起上下文相关follow-up的场景，无法准确衡量Agent在真实会话中的工具使用和上下文留存能力。

### 方法关键点
- 构建2620个初始模糊问题集，覆盖47个类别、1827个工具、11004个API端点，每个问题默认包含初始请求+2轮动态follow-up请求
- 自研开源用户模拟器，根据Agent回复动态生成澄清回答和follow-up请求，配套checker-fixer pipeline：先LLM校验生成内容是否存在上下文不一致、重复、无进展等11类缺陷，再针对性修复缺陷
- 评估体系分两类：1）任务完成率，每个subtask（初始+两轮follow-up）单独用hybrid（规则门控+LLM judge）评估是否完成；2）对话质量rubric，从一致性、相关性、效率、正确性、适配性5个维度打分

### 关键结果
对比9款闭源/开源Agent模型，最优闭源模型Claude Opus 4.8单subtask成功率69.6%，全对话3轮全完成率仅39.8%；所有模型的follow-up请求成功率均低于初始请求，下降幅度2.1~16.2个百分点；对话质量rubric排名和任务完成率排名的Spearman相关性仅0.23，两者衡量的是完全不同的能力。

### 核心结论
多轮工具调用Agent的能力不能通过单轮测试或对话流畅度推断，必须在真实多轮交互下直接测量任务完成率。
