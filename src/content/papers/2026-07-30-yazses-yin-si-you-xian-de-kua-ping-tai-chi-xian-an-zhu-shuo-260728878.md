---
title: 'YazSes: An Offline, Privacy-First, Cross-Platform Hold-to-Talk Voice-Dictation
  System'
title_zh: YazSes：隐私优先的跨平台离线按住说话语音听写系统
authors:
- Mohsen Seyedkazemi Ardebili
affiliations:
- NovaFabric
arxiv_id: '2607.28878'
url: https://arxiv.org/abs/2607.28878
pdf_url: https://arxiv.org/pdf/2607.28878
published: '2026-07-30'
collected: '2026-08-04'
category: Other
direction: 离线语音听写 · 端侧隐私计算
tags:
- On-device AI
- Privacy-Preserving
- Speech Recognition
- Faster-Whisper
- Cross-platform
- Open Source
one_liner: 开源全端运行的跨平台离线语音听写系统，保障数据隐私，CPU推理速度超实时
practical_value: '- 端侧语音交互场景可复用其int8量化Faster-Whisper CPU推理方案，无GPU即可实现超实时语音转写，降低算力成本

  - 隐私敏感的C端语音交互功能可参考全链路数据不出端、语料本地加密的设计，满足等保、数据合规要求

  - 语音指令识别模块可复用正则+小语言模型路由的混合架构，兼顾识别准确率和推理延迟，避免大模型冗余开销'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
云端语音听写准确率高但需上传用户语音，存在隐私泄露风险，现有端侧方案要么平台绑定，要么需要复杂配置，无法即插即用，无法适配隐私敏感场景、离线/物理隔离环境需求。

### 方法关键点
基于int8量化Faster-Whisper实现本地语音转写，通过协议化平台抽象实现Linux/macOS/Windows三端适配；采用正则命令语法+可选小语言模型路由映射语音到编辑器、终端操作指令；全链路语音数据不出端，仅按住时录音无持续监听，无遥测数据上报，个人语料本地加密存储。

### 关键结果数字
LibriSpeech test-clean测试集上，tiny.en模型WER 4.82%，small.en模型WER 2.59%，small.en实时因子0.52，无GPU的普通CPU即可超实时解码；命令语法动作准确率100%，普通听写场景误报率0%，单调用耗时0.021ms，非解码链路开销仅0.289ms。
