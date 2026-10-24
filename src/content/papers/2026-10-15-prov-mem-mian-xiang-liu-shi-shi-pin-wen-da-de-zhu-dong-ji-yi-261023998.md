---
title: 'ProV-Mem: Proactive Memory for Streaming Video Question Answering'
title_zh: ProV-Mem：面向流式视频问答的主动记忆框架
authors:
- Bingbing Wang
- Jing Li
- Han Gao
- Yishi Lin
- Ruifeng Xu
- Peng He
affiliations:
- The Hong Kong Polytechnic University, Department of Computing
- The Hong Kong Polytechnic University, Research Institute for Generative AI
- Tencent Inc.
- Shenzhen Loop Area Institute
arxiv_id: '2610.23998'
url: https://arxiv.org/abs/2610.23998
pdf_url: https://arxiv.org/pdf/2610.23998
published: '2026-10-15'
collected: '2026-10-24'
category: Agent
direction: 主动视觉Agent · 分层记忆架构
tags:
- VLM
- Memory_Architecture
- Streaming_VQA
- Training_Free
- Proactive_Agent
one_liner: 基于冻结VLM的免训练三层轻量主动记忆架构，实现低延迟流式主动视频问答
practical_value: '- 三层轻量记忆设计可直接复用在直播/实时短视频流主动互动Agent场景，无需微调大模型即可落地，大幅降低推理成本

  - 情景记忆的近重复内容过滤逻辑可迁移到推荐系统内容去重、直播弹幕/互动消息重复推送过滤场景，减少无效用户打扰

  - 新增的CAUC评估指标可直接用来优化实时push、直播互动消息的推送效果，量化冗余推送的惩罚权重'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
主动流式视频问答要求Agent无显式用户查询时自主监控视频流、决策响应时机、回复内容、是否输出，现有方案要么存储长时序视觉历史推理成本过高，要么丢弃历史导致漏检测事件、重复回复，无法平衡效果与实时性。
### 方法关键点
基于冻结VLM搭建免训练的三层轻量记忆架构：1. 时序触发记忆控制VLM查询时机，避免长时间无响应；2. 指令记忆通过固定prompt先验生成视觉对齐的简洁回复；3. 情景记忆过滤近重复回复，决策最终是否输出。同时提出CAUC评估指标，在PAUC基础上新增对冗余、过频、过长输出的惩罚。
### 关键结果
在ProactiveVideoQA 4个场景下CAUC全部最优，WEB/EGO/TV 3个场景PAUC最优，同时保持极低的单响应推理latency。
