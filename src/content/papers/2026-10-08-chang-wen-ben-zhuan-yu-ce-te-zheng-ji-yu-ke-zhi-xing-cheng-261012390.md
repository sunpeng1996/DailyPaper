---
title: 'Long Text to Predictive Features: LLM-Guided Blockwise Feature Engineering
  via Executable Program Search'
title_zh: 长文本转预测特征：基于可执行程序搜索的LLM引导分块特征工程
authors:
- Ziming Dai
- Dabiao Ma
- Ziheng Guo
- Jack Dong
- Zimu Zhou
affiliations:
- City University of Hong Kong
- Qfin Holdings, Inc.
- Tianjin University
- Carnegie Mellon University
arxiv_id: '2610.12390'
url: https://arxiv.org/abs/2610.12390
pdf_url: https://arxiv.org/pdf/2610.12390
published: '2026-10-08'
collected: '2026-10-09'
category: LLM
direction: LLM工业落地 · 自动特征工程
tags:
- LLM
- Feature Engineering
- Program Synthesis
- Industrial Deployment
- Risk Control
one_liner: 离线用LLM搜索可执行长文本特征抽取程序，线上零LLM调用兼顾效果与推理效率
practical_value: '- 可直接复用「离线LLM生成可执行特征代码、线上零LLM调用」的架构，处理电商场景下用户评论、客服会话、商品详情等长文本的特征抽取需求，规避线上大模型调用的高延迟、高成本问题

  - 分块增量代码生成+深度校准信用回滚的搜索机制可落地到自动特征工程流程中，替代人工编写、迭代文本特征规则的模式，降低人力成本的同时挖掘更多隐性语义特征

  - 多搜索轨迹共享探索方向的设计可减少重复探索，在生成多组互补特征时可直接套用，大幅提升非结构化数据特征挖掘的效率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
工业场景（金融风控、电商推荐等）中大量高价值信息蕴藏在用户评论、客服对话、投诉记录等非结构化长文本中，人工特征工程效率低、维护成本高；现有基于LLM的文本特征抽取方案需要线上逐样本调用大模型，无法满足高并发、低延迟的部署要求。

### 方法关键点
- 仅在离线阶段调用LLM增量生成特征抽取代码块，每个新增块经过沙箱执行校验、贝叶斯参数调优、下游模型AUC增益校验后才会被冻结加入程序
- 设计深度校准的信用引导回滚机制，基于同深度历史搜索成功率判断当前节点是否值得继续扩展，避免贪心搜索陷入局部最优
- 采用多异步搜索轨迹共享探索方向的策略，减少重复探索，生成多组互补的特征程序

### 关键实验
在2个公开数据集+2个金融私有数据集上，相比最优基线AUC绝对提升0.0069~0.0358；已落地5个真实金融风控业务，上线后KS绝对提升0.02~1.56个百分点，线上推理延迟达毫秒级，无需GPU资源。

### 核心结论
工业场景下利用LLM处理非结构化数据时，将LLM的推理能力限制在离线阶段、线上仅执行固化的轻量化程序，是兼顾效果、成本、可解释性的高可行路径。
