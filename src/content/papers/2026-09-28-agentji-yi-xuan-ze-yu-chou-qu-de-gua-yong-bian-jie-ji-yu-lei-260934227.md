---
title: When Does Selection Replace Extraction? A Pre-Registered Test of Agent Memory
  with a Typed Decision Model
title_zh: Agent记忆选择与抽取的适用边界：基于类型决策模型的预注册测试
authors:
- Rishabh Sharma
- Rishika Lall
affiliations:
- Independent Researcher
arxiv_id: '2609.34227'
url: https://arxiv.org/abs/2609.34227
pdf_url: https://arxiv.org/pdf/2609.34227
published: '2026-09-28'
collected: '2026-09-29'
category: Agent
direction: Agent 长对话记忆方案优化
tags:
- AgentMemory
- Reranking
- LLM
- NonInferiorityTest
- LongConversation
one_liner: 紧预算下Agent记忆原始轮次选择效果不逊于抽取方案 成本低3061倍
practical_value: '- 客服/导购等成本敏感的实时Agent场景，紧上下文预算下可直接放弃写时事实抽取，仅用原始对话轮次加轻量reranker，成本下降3个数量级，效果损失在5个点以内

  - Rerank的增益与上下文窗口能容纳的检索结果数强负相关：仅能放3条结果时rerank最高提效17.4个点，能放20条时增益仅1-1.5个点，可根据预算决定是否加rerank模块

  - 类型决策模型做reranker效果与gpt-4o-mini列表reranker相当，延迟仅1/3，适合对响应速度要求高的直播导购、实时咨询等场景

  - 开放域、时序类记忆查询需求，或上下文预算充足时，仍优先选择事实抽取式记忆方案，准确率更高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agent长对话记忆方案分为两派，结论互相矛盾：抽取派认为写时提炼事实能显著提升效果，选择派认为原始对话轮次加良好排序效果相当，且两方对rerank的价值也未达成共识，缺乏明确的适用边界指导工程落地。
### 方法关键点
- 采用预注册非劣效测试，设定5个点的非劣效阈值，所有对比严格匹配上下文token数，排除token不公平的干扰
- 核心对比方案：原始轮次+Jev类型决策模型单调用rerank（Turns+Jev） vs 写时LLM事实抽取方案engram v2，同时对照余弦检索、LLM reranker、Jev-Mem等主流方案
- 设计多梯度预算测试，分别验证保留3/6/20条检索结果时各方案的效果差异
### 关键结果
- 数据集：LoCoMo（778个标注问题）、LongMemEval（470个标注问题）
- 紧预算（匹配265token上下文）下，Turns+Jev效果非劣于engram v2，单侧95%下限-3.0，高于-5的阈值，写成本低3061倍
- Rerank增益随预算提升快速衰减：仅保留3条结果时，LoCoMo上增益17.4个点，LongMemEval上增益9.1个点；保留20条结果时，增益分别降至1.5和1.1个点
- Jev reranker效果与gpt-4o-mini列表式reranker相当，延迟仅为后者的1/3
### 最值得记住的一句话
Agent记忆方案的选择完全由上下文预算决定：紧预算下原始轮次+轻量rerank性价比拉满，松预算下抽取式记忆准确率更高
