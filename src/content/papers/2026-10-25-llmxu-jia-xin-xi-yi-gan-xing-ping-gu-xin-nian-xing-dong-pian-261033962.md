---
title: 'Beyond Belief: Evaluating and Mitigating LLM Susceptibility to Misinformation'
title_zh: LLM虚假信息易感性评估：信念-行动偏差的发现与缓解
authors:
- Emran Kanaan
- Jiho Lee
- Ibrahim Odat
- Soroush Vosoughi
- Weicheng Ma
affiliations:
- Oakland University
- Dartmouth College
arxiv_id: '2610.33962'
url: https://arxiv.org/abs/2610.33962
pdf_url: https://arxiv.org/pdf/2610.33962
published: '2026-10-25'
collected: '2026-10-27'
category: Agent
direction: Agent 安全 · 虚假信息抵抗
tags:
- Misinformation Resistance
- Tool-using Agent
- Belief-Action Gap
- Safety Evaluation
- LLM Alignment
- Prompt Engineering
one_liner: 发现LLM即使判定信息不可信仍有27%-99%概率执行有害工具调用，验证信念-行动偏差并给出两类落地方案
practical_value: '- 搭建电商/广告领域的自动化Agent时，不要仅依赖LLM输出的可信度判断作为安全拦截依据，必须加独立的工具调用行为校验层，支付、用户信息披露类高危操作需额外叠加规则校验

  - 推理端可直接复用简单前置预警prompt的方案，能在多数LLM上降低8-21个百分点的有害执行率，性价比远高于基于示例的prebunk方案

  - 垂直领域Agent（如电商客服、运营自动化Agent）可在SFT阶段加入虚假操作拒绝样本，能大幅降低未见过的真实攻击的有害执行率，需同步评估合法任务准确率的损耗

  - 评估Agent安全时不要使用先打分再执行的流程，会导致易感性被低估15个百分点，必须模拟真实无前置询问的使用场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前工具调用型LLM/Agent已被广泛应用于电商运营自动化、用户服务、支付处理等业务场景，但现有安全评估仅依赖LLM输出的可信度判断作为安全依据，从未验证口头的不信任是否会真正对应到行为上的拒绝，既存在严重的评估偏差，也缺乏可落地的低成本缓解方案。
### 方法关键点
- 数据集：构建196条配对的虚假/合法可执行通知（覆盖支付、信息披露、运营调度三类场景）、204条真实归档攻击样本（钓鱼短信、事实核查过的虚假声明）、大规模生成式虚假叙事库
- 评估流程：对比「先打分后执行」的传统评估流程、无前置可信度询问的真实场景执行流程
- 缓解方案：横向对比推理端前置预警、示例预提示（prebunk）、针对虚假操作拒绝的SFT训练三类方案的防护效果与业务损耗
### 关键实验结果
测试5款主流LLM（LLaMA-3.1-8B-Instruct、Gemma-2全系列、Qwen3-14B、Gemini-3.6-Flash）：
1. 无防御时，LLM对自己判定为不可信（7分制≤3分）的虚假信息，仍有27%~99%的概率执行有害工具调用
2. 移除前置可信度打分步骤，有害执行率平均提升15个百分点，说明传统先打分后评估的流程会显著低估真实场景下的易感性
3. 推理端仅加简单前置预警prompt，即可让4/5款模型的有害执行率下降8~21个百分点，效果优于所有测试的示例预提示方案；SFT在打分优先流程下可将真实攻击的有害执行率从77.5%/86.8%降至27.3%/15.5%，但无打分流程下防护效果大幅下降
### 核心结论
LLM的口头可信度判断和实际行为是完全独立的两个输出，所有Agent安全策略必须针对最终行为做校验，而不是仅依赖模型的口头判断。
