---
title: 'AMTFV: Agentic Mathematical Tool-Flow Verification for LLM Self-Correction'
title_zh: 面向大模型数学推理自纠错的智能体化工具流验证框架AMTFV
authors:
- Rui Zou
- Yutao Zhu
- Mengqi Wei
- Ji-Rong Wen
affiliations:
- Renmin University of China
- Central China Normal University
arxiv_id: '2607.29549'
url: https://arxiv.org/abs/2607.29549
pdf_url: https://arxiv.org/pdf/2607.29549
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: LLM推理 · 多智能体工具调用自纠错
tags:
- Agent
- Self-Correction
- Mathematical Reasoning
- Tool Use
- LLM
one_liner: 提出解耦数学验证建模与底层执行的多智能体自纠错框架，数学推理准确率最高提升8.3pp
practical_value: '- 可复用「上层任务建模-下层工具执行」解耦的多智能体架构，解决电商/广告场景的数值计算、规则校验类需求（如优惠券凑单、满减计算校验），避免LLM直接生成代码的不稳定问题

  - 可借鉴MTF结构化工具请求设计，定义业务场景专属的工具调用中间协议（如电商库存校验、价格计算工具接口），降低LLM工具调用出错率

  - 多轮迭代校验+工作流修订机制可迁移到推荐文案、营销活动规则自纠错场景，既提升错误检出率，也避免过度修正正确结果'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM数学推理自纠错方案存在两类缺陷：自然语言反思类方法缺乏精确计算支撑，错误检出率低；直接生成代码校验类方法过早将数学建模与底层实现耦合，易引入代码错误且故障难以定位，无法满足复杂推理场景的高可靠性要求。
### 方法关键点
- 核心设计Mathematical Tool Flow（MTF）中间接口，遵循「中断-执行-恢复」交互模式，上层智能体仅需描述计算目标，无需关注底层实现细节
- 架构拆分4类智能体分工协作：验证智能体搭建校验工作流、答案修订智能体基于工具结果修正答案、工作流修订智能体优化校验覆盖度，工具箱智能体负责将MTF请求转换为SymPy、枚举计算等工具的可执行调用
- 多轮迭代闭环机制：校验通过直接输出结果，不通过则优先修订答案，答案无变更则修订校验工作流，直到达到轮次上限
### 关键实验
在5个高难度数学推理数据集（AIME2024/2025、BRUMO2025等共170道题）上，对比Self-Refine、ProgCo等7种基线，覆盖DeepSeek、GPT、Gemini共7种模型配置：AMTFV在所有配置下准确率均为最高，相比最强基线平均准确率最高提升8.3个百分点；错误修正率达18.4%，远高于基线的9.4%~12.2%，同时正确答案误伤率仅2.8%，低于基线的3.7%~4.2%；中高验证复杂度样本上归一化准确率提升达39.2%、84.6%。
### 核心结论
让LLM聚焦擅长的高维逻辑建模，把精确计算、枚举类任务完全交给专业化工具，是提升复杂推理任务可靠性的核心路径
