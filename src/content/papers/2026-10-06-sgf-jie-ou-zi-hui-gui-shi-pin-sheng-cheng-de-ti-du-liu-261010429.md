---
title: 'SGF+: Decoupling Gradient Flows for Autoregressive Video Generation'
title_zh: SGF+：解耦自回归视频生成的梯度流
authors:
- Zihan Su
- Junhao Zhuang
- Yaowei Li
- Siwen Lu
- Haoran Li
- Lingen Li
- Haoyu Wu
- Weiyang Jin
- Songchun Zhang
- Haoyang Huang
affiliations:
- Tsinghua University
- Joy Future Academy, JD
- The Chinese University of Hong Kong
arxiv_id: '2610.10429'
url: https://arxiv.org/abs/2610.10429
pdf_url: https://arxiv.org/pdf/2610.10429
published: '2026-10-06'
collected: '2026-10-08'
category: Multimodal
direction: 多模态生成 · 自回归长视频生成
tags:
- Autoregressive_Generation
- Video_Generation
- Gradient_Decoupling
- Long_Horizon_Generation
- KV_Cache
one_liner: 解耦自回归视频生成中上下文写入与去噪的参数梯度，仅用5s训练数据支撑24h连续视频生成
practical_value: '- 推荐/生成式场景的长序列建模可借鉴参数解耦思路，分开建模历史上下文编码、当前预测的参数，避免两类任务梯度冲突，同时提升效果与长序列稳定性

  - 长时序生成/预测场景（如用户长期兴趣建模、连续内容推送序列生成）无需额外长时序训练数据，仅通过上下文模块对未来预测的贡献做监督，即可降低训练成本

  - KV cache写入、读取的参数解耦思路可迁移到长上下文Agent、长序列推荐的推理优化，提升长上下文的生成/预测一致性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
自回归视频生成任务中，当前帧去噪、KV上下文写入两个核心任务共享参数，梯度模式存在系统性负对齐，同时损害生成画质与时序一致性。
### 方法关键点
提出SGF+架构，为上下文写入、去噪任务分配独立参数，通过因果注意力保留二者交互；无需引入辅助损失，仅用原始生成目标联合优化，上下文写入模块通过对未来预测的贡献获得监督信号。
### 关键结果数字
仅用5秒视频数据训练，无需长视频微调即可支撑最长24小时连续视频生成；帧生成、块生成两种模式下，画质与长时序一致性均显著优于SGF、SF等基线方案。
