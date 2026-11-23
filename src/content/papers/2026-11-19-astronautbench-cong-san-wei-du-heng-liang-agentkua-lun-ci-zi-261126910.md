---
title: 'AstronautBench: Measuring Agent Self-Improvement Across Episodes Through Knowledge,
  Evidence, and Progress'
title_zh: AstronautBench：从三维度衡量Agent跨轮次自提升能力
authors:
- Congyuan Yu
- Runping Tian
affiliations:
- Carnegie Mellon University
arxiv_id: '2611.26910'
url: https://arxiv.org/abs/2611.26910
pdf_url: https://arxiv.org/pdf/2611.26910
published: '2026-11-19'
collected: '2026-11-23'
category: Agent
direction: Agent 自提升能力评测基准
tags:
- Agent Benchmark
- Self-Improvement
- Episodic Memory
- LLM Agent
- Embodied Agent
one_liner: 提出三维度Agent自提升评测基准，可准确衡量固定权重下的跨轮次学习效果
practical_value: '- 做Agent效果评估时不要仅看任务完成率，可新增知识正确性、知识可归因性两个维度，避免把预训练见过的知识误判为自提升效果，适配电商导购Agent、搜索Agent的评测场景

  - Agent记忆系统可参考实体中心增量存储设计，每个知识条目绑定采集证据（时间、上下文、位置），既方便归因也能解决记忆冲突，适合电商场景用户行为记忆、商品知识记忆的架构设计

  - 采用多模型家族的LLM组成评测陪审团，可大幅降低单模型Judge的偏差，可直接复用在推荐文案、Agent回答的效果评测流程中'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent自提升评测仅依赖任务进度、QA正确率、episodic memory三类单一指标，但正确答案可能来自预训练而非自身探索，进度提升也不代表掌握了对应知识，单一指标会严重误判固定权重下的跨轮次自提升真实效果。

### 方法关键点
- 基于《Outer Wilds》游戏搭建评测环境，每轮22分钟后世界完全重置，仅Agent的知识可跨轮保留，任务进度完全由其掌握的知识决定
- 从三个独立维度评估自提升效果：1）进展：累计到达的地点、解锁的传闻事实；2）知识：164道游戏相关单事实QA的正确率；3）归因：每个答案必须绑定自身探索过程中采集的帧、位置、轮次证据，由跨模型家族的两个LLM Judge分别校验正确性和归因匹配度
- 基准Agent采用实体中心增量知识库，每条知识绑定来源证据，仅追加不修改，自动处理记忆冲突

### 关键结果数字
- GPT-6.1 Sol Agent经过8轮后QA正确率从14.6%提升到26.8%，但仅59%~68%的正确答案能匹配到自身采集的证据
- 该Agent在第3轮后就不再解锁新的传闻事实，但探索地点、记忆条目仍持续增长，超过一半的后期新增正确答案仅引用前3轮的证据
- 双LLM Judge的正确性判断一致性κ达0.97，归因判断一致性κ达0.83，可靠性远高于单模型评测

### 核心结论
固定权重下Agent的自提升效果不能用单一指标衡量，知识、归因、进展三个维度往往不同步，单一指标要么高估要么低估真实提升。
