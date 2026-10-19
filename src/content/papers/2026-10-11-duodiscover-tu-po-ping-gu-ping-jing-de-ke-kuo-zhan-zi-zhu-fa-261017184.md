---
title: 'DuoDiscover: Scaling Autonomous Discovery Beyond the Evaluation Bottleneck'
title_zh: DuoDiscover：突破评估瓶颈的可扩展自主发现系统
authors:
- Shubham Agarwal
- Akshat Gupta
- Mike Heddes
- Dilara Soylu
- Rui Meng
- Patrick Tser Jern Kon
- Jiefeng Chen
- Mert Cemri
- Shu Liu
- Abe Gonzalez
affiliations:
- Google
- UC Berkeley
- Stanford University
arxiv_id: '2610.17184'
url: https://arxiv.org/abs/2610.17184
pdf_url: https://arxiv.org/pdf/2610.17184
published: '2026-10-11'
collected: '2026-10-19'
category: Agent
direction: 多Agent自主优化 · 低成本代理评估
tags:
- AutonomousAgent
- MultiFidelityOptimization
- ProxyEvaluator
- MultiAgentCoordination
- CodeOptimization
one_liner: 提出联合发现优化目标与低成本代理评估器的多Agent系统，突破高成本评估的自主发现瓶颈
practical_value: '- 面对评估成本极高的业务优化场景（如推荐全链路压测、广告策略A/B测试），可借鉴「优化目标+代理评估器」联合发现思路，先让Agent生成局部模块的低成本yardstick做迭代，大幅减少真实评估次数

  - 多Agent协作架构可直接复用：轻量编排器仅管理高成本真实评估、终止停滞Agent、迁移验证后的优化收益，无需全局任务分解，降低架构复杂度

  - 代理评估器fidelity校验机制可复用：用Kendall τ秩相关性验证代理评分与真实评分的排序一致性，动态淘汰漂移的代理评估器，避免Reward Hacking

  - 针对LLM驱动的业务优化任务（如广告文案生成、排序策略迭代），该思路可大幅降低A/B测试资源消耗，提升迭代效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
自主发现系统落地真实工程优化场景的核心瓶颈是真实评估成本极高，如vLLM全链路性能评估需85分钟，CPU微架构设计单次评估达28小时，传统方法依赖人工设计的固定评估器，无法适配动态优化目标，迭代效率极低。

### 方法关键点
- 每个worker coding Agent联合发现待优化的代码子区域（target）和对应的低成本代理评估器（yardstick），在yardstick上做快速爬山迭代，仅获得代理收益后触发真实评估
- 引入fidelity测试机制，每次真实评估后用Kendall τ秩相关性校验yardstick和真实评估的排序一致性，动态淘汰发生漂移的代理评估器，避免优化偏离真实目标
- 采用自底向上的多Agent协作架构，轻量编排器仅负责终止停滞Agent、基于验证后的收益孵化新Agent、跨Agent同步优化进展，无需全局任务分解

### 关键结果
在2个代码库基准、4个GPU/TPU内核套件、5个真实系统优化任务上全面超越基线：SWE-fficiency任务上达到人类专家平均加速比的2倍；SOL-Exec基准235个内核中121个排名第一，212个进入前三；vLLM和SQLite分别获得1.92×、1.38×的性能提升；CPU架构优化任务上比ArchAgent v2耗时缩短60%，收益提升65%，超过人类最优设计。

**最值得记住的一句话**：当评估成为优化瓶颈时，让Agent同时发现「优化什么」和「怎么快速评估」，比单纯提升搜索效率的收益高得多
