---
title: 'CMT-RAG: Complementary Memory Traces for Multi-turn Multi-hop RAG'
title_zh: CMT-RAG：面向多轮多跳RAG的互补记忆迹框架
authors:
- Lang Zhou
- Yingjian Chen
- Shuxuan Li
- Kun-Yu Lin
- Zhilin Zhao
affiliations:
- Sun Yat-sen University
- Shenzhen Loop Area Institude
- The University of Hong Kong
arxiv_id: '2607.26470'
url: https://arxiv.org/abs/2607.26470
pdf_url: https://arxiv.org/pdf/2607.26470
published: '2026-07-29'
collected: '2026-07-30'
category: RAG
direction: 多轮多跳RAG · 结构化会话记忆
tags:
- RAG
- Conversational Memory
- Multi-hop Reasoning
- State Space Model
- Benchmark
one_liner: 提出子问题级互补记忆DAG+SSM生成器的多轮多跳RAG框架，配套标注跨轮依赖的MuMu-QA基准
practical_value: '- 电商智能客服、导购类多轮Agent可借鉴子问题级DAG记忆设计，将每轮查询拆解结果、检索到的商品/政策证据、跨轮依赖结构化存储，减少大模型上下文占用，避免重复检索，提升跨轮推理准确率

  - 复杂多跳查询检索场景（如用户带历史消费上下文的商品搜索）可复用SSM+LoRA+DPO的查询拆解范式，轻量SSM做查询分解和上下文承接，比同参数Transformer方案延迟降低近50%，性能更优

  - 自研多轮RAG评测基准可参考MuMu-QA的合成思路，通过子问题重定位、推理链拼接低成本生成带跨轮依赖标注的多轮对话数据集，降低人工标注成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多轮RAG普遍采用原始对话历史、改写查询或非结构化摘要作为记忆，丢失了中间推理步骤和跨轮依赖关系，多跳查询时难以复用之前的检索证据和推理结果，要么重复检索浪费资源，要么上下文过长导致「lost-in-the-middle」效应，回答准确率不足。

### 方法关键点
- 双路互补内存设计：轻量Mamba-2 SSM作为运行时内存承接近轮对话上下文，会话级DAG作为持久化内存存储结构化记忆迹，每个节点包含子问题、检索关键词、跨轮依赖、检索段落ID、子答案
- 结构化迹生成：通过LoRA+DPO微调SSM生成器，每轮将当前查询拆解为面向检索的子问题草稿，自动关联历史迹依赖
- 无状态阅读器设计：阅读器无需感知全量对话历史，仅基于当前子问题和组装好的历史+新鲜证据回答，降低上下文依赖
- 配套MuMu-QA基准：通过子问题重定位、推理链拼接合成带跨轮子问题依赖标注的多轮多跳对话，覆盖短/长/超长对话场景

### 关键实验
在MuMu-QA长对话拆分上对比5类共15种RAG基线，用Qwen3-32B做阅读器时，CMT-RAG仅用top5检索就达到41.73 EM、55.63 F1，比直接多轮RAG高6.07 EM、6.82 F1，上下文段落数从20降到14；用Llama-3.3-70B时达到44.70 EM、57.55 F1；SSM生成器比同参数量Transformer生成器延迟降低48.4%，在RECOR、HotpotQA等公开基准上也取得SOTA或可比性能。

**最值得记住的一句话：将会话记忆与检索逻辑对齐，用子问题级的结构化记忆单元作为检索和记忆的统一载体，是提升多轮多跳RAG性能和效率的核心路径**
