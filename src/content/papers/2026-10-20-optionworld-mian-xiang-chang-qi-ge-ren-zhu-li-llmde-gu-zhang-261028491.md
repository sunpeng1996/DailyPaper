---
title: 'OptionWorld: A Benchmark for Diagnosing Failures of LLMs as Long-Term Personal
  Assistants'
title_zh: OptionWorld：面向长期个人助理LLM的故障诊断基准
authors:
- Ruoyu Zhang
- Zhaocen Liu
- Weiyi Tian
- Melissa Feng
- Shilong Liu
affiliations:
- University of British Columbia
- University of Chicago
- Independent Researcher
- Princeton University
arxiv_id: '2610.28491'
url: https://arxiv.org/abs/2610.28491
pdf_url: https://arxiv.org/pdf/2610.28491
published: '2026-10-20'
collected: '2026-10-21'
category: Agent
direction: Agent评测 · 长期任务执行故障诊断
tags:
- Agent
- Benchmark
- Long-term Assistant
- Failure Diagnosis
- LLM Evaluation
one_liner: 提出多场景长期助理评测基准，定位LLM Agent跨任务跟踪执行的三类核心故障
practical_value: '- 搭建电商用户全生命周期服务、售后跟进类长期Agent时，需单独设计「任务状态跟踪」模块，明确区分任务实际约束和Agent自身假设，避免自增限制导致任务中断

  - 可复用论文的6阶段链路评分（观测→假设→验证→及时发现→干预→结果）拆解业务Agent的故障点，精准定位瓶颈是信息获取不足还是执行跟进不到位

  - 针对长期任务的提醒逻辑，不要只做未完成任务标记，可新增「临时障碍消失检测」「重试时机触发」规则，比如用户咨询未得到答复后，当客服在线时自动触发跟进'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有长期助理Agent评测基准仅输出最终成功率，无法定位失败根因（信息不足/已获信息未利用/执行故障），难以支撑系统迭代，亟需细粒度的故障诊断评测框架。
### 方法关键点
- 构建8个60天时长的模拟场景，覆盖保险、住房、工作协调等领域，包含192个隐藏待发现任务，Agent需主动从事件和记录中识别需求，无明确任务列表
- 设计6阶递进二进制评分链路：信息观测(O)→风险识别(H)→判断有证据支撑(G)→及时识别(T)→完成干预(I)→任务成功(Y)，可定位每个任务失败的具体环节
- 定义三类核心故障分类：信息缺口（未获取/整合关键信息）、动作选择失误（错过可用行动时机）、自我限制（主动增加任务未要求的约束）
### 关键实验
评测DeepSeek、Fable、Gemini、Grok、Qwen、Astra共6个主流LLM，累计144条轨迹、3456个任务实例。最优系统Astra的任务成功率仅为61.6%；49.5%的失败案例中Agent已提前获取全部关键信息，35.5%的失败案例决策时刻上下文仍包含关键信息。三类核心故障占比分别为30.2%、21.3%、18.9%。补充实验显示：补充缺失信息可恢复部分任务成功，行动提醒可重启任务但仍可能错过截止日期，纠正错误权限限制可恢复正常问询能力。
### 核心结论
长期助理Agent的核心瓶颈早已不是信息获取和记忆能力，而是将已获取信息与未完成任务关联、在截止日期前跟进执行、区分实际约束和自身假设的任务状态维护能力。
