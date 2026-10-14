---
title: 'PsyBer-Agent: A Psychology-Driven User Agent for Recommender Systems'
title_zh: PsyBer-Agent：面向推荐系统评测的心理学驱动用户模拟Agent
authors:
- Chong Zhang
- Qijie Shen
- Haichao Zhang
- Can Wang
- Xiaobo Jin
- Jia Wang
affiliations:
- Xi'an Jiaotong-Liverpool University
- University of Liverpool
- Alibaba Group
arxiv_id: '2610.13989'
url: https://arxiv.org/abs/2610.13989
pdf_url: https://arxiv.org/pdf/2610.13989
published: '2026-09-25'
collected: '2026-10-14'
category: Agent
direction: 推荐系统预部署评测 · 用户模拟Agent
tags:
- UserSimulator
- PsychologicalModeling
- RecommenderEvaluation
- OptimalTransport
- LLMAgent
one_liner: 结合心理学显式状态建模与UGW对齐，实现高保真可扩展的推荐系统预部署用户模拟器
practical_value: '- 可复用Psy-Engine的三态（认知/情绪/自我一致性）建模框架，替代纯prompt用户模拟方案，大幅降低长周期交互下的行为漂移问题

  - 不需要微调骨干LLM的UGW轨迹对齐+轻量fast policy蒸馏方案，可直接迁移到各类用户行为仿真场景，降低推理成本与延迟

  - WebSim的百万级并发仿真架构可直接复用在电商大促前的推荐策略压测，提前发现用户疲劳、偏好偏移等长周期业务问题

  - 行为保真度评估指标体系（JSD/皮尔逊相关/EMD）可直接用到自有的用户模拟器迭代验证中，对齐真实用户行为分布'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
推荐系统预部署迭代高度依赖线上A/B测试，成本高、周期长且存在业务风险，离线日志回放无法捕捉用户疲劳、偏好偏移、情绪变化等长周期闭环交互动态。现有LLM驱动的用户模拟器多为纯prompt驱动，长交互周期下易出现行为漂移，且普遍不支持工业级大规模并发仿真，无法满足推荐策略快速迭代的评测需求。
### 方法关键点
- 核心Psy-Engine模块显式建模三类可解释用户隐状态：认知储备（吸引力-疲劳差值）、情绪满意度、自我一致性，通过固定可配置的规则实现状态转移，避免纯prompt驱动的行为不可控问题
- 采用Unbalanced Gromov–Wasserstein（UGW）最优传输对齐离线真实交互轨迹与模拟器生成的隐状态轨迹，无需微调骨干LLM，仅蒸馏轻量fast policy即可实现低延迟推理
- 配套开源WebSim仿真平台与PsyBer基准，覆盖电商、短视频、长视频等多场景，支持7类主流推荐backbone的闭环A/B测试
### 关键实验结果
在MM-ML-1M、Amazon Review、MicroLens等多数据集上对比RecAgent、Agent4Rec、DyTA4Rec等主流模拟器：
- 行为保真度全面领先：CTRGap低至0.406，JSD仅0.286，皮尔逊相关系数达0.305，单步推理延迟仅2.53s
- 扩展性满足工业需求：支持最高5M并发仿真任务，p95延迟仅3.8s，任务成功率超91%
- 与真实用户行为的HR@10、NDCG@10、CTR差值分别仅为0.003、0.0016、0.004，保真度接近真人

> 最值得记住的结论：基于心理学先验的显式状态建模+离线轨迹轻量蒸馏，是平衡用户模拟器保真度、可解释性、工业化扩展性的高性价比路径。
