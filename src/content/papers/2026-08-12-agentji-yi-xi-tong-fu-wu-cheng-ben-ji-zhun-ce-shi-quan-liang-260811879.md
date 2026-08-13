---
title: Total Recall at What Cost? Benchmarking the Serving Cost of Agentic Memory
  Systems
title_zh: Agent记忆系统服务成本基准测试：全量记忆的代价是什么？
authors:
- Natchanon Pollertlam
- Witchayut Kornsuwannawit
affiliations:
- Bricks Technology, Thailand
arxiv_id: '2608.11879'
url: https://arxiv.org/abs/2608.11879
pdf_url: https://arxiv.org/pdf/2608.11879
published: '2026-08-12'
collected: '2026-08-13'
category: Agent
direction: Agent记忆系统 · 成本-准确率权衡
tags:
- Agentic Memory
- Cost Benchmark
- LLM Inference
- Conversational Agent
- Cost-Accuracy Tradeoff
one_liner: 对3种主流Agent记忆系统做成本-准确率联合基准，给出不同场景下的成本盈亏平衡点
practical_value: '- 部署长会话Agent时不要默认选记忆系统：若平均会话轮次<50轮，直接传全上下文的成本可能低于带记忆系统的方案

  - 记忆系统与LLM backbone需联合选型：同个记忆系统在不同backbone上的单位正确回答成本可差5倍以上，例如Mem0在Gemma 4 26B上成本比gpt-oss-20b低67%

  - 多轮会话成本预测不要仅用会话长度/单轮token数作为指标：记忆系统内部触发逻辑（定期事实提取、阈值触发的记忆合并）带来的成本占比可达30%以上，仅统计会话属性的预测误差最高达69%

  - 优先匹配业务会话长度选记忆系统：短会话选Mastra OM（0轮即可盈亏平衡），长会话（>300轮）可选Hindsight（准确率达54%，成本低于全上下文）'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
长会话Agent普遍采用记忆系统降低全上下文重传的推理成本，但现有评估仅关注准确率，对记忆系统本身的多阶段推理开销（事实提取、检索、合并）缺乏系统的成本基准，从业者无法判断什么场景下用记忆系统更划算。

### 方法关键点
- 对比3种主流记忆系统（Mem0、Hindsight、Mastra Observational Memory）和2个基线（固定大小滚动窗口、全上下文重传），覆盖2种backbone（gpt-oss-20b、Gemma 4 26B A4B）、2种推理强度设置、最多400轮对话
- 构建log-log可分成本模型，单独拟合单轮token数、会话深度对成本的影响系数，用留一交叉验证评估模型泛化性
- 成本与准确率匹配测试：在LoCoMo数据集665个问答对上同步测试准确率，计算单位正确回答成本

### 关键结果
- 传统基于会话长度、单轮token数的成本预测对基线误差<6.5%，但对记忆系统的预测误差达18%~69%，记忆系统内部逻辑是成本的核心驱动因素
- 不同记忆系统的盈亏平衡点差异极大：Mastra OM最短0轮即可回本，Mem0需要0~342轮，Hindsight最长到400轮仍无法回本；400轮时盈亏平衡的记忆系统成本仅为全上下文的1/12.7
- 准确率跨度21%~54%，无系统在成本和准确率上同时最优：Mastra OM在gpt-oss-20b低推理强度下单位正确回答成本最低（0.028美元/100轮），Mem0在Gemma 4上成本最优（0.037美元/100轮）

**最值得记住的一句话**：Agent记忆系统不存在通用最优解，是否划算完全取决于预期会话长度、backbone选型和业务对准确率的要求，短会话场景下全上下文重传可能比记忆系统性价比更高。
