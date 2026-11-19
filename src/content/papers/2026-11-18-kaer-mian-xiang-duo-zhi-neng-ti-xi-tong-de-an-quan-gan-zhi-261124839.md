---
title: 'Kaer: Security-Aware Replanning for Multi-Agent Systems'
title_zh: Kaer：面向多智能体系统的安全感知重规划框架
authors:
- Tushin Mallick
- Evan Rose
- Matthew Laws
- Alina Oprea
- Cristina Nita-Rotaru
affiliations:
- Northeastern University
arxiv_id: '2611.24839'
url: https://arxiv.org/abs/2611.24839
pdf_url: https://arxiv.org/pdf/2611.24839
published: '2026-11-18'
collected: '2026-11-19'
category: MultiAgent
direction: 多智能体协作 安全重规划
tags:
- MultiAgent
- Replanning Security
- Prompt Injection Defense
- MAS Robustness
- Adversarial Defense
one_liner: 提出安全感知多Agent重规划框架Kaer，通过模板化反馈与确定性修复防御重规划劫持
practical_value: '- 电商/广告场景下对接外部不可信输入的多Agent系统，可复用抽象失败模板设计，将不可信自然语言反馈转换为预设枚举值，彻底切断重规划阶段的prompt注入路径

  - 重规划操作收敛到预先定义的确定性算子集合，每次修改后强制过业务权限校验，可避免LLM Planner被诱导生成调用用户隐私、支付接口等高风险操作，适配推荐系统的内容生成、用户运营等Agent场景

  - 针对恶意/故障Agent伪装任务成功的场景，可加轻量化LLM输出校验层，仅校验输出是否符合子任务的完成形式要求，无需校验内容正确性，即可将防御率提升约10个百分点'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
中心化编排的多Agent系统依赖动态重规划应对执行故障、未知需求等场景，但恶意Agent可在反馈中嵌入prompt注入劫持重规划流程，现有防御仅覆盖工具访问控制、静态预执行策略，未覆盖重规划阶段的安全风险，要么限制重规划灵活性，要么易被注入攻击。
### 方法关键点
- 完全隔离Agent自由文本反馈与Planner，Agent故障反馈仅能从预设的14种抽象失败模板中选择，Planner无权限访问任何Agent生成的自由文本内容
- 重规划仅允许使用7种确定性修复算子（重执行、修改指令、调整权限、重分配Agent、插入/删除子任务、修改依赖），仅可修改未完成的子任务，已执行步骤不可篡改
- 所有修订后的计划必须通过预设的任务策略、Agent权限策略双重校验，超出初始授权的修改必须强制触发用户审批
- 可选增加轻量化LLM输出校验层，检测Agent伪装任务成功的虚假上报
### 关键结果
自建Cintra benchmark，包含14个需重规划的真实任务、14种针对重规划的攻击目标，共164组任务-攻击对。对比无防御的Magentic-One、SOTA防御ControlValve：
- 在gpt-5.6-sol上，Kaer安全得分（攻击拦截率）达92.3%，比ControlValve高22.5pp，比Magentic-One高57.3pp；同时良性任务完成率64.3%，高于ControlValve的54.3%
- 增加LLM输出校验后，Kaer的安全得分进一步提升至96.8%
### 核心结论
多Agent系统的重规划是核心攻击面，将不可信输入的自由度降到最低、将系统可执行操作收敛到最小集合，是平衡可用性与安全性的核心思路。
