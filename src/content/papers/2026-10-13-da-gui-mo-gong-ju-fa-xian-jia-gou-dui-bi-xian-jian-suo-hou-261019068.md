---
title: Plan or Retrieve First? A Scale Study of Tool Discovery Architectures
title_zh: 大规模工具发现架构对比：先检索后规划vs先规划后检索
authors:
- Mingfei Zhang
- Amit Surana
- Ziauddin Majid
- Chenxi Wang
- Michael Xu
affiliations:
- Apple
arxiv_id: '2610.19068'
url: https://arxiv.org/abs/2610.19068
pdf_url: https://arxiv.org/pdf/2610.19068
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: Agent工具检索架构优化
tags:
- LLM Agent
- Tool Retrieval
- Retrieve-then-Plan
- Plan-then-Retrieve
- Adaptive Routing
one_liner: 在4.7万API规模下对比两种工具发现架构的适用边界，提出复杂度自适应路由方案
practical_value: '- 工具检索模块可直接按query复杂度切换架构：单工具/含明确实体的简单query用RtP，多工具/语义模糊的复杂query用PtR，兼顾召回效果和推理成本

  - 可复用RtP的top-1检索相似度作为零成本路由信号，无需额外训练分类器即可实现架构动态切换，规避PtR额外的LLM调用latency和token开销，实测可降低36%的工具发现阶段成本

  - 电商导购/客服Agent的工具调用模块可直接套用该范式：比如用户明确要「查iPhone 15价格」用RtP直接匹配商品查询API，用户要「做618苹果全家桶选购攻略」用PtR先分解需求再检索对应的优惠券/比价/库存/配送API

  - PtR的Abstract Tool Stub生成无需训练，零样本prompt即可实现，上线成本极低，适合快速迭代的Agent业务场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工具增强LLM Agent需从大规模API库检索匹配工具，但有限上下文窗口无法加载全量API定义，主流Retrieve-then-Plan(RtP)范式假设用户query与API文档语义差距足够小，在复杂多工具场景下该假设频繁失效，此前无工业规模下的受控实验明确两种工具发现范式的适用边界。
### 方法关键点
- 控制变量实现两种架构：RtP直接对用户query做embedding，通过FAISS检索top-K工具返回规划器；Plan-then-Retrieve(PtR)先让LLM零样本生成Abstract Tool Stubs（假设的功能签名），用stub embedding检索，合并去重后返回规划器，两者共享embedding模型、向量索引、规划器。
- 提出Intent-Registry Coupling指标，衡量用户query表述与API文档命名的语义对齐度，作为解释范式效果差异的核心维度。
### 关键实验
- 数据集采用ToolBench的46984个唯一API，测试集分三类：单工具G1（n=200）、同品类多工具G2（n=200）、跨品类多工具G3（n=100），覆盖Gemini 2.5 Flash、gpt-oss-120b两个模型族，检索预算k=1~20，API库规模1k~47k。
- 核心结果呈现复杂度依赖的交叉效应：G1单工具场景RtP召回0.372，比PtR领先28.7%；G2多工具场景PtR召回0.188，比RtP领先31.5%；该效应在所有检索预算、API规模、模型族下均稳定成立。
- 成本层面PtR比RtP多75%~104%的token开销，采用复杂度自适应路由可降低36%的工具发现开销，无召回损失。
### 核心结论
工具检索架构没有通用最优解，简单高语义对齐query用RtP控成本，复杂低语义对齐query用PtR提效果，基于RtP top-1检索分数的零成本自适应路由是工业落地的最优选择
