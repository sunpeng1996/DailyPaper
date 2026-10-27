---
title: 'Agent Memory as Recommendation: Recommender-System Design for Long-Term Memory
  of LLM Agents'
title_zh: 基于推荐系统范式的LLM Agent长时记忆选择框架设计
authors:
- Xinyu Zhang
- Weiwei Sun
affiliations:
- Fudan University
arxiv_id: '2610.34673'
url: https://arxiv.org/abs/2610.34673
pdf_url: https://arxiv.org/pdf/2610.34673
published: '2026-10-26'
collected: '2026-10-27'
category: Agent
direction: Agent长时记忆 · 推荐系统范式迁移
tags:
- LLM Agent
- Long-term Memory
- Slate Recommendation
- Cascade Ranking
- Cost Efficiency
one_liner: 将Agent记忆选择形式化为带预算Slate推荐，提出零LLM调用的AgentMemRec框架，性能超主流方案
practical_value: '- 可以直接复用「BM25+稠密向量RRF召回+轻量LambdaRank排序+预算贪婪填充」的零LLM调用记忆选择pipeline，适配电商客服Agent、个性化导购Agent的长时记忆场景，大幅降低推理成本

  - 记忆选择、RAG上下文选择场景可直接借鉴「池化完备性+排序完备性」的两阶段拆分优化目标，先扩召回池保证证据不丢，再优化排序提升上下文命中率，比盲目堆LLM调用性价比高

  - 电商推荐的slate推荐、级联排序技术可直接迁移到Agent记忆、RAG场景，现有推荐算法栈无需大改就能复用'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM Agent要支持多会话长时交互，每次请求都需要从海量历史记忆中筛选少量片段放入有限上下文窗口，现有方案要么依赖大量LLM调用构建记忆结构成本极高，要么容易遗漏跨会话证据导致回答错误，而该问题的大规模、低延迟要求、整组效果评估的特性和推荐系统高度匹配。
### 方法关键点
- 将记忆选择形式化为带token预算的slate推荐问题：请求对应用户，历史记忆对应item，上下文窗口对应推荐slate，整体架构复用推荐系统级联范式，拆分为记忆构建、召回、排序、上下文组装4个阶段
- 提出AgentMemRec零LLM调用方案：召回层用BM25+bge-m3稠密向量双路召回，RRF融合后取top128候选池；排序层用10维低成本特征（相似度、时序、长度等）训练LightGBM LambdaRank排序模型；上下文层按排序顺序贪婪填充token预算，无需动态截断
- 核心优化目标为最大化池化完备性（召回池包含所有证据的概率）和排序完备性（排序后预算内包含所有证据的概率）的乘积
### 关键实验
在LongMemEval-S（50会话历史）、LongMemEval-M（500会话历史）、LoCoMo三个会话基准上测试，对比A-Mem、HippoRAG 2、DynamicRAG、Mem0、Zep等主流记忆方案，以及调用64次LLM的reranker：AgentMemRec在LongMemEval-S/M上准确率比主流记忆方案高10~33个百分点，和64次LLM调用的reranker效果持平，推理成本低3.2倍；在LoCoMo上效果优于Mem0、Zep，和SOTA的T-Mem持平。
> 最值得记住的一句话：LLM Agent的长时记忆选择本质是带约束的slate推荐问题，成熟的推荐系统技术栈比盲目堆叠LLM调用的方案性价比高得多。
