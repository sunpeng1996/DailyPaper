---
title: Retrieval Augmented Generation Compositionality
title_zh: 检索增强生成（RAG）组合性研究与开源评估框架LASAGNA
authors:
- Ido Levy
- Segev Shlomov
- Leshem Choshen
affiliations:
- IBM
- Weizmann Institute of Science
arxiv_id: '2610.29722'
url: https://arxiv.org/abs/2610.29722
pdf_url: https://arxiv.org/pdf/2610.29722
published: '2026-10-20'
collected: '2026-10-22'
category: RAG
direction: 检索增强生成 · 端到端评估优化
tags:
- RAG
- evaluation_framework
- component_composition
- benchmarking
- corpus_scaling
one_liner: 提出开源RAG组合评估框架LASAGNA，验证组件增益不叠加、选型随指标与语料规模变化
practical_value: '- 落地RAG系统（电商商品问答、客服Agent、合规文案生成等）时，不要仅通过单组件孤立测试判断收益，必须将新组件嵌入现有完整pipeline验证，避免预期增益的大幅折损

  - 分指标做组件优化：若核心目标是检索准确性（如商品搜索、召回），优先优化embedding、索引富集、rerank模块；若核心目标是生成忠实度（如商品参数问答、合规内容生成），优先优化query
  augmentation、agentic校验模块

  - 按语料规模选型：25K以下小语料场景用轻量STANDARD配置即可，25K以上中大规模语料（如全站商品知识库）切换为BALANCED配置，可实现NDCG@10相对提升13.7%

  - 可直接复用LASAGNA框架测试自定义RAG组件（如商品领域专用reranker、结构化商品chunking规则），无需重写全链路代码，大幅降低实验成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有RAG技术均采用单组件孤立评估模式，无法确认多组件组合后增益是否保留，也不清楚检索质量、生成忠实度两类核心指标的选型差异，以及小语料下的实验结论能否迁移到大规模生产场景，缺乏统一的可控评估工具支撑端到端RAG选型。
### 方法关键点
- 开源LASAGNA框架，对RAG全链路8个核心阶段（chunking、embedding、索引富集、检索、query增强、rerank、上下文压缩、agentic校验）做接口抽象与实现隔离，替换单个组件不会影响其他环节逻辑
- 采用D-最优实验设计，累计测试450种RAG配置，覆盖8个公开benchmark，语料规模从5K到200K，同时评估NDCG@10（检索质量）、RAGAS忠实度（生成质量）、latency三类核心指标
### 关键结果
- 检索类增益组合折损严重：3种单独可带来+47% NDCG@10提升的组件，组合后实际仅实现+17%提升，增益折损63%；而忠实度类增益接近线性叠加，单独+28%的预期提升组合后实际实现+32%
- 两类指标选型无相关性：检索质量主要由embedding、索引富集、rerank决定，忠实度主要由query增强、agentic校验决定，两者Pearson相关系数仅-0.01，优化一类指标可能损害另一类
- 语料规模超过25K时配置排名翻转：200K语料下BALANCED配置比小语料最优的STANDARD配置NDCG@10相对提升13.7%
### 核心结论
新RAG技术必须在完整生产级pipeline、目标业务指标、实际语料规模下测试，孤立单组件的评估结论不具备落地参考价值
