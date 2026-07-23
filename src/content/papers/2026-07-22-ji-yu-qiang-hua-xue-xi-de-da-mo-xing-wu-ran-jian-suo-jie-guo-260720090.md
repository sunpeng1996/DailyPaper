---
title: Reinforcement Learning for Large Language Model Selective Evidence Adoption
  from Contaminated Retrieval Results
title_zh: 基于强化学习的大模型污染检索结果选择性证据采纳方法
authors:
- Yanyu Chen
- Yue Li
- Yongyi Cui
- Dongsheng Shi
- Lichang Dai
affiliations:
- East China Normal University
- Shandong University
arxiv_id: '2607.20090'
url: https://arxiv.org/abs/2607.20090
pdf_url: https://arxiv.org/pdf/2607.20090
published: '2026-07-22'
collected: '2026-07-23'
category: RAG
direction: RAG 污染检索结果证据选择优化
tags:
- RAG
- Reinforcement Learning
- DAPO
- Benchmark
- LLM Agent
- Safety Alignment
one_liner: 构建SelectBench评测集，采用定制奖励的DAPO训练提升大模型污染检索下的证据选择能力
practical_value: '- 电商RAG导购/商品问答场景可复用其三合一奖励设计：调用工具+答案正确+无违禁采纳给正奖励，采纳违禁直接给负奖励，平衡正确性与安全性，避免过度拒答或误纳错误信息

  - 构建业务脏数据评测集可参考其思路：在现有问答数据集基础上混入错误内容、过时信息、prompt注入片段，用于验证RAG/Agent系统的鲁棒性

  - 小参数LLM做RL微调时可参考其优化策略：去掉KL损失/奖励、仅在最终生成token附加奖励，降低训练复杂度的同时不损失通用能力，适合业务低成本落地

  - Agent调用搜索工具场景可固定检索结果，单独训练证据选择能力，排除检索变量干扰，实现快速迭代优化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RAG或调用搜索工具的LLM Agent常面临检索结果混杂有效证据、误导信息、prompt注入的场景，全盘拒答会浪费有效信息，全盘采纳则会引发错误回答、合规风险，现有方案缺乏针对性的评测基准和优化路径，直接影响电商问答、内容生成等场景的落地效果。
### 方法关键点
- 构建SelectBench数据集：含1170条训练样本、325条校正后的SelectBench-v2测试集，样本基于多跳问答数据集构建，混入错误答案、过时信息、prompt注入等污染片段，标注正确答案、违禁内容、注入标记等标签
- 定制DAPO强化学习pipeline：采用三元任务奖励+长度惩罚的复合奖励，采纳违禁内容/未调用工具直接给-1，回答正确且无违禁内容给+1，其余情况给0，额外惩罚超过768token的过长输出，分别实现规则匹配、冻结DeepSeek语义判优两种奖励变体
- 训练优化：去掉DAPO的KL损失与KL奖励，仅在模型最后生成token附加奖励，降低训练复杂度，基于Qwen3.5-4B做微调
### 关键结果
在SelectBench-v2测试集上，原生Qwen3.5-4B严格成功率为22.46%，DAPO-Rule提升至25.54%、违禁内容采纳率从72.62%降至69.23%；DAPO-DeepSeek严格成功率提升至26.46%、违禁内容采纳率降至68.92%，MMLU、干净HotpotQA上通用能力无明显下降，但prompt注入抵抗能力无提升，增益经多重校验后统计显著性不足。
### 核心结论
基于RL的选择性证据采纳当前仅能获得小幅方向性提升，更强的奖励设计、prompt注入抵抗能力是落地的核心瓶颈。
