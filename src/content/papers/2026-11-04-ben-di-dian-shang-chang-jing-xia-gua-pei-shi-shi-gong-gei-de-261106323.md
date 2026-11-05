---
title: Generative Retrieval under Real-Time Supply Constraints in Local Commerce
title_zh: 本地电商场景下适配实时供给约束的生成式检索方案
authors:
- Shaopeng Liang
- Biao Zhang
- Hongzhen Ye
- Zeyang Hou
- Ma Jiang
- Jintao Tu
- yunxi. hz
- Zhijia Fang
- Jianqiang Cao
- Junxue Rao
affiliations:
- Rajax Network Technology (Taobao Shangou, Alibaba)
arxiv_id: '2611.06323'
url: https://arxiv.org/abs/2611.06323
pdf_url: https://arxiv.org/pdf/2611.06323
published: '2026-11-04'
collected: '2026-11-05'
category: GenRec
direction: 生成式推荐 · 实时供给约束优化
tags:
- Generative Retrieval
- Semantic ID
- Constrained Decoding
- Local E-commerce
- CSR Index
one_liner: 提出集成RTP-LLM的请求级供给约束生成式检索管线，降低本地电商供给幻觉与无效算力消耗
practical_value: '- 本地即时零售、外卖等供给动态变化的生成式检索场景，可直接复用「CPU异步编译供给SID集合+GPU共享CSR前缀索引」的架构，将约束编译与模型prefill并行，在控制latency增量的同时大幅减少无效beam的算力浪费

  - 约束解码实现时需优先保留原模型的排序逻辑：先计算全词表log-sum-exp归一化再做非法token mask，避免因父beam概率重归一化导致排序结果偏移，保证检索效果不受约束模块影响

  - 短SID生成场景的约束解码优化不能仅看服务端RT增量，需重点评估端到端client侧latency、有效候选召回量的trade-off，避免请求传输、跨设备同步的额外开销抵消约束带来的算力收益'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
本地即时零售、外卖场景下的生成式检索依赖预训练模型生成Semantic ID召回候选，仅用全局候选空间训练的模型无法感知请求级动态供给变化（位置、天气、交通导致的商家/商品不可配送），会产生大量「ID合法但当前不可供给」的供给幻觉；后过滤机制会浪费宝贵的beam容量与推理算力，而请求级动态约束的编译、传输、解码开销高，短SID生成场景下难以摊销成本，现有方案无法兼顾召回有效性与 latency 要求。
### 方法关键点
- 架构层面将供给约束管线集成到RTP-LLM：上游供给系统输出当前请求的合格实体集合，CPU侧异步将实体对应的3-token SID编译为CSR前缀索引，编译过程与模型prefill完全并行，索引上传GPU后所有beam共享
- 解码阶段保留原模型排序逻辑：先计算全词表的log-sum-exp归一化项，再对非法token做硬mask，避免约束模块改变不同父beam的分数相对排序，保证检索结果的相关性不受影响
- 状态对齐机制：每个beam的约束状态与KV cache使用相同的父映射规则同步更新，保证生成路径与约束状态的一致性，避免错误过滤合法候选
### 关键结果
- 日更目录约束对比实验中，固定beam宽度下无效生成候选占比从56.86%降至9.70%，有效商家召回量从129提升至270，供给幻觉完全消除
- 工程优化后C++实现的3万条SID排序+CSR构建耗时仅约4ms，服务端RT增量仅0.6ms，但端到端client侧RT增量达19ms，传输、跨设备同步开销占比极高
- 不同供给量级重放实验显示，供给条目从2836到26419时，引擎侧RT增量可控制在0.2ms以内，有效候选量随供给规模同步提升

生成式检索的约束解码收益不能仅看模型推理侧开销，要端到端评估供给快照、传输、编译、推理全链路的成本与有效候选召回的ROI。
