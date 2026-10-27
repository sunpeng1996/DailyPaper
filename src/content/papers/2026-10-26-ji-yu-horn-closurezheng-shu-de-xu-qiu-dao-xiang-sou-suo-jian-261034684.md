---
title: 'Knowing When the Evidence Is Enough: Requirement-Directed Search with Horn-Closure
  Certificates'
title_zh: 基于Horn Closure证书的需求导向搜索：检索证据充足性判断
authors:
- Xinyu Zhang
- Weiwei Sun
affiliations:
- Fudan University
arxiv_id: '2610.34684'
url: https://arxiv.org/abs/2610.34684
pdf_url: https://arxiv.org/pdf/2610.34684
published: '2026-10-26'
collected: '2026-10-27'
category: RAG
direction: RAG 证据充足性判断与检索优化
tags:
- RAG
- Horn Closure
- Search Agent
- Evidence Sufficiency
- Hypergraph
one_liner: 提出基于查询需求超图与Horn Closure的证据充足性判断框架，无需额外模型调用即可完成检索决策
practical_value: '- 多跳检索/复杂query回答场景可复用需求超图+Horn Closure的轻量决策逻辑，无需额外大模型调用就能判断证据是否充足，大幅降低推理成本

  - 检索链接加实体锚定校验（匹配query实体和检索文档标题）的trick可直接复用，在21M维基语料上能提升决策准确率4~13个点，有效降低同名实体/相似文档的误召回

  - 电商商品导购/复杂售前咨询Agent可借鉴该框架，拆解用户需求为依赖子任务，自动判断是否需要进一步召回商品参数/售后规则等信息，还能明确告知用户缺失的信息点，提升交互体验'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有搜索增强系统/RAG的证据充足性判断依赖大模型整体评估，容易遗漏多跳问题的必要合取子条件，要么过早回答产生幻觉，要么过度检索浪费时延，还无法明确告知用户缺失的信息点。

### 方法关键点
- 提出Certify框架，先将查询拆解为带依赖关系的需求超图，每个超边定义一组事实共同推导出另一个事实的规则
- 按拓扑序逐需求检索，每个检索结果需经实体锚定校验（匹配需求实体与文档标题，未通过则触发二次校验），只有校验通过的结果才会被纳入事实池
- 基于Horn Closure规则计算事实池是否能推导出查询目标，无需额外模型调用：能推导则输出最小推导上下文，否则返回缺失的开放需求用于下一轮检索

### 关键实验结果
在2WikiMultiHopQA、MuSiQue、HotpotQA三个多跳QA数据集（带人工构造的缺失关键证据的孪生query）上测试，对比搜索Agent、图检索、传统充足性判断等11个基线：
- Certify输出的上下文回答准确率达80.0%，远高于全量检索上下文的56.7%
- 决策准确率比基线S2G-RAG高11.4个百分点，和Gemini-2.5-Flash的充足性标注效果相当
- 21M维基大规模语料下，实体锚定校验能提升决策准确率4~13个点

### 最值得记住的一句话
对复杂多跳需求的证据充足性判断，结构化的依赖规则+轻量符号推理的效果完全可以媲美大模型整体评估，同时成本更低、可解释性更强
