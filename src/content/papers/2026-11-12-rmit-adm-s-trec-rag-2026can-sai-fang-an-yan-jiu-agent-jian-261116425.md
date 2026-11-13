---
title: 'RMIT-ADM+S at TREC RAG 2026: Research Agents, Retriever Ablations, and Open-Weight
  Replication'
title_zh: RMIT-ADM+S TREC RAG 2026参赛方案：研究Agent、检索消融与开源复现
authors:
- Oleg Zendel
- Kun Ran
- Chenglong Ma
- Nguyen Khoi Vo
- Shuai Wang
affiliations:
- RMIT University
- The University of Queensland
- keenable.ai
arxiv_id: '2611.16425'
url: https://arxiv.org/abs/2611.16425
pdf_url: https://arxiv.org/pdf/2611.16425
published: '2026-11-12'
collected: '2026-11-13'
category: Agent
direction: Agentic RAG 架构优化与效果评估
tags:
- Agentic-RAG
- Retrieval-Ablation
- Open-Weight-LLM
- RAG-Evaluation
- TREC-RAG
one_liner: 对比7种不同配置的研究Agent系统，验证开源模型在RAG场景的性价比潜力
practical_value: '- 检索优化可复用混合RRF检索+相邻块扩展组合，相比纯语义+关键词检索减少14.4%搜索次数、8.2%token消耗，成本降低8.5%，适合电商咨询、导购类Agent降本

  - 系统选型优先测试Writer模型对效果的影响，成本敏感场景可选择中大型开源模型，本实验中GLM-5方案成本仅为闭源最优方案的18.6%，在真人偏好评估中胜率达76.5%

  - 评估体系避免单一依赖自动化覆盖率指标，需结合业务场景增加用户感知维度（如可读性、信息密度）的评估，避免指标好看但用户体验差的问题

  - 垂类检索冷启动可复用Agent交互轨迹训练检索模型，以Agent主动留存的chunk为正样本、未选择为负样本微调，无需人工标注即可提升nDCG@10约4.2个百分点'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Agentic RAG系统的架构、检索、模型选择缺乏系统性的性价比对比，闭源方案成本高企，开源模型的效果天花板尚未明确，且自动化评估指标与用户真实偏好的对齐度问题长期被忽略，TREC RAG 2026的标准化评测场景为验证不同方案的效果、成本、鲁棒性提供了公开基准。

### 方法关键点
- 设计7种异构研究Agent，覆盖闭源（GPT-5.6系列）、开源（GLM-5、Qwen3等）两类基座，对比单轮/多轮编排、混合/语义/关键词检索、相邻块扩展、预需求规划、草稿复审等14类设计选择的差异
- 检索层优化：用无权重RRF融合语义+关键词检索结果，基于Agent交互过程中主动commit的chunk作为正样本、未选择chunk作为负样本，微调256维轻量嵌入模型，降低检索成本
- 多维度评估：结合预提交阶段自动化RAGDoll评分、官方NIST覆盖率评估、真人侧写偏好三种方式，系统性对齐不同评估方法的结果差异

### 关键结果数字
- 6/7参赛方案超过赛道中位数，最优闭源方案brief-hybrid的Batch1 vital coverage达0.892，追平赛道最高水平
- 开源全链路方案owa-glm5成本仅为闭源最优方案的18.6%（$0.524/topic vs $2.823/topic），在Batch1真人侧写中显著优于闭源方案，胜率达76.5%
- 混合RRF检索相比纯语义+关键词检索减少14.4%搜索次数、8.2%token消耗，整体成本降低8.5%

### 核心结论
不存在通用最优的Agentic RAG架构，方案选型需结合业务的效果要求、成本约束、用户偏好维度综合权衡，评估方法必须匹配业务实际使用场景，不能单一依赖自动化指标。
