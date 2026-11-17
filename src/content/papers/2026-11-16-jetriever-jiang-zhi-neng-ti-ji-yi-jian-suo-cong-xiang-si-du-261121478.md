---
title: 'Jetriever: Shifting Agent Memory Retrieval from Similarity to Utility'
title_zh: Jetriever：将智能体记忆检索从相似度匹配转向效用评估
authors:
- Ruizhe Li
- Licheng Zhang
- Mingxuan Du
- Zhendong Mao
affiliations:
- University of Science and Technology of China
arxiv_id: '2611.21478'
url: https://arxiv.org/abs/2611.21478
pdf_url: https://arxiv.org/pdf/2611.21478
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: Agent记忆检索 · 效用排序优化
tags:
- Agent-Memory
- Utility-Retrieval
- RAG
- LLM-Agent
- Memory-Retrieval
one_liner: 基于轻量决策模型Jev做全量记忆效用排序，解决Agent隐式关联记忆召回盲区
practical_value: '- 电商/导购Agent场景可直接复用思路：针对用户隐式需求（如过敏史、偏好的隐式关联），用小参数量决策模型做记忆效用打分，无需依赖query扩展猜关键词，避免推荐错漏或安全事故

  - 单用户记忆池规模<2000的场景，可直接用全池效用排序替代BM25/向量检索，成本仅几分钱一次，InMind场景下R@1可从1.6%提升至84.8%

  - 工程上可采用级联检索架构：第一阶段用BM25+向量召回扩大粗筛量到数百条，第二阶段用Jev类决策模型精排，既控制成本又不会漏召回隐式关联记忆

  - 记忆分块优先拆成短片段而非长会话打包，实验显示短片段的效用排序R@1比长会话高35个百分点，效用判断准确率更高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent记忆检索普遍采用相似度匹配逻辑，仅能召回与查询存在字面/语义重叠的记忆，无法覆盖需要世界知识关联的隐式有用记忆（如用户坚果过敏史与马卡龙食谱的关联），成为Agent落地的核心瓶颈——此前InMind基准上最优记忆系统的端到端正确率仅14.4%，远低于将黄金记忆直接输入LLM的84.0%。

### 方法关键点
- 提出Jetriever全量效用排序框架，放弃相似度匹配范式，直接遍历所有存储记忆，逐片判断其对当前查询的有用性作为排序依据
- 采用Jev轻量决策模型作为打分器：基于大模型底座做RLCD校准训练，自带通用世界知识，仅输出结构化的效用概率分无需生成自由文本，推理成本远低于常规LLM
- 无ANN索引依赖，直接对所有(query, memory)对的效用分倒排取TopK，确定性排序避免隐式记忆被过滤

### 关键结果
- 数据集：InMind-125隐式关联记忆任务、MemoryAgentBench（MAB）维度比例抽样60任务
- 核心指标：InMind任务R@1达84.8%，较BM25（1.6%）、MiniLM（0.0%）提升数十倍；端到端应用正确率达76.0%，接近黄金记忆直接喂入的84.0%，远超此前SOTA的14.4%；MAB任务综合得分55.4%，较ReFind高11.1个百分点；单查询检索成本仅0.0083~0.031美元，100并发下每秒可处理71.5次打分。

### 值得记住的一句话
Agent记忆检索的核心目标是召回对回答有用的记忆，而非与查询相似的记忆。
