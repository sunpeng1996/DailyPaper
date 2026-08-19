---
title: 'Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents'
title_zh: 驾驭记忆：记忆Agent中各类存储介质的整体性评估
authors:
- Wei-Chieh Huang
- Weizhi Zhang
- Yuchen Wu
- Yankai Chen
- Eric Hanchen Jiang
- Wooseong Yang
- Yiwei Yang
- Henry Peng Zou
- Hanrong Zhang
- Ying Nian Wu
affiliations:
- University of Illinois Chicago
- University of Washington
- McGill University
- MBZUAI
- University of California, Los Angeles
arxiv_id: '2608.15008'
url: https://arxiv.org/abs/2608.15008
pdf_url: https://arxiv.org/pdf/2608.15008
published: '2026-08-14'
collected: '2026-08-19'
category: Agent
direction: Agent长时记忆存储介质选型评估
tags:
- MemoryAgent
- MemorySubstrate
- Evaluation
- Retrieval
- Efficiency
- LLM
one_liner: 统一评估7大类11种Agent记忆存储介质，给出跨场景跨规模的选型依据与路由规则
practical_value: '- 电商导购/个性化推荐Agent选型记忆存储时，用户历史问答类场景优先选结构型/分层存储，流程引导等决策类场景优先选精炼型/扁平索引存储，平衡效果与延迟

  - 可直接复用检索深度调优规则：QA类任务（如用户历史偏好查询）检索k越大效果越好，决策类任务（如下单链路引导）k控制在1-2避免注意力稀释

  - 跨多会话的长期用户记忆系统优先选精炼类存储（如策略蒸馏、技能包），latency随历史长度增长更平缓，避免长周期下性能骤降

  - 单会话等短周期任务优先用BM25等扁平索引，成本仅为结构型存储的1/10-1/100，性价比最高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长时记忆是长周期LLM Agent的核心基建，但现有评估高度集中于对话场景，仅62%的系统覆盖2个对话数据集，仅21%的系统披露效率指标，也没有跨任务、跨规模的统一对照实验，不同记忆存储介质（向量库、知识图谱、KV cache、LoRA等）的适用场景完全不明确，开发者缺乏可落地的选型依据。

### 方法关键点
- 覆盖7大类11种记忆存储介质，包含外部存储（扁平稠密/稀疏向量索引、文本摘要、结构图谱、分层树、精炼策略/技能包）和内部存储（LoRA权重更新、激活类KV缓存机制）
- 统一评测框架控制变量：固定3种backbone（Qwen3-8B、Qwen3-32B-AWQ、Gemma4-26B-MoE）、固定辅助LLM为GPT-4O-MINI，覆盖4类基准（用户对话QA、记忆能力测试、具身决策、代码生成），采集26项性能+效率全维度指标
- 两组核心消融：检索深度k梯度测试，历史长度从6K到262K tokens的可扩展性测试

### 关键结果
- 无单一介质全场景最优：对话QA场景结构型图谱存储准确率比扁平索引高15%-20%，但延迟是后者的10-100倍；具身决策场景精炼策略存储比无记忆基线高9.7%，结构型存储反而劣于基线
- 检索深度对两类任务效果完全反向：QA类任务k从1升到20准确率单调上升，决策类任务k超过2后准确率下降超7%，核心原因是注意力从当前任务上下文转移到冗余检索内容
- 长历史下精炼类存储性能提升19%的同时延迟仅增长10倍，结构型存储延迟增长超100倍，性价比骤降

没有任何一种记忆存储介质能通吃所有场景，自适应路由的多介质混合记忆系统才是长周期Agent的最优方案。
