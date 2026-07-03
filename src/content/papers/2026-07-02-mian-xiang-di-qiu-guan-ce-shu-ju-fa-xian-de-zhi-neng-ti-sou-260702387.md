---
title: Bringing Agentic Search to Earth Observation Data Discovery
title_zh: 面向地球观测数据发现的智能体搜索系统
authors:
- Minghan Yu
- Youran Sun
- Chugang Yi
- Yixin Wen
- Haizhao Yang
affiliations:
- University of Maryland, College Park
- University of Florida
arxiv_id: '2607.02387'
url: https://arxiv.org/abs/2607.02387
pdf_url: https://arxiv.org/pdf/2607.02387
published: '2026-07-02'
collected: '2026-07-03'
category: Agent
direction: 智能体搜索 · 检索重排优化
tags:
- Agentic Search
- Hybrid Retrieval
- Reranking
- Benchmark
- Knowledge Graph
one_liner: 构建地学领域47k查询-数据集检索基准，提出混合检索+智能体重排的高性能搜索pipeline
practical_value: '- 混合检索的权重计算方法可复用：不需要调参，直接用两个检索器在训练集的性能占比作为融合系数，大幅降低超参数调优成本，适合多模召回融合场景

  - 轻量语义得分校正方案（NN-SSC）性价比极高：仅训练460K参数的MLP头，不需要微调整个大编码器，就能获得比全量微调编码器更好的检索效果，适合资源有限的检索迭代场景

  - 智能体重排的落地思路可参考：仅对top-K候选做带工具调用的智能体重排，既控制成本，又能补全候选元数据外的外部知识，适合电商/广告场景下的精排阶段做补充优化'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
地学领域NASA等机构拥有海量观测数据集和工具，但元数据分散、入口不统一，即便是领域专家也很难快速定位匹配研究需求的数据集；通用LLM和预训练嵌入缺乏地学领域知识，直接用于检索效果差，RAG方案又受上下文窗口限制，重排质量是检索pipeline的核心瓶颈，同时领域内缺乏大规模公开基准支持算法的量化对比。

### 方法关键点
- 基准构建：基于NASA地球观测知识图谱的论文-数据集引用关系，生成21k条真实科研查询，构建47k+查询-数据集对的NASA-EO-Bench基准，支持监督训练
- 三阶段检索pipeline：1）路由层优先调用NASA官方工具，可直接回答的查询提前终止；2）混合检索层：将BM25 lexical得分与微调后的语义得分（两种方案：全量微调编码器、冻结编码器仅训练460K参数的NN-SSC MLP语义校正头）做线性融合，融合系数由两个检索器的训练集性能占比自动计算，无需额外调参；3）重排层：对比单轮LLM重排和带web/arXiv工具调用的智能体重排，仅对top-10候选做重排控制推理成本

### 关键结果
- NN-SSC+BM25混合检索方案比原生余弦基线的Recall@10和MRR提升超5倍
- 在200条分层测试子集上，同模型下智能体重排比单轮LLM重排的MRR最高提升28%，所有LLM零样本重排都能稳定提升MAP和MRR

### 核心结论
当召回效果达到瓶颈时，仅对top-K候选做带工具调用的轻量智能体重排，是兼顾成本和效果的可行优化路径。
