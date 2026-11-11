---
title: 'Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game'
title_zh: 《RE-SEARCH：双玩家问答游戏拆解大模型科研创意能力》
authors:
- Muhan Gao
- Hangxiao Zhu
- Xinqi Su
- Yu Zhang
- Daniel Khashabi
- Kuan-Hao Huang
affiliations:
- Texas A&M University
- Johns Hopkins University
arxiv_id: '2611.14487'
url: https://arxiv.org/abs/2611.14487
pdf_url: https://arxiv.org/pdf/2611.14487
published: '2026-11-10'
collected: '2026-11-11'
category: Eval
direction: Agent 科研创意能力评估与瓶颈分析
tags:
- LLM Ideation
- Agent Evaluation
- Scientific Discovery
- Benchmark
- Information Seeking
one_liner: 提出双玩家问答基准RE-SEARCH，拆解LLM科研创意瓶颈，核心短板为生成而非判断力
practical_value: '- 创意类、搜索类Agent无需死磕单模型生成能力，优先引入多模型生成候选池、行业知识候选集，让LLM做选择即可，成本更低收益更高，可直接复用至电商选品、营销文案创意、推荐策略探索等场景

  - 长链路Agent任务可复用结论：前30%交互步基本决定最终效果，需重点优化前序流程的prompt设计、候选生成质量，减少后续无效迭代，降低KV cache等资源消耗

  - 创意探索类Agent的搜索策略可直接套用倒U型最优广度：控制顶级探索分支数约8个，避免过度探索频繁切换方向，也不要过度利用困在局部错误方向'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM科研创意评估要么是单步生成后直接打分，忽略迭代演进过程；要么是端到端benchmark混了编码、实验等执行环节，无法单独拆解创意构思（ideation）的瓶颈，不清楚LLM在创意探索中的核心短板。
### 方法关键点
- 设计RE-SEARCH双玩家20问游戏范式：给定已发表论文的研究问题，审问者LLM通过最多100道是非问句探索论文核心方案，回答者LLM基于论文全文给出是/否/未知回复；每10步审问者输出当前创意猜想，由3个LLM法官打1-10分的还原度。
- 数据集来自200篇2025年8月后发表的ICML 2026论文，避开所有测试模型的知识cutoff，避免数据泄露，人工校验提取的问题-核心方案对准确率达93%。
- 设计两组对照实验：多模型候选问题池选择实验、前置包含/不包含正确方案的调研问卷实验，分离生成能力与判断能力的影响。
### 关键结果
- 6款主流LLM测试中，GPT-5.4效果领先，其余模型得分仅为其2/3；所有模型90%的进度在前30个问题完成，后续基本停滞，30步得分与最终得分相关度达0.87~0.92。
- 给弱模型提供多模型生成的候选问题池，得分提升1分以上；给弱模型提供包含正确方案的调研问卷，得分最高提升1.25分，模型越弱提升幅度越大。
- 创意搜索存在倒U型最优广度：最优顶级搜索分支数约8个，过度探索（平均13.7个分支）或过度利用（平均5.2~5.5个分支）都会导致效果显著下降。
### 最值得记住的结论
LLM的创意瓶颈是生成而非判断，与其投入大量资源优化单模型生成能力，引入外部候选池的收益更高。
