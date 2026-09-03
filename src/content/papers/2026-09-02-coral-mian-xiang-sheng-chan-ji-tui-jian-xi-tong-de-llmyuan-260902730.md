---
title: 'CORAL: An LLM-Native Harness for Production Recommender Systems'
title_zh: CORAL：面向生产级推荐系统的LLM原生智能代理框架
authors:
- Muhammad Rafay Azhar
- Yuhang Zhou
- Gilbert Jiang
- Yuchen Wang
- Rahul Sharma
- Matthew DeSousa
- Jiayi Liu
- Xin Guo
- Lizhu Zhang
- Xiangjun Fan
affiliations:
- Meta AI
arxiv_id: '2609.02730'
url: https://arxiv.org/abs/2609.02730
pdf_url: https://arxiv.org/pdf/2609.02730
published: '2026-09-02'
collected: '2026-09-03'
category: Agent
direction: Agent 推荐系统自动调优
tags:
- LLM Agent
- Recommender System
- Closed-loop Optimization
- Production Deployment
- Constrained Optimization
one_liner: 搭建LLM驱动的闭环自动优化框架，替代人工调优生产推荐系统配置，兼顾效果与效率
practical_value: '- 可复用「LLM负责决策推理+数值约束优化器做边界校验」的分工架构，避免LLM输出违反成本预算、业务规则的结果，大幅降低线上部署风险

  - 记忆模块直接参考三段式设计：观测存储（实时运行指标）+ 评估存储（历史性能判断）+ 决策存储（历史配置与效果），无需微调LLM即可实现上下文内迭代优化

  - 落地优先选择资源分配类场景（召回源配额、用户分群算力分配等），这类问题规则清晰、效果易量化，是Agent调优推荐系统的最优切入点

  - 采用按周期而非按请求调用LLM的模式，极大降低推理成本，Meta两个落地场景单轮LLM调用成本仅数十美元，远低于人工调优的收益与人力成本'
score: 10
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
工业级推荐系统包含召回、排序、服务等多阶段链路，存在大量可调参数（如召回源预算、排序权重、缓存策略、分群规则），传统调优依赖人工提出假设、上线AB实验验证，迭代周期长达数周，受限于工程师人力投入，很多模块长期得不到优化，易随内容生态、用户行为、上游模型变化出现性能漂移。现有LLM在推荐领域的应用多聚焦于排序、用户建模或离线模型开发，很少有能直接作用于线上生产系统、从自身决策效果中闭环学习的成熟方案。

### 方法关键点
- 三段式持久化记忆：存储三类信息，分别是各模块实时运行统计的观测数据、LLM对模块性能的自然语言评估数据、历史配置与对应效果的决策数据，支持跨周期经验复用
- 工具链分工设计：包含分析、检索、归因、约束优化器四类工具，LLM负责基于多源异构信号输出调优决策，约束优化器自动将候选配置投影到预算可行域，保证所有决策符合成本约束
- 固定周期闭环流程：默认每3天为一个迭代周期，依次执行观测收集、LLM推理决策、约束校验、线上部署、效果归因、记忆更新，全程无需微调LLM，仅通过上下文积累实现决策质量提升

### 关键实验
在Meta两个亿级用户社交平台开展AB实验：视频推荐场景在无新增服务成本的前提下，全局观看会话提升0.16%，低信号/新用户会话提升0.23%；另一服务场景在不降低用户参与度的前提下，年算力成本节省达百万美元级，优化效果随迭代周期逐步提升，单轮LLM推理成本仅几十美元。

### 核心结论
LLM代理替代人工完成推荐系统的持续运维调优具备极高的落地性价比，通过「LLM做认知决策+确定性工具做边界约束」的架构，能在极低的成本下获得远高于人工调优的迭代效率。
