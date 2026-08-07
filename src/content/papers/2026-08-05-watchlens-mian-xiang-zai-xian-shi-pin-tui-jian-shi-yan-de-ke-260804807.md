---
title: 'WatchLens: A Configurable Platform for Online Video Recommendation Experiments'
title_zh: WatchLens：面向在线视频推荐实验的可配置开源平台
authors:
- Deogyong Kim
- Dongha Lee
affiliations:
- Yonsei University
arxiv_id: '2608.04807'
url: https://arxiv.org/abs/2608.04807
pdf_url: https://arxiv.org/pdf/2608.04807
published: '2026-08-05'
collected: '2026-08-07'
category: RecSys
direction: 视频推荐 · 在线实验平台搭建
tags:
- Video Recommendation
- Online Experiment
- Modular Architecture
- Logging System
- Open Source
one_liner: 开源可配置视频推荐在线实验平台，内置标准化日志层直接关联推荐策略与用户行为事件
practical_value: '- 可复用模块化架构设计：将UI、内容源、推荐策略解耦，支持feed、详情页独立配置策略，可直接用于业务侧快速AB实验平台的搭建

  - 埋点体系可直接借鉴：事件上报时直接关联当前推荐策略ID、排序位置，无需事后回溯拼接，大幅降低推荐策略归因分析的复杂度

  - 小流量验证场景可直接二次改造：开源单服务部署的框架可快速适配短视频、电商内容化场景的小流量策略验证，无需从零搭建实验环境'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有视频推荐用户研究基础设施无法在同一工作流中同时关联推荐策略条件与用户播放行为，归因需事后重构，误差高、效率低。
### 方法关键点
1. 采用模块化架构，UI、内容源、推荐策略完全解耦可独立配置，支持feed流、播放页分别绑定不同推荐策略；
2. 内置标准化日志层，所有用户事件上报时自动附带对应推荐策略ID、排序位置，直接建立策略与行为的关联链路，无需事后回溯拼接。
### 关键结果
- 短视频场景验证：固定UI、feed流策略、内容池，仅变更播放页推荐策略即可完成会话级的策略效果对比；
- 平台支持单服务器部署，完全开源，可直接用于可复现的在线推荐研究。
