---
title: 'LiveAudio: From Bidirectional to Autoregressive Diffusion for Real-Time Streaming
  Video-to-Audio Generation'
title_zh: LiveAudio：基于双向转自回归扩散的实时流式视频转音频生成
authors:
- Yuxuan Jiang
- Zehua Chen
- Yusheng Dai
- Andong Wang
- Weibei Dou
- Jun Zhu
affiliations:
- Tsinghua University
- Monash University
- Renmin University of China
arxiv_id: '2611.30714'
url: https://arxiv.org/abs/2611.30714
pdf_url: https://arxiv.org/pdf/2611.30714
published: '2026-11-23'
collected: '2026-11-27'
category: Multimodal
direction: 多模态生成 · 流式低延迟扩散模型
tags:
- Diffusion Model
- Streaming Generation
- Video-to-Audio
- Knowledge Distillation
- Low Latency
one_liner: 将预训练双向扩散视频转音频模型改造为低延迟流式生成框架，效果优于现有流方案
practical_value: '- 离线预训练双向大模型转在线流式服务的「渐进式因果微调+知识蒸馏」方案，可直接复用在直播实时配音、实时内容审核、流式会话推荐等需要低延迟输出的业务场景，避免从零训练流式模型的效果损失

  - 时序输入分块生成、每块仅依赖已输入历史数据的设计思路，可迁移到实时推荐系统的流式用户行为建模，无需等待全量会话数据即可更新推荐结果，降低推荐响应延迟

  - 单A100 GPU下实时因子0.79、首包延迟143ms的性能指标，可作为实时多模态生成服务的性能基线参考，用于评估同类业务的优化效果'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视频转音频生成模型多为双向结构，需等待全量视频输入才能生成音频，无法满足直播、互动游戏等场景的实时低延迟需求，从零训练流式模型又难以保证音质和音画同步性。
### 方法关键点
提出LiveAudio流式生成框架，基于预训练双向扩散模型改造，通过渐进式因果微调+知识蒸馏转换为自回归流式生成器，按块生成音频，每块仅依赖已播放的输入视频，大幅降低单块采样步数。
### 关键结果数字
在VGGSound数据集上，音频质量、音画同步性均优于现有流式模型，同步性甚至超过原双向基线模型；单A100 GPU上实时因子0.79，首帧生成延迟143ms，满足实时生产要求。
