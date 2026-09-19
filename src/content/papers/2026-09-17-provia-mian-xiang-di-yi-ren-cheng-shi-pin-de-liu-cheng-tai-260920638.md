---
title: 'PROVIA: Procedure State Tracking for Online Mistake Detection in Egocentric
  Videos'
title_zh: PROVIA：面向第一人称视频的流程状态跟踪在线错误检测方法
authors:
- Di Wen
- Kailun Yang
- Jimmy Weissert
- Luc Maria Scherrer
- Cedric Zöllner
- Ruiping Liu
- Yufan Chen
- Jiale Wei
- Junwei Zheng
- Kunyu Peng
arxiv_id: '2609.20638'
url: https://arxiv.org/abs/2609.20638
pdf_url: https://arxiv.org/pdf/2609.20638
published: '2026-09-17'
collected: '2026-09-19'
category: Other
direction: 第一人称视频 流程在线错误检测
tags:
- Egocentric Video
- Procedure State Tracking
- Online Anomaly Detection
- Bayesian State Merging
- Error Detection
one_liner: 提出双状态跟踪的PROVIA框架，实现第一人称视频流程低误报在线错误检测
practical_value: '- 双状态（事实执行状态/预期流程状态）分离跟踪的思路，可迁移到电商直播运营质检、客服操作合规性检测等业务流程异常检测场景

  - 固定误报率预算约束下的序列报警优化方法，可复用在推荐/广告系统的实时异常流量、作弊行为检测任务

  - 基于完整流程而非首次错误截断的评估范式，可用于优化业务错误检测类系统的效果评测指标设计'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有第一人称视频在线错误检测采用首次错误截断的评估范式，存在基准作弊漏洞，无法适配错误后恢复的真实场景，亟需支持完整流程下的低误报在线检测能力。
**方法关键点**：1. 双状态跟踪机制：分离记录含错误的实际执行事实状态，以及基于正确示范经贝叶斯状态合并生成自动机的可接受进度状态，仅正确分支允许状态跃迁，错误/修正分支保留原状态；2. 采用序列检验将逐帧错误概率转换为报警，支持固定误报率预算约束。
**关键结果数字**：在4个公开数据集上错误检测排序优于所有基线，每分钟0.1次误报预算下，CaptainCook4D数据集召回0.154（基线0.128），HoloAssist数据集召回0.034（基线0.015），全预算区间领先，推理速度58-70FPS。
