---
title: 'WorldLeague: Benchmarking Physical Agency'
title_zh: WorldLeague：面向具身智能的物理智能体能力评测基准
authors:
- Xinyang Zhou
- Qi Li
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2611.30989'
url: https://arxiv.org/abs/2611.30989
pdf_url: https://arxiv.org/pdf/2611.30989
published: '2026-11-22'
collected: '2026-11-24'
category: Agent
direction: 具身智能Agent 物理能力评测基准
tags:
- Embodied AI
- Agent Benchmark
- VLM
- VLA
- WAM
one_liner: 推出覆盖6类能力的60项模拟机器人任务基准，可统一评测VLM/VLA/WAM三类具身模型的物理执行能力
practical_value: '- 电商智能拣选/仓储机器人的Agent能力评测，可复用该基准的「任务分维度打分+进度/完成率双指标」框架，避免只看最终结果忽略中间过程能力

  - 用LLM/VLM做上层决策、下层对接执行器的具身Agent架构，可借鉴其决策保留的动作抽象设计：上层模型仅负责目标选择、动作参数、序列规划，底层执行器负责运动控制与反馈回传，降低架构耦合度

  - 该研究验证71.8%的VLM能正确回答场景问题但实际执行得分为0，纯文本/视觉问答评测不能替代物理交互评测，落地具身Agent必须加真实/模拟环境的执行效果校验'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有具身AI基准多围绕具体家务任务设计，无法拆解评测智能体感知、记忆、规划、动作等不同维度的底层能力，也缺少统一框架对齐VLM、VLA、WAM三类不同架构具身模型的物理执行水平，难以回答当前AI系统能自主完成多大范围物理目标的核心问题。

### 方法关键点
- 设计3条任务赛道共60项模拟机器人任务：WorldSeek（探索找物，测导航/目标对齐）、WorldShape（物体重排，测几何/物理推理）、WorldShift（场景适配，测时序记忆/约束管理），覆盖6类核心能力维度
- 设计统一评测接口：VLM通过WorldHarness抽象层发送动作指令（选择目标、动作参数、序列），底层控制器执行后回传反馈；VLA/WAM直接用原生控制接口，三类模型共用相同的任务目标、约束与打分规则
- 提出双维度评测指标：Interactive Score（0-100分，衡量任务完成进度）、物理成功率（是否完全满足所有目标与约束），最终输出Physical Agency Profile反映模型各维度能力

### 关键结果
- 评测13款主流具身模型，Claude Fable 5.2拿到最高平均Interactive Score 28.58/100，仅完成13/60项任务，当前顶尖模型物理执行能力仍处于较低水平
- GPT-6.1-Sol与GPT-6-Astra在约束管理类任务并列第一，完成3/6项任务
- 71.8%的VLM在能完全正确回答场景终端QA的情况下，物理任务Interactive Score为0，认知能力与执行能力存在显著断层

### 核心结论
对具身智能体而言，对场景的正确认知与中间动作的正确执行，与最终物理目标的完成之间存在巨大鸿沟，不能用文本/视觉问答评测替代物理交互评测
