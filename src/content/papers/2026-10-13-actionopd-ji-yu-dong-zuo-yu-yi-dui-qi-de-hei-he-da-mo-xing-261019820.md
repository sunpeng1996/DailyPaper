---
title: 'ActionOPD: Distilling Decisions, Not Tokens'
title_zh: ActionOPD：基于动作语义对齐的黑盒大模型Agent蒸馏方法
authors:
- Huining Yuan
- Xiangmin Yi
- Zelai Xu
- Zixu Wang
- Xinlei Chen
- Xiao-Ping Zhang
- Yu Wang
- Chao Yu
affiliations:
- Tsinghua University
arxiv_id: '2610.19820'
url: https://arxiv.org/abs/2610.19820
pdf_url: https://arxiv.org/pdf/2610.19820
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: Agent 蒸馏 · 语义动作对齐
tags:
- Agent Distillation
- On-Policy Distillation
- Semantic Alignment
- Black-Box LLM
- Tool Use
- RLHF
one_liner: 提出动作级on-policy蒸馏方法，无需教师token概率或分词对齐，跨模型家族蒸馏提升Agent效果3.3-6.9pp
practical_value: '- 电商智能客服/导购Agent蒸馏可直接复用该框架：无需对齐师生分词器，可调用GPT-4/Claude等黑盒大模型作为教师，大幅降低蒸馏门槛，灵活适配业务场景

  - 语义匹配奖励设计可迁移到推荐/广告场景：工具调用忽略参数顺序/格式差异仅校验语义一致性，自然语言回复比对意图和事实而非全文匹配，适合query改写、话术生成等任务的对齐

  - Self-ActionOPD思路可用于无标注Agent迭代：给同模型添加特权信息（业务规则、用户私域标签）作为教师，蒸馏出仅用公共上下文的轻量化模型，无需额外标注成本即可落地业务规则

  - state-group rollout工程方案可直接复用：同状态采样多个学生输出选最高奖励执行，兼顾探索性和分布对齐，减少离线蒸馏的师生状态分布偏移问题，适合多轮交互推荐Agent训练'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent蒸馏存在两类核心问题：离线蒸馏模仿教师token序列存在师生状态分布偏移，泛化性差；token级on-policy蒸馏要求师生同模型家族、共享分词器且需要教师token概率，无法直接用黑盒大模型当教师，且token级对齐忽略决策语义，相同决策不同措辞会被判定为不匹配，浪费监督信号。

### 方法关键点
- 核心优化目标为学生遇到的状态下，学生输出动作与教师动作的语义对齐概率，而非复现教师token序列
- 奖励设计：每个状态采样K=3个教师动作，工具调用通过参数归一化校验匹配度，自然语言回复比对意图与事实，匹配得基础奖励+额外匹配次数的频率奖励，无效动作扣1分
- 训练流程：每个状态采样N=4个学生输出，选最高奖励的执行推进交互，所有输出用PPO优化，优势按同组奖励均值归一化，消除组间奖励差异干扰
- 扩展Self-ActionOPD：给同模型教师添加特权信息（任务规则、目标），蒸馏出仅用公共上下文的学生，实现无标注自提升

### 关键实验
训练基于AWM、EnvScaler共6697个工具调用任务，在BFCL、ToolSandbox、AppWorld、τ2-bench四个分布外数据集测试，对比离线KD、token级OPD基线：
- 给Qwen3-4B/8B带来3.3-6.9pp的平均性能提升，跨模型家族（DeepSeek教师蒸馏Qwen学生）效果稳定
- τ2-bench pass1指标比token级OPD高0.4pp，无需教师logit或分词对齐；Self-ActionOPD给base模型带来4.8pp的pass1提升

**最值得记住的一句话：Agent蒸馏的核心是对齐决策语义而非复现token序列，黑盒大模型可作为低成本教师快速蒸馏出可用的小模型Agent**
