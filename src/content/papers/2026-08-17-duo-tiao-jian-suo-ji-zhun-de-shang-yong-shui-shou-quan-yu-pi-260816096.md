---
title: 'The Commercial Tax: Rent-vs-Own Blind Spots in Multi-Hop Retrieval Benchmarks'
title_zh: 多跳检索基准的商用税：授权与成本披露盲点研究
authors:
- Luis M. Sanchez
- Kosrow Dehnad
affiliations:
- Toryx AI
- Columbia University
arxiv_id: '2608.16096'
url: https://arxiv.org/abs/2608.16096
pdf_url: https://arxiv.org/pdf/2608.16096
published: '2026-08-17'
collected: '2026-08-18'
category: RAG
direction: RAG多跳检索 授权与成本评估
tags:
- RAG
- Multi-Hop Retrieval
- Embedding Model
- Licensing
- Cost Evaluation
- Benchmark
one_liner: 审计多跳检索基准的嵌入模型授权与落地成本，证明商用可自部署嵌入已追平非商用SOTA
practical_value: '- 选型嵌入模型前必须核查训练数据对应的商用授权，避免将非商用SOTA（如NV-Embed-v2）直接用到生产，面临合规风险

  - 多跳检索场景选型嵌入不要迷信通用排行榜，必须在业务专属多跳数据集上实测，如BGE-M3通用排名高但在MuSiQue上表现倒数

  - 大语料RAG系统成本核心在索引构建（如图谱抽取）而非嵌入或query响应，1TB语料下索引成本是嵌入的7.5~900倍，架构选型优先优化索引环节ROI

  - 允许自部署的商用嵌入模型（如Nemotron-3-Embed-8B）已追平非商用SOTA，中小规模语料用自部署嵌入比API调用长期成本更低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前多跳RAG检索基准仅公开效果指标，完全遗漏企业落地两个核心决策因素：检索依赖的嵌入模型是否可商用、落地部署的实际成本，导致企业参考论文指标选型时踩合规和预算大坑。
### 方法关键点
- 审计4个主流多跳检索系统（HippoRAG-2、PropRAG、SAG、KET-RAG）的嵌入模型授权、成本披露情况
- 统一用MuSiQue多跳问答基准的1000条问题、11656条维基百科段落测试集，在相同测试框架下实测13款来自8家厂商的嵌入模型的Recall@5/10，附带bootstrap置信区间
- 构建标准化成本模型，拆分一次性嵌入/索引成本、 recurring query响应成本，线性外推到1TB企业级语料规模测算
### 关键结果
- 2026年7月前商用嵌入效果比非商用SOTA NV-Embed-v2低2.31个Recall@5点，存在明确「商用税」；NVIDIA新发布的可商用自部署Nemotron-3-Embed-8B效果与NV-Embed-v2无统计差异（Recall@5仅高0.24点，p=0.69），商用税已在前沿抹平
- 3款依赖NV-Embed-v2的SOTA多跳系统均未披露其非商用授权，5款审计系统中仅2款披露了索引成本
- 1TB语料下GraphRAG索引成本因配置差异可达11倍价差（42.8万~463.7万美元），是嵌入成本的7.5~900倍
### 最值得记住的一句话
论文指标不带授权和成本就是纸上谈兵，工业级RAG选型的优先级是合规>总持有成本>基准裸分。
