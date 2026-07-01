---
title: 'One Model, Many Latencies: Universal Speech Enhancement for Diverse Real-Time
  Applications'
title_zh: 适配多延迟约束的通用实时语音增强单模型框架
authors:
- Szu-Wei Fu
- Rong Chao
- Xuesong Yang
- Sung-Feng Huang
- Ante Jukić
- Yu Tsao
- Yu-Chiang Frank Wang
affiliations:
- NVIDIA
- Academia Sinica
arxiv_id: '2606.25621'
url: https://arxiv.org/abs/2606.25621
pdf_url: https://arxiv.org/pdf/2606.25621
published: '2026-06-23'
collected: '2026-07-01'
category: Other
direction: 实时语音处理 · 多延迟适配统一建模
tags:
- Speech Enhancement
- Real-time Inference
- Latency Control
- Early Exit
- Unified Modeling
one_liner: 提出单模型支持灵活调整算法与计算延迟，适配不同实时语音场景无需单独重训
practical_value: '- 单模型适配多延迟约束的架构思路可直接迁移到生成式推荐/LLM在线服务场景，用同一套权重覆盖端侧、云侧不同算力/RT SLA要求，大幅降低多版本模型的训练维护成本

  - 两阶段共享转多解码器的训练策略可复用在带多出口/多配置的模型训练流程中，有效缩小灵活配置模型与专用配置模型的性能差距

  - 并行卷积层适配不同上下文窗口padding的设计，可借鉴到用户行为序列建模任务，支持灵活调整序列长度而不损失建模效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
不同实时语音应用对延迟预算的要求差异显著，传统方案需要为每个场景单独训练专属增强模型，训练、部署维护成本极高，现有通用语音增强模型的非因果架构也无法适配实时场景要求。
### 方法关键点
1. 算法延迟通过可配置look-ahead帧数灵活调整，引入对应不同look-ahead设置的并行卷积层，解决不同padding配置带来的学习效率低下问题
2. 计算延迟通过early-exit机制控制，支持在不同网络深度完成推理，适配不同算力约束
3. 采用两阶段训练策略，先训练共享解码器，再过渡到多解码器结构，缩小灵活通用模型与单场景专用模型的性能gap
### 结果
单个模型可直接部署在不同延迟预算的场景下，无需针对每个场景单独重训，模型权重已开源至Hugging Face。
