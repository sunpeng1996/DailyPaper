---
title: 'VisDocAgentBench: Benchmarking Agents for Visually Rich Document Retrieval'
title_zh: VisDocAgentBench：富视觉文档智能检索Agent基准测试集
authors:
- Lexiang Hu
- Yanzhao Zhang
- Mingxin Li
- Dingkun Long
- Yikang Li
- Fuwei Zhang
- Yisen Wang
- Zhouchen Lin
affiliations:
- Peking University
- Alibaba Group
arxiv_id: '2608.17889'
url: https://arxiv.org/abs/2608.17889
pdf_url: https://arxiv.org/pdf/2608.17889
published: '2026-08-18'
collected: '2026-08-19'
category: Eval
direction: Agent多模态检索 · 基准评估
tags:
- Agentic Search
- Multimodal Retrieval
- Document Retrieval
- Benchmark
- Vision-Language
one_liner: 构建统一评估静态与Agent范式的富视觉文档检索基准 量化多跳检索能力瓶颈
practical_value: '- 做电商多模态商品/详情页多跳检索场景（如找符合「特定材质+活动规则+资质认证」跨页描述的商品）时，可参考论文的证据路径分级构造方法，设计分层难度测试集，量化现有检索系统的能力边界

  - 构建多模态Agent检索系统时，优先采用「视觉检索+按需OCR提取」架构，比纯OCR索引的R@1至少提升12.5个百分点；同时将迭代搜索、页面直接检查作为核心工具能力，这两个模块带来的性能增益最大

  - 设计多跳检索的Agent规划策略时，可参考论文错误归因：80%+的错误来自目标发现和候选检查环节，可针对性优化证据链跟踪、跨页语义对齐的prompt设计

  - 搭建业务相关的检索基准时，可复用其关系保留的构造Pipeline：先提取角色化描述符+跨页对齐，再做AI+人工双审+难负例验证，能大幅提升基准的区分度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有富视觉文档检索基准多聚焦单跳query-页面匹配，Agent类搜索基准多评估下游问答、报告生成等任务，缺乏对迭代证据积累下的文档排序能力的统一评估框架，无法量化静态检索到Agent检索的能力差异与核心瓶颈，也无法指导多模态检索Agent的架构优化。

### 方法关键点
- 构建闭合语料：覆盖10个主题的100篇学术论文共2375个页面，设计3级证据结构：直接匹配（L1）、单语义桥（L2）、双语义桥（L3），平衡语义、关系、视觉三类查询条件
- 关系保留的构造流程：先用VLM提取查询锚点、语义桥、视觉目标三类角色化描述符，生成跨页语义对齐的证据路径，再经AI+人工双审、难负例验证，最终得到120条唯一目标的查询
- 统一评估契约：静态检索、Agent检索都要求返回top10排序结果，采用Recall@k、MRR@10作为统一指标，消除范式差异带来的评估偏差

### 关键实验结果
对比7类静态检索基线、9款不同规划器的Agent检索：
1. 最强静态视觉检索器Nemotron ColEmbed在L1单跳场景R@1达97.5%，但在L3多跳场景仅2.5%，单跳匹配完全无法应对跨页证据需求
2. Agent检索大幅弥补多跳缺陷，Claude Opus 5搭配视觉检索的整体R@1达67.5%，比纯OCR索引的同规划器Agent高30个百分点
3. 消融实验显示，移除迭代搜索使R@1下降8.34个百分点，移除页面直接检查使R@1下降15.84个百分点，是Agent检索的核心增益来源

### 核心结论
多模态Agent检索的核心收益来自模态保留的全局发现+证据导向的迭代验证，工具本身无法带来增益，规划器对证据链的整合能力才是性能瓶颈
