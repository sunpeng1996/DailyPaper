---
title: Few-Step Streaming Video Generation via Condition Shifting
title_zh: 基于条件偏移的少步长流式视频生成方法
authors:
- Deyuan Liu
- Jungang Li
- Kaiwen Zheng
- Kai Jiang
- Jintao Chen
- Yaole Wang
- Ming Lin
- Tao Lin
- Jianfei Chen
- Jun Zhu
affiliations:
- Tsinghua University
- Shengshu Technology
- Westlake University
arxiv_id: '2611.14033'
url: https://arxiv.org/abs/2611.14033
pdf_url: https://arxiv.org/pdf/2611.14033
published: '2026-11-09'
collected: '2026-11-11'
category: Multimodal
direction: 多模态生成 · 少步长流式视频生成
tags:
- Video Generation
- Streaming Generation
- Condition Shifting
- Knowledge Distillation
- Multimodal
one_liner: 通过条件偏移消除独立伪分数网络，实现低训练开销的高性能少步长流式视频生成
practical_value: '- 生成电商营销短视频、商品展示内容时，可复用条件偏移思路取消独立打分网络，降低训练显存占用与迭代耗时，适配大批次内容生成需求

  - 流式生成长序列内容（如直播切片、商品解说长视频）时，可参考少步采样+冻结教师模型+Self-Replay Forcing的训练范式，平衡生成质量与速度

  - 做生成内容的用户偏好评估时，可复用分维度（指令遵循、一致性、质量）的净偏好率指标设计，对齐业务侧真实体验需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
少步采样可降低流式视频生成的推理开销，但现有DMD方法依赖独立伪分数网络做监督，额外增加训练显存与计算成本，还需跟踪动态变化的生成器状态。
### 方法关键点
将APEX扩展到流式视频生成场景，通过条件偏移在生成器内部估计生成分布的速度场：原始文本条件用于正常生成任务，偏移后的条件用于伪样本估计，两套任务共享同一套模型参数，无需独立伪分数网络，同时保留S2-Avatar的冻结参考教师模型、Self-Replay Forcing、感知正则化模块。
### 关键结果数字
相比S2-Avatar，Progressive赛道指令符合度3.856（基线3.831），双赛道视觉美学得分0.6419（基线0.6326）；人类评估指令遵循净偏好率高30.0%，一致性、视频质量净偏好率高4.3%；相比DMD，单GPU峰值显存低4.4%，平均迭代耗时短9.2%
