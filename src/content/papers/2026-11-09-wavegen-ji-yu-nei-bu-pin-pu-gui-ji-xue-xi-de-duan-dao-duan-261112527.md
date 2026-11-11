---
title: 'WaveGen: Truly End-to-End Waveform Generation via Internal Spectral Trajectory
  Learning'
title_zh: WaveGen：基于内部频谱轨迹学习的端到端波形生成框架
authors:
- Sang-Hoon Lee
- Ha-Yeong Choi
affiliations:
- Ajou University
- KT Corp.
arxiv_id: '2611.12527'
url: https://arxiv.org/abs/2611.12527
pdf_url: https://arxiv.org/pdf/2611.12527
published: '2026-11-09'
collected: '2026-11-11'
category: Other
direction: 端到端文本转语音 · 扩散生成
tags:
- TTS
- Diffusion Model
- End-to-End
- Waveform Generation
- Spectral Learning
one_liner: 提出基于Spectral Forcing的全端到端文本转波形扩散框架，无需外部中间模块性能达SOTA
practical_value: '- 电商智能客服、商品讲解音频生成场景可直接复用WaveGen端到端架构，砍掉多模块拼接的TTS链路，降低工程部署复杂度

  - 语音交互类Agent可借鉴Spectral Forcing的解耦扩散头设计，单模型完成文本-语音对齐与波形生成，减少外部依赖

  - 端到端生成任务训练可复用多尺度频谱v-loss优化目标，适配无外部预训练表征的单阶段训练场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有TTS链路依赖独立训练的中间模块（神经音频编解码器、Mel声码器、时长预测器）与外部自监督表征，链路冗余、部署成本高，无真正端到端的单模型方案。
### 方法关键点
1. 基于Spectral Forcing设计全端到端扩散式文本转波形框架，单模型联合学习内部频谱轨迹与目标波形轨迹，内置文本-语音对齐能力，完全移除外部中间模块与自监督表征依赖；
2. 采用解耦扩散头架构，搭配多尺度频谱v-loss作为训练目标，支持单阶段训练。
### 关键结果数字
参数可在0.1B-0.6B区间稳定缩放，单架构、开源数据单阶段训练在Emilia数据集达SOTA，Seed-en基准上WER 1.47、SIM 0.75，代码与权重全开源。
