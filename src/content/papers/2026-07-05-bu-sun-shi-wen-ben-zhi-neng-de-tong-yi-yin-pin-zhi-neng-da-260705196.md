---
title: Unified Audio Intelligence Without Regressing on Text Intelligence
title_zh: 不损失文本智能的统一音频智能大模型
authors:
- Zhifeng Kong
- Sang-gil Lee
- Jaehyeon Kim
- Boxin Wang
- Zihan Liu
- Sungwon Kim
- Yang Chen
- Arushi Goel
- Rajarshi Roy
- Wenliang Dai
arxiv_id: '2607.05196'
url: https://arxiv.org/abs/2607.05196
pdf_url: https://arxiv.org/pdf/2607.05196
published: '2026-07-05'
collected: '2026-07-08'
category: Multimodal
direction: 多模态大模型 · 音文统一建模
tags:
- Multimodal-LLM
- MoE
- Unified-Model
- Audio-Text-Fusion
- Speech-Processing
one_liner: 基于MoE文本基座构建统一音文LLM，音文能力均达SOTA且文本能力几乎无退化
practical_value: '- 多模态LLM增量改造可复用该范式：将新模态编码投影到文本嵌入空间，统一token处理逻辑，兼容现有LLM训推基建，大幅降低多模态落地成本

  - 多模态对齐后追加纯文本RL和蒸馏步骤，可有效降低新增模态对原有文本能力的侵蚀，适合需要保留基座Agent、推理能力的多模态场景

  - 统一跨模态生成架构可直接复用在电商语音导购、音频内容推荐、语音搜索等场景，无需维护多套独立模态模型'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有音频LLM大多会牺牲基座原有文本推理、Agent等核心能力，无法满足通用场景对多模态和文本能力的双重需求，且架构普遍难以兼容现有LLM基建。
### 方法关键点
1. 基于Nemotron 30B MoE文本基座，采用单Transformer decoder统一架构：音频输入编码后投影到文本嵌入空间，生成阶段统一处理文本token和量化音频输出token；
2. 训练数据包含157.4B音频token、320.5B文本token，采用「多阶段有监督训练+纯文本Cascade RL+多域on-policy蒸馏」的训练流程。
### 关键结果
音频理解、语音识别翻译、TTS、音频生成、语音到语音生成任务均达SOTA，基座原有的推理、对齐、长上下文、Agent能力仅出现边际退化甚至无退化，已开放模型权重。
