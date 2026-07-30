---
title: 'SpeechLLM Meets Federated Learning for End-to-End ASR: English and Italian
  Case Studies'
title_zh: 面向端到端自动语音识别的SpeechLLM联邦学习：英意语案例研究
authors:
- Mohamed Nabih Ali
- Daniele Falavigna
- Alessio Brutti
affiliations:
- Fondazione Bruno Kessler
- Center of Augmented Intelligence
arxiv_id: '2607.25716'
url: https://arxiv.org/abs/2607.25716
pdf_url: https://arxiv.org/pdf/2607.25716
published: '2026-07-28'
collected: '2026-07-30'
category: Training
direction: SpeechLLM 联邦训练优化
tags:
- Federated Learning
- SpeechLLM
- ASR
- Communication Efficiency
- Model Training
one_liner: 首个面向SpeechLLM端到端ASR的联邦训练方案，降低通信开销同时保持词错率竞争力
practical_value: '- 跨端隐私场景下训练大模型时，可复用本文针对高维参数的通信高效优化策略，降低梯度传输开销

  - 电商语音搜索、语音客服类Agent迭代时，可参考该联邦训练方案，在不收集用户原始语音数据的前提下优化ASR效果

  - 分布式训练多模态大模型时，可借鉴本文的编码器架构消融思路，根据业务算力约束选择最优模型配置'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
联邦学习(FL)可实现跨分布式数据源的隐私保护ASR训练，但当前尚无针对大规模SpeechLLM的联邦训练落地研究，高维参数带来的梯度通信开销、分布式节点算力约束是核心痛点。
### 方法关键点
针对SpeechLLM架构特性设计通信高效的联邦优化策略，适配高维参数空间、降低梯度传输成本、兼容分布式节点算力约束；同时开展不同语音编码器架构的消融实验，探索联邦框架下的最优模型配置。
### 关键结果
在英语、意大利语单语种ASR任务上，对比中心化训练基线，在不同声学条件、说话风格下均保持效果稳定，词错率具备竞争力，同时显著降低通信成本，为多语种场景下SpeechLLM的联邦部署提供了可行基础。
