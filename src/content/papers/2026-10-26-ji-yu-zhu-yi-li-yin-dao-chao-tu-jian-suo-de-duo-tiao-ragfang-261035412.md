---
title: 'Read the Route: Attention-Steered Hypergraph Retrieval for Multi-hop RAG'
title_zh: 基于注意力引导超图检索的多跳RAG方法HyperAddress
authors:
- Jiate Liu
- Liuyi Chen
- Xiaofei Yuan
- Yifu Tang
- Zihan Yang
- Xu Zhou
- Zhengyi Yang
affiliations:
- The University of New South Wales
- Hunan University
- Euler AI
- Vecton AI
- The University of Sydney
arxiv_id: '2610.35412'
url: https://arxiv.org/abs/2610.35412
pdf_url: https://arxiv.org/pdf/2610.35412
published: '2026-10-26'
collected: '2026-10-27'
category: RAG
direction: 多跳RAG · 超图检索与注意力引导
tags:
- Multi-hop-RAG
- GraphRAG
- Hypergraph-Retrieval
- Attention-Head
- Personalized-PageRank
one_liner: 利用LLM稀疏寻址注意力头引导超图游走，无生成实现高性能低成本多跳RAG检索
practical_value: '- 电商多意图query检索、Agent工具调用链匹配等多轮场景可复用「注意力头打分+超图PPR」框架，替代逐跳LLM生成推理，检索速度提升2倍以上，大幅降低推理成本

  - 可针对业务场景从LLM中筛选特定功能的稀疏注意力头，仅运行头所在层前向传播即可获取语义信号，无需全量LLM推理，适合低延迟检索场景

  - 电商商品/内容知识图谱构建可参考「描述标注超图」结构：将item/内容作为节点、实体作为超边，离线标注实体在内容中的指代描述，多跳关联召回率提升显著

  - 业务多跳检索效果随跳数下降的问题，可通过「注意力逐词打分+动态调整PPR重启分布与转移权重」的思路优化，跳数越高增益越明显'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多跳RAG两类方案均存在短板：扩散/相似性类检索沿固定边权重扩展，无法识别query隐含实体指代，误差随跳数持续累积；探索类方案需逐跳调用LLM生成子问题或推理路径，推理成本高、延迟大，难以落地高并发业务场景。

### 方法关键点
- 离线构建描述标注超图：以段落为顶点、实体为超边，标注每个段落中实体的指代描述，无需预定义三元组，支持增量更新
- 无监督筛选LLM稀疏寻址头：仅运行中低层前向传播，无需生成token即可获取query对上下文实体的指代打分，单次前向可覆盖多跳隐含关联
- 注意力引导Personalized PageRank检索：用寻址头的实体得分动态调整随机游走的重启分布与转移权重，2轮迭代即可完成多跳检索

### 关键结果
在MuSiQue、2WikiMultiHopQA、HotpotQA三个多跳QA基准上对比9个SOTA基线：
- 平均Recall@5比最强基线PropRAG高3.5个百分点，All@5高7.4个百分点，4跳场景下增益达6.3个百分点
- 检索速度是PropRAG的2倍以上，索引构建成本仅为同类GraphRAG方法的一半，query阶段无任何token生成开销
- 用1.7B小模型即可超过27B模型驱动的IRCoT基线效果，成本优势显著

### 核心结论
LLM的注意力头已经蕴含了多跳指代识别能力，无需生成token即可引导结构检索，效果和成本均优于逐跳生成推理方案
