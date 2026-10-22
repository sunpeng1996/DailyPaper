---
title: Qwen-Audio-3.1-ASR Technical Report
title_zh: Qwen-Audio-3.1-ASR 技术报告
authors:
- Chuanmeng Bian
- Daren Chen
- Peixin Chen
- Zhigao Chen
- Chong Deng
- Zhiyun Fan
- Zhifu Gao
- Bo Gong
- Qing Gu
- Jiajun He
affiliations:
- Alibaba Token Foundry, Alibaba Group
arxiv_id: '2610.28711'
url: https://arxiv.org/abs/2610.28711
pdf_url: https://arxiv.org/pdf/2610.28711
published: '2026-10-19'
collected: '2026-10-22'
category: Multimodal
direction: 多模态大模型 · 音频理解与语音识别
tags:
- ASR
- Speech Recognition
- Speaker Diarization
- Audio Understanding
- Multimodal LLM
one_liner: 基于Qwen-Audio-3.0迭代的多语言音频大模型，提升识别精度，新增说话人分轨转写与通用音频理解能力
practical_value: '- 可直接复用其16种中文方言、30种语言的ASR能力，落地电商直播语音转写、语音搜索Query识别场景，覆盖下沉市场方言用户需求

  - 其分层热词定制、上下文感知转写能力可直接集成到语音交互Agent，优化电商客服语音对话转写、商品名/品牌名识别准确率

  - 说话人分轨+时间戳输出能力可用于直播内容理解、用户语音反馈分析，抽取结构化的主播讲解、用户提问内容用于标签生成和推荐召回'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有音频大模型难以兼顾多语言方言识别精度、复杂场景下的说话人分轨、通用音频理解能力，无法适配直播、语音交互等场景的差异化部署需求。
### 方法关键点
基于Qwen-Audio-3.0-ASR迭代，保留30种语言、16种中文方言支持，新增三类核心能力：1）指令控制能力：历史上下文感知、分层热词定制、原生转写润色；2）说话人分轨ASR：输出结构化的说话人标签、时间戳、识别文本，支持跨轮标签一致性、重叠语音识别；3）通用音频理解：覆盖音频/语音/音乐字幕生成、时间定位、声音事件检测、音频问答；同时提供异步、低延迟流式、交互输入、非流式等多部署变体。
### 关键结果
- 通用音频理解任务相对上一代误差降低32.9%
- 说话人分轨ASR最低平均cpWER达12.93%
- MMAU得分81.60、MMSU得分82.24，性能超过Gemini-3.1-Pro等基线
