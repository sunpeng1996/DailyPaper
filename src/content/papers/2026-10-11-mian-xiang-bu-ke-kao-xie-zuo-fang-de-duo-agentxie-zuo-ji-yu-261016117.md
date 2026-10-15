---
title: 'Beyond Perfect Teammates: Multi-Agent Collaboration with Unreliable Colleagues'
title_zh: 面向不可靠协作方的多Agent协作基准与能力测评
authors:
- Chen Huang
- Yiyang Zhang
- Yuhao Wu
- Yang Deng
- Wenxuan Zhang
affiliations:
- Singapore University of Technology and Design
- Singapore Management University
arxiv_id: '2610.16117'
url: https://arxiv.org/abs/2610.16117
pdf_url: https://arxiv.org/pdf/2610.16117
published: '2026-10-11'
collected: '2026-10-15'
category: Agent
direction: 多Agent协作 · 不可靠场景鲁棒性测评
tags:
- Multi-Agent
- Collaboration Robustness
- Benchmark
- Fault Recovery
- LLM Agent
one_liner: 提出UNCOBENCH基准，测评多Agent在不可靠协作场景下的证据校验与故障恢复能力
practical_value: '- 搭建业务多Agent系统时，需额外针对三类不可靠场景（输出错配、信息不全、无响应）设计校验逻辑，而非默认协作方输出可靠

  - 可复用UNCOBENCH的故障注入方法，对内部Agent工作流做压力测试，提前定位协作链路的鲁棒性短板

  - 针对Misaligned类故障（对准确率影响最大），可在Agent调用后增加上下文匹配校验规则，避免直接使用错误证据导致决策失误'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多Agent系统与测评均默认协作方输出完全可靠、响应及时，但真实场景中协作Agent常出现回复上下文错配、信息不全、无响应等非恶意故障，导致主Agent决策错误，当前缺乏专门基准区分Agent的基础任务能力与故障恢复能力。

### 方法关键点
- 定义三类不可靠协作场景：Misaligned（输出上下文错配）、Incomplete（信息不全）、Missed（无响应）
- 提出自动化基准构造流水线，结合LLM生成结构化场景与程序校验，保障任务答案唯一、角色信息不可替代
- 构造1000组配对任务，相同决策背景下分别对应可靠、三类不可靠共4种场景，固定ground truth排除任务难度干扰

### 关键实验
在10款开源/闭源LLM上测评，发现可靠场景下性能相近的模型鲁棒性差异极大：Claude Opus 5可靠场景准确率96.7%，Misaligned场景仅下降6pp到90.7%，而GPT-5.6 Sol可靠场景准确率98.7%，Misaligned场景暴跌52.9pp到45.8%；三类场景中Misaligned最难，最高准确率下降可达78.8pp，Missed最易恢复，多数模型准确率下降仅0.2%~3.3pp；混合多故障场景下最高准确率仅45.2%。

多Agent协作的鲁棒性不仅取决于基础推理能力，更取决于主动校验证据、诊断故障、针对性恢复信息的能力。
