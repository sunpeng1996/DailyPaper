---
title: 'DeepWeaver: Bridging the Evidence Synthesis Gap in Open-Ended Question Answering'
title_zh: DeepWeaver：弥合开放式问答中证据合成鸿沟的框架
authors:
- Xujia Wang
- Yizhe Zhang
- Bin Xu
- Lei Hou
- Juanzi Li
affiliations:
- Tsinghua University
arxiv_id: '2608.18988'
url: https://arxiv.org/abs/2608.18988
pdf_url: https://arxiv.org/pdf/2608.18988
published: '2026-08-19'
collected: '2026-08-20'
category: RAG
direction: RAG证据合成优化 · 结构化思维链
tags:
- RAG
- Evidence Synthesis
- Thought Block Chain
- Open-domain QA
- Research Agent
one_liner: 通过结构化Thought Block Chain迭代编织噪声证据，提升开放式问答的回答完整性与引文准确性
practical_value: '- 电商场景商品介绍/问答的证据合成可复用TBC结构：将零散用户评论、商品卖点、竞品信息按维度聚合成思维块，避免生成内容遗漏关键信息、错用证据

  - 商品选品、行业分析类深度调研Agent可直接集成DeepWeaver作为检索后模块：仅需2轮迭代就能大幅提升证据覆盖率、引文准确性，ROI远高于单纯扩大上下文窗口

  - 长上下文信息利用率低的问题可通过「主TBC+残余证据子TBC迭代合并」思路解决：不需要依赖超长上下文大模型，通过分块聚合残余信息即可提升信息召回率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RAG和深度调研Agent的retrieve-then-generate流程存在**证据合成鸿沟**：LLM无法有效利用大量噪声、碎片化的检索证据，直接生成会出现证据利用不足、引文错配、信息被压缩成泛化摘要等问题，单纯优化检索质量、扩大上下文窗口无法解决该问题。

### 方法关键点
- 提出**Thought Block Chain (TBC)** 结构化表示：每个思维块存储对应主张、关键词、关键信息、支撑证据片段，实现主张与证据的显式映射
- 三阶段证据编织流程：1）Draft：基于初始检索证据生成回答草稿，提取主TBC；2）Subordinate：识别未被主TBC覆盖的残余证据，生成从属TBC挖掘遗漏主张；3）Commit：合并主/从属TBC的重叠主张，丢弃低质量块，重复2-3轮迭代
- 最终基于迭代完成的TBC分块生成回答，每个块仅关联对应证据子集，降低上下文压力，提升引文准确率

### 关键结果
- 自研LoQA基准数据集：100道水环境领域专业开放式问题，每道匹配200段（约20万token）含噪声的检索证据，从内容充分性、引文准确性、细节保留度三个维度评估
- 跨Qwen、DeepSeek等多个LLM backbone均稳定提升：在Qwen3-30B上，相比原生RAG，论点充分性提升15.5%，相关引文数提升14.7，细节保留度提升16.6%
- 在DeepResearch Bench上，相比SOTA深度调研Agent WebWeaver，有效引文数提升33.39，引文准确率提升37.02%，综合得分超过OpenAI深度调研Agent

### 核心结论
即使使用更强的长上下文模型，显式的证据合成机制对提升噪声场景下的信息利用率，也比单纯依赖模型本身的上下文能力更有效。
