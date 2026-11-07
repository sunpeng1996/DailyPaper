---
title: 'Gabor Gabor: E-Gaborformer, a Strictly Causal Speech Recognizer with Gabor-Dictionary
  Convolutions and Delta-Rule Memory'
title_zh: E-Gaborformer：结合Gabor卷积与Delta规则记忆的严格因果语音识别器
authors:
- Nir Krakowski
- Tamir Cohen
- Ohad Zohar
- Chen Zarfati
affiliations:
- Deepdub
arxiv_id: '2611.08092'
url: https://arxiv.org/abs/2611.08092
pdf_url: https://arxiv.org/pdf/2611.08092
published: '2026-11-05'
collected: '2026-11-07'
category: Agent
direction: 实时语音Agent · 低内存流式ASR优化
tags:
- ASR
- causal_model
- streaming_inference
- speech_agent
- memory_optimization
one_liner: 提出严格因果语音识别编码器E-Gaborformer，在恒定低内存下实现优于同类模型的精度与训练速度
practical_value: '- 长会话实时Agent场景可复用「固定大小状态+滑动窗口注意力」架构，避免KV cache随会话长度膨胀，大幅降低长时服务成本

  - 可借鉴固定字典卷积的设计思路，在时序特征抽取模块减少可训练参数量，同时保留稳定的时序建模能力

  - 同一权重支持无前瞻/固定前瞻两种推理模式的设计，可迁移到实时推荐/多轮对话Agent场景，兼顾低延迟与精度要求

  - RNN-T lattice的二类损失改造思路可复用，能大幅提升序列建模类任务的训练效率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
实时语音Agent的ASR需满足严格因果（无未来音频依赖）、单路会话内存不随通话长度增长的要求，现有因果注意力模型的KV cache随时长线性膨胀，长会话服务成本极高。
### 方法关键点
1. 编码器按3:1比例混合Gated DeltaNet-2循环层与滑动窗口注意力，所有时序卷积基于固定因果Gabor原子字典构建，保持单路状态恒定；
2. 对RNN-T lattice做二类问题改造，可计算精确损失与梯度。
### 关键结果
- 生产级单路状态恒定19MB，同规模因果注意力编码器10分钟通话内存超1GB；
- LibriSpeech上收敛速度提升18%，精度持平/优于同配置E-Branchformer；
- 0.6B参数量生产模型英文流量WER比同规模NVIDIA Nemotron 3.5 ASR低28~31%，希伯来语WER比前代系统低20%；
- 同权重支持严格因果/480ms前瞻解码无精度损失，训练速度提升2.6倍
