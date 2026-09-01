---
title: 'AgenticRag-R1: Agentic Reinforcement Learning with Stack Memory for Multi-Step
  Reasoning, Retrieval and Memorizing'
title_zh: AgenticRAG-R1：带栈内存的智能体强化学习多步推理检索框架
authors:
- Xinke Jiang
- Yue Fang
- Zhibang Yang
- Jiaran Gao
- Zhixin Zhang
- Tao Feng
- Rihong Qiu
- Wentao Zhang
- Hongxin Ding
- Ruizhe Zhang
affiliations:
- 北京大学软件工程国家工程研究中心
- 北京大学计算机学院
- 教育部高可信软件技术重点实验室
- GRG Banking Equipment Co., Ltd.
- 北京大学前沿计算研究中心
arxiv_id: '2608.29622'
url: https://arxiv.org/abs/2608.29622
pdf_url: https://arxiv.org/pdf/2608.29622
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: Agent · 多步推理RAG RL优化
tags:
- Agentic RAG
- Reinforcement Learning
- Stack Memory
- Multi-step Reasoning
- Trajectory Filtering
one_liner: 提出融合栈内存、细粒度动作空间与信息感知轨迹筛选的RL增强Agentic RAG框架
practical_value: '- 电商商品问答、客服场景可复用细粒度动作设计：新增<backtrack>、<summary>等栈操作动作，解决多轮检索推理的错误累积问题，提升多跳用户问题答准率

  - RL训练流程可直接复用分层奖励+信息感知轨迹筛选机制：分层奖励解决稀疏终局奖励的credit assignment问题，轨迹筛选优先保留高方差高价值样本，提升小样本下RL训练效率

  - 长路径任务（如导购路径规划、深层用户需求挖掘）可复用栈内存设计：LIFO结构支持推理状态回滚，解决现有Agent多轮决策容易跑偏的问题

  - 可直接参考奖励预算归一化方法，避免Agent为拿过程奖励频繁调用检索工具的reward hacking问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agentic RAG在多步推理场景存在两大痛点：一是采用粗粒度动作空间与仅终局奖励，导致reward分配模糊，易倾向短路径模板化推理，且中间错误无法修正引发误差累积；二是训练数据中短路径低信息样本占比高，RL易过拟合到简单策略，无法习得复杂长路径推理能力。

### 方法关键点
- 动作与内存设计：定义6种细粒度可解释动作（<plan>/<think>/<search>/<backtrack>/<summary>/<conclusion>），搭配LIFO栈内存，支持中间推理状态的压入、弹出、修改，可回滚错误步骤
- 分层奖励机制：拆分为终局奖励（答案与ground truth匹配度）和过程奖励（动作格式合规分+检索结果relevance分+内存操作合理性分），新增奖励预算归一化避免过度调用动作的reward hacking
- 信息感知轨迹筛选：基于UCB思想设计轨迹评分，同时考虑单样本多rollout的奖励均值、方差和单轨迹奖励，全局筛选top p高价值轨迹参与训练，优先保留高复杂度样本

### 关键实验
在HotpotQA、2WikiMultiHopQA、Bamboogle等7个多跳推理、开放域QA基准上测试，对比ReAct、Search-R1、ARPO等12个基线，3B Qwen2.5 backbone下HotpotQA F1提升6.76%、2Wiki提升3.02%，7B backbone下Bamboogle提升7.1%；长路径实验中，最大推理步数从10升至30时，TriviaQA F1从37.53%升至55.28%，性能随步数增长单调提升，无基线的波动或退化问题。

最值得记住的结论：仅靠终局奖励的RL-based Agent极易陷入短路径懒惰策略，细粒度动作+过程奖励+高价值样本筛选三者结合是解锁长路径复杂推理能力的核心。
