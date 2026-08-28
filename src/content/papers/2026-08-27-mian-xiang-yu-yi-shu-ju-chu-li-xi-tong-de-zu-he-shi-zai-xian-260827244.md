---
title: Compositional Online Learning for Semantic Data Processing Systems
title_zh: 面向语义数据处理系统的组合式在线学习框架
authors:
- Paweł Liskowski
- Fuheng Zhao
- Benjamin Han
- Anupam Datta
- Dimitris Tsirogiannis
affiliations:
- Snowflake Inc.
arxiv_id: '2608.27244'
url: https://arxiv.org/abs/2608.27244
pdf_url: https://arxiv.org/pdf/2608.27244
published: '2026-08-27'
collected: '2026-08-28'
category: LLM
direction: LLM语义查询 · 组合式在线学习优化
tags:
- Online Learning
- LLM Inference Optimization
- Semantic SQL
- Query Optimization
- Cascade Routing
one_liner: 利用LLM调用往返间隙组合在线学习组件，语义SQL查询成本最高降低11.4倍
practical_value: '- 做Agent/RAG批量语义处理任务时，可复用「把CPU侧轻量更新藏在LLM调用往返间隙」的设计，不增加端到端 latency
  即可做在线调优，多步LLM调用的路由、prompt选择都可套用该模式。

  - 电商商品语义过滤、用户评论标签生成等批量LLM任务，可直接套用「filter排序+级联路由」的组合优化范式：小模型做proxy、大模型做oracle，先排序高筛选率谓词提前短路，再用级联减少大模型调用，成本可降至原有的1/8。

  - 多个优化组件组合时，需关注上下游分布偏移的损耗：上游筛选后的样本会导致下游proxy校准漂移，需定期用真实oracle标签重校准小模型的阈值，避免收益衰减。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
语义数据处理系统中LLM调用占总查询成本的80~90%，单调用成本是关系型谓词的10^5~10^7倍，传统自适应查询处理要求学习器极轻量的约束在LLM高延迟场景下完全反转——LLM往返的数百毫秒足够承载CPU侧的学习更新，但此前没有框架研究多个在线学习组件的组合收益是否可叠加。

### 方法关键点
1. 提出LLM调用边界的组合式在线学习框架，核心模式是将训练步骤藏在LLM调用往返间隙，不占用关键路径，设计空间沿「决策粒度+更新 cadence」两个轴划分；
2. 在Cortex AISQL落地3个组件：无学习的响应缓存、per-call在线更新的filter排序组件Larch（用MLP做选择性预估，动态调整谓词顺序通过短路减少调用）、per-batch在线更新的级联路由组件GAMCAL（用校准GAM做proxy得分校准，动态调整阈值减少大模型调用）；
3. 提出带成本语义的顺序组合规则，两个学习组件的收益在独立假设下可乘性叠加，同时量化3种跨组件交互的损耗。

### 关键结果
在典型5个语义谓词的联合过滤workload下，独立假设下两个组件叠加最高降本11.4×，考虑跨组件漂移的实际降本约8×；Larch单独比Palimpzest、Quest降低token开销最多19×，GAMCAL单独比SUPG级联最多减少58%的大模型调用即可达到相同F1。

**最值得记住的一句话**：在LLM绑定的语义计算场景下，传统自适应查询处理「学习器必须极轻量」的约束完全反转，利用LLM往返间隙做在线优化是几乎无额外成本的降本手段。
