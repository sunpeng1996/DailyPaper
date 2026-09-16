---
title: Benchmarking Embedding Models for ESG Data
title_zh: ESG领域文本嵌入模型基准测试与14种模型性能对比
authors:
- Motaz Saad
- Veronica Cretì
- Ivan Gentile
- Kianna Kazemi
- Antonella Longo
affiliations:
- University of Salento
- IFAB Foundation
arxiv_id: '2609.15434'
url: https://arxiv.org/abs/2609.15434
pdf_url: https://arxiv.org/pdf/2609.15434
published: '2026-09-14'
collected: '2026-09-16'
category: Eval
direction: 垂直领域RAG 嵌入模型评测
tags:
- Embedding
- RAG
- Benchmark
- Information Retrieval
- ESG
one_liner: 构建专家校验的英意双语ESG基准数据集，测评14种开源闭源嵌入模型的检索与RAG性能
practical_value: '- 构建垂直领域（如电商合规、商品语义检索）RAG系统时，不要直接依赖通用MTEB榜单选嵌入模型，需基于自建领域评测集验证选型效果

  - 单语言垂直场景优先测试小参数开源嵌入模型，如Qwen3-embedding-0.6b在英文ESG场景性能接近4B大模型，可大幅降低部署成本、规避数据泄露风险

  - 工程优化上可采用PCA将嵌入维度降至16-32维，几乎不损失检索精度，同时能降低向量数据库存储开销、提升检索吞吐量，可直接复用至所有RAG系统

  - 快速构建垂直领域评测集时，可采用LLM生成query-doc-相关性三元组，再经领域专家小批量校验，效率远高于纯人工标注'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
通用嵌入模型基准（如MTEB）未覆盖ESG这类垂直领域的专业术语、语义特性，而ESG数据广泛应用于金融风控、合规报告、可持续性评估等场景，RAG系统的检索精度高度依赖嵌入模型的领域适配性，此前缺乏标准化ESG嵌入模型评测基准，无法指导实际场景的模型选型。
### 方法关键点
- 构建英意双语ESG评测数据集：采用GPT-4生成query-doc三元组，每个query对应高相关、中相关、不相关3个等级的文档，再经ESG领域专家逐份校验，最终得到624条高质量样本
- 覆盖14种主流嵌入模型，包含开源（Qwen3系列、bge-m3、nomic-embed等）与闭源（OpenAI embedding系列、Gemini embedding系列）两类
- 采用NDCG@K、Precision@K作为核心评价指标，同时验证PCA降维对检索精度的影响
### 关键实验结果
- 英文场景：开源qwen3-embedding-4b以NDCG 0.983排名第一，超过所有闭源模型；qwen3-embedding-0.6b以NDCG 0.978位列第二，性能接近4B大模型
- 意大利语场景：闭源text-embedding-3-large以NDCG 0.975领先，开源模型中qwen3-embedding-0.6b以0.972保持强竞争力
- 90%以上的模型经PCA降维到16维时，NDCG无明显下降甚至略有提升，验证了低维嵌入的工业可用性
### 核心结论
垂直领域RAG系统的嵌入模型选型不能依赖通用基准排名，小参数开源模型在单语言垂直场景往往能取得超过闭源大模型的极高性价比
