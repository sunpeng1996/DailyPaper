---
title: Smart Content Ingestion for Generative AI Workloads
title_zh: 面向生成式AI工作负载的智能内容摄入系统
authors:
- Abbas Raza Ali
- Muhammad Ajmal Siddiqui
- Moona Zahid
affiliations:
- Citigroup Inc. London
- Ernst & Young LLP London
- NVIDIA Corporation London
arxiv_id: '2610.07091'
url: https://arxiv.org/abs/2610.07091
pdf_url: https://arxiv.org/pdf/2610.07091
published: '2026-10-05'
collected: '2026-10-07'
category: RAG
direction: RAG系统 · 多模态文档摄入Pipeline
tags:
- RAG
- Content Ingestion
- OCR
- Chunking
- Retrieval Evaluation
one_liner: 提出生产级可测量多模态文档摄入Pipeline，覆盖OCR路由、分块、全链路评测
practical_value: '- 电商/客服Agent知识库搭建可复用选择性OCR路由策略：仅将图片占比>80%的页面路由至OCR模型，其余走原生文本解析，可降低90%以上的内容提取模型成本

  - 搜索推荐RAG场景可直接复用确定性父子分块方案：子块≤512tok用于向量检索，父块≤3.5k tok用于生成上下文填充，附文档层级面包屑前缀，无需语义分块额外开销即可提升检索准确率

  - 迭代RAG链路时可复用只读检索评估方案：基于页面自动生成接地测试问题，复用生产embedding指纹做零标注检索效果评测，支持快速AB测试分块、embedding选型效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式AI与RAG系统依赖多模态异构企业数据（PDF、表格、扫描件等），内容提取阶段的错误是下游检索、推理环节无法修复的瓶颈，现有开源工具缺乏全链路可测量、可配置的生产级摄入能力，提取效果与算力成本难以平衡。

### 方法关键点
- 设计四阶段可溯源Pipeline：多模态内容提取→评测集构建与提取效果评估→结构感知父子分块→只读检索效果评测，各环节输出可量化指标，无黑箱
- 选择性OCR路由：按页面图片占比阈值（默认0.8）分流，仅少量图片主导页调用OCR/VLM，其余走原生结构化解析，大幅降低成本
- 稀缺优先多标签采样构建均衡评测集，融合CER（字符错误率）、WER（词错误率）、TEDS（表结构相似度）的复合评分体系，可量化提取精度
- 确定性父子分块：子块≤512tok用于向量检索，父块≤3.5k tok用于生成上下文填充，查询时上下文扩展为O(1)复杂度，添加文档层级面包屑前缀提升检索准确率
- 只读检索评估：基于页面自动生成接地问答，复用生产环境的embedding指纹计算hit@k、MRR，评测过程不修改生产索引

### 关键结果
在180份文档的Orion语料上测试，最优提取后端Gemini 3.1 Pro复合得分97.37，CER仅0.13%，表结构TEDS达0.995；分块策略在25050个合成问答上hit@1=68.6%，hit@10=92.8%，MRR=0.77，单查询平均延迟0.81s。

### 核心结论
内容提取是企业Agent系统的感知层，其错误无法被下游检索或重排序修复，全链路可测量的摄入能力是GenAI系统落地的核心前提。
