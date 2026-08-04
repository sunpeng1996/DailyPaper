---
title: 'Deep Agentic Search for Repository-Level Code Question Answering: An Empirical
  Study'
title_zh: 仓库级代码问答的语义搜索与深度智能搜索实证对比研究
authors:
- Amirkia Rafiei Oskooei
- Bora Ilci
- Alperen Kayim
- Mehmet Egemen Uzun
- Berat Can
- Kaan Emre Kara
- Ozan Orhan
- Mehmet S. Aktas
affiliations:
- Yildiz Technical University
- Intellica Business Intelligence
arxiv_id: '2608.01507'
url: https://arxiv.org/abs/2608.01507
pdf_url: https://arxiv.org/pdf/2608.01507
published: '2026-08-02'
collected: '2026-08-04'
category: Agent
direction: 代码Agent 检索与子代理探索范式对比
tags:
- Code Agent
- Agentic Search
- Semantic Search
- RAG
- Code QA
one_liner: 实证对比代码仓库级QA的两种主流搜索范式，明确语义搜索准确率更高、成本远低于深度智能搜索
practical_value: '- 分层Agent架构需新增交接校验逻辑：本文41.8%的深度Agent失败来自主副Agent的无报错隐性交接错误，电商智能导购、售后等分层Agent业务可要求子代理返回结构化结果，主代理增加二次校验环节降低错误率

  - 静态可索引只读场景优先选RAG方案：对于商品库、商家规则、活动说明等可提前建索引的查询场景，RAG准确率比分层Agent高近20个百分点，单正确回答成本仅为后者的1/2~1/24，ROI优势显著

  - Agent架构选型需做实证验证：不要盲目相信「分层Agent可避免上下文污染效果更优」的直觉结论，新架构上线前必须做小流量AB测，量化效果与成本收益

  - 设置工具调用上限降低无效成本：两种范式下工具调用次数超过阈值后准确率均随调用量上升而下降，业务侧需设置工具调用最大次数、超时终止逻辑，避免无效token消耗'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前代码Agent处理仓库级QA的主流方案分为两类：一是基于预建向量索引的语义搜索RAG方案，二是分层深度智能搜索方案（主计划器委托独立上下文的子代理做资源探索，仅返回浓缩结果避免上下文污染），后者已被Claude Code等主流产品采用，但一直缺乏量化的效果、成本对比，选型完全依赖行业直觉，亟需实证数据支撑。

### 方法关键点
- 对比两组架构：① 基于ReAct的语义搜索Agent，仅开放仓库结构查询、向量检索、文件读取三类工具；② 基于LangChain Deep Agent的分层深度搜索Agent，主代理负责规划，子代理在独立上下文执行shell类探索指令，仅返回浓缩结果给主代理
- 实验对齐控制：4款大模型（Gemini 2.5 Flash/Pro、Gemini 3 Flash、Qwen3-235B）在两组架构中复用，采用第三方Claude Sonnet 4.6作为裁判，严格对齐SWE-QA基准的评分规则
- 失败根因分析：对所有失败案例按「错误机制-答案症状」双维度标注，定位两种方案的核心缺陷

### 关键实验结果
- 数据集：SWE-QA基准，覆盖15个不同规模Python仓库共720条问题
- 准确率：语义搜索整体Pass率65.2%，深度智能搜索仅46.2%，该优势在4款模型、所有问题类型、14/15的测试仓库上一致成立
- 成本：语义搜索单正确回答的平均成本仅为深度智能搜索的43%，在Qwen3-235B场景下成本差可达24倍
- 失败根因：41.8%的深度智能搜索失败来自主副Agent的交接错误，且多为无报错的自信错误答案，隐蔽性极强

最值得记住的结论：静态可索引的只读查询场景下，基于RAG的语义搜索在效果、成本上全面优于分层子代理探索的深度智能搜索，盲目引入分层架构避免上下文污染反而会引入更难排查的隐性错误。
