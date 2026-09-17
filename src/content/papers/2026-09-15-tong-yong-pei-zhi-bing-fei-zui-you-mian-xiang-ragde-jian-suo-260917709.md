---
title: One Size Does Not Fit All! Dynamic Retriever and Generator Selection for RAG
title_zh: 通用配置并非最优：面向RAG的检索器与生成器动态选择框架
authors:
- Neeraj Anand
- Payel Santra
- Partha Basuchowdhuri
- Debasis Ganguly
- Sumit Bhatia
affiliations:
- Adobe Systems
- IACS Kolkata
- University of Glasgow
arxiv_id: '2609.17709'
url: https://arxiv.org/abs/2609.17709
pdf_url: https://arxiv.org/pdf/2609.17709
published: '2026-09-15'
collected: '2026-09-17'
category: RAG
direction: 自适应RAG · 检索生成配置动态路由
tags:
- RAG
- DynamicRouting
- QPP
- EfficiencyOptimization
- SFT
one_liner: 提出两种RAG检索生成配置动态选择方案，优化效果效率trade-off无需固定配置
practical_value: '- 电商商品/客服问答类RAG系统可直接复用框架分层思路：简单事实类query走BM25+轻量化生成器，复杂多跳需求走重排序检索+大模型推理，可降低推理成本40%以上

  - 无标注数据场景优先用DRAGQPP方案：用Avg-IDF做检索难度预判、检索上下文perplexity做生成难度预判，零训练成本即可达到与静态高配RAG相当的效果

  - 有标注数据场景可上线DRAGSFT：用小参数LLM微调做路由决策，相比静态最高配RAG可实现效果提升2~12%的同时延迟降低40%~50%'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG系统全量query采用固定的检索器+生成器配置，未考虑不同query的复杂度差异，简单query浪费大量算力，复杂query效果不达预期；此前的自适应RAG研究仅单独优化检索或生成模块，未探索两者联合选择的最优trade-off，算力浪费和效果天花板问题突出。

### 方法关键点
- **DRAGQPP（训练免路由）**：两步决策，第一步基于query的Avg-IDF预检索QPP分数预判检索难度，从4档检索器（BM25→E5→E5+BGE重排→query拆分+重排）选择最低算力可满足需求的配置；第二步基于检索到的上下文的perplexity预判生成难度，从低/中/高三档生成推理档位中选择适配配置
- **DRAGSFT（监督路由）**：将检索生成对选择转化为多分类任务，微调小参数LLM直接输出最优配置对，避免阈值校准成本，路由决策开销极低

### 关键实验
在TriviaQA、HotpotQA、MuSiQue、OOD数据集FRAMES上验证，对比静态最高配RAG基线：DRAGQPP效果持平的前提下推理延迟降低47%~59%；DRAGSFT效果提升2~12%的同时延迟降低40%~50%，OOD场景下仍保持性能优势。

### 核心结论
RAG系统中检索质量提升带来的效果增益远高于单独提升生成模型推理复杂度，推理能力无法弥补检索质量不足的短板
