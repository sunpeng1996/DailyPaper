---
title: 'ABF-Bench: A Verifiable Benchmark for Agentic Blockchain Forensics'
title_zh: ABF-Bench：面向智能体区块链取证的可验证基准
authors:
- Xiaohang Yu
- Hejia Geng
- William Knottenbelt
affiliations:
- Imperial College London
- University of Oxford
arxiv_id: '2610.23656'
url: https://arxiv.org/abs/2610.23656
pdf_url: https://arxiv.org/pdf/2610.23656
published: '2026-10-15'
collected: '2026-11-01'
category: Agent
direction: Agent 可验证多跳推理任务基准
tags:
- Agent
- Benchmark
- Working Memory
- Verifiable Reasoning
- Multi-hop Tracing
one_liner: 提出面向LLM Agent的可验证区块链取证基准与配套带工作内存的Agent框架
practical_value: '- 可借鉴「每步结论必须绑定检索到的原始证据」的设计，给电商合规Agent、客诉处理Agent加溯源校验，大幅降低LLM幻觉导致的错误输出

  - 多跳推理任务可复用带working memory的Agent架构，提升用户转化路径归因、黑灰产作弊链路排查等场景的召回率

  - 评测任务构建可复用保守截断规则，明确任务边界，解决当前搜索/推荐Agent评测歧义大、标准不统一的问题'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
区块链取证属于对抗性开放任务，洗钱手法动态变化，传统固定规则追踪工具适配性差，且暂无可验证的LLM Agent评测基准，无法客观衡量Agent在需绑定原始证据的多跳追踪任务上的表现。
### 方法关键点
1. 构建ABF-Bench：基于真实洗钱案例生成跨账本资金追踪任务，要求Agent所有追踪结论必须绑定自身检索到的原始账本记录；采用保守截断规则明确任务边界，生成标准答案参考图，覆盖多跳转账、跨链流转、混币等多类场景。
2. 提出适配任务的ABF Agent Harness：基于working memory实现多轮推理的证据管理。
### 关键结果
ABF Agent Harness边召回达75%，较同底座Codex高28pct、较Claude Code高65pct；未知托管服务识别率89%（固定顺序追踪器为0%），证据保真度98%；大任务存在提前终止问题，最终召回低于最优固定追踪器。
