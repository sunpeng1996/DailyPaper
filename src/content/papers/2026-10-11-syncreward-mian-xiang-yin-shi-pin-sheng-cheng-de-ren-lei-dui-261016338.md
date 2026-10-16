---
title: 'SyncReward: Human-Aligned Synchronization Reward for Audio-Visual Generation'
title_zh: SyncReward：面向音视频生成的人类对齐同步奖励模型
authors:
- Kaisi Guan
- Ying Ba
- Wenjing Wang
- Xihua Wang
- Chen Li
- Jing Lyu
- Ruihau Song
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- WeChat, Tencent Inc.
arxiv_id: '2610.16338'
url: https://arxiv.org/abs/2610.16338
pdf_url: https://arxiv.org/pdf/2610.16338
published: '2026-10-11'
collected: '2026-10-16'
category: Multimodal
direction: 多模态生成 · 音视频同步奖励建模
tags:
- Multimodal Generation
- Reward Model
- Audio-Visual Alignment
- Human Alignment
- Dataset
- Benchmark
one_liner: 构建80K标注数据集与评估基准，提出人类对齐的音视频生成同步奖励模型
practical_value: '- 电商音视频带货素材生成场景可复用同步奖励逻辑，解决口型、动作与音效不匹配的生成质量问题，通过best-of-N推理或RL后训优化生成结果

  - 多模态内容质量评估可参考「真实数据对比预训练+生成数据人工标注微调」的奖励模型构建范式，降低标注成本同时对齐人类感知

  - 多模态生成任务的评估体系可参考分类taxonomy构建思路，覆盖不同场景细分case，提升评估基准的鲁棒性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前音视频生成任务普遍存在音频与视觉事件时间不同步问题，核心瓶颈是缺乏同步性标注数据、可靠评估基准和对齐人类感知的同步评估模型。

### 方法关键点
1. 构建含80K专业同步评分的SyncReward-Data-80K数据集，覆盖语音、触发事件、乐器、环境音4大类音视频场景；
2. 搭建含1K多专家标注样本的SyncReward-Bench基准，验证现有同步度量与多模态模型和人类判断存在显著偏差；
3. 提出SyncReward奖励模型，结合真实片段语义-时序对比预训练+生成片段人工标注微调。

### 关键结果
SyncReward作为评估指标时与人类评分一致性为所有参评方法最高；作为奖励函数时，通过推理时best-of-N选择、RL后训可显著提升生成音视频的同步性
