---
title: 'Vibe-Trading: Towards Agent-Native Trading'
title_zh: Vibe-Trading：面向Agent原生的交易框架
authors:
- Haozhe Wu
- Zhonghang Li
- Chao Huang
affiliations:
- The University of Hong Kong
arxiv_id: '2611.24845'
url: https://arxiv.org/abs/2611.24845
pdf_url: https://arxiv.org/pdf/2611.24845
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: Agent原生交易框架 · 全链路可信执行
tags:
- Agent
- Trading Agent
- State Tracking
- Provenance
- Multi-Agent
one_liner: 提出全链路Agent原生交易框架，解决动态环境下Agent状态追溯、结果可信与权限管控问题
practical_value: '- 动态环境下的状态-结果绑定方案可复用到大促/实时流量场景的推荐Agent，将召回/排序结果与对应时间窗口、用户实时行为、数据快照绑定，避免决策过时

  - 全链路结果溯源+权限隔离的架构设计可落地到广告投放Agent，将投放策略的生成、回测、上线全流程做证据留存，加显式权限gate控制实际投放动作，降低事故风险

  - 全流程打通的工作空间设计思路可迁移到推荐A/B测试平台，将策略研发、离线评估、线上放量的全链路数据打通，支持实验可复现、迭代可追溯'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有Agent多基于静态工作流，动态环境下难以维持可靠状态绑定，金融交易场景下价格、舆情、仓位、资金持续变化，决策脱离对应时间、数据、上下文会直接失效。
### 方法关键点
1. 推出全链路Agent原生交易框架Vibe-Trading，整合市场调研、数据接入、策略生成、回测、仿真交易、多Agent协作、实盘执行全流程能力；
2. 核心架构实现结果、证据、研究历史、交易权限的全链路绑定，每个输出留存来源、时间范围、配置、运行记录；
3. 配套共享证据对齐、版本化研究记录、显式权限gate三大机制，严格区分策略研发与实盘执行环节。
### 关键结果
框架已开源，可完整支撑可追溯、可复现、仅在显式授权下执行的交易Agent落地，适配动态环境下的Agent任务需求
