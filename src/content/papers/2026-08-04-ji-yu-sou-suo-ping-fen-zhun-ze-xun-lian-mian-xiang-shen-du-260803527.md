---
title: Training Documents Reranker with Search Rubrics for Deep Research Agent
title_zh: 基于搜索评分准则训练面向深度研究Agent的文档重排器
authors:
- Wenhan Liu
- Yu Lu
- Qiaolin Xia
- Hui Xu
- Tong Zhao
- Jian Xi
- Yutao Zhu
- Haijin Liang
- Haibo Shi
- Hao Wang
affiliations:
- Renmin University of China
- Tencent
arxiv_id: '2608.03527'
url: https://arxiv.org/abs/2608.03527
pdf_url: https://arxiv.org/pdf/2608.03527
published: '2026-08-04'
collected: '2026-08-05'
category: Agent
direction: Agent 检索模块优化 · RAG 重排
tags:
- Reranker
- RAG
- Agent
- SFT
- Reinforcement Learning
- Rubric
one_liner: 提出基于分层搜索评分准则的两阶段训练框架，打造适配Agent和RAG的高性能文档重排器RubricRanker
practical_value: '- 可复用分层评分准则设计思路，给电商/内容场景的RAG重排器定义集级（覆盖度、去重、一致性）和单文档级（权威、时效）的质量标准，解决单文档相关度排序无法满足下游生成需求的问题

  - 两阶段训练框架可直接落地：第一阶段用强LLM基于自定义准则打银标做SFT冷启动，第二阶段用准则加权的RL奖励微调，相比直接端到端RL训练更稳定，效果更好

  - 针对电商导购/咨询Agent场景，优化重排器后可显著减少Agent的搜索调用次数，降低latency同时提升回答质量，适合落地到高并发的智能客服、商品咨询Agent'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有文档重排器仅优化单文档与查询的相关度，返回的Top-k文档集合往往无法满足深度研究Agent的复杂信息需求，普遍存在关键信息维度缺失、内容冗余、来源不可靠等问题，既浪费Agent有限的上下文窗口，还可能导致回答错误；而现有面向单轮RAG的生成式重排器泛化性差，无法适配开放域Agent多轮搜索的场景。
### 方法关键点
- 设计分层元评分准则：集级维度覆盖相关度（多维度信息覆盖）、简洁性（无冗余内容）、一致性（无事实冲突）；单文档维度覆盖来源权威性、时效性，每个查询基于元准则+强LLM生成的参考答案，生成带权重的查询专属评分准则
- 采用两阶段训练框架：第一阶段用强LLM基于查询专属准则选择最优文档集生成银标，对Qwen3-8B基座做SFT冷启动；第二阶段用GRPO算法做RL训练，基于分层准则加权计算奖励，推理阶段无需输入评分准则，直接输出最优文档子集
### 关键结果
- 深度研究场景：在4个基准数据集上平均得分60.1，较最强基线Rank4Gen高出2.6个点，Agent搜索调用次数最高降低17.1%
- RAG场景：在5个公开基准数据集上平均EM得分40.0，较Rank4Gen高出2个点
### 核心结论
面向下游生成任务优化的重排器，核心是对齐**文档集合整体质量**而非单文档相关度，用结构化评分准则做监督信号比纯端到端偏好对齐更可控、泛化性更强
