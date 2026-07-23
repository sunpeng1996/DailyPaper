---
title: 'PercepCap: Video Captioner with Structured Spatio-Temporal Perception'
title_zh: PercepCap：具备结构化时空感知能力的视频字幕生成模型
authors:
- Yifan Xu
- Zihao Wang
- Zhixiao Wang
- Jiaming Zhang
- Yichun Yang
- Desen Meng
- Yuanxing Zhang
- Pengfei Wan
- Limin Wang
affiliations:
- 南京大学计算机软件新技术国家重点实验室
- 快手科技Kling团队
- 上海人工智能实验室
arxiv_id: '2607.20389'
url: https://arxiv.org/abs/2607.20389
pdf_url: https://arxiv.org/pdf/2607.20389
published: '2026-07-22'
collected: '2026-07-23'
category: Multimodal
direction: 多模态大模型 · 视频时空感知字幕生成
tags:
- MLLM
- Video Captioning
- Spatio-Temporal Perception
- Two-stage Training
- Reinforcement Learning
one_liner: 提出感知-描述两阶段视频字幕框架，通过显式时空感知证据提升生成字幕质量
practical_value: '- 电商短视频商品解说、直播内容自动打标签场景，可复用「先感知（物体轨迹+时序事件）再生成文案」的两阶段范式，大幅降低生成幻觉

  - 多模态生成任务可借鉴Caption-Anchored数据构造方法：先锁定生成目标再反向对齐感知标注，显著降低人工标注成本

  - 生成式电商文案、内容种草文案场景可迁移两阶段训练策略：先用SFT适配生成链路，再用联合奖励RL同步优化事实准确性和表达流畅性'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有MLLM做视频字幕生成时直接输出结果，无显式感知证据支撑，时空感知错误仅能从最终字幕发现，难定位、难监督，幻觉问题突出。

### 方法关键点
1. 采用「感知-描述」生成链路：先输出包含物体轨迹、时序事件的时空感知轨迹，再基于感知证据生成最终字幕；
2. 两阶段训练：第一阶段PD-SFT微调适配两阶段生成链路，第二阶段PG-RL用感知链路+最终字幕的联合奖励，同步优化感知准确性和生成质量；
3. 提出字幕锚定的感知数据构造pipeline：先生成字幕，提取提及的物体、事件后反向回标视频中的框和时间戳，生成对齐的训练数据，保证感知痕迹和字幕对应。

### 关键结果
在DREAM-1K、CaReBench等字幕评估集，以及ShortVidBench等字幕转QA评估集上，效果均优于Qwen3-VL基线，达到领先字幕质量。
