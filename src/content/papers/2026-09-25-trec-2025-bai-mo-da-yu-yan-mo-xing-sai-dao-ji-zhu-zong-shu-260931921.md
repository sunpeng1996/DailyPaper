---
title: Overview of the TREC 2025 Million Large Language Models track
title_zh: TREC 2025 百万大语言模型赛道技术综述
authors:
- Evangelos Kanoulas
- Panagiotis Eustratiadis
- Jamie Callan
- Mark Sanderson
- Yongkang Li
- Jingfen Qiao
- Gabrielle Poerwawinata
- Vaishali Pal
affiliations:
- University of Amsterdam
- Carnegie Mellon University
- RMIT
arxiv_id: '2609.31921'
url: https://arxiv.org/abs/2609.31921
pdf_url: https://arxiv.org/pdf/2609.31921
published: '2026-09-25'
collected: '2026-09-29'
category: Agent
direction: Agent 专业LLM专家检索评测
tags:
- LLM Retrieval
- Agentic AI
- Benchmark
- RAG
- Learning to Rank
one_liner: 发布首个大规模Agent生态下的专业LLM专家检索基准与评测数据集
practical_value: '- 多Agent/MoE路由场景可复用基于历史响应行为建模专家能力的思路，无需依赖静态专家描述，解决小样本下跨场景专家适配问题

  - 搭建垂直领域多专家池时，可采用共享基座+专属RAG知识库的低成本方案，配合基座知识泄漏过滤策略，快速构造电商多场景（服饰/3C/生鲜）专属Agent

  - 多专家排序优先落地无监督方案：基于细粒度响应级语义特征的BM25/向量检索方案，比小样本监督训练泛化性更好，工程落地成本更低

  - LLM垂直场景选型评测可复用论文的3级LLM-as-Judge打分模板，配合过滤基座可答对query的测试集构造方法，提升评测准确率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
面向未来百万级专业LLM组成的Agent协作生态，现有专家选择方案依赖静态模型元数据/描述，无法覆盖分散、异构的专业模型能力，缺乏大规模公开基准支撑相关技术研发。

### 方法关键点
- 重构IR任务范式：将检索目标从文档替换为LLM，给定用户query，仅基于模型历史可观测行为（生成响应、token级log概率）排序预期性能最优的专业模型，不依赖任何模型元数据
- 低成本模拟千级专业LLM：采用共享基座LLM+专属领域RAG知识库的方案，通过prompt强制检索依赖+query过滤（移除基座可直接答对的query）两种策略避免参数知识泄漏，保证专家领域特异性，最终构造1131个不同领域的模拟专家
- 公开基准数据集：包含1.4万+query的历史行为发现集、342条带3级能力标注的开发集、16条有效测试集，评测指标为nDCG@10、MRR

### 关键结果
共收集19支参赛队伍的提交方案：最优无监督方案（基于细粒度响应级特征+BM25检索）nDCG@10达0.174；基于小开发集监督训练的最优方案nDCG@10为0.152，泛化性弱于无监督行为建模方案。

### 核心结论
未来信息检索的核心目标将逐步从检索相关文档转向检索最适合回答用户query的专业LLM，基于历史行为证据的动态能力建模是该方向的核心落地路径
