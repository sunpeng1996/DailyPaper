---
title: 'ForeDreamer: A Self-Evolving Dual-Agent Memory Architecture for Future Event
  Prediction'
title_zh: ForeDreamer：面向未来事件预测的自进化双Agent记忆架构
authors:
- Linhao Zhong
- Zongze Du
- Linyu Wu
- Yu Bo
- Hourong Li
- Chenchen Jing
- Hao Chen
- Yuling Xi
- Chunhua Shen
affiliations:
- Zhejiang University
- Ant Group
- National University of Singapore
- Zhejiang University of Technology
arxiv_id: '2608.20920'
url: https://arxiv.org/abs/2608.20920
pdf_url: https://arxiv.org/pdf/2608.20920
published: '2026-08-21'
collected: '2026-08-24'
category: Agent
direction: Agent 自进化记忆架构优化
tags:
- LLM Agent
- Self-Evolution
- Dual-Agent
- Memory Architecture
- Event Prediction
one_liner: 提出分离事实与经验记忆的双Agent架构，通过双轨自进化提升开放网络事件预测性能
practical_value: '- 处理嘈杂多源用户行为/搜索日志时，可借鉴「主Agent + 记忆处理子Agent」分工，将原始日志提炼为结构化事实记忆，降低主模型输入噪声，适用于长周期用户兴趣建模、大促趋势预测等场景

  - 可复用双轨自进化机制：文本经验轨道沉淀业务决策经验（如选品策略、搜索query优化规则），流程经验轨道迭代数据处理工具（如噪声过滤、信息抽取工具），降低重复开发成本

  - 工具复用+多样性探索的优化思路可直接迁移到Agent工具链迭代场景：通过现有工具聚类复用减少冗余开发，新增多样性探索调度避免陷入局部最优策略'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
开放网络未来事件预测需要从嘈杂、冗余、冲突的公开数据中提炼有效信号，现有RAG、通用Agent记忆方案要么直接投喂原始检索结果，要么仅支持简单的信息存储复用，无法适配高噪声、时间敏感的预测场景，导致预测校准度、准确率不足。

### 方法关键点
- 架构层面分离两类记忆：事实记忆为当前查询定制的结构化检索证据，经验记忆为跨任务积累的持久化经验；采用双Agent分工：主Agent负责搜索规划、证据融合与最终预测，记忆处理子Agent通过MemGuide（流程指引）+ MemTools（可执行处理工具）将原始搜索结果转化为事实记忆
- 双轨自进化机制：文本经验轨道通过增删改操作迭代经验库，优化搜索规划、证据融合、预测校准逻辑；流程经验轨道迭代MemGuide与MemTools，新增组合工具复用、多样性引导探索两个优化，减少重复工具开发、避免策略局部收敛

### 关键实验
在Prophet Arena、FutureX两个公开事件预测benchmark上对比Full Text、RAG、Mem0、HippoRAG 2等8个基线：
- 基于Qwen3.5-Flash backbone时，Prophet Arena平均Brier分数低至0.1471，比最优基线降低16.4%；FutureX准确率达0.4108，比最优基线提升17.5%
- 消融实验验证双轨进化、两个优化策略均带来显著性能提升，且效果不受搜索提供商、检索量、上下文长度等配置影响

### 最值得记住的一句话
Agent记忆不应仅作为静态信息存储载体，更要通过进化沉淀任务决策经验与数据处理流程，才能在高噪声开放场景下获得稳定性能增益
