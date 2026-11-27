---
title: Evaluating Memanto on DolphinBench for AI Agents
title_zh: 基于DolphinBench的记忆Agent Memanto性能测评
authors:
- Suleman Khan
- Rasa Rahnema
- Tara Khani
- Majid Fekri
- Fattane Zarrinkalam
affiliations:
- University of Guelph
- EdgeAI Innovations Inc.
arxiv_id: '2611.28231'
url: https://arxiv.org/abs/2611.28231
pdf_url: https://arxiv.org/pdf/2611.28231
published: '2026-11-19'
collected: '2026-11-27'
category: Agent
direction: Agent长时记忆系统测评
tags:
- AI Agent
- Long-term Memory
- Benchmark
- Information Theoretic Retrieval
- DolphinBench
one_liner: 基于信息论打分的记忆Agent Memanto在DolphinBench上取得远超基线的精度、成本与延迟表现
practical_value: '- 电商导购、客服类Agent的记忆系统可复用「信息论相关性打分+阈值过滤+TopN召回」策略，避免遗漏更新后的事实，提升多轮任务准确率

  - 单任务迭代次数限制、推理effort分级、召回记忆量封顶三种工程手段可大幅降低推理成本和latency，且不会显著降低准确率，适合C端高并发Agent场景落地

  - 记忆系统选型不能只看召回准确率，需结合任务完成率、成本、延迟三个维度做端到端测评，可复用DolphinBench的「有记忆能过、无记忆必败」验证方法自建业务测评集'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent记忆基准多为显式问答格式，直接告知需要召回的信息，不符合真实场景中用户需求隐式、需要Agent自主判断需召回记忆并完成工具调用的情况；且多数基准未强制要求披露成本、延迟指标，无法指导工业级落地。

### 方法关键点
- 测评对象Memanto记忆Agent采用信息论相关性打分（ITS）做记忆排序，无近似近邻索引误差，相同查询返回结果完全一致
- 召回策略设置0.1的相关性阈值过滤无关记忆，同时设置Top50的召回上限控制上下文窗口大小
- 基于DolphinBench测评，该数据集共600个职场模拟任务，所有任务均通过「给记忆能通过、不给记忆必失败」的验证，强制要求同时报告准确率、总成本、中位数延迟三个指标

### 关键实验
- 基线为DolphinBench官方报道的Hermes框架下5种记忆方案（内置记忆、Mem0、Honcho、Hindsight、Supermemory），均基于GPT-5.6-Luna，单任务最多60次迭代
- Memanto方案在Hermes框架+GPT-6-Luna下，单任务最多6次迭代，实现83.83%的任务通过率，比最优基线Mem0的70.67%高13.16个百分点
- 总运行成本为$10.86，比最便宜的基线（内置记忆$61.48）低82.3%；中位数任务延迟15.32s，比最快基线Mem0的37.69s低59.4%

### 核心结论
记忆系统的选型不仅决定Agent的召回能力，还直接决定任务完成率和落地的综合成本，必须做端到端的全链路测评。
